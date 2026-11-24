# Movimentos de cada estilo novo (12–15)

Leia a ficha do estilo escolhido antes de escrever as cenas. Cores e fontes vêm de `temas.json`; aqui está o vocabulário de movimento.

## Arco dinâmico (padrão para quem manda vídeo falando)
Varie o layout para o vídeo nunca ficar igual por mais de ~6 s:
1. **Começo com a pessoa** em tela cheia (`f`): gancho grande sobre o rosto, zoom de ênfase.
2. **Tela dividida** (`p`): o assunto vira motion em cima, a pessoa no card embaixo.
3. **Pessoa sem fundo** (`r`): a pessoa recortada sobre o fundo do estilo, com o título enorme **atrás da cabeça** (texto entre o fundo e a pessoa).
4. Volta ao rosto (`f`) ou a um motion puro (`m`) para respirar, e repete o ciclo com outro assunto.
5. Final em `f` ou `r` com o CTA.
Regras do recorte: rode `recortar.py` só nos trechos `r` (leva ~2–3 s por segundo). Use `recorte(id, dur)` com escala 1 em vídeo de meio corpo (escala < 1 mostra as bordas cortadas do corpo); escala 0,8–0,9 só se a pessoa estiver de corpo inteiro com espaço em volta. Para o texto ficar atrás da cabeça, posicione o título por volta de y = 450–650 (onde fica a cabeça) e coloque o `recorte(...)` **depois** do título no body.
**Antes, olhe um quadro do recorte e ache o topo da cabeça.** Se a cabeça estiver alta (boné, touca, cabelo volumoso, pessoa perto da câmera), suba o título para terminar logo acima ou no topo da cabeça: só a base das letras passa por trás. Título que some atrás da cabeça não serve. Textos complementares vão na frente do corpo (y ≈ 1150, antes da legenda em 1290).

## 12 · Editorial Vermelho Recortado
- Fundo claro liso (cinza-gelo) com leve luz radial; a pessoa recortada no centro.
- Títulos em **Inter Black itálico, caixa alta**, com degradê vermelho (`background: linear-gradient(180deg, var(--ac2), var(--ac)); -webkit-background-clip: text; color: transparent`), entrando com escala e borrão; palavra de apoio pequena em itálico cinza acima ("my name is" → **NOME**).
- **Pixels vermelhos** (quadradinhos de 30–40 px) piscando em `steps(3)` nos cantos e em volta do texto; glitch rápido na troca de palavra.
- **Cartões de foto** com borda vermelha e cantos arredondados entrando inclinados ao lado da pessoa (prints, fotos de clientes, perfis), etiqueta vermelha com o nome.
- Mockup de celular com conteúdo dentro quando falar de redes/app.
- Som: clique/glitch nos pixels, pop nos cartões, impacto seco no título.

## 13 · UI Glass Laranja (produto, sistema, serviço)
- Fundo cinza muito claro com círculos e arcos finos; troca para **cena escura** (preto com brilho laranja) e para **cena laranja chapada** nos momentos de virada.
- **Pílulas de vidro** brancas com ícone de linha laranja + palavra (ex.: reservas, financeiro, compras) entrando em cascata e girando em perspectiva 3D (`rotationY`, `rotationX`), depois orbitando em volta do logo/ícone central.
- **Telas do produto** (prints que a pessoa mandar) em cartões inclinados 15–25°, com sombra suave; um cartão laranja com o número grande ("35%").
- Linha do tempo com bolinhas numeradas (1 → 2 → 3) para passos.
- Escrita à mão: traço laranja que se desenha sob uma palavra ou em volta de "tudo isso".
- Fecha com ícone 3D, check, logo e o site/@ numa pílula de vidro.
- Pessoa: opcional, num card pequeno ou em `r` no começo e no fim.

## 14 · Dark Kinetic Tipográfico
- Fundo quase preto com brilho difuso; **texto cinético** palavra a palavra, pequeno e grande na mesma frase.
- Destaques: palavra dentro de **chip laranja** ou **roxo** (`.pill.acp`), palavra em **serifa itálica** grande, palavra riscada em vermelho ("~~editado~~"), cursor de digitação piscando no fim da palavra.
- Mockups escuros de interface (janela, linha do tempo, barra "renderizando 98%", caixa de comentário) entrando com perspectiva; cursor de mouse com etiqueta clicando.
- Uma cena clara (papel creme) no meio para quebrar o ritmo.
- Final: "comenta PALAVRA" com a palavra gigante em roxo e a caixa de comentário.
- Pessoa: opcional; se houver, em bolha redonda no canto ou em `r` entre os blocos.

## 15 · Avatar Dourado (talking head premium)
- Fundo preto com **brilho dourado**; a pessoa em tela cheia com o título dourado com glow na altura do peito.
- A pessoa dentro de um **card inclinado em 3D** com borda dourada: cena `r` com o `recorte` dentro de uma moldura girada com `rotationY` 15–20°, e objetos 3D dourados entrando na frente.
- **Órbita de palavras**: a pessoa num círculo com borda dourada e 3–4 pílulas (ex.: Motion, SFX, Lettering) girando em volta.
- Cena clara de contraste com ícone dourado (cérebro, relógio) e barra de progresso.
- **Silhueta**: o recorte da pessoa preenchido de branco (`filter: brightness(0) invert(1)`) quando falar de "modelo"/"conceito", com cartões de B-roll flutuando em volta.
- Legenda em glow dourado, palavras em caixa alta.

## Exemplos prontos
`exemplos/estilo-12.py` a `estilo-16.py` são os roteiros (o 16 é um vídeo real de 65 s, formato Dor e solução, com B-roll e perfil) que geraram as amostras da galeria (fala de 16 s: "cansado de tentar..."). Leia o do estilo escolhido antes de escrever o seu: mostram o arco dinâmico, o recorte com título atrás, a pessoa dentro de um cartão (`recorte(id, dur, escala=0.62, x=-190, y=-957)` mostra rosto e ombros num cartão de 700×720 em x=190, y=520) e as legendas escondidas nas cenas de texto puro (`escrever(..., sem_legenda=("m",))`).
