# Constancy Editor

Editor de vídeo do **Método Constancy** dentro do Claude Code. Você escolhe o estilo visual e um dos **8 formatos da Copy Magnética**, envia o vídeo, responde umas perguntas, e o Claude edita no seu computador: motion design, legendas palavra por palavra, cortes, efeitos sonoros e a sua música. Sai um MP4 vertical pronto para Reels e TikTok, mais a legenda da publicação.

## O que você precisa
- **Claude Code** instalado (app do Claude para computador ou terminal) e um plano pago do Claude.
- Mac com Apple Silicon ou Intel (testado), ou Windows 10/11 (instalador incluído).
- ~3 GB livres (motor de vídeo, navegador de renderização e modelo de transcrição).

## Instalação (uma vez)
No Claude Code, digite os dois comandos:
```
/plugin marketplace add mktmartinez1-del/constancy-editor
/plugin install constancy-editor@metodo-constancy
```
Depois escreva no Claude: **"instale o Constancy Editor"**. Ele roda o instalador, que coloca o Node.js, o FFmpeg, o motor de vídeo e o modelo de transcrição em português. No Mac, se faltar o Homebrew, o Claude mostra um comando para você colar no Terminal (ele pede a senha do Mac).

## Como usar
Digite **/editor-magnetico** e siga as escolhas:
1. **Estilo**: abre uma galeria com as 17 amostras. Responda o número.
2. **Formato**: Dica de valor, Dor e solução, React, Comparativo, Trend com texto, Lista e ranking, Storytelling narrado ou Conexão real.
3. **Edição**: sua música (ou sem música), ritmo dinâmico ou minimalista, palavra do CTA.
4. **Vídeo**: arraste o arquivo para o chat (ou coloque em `Constancy-Videos/videos-brutos`). Ainda não gravou? O Claude cria o roteiro e a lista de takes pelo método.
5. **Pronto**: o MP4 aparece em `Constancy-Videos/exportacao`, com a legenda da publicação ao lado.

Quer mudar algo? É só pedir ("troca a frase do começo", "música mais baixa").

## Pastas
```
~/Constancy-Videos/
  videos-brutos/   seus vídeos
  projetos/        um projeto por vídeo (pode apagar depois)
  exportacao/      os vídeos prontos
```

## Licenças
Veja `LICENCAS.md`. O pacote não inclui músicas: use as suas (com direito de uso) ou deixe o vídeo sem trilha.
