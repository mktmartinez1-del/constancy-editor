#!/bin/bash
# Constancy Editor · instalador para Mac. Rode no Terminal:  bash instalar-mac.sh
set -e
echo "== Constancy Editor: preparando seu Mac =="
if ! command -v brew >/dev/null 2>&1; then
  for b in /opt/homebrew/bin/brew /usr/local/bin/brew; do [ -x "$b" ] && eval "$($b shellenv)"; done
fi
if ! command -v brew >/dev/null 2>&1; then
  echo
  echo "Falta o Homebrew (instalador de programas do Mac). Cole este comando no Terminal, aperte Enter e digite a senha do Mac:"
  echo '  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
  echo "Depois rode este instalador de novo."
  exit 1
fi
command -v node   >/dev/null 2>&1 || brew install node
command -v ffmpeg >/dev/null 2>&1 || brew install ffmpeg
command -v python3 >/dev/null 2>&1 || brew install python
echo "-- motor de vídeo (HyperFrames) e navegador de renderização"
npx --yes hyperframes@0.9.81 browser ensure
echo "-- modelo de transcrição em português (Parakeet, ~600 MB, só na primeira vez)"
npx --yes hyperframes@0.9.81 models install parakeet || echo "aviso: Parakeet não instalou; a transcrição vai usar o Whisper."
mkdir -p "$HOME/Constancy-Videos/videos-brutos" "$HOME/Constancy-Videos/projetos" "$HOME/Constancy-Videos/exportacao"
bash "$(dirname "$0")/verificar.sh"
echo
echo "Pronto! Abra o Claude Code e digite:  /editor-magnetico"
