# Guia de Estilo — Editor de Vídeo

Base de estilo do Constancy Editor.
**Regra:** todo vídeo editado aqui segue este guia, salvo pedido diferente seu.
A parte 10 descreve cada referência sozinha e é a base do futuro **catálogo de estilos**.

---

## 1. O DNA comum (o que as 10 referências têm em comum)

1. **Uma ideia por tela.** Cada momento mostra uma frase curta, uma palavra-chave ou um objeto. Nunca um parágrafo.
2. **O texto é o motion.** As palavras faladas viram tipografia animada (texto cinético). A legenda não é rodapé, é o elemento principal da cena.
3. **Contraste de pesos na mesma frase.** Palavra de apoio pequena e leve + palavra-chave enorme e pesada (ex.: "You're not *competing* on **price.**").
4. **Uma cor de destaque só.** Fundo neutro (branco, creme ou quase preto) + 1 cor viva de acento. Nada de arco-íris.
5. **Metáfora visual literal.** O que é dito aparece como objeto: "cérebro" → cérebro 3D; "estrutura" → coluna grega; "esconde o problema" → lupa; "sucesso" → troféu.
6. **Movimento contínuo.** A tela nunca fica parada. Mesmo sem corte, sempre tem algo entrando, girando, desfocando ou dando zoom lento.
7. **Som em cada movimento.** Whoosh, click, pop e impacto acompanham cada entrada de texto e objeto, sobre uma trilha de fundo baixa.
8. **Gancho em até 1 s, CTA no final.** Começa com a palavra mais forte em tela ("ATENÇÃO", "Attention", "2027") e termina com logo, @ ou "comente X".

---

## 2. Formato técnico (saída)

| Item | Padrão |
|---|---|
| Proporção | 9:16 vertical, **1080×1920** |
| Frame rate | **30 fps** (padrão). **60 fps** só em motion design puro, onde a fluidez aparece (refs 01, 03 e 04 são 60) |
| Codec de entrega | H.264 High, yuv420p, AAC 48 kHz, ~16–20 Mbps |
| Cor | SDR Rec.709. Gravação de iPhone em HDR (HLG/Dolby Vision) → converter para SDR |
| Loudness | **-14 LUFS** integrado (todas as refs medem -14,1 a -14,9), pico real ≤ -1 dBTP |
| Duração | 15–35 s é o padrão (8 das 10 refs). Até 2:20 só no formato "explicação/tutorial"  |

---

## 3. Ritmo e cortes

Medido nas referências:

| Tipo de vídeo | Troca de cena | Exemplo |
|---|---|---|
| Talking head + motion (energético) | a cada **0,9–2,5 s** (mediana 2,2 s) | ,  |
| Motion design com narração | troca **visual** a cada 1–1,5 s, **corte seco** raro (3–7 s) | , 05, 06, 07 |
| Teaser/intro sem fala | cena inteira em 7–15 s, com 1–2 "beats" fortes | ,  |
| Explicação longa (camadas) | layout muda a cada 3–6 s, legenda troca a cada palavra |  |

Regras:
- **O ritmo é dado pela fala, não pelo corte.** O conteúdo muda a cada frase (≈ 1–2 s) mesmo quando o plano continua o mesmo.
- **Cortar todos os silêncios e respirações** da fala (jump cut). Velocidade de fala de 2,2 a 3,8 palavras/s.
- Transições preferidas, nesta ordem:
  1. **Match / morph:** um elemento vira o próximo (ícone → app → logo).
  2. **Whip com motion blur:** a câmera passa rápido e o texto sai borrado .
  3. **Desfoque de entrada/saída** (blur 20 → 0 px) no texto e no fundo.
  4. **Vidro canelado** (fluted glass, faixas verticais) como "wipe" especial: 1 por vídeo no máximo .
  5. **Zoom de ênfase** no rosto (+8–15%) na palavra importante.
- **Proibido:** transições prontas genéricas (cubo, página virando, estrela), dissolve longo.

---

## 4. Enquadramento e layout

### Zonas seguras do Instagram (obrigatório)
- Nada importante nos **250 px de cima** nem nos **420 px de baixo**.
- **Coluna direita de 160 px** livre a partir de y≈1000 (ícones de curtir/comentar/compartilhar).
- Títulos começam em **y ≥ 280**. Legenda centralizada em **x≈500**, **y≈1420**, largura máx. ≈ 820 px.

### Quatro layouts que se repetem
| Layout | Como é | Refs |
|---|---|---|
| **A. Tela cheia de motion** | Sem pessoa. Fundo liso ou com gradiente sutil, objeto/ícone 3D no centro, texto acima ou abaixo | 01, 04, 05, 06, 07, 09 |
| **B. Rosto em card** | Pessoa recortada num card de cantos arredondados (raio ~40 px, borda fina colorida de 2–3 px) na metade de baixo, título na metade de cima | 03 |
| **C. Talking head com texto sobre o corpo** | Pessoa em tela cheia, texto cinético grande na altura do peito/rosto, com glow | 08, 10 |
| **D. Pessoa como personagem** | Pessoa em pé ou sentada sob um spot de luz, ambiente escuro, texto flutuando acima | 09 |

- Rosto do apresentador: olhos no **terço superior** do quadro (B: dentro do card; C: y≈600–750).
- **Avatar-bolha:** quando o motion ocupa a tela, o rosto continua presente num **círculo de ~200 px** num canto superior com borda colorida . Mantém a conexão com quem fala.
- Mockups de interface (celular, chat, busca, perfil do Instagram) são recriados limpos e entram **inclinados em 3D** (rotação de 10–25°) com sombra suave.
- Elementos de "HUD" leves dão acabamento: cantoneiras de câmera nas bordas, "● REC", números de seção ("01", "06/10"), linhas-guia finas.

---

## 5. Tipografia

### Sistema de duas fontes (o padrão de todas as refs)
| Papel | Estilo | Fontes gratuitas equivalentes |
|---|---|---|
| **Principal** (títulos, palavras-chave, legenda) | Sans geométrica/grotesca, **Bold–Black**, espaçamento entre letras levemente apertado (-2% a -4%) | **Inter Tight**, **Manrope**, **Plus Jakarta Sans**, **Satoshi**, **Sora** |
| **Contraste** (1 palavra por frase) | Serifa **itálica** elegante, peso regular | **Instrument Serif Italic**, **Playfair Display Italic**, **DM Serif Display Italic** |
| **Impacto** (opcional, palavra de choque) | Condensada pesada em CAIXA ALTA | **Anton**, **Bebas Neue**, **Oswald Bold** |
| **Detalhe técnico** (opcional) | Monoespaçada pequena, para "código", rótulos e HUD | **JetBrains Mono**, **IBM Plex Mono** |

### Regras
- Palavra-chave: **140–220 px** de altura. Palavra de apoio: **40–60 px**. A diferença de tamanho é de no mínimo **3×**.
- A serifa itálica entra na palavra emocional ou de ironia: *spends*, *competing*, *continua*, *inteiro*, *disso*, *profissão?*.
- No máximo **2 linhas** por tela, **1–4 palavras** por linha.
- Alinhamento centralizado por padrão. Escalonado (uma palavra mais à esquerda, a seguinte mais à direita) para dar dinâmica .
- Ponto final colorido na cor de acento: "price**.**", "value**.**", "pay**.**" .
- Riscar a palavra errada com um traço vermelho animado ("~~Content~~ is failing", ). Circular a palavra-chave com um traço desenhado à mão .

---

## 6. Cores

### Estrutura
- **60% fundo neutro** + **30% texto neutro** (preto ou branco) + **10% acento**.
- Fundos claros: branco puro a gelo `#F4F4F2`–`#FFFFFF`, ou creme `#F7EDE2`.
- Fundos escuros: quase preto com leve tom `#05060C`–`#101010`, com **gradiente radial** ou spot de luz no centro (nunca preto chapado).
- **Glow** suave na cor do acento em textos sobre fundo escuro (blur 20–40 px, 40–60% de opacidade).

### Paletas medidas nas referências (escolher UMA por vídeo)
| Nome | Fundo | Acento | Texto | Ref |
|---|---|---|---|---|
| Verde clean | `#FFFFFF` | `#2ABD20` | `#111111` | 01 |
| Roxo noturno | `#05060C` → `#171B39` | `#6D70EC` / `#7C5CFF` | `#F8F9FC` | 03 |
| Ouro premium | `#080500` → `#35240C` / creme `#F7EDE2` | `#CFAD6D` | `#FFFFFF` | 04 |
| Editorial vermelho e verde | `#D8DADA` (cinza claro) | `#C8102E` + `#0E7A4F` | `#1A1A1A` | 05 |
| Papel e vinho | `#F2F2F0` | `#8B1A1A` | `#1A1A1A` | 06 |
| Cobalto | `#010407` → `#0B1A4A` / `#F4F4F4` | `#2B3FE0` | `#FFFFFF` | 07 |
| Lima elétrico | `#050605` / footage escuro | `#D4FF3A` (texto `#ECFEB3` com glow) | `#FFFFFF` | 09, 10 |
| Azul tech | `#000000` → `#0A1A5C` | `#1E4BFF` | `#FFFFFF` | 02 |

- **Padrão quando não houver marca:** *Roxo noturno* para conteúdo educacional e *Lima elétrico* para conteúdo de vendas/negócios.
- Para a marca Constancy, use `#FF7900` / `#FFAA21` sobre `#170A04`, com a fonte Manrope.
- Footage de pessoa: grade levemente dessaturado e com contraste alto, sombras profundas e pele natural. O acento colorido vem dos gráficos, não da imagem.

---

## 7. Animações (vocabulário de movimento)

### Curvas e tempos
- Entradas: **ease-out forte** (`expo.out` / `power4.out`), **0,35–0,6 s**.
- Saídas: **ease-in** rápido, **0,2–0,3 s**, ou continuar o movimento para fora da tela.
- Objetos com "peso": **spring** com leve overshoot (`back.out(1.4)`).
- Sempre adicionar **motion blur** em movimentos rápidos (ou desfoque direcional de 10–30 px).

### Os 12 movimentos que mais aparecem
1. **Palavra por palavra:** cada palavra entra no tempo exato da fala (subindo de y+30 px, opacidade 0→1, blur 12→0). *Base de tudo.*
2. **Blur-in:** texto nasce desfocado e entra em foco .
3. **Escala com glow:** palavra-chave entra de 85% → 100% com flash de brilho .
4. **Troca de palavra no mesmo lugar:** "price" sai desfocando e "value" entra no mesmo ponto .
5. **Traço desenhado:** círculo, sublinhado ou risco que se desenha em 0,4 s (trim path).
6. **Pílulas/chips empilhando:** listas viram tags arredondadas que entram uma a uma, alternando cheia e contorno .
7. **Objeto 3D girando** devagar (5–15°/s) enquanto o texto conversa com ele: celular, logo, troféu, coluna.
8. **Câmera viva:** zoom lento contínuo de 100 → 108% em cada cena e pequenos drift/parallax entre camadas.
9. **Cursor simulado:** mãozinha ou seta que clica, digita na busca ou aperta "enviar" .
10. **Mockup que digita:** chat ou busca com texto aparecendo letra por letra e balões entrando .
11. **Revelação por máscara:** texto surge de trás de uma linha ou de um objeto (: "ATENÇÃO" saindo do sino).
12. **Gráfico que se desenha:** linhas, barras e ondas sonoras animadas acompanhando o que é dito .

### Elementos decorativos (com moderação)
- Partículas e brilhos (✦, +, ×) na cor de acento, piscando .
- Círculos/arcos finos girando ao fundo .
- Textura de papel, rabiscos de rascunho e anotações técnicas .
- **Máximo de 2 decorações** por cena.

---

## 8. Legendas

O padrão das refs: **legenda dinâmica integrada ao motion**, não legenda de TV.

| Item | Padrão |
|---|---|
| Unidade | **1 palavra por vez**  ou **grupo de 2–4 palavras**  |
| Posição | Faixa central-baixa, **y≈1420** (layout B: logo abaixo do topo do card; layout C: altura do peito) |
| Fonte | Sans Bold, **64–80 px**, branca, sombra suave (0 4 20 rgba(0,0,0,.45)), sem caixa de fundo |
| Destaque | Palavra-chave em **cor de acento** ou em **serifa itálica CAIXA ALTA** ("CÂMERA", "ÊNFASE", "CÓDIGO") |
| Animação | Pop: escala 90→100% + opacidade em 0,12 s. A palavra entra exatamente quando é falada |
| Sincronia | Timestamps por palavra do Whisper large-v3 (`--language pt`), revisados à mão |
| Texto | Corrigir erros do Whisper, sem pontuação final, números em algarismos ("3.500", "2027") |

- Quando o motion já mostra a palavra grande na tela , **a legenda some** para não repetir.
- Gerar `.srt` também, para acessibilidade, mesmo quando a legenda estiver queimada no vídeo.

---

## 9. Som

Visto no espectrograma: todas as refs têm **dezenas de transientes** (efeitos) sobre a trilha.

| Camada | Padrão |
|---|---|
| **Voz** | Principal. Limpa (isolada de ruído), comprimida, -14 LUFS no mix final, cortes sem respiração |
| **Trilha** | Eletrônica/ambiente minimalista, sem vocal, **-20 a -26 dB abaixo da voz** (ducking). Sem voz: a trilha sobe |
| **Efeitos (SFX)** | **1 som por evento visual:** whoosh (transição), click/tick (texto ou chip), pop (palavra-chave), swipe/riser (antes da revelação), impact/boom (palavra de choque), digitação (mockup), "ding" (check/sucesso) |
| **Densidade** | ~1 SFX a cada 0,5–1,5 s. A  diz usar "193 sons" em 2:20 |
| **Silêncio dramático** | 0,3–0,5 s de corte total de som antes da frase mais importante  |
| **Final** | Impacto + cauda de reverb no logo ou CTA |

- O som não pode chamar mais atenção que a voz. Os SFX ficam entre -18 e -10 dB.
- Os cortes caem **no beat** da trilha quando não há fala.

---

## 10. Os 15 estilos do catálogo

| # | Estilo | Paleta (fundo · acento) | Fontes | Quando usar |
|---|---|---|---|---|
| 01 | **Clean Minimal** | `#ffffff` · `#2abd20` | Inter + Playfair Display itálico | educacional leve, dicas, listas; visual limpo e claro |
| 02 | **Neon 3D Tech** | `#000000` · `#1e4bff` | Inter + Playfair Display itálico | tecnologia, apps, lançamentos; pouca fala |
| 03 | **Bolo de Camadas** | `#05060c` · `#7c5cff` | Inter + Playfair Display itálico | explicação longa, tutorial, fala + gráficos (precisa de gravação) |
| 04 | **Ouro Premium** | `#080500` · `#cfad6d` | Montserrat + Playfair Display itálico | alto padrão, mentoria, finanças, luxo |
| 05 | **Editorial com Objetos** | `#d8dada` · `#c8102e` | Montserrat + Playfair Display itálico | opinião, notícia, provocação; manchetes fortes |
| 06 | **Papel e Rascunho** | `#f2f2f0` · `#8b1a1a` | Inter + Playfair Display itálico | processo, bastidor, raciocínio, storytelling |
| 07 | **Cobalto Apps** | `#010407` · `#2b3fe0` | Inter + Playfair Display itálico | ferramentas, IA, automação, CTA de comentário |
| 08 | **Talking Head + Painéis** | `#0b0d0c` · `#2ee66b` | Inter + Playfair Display itálico | fala para câmera com dados e painéis (precisa de gravação) |
| 09 | **Spotlight Cinema** | `#050605` · `#d4ff3a` | Inter + Playfair Display itálico | trend curta, frase de impacto, pouca fala (precisa de gravação) |
| 10 | **Kinetic Lima** | `#050605` · `#d4ff3a` | Inter + Playfair Display itálico | talking head energético, vendas, negócios (precisa de gravação) |
| 11 | **Tela Dividida Editorial** | `#fff7ef` · `#ff7900` | Manrope + Instrument Serif itálico | talking head com prints, perfis, provas e números; o mais versátil (precisa de gravação) |
| 12 | **Editorial Vermelho Recortado** | `#efeeee` · `#d0021b` | Inter + Playfair Display itálico | apresentação pessoal, autoridade, marca pessoal; a pessoa sem fundo com títulos vermelhos enormes atrás (precisa de gravação) |
| 13 | **UI Glass Laranja** | `#f1f1f1` · `#ff5a1f` | Inter + Playfair Display itálico | apresentar produto, sistema, app ou serviço; cartões de vidro, telas e ícones em 3D |
| 14 | **Dark Kinetic Tipográfico** | `#0b0b0d` · `#ff5a1f` | Inter + Playfair Display itálico | ideia, opinião, bastidor de processo; texto cinético com palavras em destaque, cursor e telas |
| 15 | **Avatar Dourado** | `#070605` · `#e8b04a` | Inter + Playfair Display itálico | talking head premium: pessoa em card inclinado com brilho dourado, órbita de palavras, recorte com texto atrás (precisa de gravação) |

Amostras em `galeria/amostras/`; cenas de exemplo em `estilos/sNN.html` (01–10); movimentos dos estilos 12–15 e o arco dinâmico em `estilos/movimentos.md`.

## 11. Estrutura padrão de um vídeo

1. **Gancho (0–2 s):** palavra ou número gigante + pergunta ou afirmação forte. Movimento já no quadro 1.
2. **Problema (2–8 s):** 2–3 frases curtas, cada uma com uma metáfora visual.
3. **Virada (8–15 s):** "não é X, é Y". Troca de palavra no mesmo lugar e silêncio dramático antes.
4. **Prova/explicação (15–30 s):** mockups, gráficos e listas em chips.
5. **CTA (últimos 2–4 s):** "comente PALAVRA", @ ou logo, com impacto sonoro. A palavra do CTA fica na cor de acento.

---

## 12. Checklist antes de exportar

- [ ] Gancho visual no 1º quadro, sem tela preta no início
- [ ] Silêncios e respirações cortados
- [ ] Toda fala tem legenda/texto sincronizado por palavra, revisado
- [ ] Uma paleta só, uma cor de acento, no máximo 2 famílias de fonte (+ mono opcional)
- [ ] Nenhuma cena parada mais de 1,5 s sem movimento
- [ ] Zonas seguras do Instagram respeitadas em todos os quadros
- [ ] SFX em cada entrada importante, trilha com ducking sob a voz
- [ ] -14 LUFS, pico ≤ -1 dBTP
- [ ] 1080×1920, H.264, SDR, 30 fps (ou 60 no motion puro)
- [ ] Exportado com `renderizar.py final` (vai para ~/Constancy-Videos/exportacao)
