#!/usr/bin/env python3
"""Confere, renderiza e entrega.

Uso:
  python3 renderizar.py <pasta-do-projeto> checar                 # erros e avisos do HyperFrames, resumidos
  python3 renderizar.py <pasta-do-projeto> quadros 3.5,12,20.2    # PNGs para revisar (imprime o caminho da folha de contato)
  python3 renderizar.py <pasta-do-projeto> final <titulo-curto>   # MP4 em ~/Constancy-Videos/exportacao + legenda da publicação
"""
import datetime, glob, json, os, re, subprocess, sys

HF = ["npx", "--yes", "hyperframes@0.9.81"]
SAIDA = os.environ.get("CONSTANCY_SAIDA") or os.path.expanduser("~/Constancy-Videos/exportacao")

def checar(p):
    r = subprocess.run(HF + ["check", "--json"], cwd=p, capture_output=True, text=True)
    try:
        d = json.loads(r.stdout[r.stdout.index("{"):])
    except Exception:
        print(r.stdout[-3000:], r.stderr[-2000:]); return 1
    erros = 0
    for k, v in d.items():
        if isinstance(v, dict) and "findings" in v:
            for f in v["findings"]:
                if f.get("severity") in ("error", "warning"):
                    erros += f["severity"] == "error"
                    print(f"[{f['severity']}] {k}/{f.get('code')} t={f.get('time')} {f.get('message', '')[:220]}")
    print("ERROS:", erros)
    return erros

def quadros(p, tempos):
    p = os.path.abspath(p); out = os.path.join(p, ".revisao")
    subprocess.run(HF + ["snapshot", "--at", tempos, "-o", out, "--no-end"], cwd=p, capture_output=True, text=True)
    for f in sorted(glob.glob(os.path.join(out, "contact-sheet*.jpg"))): print(os.path.abspath(f))

def final(p, titulo):
    os.makedirs(SAIDA, exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", titulo.lower()).strip("-")[:40] or "video"
    hoje = datetime.date.today().isoformat()
    v = 1
    while os.path.exists(os.path.join(SAIDA, f"{hoje}_{slug}_v{v}.mp4")): v += 1
    dst = os.path.join(SAIDA, f"{hoje}_{slug}_v{v}.mp4")
    r = subprocess.run(HF + ["render", "-o", dst, "--sdr", "--quality", "delivery"], cwd=p)
    if r.returncode != 0 or not os.path.exists(dst): raise SystemExit("A renderização falhou. Rode 'checar' e corrija os erros.")
    lu = subprocess.run(["ffmpeg", "-hide_banner", "-i", dst, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    i = re.findall(r"I:\s+(-?[0-9.]+) LUFS", lu); pk = re.findall(r"Peak:\s+(-?[0-9.]+) dBFS", lu)
    leg = os.path.join(p, "legenda_publicacao.txt")
    if os.path.exists(leg):
        open(dst[:-4] + "_legenda.txt", "w").write(open(leg).read())
    print(f"ok: {dst}\n   volume {i[-1] if i else '?'} LUFS · pico {pk[-1] if pk else '?'} dBFS")

if __name__ == "__main__":
    if len(sys.argv) < 3: print(__doc__); sys.exit(1)
    p, cmd = sys.argv[1], sys.argv[2]
    if cmd == "checar": sys.exit(1 if checar(p) else 0)
    if cmd == "quadros": quadros(p, sys.argv[3])
    if cmd == "final": final(p, " ".join(sys.argv[3:]) or "video")
