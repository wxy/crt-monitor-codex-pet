<div align="center">

# CRT Monitor

### A tiny retro monitor that keeps an eye on your code.

[简体中文](README.zh-CN.md) · English

![CRT Monitor design](assets/source-design.png)

**Codex Pet v2** · **88 frames** · **Transparent WebP** · **macOS / Windows / Linux**

</div>

CRT Monitor is an original chibi CRT desktop companion for Codex. Its warm beige shell, dark green glass, glowing pixel expressions, and tiny rounded feet turn coding states into a small retro-computing character on your desktop.

While Codex works, waits, reviews, or hits an error, CRT Monitor responds with terminal activity, status symbols, diagnostics, code lines, and directional expressions.

## Install

### macOS / Linux

```bash
./scripts/install.sh
```

### Windows PowerShell

```powershell
./scripts/install.ps1
```

Or install manually:

```bash
mkdir -p ~/.codex/pets/crt-monitor
cp pet/pet.json pet/spritesheet.webp ~/.codex/pets/crt-monitor/
```

Restart Codex, then choose **CRT Monitor** in **Settings → Appearance → Pets**.

## Pet format

| | |
| --- | --- |
| Runtime | Codex Pet v2 |
| Atlas | `1536 × 2288` WebP |
| Grid | `8 × 11` |
| Frame | `192 × 208` |
| Animations | 9 standard states + 16 look directions |
| Background | Transparent |

The native-resolution [8×11 contact sheet](assets/preview-grid.png) is generated directly from the runtime atlas without scaling. The [frame audit](assets/frame-audit.md) records hashes for all 88 decoded cells and all eight columns.

## Contributing

Contributions that improve animation continuity, screen expressions, accessibility, documentation, installers, or compatible visual variants are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Code and scripts are licensed under the [MIT License](LICENSE).

The CRT Monitor character design and artwork are licensed under [CC BY 4.0](LICENSE-ARTWORK).

---

<div align="center">
<sub>CRT Monitor is an independent community pet project and is not affiliated with or endorsed by OpenAI.</sub>
</div>
