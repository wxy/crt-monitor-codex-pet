#!/usr/bin/env python3
from collections import defaultdict
from hashlib import sha256
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SPRITESHEET = ROOT / "pet/spritesheet.webp"
PREVIEW = ROOT / "assets/preview-grid.png"
AUDIT = ROOT / "assets/frame-audit.md"

COLS, ROWS = 8, 11
CELL_W, CELL_H = 192, 208
EXPECTED_SIZE = (COLS * CELL_W, ROWS * CELL_H)

atlas = Image.open(SPRITESHEET).convert("RGBA")
if atlas.size != EXPECTED_SIZE:
    raise SystemExit(f"expected {EXPECTED_SIZE}, got {atlas.size}")

# Native-resolution contact sheet. The checkerboard is only a preview backdrop;
# atlas pixels are composited at 1:1 with no scaling or interpolation.
checker = Image.new("RGBA", atlas.size, "#f2f4f4")
draw = ImageDraw.Draw(checker)
checker_size = 32
for y in range(0, atlas.height, checker_size):
    for x in range(0, atlas.width, checker_size):
        if (x // checker_size + y // checker_size) % 2:
            draw.rectangle(
                (x, y, min(x + checker_size - 1, atlas.width - 1), min(y + checker_size - 1, atlas.height - 1)),
                fill="#d7dbdc",
            )
preview = Image.alpha_composite(checker, atlas)
guide = ImageDraw.Draw(preview)
for x in range(0, atlas.width + 1, CELL_W):
    guide.line((min(x, atlas.width - 1), 0, min(x, atlas.width - 1), atlas.height - 1), fill="#00a88f", width=1)
for y in range(0, atlas.height + 1, CELL_H):
    guide.line((0, min(y, atlas.height - 1), atlas.width - 1, min(y, atlas.height - 1)), fill="#00a88f", width=1)
preview.convert("RGB").save(PREVIEW, format="PNG", optimize=True)

frame_hashes = []
hash_locations = defaultdict(list)
for row in range(ROWS):
    row_hashes = []
    for col in range(COLS):
        frame = atlas.crop((col * CELL_W, row * CELL_H, (col + 1) * CELL_W, (row + 1) * CELL_H))
        digest = sha256(frame.tobytes()).hexdigest()
        row_hashes.append(digest)
        hash_locations[digest].append((row + 1, col + 1))
    frame_hashes.append(row_hashes)

column_hashes = []
for col in range(COLS):
    column_bytes = b"".join(
        atlas.crop((col * CELL_W, row * CELL_H, (col + 1) * CELL_W, (row + 1) * CELL_H)).tobytes()
        for row in range(ROWS)
    )
    column_hashes.append(sha256(column_bytes).hexdigest())

duplicates = [(digest, locations) for digest, locations in hash_locations.items() if len(locations) > 1]
duplicate_columns = defaultdict(list)
for col, digest in enumerate(column_hashes, 1):
    duplicate_columns[digest].append(col)
duplicate_column_groups = [cols for cols in duplicate_columns.values() if len(cols) > 1]

lines = [
    "# Runtime Sprite Audit",
    "",
    f"- Atlas: `{atlas.width}×{atlas.height}` WebP",
    f"- Grid: `{COLS}×{ROWS}` (`{COLS * ROWS}` frames)",
    f"- Cell: `{CELL_W}×{CELL_H}` RGBA after decoding",
    f"- Atlas SHA-256: `{sha256(SPRITESHEET.read_bytes()).hexdigest()}`",
    "- Method: SHA-256 over every decoded RGBA cell; SHA-256 over each complete 11-frame column.",
    "",
    "## Duplicate result",
    "",
]
if duplicates:
    lines.append("Exact duplicate decoded frames were found:")
    lines.append("")
    for digest, locations in duplicates:
        joined = ", ".join(f"R{row}C{col}" for row, col in locations)
        lines.append(f"- `{digest}`: {joined}")
else:
    lines.append("No exact duplicate decoded frames were found among the 88 cells.")
lines.extend(["", "No complete duplicate columns were found." if not duplicate_column_groups else f"Duplicate column groups: {duplicate_column_groups}", "", "## Per-frame hashes", ""])
lines.append("| Row | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |")
lines.append("| ---: | --- | --- | --- | --- | --- | --- | --- | --- |")
for row, hashes in enumerate(frame_hashes, 1):
    lines.append("| " + str(row) + " | " + " | ".join(f"`{digest[:12]}`" for digest in hashes) + " |")
lines.extend(["", "## Per-column hashes", ""])
for col, digest in enumerate(column_hashes, 1):
    lines.append(f"- C{col}: `{digest}`")
lines.append("")

AUDIT.write_text("\n".join(lines), encoding="utf-8")
print(f"wrote {PREVIEW.relative_to(ROOT)} ({preview.width}x{preview.height})")
print(f"wrote {AUDIT.relative_to(ROOT)}")
print(f"exact duplicate frame groups: {len(duplicates)}")
print(f"exact duplicate column groups: {len(duplicate_column_groups)}")
