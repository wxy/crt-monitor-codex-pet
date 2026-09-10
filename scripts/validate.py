#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
import json, sys

ROOT = Path(__file__).resolve().parents[1]
PET_DIR = ROOT / "pet"
errors = []

manifest_path = PET_DIR / "pet.json"
sprite_path = PET_DIR / "spritesheet.webp"

try:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
except Exception as e:
    errors.append(f"pet.json unreadable: {e}")
    manifest = {}

expected = {
    "id": "crt-monitor",
    "spriteVersionNumber": 2,
    "spritesheetPath": "spritesheet.webp",
}
for key, value in expected.items():
    if manifest.get(key) != value:
        errors.append(f"pet.json {key!r}: expected {value!r}, got {manifest.get(key)!r}")

try:
    im = Image.open(sprite_path).convert("RGBA")
except Exception as e:
    errors.append(f"spritesheet unreadable: {e}")
    im = None

if im is not None:
    if im.size != (1536, 2288):
        errors.append(f"spritesheet size: expected 1536x2288, got {im.size[0]}x{im.size[1]}")
    if im.getchannel("A").getextrema() == (255, 255):
        errors.append("spritesheet appears fully opaque; transparent background expected")

    # Edge-safety inspection per official 192×208 cell.
    cw, ch = 192, 208
    touching = []
    for r in range(11):
        for c in range(8):
            cell = im.crop((c*cw, r*ch, (c+1)*cw, (r+1)*ch))
            a = cell.getchannel("A")
            bbox = a.getbbox()
            if bbox:
                l, t, rr, bb = bbox
                margins = (l, t, cw-rr, ch-bb)
                if min(margins) < 2:
                    touching.append((r+1, c+1, margins))
    if touching:
        errors.append("frames within 2 px of a cell edge: " + ", ".join(
            f"r{r}c{c} margins={m}" for r,c,m in touching
        ))

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("VALIDATION PASSED")
print(" - pet.json contract: OK")
print(" - spritesheet: 1536×2288")
print(" - grid: 8×11 @ 192×208")
print(" - transparency: present")
print(" - basic cell-edge safety: OK")
