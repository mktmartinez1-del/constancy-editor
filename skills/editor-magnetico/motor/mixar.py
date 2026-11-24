#!/usr/bin/env python3
"""Mixa voz + música (opcional) + efeitos → <projeto>/assets/audio/mix.wav, -14 LUFS.

Uso:  python3 mixar.py <pasta-do-projeto> [--musica arquivo|nenhuma] [--inicio-musica 0] [--volume-musica 1.0] [--fim 35.2]

Efeitos: <projeto>/audio/cues.json  =  [{"t": 1.2, "som": "pop", "vol": 0.3}, ...]
  "som" é um apelido (lista em SONS abaixo) ou um caminho dentro de assets/sfx (ex.: "whoosh/fs-264777-swoosh.ogg").
Música: normalizada em -26 LUFS antes de abaixar sob a voz (fica ~10 dB abaixo da fala). Repete se for curta.
"""
import json, os, subprocess, sys

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SFX = os.path.join(SKILL, "assets", "sfx")
SONS = {   # sons curtos e secos; nada de "braaam" de trailer
    "whoosh": "whoosh/fs-264777-swoosh.ogg", "whoosh-rapido": "whoosh/fs-683101-quick-woosh.ogg",
    "swipe": "transition/fs-702773-swipe-wav.ogg", "pop": "pop/fs-824189-pop-in-sfx.ogg", "plop": "pop/fs-447910-plop.ogg",
    "impacto": "impact/kenney-impact-impactpunch-heavy-000.ogg", "impacto-suave": "impact/kenney-impact-impactsoft-heavy-000.ogg",
    "batida": "impact/fs-222517-dramatic-hit.ogg", "ding": "ding/fs-349504-triangle-open-04.ogg",
    "notificacao": "ding/fs-571513-soft-notifications-bell-ding-d.ogg", "confirmar": "ding/kenney-interface-confirmation-001.ogg",
    "tick": "tick/fs528561.ogg", "clique": "click/kenney-interface-click-001.ogg", "digitar": "typing/fs-416777-digital-typing-wav.ogg",
    "revelar": "typing/fs-511418-data-reveal-sound.ogg", "subida": "riser/fs-685256-riser-sound-effect-short-wav.ogg",
    "blip": "ui-blip/kenney-digital-twotone1.ogg", "glitch": "glitch/kenney-interface-glitch-002.ogg",
}

def arg(nome, padrao):
    a = sys.argv
    return a[a.index(nome) + 1] if nome in a else padrao

def dur(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(1)
    pasta = sys.argv[1]
    voz = os.path.join(pasta, "assets", "audio", "voz.wav")
    DUR = float(arg("--fim", 0)) or dur(voz)
    musica = arg("--musica", "nenhuma")
    ini = float(arg("--inicio-musica", 0)); vol = float(arg("--volume-musica", 1.0))
    cues_f = os.path.join(pasta, "audio", "cues.json")
    cues = json.load(open(cues_f)) if os.path.exists(cues_f) else []
    ins = ["-i", voz]
    fc = [f"[0:a]aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur={DUR},asplit=2[voz][sc]"]
    mix = ["[voz]"]
    if musica != "nenhuma":
        md = DUR - ini
        ins += ["-stream_loop", "-1", "-i", os.path.expanduser(musica)]
        fc.append(f"[1:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{md},asetpts=N/SR/TB,afade=t=in:d=1.2,afade=t=out:st={max(md - 2.5, 0)}:d=2.5,"
                  f"loudnorm=I=-26:TP=-3,volume={vol},adelay={int(ini * 1000)}|{int(ini * 1000)},apad=whole_dur={DUR}[m0]")
        fc.append("[m0][sc]sidechaincompress=threshold=0.025:ratio=6:attack=25:release=400[mus]")
        mix.append("[mus]")
    else:
        fc.append("[sc]anullsink")
    base = len(ins) // 2 if "-stream_loop" not in ins else 2
    n_in = 1 + (1 if musica != "nenhuma" else 0)
    ok = []
    for c in cues:
        f = os.path.join(SFX, SONS.get(c["som"], c["som"]))
        if not os.path.exists(f): print("  aviso: som não encontrado:", c["som"]); continue
        ins += ["-i", f]; j = n_in + len(ok)
        t = max(0, float(c["t"]))
        fc.append(f"[{j}:a]aresample=48000,aformat=channel_layouts=stereo,volume={c.get('vol', 0.3)},adelay={int(t * 1000)}|{int(t * 1000)}[s{len(ok)}]")
        ok.append(c)
    if ok:
        fc.append("".join(f"[s{k}]" for k in range(len(ok))) + f"amix=inputs={len(ok)}:normalize=0,apad=whole_dur={DUR}[sfx]")
        mix.append("[sfx]")
    fc.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0,atrim=0:{DUR},loudnorm=I=-13.6:TP=-1.0:LRA=11,alimiter=limit=0.89:level=false[out]")
    out = os.path.join(pasta, "assets", "audio", "mix.wav")
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *ins, "-filter_complex", ";".join(fc), "-map", "[out]", "-ar", "48000", out], check=True)
    print(f"ok: mix.wav {DUR:.2f}s · música: {os.path.basename(musica)} · {len(ok)} efeitos")

if __name__ == "__main__":
    main()
