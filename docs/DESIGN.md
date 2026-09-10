# Design Notes

## Character

CRT Monitor is an original chibi retro computer monitor with:

- warm cream/beige CRT housing
- dark green-black glass screen
- green pixel/emoticon status graphics
- small rounded feet
- compact side nub/hand for the waving state
- soft, friendly retro-computing silhouette

## Runtime state language

| Row | State | Visual intent |
| ---: | --- | --- |
| 0 | idle | relaxed / happy face |
| 1 | running-right | movement facing right |
| 2 | running-left | movement facing left |
| 3 | waving | side hand/nub visible without clipping |
| 4 | jumping | lifted / energetic pose |
| 5 | failed | red error diagnostics |
| 6 | waiting | question or exclamation |
| 7 | running | terminal/progress/spinner |
| 8 | review | code lines; one magnifier frame |
| 9 | look-right | directional look sequence |
| 10 | look-left | complementary directional look sequence |

## Production constraints

The source board and runtime atlas both present the final 8×11 frame set. The contact sheet is generated from the runtime atlas at native resolution, with no scaling or interpolation. Per-frame and per-column decoded-pixel hashes are recorded in [`assets/frame-audit.md`](../assets/frame-audit.md).

Important invariants:

1. Never infer transparency from black/dark pixels; the CRT screen must stay opaque.
2. Never trim and rescale each sprite independently.
3. Use a shared scale/baseline so playback does not visibly pop.
4. Keep waving and magnifier props within the 192×208 frame boundary.
5. Final runtime spritesheet contains no QA grid lines.
