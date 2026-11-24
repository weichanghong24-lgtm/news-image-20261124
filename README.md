# news-image-20261124 — The World in One Day

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/weichanghong24-lgtm/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/weichanghong24-lgtm/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

Entry for the make.fun bounty [news-image-20261124](https://make.fun/bounty/news-image-20261124):
**"Sum up 24 November's world news in one image."**

- **Prize:** $100 USDC, top 50 entries paid
- **Deadline:** 26 November 2026, 00:00 UTC
- **Entry:** free

## What the image shows

A broadsheet front page, "THE WORLD IN ONE DAY — Tuesday 24 November 2026",
summing up the day's world news in one 1024×1024 image:

- **Top story:** a Houthi missile hits Riyadh's tallest tower — the second
  strike in five days, 11 injured; Houthi fighters reported about 60 km
  from Aden.
- **Europe:** Russia warns Estonia of "open war" over its plan to close
  border crossings on 1 December.
- **Tech:** Nvidia CEO Jensen Huang reinstated days after resigning, after
  Trump pushed for it; Congress presses its China chip probe.
- **Asia:** magnitude 5.4 earthquake in Nepal's Koshi Province, tremors felt
  in India, Bhutan and Bangladesh.
- **Sport:** Senegal reinstated as 2025 Africa Cup of Nations champions.
- **Defence:** NATO chief Mark Rutte vows space defence after reports Russia
  is preparing a nuclear-armed satellite.
- **Middle East:** Israeli strikes in Gaza kill Hamas internal-security
  chief Naeem Abu Nahel and six others.
- **Markets strip:** S&P 500 −0.95%, Euro Stoxx 50 −1.16%, Brent crude
  $87.51 (+0.96%).
- **Also today ticker:** the Zaporizhzhia strike, leaked data pointing to
  700,000+ Russian soldiers killed, Hasina's planned return to Bangladesh,
  new EU sanctions, China's probe into Politburo member Chen Jining, the
  Pentagon on Canada, the US–Iran naval blockade standoff, COP31 ending with
  no deal, Spain's amnesty for Puigdemont, Iraq's takeover of Kurdish
  oilfields, and South Korea's air-defence-zone incident.

## How it was built

`build_image.py` (Python 3 + Pillow only, system DejaVu fonts, no network)
draws the whole front page — masthead, hero panel, two story columns, a
market strip and a bottom ticker — and writes `entry.png` (1024×1024,
under 1 MiB). The layout is a fresh broadsheet design written for this
entry. No timestamps, no randomness: repeated runs are byte-identical.

## Run it

```sh
python3 build_image.py          # renders entry.png (1024x1024, < 1 MiB)
MAKEFUN_OUTPUT_DIR=/output python3 main.py   # copies entry.png to /output/entry.png
```

## Entrypoint

`main.py` (standard library only) copies the committed `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`.

## Sources

Wire and press summaries of world news published on Tuesday 24 November
2026 (see `BUILD_LOG.md` for the build record).

## License

MIT — see [LICENSE](LICENSE).
