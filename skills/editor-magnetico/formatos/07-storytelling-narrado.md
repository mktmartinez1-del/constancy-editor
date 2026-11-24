# 07 · Storytelling narrado

**Objetivo:** contar um acontecimento real com locução e imagens que sustentam a história.
**Duração típica:** 35–60 s. **Estilos que combinam:** 06, 04, 03.

## Mídias
| Papel | Obrigatório | O que é |
|---|---|---|
| `locucao` | sim | a narração (áudio ou vídeo) |
| `take1`, `take2`, ... | sim | imagens de cada momento da história (2–4 s cada) |
| `principal` | não | se a pessoa aparece falando em algum momento |

**Regras:** cada bloco da narração precisa de uma imagem enviada (peça o que faltar, pelo nome). Identifique reconstituições. Se a locução faltar, peça; nunca invente fala.

## Briefing
1. Tipo de relato: dia de trabalho, projeto, imprevisto, venda/investimento/economia, cliente, situação engraçada ou indefinido.
2. Começo, conflito, surpresa, solução, resultado, pessoas envolvidas e oferta.
3. Tem cliente na história? Anonimize e confirme a autorização.

## Se ainda vai gravar: 3 ângulos
Suspense · Humor de bastidor · Transformação/emoção/resultado real. Depois: principal + 3 versões com os mesmos fatos (variando o ponto de partida, o recorte ou a ordem). Inclua a locução completa e a lista de takes.

## Como a pessoa manda
- **Takes soltos** (um arquivo por momento) **ou já colados** num vídeo só, e **o áudio da narração** separado.
- Takes colados: use `cortes_de_cena` do preparar.py para achar cada take dentro do vídeo.
- Casa cada frase da narração com a imagem que mostra aquilo (pela transcrição da locução + o que aparece nos takes; olhe quadros de cada take). Se uma frase não tem imagem, use um texto/motion em tela cheia (`m`) em vez de inventar imagem.

## Receita de edição
| Trecho | Layout | O que acontece |
|---|---|---|
| 0–4 s | `f` | Abre pelo conflito (in media res), uma pausa curta de som. |
| volta | `f` | Volta à preparação: takes de 2–4 s em sequência guiados pela locução. |
| virada | `f` / `m` | A revelação com texto grande e silêncio de 0,3 s antes. |
| final | `f` | Resultado + CTA. |
- EDL: `"locucao": "locucao"` e segmentos com os takes `"mudo": true` (a voz vem da locução). A soma dos takes deve cobrir a duração da locução.
