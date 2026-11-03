# BOOK 1 — PRODUCTION LOCKS

| Lock | Value | Source |
|---|---|---|
| Trim | 8.5" × 11" (large trim) | Toddler “jumbo” format; KDP [Print Options](https://kdp.amazon.com/en_US/help/topic/G201834180) |
| Bleed | **No** | Art inset; avoids cropped outlines |
| Interior ink | **Black ink, white paper** | Line art; [Print Options](https://kdp.amazon.com/en_US/help/topic/G201834180) |
| File pages | **104** even | 4 front + 100 drawings; KDP page-count / print-cost rules ([Printing cost](https://kdp.amazon.com/en_US/help/topic/G201834340)); competitor 100-page cluster from local market research (not committed — see `.gitignore`) |
| Coloring drawings | **100** unique closed-shape pictures | Competitor 100-page cluster; limbs are capsules, not stick lines |
| Gutter | 0.50" | Above 0.375" min for ≤150 pp ([Trim, Bleed, Margins](https://kdp.amazon.com/help/topic/GVBQ3CMEQW3W2VL6)) |
| Outer/top/bottom | 0.50" | Above 0.25" no-bleed min |
| Stroke | 8 pt outer / 5 pt inner | Toddler thick line; no gray fill, no shading on interior |
| Art fit | Each drawing scaled to fit **440 × 520 pt** max, centered; stroke stays **8 pt / 5 pt** (geometry scales, line weight does not) | `_shared/fit_art.py`; added 2026-10-25 so every page is "one big picture". Measured margins ≥ 1.0" (lock above is 0.50") |
| DPI | Vector PDF | KDP wants ≥300 dpi for raster; we stay vector |
| Fonts | **DejaVu Sans / DejaVu Sans Bold, embedded** | KDP: embed all fonts in interior and cover ([Paperback Fonts](https://kdp.amazon.com/help/topic/G202145450), [Submission Guidelines](https://kdp.amazon.com/en_US/help/topic/G201857950)). Helvetica Type 1 does not embed and trips Print Previewer. |
| Cover finish | Glossy | KDP: typical for children’s books |
| Cover text inset | ≥ 0.25" inside trim | Official min is 0.125" ([Paperback Cover](https://kdp.amazon.com/help/topic/G201953020)) |
| Spine text | 7 pt; 104 pp > 79 pp allowed | Spine = 0.234208"; 0.0625" clearance each side |
| Barcode | Leave 2.0" × 1.2" lower-right **back**, **0.25" from spine and from trim** | KDP places barcode; covers with art/text in that box are rejected ([Barcodes](https://kdp.amazon.com/en_US/help/topic/G5HDYGP4BXLX4RUW)). Transparency codes are retired for books created after November 2025 — this title does not get an extra code above the box. |
| List price | ≥ $9.99 / €9.99 / £7.99 | 60% print royalty floor |
| Reading age | 2–5 | Metadata |
| ISBN | **979-8-1940-3221-1** (KDP-assigned) | Free KDP ISBN; manuscript must match ([ISBN](https://kdp.amazon.com/en_US/help/topic/G201834170)) |
| Imprint | **Independently published** | Forced on free KDP ISBN. Author/brand/copyright is **Unloved Productions**, not the KDP imprint field |
| Low-content checkbox | **Off** | Official: coloring books are *not generally* low-content ([Low-Content Books](https://kdp.amazon.com/help/topic/GGE5T76TWKA85DJM)) |
| AI disclosure | **Not AI-generated** | Geometry drawn in code, not an image model |
| eBook | **Do not publish** | Coloring books are print; Kindle is the wrong format |

Spine (white B&W): `104 × 0.002252" = 0.234208"` ([Paperback Cover](https://kdp.amazon.com/help/topic/G201953020)).
