#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re, shutil

ROOT = Path(__file__).resolve().parents[1]

parser = argparse.ArgumentParser(description="Prepare Awesome Codex Pet submission folder.")
parser.add_argument("handle", help="GitHub handle / author slug")
parser.add_argument("--author", help="Display author name; defaults to handle")
args = parser.parse_args()

raw_handle = args.handle.strip()
handle = re.sub(r"[^a-z0-9-]+", "-", raw_handle.lower()).strip("-")
if not handle:
    raise SystemExit("Invalid handle")

author = args.author or raw_handle
slug = f"crt-monitor--{handle}"
dest = ROOT / "community" / "generated" / slug

if dest.exists():
    shutil.rmtree(dest)
dest.mkdir(parents=True)

shutil.copy2(ROOT / "pet" / "spritesheet.webp", dest / "spritesheet.webp")

pet = {
    "id": slug,
    "displayName": "CRT Monitor",
    "description": "A tiny retro CRT monitor that keeps an eye on your code.",
    "spriteVersionNumber": 2,
    "spritesheetPath": "spritesheet.webp"
}
(dest / "pet.json").write_text(json.dumps(pet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

submission = {
    "slug": slug,
    "pet_slug": "crt-monitor",
    "author_slug": handle,
    "name": "CRT Monitor",
    "localized_names": {
        "en": "CRT Monitor",
        "zh": "CRT 显示器"
    },
    "author": author,
    "primary_category": "Robots",
    "canonical_key": f"original/{handle}/crt-monitor",
    "tags": ["robot", "retro-computing", "crt", "coding"],
    "source_type": "original",
    "source_url": f"https://github.com/{raw_handle}/crt-monitor-codex-pet",
    "license": "CC BY 4.0",
    "preview_image": f"../../assets/previews/{slug}/gifs/idle.gif",
    "codex_install": {
        "pet_json": "pet.json",
        "spritesheet": "spritesheet.webp"
    }
}
(dest / "submission.json").write_text(
    json.dumps(submission, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

print(dest)
print("Ready for the Awesome Codex Pet submission folder.")
