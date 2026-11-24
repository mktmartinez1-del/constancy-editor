#!/usr/bin/env python3
# Amostra do estilo 15 · Avatar Dourado
import json, sys
sys.path.insert(0, "%MOTOR%")   # caminho da pasta motor/ (o roteiro.py do projeto já vem com ele)
from cenas_base import tema, escrever, palavras, dur_video, recorte

T = tema("15"); W = palavras(); VDUR = dur_video(); FIM = 16.4
CENAS = {"c1": (0.0, 4.7, "f"), "r1": (4.76, 10.0, "r"), "c3": (10.07, 14.4, "m"), "c4": (14.47, 16.3, "p")}
G = """
    #root .gd { color: var(--ac2); text-shadow: 0 0 30px rgba(232,176,74,.75), 0 0 80px rgba(232,176,74,.35); }
    #root .gp { position: absolute; padding: 12px 26px; border-radius: 999px; background: rgba(20,16,8,.75); border: 2px solid var(--ac); color: #fff; font-size: 34px; font-weight: 600; box-shadow: 0 0 24px rgba(232,176,74,.35); white-space: nowrap; }
"""
S = {}
S["c1"] = dict(css=G + """
    #c1-s { top: 960px; font-size: 52px; text-transform: none; font-weight: 600; color: #fff; text-shadow: 0 4px 20px rgba(0,0,0,.6); }
    #c1-t { top: 1020px; font-size: 150px; letter-spacing: -.05em; }
""", body="""
    <div id="c1-s" class="t">cansado de</div>
    <div id="c1-t" class="t gd">TENTAR</div>
""", js="""
    IN("#c1-s", 1.3);
    IN("#c1-t", 2.04, { scale: 1.5 });
    tl.to("#c1-t", { scale: 1.12, duration: .12, yoyo: true, repeat: 1 }, 2.52);
    tl.to("#c1-t", { scale: 1.2, duration: .12, yoyo: true, repeat: 1 }, 2.92);
    OUT(["#c1-s", "#c1-t"], 4.4);
""")
S["r1"] = dict(css=G + """
    #r1-bg { position: absolute; inset: 0; background: radial-gradient(55% 35% at 50% 45%, #3a2a0e, var(--bg) 70%); }
    #r1-st { position: absolute; left: 0; right: 0; top: 0; bottom: 0; perspective: 1600px; }
    #r1-card { position: absolute; left: 190px; top: 520px; width: 700px; height: 720px; border-radius: 40px; overflow: hidden; border: 4px solid var(--ac); box-shadow: 0 0 60px rgba(232,176,74,.45); background: radial-gradient(80% 60% at 50% 30%, #2a2010, #0d0b06); }
    #r1-t { top: 300px; font-size: 64px; text-transform: none; font-weight: 700; }
    #r1-t .it { color: var(--ac2); font-size: 84px; }
    #r1-orb { position: absolute; left: 540px; top: 900px; width: 0; height: 0; }
""", body="""
    <div id="r1-bg"></div>
    <div id="r1-t" class="t luz">eu também <span class="it">passei</span></div>
    <div id="r1-st"><div id="r1-card">""" + recorte("r1", 5.24, escala=0.62, x=-190, y=-957) + """</div></div>
    <div id="r1-orb">
      <div id="r1-o1" class="gp" style="left:-500px;top:-380px">postar</div>
      <div id="r1-o2" class="gp" style="left:330px;top:-200px">gravar</div>
      <div id="r1-o3" class="gp" style="left:-520px;top:140px">editar</div>
      <div id="r1-o4" class="gp" style="left:250px;top:330px">desistir</div>
    </div>
""", js="""
    tl.fromTo("#r1-card", { opacity: 0, rotationY: 40, scale: .8 }, { opacity: 1, rotationY: 16, scale: 1, duration: .7, ease: "expo.out" }, 0);
    tl.to("#r1-card", { rotationY: -10, duration: 5, ease: "sine.inOut" }, .7);
    IN("#r1-t", 1.9);
    tl.fromTo("#r1-orb .gp", { opacity: 0, scale: .3 }, { opacity: 1, scale: 1, duration: .45, ease: "back.out(2)", stagger: .25 }, 3.39);
    tl.fromTo("#r1-orb", { rotation: -6 }, { rotation: 6, duration: 2, ease: "sine.inOut" }, 3.3);
""")
S["c3"] = dict(css=G + """
    #c3-bg { position: absolute; inset: 0; background: radial-gradient(50% 35% at 50% 45%, #3a2a0e, var(--bg) 70%); }
    #c3-i { position: absolute; left: 290px; top: 560px; width: 500px; height: 500px; object-fit: contain; filter: drop-shadow(0 0 60px rgba(232,176,74,.55)); }
    #c3-a { top: 330px; font-size: 54px; text-transform: none; font-weight: 600; color: #fff; }
    #c3-b { top: 1120px; font-size: 120px; letter-spacing: -.05em; }
""", body="""
    <div id="c3-bg"></div>
    <div id="c3-a" class="t">eu fazia pra muita gente</div>
    <img id="c3-i" src="assets/img/trophy-gold.png" alt="" />
    <div id="c3-b" class="t gd">GENTE GRANDE</div>
""", js="""
    IN("#c3-a", 0.5);
    tl.fromTo("#c3-i", { opacity: 0, scale: .4, rotationY: -60, y: 80 }, { opacity: 1, scale: 1, rotationY: 0, y: 0, duration: .8, ease: "expo.out" }, 1.36);
    tl.to("#c3-i", { y: -20, rotation: 4, duration: 3, ease: "sine.inOut" }, 2.2);
    IN("#c3-b", 2.56, { scale: 1.4 });
""")
S["c4"] = dict(css=G + """
    #c4-a { top: 120px; font-size: 130px; letter-spacing: -.05em; }
    #c4-a .it { color: var(--ac2); font-size: 150px; }
""", body="""    <div class="z">
      <div id="c4-a" class="t gd">e pra <span class="it">mim?</span></div>
    </div>""", js="""
    IN("#c4-a", 0.9, { scale: 1.4 });
""")
CUES = [{"t": 2.04, "som": "impacto-suave", "vol": .35}, {"t": 2.52, "som": "impacto-suave", "vol": .3}, {"t": 2.92, "som": "impacto", "vol": .35},
        {"t": 4.76, "som": "whoosh", "vol": .3}, {"t": 6.66, "som": "pop", "vol": .25}, {"t": 8.15, "som": "pop", "vol": .25}, {"t": 8.4, "som": "pop", "vol": .25},
        {"t": 8.65, "som": "pop", "vol": .25}, {"t": 8.9, "som": "pop", "vol": .25}, {"t": 10.07, "som": "whoosh", "vol": .3}, {"t": 11.43, "som": "subida", "vol": .25},
        {"t": 12.63, "som": "batida", "vol": .35}, {"t": 14.47, "som": "whoosh-rapido", "vol": .25}, {"t": 15.37, "som": "ding", "vol": .3}]
escrever(CENAS, S, T, W, FIM, VDUR, punch=[2.04, 2.92], correcoes={})
json.dump(CUES, open("audio/cues.json", "w"))
