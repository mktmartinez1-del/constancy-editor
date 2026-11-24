"""Biblioteca de cenas do Constancy Editor.

Um projeto tem um roteiro.py que importa este módulo, define as cenas e chama escrever().
Tipos de cena (CENAS[id] = (início, fim, tipo)):
  "p"  tela dividida: painel de motion em cima, rosto num card embaixo
  "f"  tela cheia: vídeo inteiro + textos por cima (com escurecimento leve)
  "m"  motion puro: o vídeo some, a cena ocupa a tela toda (a voz continua)
  "r"  recorte: o vídeo some e a pessoa volta SEM FUNDO dentro da cena (recortar.py), com texto e objetos atrás dela
Antes da primeira cena (ou entre cenas) o vídeo roda em tela cheia, sem nada por cima.
"""
import html, json, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(AQUI)
TEMAS = {k: v for k, v in json.load(open(os.path.join(SKILL, "estilos", "temas.json"))).items() if not k.startswith("_")}
GSAP = "https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"

def tema(estilo):
    t = dict(TEMAS[str(estilo).zfill(2)])
    t["id"] = str(estilo).zfill(2)
    return t

def fontes_css(t):
    css = []
    if "Manrope" in (t["sans"], t["display"]):
        css.append('@font-face { font-family: "Manrope"; src: url("assets/fonts/Manrope.ttf") format("truetype"); font-weight: 200 800; }')
    if t["serif"] == "Instrument Serif":
        css.append('@font-face { font-family: "Instrument Serif"; src: url("assets/fonts/InstrumentSerif-Italic.ttf") format("truetype"); font-style: italic; }')
    return "\n    ".join(css)

def vars_css(t):
    return (f'--bg: {t["fundo"]}; --bg2: {t["fundo2"]}; --ink: {t["tinta"]}; --sub: {t["sub"]}; --ac: {t["acento"]}; '
            f'--ac2: {t["acento2"]}; --card: {t["card"]}; --sans: "{t["sans"]}", sans-serif; --serif: "{t["serif"]}", serif; --disp: "{t["display"]}", sans-serif;')

# ---------------------------------------------------------------- cena (sub-composição)
HEAD = """<template>
  <style>
    %FONTES%
    #root { %VARS% position: absolute; inset: 0; overflow: hidden; font-family: var(--sans); color: var(--ink); }
    #root .z { position: absolute; left: 70px; right: 70px; top: 275px; height: 530px; }
    #root .zm { position: absolute; left: 80px; right: 160px; top: 300px; bottom: 440px; }
    #root .t { position: absolute; left: 0; right: 0; text-align: center; font-family: var(--disp); font-weight: 800; letter-spacing: -0.035em; line-height: .95; text-transform: uppercase; }
    #root .s { position: absolute; left: 0; right: 0; text-align: center; font-weight: 600; letter-spacing: -0.02em; line-height: 1.1; }
    #root .it { font-family: var(--serif); font-style: italic; font-weight: 400; text-transform: none; letter-spacing: -0.01em; color: var(--ac); position: relative; }
    #root .ac { color: var(--ac); }
    #root .ac2 { color: var(--ac2); }
    #root .rd { color: #e8361c; }
    #root .sub { color: var(--sub); }
    #root .ul { position: relative; display: inline-block; }
    #root .ul::after { content: ""; position: absolute; left: 0; right: 0; bottom: -6px; height: 8px; border-radius: 4px; background: var(--ac); transform-origin: 0 50%; transform: scaleX(var(--u, 1)); }
    #root .ico { position: absolute; width: 190px; height: 190px; object-fit: contain; filter: drop-shadow(0 24px 30px rgba(0,0,0,.28)); }
    #root .card { position: absolute; border-radius: 26px; background: var(--card); box-shadow: 0 20px 50px rgba(0,0,0,.16); border: 2px solid rgba(127,127,127,.12); }
    #root .pill { display: inline-block; padding: 12px 26px; border-radius: 999px; background: var(--ink); color: var(--bg); font-weight: 800; font-size: 34px; letter-spacing: .02em; }
    #root .pill.acp { background: var(--ac); color: %SOBRE_AC%; }
    #root .luz { color: #fff; text-shadow: 0 8px 40px rgba(0,0,0,.55); }
    #root .bub { position: absolute; padding: 26px 34px; border-radius: 34px; background: #fff; color: #170a04; font-size: 46px; font-weight: 700; line-height: 1.15; box-shadow: 0 24px 60px rgba(0,0,0,.3); }
    #root .num { font-family: var(--disp); font-weight: 800; letter-spacing: -.05em; line-height: .9; }
    /* perfil do Instagram (print real em um celular + dados) */
    #root .ph { position: absolute; left: 10px; top: 0; width: 290px; height: 530px; border-radius: 44px; background: #0c0c0c; border: 7px solid #1b1b1b; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,.35); }
    #root .ph img { position: absolute; left: 0; top: 0; width: 276px; height: auto; }
    #root .inf { position: absolute; left: 350px; top: 6px; width: 590px; }
    #root .avr { width: 150px; height: 150px; border-radius: 50%; padding: 6px; background: conic-gradient(from 200deg, #feda75, #fa7e1e, #d62976, #962fbf, #4f5bd5, #feda75); }
    #root .avr img { width: 100%; height: 100%; border-radius: 50%; border: 5px solid var(--bg); object-fit: cover; display: block; }
    #root .nm { font-size: 52px; font-weight: 800; letter-spacing: -.03em; margin-top: 16px; line-height: 1.05; white-space: nowrap; }
    #root .vf { display: inline-flex; width: 40px; height: 40px; border-radius: 50%; background: #0095f6; color: #fff; font-size: 26px; align-items: center; justify-content: center; vertical-align: 6px; margin-left: 8px; }
    #root .hd { font-size: 32px; font-weight: 600; color: var(--sub); margin-top: 4px; }
    #root .fw { margin-top: 18px; font-size: 88px; font-weight: 800; letter-spacing: -.04em; line-height: .9; }
    #root .fw small { font-size: 30px; font-weight: 700; color: var(--sub); letter-spacing: 0; margin-left: 10px; }
    #root .lk { margin-top: 24px; display: inline-flex; align-items: center; gap: 12px; padding: 14px 26px; border-radius: 999px; background: var(--ink); color: var(--bg); font-size: 28px; font-weight: 700; }
    #root .lk b { color: var(--ac2); }
    /* ranking com adesivos que descolam */
    #root .rk { position: absolute; inset: 0; display: grid; gap: 18px; }
    #root .rk-c { position: relative; border-radius: 22px; background: var(--card); border: 2px solid rgba(127,127,127,.15); box-shadow: 0 14px 30px rgba(0,0,0,.14); }
    #root .rk-r { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px; padding: 14px; text-align: center; }
    #root .rk-r b { font-family: var(--disp); font-size: 30px; font-weight: 800; color: var(--ac); }
    #root .rk-r span { font-size: 29px; font-weight: 800; line-height: 1.05; letter-spacing: -.02em; }
    #root .rk-r img { width: 76px; height: 76px; object-fit: contain; }
    #root .rk-s { position: absolute; inset: -2px; border-radius: 22px; background: linear-gradient(150deg, var(--ac2), var(--ac)); display: flex; align-items: center; justify-content: center; font-family: var(--disp); font-size: 96px; font-weight: 800; letter-spacing: -.05em; color: %SOBRE_AC%; box-shadow: 0 10px 24px rgba(0,0,0,.22); transform-origin: 100% 100%; overflow: hidden; }
    #root .rk-s::after { content: ""; position: absolute; right: 0; bottom: 0; width: 46px; height: 46px; background: linear-gradient(135deg, rgba(255,255,255,0) 50%, rgba(255,255,255,.85) 50%); border-top-left-radius: 14px; box-shadow: -4px -4px 10px rgba(0,0,0,.15); }
    %CSS%
  </style>
  <div id="root" data-composition-id="%ID%" data-width="1080" data-height="1920">
%BODY%
  </div>
  <script>
    const tl = gsap.timeline({ paused: true });
    const IN = (sel, t, from = { y: 40 }) => tl.fromTo(sel, { opacity: 0, filter: "blur(12px)", ...from }, { opacity: 1, filter: "blur(0px)", y: 0, x: 0, scale: 1, rotation: 0, duration: 0.45, ease: "expo.out" }, t);
    const POP = (sel, t, st = 0.08) => tl.fromTo(sel, { opacity: 0, scale: 0.4, rotation: -12 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.55, ease: "back.out(1.7)", stagger: st }, t);
    const OUT = (sel, t) => tl.to(sel, { opacity: 0, y: -40, filter: "blur(12px)", duration: 0.25, ease: "power3.in" }, t);
    const UL = (sel, t) => tl.fromTo(sel, { "--u": 0 }, { "--u": 1, duration: 0.4, ease: "power3.out" }, t);
    const RISCO = (sel, t) => tl.fromTo(sel, { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: "power4.out" }, t);
    const BOLHA = (sel, t) => tl.fromTo(sel, { opacity: 0, scale: 0.6, y: 40 }, { opacity: 1, scale: 1, y: 0, duration: 0.5, ease: "back.out(1.7)" }, t);
    const PERFIL = (p, t) => {
      tl.fromTo(p + " .ph", { opacity: 0, x: -120, rotation: -8 }, { opacity: 1, x: 0, rotation: -3, duration: 0.6, ease: "expo.out" }, t);
      tl.fromTo(p + " .ph img", { y: 0 }, { y: -40, duration: 6, ease: "none" }, t);
      POP(p + " .avr", t + 0.12);
      IN(p + " .nm", t + 0.22, { x: 60 });
      IN(p + " .hd", t + 0.3, { x: 60 });
      IN(p + " .fw", t + 0.4, { scale: 0.6 });
      IN(p + " .lk", t + 0.55, { y: 30 });
    };
    const SAI = (p, t) => tl.to(p, { opacity: 0, x: -140, duration: 0.22, ease: "power3.in" }, t);
    // ranking: o adesivo nº n descola (dobra a ponta, levanta e voa) e o cartão cresce enquanto o item é falado
    const DESCOLAR = (p, n, t, dur = 1.6) => {
      const st = `${p}-s${n}`, c = `${p}-c${n}`;
      tl.to(st, { skewX: -8, scaleY: 0.94, rotation: -4, duration: 0.14, ease: "power2.out" }, t);
      tl.to(st, { x: 220, y: -260, rotation: -38, scale: 0.7, opacity: 0, duration: 0.5, ease: "power2.in" }, t + 0.14);
      tl.fromTo(c, { scale: 1, zIndex: 1 }, { scale: 1.12, zIndex: 5, duration: 0.3, ease: "back.out(2)" }, t + 0.1);
      tl.fromTo(`${c} .rk-r`, { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.3, ease: "expo.out" }, t + 0.2);
      tl.to(c, { scale: 1, duration: 0.35, ease: "power2.inOut" }, t + dur);
    };
    const ADESIVOS = (p, t) => tl.fromTo(`${p} .rk-c`, { opacity: 0, scale: 0.5, rotation: -10 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.45, ease: "back.out(1.8)", stagger: { each: 0.06, from: "end" } }, t);
%JS%
    window.__timelines["%ID%"] = tl;
  </script>
</template>
"""

def perfil(pid, k, nome, handle, seguidores, verificado=True, estilo=""):
    """Card de perfil do Instagram. Precisa de assets/ig/tela_<k>.jpg e av_<k>.png (ver capturar_perfil em referencias/pipeline.md)."""
    vf = '<span class="vf">✓</span>' if verificado else ""
    return f"""    <div id="{pid}" style="position:absolute;inset:0;{estilo}">
      <div class="ph"><img src="assets/ig/tela_{k}.jpg" alt="" /></div>
      <div class="inf">
        <div class="avr"><img src="assets/ig/av_{k}.png" alt="" /></div>
        <div class="nm">{html.escape(nome)}{vf}</div>
        <div class="hd">@{handle}</div>
        <div class="fw">{seguidores}<small>seguidores</small></div>
        <div class="lk">🔗 <b>@{handle}</b></div>
      </div>
    </div>"""

def ranking(pid, itens, colunas=None, imagens=None, estilo=""):
    """Grade de adesivos numerados. itens: nomes do nº 1 ao nº N (até 10). imagens: {n: "assets/img/x.png"} opcional.
    No JS: ADESIVOS("#pid", t) para entrarem, DESCOLAR("#pid", n, t) quando o item n for falado."""
    n = len(itens); imagens = imagens or {}
    col = colunas or (5 if n > 6 else 3 if n > 4 else n)
    lin = -(-n // col)
    cards = []
    for i in range(n, 0, -1):   # mostra do maior para o menor (contagem regressiva), lendo da esquerda para a direita
        img = f'<img src="{imagens[i]}" alt="" />' if i in imagens else ""
        cards.append(f'<div id="{pid}-c{i}" class="rk-c"><div class="rk-r"><b>nº {i}</b>{img}<span>{html.escape(itens[i-1])}</span></div><div id="{pid}-s{i}" class="rk-s">{i}</div></div>')
    return f'<div id="{pid}" class="rk" style="grid-template-columns: repeat({col}, 1fr); grid-template-rows: repeat({lin}, 1fr);{estilo}">' + "".join(cards) + "</div>"

def recorte(cid, dur, escala=1.0, y=0, x=0, estilo=""):
    """A pessoa sem fundo (assets/video/recorte_<cid>.webm, gerado por recortar.py) ocupando a tela da cena.
    escala/x/y mexem no enquadramento (ex.: escala=0.82, y=260 = corpo inteiro mais embaixo). No JS, anime "#<cid>-rc" (o invólucro)."""
    return (f'<div id="{cid}-rc" style="position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:50% 100%;'
            f'transform:translate({x}px,{y}px) scale({escala});{estilo}"><video id="{cid}-rv" class="clip" data-start="0" data-duration="{round(dur, 3)}" '
            f'src="assets/video/recorte_{cid}.webm" muted playsinline style="position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover"></video></div>')

def cena(sid, t, css="", body="", js=""):
    sobre_ac = "#111" if t["acento"].lower() in ("#d4ff3a", "#ffd23f", "#2ee66b", "#ffaa21", "#cfad6d") else "#fff"
    return (HEAD.replace("%FONTES%", fontes_css(t)).replace("%VARS%", vars_css(t)).replace("%SOBRE_AC%", sobre_ac)
            .replace("%ID%", sid).replace("%CSS%", css).replace("%BODY%", body).replace("%JS%", js))

# ---------------------------------------------------------------- legendas
LEG_CSS = {
    "caixa": """#root .lg span { display: inline-block; padding: 12px 26px; border-radius: 20px; background: var(--ink); color: var(--bg); font-size: 50px; font-weight: 800; line-height: 1.15; letter-spacing: -0.02em; box-shadow: 0 12px 30px rgba(0,0,0,.3); white-space: nowrap; }
    #root .lg.full span, #root .lg.motion span { background: rgba(10,10,10,.72); color: #fff; }
    #root .lg i { font-style: normal; opacity: .38; }""",
    "solta": """#root .lg span { display: inline-block; color: #fff; font-size: 64px; font-weight: 800; line-height: 1.1; letter-spacing: -0.02em; text-shadow: 0 4px 20px rgba(0,0,0,.6); white-space: nowrap; }
    #root .lg.split span { color: var(--ink); text-shadow: none; font-size: 52px; }
    #root .lg i { font-style: normal; opacity: .35; }
    #root .lg i.on { color: var(--ac2); }""",
    "glow": """#root .lg span { display: inline-block; color: var(--ac2); font-size: 66px; font-weight: 900; line-height: 1.1; letter-spacing: -0.03em; text-transform: uppercase; text-shadow: 0 0 24px color-mix(in srgb, var(--ac) 60%, transparent), 0 4px 20px rgba(0,0,0,.6); white-space: nowrap; }
    #root .lg.split span { font-size: 52px; }
    #root .lg i { font-style: normal; opacity: .3; }""",
}

def _modo(t, segs):
    for a, b, k in segs:
        if a + 0.3 <= t < b:
            return {"p": "split", "f": "full", "m": "motion", "r": "motion"}[k]
    return "full"

def legendas(palavras, CENAS, t, inicio=0.0, fim=None, correcoes=None, max_palavras=3, sem_legenda=()):
    """palavras: [{text,start,end}] já na linha do tempo final. Retorna o HTML da composição de legendas."""
    correcoes = correcoes or {}
    segs = [(a, b, k) for a, b, k in CENAS.values()]
    ws = [w for w in palavras if w["start"] >= inicio - 0.05]
    if sem_legenda:   # tipos de cena onde o texto da tela já é a legenda (ex.: "m")
        ws = [w for w in ws if not any(a + 0.3 <= w["start"] < b and k in sem_legenda for a, b, k in segs)]
    def fix(txt):
        m = re.match(r"^(\W*)([\wÀ-ú%]+)(\W*)$", txt)
        return m.group(1) + correcoes.get(m.group(2), m.group(2)) + m.group(3) if m else txt
    grupos, cur = [], []
    for i, w in enumerate(ws):
        cur.append(w)
        nx = ws[i + 1] if i + 1 < len(ws) else None
        if (len(cur) >= max_palavras or w["text"].endswith((".", "?", "!", ",")) or nx is None
                or nx["start"] - w["end"] > 0.35 or _modo(nx["start"], segs) != _modo(cur[0]["start"], segs)):
            grupos.append(cur); cur = []
    linhas = []
    for gi, g in enumerate(grupos):
        s = g[0]["start"]
        e = grupos[gi + 1][0]["start"] if gi + 1 < len(grupos) else g[-1]["end"] + 0.3
        e = min(e, g[-1]["end"] + 0.6)
        pal = " ".join(f'<i data-t="{round(w["start"] - s, 2)}">{html.escape(fix(w["text"]))}</i>' for w in g)
        linhas.append(f'      <div id="lg{gi:03d}" class="clip lg {_modo(s, segs)}" data-start="{round(s, 2)}" data-duration="{round(max(e - s, 0.1), 2)}"><span>{pal}</span></div>')
    fim = fim or (ws[-1]["end"] + 1 if ws else 1)
    return f"""<template>
  <style>
    {fontes_css(t)}
    #root {{ {vars_css(t)} position: absolute; inset: 0; pointer-events: none; font-family: var(--sans); }}
    #root .lg {{ position: absolute; left: 100px; right: 160px; text-align: center; }}
    #root .lg.split {{ top: 815px; left: 90px; right: 90px; }}
    #root .lg.full, #root .lg.motion {{ top: 1290px; }}
    {LEG_CSS[t["legenda"]]}
    {"#root .lg.motion span { color: var(--ink); text-shadow: none; } #root .lg.motion i.on { color: var(--ac); }" if t["claro"] and t["legenda"] != "caixa" else ""}
  </style>
  <div id="root" data-composition-id="legendas" data-width="1080" data-height="1920">
{chr(10).join(linhas)}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    document.querySelectorAll("#root .lg").forEach((g) => {{
      const s = parseFloat(g.dataset.start);
      tl.fromTo(g.querySelector("span"), {{ opacity: 0, y: 14, scale: 0.92 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.14, ease: "power3.out" }}, s);
      g.querySelectorAll("i").forEach((w) => {{
        const tw = s + parseFloat(w.dataset.t);
        tl.fromTo(w, {{ opacity: 0.35 }}, {{ opacity: 1, duration: 0.08 }}, tw);
      }});
    }});
    tl.set({{}}, {{}}, {fim});
    window.__timelines["legendas"] = tl;
  </script>
</template>
"""

# ---------------------------------------------------------------- composição raiz
INDEX = """<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="%GSAP%"></script>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: %BG%; }
      #root { position: relative; width: 100%; height: 100%; }
      #bg { position: absolute; inset: 0; background: radial-gradient(90% 45% at 50% 22%, %BG% 0%, %BG% 50%, %BG2% 100%); }
      #bg-grid { position: absolute; left: 0; right: 0; top: 0; height: 900px; background-image: linear-gradient(%GRID% 1px, transparent 1px), linear-gradient(90deg, %GRID% 1px, transparent 1px); background-size: 60px 60px; }
      #cam { position: absolute; inset: 0; clip-path: inset(0px 0px 0px 0px round 0px); }
      #cam-in { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; transform-origin: 50% 0%; }
      #fala { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; object-fit: cover; }
      #cam-ring { position: absolute; left: 60px; top: 900px; width: 960px; height: 960px; border-radius: 56px; border: 4px solid %AC%; box-shadow: 0 30px 80px rgba(0,0,0,.25); opacity: 0; }
      #dim { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,.6) 0%, rgba(0,0,0,0) 42%, rgba(0,0,0,0) 62%, rgba(0,0,0,.45) 100%); opacity: 0; }
    </style>
  </head>
  <!-- Gerado por roteiro.py (Constancy Editor). Edite o roteiro e rode de novo; não edite este arquivo à mão. -->
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="%FIM%" data-width="1080" data-height="1920">
      <div id="bg"></div>
      <div id="bg-grid"></div>
      <div id="cam">
        <div id="cam-in">
          <video id="fala" class="clip" data-start="0" data-duration="%VDUR%" data-track-index="0" src="assets/video/fala.mp4" muted playsinline></video>
        </div>
      </div>
      <div id="cam-ring"></div>
      <div id="dim"></div>
%EXTRA%
%HOSTS%
      <div id="legendas" data-composition-id="legendas" data-composition-src="compositions/legendas.html" data-start="0" data-duration="%FIM%" data-track-index="2" data-track-kind="captions" data-width="1080" data-height="1920"></div>
      <audio id="mix" class="clip" data-start="0" data-duration="%FIM%" data-track-index="3" src="assets/audio/mix.wav"></audio>
    </div>
    <script>
      const tl = gsap.timeline({ paused: true });
      const SEGS = %SEGS%;
      const PUNCH = %PUNCH%;
      const FULL = { clipPath: "inset(0px 0px 0px 0px round 0px)" };
      const SPLIT = { clipPath: "inset(900px 60px 60px 60px round 56px)" };
      tl.set("#cam", { ...FULL, opacity: 1 }, 0); tl.set("#cam-in", { scale: 1, y: 0 }, 0); tl.set("#cam-ring", { opacity: 0 }, 0); tl.set("#dim", { opacity: 0 }, 0);
      let st = "o";   // o = vídeo cheio sem nada, f = cheio com textos, p = dividido, m = motion (vídeo escondido)
      const ir = (k, t) => {
        if (k === st) return;
        const io = { immediateRender: false };
        if (k === "p") {
          if (st === "m" || st === "r") tl.fromTo("#cam", { opacity: 0 }, { opacity: 1, duration: 0.3, ...io }, t);
          tl.fromTo("#cam", FULL, { ...SPLIT, duration: 0.6, ease: "power3.inOut", ...io }, t);
          tl.fromTo("#cam-in", { scale: 1, y: 0 }, { scale: %SS%, y: %SY%, duration: 0.6, ease: "power3.inOut", ...io }, t);
          tl.fromTo("#cam-ring", { opacity: 0 }, { opacity: 1, duration: 0.3, ...io }, t + 0.4);
          tl.to("#dim", { opacity: 0, duration: 0.2 }, t);
        } else if (k === "f" || k === "o") {
          if (st === "p") {
            tl.fromTo("#cam", SPLIT, { ...FULL, duration: 0.55, ease: "power3.inOut", ...io }, t);
            tl.fromTo("#cam-in", { scale: %SS%, y: %SY% }, { scale: 1, y: 0, duration: 0.55, ease: "power3.inOut", ...io }, t);
            tl.to("#cam-ring", { opacity: 0, duration: 0.15 }, t);
          }
          if (st === "m" || st === "r") tl.fromTo("#cam", { opacity: 0 }, { opacity: 1, duration: 0.35, ...io }, t);
          tl.to("#dim", { opacity: k === "f" ? 1 : 0, duration: 0.4 }, t + 0.2);
        } else if (k === "m" || k === "r") {
          if (st === "p") { tl.to("#cam-ring", { opacity: 0, duration: 0.15 }, t); }
          tl.to("#cam", { opacity: 0, duration: 0.35 }, t);
          tl.to("#dim", { opacity: 0, duration: 0.2 }, t);
          if (st === "p") { tl.set("#cam", FULL, t + 0.4); tl.set("#cam-in", { scale: 1, y: 0 }, t + 0.4); }
        }
        st = k;
      };
      let fimAnt = 0;
      SEGS.forEach(([a, b, k]) => { if (a - fimAnt > 0.05 && st !== "o") ir("o", fimAnt); ir(k, a); fimAnt = b; });
      if (%FIM% - fimAnt > 0.05) ir("o", fimAnt);
      PUNCH.forEach((t) => {
        tl.to("#cam-in", { scale: 1.08, duration: 0.15, ease: "power3.out" }, t);
        tl.to("#cam-in", { scale: 1, duration: 0.6, ease: "power2.inOut" }, t + 0.8);
      });
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""

def escrever(CENAS, S, t, palavras, fim, video_dur, punch=(), inicio_legendas=0.0, correcoes=None, extra_root="", pasta=".", sem_legenda=(), cam_split=(0.9, 620)):
    """cam_split = (escala, deslocamento y) do vídeo dentro do card da tela dividida. Pessoa de corpo inteiro e longe: (1.25, 378)."""
    """Escreve compositions/*.html, compositions/legendas.html e index.html.
    S[id] = dict(css=..., body=..., js=...).  punch = tempos de zoom rápido no rosto (só em cenas "f" ou fora de cenas)."""
    os.makedirs(os.path.join(pasta, "compositions"), exist_ok=True)
    for sid, d in S.items():
        open(os.path.join(pasta, "compositions", f"{sid}.html"), "w").write(cena(sid, t, d.get("css", ""), d.get("body", ""), d.get("js", "")))
    open(os.path.join(pasta, "compositions", "legendas.html"), "w").write(
        legendas(palavras, CENAS, t, inicio=inicio_legendas, fim=fim, correcoes=correcoes, sem_legenda=sem_legenda))
    segs = sorted([(a, b, k) for a, b, k in CENAS.values()])
    # punch só onde o rosto está em tela cheia e longe de trocas de layout
    ok = [p for p in punch if not any(a - 0.2 <= p <= b + 1.6 and k not in ("f",) for a, b, k in segs) and not any(abs(p + 1.4 - a) < 0.3 for a, b, k in segs)]
    hosts = "\n".join(f'      <div id="{sid}" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" data-start="{a}" data-duration="{round(b - a, 3)}" data-track-index="1" data-track-kind="graphics" data-width="1080" data-height="1920"></div>'
                      for sid, (a, b, k) in sorted(CENAS.items(), key=lambda x: x[1][0]))
    grid = "rgba(0,0,0,.045)" if t["claro"] else "rgba(255,255,255,.05)"
    out = (INDEX.replace("%GSAP%", GSAP).replace("%BG%", t["fundo"]).replace("%BG2%", t["fundo2"]).replace("%GRID%", grid)
           .replace("%AC%", t["acento"]).replace("%FIM%", str(round(fim, 3))).replace("%VDUR%", str(round(video_dur, 3)))
           .replace("%EXTRA%", extra_root).replace("%HOSTS%", hosts).replace("%SEGS%", json.dumps(segs)).replace("%PUNCH%", json.dumps(sorted(ok))).replace("%SS%", str(cam_split[0])).replace("%SY%", str(cam_split[1])))
    open(os.path.join(pasta, "index.html"), "w").write(out)
    print(f"ok: {len(S)} cenas, layout {len(segs)} trechos, estilo {t['id']} {t['nome']}")

def palavras(pasta="."):
    w = json.load(open(os.path.join(pasta, "assets", "transcript.json")))
    return w.get("words", w) if isinstance(w, dict) else w

def dur_video(pasta="."):
    return json.load(open(os.path.join(pasta, "assets", "fala.json")))["duracao"]
