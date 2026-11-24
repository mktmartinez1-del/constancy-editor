# Constancy Editor · instalador para Windows 10/11 (PowerShell). Rode:  powershell -ExecutionPolicy Bypass -File instalar-windows.ps1
$ErrorActionPreference = "Stop"
Write-Host "== Constancy Editor: preparando seu Windows =="
function Tem($c) { $null -ne (Get-Command $c -ErrorAction SilentlyContinue) }
if (-not (Tem winget)) { Write-Host "Falta o winget (Instalador de Aplicativos). Atualize o 'Instalador de Aplicativo' na Microsoft Store e rode de novo."; exit 1 }
if (-not (Tem node))    { winget install -e --id OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements }
if (-not (Tem ffmpeg))  { winget install -e --id Gyan.FFmpeg --accept-package-agreements --accept-source-agreements }
if (-not (Tem python))  { winget install -e --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements }
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
npx --yes hyperframes@0.9.81 browser ensure
npx --yes hyperframes@0.9.81 models install parakeet
New-Item -ItemType Directory -Force -Path "$HOME\Constancy-Videos\videos-brutos","$HOME\Constancy-Videos\projetos","$HOME\Constancy-Videos\exportacao" | Out-Null
Write-Host ""
Write-Host "Pronto! Feche e abra o terminal, abra o Claude Code e digite:  /editor-magnetico"
