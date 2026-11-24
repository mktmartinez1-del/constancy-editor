#!/bin/bash
# Confere se tudo que o Constancy Editor precisa está instalado.
ok=1
chk() { if command -v "$1" >/dev/null 2>&1; then echo "✓ $2"; else echo "✗ $2  →  $3"; ok=0; fi; }
chk node    "Node.js"  "rode o instalador (instalar-mac.sh)"
chk ffmpeg  "FFmpeg"   "rode o instalador (instalar-mac.sh)"
chk python3 "Python 3" "rode o instalador (instalar-mac.sh)"
if [ $ok = 1 ]; then
  if npx --yes hyperframes@0.9.81 browser path >/dev/null 2>&1; then echo "✓ Motor de vídeo (HyperFrames + Chrome)"; else echo "✗ Motor de vídeo  →  npx --yes hyperframes@0.9.81 browser ensure"; ok=0; fi
fi
mkdir -p "$HOME/Constancy-Videos/videos-brutos" "$HOME/Constancy-Videos/projetos" "$HOME/Constancy-Videos/exportacao"
[ $ok = 1 ] && echo "TUDO OK" || { echo "FALTA INSTALAR ALGO (veja acima)"; exit 1; }
