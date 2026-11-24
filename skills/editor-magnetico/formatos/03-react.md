# 03 · React

**Objetivo:** reagir a um vídeo-fonte, explicar um detalhe e entregar uma análise.
**Duração típica:** 30–90 s (o que a fala pedir). **Estilos que combinam:** 11, 08, 10.

## Mídias
| Papel | Obrigatório | O que é |
|---|---|---|
| `principal` | sim | a reação. Muitas vezes já vem montada (fonte em cima + pessoa embaixo nos primeiros segundos) |
| `fonte` | se não estiver dentro da principal | o clipe original, com direito de uso |
| `demo` | não | demonstração do jeito certo |
| prints de perfil | não | quando a pessoa cita alguém, capture o perfil (ver pipeline.md → perfis do Instagram) |

**Regra:** guarde o tempo da pausa na fonte e na linha do tempo. Sem fonte autorizada, peça outra ou ofereça uma simulação própria identificada como simulação.

## Briefing
1. Assunto e oferta.
2. Link, arquivo ou descrição do vídeo-fonte. Se não der para acessar: a sequência visual e as falas.
3. Quem é citado no vídeo? (Peça os links dos perfis para mostrar na tela.)

## Se ainda vai gravar
Com a fonte escolhida: React principal + 3 versões, cada uma com headline, reação falada, **ponto exato da pausa**, análise no quadro, enquadramento e CTA.

## Receita de edição
| Trecho | Layout | O que acontece |
|---|---|---|
| abertura | original | Se a principal já tem o react montado no começo, **não mexa**: deixe rodar (INICIO = fim desse trecho; ache o corte com `cortes_de_cena` do preparar.py). Se não tem, monte: fonte em cima e pessoa embaixo (cena `p` com `<video>` da fonte no painel) e headline no 1º quadro. |
| pausa | `p` | Congele a fonte no quadro do detalhe (`{"midia":"fonte","congelar":T,"dur":1.5}` no EDL ou imagem no painel) e destaque o ponto (círculo, seta, zoom). |
| análise | `p` / `f` | Prioridade à voz. Quando cita uma pessoa: perfil real dela no painel de cima (print + foto + seguidores + @), no segundo exato do nome. Números citados viram chips que aparecem na hora da fala. |
| final | `f` | CTA (palavra para comentar) com caixa de comentário digitando a palavra, e encerramento com @ da pessoa. |
- Música só depois do trecho original (`--inicio-musica INICIO`).
