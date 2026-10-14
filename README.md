# Tupo stroke data

Stroke-order data for the 1940 simplified Chinese characters taught in
Tupo, a Mandarin learning app for iOS (the
characters of HSK 3.0 levels 1 to 6). One JSON file per character.

## Source

Converted from [Make Me a Hanzi](https://github.com/skishore/makemeahanzi)
by Shaunak Kishore, `graphics.txt` at commit
[`bddc96d41bef`](https://github.com/skishore/makemeahanzi/tree/bddc96d41bef78427ed0e034e9f7e31d71fd1b92).
`graphics.txt` is derived from the **Arphic PL KaitiM GB** and **Arphic PL
UKai** fonts by Arphic Technology Co., Ltd.

## Licence

These files are licensed under the **Arphic Public License**, the licence
of `graphics.txt`. The full text is in `ARPHICPL.TXT` (also copied to
`LICENSE` so GitHub shows it); it must stay with the files, unaltered.
Anyone may copy, modify and redistribute this data under that licence.

## Changes from Make Me a Hanzi

- Each character's line of `graphics.txt` was copied into a file of its
  own, `data/strokes-<hex codepoint>.json` (e.g. 你 U+4F60 →
  `strokes-4f60.json`), and only the characters Tupo teaches were kept.
- A `notice` field was added to each file saying what changed and when,
  as the licence requires.
- The `strokes` and `medians` are **unchanged**.

`tools/split_graphics.py` reproduces the files from `graphics.txt`:
`python3 tools/split_graphics.py path/to/graphics.txt characters.txt`
(`characters.txt` lists the characters kept).

## Format

```json
{"character": "你", "strokes": ["M 272 567 Q …", …], "medians": [[[x, y], …], …], "notice": "…"}
```

- `strokes`: one SVG path per stroke, in stroke order (the outline of the stroke).
- `medians`: for each stroke, points along its centre line, in drawing direction.
- Coordinates: a 1024 × 1024 box with y pointing up and the baseline at 900.
  In SVG, draw inside `<g transform="scale(1, -1) translate(0, -900)">`
  with `viewBox="0 0 1024 1024"`.

Exported 2026-10-14.
