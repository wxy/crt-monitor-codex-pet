# CRT Monitor — Codex Pet

A tiny retro monitor that keeps an eye on your code.

![CRT Monitor design](assets/source-design.png)

**Codex Pet v2 · 88 animation frames · transparent WebP · macOS / Windows / Linux · original character**

CRT Monitor is an original chibi CRT desktop companion designed for Codex. Its screen changes with runtime state: terminal activity while working, question/exclamation marks while waiting, error diagnostics on failure, code lines during review, and directional poses in the v2 look rows.

## Install

### macOS / Linux

```bash
./scripts/install.sh
```

Or manually copy the runtime files:

```bash
mkdir -p ~/.codex/pets/crt-monitor
cp pet/pet.json pet/spritesheet.webp ~/.codex/pets/crt-monitor/
```

Restart Codex, then select **CRT Monitor** under **Settings → Appearance → Pets**.

### Windows PowerShell

```powershell
./scripts/install.ps1
```

## Sprite contract

| Property | Value |
| --- | --- |
| Version | Codex Pet v2 |
| Atlas | `1536 × 2288` WebP |
| Grid | `8 × 11` |
| Cell size | `192 × 208` |
| Standard animation rows | 9 |
| Look-direction rows | 2 |
| Transparency | RGBA / transparent WebP |

## Contributing

Contributions are welcome: animation refinement, alternate screen expressions, accessibility improvements, documentation, installer fixes, and compatible visual variants.

Please keep the original CRT silhouette and state meanings recognizable when contributing to the main pet. Larger visual reinterpretations are better proposed as separate variants.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licensing

Code and scripts: **MIT** — see [LICENSE](LICENSE).

Character design and artwork: **CC BY 4.0** — see [LICENSE-ARTWORK](LICENSE-ARTWORK).
