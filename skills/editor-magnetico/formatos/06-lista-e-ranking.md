# 06 · Lista e ranking

**Objetivo:** organizar itens em contagem regressiva, guardando o mais forte para o nº 1.
**Duração típica:** 25–45 s. **Estilos que combinam:** 01, 05, 07, 11.

## Mídias
| Papel | Obrigatório | O que é |
|---|---|---|
| `principal` | sim | abertura + fala dos itens (pode ser um take só) |
| `item1`, `item2`, `item3`... | não | um take por item mostrando a ação |
| `fechamento` | não | CTA |

**Regra:** cada número aparece junto com o take e a fala dele. Em passos que dependem um do outro, mantenha a ordem certa.

## Briefing
1. Tipo de lista: favoritos, checklist, erros, gastos/preços/economia, ranking sincero e engraçado ou indefinido.
2. Os itens e os valores reais (quando houver números).

## Se ainda vai gravar: 3 listas numeradas
Curiosidade · Custo/economia com dados reais · Ranking cômico sincero. Depois: principal + 3 versões com headline, contagem, comentário curto por item, ação visual, nº 1 e CTA.

## Mecânica visual: adesivos que descolam
A pessoa grava um vídeo parado falando a lista (ex.: "as 10 melhores localizações de Orlando", começando pela 10ª).
- No começo, todos os itens aparecem como **adesivos numerados lado a lado** (grade 5×2 para 10, 3×2 para 6, 3 em linha para 3), no painel de cima.
- A cada item falado, o adesivo daquele número **descola** (dobra e voa) e revela o nome do item (e uma foto/ícone, se houver) no tempo exato da fala; esse cartão cresce um pouco enquanto ela fala dele.
- Os itens já revelados ficam abertos; o nº 1 é o último e o mais enfático (impacto, cor de acento, zoom no rosto).
- Use `ranking(pid, itens)` no body e `DESCOLAR(pid, n, t)` no JS (cenas_base.py). Itens em ordem de 1 a N; os nomes vêm da fala (corrija a grafia).
- Adapte: lista de preços vira etiqueta de preço; "erros" podem ganhar um X vermelho; ranking engraçado pode ter emoji/ícone.

## Receita de edição
| Trecho | Layout | O que acontece |
|---|---|---|
| 0–4 s | `f` | Headline + promessa do nº 1 ("o nº 1 ninguém faz"). |
| cada item | `p` | Cartela grande com o número (nº 3 → nº 2 → nº 1) entrando com impacto, título do item em 1–3 palavras, ícone. Troca de cartela no tempo exato da fala. |
| nº 1 | `p` → `f` | Mais tempo e mais ênfase (zoom, cor de acento, som de impacto). |
| final | `f` | "Salva essa lista" / "comenta PALAVRA". |
