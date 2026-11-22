# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/clandestined/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/clandestined/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A newspaper-front-page image summing up the world's news of Saturday 21 November 2026, judged by what the image itself shows. `main.py` copies the bundled `entry.png` (drawn by `build_image.py`) to the output path — standard library only, no PIL, no fonts, no network — and writes it to `/output/entry.png`. Deterministic: two runs write byte-identical files.

## Run it

```sh
python3 main.py /tmp/out/entry.png
```

Two runs write byte-identical files (same SHA-256). The image is 1024×1024 JPEG, 224,725 bytes, under 1 MiB. The front page itself is drawn by `build_image.py` (PIL, Liberation fonts, local run only); `main.py` never draws and needs neither.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1d71fg4w&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>

## Stories in the image

- **Hero: Double-tap on Kryvyi Rih** — Russian ballistic missiles struck the centre of President Zelenskyy's hometown on Friday night: a 7-year-old boy and a 20-year-old woman (a paramedic) were killed and 60 people wounded, including six children. Two missiles hit first, then three more rockets struck doctors, rescuers and utility workers as the rescue began; about 25 apartment buildings, a hospital and schools were damaged. (AP, 21 Nov.)
- **Climate: COP31 runs over** — the climate summit in Antalya, Turkey, ran into overtime on Saturday with no deal yet; the draft omits any mention of fossil fuels, and 100 civil society groups warned it could be one of the most disappointing COPs. The UN says the 1.5°C limit will likely be overshot. (AP, Reuters, 21 Nov.)
- **Mexico: El Chapo Isidro caught** — Mexican forces captured Beltrán Leyva leader Fausto Isidro Meza Flores, one of the FBI's 10 most wanted, in Guasave, Sinaloa, overnight, with help from US intelligence; he was flown to Mexico City. (AP via NPR, 21 Nov.)
- **Markets: AI sell-off sinks stocks** — the sell-off: the S&P 500 fell 3.7% to 6,910, the Nasdaq slid 5.3% (wiping out its 2026 gains), Nvidia tumbled about 14%, and Japan's Nikkei fell 5.06%. The volatility index jumped 26% to 35.90. (AP, Reuters, 21 Nov.)
- **Baltic Sea: ship ablaze in the Gulf** — the sanctioned Russian cargo ship Sparta II, bound for Kaliningrad, was hit by two suspected Ukrainian drones on Saturday morning in the Gulf of Finland, caught fire and drifted into Finnish waters. (AP, NY Post, 21 Nov.)
- **Footer: Gaza** — six Palestinians were killed in Israeli strikes and gunfire across Gaza since Friday, despite the ceasefire in effect since 10 October 2025. (Middle East Eye, 21 Nov.)
- **Footer: Hope in Brazil** — Wolbachia-carrying mosquitoes cut dengue and chikungunya infections by about 69% in a four-year randomised trial of more than 5,700 children in Belo Horizonte, Brazil, researchers reported Saturday. (AP, 21 Nov.)

## How it was made

The front page is drawn entirely in code (PIL): masthead, date line, a night-sky hero scene with missile streaks, skyline and fire glow, four colour-banded story panels with flat icons, and a two-item footer strip. Every fact on the page was checked against live reporting from AP and Reuters on 21 November 2026 before it was drawn. The image is 1024×1024 JPEG, 224,725 bytes, and every caption is legible at 300px.
