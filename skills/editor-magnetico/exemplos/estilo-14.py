#!/usr/bin/env python3
# Amostra do estilo 14 · Dark Kinetic Tipográfico
import json, sys
sys.path.insert(0, "%MOTOR%")   # caminho da pasta motor/ (o roteiro.py do projeto já vem com ele)
from cenas_base import tema, escrever, palavras, dur_video, recorte

T = tema("14"); W = palavras(); VDUR = dur_video(); FIM = 16.4
CENAS = {"c1": (0.0, 1.95, "f"), "c2": (2.0, 6.4, "m"), "c3": (6.47, 10.0, "p"), "r1": (10.07, 16.3, "r")}
K = """
    #root .ch { display: inline-block; padding: 2px 18px 6px; border-radius: 14px; background: var(--ac); color: #fff; }
    #root .ch.ro { background: var(--ac2); }
    #root .cur { display: inline-block; width: 8px; height: .9em; background: var(--ac); vertical-align: -0.1em; margin-left: 6px; }
    #root .kt { position: absolute; left: 80px; right: 160px; font-weight: 800; letter-spacing: -.04em; line-height: 1; color: #fff; }
    #root .kt small { display: block; font-size: .42em; font-weight: 600; color: var(--sub); letter-spacing: -.02em; margin-bottom: 10px; }
    #root .glow { position: absolute; border-radius: 50%; filter: blur(80px); opacity: .35; }
"""
S = {}
S["c1"] = dict(css=K + "#c1-a { top: 300px; font-size: 96px; }", body="""
    <div id="c1-a" class="kt"><small>você deve estar</small>cansado de <span class="ch">tentar</span></div>
""", js="""
    IN("#c1-a", 0.9, { x: -50 });
    tl.fromTo("#c1-a .ch", { scale: .3, opacity: 0 }, { scale: 1, opacity: 1, duration: .35, ease: "back.out(2.5)" }, 1.88);
""")
S["c2"] = dict(css=K + """
    #c2-bg { position: absolute; inset: 0; background: radial-gradient(70% 40% at 30% 40%, #1c1410, var(--bg) 70%); }
    #c2-l1 { top: 330px; font-size: 150px; }
    #c2-l2 { top: 490px; font-size: 150px; }
    #c2-l3 { top: 650px; font-size: 150px; }
    #c2-n { top: 420px; font-size: 110px; }
    #c2-x { position: absolute; left: 80px; width: 560px; top: 480px; height: 14px; border-radius: 7px; background: #e8361c; transform-origin: 0 50%; }
    #c2-d { top: 600px; font-size: 130px; }
    #c2-d .it { font-size: 150px; color: #fff; }
    #c2-v { top: 860px; font-size: 64px; color: var(--sub); }
""", body="""
    <div id="c2-bg"></div>
    <div class="glow" style="left:-100px;top:500px;width:600px;height:600px;background:var(--ac)"></div>
    <div id="c2-l1" class="kt">tentar<span class="cur"></span></div>
    <div id="c2-l2" class="kt"><span class="ch">tentar</span></div>
    <div id="c2-l3" class="kt"><span class="ch ro">tentar</span></div>
    <div id="c2-n" class="kt">não conseguir</div>
    <div id="c2-x"></div>
    <div id="c2-d" class="kt">no <span class="it">digital.</span></div>
    <div id="c2-v" class="kt">não é verdade?<span class="cur"></span></div>
""", js="""
    IN("#c2-l1", 0.04, { y: 60 });
    tl.fromTo("#c2-l1 .cur", { opacity: 1 }, { opacity: 0, duration: .01, repeat: 5, yoyo: true, repeatDelay: .2 }, 0.1);
    IN("#c2-l2", 0.52, { y: 60 });
    IN("#c2-l3", 0.92, { y: 60 });
    OUT(["#c2-l1", "#c2-l2", "#c2-l3"], 1.3);
    IN("#c2-n", 1.48, { x: -60 });
    RISCO("#c2-x", 1.9);
    IN("#c2-d", 2.2, { scale: 1.3 });
    IN("#c2-v", 2.76);
""")
S["c3"] = dict(css=K + """
    #c3-w { position: absolute; left: 60px; right: 60px; top: 10px; height: 330px; border-radius: 22px; background: #16161b; border: 1px solid rgba(255,255,255,.1); box-shadow: 0 30px 60px rgba(0,0,0,.5); overflow: hidden; }
    #c3-w .bar { height: 46px; background: #1e1e25; display: flex; gap: 10px; align-items: center; padding-left: 18px; }
    #c3-w .bar i { width: 14px; height: 14px; border-radius: 50%; background: #444; }
    #c3-w .bar i:nth-child(1) { background: #ff5f57; } #c3-w .bar i:nth-child(2) { background: #febc2e; } #c3-w .bar i:nth-child(3) { background: #28c840; }
    #c3-t { position: absolute; left: 40px; top: 90px; font-size: 64px; font-weight: 800; color: #fff; letter-spacing: -.03em; }
    #c3-p { position: absolute; left: 40px; right: 40px; top: 200px; height: 18px; border-radius: 9px; background: rgba(255,255,255,.08); }
    #c3-pf { position: absolute; left: 0; top: 0; bottom: 0; width: 100%; border-radius: 9px; background: linear-gradient(90deg, var(--ac2), var(--ac)); transform-origin: 0 50%; }
    #c3-pc { position: absolute; right: 40px; top: 240px; font-size: 40px; font-weight: 800; color: #fff; }
    #c3-q { top: 400px; font-size: 80px; text-align: center; left: 0; right: 0; }
    #c3-q .it { font-size: 96px; color: var(--ac); }
""", body="""    <div class="z">
      <div id="c3-w"><div class="bar"><i></i><i></i><i></i></div>
        <div id="c3-t">eu também <span class="ch">passei</span></div>
        <div id="c3-p"><div id="c3-pf"></div></div><div id="c3-pc">um tempo atrás</div></div>
      <div id="c3-q" class="kt">de que <span class="it">forma?</span></div>
    </div>""", js="""
    tl.fromTo("#c3-w", { opacity: 0, y: 60, rotationX: 30 }, { opacity: 1, y: 0, rotationX: 0, duration: .6, ease: "expo.out" }, 0.1);
    IN("#c3-t", 0.5, { x: -40 });
    tl.fromTo("#c3-pf", { scaleX: 0 }, { scaleX: 1, duration: 1.4, ease: "power2.inOut" }, 0.7);
    IN("#c3-pc", 1.76);
    IN("#c3-q", 2.6, { scale: 1.3 });
""")
S["r1"] = dict(css=K + """
    #r1-bg { position: absolute; inset: 0; background: radial-gradient(60% 40% at 50% 38%, #2a1a12, var(--bg) 70%); }
    #r1-a { top: 400px; font-size: 54px; color: var(--sub); text-align: center; left: 0; right: 0; font-weight: 600; }
    #r1-b { top: 470px; font-size: 210px; text-align: center; left: 0; right: 0; letter-spacing: -.07em; }
    #r1-b span { -webkit-text-stroke: 4px var(--ac); color: transparent; }
    #r1-m { top: 330px; left: 0; right: 0; text-align: center; font-size: 110px; }
    #r1-x { position: absolute; left: 320px; right: 320px; top: 395px; height: 12px; border-radius: 6px; background: #e8361c; transform-origin: 0 50%; }
""", body="""
    <div id="r1-bg"></div>
    <div id="r1-a" class="kt">eu fazia pra muita</div>
    <div id="r1-b" class="kt">GENTE <span>GRANDE</span></div>
    """ + recorte("r1", 6.23) + """
    <div id="r1-m" class="kt">pra <span class="ch ro">mim</span></div>
    <div id="r1-x"></div>
""", js="""
    tl.fromTo("#r1-rc", { y: 300, opacity: 0 }, { y: 0, opacity: 1, duration: .6, ease: "expo.out" }, 0);
    IN("#r1-a", 0.3);
    IN("#r1-b", 1.36, { scale: 1.4 });
    tl.fromTo("#r1-b span", { opacity: 0 }, { opacity: 1, duration: .2 }, 2.96);
    OUT(["#r1-a", "#r1-b"], 4.3);
    IN("#r1-m", 5.4, { scale: 1.3 });
    RISCO("#r1-x", 5.9);
""")
CUES = [{"t": 1.88, "som": "pop", "vol": .3}, {"t": 2.0, "som": "whoosh-rapido", "vol": .3}, {"t": 2.04, "som": "digitar", "vol": .25}, {"t": 2.52, "som": "pop", "vol": .3},
        {"t": 2.92, "som": "pop", "vol": .3}, {"t": 3.9, "som": "swipe", "vol": .3}, {"t": 4.2, "som": "impacto-suave", "vol": .35}, {"t": 6.47, "som": "whoosh", "vol": .3},
        {"t": 7.17, "som": "subida", "vol": .2}, {"t": 9.07, "som": "pop", "vol": .3}, {"t": 10.07, "som": "whoosh", "vol": .3}, {"t": 11.43, "som": "impacto", "vol": .35},
        {"t": 13.03, "som": "blip", "vol": .3}, {"t": 15.47, "som": "pop", "vol": .3}, {"t": 15.97, "som": "swipe", "vol": .3}]
escrever(CENAS, S, T, W, FIM, VDUR, punch=[], correcoes={}, sem_legenda=("m",))
json.dump(CUES, open("audio/cues.json", "w"))
