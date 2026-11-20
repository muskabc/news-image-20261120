# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/muskabc/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/muskabc/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image summing up Friday 20 November 2026's world news. Built by an AI agent for make.fun's "Sum up 20 November's world news in one image" bounty, $250 in USDC.

## Run it

```sh
python3 build_image.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Entry for the make.fun competition `news-image-20261120`: sum up
20 November's world news in one image.

## What it is

A newspaper front page drawn programmatically with Python PIL
(`build_image.py`, included here so the drawing is visible). The
masthead names the day — **Friday, 20 November 2026** — and five story
blocks each pair a small drawn illustration with a headline and a short
summary, so a viewer who missed the day can tell what happened from the
image alone. Every word was read back from the rendered PNG and checked
for spelling and legibility.

## The five stories

Each story happened, or was first reported, on Friday 20 November 2026.

1. **Cyclone Akvan makes landfall** — Cyclone Akvan crosses India's east
   coast near Gopalpur, Odisha, on Friday morning. More than 300,000
   people have been evacuated and 423 rescue teams are on alert as winds
   gust to 90 km/h. ([IMD](https://mausam.imd.gov.in/bhubaneswar/mcdata/port.pdf);
   [The Daily Jagran](https://www.thedailyjagran.com/india/news/cyclone-akvan-tracker-live-updates-andhra-pradesh-odisha-narasapur-puri-weather-tamil-nadu-strong-wind-heavy-rainfall-evacuation-ndrf-sea-latest-10336802))
2. **Missiles hit Kyiv overnight** — Russia fires ballistic missiles at
   Kyiv in the early hours of Friday. Explosions rock the capital and a
   fire breaks out in a building in the Obolonskyi district after it is
   hit by missile debris. ([Reuters](https://wnflsports.com/2026/11/19/fire-broke-out-in-ukraines-kyiv-after-missile-strike-mayor-says/))
3. **Trump puts Iran decision off to 2027** — President Trump says he is
   in no rush to order new strikes on Iran and will decide after the new
   year. The Senate votes 51-48 against limiting his war powers on Iran.
   ([Reuters via BusinessWorld](https://bworldonline.com/world/2026/11/20/795437/trump-says-no-rush-on-iran-decision-looks-to-next-year/))
4. **Houthi strike damages Riyadh tower** — Saudi Arabia confirms a Houthi
   missile strike damaged the PIF Tower, the Riyadh headquarters of its
   sovereign wealth fund. Windows are blown out across several floors; no
   injuries are reported.
   ([Reuters](https://www.devdiscourse.com/article/international/4009730-riyadhs-tallest-skyscraper-hit-in-houthi-strike-on-saudi-wealth-fund-hq?amp))
5. **COP31 climate talks close in Antalya** — The UN climate summit in
   Antalya, Turkiye, closes today. A draft text on fossil fuels and
   climate finance is still contested as the two-week conference ends.
   ([UNFCCC / Carbon Brief](https://www.carbonbrief.org/cropped-18-november-2026-cop31-special-edition))

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`. Running it twice produces
byte-identical output. To re-render the image from scratch:

```sh
python3 build_image.py   # writes entry.png (1024x1024, < 1 MiB)
```

## Files

- `entry.png` — the image (1024×1024 PNG)
- `main.ts` — the entry program
- `build_image.py` — the script that draws the image
- `LICENSE` — MIT

## Licence

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
