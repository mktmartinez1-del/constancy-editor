#!/usr/bin/env python3
"""Corretor Magnético · formato 02 Dor e solução · estilo 16 Místico Adivinhação (roxo e azul) · sem música.
Versão anterior (estilo 14): roteiro_estilo14.py"""
import json, random, sys
sys.path.insert(0, "%MOTOR%")   # caminho da pasta motor/
from cenas_base import tema, escrever, palavras, dur_video, recorte, perfil

T = tema("16"); W = palavras(); VDUR = dur_video(); FIM = 65.4

CENAS = {
    "a": (0.0, 2.55, "f"), "b": (2.6, 8.05, "m"), "c": (8.1, 13.45, "p"), "rd": (13.5, 19.2, "r"),
    "e": (19.28, 24.6, "m"), "f": (24.7, 28.95, "p"), "g1": (29.0, 32.95, "p"), "g2": (33.0, 35.3, "p"),
    "g3": (35.35, 38.8, "f"), "h": (38.85, 41.05, "m"), "ri": (41.1, 46.8, "r"), "j": (46.9, 54.75, "p"),
    "k1": (54.8, 57.4, "f"), "k2": (57.45, 60.95, "p"), "l": (61.0, 63.75, "f"), "z": (63.77, 65.4, "m"),
}

def estrelas(n=40, seed=1):
    r = random.Random(seed)
    return "".join(f'<i class="st" style="left:{r.random() * 1080:.0f}px;top:{r.random() * 1920:.0f}px;'
                   f'width:{r.choice([3, 4, 5, 6])}px;height:{r.choice([3, 4, 5, 6])}px;opacity:{0.25 + r.random() * 0.6:.2f}"></i>' for _ in range(n))

# vocabulário místico: céu estrelado, aura, bola de cristal, cartas de tarô, brilhos ✦
X = """
    #root .ceu { position: absolute; inset: 0; background: radial-gradient(75% 45% at 50% 38%, #2a1a6b 0%, #150c3a 45%, var(--bg) 80%); }
    #root .st { position: absolute; border-radius: 50%; background: #e9e2ff; box-shadow: 0 0 8px #c4b5fd; }
    #root .aura { position: absolute; border-radius: 50%; filter: blur(90px); opacity: .45; }
    #root .mx { position: absolute; left: 80px; right: 160px; color: var(--ink); font-weight: 800; letter-spacing: -.035em; line-height: 1; }
    #root .ms { font-family: var(--serif); font-style: italic; font-weight: 400; letter-spacing: -.01em; background: linear-gradient(90deg, #d8b4fe, #93c5fd); -webkit-background-clip: text; color: transparent; filter: drop-shadow(0 0 18px rgba(168,85,247,.55)); padding: 0 .06em; }
    #root .gl { text-shadow: 0 0 28px rgba(168,85,247,.75), 0 0 70px rgba(96,165,250,.35); }
    #root .sh { text-shadow: 0 6px 30px rgba(0,0,0,.7), 0 0 30px rgba(168,85,247,.45); }
    #root .sp { position: absolute; color: #e9d5ff; text-shadow: 0 0 14px #a855f7, 0 0 30px #60a5fa; font-size: 46px; line-height: 1; font-style: normal; }
    #root .bola { position: absolute; border-radius: 50%; overflow: hidden; background: radial-gradient(circle at 34% 28%, rgba(255,255,255,.7) 0%, rgba(216,180,254,.35) 12%, rgba(124,58,237,.35) 40%, rgba(37,99,235,.35) 65%, rgba(10,6,24,.92) 82%); box-shadow: 0 0 90px rgba(168,85,247,.65), 0 0 160px rgba(96,165,250,.3), inset 0 0 70px rgba(96,165,250,.55), inset 0 -30px 60px rgba(10,6,24,.8); }
    #root .bola .nv { position: absolute; inset: -20%; background: conic-gradient(from 0deg, transparent, rgba(192,132,252,.55), transparent 30%, rgba(96,165,250,.5), transparent 60%, rgba(232,121,249,.45), transparent); filter: blur(30px); }
    #root .bola .tx { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; text-align: center; color: #fff; font-weight: 800; letter-spacing: -.03em; text-shadow: 0 0 20px rgba(255,255,255,.6); }
    #root .base { position: absolute; border-radius: 50%; background: radial-gradient(ellipse at 50% 30%, #3b2a7a, #120a2e 70%); box-shadow: 0 20px 50px rgba(0,0,0,.6); }
    #root .tc { position: absolute; border-radius: 22px; }
    #root .tc .fc, #root .tc .vs { position: absolute; inset: 0; border-radius: 22px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 18px; }
    #root .tc .vs { background: repeating-linear-gradient(45deg, #2a1b5e 0 14px, #20154a 14px 28px); border: 3px solid #a78bfa; box-shadow: 0 0 30px rgba(168,85,247,.45); }
    #root .tc .vs::after { content: "✦"; font-size: 70px; color: #e9d5ff; text-shadow: 0 0 20px #a855f7; }
    #root .tc .fc { background: linear-gradient(170deg, #241556, #0f0a2a); border: 3px solid #c4b5fd; box-shadow: 0 0 40px rgba(168,85,247,.55); opacity: 0; color: #fff; }
    #root .tc .fc img { width: 110px; height: 110px; margin-bottom: 12px; }
    #root .tc .fc b { font-size: 40px; font-weight: 800; letter-spacing: -.02em; line-height: 1.05; }
    #root .tc .fc em { font-style: normal; font-size: 22px; letter-spacing: .3em; color: #c4b5fd; margin-bottom: 10px; }
    #root .chp { display: inline-block; padding: 6px 22px 10px; border-radius: 999px; background: linear-gradient(90deg, #7c3aed, #2563eb); color: #fff; box-shadow: 0 0 24px rgba(124,58,237,.55); }
    #root .vc { position: absolute; top: 40px; width: 445px; height: 490px; border-radius: 26px; overflow: hidden; border: 3px solid #a78bfa; box-shadow: 0 0 40px rgba(168,85,247,.45); background: #000; }
    #root .vc video { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
    #root .vc.s3 { width: 300px; height: 470px; top: 60px; }
    #root .tag { position: absolute; left: 0; right: 0; top: 0; text-align: center; z-index: 3; font-size: 44px; font-weight: 700; }
"""
JS = """
    const VIRAR = (c, t) => {   // carta de tarô vira e revela a frente
      tl.to(c, { rotationY: 90, duration: .22, ease: "power2.in" }, t);
      tl.set(c + " .vs", { opacity: 0 }, t + .22); tl.set(c + " .fc", { opacity: 1 }, t + .22);
      tl.fromTo(c, { rotationY: -90 }, { rotationY: 0, duration: .32, ease: "back.out(1.6)", immediateRender: false }, t + .22);
    };
    const BRILHO = (sel, t) => tl.fromTo(sel, { opacity: 0, scale: .2, rotation: -45 }, { opacity: 1, scale: 1, rotation: 0, duration: .35, ease: "back.out(3)", stagger: .07 }, t);
    const PISCAR = (sel, t0, dur) => tl.to(sel, { opacity: .15, duration: .6, ease: "sine.inOut", yoyo: true, repeat: Math.max(1, Math.floor(dur / .6) - 1), stagger: { each: .09, from: "random" } }, t0);
    const NEVOA = (sel, t0, dur) => tl.fromTo(sel, { rotation: 0 }, { rotation: 300, duration: dur, ease: "none" }, t0);
"""
def cj(js): return JS + js
def carta(cid, x, y, w, h, frente):
    return f'<div id="{cid}" class="tc" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="vs"></div><div class="fc">{frente}</div></div>'
def clip(cid, n, dur, ini, estilo, extra=""):
    return (f'<div id="{cid}" class="vc {extra}" style="{estilo}"><video id="{cid}-v" class="clip" data-start="0" data-duration="{dur}" data-media-start="{ini}" '
            f'src="assets/video/broll{n}.mp4" muted playsinline></video></div>')

S = {}
S["a"] = dict(css=X + """
    #a-p { top: 290px; font-size: 190px; }
    #a-d { top: 500px; font-size: 64px; }
""", body="""
    <div id="a-p" class="mx"><span class="ms">Para.</span></div>
    <div id="a-d" class="mx sh">deixa eu <span class="ms" style="font-size:84px">adivinhar…</span></div>
    <i data-layout-ignore class="sp" style="left:560px;top:300px">✦</i><i data-layout-ignore class="sp" style="left:650px;top:420px;font-size:30px">✦</i><i data-layout-ignore class="sp" style="left:120px;top:250px;font-size:34px">✦</i>
""", js=cj("""
    tl.fromTo("#a-p", { opacity: 0, scale: 1.4, filter: "blur(14px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: .25, ease: "power3.out" }, 0.0);
    [0.32, 0.72].forEach((t) => tl.fromTo("#a-p", { scale: 1.1 }, { scale: 1, duration: .2, ease: "power2.out" }, t));
    BRILHO("#root .sp", 0.5);
    IN("#a-d", 1.2, { x: -40 });
    OUT(["#a-p", "#a-d", "#root .sp"], 2.3);
"""))
S["b"] = dict(css=X + """
    #b-b { left: 250px; top: 520px; width: 580px; height: 580px; }
    #b-base { left: 330px; top: 1060px; width: 420px; height: 110px; }
    #b-t1, #b-t2, #b-t3 { font-size: 74px; line-height: 1.05; padding: 0 70px; }
    #b-q { top: 300px; font-size: 60px; text-align: center; left: 0; right: 0; }
    #b-v { top: 1210px; font-size: 64px; text-align: center; left: 0; right: 0; }
""", body=f"""
    <div class="ceu"></div>{estrelas(45, 2)}
    <div class="aura" style="left:200px;top:480px;width:680px;height:680px;background:#7c3aed"></div>
    <div id="b-q" class="mx gl">a bola de cristal diz…</div>
    <div id="b-base" class="base"></div>
    <div id="b-b" class="bola"><div class="nv"></div>
      <div id="b-t1" class="tx">corretor</div>
      <div id="b-t2" class="tx">nos Estados Unidos</div>
      <div id="b-t3" class="tx">sem resultado no digital</div>
    </div>
    <div id="b-v" class="mx"><span class="ms">não é verdade?</span></div>
""", js=cj("""
    tl.fromTo("#b-b", { opacity: 0, scale: .6 }, { opacity: 1, scale: 1, duration: .7, ease: "expo.out" }, 0.0);
    tl.fromTo("#b-base", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: .5 }, 0.2);
    NEVOA("#b-b .nv", 0, 5.4);
    PISCAR("#root .st", 0.2, 5);
    IN("#b-q", 0.0);
    tl.fromTo("#b-t1", { opacity: 0, filter: "blur(16px)", scale: .8 }, { opacity: 1, filter: "blur(0px)", scale: 1, duration: .45 }, 0.04);
    tl.to("#b-t1", { opacity: 0, filter: "blur(16px)", duration: .25 }, 1.3);
    tl.fromTo("#b-t2", { opacity: 0, filter: "blur(16px)", scale: .8 }, { opacity: 1, filter: "blur(0px)", scale: 1, duration: .45 }, 1.48);
    tl.to("#b-t2", { opacity: 0, filter: "blur(16px)", duration: .25 }, 3.2);
    tl.fromTo("#b-t3", { opacity: 0, filter: "blur(16px)", scale: .8 }, { opacity: 1, filter: "blur(0px)", scale: 1, duration: .45 }, 3.4);
    IN("#b-v", 4.76);
"""))
PONTOS = "".join(f'<i class="pt{" ap" if n in (2, 7) else ""}">✦</i>' for n in range(10))
S["c"] = dict(css=X + """
    #c-t { top: 10px; font-size: 72px; left: 0; right: 0; text-align: center; }
    #c-g { position: absolute; left: 70px; right: 70px; top: 150px; display: grid; grid-template-columns: repeat(5, 1fr); gap: 20px; justify-items: center; }
    #root .pt { font-style: normal; font-size: 110px; line-height: 1; color: #6d5fa8; text-shadow: 0 0 20px rgba(168,85,247,.5); }
    #c-s { top: 425px; font-size: 50px; left: 0; right: 0; text-align: center; }
""", body="""    <div class="z">
      <div id="c-t" class="mx">a <span class="chp">maioria</span> dos corretores</div>
      <div id="c-g">""" + PONTOS + """</div>
      <div id="c-s" class="mx">sem resultado <span class="ms" style="font-size:62px">no digital</span></div>
    </div>""", js=cj("""
    tl.fromTo("#c-g .pt", { opacity: 0, scale: .2, rotation: -60 }, { opacity: 1, scale: 1, rotation: 0, duration: .4, ease: "back.out(2.5)", stagger: .05 }, 0.4);
    IN("#c-t", 2.54);
    tl.to("#c-g .pt:not(.ap)", { color: "#2a2350", textShadow: "0 0 0px rgba(0,0,0,0)", duration: .35, stagger: .04 }, 3.1);
    tl.to("#c-g .pt.ap", { color: "#93c5fd", textShadow: "0 0 30px #60a5fa, 0 0 60px #a855f7", scale: 1.15, duration: .35 }, 3.6);
    IN("#c-s", 4.38);
"""))
LEQUE = "".join(f'<div class="lq" style="transform: rotate({-56 + i * 16}deg)"><div class="lqc">{i + 1}</div></div>' for i in range(8))
S["rd"] = dict(css=X + """
    #rd-q { top: 250px; font-size: 110px; left: 0; right: 0; text-align: center; }
    #rd-n { top: 240px; font-size: 118px; left: 0; right: 0; text-align: center; }
    #rd-lq { position: absolute; left: 540px; top: 1100px; width: 0; height: 0; }
    #root .lq { position: absolute; left: -85px; top: -760px; width: 170px; height: 760px; transform-origin: 50% 100%; }
    #root .lqc { width: 170px; height: 250px; border-radius: 16px; background: linear-gradient(170deg, #2a1b5e, #120a2e); border: 3px solid #a78bfa; box-shadow: 0 0 30px rgba(168,85,247,.55); color: #e9d5ff; font-size: 80px; font-weight: 800; display: flex; align-items: center; justify-content: center; }
    #rd-s { top: 1160px; font-size: 56px; left: 0; right: 0; text-align: center; }
""", body=f"""
    <div class="ceu"></div>{estrelas(40, 4)}
    <div class="aura" style="left:240px;top:520px;width:600px;height:600px;background:#7c3aed"></div>
    <div id="rd-lq">{LEQUE}</div>
    <div id="rd-q" class="mx gl">por <span class="ms" style="font-size:130px">quê?</span></div>
    <div id="rd-n" class="mx gl">8 <span class="ms" style="font-size:132px">formatos</span></div>
    """ + recorte("rd", 5.7) + """
    <div id="rd-s" class="mx sh">que realmente funcionam</div>
""", js=cj("""
    tl.fromTo("#rd-rc", { y: 300, opacity: 0 }, { y: 0, opacity: 1, duration: .6, ease: "expo.out" }, 0);
    PISCAR("#root .st", 0.2, 5.4);
    IN("#rd-q", 0.5, { scale: 1.3 });
    OUT("#rd-q", 2.5);
    tl.fromTo("#rd-lq .lqc", { opacity: 0, y: 200 }, { opacity: 1, y: 0, duration: .5, ease: "expo.out", stagger: .08 }, 2.82);
    IN("#rd-n", 2.82, { scale: 1.4 });
    IN("#rd-s", 4.42);
"""))
S["e"] = dict(css=X + """
    #e-b { left: 290px; top: 820px; width: 500px; height: 500px; opacity: .55; }
    #e-n { top: 310px; font-size: 60px; left: 0; right: 0; text-align: center; color: var(--sub); font-weight: 600; }
    #e-c { top: 400px; font-size: 140px; left: 0; right: 0; text-align: center; }
    #e-m { top: 560px; font-size: 160px; left: 0; right: 0; text-align: center; }
    #e-r { position: absolute; left: 80px; right: 160px; top: 1360px; display: flex; gap: 14px; justify-content: center; }
    #e-r span { font-size: 38px; white-space: nowrap; }
""", body=f"""
    <div class="ceu"></div>{estrelas(50, 5)}
    <div id="e-b" class="bola"><div class="nv"></div></div>
    <div id="e-n" class="mx">nós criamos o</div>
    <div id="e-c" class="mx gl">CORRETOR</div>
    <div id="e-m" class="mx"><span class="ms">Magnético</span></div>
    <i data-layout-ignore class="sp" style="left:170px;top:560px">✦</i><i data-layout-ignore class="sp" style="left:880px;top:500px;font-size:34px">✦</i><i data-layout-ignore class="sp" style="left:820px;top:700px;font-size:28px">✦</i>
    <div id="e-r"><span class="chp">1 · passo</span><span class="chp">2 · a passo</span><span class="chp">3 · o que fazer</span></div>
""", js=cj("""
    PISCAR("#root .st", 0.1, 5);
    NEVOA("#e-b .nv", 0, 5.3);
    IN("#e-n", 0.1);
    IN("#e-c", 0.72, { y: 50 });
    IN("#e-m", 1.36, { scale: 1.4 });
    BRILHO("#root .sp", 1.5);
    tl.fromTo("#e-r span", { opacity: 0, y: 30, scale: .7 }, { opacity: 1, y: 0, scale: 1, duration: .4, ease: "back.out(2)", stagger: .5 }, 3.44);
"""))
S["f"] = dict(css=X, body="""    <div class="z" style="perspective:1400px">
      """ + carta("f-1", 10, 40, 285, 450, '<em>I</em><img src="assets/img/target.png" alt="" /><b>método</b>')
          + carta("f-2", 327, 40, 285, 450, '<em>II</em><img src="assets/img/video-camera.png" alt="" /><b>aulas gravadas</b>')
          + carta("f-3", 644, 40, 285, 450, '<em>III</em><img src="assets/img/location.png" alt="" /><b>presencial</b>') + """
    </div>""", js=cj("""
    tl.fromTo("#root .tc", { opacity: 0, y: 80 }, { opacity: 1, y: 0, duration: .5, ease: "expo.out", stagger: .12 }, 0.0);
    VIRAR("#f-1", .26); VIRAR("#f-2", .82); VIRAR("#f-3", 3.3);
"""))
S["g1"] = dict(css=X, body="""    <div class="z">
      """ + clip("g1-a", 3, 3.95, 2.0, "left:0;transform:rotate(-3deg)") + clip("g1-b", 6, 3.95, 0.8, "left:495px;transform:rotate(3deg)") + """
      <div id="g1-t" class="tag"><span class="chp">treinamento presencial</span></div>
    </div>""", js=cj("""
    tl.fromTo("#g1-a", { opacity: 0, x: -120, rotation: -12 }, { opacity: 1, x: 0, rotation: -3, duration: .55, ease: "expo.out" }, 0.1);
    tl.fromTo("#g1-b", { opacity: 0, x: 120, rotation: 12 }, { opacity: 1, x: 0, rotation: 3, duration: .55, ease: "expo.out" }, 0.45);
    tl.fromTo("#g1-t", { opacity: 0, y: -30, scale: .7 }, { opacity: 1, y: 0, scale: 1, duration: .4, ease: "back.out(2)" }, 3.0);
"""))
S["g2"] = dict(css=X + """
    #root .nm, #root .fw { color: #fff; }
    #root .ph { box-shadow: 0 0 40px rgba(168,85,247,.55); border-color: #6d4fd6; }
""", body="""    <div class="z">
""" + perfil("g2-pf", "ricardo", "Ricardo Resstel", "ricardoresstel", "39,9 mil", True) + """
      <i data-layout-ignore class="sp" style="left:330px;top:-10px">✦</i><i data-layout-ignore class="sp" style="left:900px;top:120px;font-size:30px">✦</i>
    </div>""", js=cj("""
    PERFIL("#g2-pf", 0.04);
    BRILHO("#root .sp", 0.4);
"""))
S["g3"] = dict(css=X + """
    #g3-c { top: 300px; font-size: 90px; }
    #g3-d { top: 420px; font-size: 68px; }
""", body="""
    <div id="g3-c" class="mx sh">+ aulas <span class="ms" style="font-size:110px">gravadas</span></div>
    <div id="g3-d" class="mx sh">aula por aula</div>
""", js=cj("""
    IN("#g3-c", 0.15, { x: -60 });
    IN("#g3-d", 1.77);
    OUT(["#g3-c", "#g3-d"], 3.2);
"""))
S["h"] = dict(css=X + """
    #h-a { top: 330px; font-size: 72px; left: 0; right: 0; text-align: center; }
    #h-n { top: 450px; font-size: 320px; left: 0; right: 0; text-align: center; line-height: .9; }
    #h-r { top: 790px; font-size: 64px; left: 0; right: 0; text-align: center; }
""", body=f"""
    <div class="ceu"></div>{estrelas(40, 8)}
    <div class="aura" style="left:290px;top:420px;width:500px;height:400px;background:#2563eb"></div>
    <div id="h-a" class="mx">editar no <span class="chp">CapCut</span></div>
    <div id="h-n" class="mx"><span class="ms">10x</span></div>
    <div id="h-r" class="mx gl">mais rápido</div>
""", js=cj("""
    PISCAR("#root .st", 0, 2);
    IN("#h-a", 0.2);
    tl.fromTo("#h-n", { scale: .3, opacity: 0 }, { scale: 1, opacity: 1, duration: .45, ease: "back.out(2)" }, 1.15);
    IN("#h-r", 1.6);
"""))
S["ri"] = dict(css=X + """
    #ri-n { top: 270px; font-size: 110px; left: 0; right: 0; text-align: center; line-height: .95; }
    #ri-a { top: 1160px; font-size: 56px; left: 0; right: 0; text-align: center; }
""", body=f"""
    <div class="ceu"></div>{estrelas(45, 9)}
    <div class="aura" style="left:200px;top:500px;width:680px;height:680px;background:#2563eb"></div>
    <div id="ri-n" class="mx gl">COPY<br /><span class="ms" style="font-size:130px">Magnética</span></div>
    """ + recorte("ri", 5.7) + """
    <div id="ri-a" class="mx sh">a ferramenta no <span class="chp">ChatGPT</span></div>
""", js=cj("""
    tl.fromTo("#ri-rc", { y: 300, opacity: 0 }, { y: 0, opacity: 1, duration: .6, ease: "expo.out" }, 0);
    PISCAR("#root .st", 0.2, 5.4);
    IN("#ri-a", 0.18);
    IN("#ri-n", 2.98, { scale: 1.3 });
"""))
ITENS = [("gravar", .46), ("editar", 1.26), ("postar no Instagram", 2.54), ("Reels teste", 4.14), ("ganhar seguidores", 5.58)]
S["j"] = dict(css=X + """
    #j-w { position: absolute; left: 60px; right: 60px; top: 0; height: 520px; border-radius: 26px; background: linear-gradient(170deg, rgba(42,27,94,.85), rgba(15,10,42,.9)); border: 2px solid rgba(196,181,253,.5); box-shadow: 0 0 40px rgba(124,58,237,.35); }
    #j-h { position: absolute; left: 40px; top: 22px; font-size: 30px; letter-spacing: .3em; color: #c4b5fd; }
    #root .ck { position: absolute; left: 40px; display: flex; align-items: center; gap: 20px; font-size: 44px; font-weight: 700; color: #fff; }
    #root .ck i { font-style: normal; font-size: 40px; color: #6d5fa8; }
    #j-v { position: absolute; left: 0; right: 0; top: 400px; text-align: center; font-size: 120px; }
""", body="""    <div class="z">
      <div id="j-w"><div id="j-h">SUA PREVISÃO</div>
""" + "".join(f'        <div id="j-{n}" class="ck" style="top:{80 + n * 62}px"><i>✦</i>{txt}</div>\n' for n, (txt, _) in enumerate(ITENS)) + """      </div>
      <div id="j-v"><span class="ms">e vender.</span></div>
    </div>""", js=cj("""
    tl.fromTo("#j-w", { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: .5, ease: "expo.out" }, 0.05);
""" + "".join(f'    IN("#j-{n}", {t}, {{ x: -40 }}); tl.to("#j-{n} i", {{ color: "#c4b5fd", textShadow: "0 0 16px #a855f7", duration: .25 }}, {t + 0.2});\n' for n, (_, t) in enumerate(ITENS)) + """
    tl.to("#j-w", { opacity: .3, duration: .3 }, 7.1);
    tl.fromTo("#j-v", { opacity: 0, scale: .4 }, { opacity: 1, scale: 1, duration: .45, ease: "back.out(2)" }, 7.34);
"""))
S["k1"] = dict(css=X + """
    #k-a { top: 300px; font-size: 72px; }
    #k-b { top: 400px; font-size: 130px; }
""", body="""
    <div id="k-a" class="mx sh">você também com</div>
    <div id="k-b" class="mx"><span class="ms">resultado</span></div>
""", js=cj("""
    IN("#k-a", 0.4, { x: -50 });
    IN("#k-b", 1.33, { scale: 1.3 });
"""))
S["k2"] = dict(css=X, body="""    <div class="z">
      """ + clip("k2-a", 5, 3.5, 6.0, "left:0;transform:rotate(-4deg)", "s3") + clip("k2-b", 3, 3.5, 12.0, "left:320px", "s3") + clip("k2-c", 7, 3.5, 3.5, "left:640px;transform:rotate(4deg)", "s3") + """
      <div id="k2-t" class="tag"><span class="chp">junto com a gente</span></div>
    </div>""", js=cj("""
    tl.fromTo(["#k2-a", "#k2-b", "#k2-c"], { opacity: 0, y: 120, scale: .8 }, { opacity: 1, y: 0, scale: 1, duration: .5, ease: "back.out(1.6)", stagger: .15 }, 0.2);
    tl.fromTo("#k2-t", { opacity: 0, y: -30, scale: .7 }, { opacity: 1, y: 0, scale: 1, duration: .4, ease: "back.out(2)" }, 3.08);
"""))
S["l"] = dict(css=X + """
    #l-a { top: 300px; font-size: 92px; }
    #l-b { top: 420px; font-size: 64px; }
    #l-s { left: 470px; top: 540px; font-size: 110px; }
""", body="""
    <div id="l-a" class="mx sh">chama a <span class="ms" style="font-size:110px">gente</span></div>
    <div id="l-b" class="mx sh">aqui embaixo</div>
    <i id="l-s" data-layout-ignore class="sp">↓</i>
""", js=cj("""
    IN("#l-a", 0.41, { x: -50 });
    IN("#l-b", 1.05);
    tl.fromTo("#l-s", { opacity: 0, y: -40 }, { opacity: 1, y: 0, duration: .35, ease: "back.out(2)" }, 1.2);
    tl.to("#l-s", { y: 30, duration: .4, yoyo: true, repeat: 3, ease: "sine.inOut" }, 1.6);
"""))
S["z"] = dict(css=X + """
    #z-b { left: 340px; top: 360px; width: 400px; height: 400px; }
    #z-c { top: 820px; font-size: 120px; left: 0; right: 0; text-align: center; }
    #z-m { top: 940px; font-size: 150px; left: 0; right: 0; text-align: center; }
    #z-s { top: 1180px; font-size: 46px; left: 0; right: 0; text-align: center; color: var(--sub); font-weight: 600; }
""", body=f"""
    <div class="ceu"></div>{estrelas(50, 12)}
    <div id="z-b" class="bola"><div class="nv"></div></div>
    <div id="z-c" class="mx gl">CORRETOR</div>
    <div id="z-m" class="mx"><span class="ms">Magnético</span></div>
    <div id="z-s" class="mx">chama a gente aqui embaixo ↓</div>
""", js=cj("""
    NEVOA("#z-b .nv", 0, 1.6);
    tl.fromTo("#z-b", { opacity: 0, scale: .6 }, { opacity: 1, scale: 1, duration: .5, ease: "expo.out" }, 0.0);
    IN("#z-c", 0.1, { y: 40 });
    IN("#z-m", 0.3, { scale: 1.3 });
    IN("#z-s", 0.6);
"""))

PUNCH = [0.0, 56.13]
CORRECOES = {"auladas": "aulas gravadas", "Cop": "Copy", "Reals": "Reels", "test": "teste"}
# som: poucos efeitos, suaves e baixos (brilho, vidro, whoosh macio). Nada de bipe, digitação ou som de telefone.
WH, VD, BR, SB = "whoosh/fs-264777-swoosh.ogg", "ding/kenney-interface-glass-001.ogg", "ding/fs-349504-triangle-open-04.ogg", "riser/fs-464250-echo-chromatic-riser-wav.ogg"
POP = "pop/fs-447910-plop.ogg"
CUES = [{"t": t, "som": s, "vol": v} for t, s, v in [
    (0.0, "impacto-suave", .18), (0.5, BR, .1),
    (2.6, WH, .14), (2.65, SB, .1), (4.08, VD, .1), (6.0, VD, .1),
    (8.1, WH, .12), (11.2, BR, .1),
    (13.5, WH, .14), (16.32, "impacto-suave", .16), (16.4, BR, .1),
    (19.28, WH, .14), (20.64, SB, .12), (22.72, POP, .1), (23.22, POP, .1), (23.72, POP, .1),
    (24.7, WH, .12), (24.96, VD, .1), (25.52, VD, .1), (28.0, VD, .1),
    (29.0, WH, .12), (32.0, POP, .1), (33.04, BR, .1), (35.35, WH, .1),
    (38.85, WH, .12), (40.0, "impacto-suave", .15),
    (41.1, WH, .14), (44.08, SB, .12),
    (46.9, WH, .12), (47.36, VD, .08), (48.16, VD, .08), (49.44, VD, .08), (51.04, VD, .08), (52.48, VD, .08), (54.24, BR, .14),
    (54.8, WH, .1), (57.45, WH, .12), (60.53, POP, .1),
    (61.41, POP, .1), (63.77, WH, .12), (63.9, BR, .12),
]]
for sid in S:   # seletores de grupo restritos à própria cena
    S[sid]["js"] = S[sid]["js"].replace('"#root ', f'"#{sid} ')
escrever(CENAS, S, T, W, FIM, VDUR, punch=PUNCH, correcoes=CORRECOES, sem_legenda=("m",))
json.dump(CUES, open("audio/cues.json", "w"), indent=1)
