#!/usr/bin/env python3
"""Roteiro de edição deste projeto (gerado pelo Constancy Editor).
O Claude edita este arquivo e roda:  python3 roteiro.py
Depois:  python3 <motor>/mixar.py .  e  python3 <motor>/renderizar.py . checar|quadros|final
"""
import json, sys
sys.path.insert(0, "%MOTOR%")   # caminho da pasta motor/ (o roteiro.py do projeto já vem com ele)
from cenas_base import tema, escrever, palavras, dur_video, perfil, recorte

T = tema("12")                  # estilo escolhido no catálogo (01–17)
W = palavras()                        # palavras da fala na linha do tempo final (depois do montar.py)
VDUR = dur_video()
FIM = round(VDUR + 1.5, 2)            # +1,5 s para o encerramento (logo/@/CTA)
INICIO = 0.0                          # React: tempo em que acaba o trecho original que não deve ser mexido

CENAS = {
    "c01": (0.0, 4.7, "f"),
    "c02": (6.47, 10.0, "p"),
    "r1": (10.07, 16.2, "r"),
}
S = {}
S["c01"] = dict(css="""
    #c01-a { top: 300px; font-size: 60px; font-style: italic; font-weight: 700; color: #fff; }
    #c01-b { top: 360px; font-size: 170px; font-style: italic; font-weight: 900; color: #ff2d3d; text-shadow: 0 8px 40px rgba(0,0,0,.4); }
""", body="""
    <div id="c01-a" class="s luz">cansado de</div>
    <div id="c01-b" class="t">tentar?</div>
""", js="""
    IN("#c01-a", 0.6, { x: -60 });
    IN("#c01-b", 1.9, { scale: 1.5 });
    OUT(["#c01-a", "#c01-b"], 4.3);
""")
S["c02"] = dict(css="""
    #c02-a { top: 40px; font-size: 60px; font-style: italic; color: var(--sub); text-transform: none; font-weight: 600; }
    #c02-b { top: 120px; font-size: 150px; font-style: italic; font-weight: 900; background: linear-gradient(180deg, var(--ac2), var(--ac)); -webkit-background-clip: text; color: transparent; }
    #root .px { position: absolute; width: 34px; height: 34px; background: var(--ac); }
""", body="""    <div class="z">
      <div id="c02-a" class="t">eu também</div>
      <div id="c02-b" class="t">passei</div>
      <div class="px" style="left:60px;top:300px"></div><div class="px" style="left:94px;top:334px;opacity:.5"></div><div class="px" style="right:80px;top:40px"></div><div class="px" style="right:46px;top:6px;opacity:.4"></div>
    </div>""", js="""
    IN("#c02-a", 0.2, { x: -60 });
    IN("#c02-b", 0.5, { scale: 1.4 });
    tl.fromTo("#c02 .px", { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.2, stagger: 0.07, ease: "steps(3)" }, 0.6);
""")
S["r1"] = dict(css="""
    #r1-bg { position: absolute; inset: 0; background: radial-gradient(70% 45% at 50% 40%, #ffffff 0%, var(--bg) 60%, var(--bg2) 100%); }
    #r1-a { top: 430px; font-size: 54px; font-style: italic; font-weight: 600; color: var(--sub); text-transform: none; }
    #r1-b { top: 490px; font-size: 250px; font-style: italic; font-weight: 900; letter-spacing: -.06em; background: linear-gradient(180deg, var(--ac2), var(--ac) 70%); -webkit-background-clip: text; color: transparent; }
    #r1-c { top: 330px; font-size: 92px; font-style: italic; font-weight: 900; color: var(--ink); }
    #r1-x { position: absolute; left: 330px; right: 330px; top: 380px; height: 14px; border-radius: 7px; background: var(--ac); transform-origin: 0 50%; }
""", body="""
    <div id="r1-bg"></div>
    <div id="r1-a" class="t">pra muita</div>
    <div id="r1-b" class="t">gente</div>
    """ + recorte("r1", 6.13) + """
    <div id="r1-c" class="t">pra mim</div>
    <div id="r1-x"></div>
""", js="""
    tl.fromTo("#r1-rc", { y: 260, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "expo.out" }, 0.0);
    IN("#r1-a", 0.2);
    IN("#r1-b", 0.4, { scale: 1.3 });
    tl.to("#r1-b", { scale: 1.06, duration: 5, ease: "none" }, 0.9);
    OUT(["#r1-a", "#r1-b"], 4.2);
    IN("#r1-c", 4.5);
    RISCO("#r1-x", 5.3);
""")

# zoom rápido no rosto em palavras fortes (só vale em tela cheia)
PUNCH = [1.9]

# correções de transcrição para a legenda: {"palavra errada": "certa"}
CORRECOES = {}

# efeitos sonoros: 1 por evento visual (apelidos em mixar.py → SONS)
CUES = [
    {"t": 1.9, "som": "impacto-suave", "vol": 0.35}, {"t": 6.47, "som": "whoosh", "vol": 0.3}, {"t": 8.37, "som": "pop", "vol": 0.3},
    {"t": 12.67, "som": "pop", "vol": 0.3}, {"t": 15.5, "som": "swipe", "vol": 0.3}, {"t": 16.23, "som": "whoosh", "vol": 0.3},
    {"t": 17.43, "som": "tick", "vol": 0.3}, {"t": 20.73, "som": "impacto", "vol": 0.35}, {"t": 23.03, "som": "whoosh-rapido", "vol": 0.25},
]

escrever(CENAS, S, T, W, FIM, VDUR, punch=PUNCH, inicio_legendas=INICIO, correcoes=CORRECOES)
json.dump(CUES, open("audio/cues.json", "w"), indent=1)
