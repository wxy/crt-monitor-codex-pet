<div align="center">

# CRT Monitor

### 一台会盯着你代码看的复古小显示器。

简体中文 · [English](README.md)

![CRT Monitor 设计图](assets/source-design.png)

**Codex Pet v2** · **88 帧** · **透明 WebP** · **macOS / Windows / Linux**

</div>

CRT Monitor 是为 Codex 设计的原创 Q 版 CRT 桌面伙伴。暖米色机身、深绿玻璃屏幕、发光像素表情和两只小圆脚，把编码状态变成一只带着复古计算机气质的小角色。

当 Codex 工作、等待、Review 或遇到错误时，CRT Monitor 会通过终端活动、状态符号、错误诊断、代码行和方向表情做出对应反应。

## 安装

### macOS / Linux

```bash
./scripts/install.sh
```

### Windows PowerShell

```powershell
./scripts/install.ps1
```

也可以手动安装：

```bash
mkdir -p ~/.codex/pets/crt-monitor
cp pet/pet.json pet/spritesheet.webp ~/.codex/pets/crt-monitor/
```

重启 Codex，然后在 **Settings → Appearance → Pets** 中选择 **CRT Monitor**。

## Pet 格式

| | |
| --- | --- |
| Runtime | Codex Pet v2 |
| Atlas | `1536 × 2288` WebP |
| 网格 | `8 × 11` |
| 单帧 | `192 × 208` |
| 动画 | 9 个标准状态 + 16 个观察方向 |
| 背景 | 透明 |

## 参与贡献

欢迎改进动画连续性、屏幕表情、无障碍表现、文档、安装脚本以及兼容的视觉变体。详细说明见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

代码和脚本采用 [MIT License](LICENSE)。

CRT Monitor 的角色设计和美术资源采用 [CC BY 4.0](LICENSE-ARTWORK)。

---

<div align="center">
<sub>CRT Monitor 是独立的社区 Pet 项目，与 OpenAI 无隶属或官方背书关系。</sub>
</div>
