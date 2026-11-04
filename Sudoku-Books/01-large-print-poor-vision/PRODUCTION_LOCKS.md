# SUDOKU 01 — PRODUCTION LOCKS

| Lock | Value | Source |
|---|---|---|
| Trim | 8.5" × 11" | KDP large trim ([Print Options](https://kdp.amazon.com/en_US/help/topic/G201834180)) |
| Bleed | No on the interior. 0.125" on the cover only | Interior art stays inside the gutter |
| Interior ink | Black ink | Line art |
| Paper | Cream | Thicker stock than white. Spine factor is not the white-paper factor |
| File pages | 124, even | 4 front + 40 puzzle leaves (puzzle + blank verso) + 40 solution pages |
| Puzzles | 40 easy, one solution each, 47–53 givens, 180-degree symmetry | Seed `20261103` in `production/sudoku.py` |
| Puzzle page | Odd page, one grid, digits 40 pt | The working page |
| Verso | Blank. No page number, no footer | The show-through fix |
| Solutions | Pages 85–124, one full-size grid, clues bold | Never the back of that puzzle |
| Gutter | 0.625" | Above the 0.375" minimum for 151 pages or fewer ([Trim, Bleed, Margins](https://kdp.amazon.com/help/topic/GVBQ3CMEQW3W2VL6)) |
| Outer / top / bottom | 0.50" / 0.55" / 0.50" | Above the 0.25" no-bleed minimum |
| Grid lines | 3.25 pt box borders, 1.15 pt cell borders | Black on unpainted paper. Cream is the paper, not a printed tint |
| Fonts | DejaVu Sans and DejaVu Sans Bold, embedded | Ghostscript rewrite after ReportLab |
| Cover finish | Matte | Less glare than glossy for this reader |
| Cover text inset | ≥ 0.25" inside trim | Official minimum is 0.125" |
| Spine | 124 × 0.0025" = 0.310000". Text 7 pt | Cream factor ([Paperback Cover](https://kdp.amazon.com/help/topic/G201953020)). 124 pages is over the 79-page spine-text minimum |
| Barcode | 2.0" × 1.2" lower-right back, 0.25" from the spine and from the trim, white box through the bleed | KDP places the barcode |
| List price | $9.99 / £7.99 / €9.99 / CAD $13.99 / AUD $13.99 / ¥1000 / 40 PLN / 110 SEK | 60% royalty floors ([Paperback Royalty](https://kdp.amazon.com/en_US/help/topic/G201834330)). Entered on the pricing page before publish. |
| US print | $1.00 + $0.017 × 124 = $3.108 | Large trim, black ink, 110–828 pages ([Printing Cost](https://kdp.amazon.com/en_US/help/topic/G201834340)). Cream and white share this chart |
| UK print | £0.85 + £0.012 × 124 = £2.338 | Same chart, large trim |
| EU print | €0.75 + €0.016 × 124 = €2.734 | Amazon.de/es/fr/it/nl/ie/com.be |
| ISBN | 9798167680128 | Free KDP ISBN. Imprint is Independently published. Title id RB22WEEEPAA. ASIN B0HQ9ZBP9J. Bookshelf Live on 2026-11-04. |
| Author | Unloved Productions | Not the imprint field |
| Low-content checkbox | Off | These are puzzles, not a blank log |
| AI disclosure | Not AI-generated | Grids are code, not an image model |
| eBook | Do not publish | Paperback only |
| Series | None | Listing is live. Do not open a series until a new phrase passes the same rule |

Cover size: bleed 0.125 + 8.5 + 0.31 + 8.5 + 0.125 = 17.56" wide, 11.25" tall.

Do not build this cover with `Coloring-Books/_shared/cover_lib.py`. That engine multiplies pages by the white-paper factor 0.002252.
