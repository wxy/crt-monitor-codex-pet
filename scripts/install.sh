#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${CODEX_HOME:-$HOME/.codex}/pets/crt-monitor"

mkdir -p "$DEST"
cp "$ROOT/pet/pet.json" "$DEST/pet.json"
cp "$ROOT/pet/spritesheet.webp" "$DEST/spritesheet.webp"

echo "Installed CRT Monitor to: $DEST"
echo "Restart Codex and select CRT Monitor under Settings -> Appearance -> Pets."
