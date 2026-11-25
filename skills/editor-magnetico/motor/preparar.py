#!/usr/bin/env python3
"""Cria (ou atualiza) um projeto e prepara as mídias.

Uso:
  python3 preparar.py <pasta-do-projeto> papel=/caminho/arquivo.mov [papel2=/outro.mp4 ...] [--estilo 11] [--sem-transcricao papel]

Para cada mídia: converte para SDR 1080p 30 fps (iPhone HDR incluído), extrai o áudio,
transcreve a fala (palavra a palavra) e detecta cortes de cena. Grava assets/midias.json
e imprime a transcrição com tempos, para o Claude planejar a edição.
Papéis comuns: principal, fonte (React), a / b (Comparativo), locucao, take1, take2, apoio1...
"""
import json, os, re, shutil, subprocess, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(AQUI)
HF = ["npx", "--yes", "hyperframes@0.9.81"]

def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)

def probe(f):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration:stream=codec_type,width,height,color_transfer,r_frame_rate:stream_side_data=rotation",
                          "-of", "json", f], capture_output=True, text=True, check=True).stdout
    d = json.loads(out)
    v = next((s for s in d["streams"] if s["codec_type"] == "video"), None)
    a = any(s["codec_type"] == "audio" for s in d["streams"])
    info = {"duracao": float(d["format"]["duration"]), "tem_audio": a, "tem_video": v is not None}
    if v:
        rot = 0
        for sd in v.get("side_data_list", []) or []:
            if "rotation" in sd:
                rot = int(float(sd["rotation"]))
        w, h = v["width"], v["height"]
        if abs(rot) in (90, 270): w, h = h, w
        info.update(largura=w, altura=h, hdr=v.get("color_transfer") in ("arib-std-b67", "smpte2084"), fps=v.get("r_frame_rate"))
    return info

def faixa_audio(f):
    """Primeira faixa de áudio decodificável (iPhone grava áudio espacial apple_apac como faixa 1)."""
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index,codec_name",
                          "-of", "csv=p=0", f], capture_output=True, text=True).stdout.split()
    for linha in out:
        idx, cod = linha.split(",")[:2]
        if cod not in ("apple_apac", "unknown", ""): return f"0:{idx}"
    return "0:a:0"

def tem_filtro(nome):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-filters"], capture_output=True, text=True)
    return f" {nome} " in r.stdout

def proxy(src, dst, info, tmp):
    """Vídeo SDR, 30 fps, preenchendo 1080x1920 se for vertical (horizontal mantém e o Claude decide o enquadramento)."""
    vertical = info["altura"] >= info["largura"]
    esc = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" if vertical else "scale=1920:-2"
    entrada, pre = src, []
    if info.get("hdr"):
        if tem_filtro("zscale"):
            pre = ["zscale=t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p"]
        elif shutil.which("avconvert"):   # macOS: conversão HDR→SDR nativa da Apple
            entrada = os.path.join(tmp, "sdr.mov")
            ok = subprocess.run(["avconvert", "-s", src, "-p", "Preset1920x1080", "-o", entrada, "--replace"],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
            if not ok:   # avconvert recusa MOV regravado com áudio espacial (apac): tenta só com vídeo + áudio comum
                limpo = os.path.join(tmp, "sem_apac.mov")
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-map", "0:v:0", "-map", faixa_audio(src),
                                "-c", "copy", limpo], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                ok = os.path.exists(limpo) and subprocess.run(
                    ["avconvert", "-s", limpo, "-p", "Preset1920x1080", "-o", entrada, "--replace"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
            if not ok:
                print("  aviso: não consegui converter o HDR; as cores podem ficar um pouco lavadas.")
                entrada = src
        else:
            print("  aviso: vídeo HDR e este FFmpeg não tem zscale; as cores podem ficar lavadas.")
    vf = ",".join(pre + [esc, "fps=30", "format=yuv420p"])
    sh(["ffmpeg", "-v", "error", "-y", "-i", entrada, "-vf", vf, "-c:v", "libx264", "-crf", "16", "-preset", "fast",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", dst])

def cortes(f):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", f, "-vf", "scale=160:-2,select='gt(scene,0.32)',showinfo", "-an", "-f", "null", "-"],
                       capture_output=True, text=True)
    return [round(float(x), 2) for x in re.findall(r"pts_time:([0-9.]+)", r.stderr)]

def transcrever(f, saida, pasta):
    for eng in (["--engine", "parakeet"], ["--engine", "whisper", "--model", "large-v3", "--language", "pt"]):
        r = subprocess.run(HF + ["transcribe", f, "--json", "-d", pasta] + eng, capture_output=True, text=True)
        linhas = [l for l in r.stdout.splitlines() if l.strip().startswith("{")]
        try:
            res = json.loads(linhas[-1])
            if res.get("ok"):
                shutil.move(res["transcriptPath"], saida)
                return res.get("engine")
        except Exception:
            pass
    raise SystemExit("Não consegui transcrever. Rode o instalador de novo (ele instala o Parakeet).")

def imprimir(words, dur):
    linha, st = [], None
    for w in words:
        if st is None: st = w["start"]
        linha.append(w["text"])
        if w["text"].endswith((".", "?", "!")) or len(linha) >= 16:
            print(f"    {st:7.2f}–{w['end']:7.2f}  {' '.join(linha)}"); linha, st = [], None
    if linha: print(f"    {st:7.2f}  {' '.join(linha)}")

def projeto_novo(pasta, estilo):
    for d in ("assets/video", "assets/audio", "assets/img", "assets/ig", "assets/fonts", "assets/transcricoes", "compositions", "audio"):
        os.makedirs(os.path.join(pasta, d), exist_ok=True)
    for f in os.listdir(os.path.join(SKILL, "assets", "fonts")):
        if f.endswith(".ttf"):
            shutil.copy(os.path.join(SKILL, "assets", "fonts", f), os.path.join(pasta, "assets", "fonts", f))
    nome = os.path.basename(os.path.abspath(pasta))
    json.dump({"$schema": "https://hyperframes.heygen.com/schema/hyperframes.json", "paths": {"blocks": "compositions", "assets": "assets"},
               "media": {"autoProxy": True}, "authoringSkill": "hyperframes"}, open(os.path.join(pasta, "hyperframes.json"), "w"), indent=2)
    json.dump({"name": nome, "private": True, "type": "module"}, open(os.path.join(pasta, "package.json"), "w"), indent=2)
    json.dump({"id": nome, "name": nome}, open(os.path.join(pasta, "meta.json"), "w"))
    rot = os.path.join(pasta, "roteiro.py")
    if not os.path.exists(rot):
        s = open(os.path.join(SKILL, "modelo", "roteiro_modelo.py")).read().replace("%MOTOR%", AQUI).replace("%ESTILO%", str(estilo))
        open(rot, "w").write(s)

def main():
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(1)
    pasta = a.pop(0)
    estilo = "11"
    if "--estilo" in a:
        i = a.index("--estilo"); estilo = a[i + 1]; del a[i:i + 2]
    sem = set()
    while "--sem-transcricao" in a:
        i = a.index("--sem-transcricao"); sem.add(a[i + 1]); del a[i:i + 2]
    projeto_novo(pasta, estilo)
    mj = os.path.join(pasta, "assets", "midias.json")
    midias = json.load(open(mj)) if os.path.exists(mj) else {}
    tmp = os.path.join(pasta, ".tmp"); os.makedirs(tmp, exist_ok=True)
    for par in a:
        papel, src = par.split("=", 1)
        src = os.path.expanduser(src)
        if not os.path.exists(src): raise SystemExit(f"Arquivo não encontrado: {src}")
        info = probe(src); info["original"] = os.path.abspath(src)
        print(f"\n■ {papel}: {os.path.basename(src)} · {info['duracao']:.1f}s" + (f" · {info['largura']}x{info['altura']}{' · HDR' if info.get('hdr') else ''}" if info["tem_video"] else " · só áudio"))
        if info["tem_video"]:
            dst = os.path.join(pasta, "assets", "video", f"{papel}.mp4")
            proxy(src, dst, info, tmp); info["proxy"] = os.path.relpath(dst, pasta)
            info["cortes_de_cena"] = cortes(dst)
            if info["cortes_de_cena"]: print(f"  cortes de cena em: {info['cortes_de_cena'][:30]}")
        if info["tem_audio"]:
            wav = os.path.join(pasta, "assets", "audio", f"{papel}.wav")
            sh(["ffmpeg", "-v", "error", "-y", "-i", src, "-map", faixa_audio(src), "-vn", "-ac", "2", "-ar", "48000", wav]); info["audio"] = os.path.relpath(wav, pasta)
            if papel not in sem:
                tj = os.path.join(pasta, "assets", "transcricoes", f"{papel}.json")
                info["motor_transcricao"] = transcrever(wav, tj, pasta); info["transcricao"] = os.path.relpath(tj, pasta)
                w = json.load(open(tj)); w = w.get("words", w) if isinstance(w, dict) else w
                print(f"  transcrição ({len(w)} palavras):"); imprimir(w, info["duracao"])
        midias[papel] = info
    json.dump(midias, open(mj, "w"), indent=2, ensure_ascii=False)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"\nok → {mj}")

if __name__ == "__main__":
    main()
