$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
if ($env:CODEX_HOME) {
    $CodexHome = $env:CODEX_HOME
} else {
    $CodexHome = Join-Path $HOME ".codex"
}

$Dest = Join-Path $CodexHome "pets\crt-monitor"
New-Item -ItemType Directory -Force -Path $Dest | Out-Null

Copy-Item (Join-Path $Root "pet\pet.json") (Join-Path $Dest "pet.json") -Force
Copy-Item (Join-Path $Root "pet\spritesheet.webp") (Join-Path $Dest "spritesheet.webp") -Force

Write-Host "Installed CRT Monitor to: $Dest"
Write-Host "Restart Codex and select CRT Monitor under Settings -> Appearance -> Pets."
