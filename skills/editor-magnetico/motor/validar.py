#!/usr/bin/env python3
"""Confere se o projeto tem o que o formato precisa antes de editar/renderizar.

Uso:  python3 validar.py <pasta-do-projeto>
Lê <projeto>/plano.json  ({"formato": "03", "estilo": "11", "musica": "...", "cta": "...", ...})
e <projeto>/assets/midias.json. Sai com código 1 e diz o arquivo que falta, pelo nome do papel.
"""
import json, os, sys

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    p = sys.argv[1]
    plano = json.load(open(os.path.join(p, "plano.json")))
    req = json.load(open(os.path.join(SKILL, "formatos", "requisitos.json")))[str(plano["formato"]).zfill(2)]
    mj = os.path.join(p, "assets", "midias.json")
    midias = json.load(open(mj)) if os.path.exists(mj) else {}
    falta = [r for r in req["obrigatorios"] if r not in midias]
    for k, m in midias.items():
        if m.get("proxy") and not os.path.exists(os.path.join(p, m["proxy"])): falta.append(f"{k} (arquivo convertido sumiu: rode o preparar.py de novo)")
    mus = plano.get("musica")
    if mus and mus != "nenhuma" and not os.path.exists(os.path.expanduser(mus)): falta.append(f"música ({mus})")
    if plano["formato"] in ("05", 5) and not os.path.exists(os.path.join(p, "legenda_publicacao.txt")):
        print("aviso: Trend com texto precisa de legenda_publicacao.txt (a legenda é parte do formato).")
    print(f"Formato {req['nome']} · mídias: {', '.join(midias) or 'nenhuma'}")
    if falta:
        print("FALTA:", "; ".join(falta)); sys.exit(1)
    print("ok: tudo que o formato exige está aqui")

if __name__ == "__main__":
    main()
