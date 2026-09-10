# Contributing

Thanks for improving CRT Monitor.

## Good contributions

- Fix clipping, scale popping, baseline jumps, or animation continuity.
- Improve installer or validation scripts.
- Improve documentation and translations.
- Add screen expressions that preserve the meaning of the runtime state.
- Propose alternate visual variants without replacing the canonical original.

## Asset rules

The code/scripts are MIT licensed. Artwork is CC BY 4.0. By contributing artwork, you confirm you have the right to license your contribution under CC BY 4.0.

## Before opening a pull request

Run:

```bash
python3 scripts/validate.py
```

For an Awesome Codex Pet submission, generate a clean three-file folder:

```bash
python3 scripts/prepare-community-submission.py YOUR_GITHUB_HANDLE
```

Do not put QA previews, README files, or source art inside the community pet folder.
