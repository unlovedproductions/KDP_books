# BOOK 1 — PRODUCTION LOCKS

**Locked:** 2026-08-21 (first typeset)  
**Title:** Stoic Foundations  
**Subtitle:** A Guided Workbook on Judgment, Control, and Assent  
**Series:** The Stoic Collection — Book 1  
**Manuscript:** `02_APPROVED/Manuscripts/BOOK 1 — STOIC FOUNDATIONS — MANUSCRIPT.md` (Approved 2026-08-21)

| Decision | Lock |
| --- | --- |
| Author / imprint | **UnlovedProductions** |
| ISBN | **Free KDP ISBN** (insert on copyright page when Amazon assigns; re-export interior) |
| Copyright | **© 2026 UnlovedProductions** |
| Amazon title field | ***Stoic Foundations* only** — do not add Journal / Workbook / Notebook |
| Low-content checkbox | **Do not check** — medium-content guided workbook |
| Trim | 6 × 9 in |
| Interior | Black & white |
| Paper | White |
| Bleed | None (interior); cover wrap uses 0.125 in bleed |
| Target pages | 120 (band 116–124; must be even) |
| **Interior page count (this export)** | **124** |
| Fonts | Liberation Serif / Sans (Book 2 house stack) |
| Spine (white B&W) | `pages × 0.002252"` = **0.279248"** at 124 pp |
| Spine text clearance | **0.375"** from top and bottom cover edges; **0.0625"** from spine folds |

## Production outputs

| Asset | Path |
| --- | --- |
| Interior PDF | `03_WORKING/Other_Working_Materials/production/output/Stoic_Foundations_Book1_INTERIOR.pdf` |
| Cover PDF | `03_WORKING/Other_Working_Materials/production/output/Stoic_Foundations_Book1_COVER.pdf` |
| Page count | `…/output/book1_interior_page_count.txt` |
| Cover math | `…/output/book1_cover_dimensions.txt` |
| Interior typesetter | `…/production/typeset_book1.py` |
| Cover generator | `…/production/cover_book1.py` |

## Typesetting / cover handoff

**Interior:** regenerate via `typeset_book1.py` (venv: `production/.venv`).  
**Cover:** regenerate via `cover_book1.py` after any page-count change.  
Confirm spine with KDP Cover Calculator before final upload.

**After KDP title creation:** paste assigned ISBN onto copyright page → re-export interior PDF → upload.

**Still yours in KDP:** Online Previewer · physical proof · ISBN insert + interior re-export. Do not upload while [`BOOK 1 — KDP PRESUBMIT COMPLIANCE AUDIT.md`](../../04_OUTPUT/Audits/BOOK%201%20—%20KDP%20PRESUBMIT%20COMPLIANCE%20AUDIT.md) has **FAIL** or open **HOLD**.

Listing copy: `02_APPROVED/Product_Specifications/BOOK 1 — KDP LISTING SETUP.md`

**Not this pass:** Book 2 product-text SSW-1 rewrite.
