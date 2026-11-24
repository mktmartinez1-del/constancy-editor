#!/usr/bin/env python3
"""Monta o vídeo-base (assets/video/fala.mp4 + assets/audio/voz.wav + assets/transcript.json) a partir de um EDL.

Uso:  python3 montar.py <pasta-do-projeto> [edl.json]      (padrão: <projeto>/edl.json)

edl.json:
{
  "segmentos": [                                   # em ordem; tempos em segundos na mídia de origem
    {"midia": "principal", "de": 0.0, "ate": 12.4},
    {"midia": "fonte", "congelar": 3.0, "dur": 1.5},     # quadro parado (pausa do React)
    {"midia": "b", "de": 2.0, "ate": 6.0, "mudo": true}   # usa a imagem e silencia o som deste trecho
  ],
  "cortar_pausas": 0.35,          # opcional: se "segmentos" faltar, corta silêncios > X s da mídia "principal"
  "remover": [[31.2, 33.0]],      # opcional, junto com cortar_pausas: trechos (tempo da principal) para tirar (erros, repetições)
  "locucao": "locucao"            # opcional: troca o áudio inteiro por essa mídia (Storytelling narrado)
}
Sem edl.json: usa a mídia "principal" inteira, sem cortes (vídeo já editado).
"""
import json, os, subprocess, sys

def carregar_palavras(pasta, info):
    if not info.get("transcricao"): return []
    w = json.load(open(os.path.join(pasta, info["transcricao"])))
    return w.get("words", w) if isinstance(w, dict) else w

def segs_por_pausas(words, dur, pausa, remover):
    if not words: return [{"midia": "principal", "de": 0.0, "ate": dur}]
    segs, a, b = [], max(0.0, words[0]["start"] - 0.12), words[0]["end"]
    for w in words[1:]:
        if w["start"] - b > pausa:
            segs.append((a, b + 0.12)); a = max(b + 0.12, w["start"] - 0.12)
        b = w["end"]
    segs.append((a, min(dur, b + 0.25)))
    for r0, r1 in remover:   # tira trechos marcados
        novo = []
        for s0, s1 in segs:
            if r1 <= s0 or r0 >= s1: novo.append((s0, s1)); continue
            if s0 < r0: novo.append((s0, r0))
            if r1 < s1: novo.append((r1, s1))
        segs = novo
    return [{"midia": "principal", "de": round(s0, 3), "ate": round(s1, 3)} for s0, s1 in segs if s1 - s0 > 0.15]

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(1)
    pasta = sys.argv[1]
    edl_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(pasta, "edl.json")
    midias = json.load(open(os.path.join(pasta, "assets", "midias.json")))
    edl = json.load(open(edl_path)) if os.path.exists(edl_path) else {}
    if "principal" not in midias and not edl.get("segmentos"):
        raise SystemExit("Falta a mídia 'principal' (ou um edl.json com segmentos).")
    segs = edl.get("segmentos")
    if not segs:
        p = midias["principal"]
        if edl.get("cortar_pausas"):
            segs = segs_por_pausas(carregar_palavras(pasta, p), p["duracao"], edl["cortar_pausas"], edl.get("remover", []))
        else:
            segs = [{"midia": "principal", "de": 0.0, "ate": p["duracao"]}]
    ins, fc, words_out, t_out = [], [], [], 0.0
    idx = {}
    def entrada(papel):
        if papel not in idx:
            m = midias[papel]
            if not m.get("proxy"): raise SystemExit(f"A mídia '{papel}' não tem vídeo.")
            idx[papel] = len(ins) // 2
            ins.extend(["-i", os.path.join(pasta, m["proxy"])])
        return idx[papel]
    def quadro(s):
        if s.get("enquadrar") == "conter":   # vídeo horizontal inteiro, com fundo desfocado
            return "split[c1][c2];[c1]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:3[bgx];[c2]scale=1080:-2[fgx];[bgx][fgx]overlay=0:(H-h)/2"
        return "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920"
    for j, s in enumerate(segs):
        m = midias[s["midia"]]; k = entrada(s["midia"])
        if "congelar" in s:
            d = float(s["dur"]); t0 = float(s["congelar"])
            fc.append(f"[{k}:v]trim=start={t0}:duration=0.04,setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={d},trim=duration={d},setpts=PTS-STARTPTS,{quadro(s)},fps=30,format=yuv420p[v{j}]")
            fc.append(f"anullsrc=r=48000:cl=stereo,atrim=duration={d}[a{j}]")
        else:
            a0, a1 = float(s["de"]), float(s["ate"]); d = a1 - a0
            fc.append(f"[{k}:v]trim=start={a0}:end={a1},setpts=PTS-STARTPTS,{quadro(s)},fps=30,format=yuv420p[v{j}]")
            if m.get("tem_audio") and not s.get("mudo"):
                fc.append(f"[{k}:a]atrim=start={a0}:end={a1},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo[a{j}]")
            else:
                fc.append(f"anullsrc=r=48000:cl=stereo,atrim=duration={d}[a{j}]")
            if not s.get("mudo"):
                for w in carregar_palavras(pasta, m):
                    if w["start"] >= a0 - 0.02 and w["end"] <= a1 + 0.05:
                        words_out.append({**w, "start": round(w["start"] - a0 + t_out, 3), "end": round(min(w["end"], a1) - a0 + t_out, 3)})
        t_out += d
    n = len(segs)
    fc.append("".join(f"[v{j}][a{j}]" for j in range(n)) + f"concat=n={n}:v=1:a=1[v][a]")
    dst_v = os.path.join(pasta, "assets", "video", "fala.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-c:a", "aac", "-b:a", "192k", dst_v], check=True)
    voz = os.path.join(pasta, "assets", "audio", "voz.wav")
    if edl.get("locucao"):
        loc = midias[edl["locucao"]]
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(pasta, loc["audio"]), "-ac", "2", "-ar", "48000", voz], check=True)
        words_out = carregar_palavras(pasta, loc)
        t_out = max(t_out, loc["duracao"])
    else:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", dst_v, "-vn", "-ac", "2", "-ar", "48000", voz], check=True)
    json.dump({"words": words_out}, open(os.path.join(pasta, "assets", "transcript.json"), "w"), ensure_ascii=False)
    real = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", dst_v], capture_output=True, text=True).stdout)
    json.dump({"duracao": real, "segmentos": segs, "duracao_audio": t_out}, open(os.path.join(pasta, "assets", "fala.json"), "w"), indent=2)
    print(f"ok: fala.mp4 {real:.2f}s · {n} segmentos · {len(words_out)} palavras na linha do tempo final")
    linha, st = [], None
    for w in words_out:
        if st is None: st = w["start"]
        linha.append(w["text"])
        if w["text"].endswith((".", "?", "!")) or len(linha) >= 16:
            print(f"    {st:7.2f}–{w['end']:7.2f}  {' '.join(linha)}"); linha, st = [], None
    if linha: print(f"    {st:7.2f}  {' '.join(linha)}")

if __name__ == "__main__":
    main()
