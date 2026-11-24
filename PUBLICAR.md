# Como publicar uma nova versão (só para o dono)

Repositório: https://github.com/mktmartinez1-del/constancy-editor (público)

1. Aumente `version` em `.claude-plugin/plugin.json` e `.claude-plugin/marketplace.json`.
2. Nesta pasta: `git add -A && git commit -m "versão X" && git push`.
3. Quem já instalou atualiza com `/plugin marketplace update metodo-constancy`.
