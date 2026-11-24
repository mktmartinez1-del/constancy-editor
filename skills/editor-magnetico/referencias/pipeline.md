# Pipeline técnico

`M` = pasta `motor/` desta skill. `P` = pasta do projeto (`~/Constancy-Videos/projetos/AAAA-MM-DD_nome`). Rode tudo com `python3`.
Comandos longos (preparar com vídeo grande, render) vão em segundo plano.

## 1. Preparar
```
python3 M/preparar.py P principal=/caminho/video.mov [fonte=...] [a=... b=...] --estilo NN
```
- Converte para SDR 1080×1920 30 fps (HDR do iPhone: zscale ou `avconvert` no Mac), extrai áudio, transcreve (Parakeet; cai para Whisper large-v3), detecta cortes de cena.
- Imprime a transcrição com tempos. **Leia inteira** antes de planejar.
- Cria `P/roteiro.py` a partir do modelo.

## 2. Validar
Escreva `P/plano.json`: `{"formato":"03","estilo":"11","musica":"/caminho/ou nenhuma","cta":"NEUSA","ritmo":"dinamico|minimalista","titulo":"..."}` e rode `python3 M/validar.py P`. Se faltar mídia, peça **pelo nome do take** antes de seguir.

## 3. Montar (cortes)
- Vídeo já editado pela pessoa: não precisa de `edl.json`.
- Bruto com pausas: `{"cortar_pausas": 0.35, "remover": [[t0, t1]]}` (remova repetições/erros que você viu na transcrição).
- Vários takes / React com pausa / Storytelling: `segmentos` explícitos (ver docstring de `montar.py`).
```
python3 M/montar.py P
```
Imprime a transcrição **na linha do tempo final**: é com esses tempos que você escreve as cenas.

## 4. Roteiro (cenas)
Edite `P/roteiro.py` e rode `cd P && python3 roteiro.py`.
- `CENAS[id] = (início, fim, tipo)` com tipo `p` (tela dividida), `f` (tela cheia com texto) ou `m` (motion puro).
- Cada cena: `S[id] = dict(css=..., body=..., js=...)`. Tempos do `js` são **locais** (0 = início da cena).
- Helpers no JS: `IN(sel,t,from)`, `POP(sel,t)`, `OUT(sel,t)`, `UL(sel,t)` (sublinhado), `RISCO(sel,t)`, `BOLHA(sel,t)`, `PERFIL(sel,t)`, `SAI(sel,t)`.
- Classes: `.z` (área do painel na tela dividida: 940×530 a partir de y=275), `.zm` (área segura em motion/tela cheia), `.t` título, `.s` subtítulo, `.it` palavra em serifa itálica na cor de acento, `.ac` cor de acento, `.ul` sublinhado, `.pill`/`.pill.acp`, `.card`, `.bub` (balão de fala branco), `.ico` (ícone 3D), `.luz` (texto claro com sombra, para usar sobre o vídeo), `.num` (número gigante).
- Ícones: copie de `assets/icons/dynamic-color/` (ou `dynamic-premium/` para dourado) para `P/assets/img/` e use `assets/img/x.png`. Lista em `assets/icons/indice.json`.
- Cada elemento entra **no segundo exato da palavra** (pegue o tempo da transcrição). Uma ideia por tela; segure cada texto pelo menos 0,5 s + 0,3 s por palavra.
- Ranking: `ranking(pid, itens)` no body (itens do nº 1 ao nº N) e no JS `ADESIVOS("#pid", t)` para entrarem e `DESCOLAR("#pid", n, t)` no segundo em que o item n é falado.
- `PUNCH`: zoom rápido no rosto em palavras fortes (só tela cheia).
- `CORRECOES`: nomes próprios e palavras que a transcrição errou (ex.: `{"Nelza": "Neusa"}`).
- `CUES`: 1 efeito por evento visual (pop em chip/número, whoosh em troca de layout, tick em listas, notificação em "nova venda", digitar em caixa de comentário).

### Zonas seguras (Reels/TikTok)
Nada importante nos 250 px de cima nem nos 420 px de baixo; coluna direita de 160 px livre a partir de y≈1000. O `.z` e as legendas já respeitam isso; confira nos quadros.

### Perfis do Instagram (quando a pessoa cita alguém)
Peça os links. Abra cada perfil no navegador em tamanho de celular (375×812), feche o pop-up "Veja o perfil completo no app" e tire um print em escala 1 (750×1624). Salve como `P/assets/ig/<k>.jpg` e recorte:
```
ffmpeg -i <k>.jpg -vf "crop=196:196:42:142" P/assets/ig/av_<k>.png
ffmpeg -i <k>.jpg -vf "crop=750:1504:0:120" -q:v 2 P/assets/ig/tela_<k>.jpg
```
Confira o recorte do avatar olhando a imagem. Use `perfil(pid, k, nome, handle, seguidores, verificado)` no body e `PERFIL("#pid", t)` no JS. Use os números reais da página, com a data do print.
Se não houver navegador disponível, peça à pessoa um print do perfil.

## 4b. Pessoa sem fundo (cenas `r`)
```
python3 M/recortar.py P <id-da-cena> <início> <fim>
```
Gera `assets/video/recorte_<id>.webm` com transparência. No body da cena: fundo do estilo → título (fica atrás) → `recorte(id, dur)` → o que fica na frente. Anime o invólucro `#<id>-rc` (entrada subindo, leve zoom). Detalhes e enquadramento em `estilos/movimentos.md`.

## 5. Som
```
python3 M/mixar.py P --musica /caminho/musica.mp3 --inicio-musica 0      # ou --musica nenhuma
```
- Música enviada pela pessoa (qualquer formato de áudio ou vídeo). Fica ~10 dB abaixo da voz e abaixa sozinha quando há fala.
- Sem música da pessoa: `--musica nenhuma` (só voz + efeitos). Não baixe músicas da internet: o produto não tem licença para isso.
- React: `--inicio-musica` = fim do trecho original.
- Gosto do método: sem "braaam" de trailer, sem trilha agitada demais, **sem bipes, digitação ou sons de telefone**. Efeitos discretos: volume 0,08–0,18 na maioria (whoosh macio, vidro, ding de triângulo, plop); no máximo ~0,2 num impacto suave. Menos é mais: um efeito por troca de cena e por elemento importante, não por palavra.

## 6. Revisar e entregar
```
python3 M/renderizar.py P checar               # corrija todo ERRO; pese os avisos (zona segura, texto curto demais)
python3 M/renderizar.py P quadros 2,8.5,15,...  # olhe a folha de contato (Read na imagem)
python3 M/renderizar.py P final "titulo curto"  # MP4 em ~/Constancy-Videos/exportacao (+ _legenda.txt)
```
Revise pelo menos um quadro por cena: texto cortado, sobreposição, legibilidade, rosto coberto, zona segura.
Ajustes depois da entrega: só áudio mudou → rode `mixar.py` e troque a faixa sem renderizar de novo:
`ffmpeg -i video_v1.mp4 -i P/assets/audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest video_v2.mp4`.

## Problemas comuns
- `npx` pede rede na 1ª vez: normal. `hyperframes doctor` mostra o que falta.
- Transcrição falhou: `npx --yes hyperframes@0.9.81 models install parakeet`.
- Cores lavadas em vídeo de iPhone no Windows/Linux: o FFmpeg precisa do filtro `zscale` (instalador do Windows já baixa um FFmpeg completo).
