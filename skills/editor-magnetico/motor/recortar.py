#!/usr/bin/env python3
"""Recorta a pessoa (remove o fundo) num trecho do vídeo final, para cenas do tipo "r".

Uso:  python3 recortar.py <pasta-do-projeto> <id-da-cena> <início> <fim>
Gera <projeto>/assets/video/recorte_<id>.webm (com transparência), alinhado ao início da cena.
Leva ~2–3 s por segundo de vídeo no Mac com Apple Silicon (rode em segundo plano se o trecho for longo).
"""
import os, subprocess, sys

HF = ["npx", "--yes", "hyperframes@0.9.81"]

def main():
    if len(sys.argv) < 5: print(__doc__); sys.exit(1)
    p, cid, a, b = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
    tmp = os.path.join(p, "assets", "video", f".trecho_{cid}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-t", str(b - a), "-i", os.path.join(p, "assets", "video", "fala.mp4"),
                    "-an", "-c:v", "libx264", "-crf", "14", "-preset", "fast", tmp], check=True)
    out = os.path.join(p, "assets", "video", f"recorte_{cid}.webm")
    r = subprocess.run(HF + ["remove-background", tmp, "-o", out, "--quality", "best"], capture_output=True, text=True)
    os.remove(tmp)
    if r.returncode != 0 or not os.path.exists(out):
        print(r.stdout[-1500:], r.stderr[-1500:]); raise SystemExit("A remoção de fundo falhou.")
    print(f"ok: {out} ({b - a:.1f}s)")

if __name__ == "__main__":
    main()
