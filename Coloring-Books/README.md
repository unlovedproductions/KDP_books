# Coloring-Books — production toolchain

Two KDP toddler coloring books, both drawn in code (vector PDF, no image model):

| Folder | Book | Interior | Cover |
|---|---|---|---|
| `01-toddler-bold-easy/` | Big Easy Coloring Book for Toddlers Ages 2-5 | `Toddler_Bold_Easy_INTERIOR.pdf` | `Toddler_Bold_Easy_COVER.pdf` |
| `02-toddler-trucks-construction/` | Big Easy Trucks Coloring Book for Toddlers Ages 2-5 | `Toddler_Trucks_INTERIOR.pdf` | `Toddler_Trucks_COVER.pdf` |

Each folder's `PRODUCTION_LOCKS.md` is the spec (trim, stroke, margins, fonts, ISBN, spine math).
`PROJECT_BRIEF.md` and `KDP_LISTING.md` hold the brief and the KDP listing fields.

## Setup

System tools (not installable with pip):

- **Ghostscript** (`gs`) — re-embeds fonts in the finished PDFs (KDP requires embedded fonts).
- **Poppler** (`pdftoppm`) — used to measure each drawing so it can be fitted to the page, and to make previews.

```bash
# Debian / Ubuntu / Pop!_OS
sudo apt install ghostscript poppler-utils
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Fonts (DejaVu Sans / Bold) are bundled in each book's `production/fonts/`.

## Build

Run from the book's `production/` folder. Build the **interior first**: it writes
`output/interior_page_count.txt`, which the cover reads to compute the spine.

```bash
cd 01-toddler-bold-easy/production      # or 02-toddler-trucks-construction/production
python3 generate_interior.py            # -> output/*_INTERIOR.pdf (104 pages)
python3 generate_cover.py               # -> output/*_COVER.pdf + cover_dimensions.txt
```

## Output check

```bash
pdfinfo output/*_INTERIOR.pdf | grep Pages     # 104
pdffonts output/*_INTERIOR.pdf                  # every font: emb = yes
pdftoppm -r 100 -png -f 1 -l 6 output/*_INTERIOR.pdf output/preview/interior
```

## Layout notes

- `drawings.py` — the 100 drawings per book (`PAGES`). Stroke widths are `OUTER = 8 pt` / `INNER = 5 pt`.
- `_shared/fit_art.py` — measures each drawing and scales its geometry to fit 440 × 520 pt. Strokes are
  compensated (`drawings.STROKE_K = 1/scale`) so printed line weight never changes.
- After any change that alters the page count, rebuild the interior **and** the cover.
- Interior copyright pages carry the KDP ISBN from the locks; if an ISBN changes, edit it in
  `generate_interior.py` and re-upload the interior.
