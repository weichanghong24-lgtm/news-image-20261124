# Build log — news-image-20261124

## v1 — 2026-11-24 22:30 CET (first write + run)

- Wrote `build_image.py` from scratch (fresh broadsheet front-page layout:
  masthead, hero panel, two story columns, market strip, bottom ticker).
  Python 3 + Pillow only, system DejaVu fonts, no network, deterministic.
- Wrote `main.py` from scratch (stdlib only; copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`).
- Wrote `README.md` (with the three make.fun badges for
  news-image-20261124 and the bounty link), `LICENSE` (MIT), and
  `.makefun/owner.json` (wallet `9JyNJ9EJWQokXcAz8datkBvJnrgqy5AZy3NS7v7xXx7M`).
- First render: `entry.png`, 1024×1024, 140,429 bytes.
  sha256 `c97982f5dce809463ef64255c8de342cd9165f38a18e0100ca8a4a57756464eb`
- Visual check found three problems: the hero deck overflowed the panel
  border, the left column's third story ran into the market strip, and the
  bottom ticker ran past the footer and overlapped it.

## v2 — 2026-11-24 22:35 CET (layout fixes)

- Reason: fix the three overflows found in the v1 visual check.
- Hero: headline 46 → 40 px, deck shortened to one fact line, panel
  152–348 → 150–340.
- Columns: start 372 → 356, headline 25 → 24 px, body 17 → 16 px,
  tighter rule/gap spacing.
- Market strip 776–848 → 786–852; ticker shortened (~430 chars),
  16 → 15 px, leading 23 → 20; footer moved to y 999.
- Re-render: `entry.png`, 1024×1024, 129,174 bytes.
  sha256 `b5d867d369e0bed74fe9c399ed4e893e9b0519399593c111f55be5412409217e`
- Visual check: clean — no overflow, no overlap, all text legible.

## v3 — 2026-11-24 22:36 CET (verification, no code change)

- Determinism: ran `build_image.py` twice more; all three runs give the
  same sha256 `b5d867d369e0bed74fe9c399ed4e893e9b0519399593c111f55be5412409217e`.
- Entrypoint: ran `main.py` twice into two fresh empty output dirs
  (`/tmp/out1`, `/tmp/out2`); both outputs match `entry.png`'s sha256.
- Final file: `entry.png`, 1024×1024, 129,174 bytes (< 1 MiB).
- Local git init + commit in this directory only (no remote, no push).
