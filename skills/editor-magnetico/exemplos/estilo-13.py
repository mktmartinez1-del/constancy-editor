#!/usr/bin/env python3
# Amostra do estilo 13 · UI Glass Laranja
import json, sys
sys.path.insert(0, "%MOTOR%")   # caminho da pasta motor/ (o roteiro.py do projeto já vem com ele)
from cenas_base import tema, escrever, palavras, dur_video, recorte

T = tema("13"); W = palavras(); VDUR = dur_video(); FIM = 16.4
CENAS = {"c1": (0.0, 1.95, "f"), "c2": (2.0, 6.4, "m"), "c3": (6.47, 10.0, "p"), "r1": (10.07, 16.3, "r")}
GL = """
    #root .gl { position: absolute; display: inline-flex; align-items: center; gap: 18px; padding: 20px 34px 20px 20px; border-radius: 999px; background: rgba(255,255,255,.78); border: 2px solid #fff; box-shadow: 0 24px 50px rgba(0,0,0,.12), inset 0 -6px 14px rgba(0,0,0,.04); font-size: 52px; font-weight: 600; letter-spacing: -.03em; color: #1b1b1b; white-space: nowrap; }
    #root .gl i { width: 70px; height: 70px; border-radius: 50%; border: 3px solid var(--ac); color: var(--ac); font-style: normal; font-size: 36px; font-weight: 700; display: flex; align-items: center; justify-content: center; }
    #root .arc { position: absolute; border-radius: 50%; border: 2px solid rgba(0,0,0,.07); }
"""
S = {}
S["c1"] = dict(css=GL + "#c1-p { left: 50%; top: 320px; }", body="""
    <div id="c1-p" class="gl"><i>↻</i>cansado de tentar?</div>
""", js="""
    tl.fromTo("#c1-p", { xPercent: -50, opacity: 0, y: 40, scale: .8 }, { xPercent: -50, opacity: 1, y: 0, scale: 1, duration: .5, ease: "back.out(1.6)" }, 1.0);
""")
S["c2"] = dict(css=GL + """
    #c2-bg { position: absolute; inset: 0; background: radial-gradient(80% 50% at 50% 40%, #fafafa, var(--bg) 60%, var(--bg2)); }
    #c2-st { position: absolute; left: 0; right: 0; top: 380px; height: 520px; perspective: 1400px; }
    #c2-x { position: absolute; left: 360px; top: 730px; width: 360px; height: 360px; border-radius: 50%; background: radial-gradient(circle at 35% 30%, #ff9a3c, var(--ac) 60%, #d93d00); box-shadow: 0 40px 80px rgba(255,90,31,.45); color: #fff; font-size: 180px; font-weight: 300; display: flex; align-items: center; justify-content: center; }
    #c2-t { top: 1150px; font-size: 54px; color: var(--ink); text-transform: none; font-weight: 600; letter-spacing: -.03em; }
    #c2-v { top: 300px; font-size: 76px; text-transform: none; font-weight: 700; }
""", body="""
    <div id="c2-bg"></div>
    <div class="arc" style="left:-300px;top:200px;width:900px;height:900px"></div><div class="arc" style="right:-400px;top:900px;width:1000px;height:1000px"></div>
    <div id="c2-st">
      <div id="c2-a" class="gl" style="left:170px;top:0"><i>1</i>tentar</div>
      <div id="c2-b" class="gl" style="left:300px;top:150px"><i>2</i>tentar</div>
      <div id="c2-c" class="gl" style="left:430px;top:300px"><i>3</i>tentar</div>
    </div>
    <div id="c2-v" class="t">e nada <span class="it">funciona</span></div>
    <div id="c2-x">✕</div>
    <div id="c2-t" class="t">não conseguir no digital</div>
""", js="""
    [["#c2-a", 0.04], ["#c2-b", 0.52], ["#c2-c", 0.92]].forEach(([s, t]) => tl.fromTo(s, { opacity: 0, rotationY: -55, rotationX: 15, x: -160 }, { opacity: 1, rotationY: -18, rotationX: 8, x: 0, duration: .6, ease: "expo.out" }, t));
    tl.to("#c2-st", { y: -40, duration: 4, ease: "none" }, 0.3);
    tl.to(["#c2-a", "#c2-b", "#c2-c"], { opacity: .35, duration: .3 }, 1.4);
    POP("#c2-x", 1.48);
    IN("#c2-t", 1.7);
    OUT("#c2-st", 2.75);
    IN("#c2-v", 2.9, { y: -30 });
""")
S["c3"] = dict(css=GL + """
    #c3-l { position: absolute; left: 90px; right: 90px; top: 120px; height: 4px; background: rgba(0,0,0,.08); }
    #c3-lf { position: absolute; left: 90px; right: 90px; top: 120px; height: 4px; background: var(--ac); transform-origin: 0 50%; }
    #root .dt { position: absolute; top: 82px; width: 80px; height: 80px; border-radius: 50%; background: #fff; border: 3px solid var(--ac); color: var(--ac); font-size: 34px; font-weight: 800; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 24px rgba(255,90,31,.25); }
    #root .dl { position: absolute; top: 180px; width: 260px; text-align: center; font-size: 32px; font-weight: 600; color: var(--sub); }
    #c3-g { left: 50%; top: 300px; }
    #c3-g img { width: 70px; height: 70px; }
""", body="""    <div class="z">
      <div id="c3-l"></div><div id="c3-lf"></div>
      <div class="dt" style="left:50px">1</div><div class="dl" style="left:-40px">eu também</div>
      <div class="dt" style="left:430px">2</div><div class="dl" style="left:340px;color:#1b1b1b">passei</div>
      <div class="dt" style="left:810px">3</div><div class="dl" style="left:720px">e mudei</div>
      <div id="c3-g" class="gl"><img src="assets/img/clock.png" alt="" />um tempo atrás</div>
    </div>""", js="""
    tl.fromTo("#c3 .dt", { opacity: 0, scale: .3 }, { opacity: 1, scale: 1, duration: .4, ease: "back.out(2)", stagger: .5 }, 0.2);
    tl.fromTo("#c3 .dl", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: .35, stagger: .5 }, 0.3);
    tl.fromTo("#c3-lf", { scaleX: 0 }, { scaleX: 1, duration: 1.4, ease: "power2.inOut" }, 0.3);
    tl.fromTo("#c3-g", { xPercent: -50, opacity: 0, y: 40, rotationX: 40 }, { xPercent: -50, opacity: 1, y: 0, rotationX: 0, duration: .55, ease: "expo.out" }, 1.76);
""")
S["r1"] = dict(css=GL + """
    #r1-bg { position: absolute; inset: 0; background: radial-gradient(70% 45% at 50% 35%, #ffffff, var(--bg) 60%, var(--bg2)); }
    #r1-a { top: 400px; font-size: 54px; text-transform: none; font-weight: 600; color: var(--sub); }
    #r1-b { top: 470px; font-size: 200px; letter-spacing: -.06em; color: #1b1b1b; }
    #r1-b span { color: var(--ac); }
    #r1-orb { position: absolute; left: 540px; top: 760px; width: 0; height: 0; }
    #r1-orb .gl { font-size: 40px; padding: 14px 28px 14px 14px; }
    #r1-orb .gl i { width: 54px; height: 54px; font-size: 26px; }
    #r1-m { left: 50%; top: 330px; background: var(--ac); color: #fff; border-color: var(--ac); font-size: 64px; font-weight: 800; }
    #r1-m i { border-color: #fff; color: #fff; }
""", body="""
    <div id="r1-bg"></div>
    <div class="arc" style="left:90px;top:330px;width:900px;height:900px"></div>
    <div id="r1-a" class="t">eu fazia pra muita</div>
    <div id="r1-b" class="t"><span>GENTE</span></div>
    """ + recorte("r1", 6.23) + """
    <div id="r1-orb">
      <div id="r1-o1" class="gl" style="left:-470px;top:-60px"><i>★</i>marcas</div>
      <div id="r1-o2" class="gl" style="left:180px;top:120px"><i>$</i>empresas</div>
      <div id="r1-o3" class="gl" style="left:-430px;top:300px"><i>✓</i>clientes</div>
    </div>
    <div id="r1-m" class="gl"><i>?</i>e pra mim?</div>
""", js="""
    tl.fromTo("#r1-rc", { y: 300, opacity: 0 }, { y: 0, opacity: 1, duration: .6, ease: "expo.out" }, 0);
    IN("#r1-a", 0.3);
    IN("#r1-b", 1.36, { scale: 1.3 });
    tl.fromTo("#r1-orb .gl", { opacity: 0, scale: .4, rotationY: 60 }, { opacity: 1, scale: 1, rotationY: 0, duration: .5, ease: "back.out(1.6)", stagger: .2 }, 2.56);
    tl.to("#r1-orb", { rotation: 4, duration: 3, ease: "sine.inOut" }, 2.6);
    OUT(["#r1-a", "#r1-b", "#r1-orb"], 4.3);
    tl.fromTo("#r1-m", { xPercent: -50, opacity: 0, scale: .6 }, { xPercent: -50, opacity: 1, scale: 1, duration: .5, ease: "back.out(1.8)" }, 5.2);
""")
CUES = [{"t": 1.0, "som": "pop", "vol": .3}, {"t": 2.0, "som": "whoosh", "vol": .3}, {"t": 2.04, "som": "swipe", "vol": .25}, {"t": 2.52, "som": "swipe", "vol": .25},
        {"t": 2.92, "som": "swipe", "vol": .25}, {"t": 3.48, "som": "impacto-suave", "vol": .35}, {"t": 4.9, "som": "plop", "vol": .25}, {"t": 6.47, "som": "whoosh", "vol": .3},
        {"t": 6.7, "som": "tick", "vol": .3}, {"t": 7.2, "som": "tick", "vol": .3}, {"t": 7.7, "som": "tick", "vol": .3}, {"t": 8.23, "som": "pop", "vol": .3},
        {"t": 10.07, "som": "whoosh", "vol": .3}, {"t": 11.43, "som": "impacto", "vol": .35}, {"t": 12.63, "som": "pop", "vol": .28}, {"t": 12.83, "som": "pop", "vol": .28},
        {"t": 13.03, "som": "pop", "vol": .28}, {"t": 15.27, "som": "pop", "vol": .35}]
escrever(CENAS, S, T, W, FIM, VDUR, punch=[], correcoes={})
json.dump(CUES, open("audio/cues.json", "w"))
