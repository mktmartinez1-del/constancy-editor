#!/usr/bin/env python3
"""Gera galeria/index.html a partir de estilos/temas.json e das amostras em galeria/amostras/ (rode depois de adicionar estilos)."""
import html, json, os
SK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
t = {k: v for k, v in json.load(open(os.path.join(SK, "estilos", "temas.json"))).items() if not k.startswith("_")}
F = [("01","Dica de valor","Ensinar uma ação que o público consegue repetir","o vídeo falando"),
("02","Dor e solução","Dor, consequência e como o seu produto resolve","o vídeo + a ideia e o produto"),
("03","React","Reagir a um vídeo, pausar no detalhe e analisar","a reação + o vídeo-fonte + perfis citados"),
("04","Comparativo","A ou B lado a lado, o público escolhe","os dois vídeos"),
("05","Trend com texto","Clipe curto com texto; a legenda cumpre a promessa","um clipe + a frase"),
("06","Lista e ranking","Adesivos numerados que descolam do nº 10 ao nº 1","o vídeo falando a lista"),
("07","Storytelling narrado","História real com narração e imagens","os takes + o áudio narrado"),
("08","Conexão real","Direto para a câmera, com legenda e B-roll","o vídeo mais longo")]
def card(k, v):
    a = os.path.join(SK, "galeria", "amostras", v["amostra"])
    claro = v["acento"].lower() in ("#d4ff3a", "#2ee66b", "#cfad6d", "#ffaa21", "#e8b04a")
    if os.path.exists(a + ".mp4"):
        media = f'<video src="amostras/{v["amostra"]}.mp4" poster="amostras/{v["amostra"]}.jpg" muted loop playsinline autoplay preload="metadata"></video>'
    else:
        media = (f'<div class="ph" style="background:linear-gradient(160deg,{v["fundo"]},{v["fundo2"]});color:{v["tinta"]}">'
                 f'<b style="color:{v["acento"]}">{html.escape(v["nome"])}</b><small>amostra em produção</small></div>')
    return (f'<article class="st">{media}<div class="meta"><span class="n" style="background:{v["acento"]};color:{"#111" if claro else "#fff"}">{k}</span>'
            f'<h3>{html.escape(v["nome"])}</h3><p>{html.escape(v["quando"])}</p></div></article>')
cards = "".join(card(k, v) for k, v in t.items())
fm = "".join(f'<li><b>{n}</b><div><h4>{a}</h4><p>{b}</p><p class="m">você manda: {m}</p></div></li>' for n, a, b, m in F)
page = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Editor Magnético</title>
<style>
:root{{--bg:#120904;--card:#1f130b;--ink:#fff7ef;--sub:#c9b5a3;--ac:#ff7900;--line:rgba(255,247,239,.1)}}
@media (prefers-color-scheme: light){{:root:not([data-theme="dark"]){{--bg:#fff7ef;--card:#ffffff;--ink:#170a04;--sub:#7a6a5c;--line:rgba(23,10,4,.1)}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:40px 16px 80px}}
header h1{{font-size:clamp(32px,5vw,54px);margin:0;letter-spacing:-.03em}}header h1 em{{font-family:Georgia,serif;font-weight:400;color:var(--ac)}}
header p{{color:var(--sub);max-width:640px;margin:10px 0 0}}
.steps{{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0 8px}}.steps span{{padding:8px 14px;border-radius:999px;border:1px solid var(--line);font-size:14px}}.steps span b{{color:var(--ac)}}
h2{{font-size:24px;margin:44px 0 6px;letter-spacing:-.02em}}h2+p{{color:var(--sub);margin:0 0 18px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px}}
.st{{background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden}}
.st video,.st .ph{{width:100%;aspect-ratio:9/16;object-fit:cover;display:block;background:#000}}
.ph{{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;text-align:center;padding:16px}}.ph b{{font-size:22px;font-style:italic}}.ph small{{opacity:.6}}
.meta{{padding:12px 14px 16px}}.meta h3{{margin:8px 0 4px;font-size:17px}}.meta p{{margin:0;color:var(--sub);font-size:13.5px}}
.n{{display:inline-block;font-weight:800;font-size:13px;padding:3px 9px;border-radius:999px}}
ol{{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}}
li{{display:flex;gap:14px;align-items:flex-start;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px}}
li b{{font-size:22px;color:var(--ac);min-width:30px}}li h4{{margin:0 0 2px;font-size:17px}}li p{{margin:0;color:var(--sub);font-size:14px}}li p.m{{margin-top:6px;color:var(--ink);font-size:13px}}
footer{{margin-top:48px;color:var(--sub);font-size:13px}}
</style></head><body><main>
<header><h1>Editor <em>Magnético</em></h1><p>Escolha primeiro o estilo, depois o formato, e responda no Claude digitando o número. O Claude edita o vídeo no seu computador.</p>
<div class="steps"><span><b>1</b> estilo</span><span><b>2</b> formato</span><span><b>3</b> música e ritmo</span><span><b>4</b> envie o vídeo</span><span><b>5</b> receba o MP4</span></div></header>
<h2>1 · Estilos</h2><p>Amostras sem som. Nos estilos com gravação, o vídeo alterna você em tela cheia, tela dividida e você sem fundo com o título atrás.</p>
<div class="grid">{cards}</div>
<h2>2 · Os 8 formatos da Copy Magnética</h2><p>Cada formato tem a própria mecânica de edição.</p><ol>{fm}</ol>
<footer>Método Constancy · Copy Magnética AI. Fontes OFL, ícones 3dicons (CC0) e efeitos sonoros CC0.</footer>
</main></body></html>'''
open(os.path.join(SK, "galeria", "index.html"), "w").write(page)
print("ok: galeria com", len(t), "estilos")
