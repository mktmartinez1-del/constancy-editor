$ok = $true
foreach ($p in @(@("node","Node.js"),@("ffmpeg","FFmpeg"),@("python","Python 3"))) {
  if (Get-Command $p[0] -ErrorAction SilentlyContinue) { Write-Host "OK $($p[1])" } else { Write-Host "FALTA $($p[1]) -> rode instalar-windows.ps1"; $ok = $false }
}
New-Item -ItemType Directory -Force -Path "$HOME\Constancy-Videos\videos-brutos","$HOME\Constancy-Videos\projetos","$HOME\Constancy-Videos\exportacao" | Out-Null
if ($ok) { Write-Host "TUDO OK" } else { exit 1 }
