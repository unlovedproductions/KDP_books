# BOOK 1 — KDP PRESUBMIT COMPLIANCE AUDIT

**Document type:** Collection publish gate (this title)  
**Copied from:** `04_OUTPUT/Audits/KDP PRESUBMIT COMPLIANCE AUDIT.md`  
**Does not override:** Master AI Role → Series Bible → Book 1 Brief → Book 1 MDS  
**Does block:** Upload / Publish while any **FAIL** or unresolved **HOLD** remains  

**This run:** 2026-11-04. Re-export the same evening removed the copyright-page ISBN placeholder. Page count stayed **124**. Cover file was not regenerated; page count and spine math are unchanged.

A compliance audit cannot guarantee KDP approval.

---

## Compliance Doc Brief

Fetched 2026-11-04 from official `kdp.amazon.com/help` only. No skill snapshot existed. The 2026-08-21 auditor report is a prior repo audit, not a substitute for this pull.

| Source | URL | Material points | Fetch |
| --- | --- | --- | --- |
| Content Guidelines | https://kdp.amazon.com/help/topic/G200672390 | Illegal/infringing; offensive; **AI-generated must be disclosed** (substantial edits still count as generated); AI-assisted need not; poor CX / misleading description; undifferentiated public-domain reprints restricted | OK |
| Metadata Guidelines for Books | https://kdp.amazon.com/help/topic/G201097560 | Title = cover title only; no repeating generic keywords in the title; subtitle follows the same rules; title+subtitle under 200 characters; series name is the name only, number is digits in its own field; public-domain and low-content books cannot create a series; description bans URLs, reviews, prices, keyword piles; cover title/subtitle/author/series must match metadata; print needs an ISBN except low-content; a printed ISBN must match title setup | OK |
| Cover Image Guidelines | https://kdp.amazon.com/help/topic/G6GTK3T3NUHKLEFX | **Ebook marketing cover** (JPEG/PNG/GIF/TIFF, 2560×1600 recommended). Not the print-wrap spec | OK |
| Guide to Kindle Content Quality | https://kdp.amazon.com/help/topic/G200952510 | Typos, metadata mismatch, duplicate/missing/wrong content, disappointing content, journals/coloring unsuited to Kindle. Ebook-oriented | OK |
| Create a Paperback Cover | https://kdp.amazon.com/en_US/help/topic/G201953020 | One PDF wrap; spine text only at ≥79 pages; white paper spine = page count × **0.002252"**; **0.125"** bleed on outside edges; front/back text ≥ **0.125"** inside trim; spine text ≥ **0.0625"** from the spine edge; text ≥ **7 pt**; remove template text; embed fonts | OK |
| Set Trim Size, Bleed, and Margins | https://kdp.amazon.com/help/topic/GVBQ3CMEQW3W2VL6 | 6×9 allowed (24–828 pp, black on white). No-bleed outside margins ≥ **0.25"**. For 24–150 pp, inside/gutter ≥ **0.375"** | OK |
| Paperback and Hardcover Manuscript Templates | https://kdp.amazon.com/en_US/help/topic/G201834230 | Leftover template/placeholder text can error on upload or fail review. An ISBN on the copyright page is optional; if printed, it must match the assigned number and the `978-X-XXXX-XXXX-X` form. Text ≥ 7 pt. Embed fonts | OK |
| Low-Content Books | https://kdp.amazon.com/help/topic/GGE5T76TWKA85DJM | Notebooks, diaries/journals, and **prompt journals** are low-content examples (exceptions exist). Low-content cannot take a free KDP ISBN and cannot create a series. If it is low-content and the box is unchecked, KDP says the book will be rejected | OK |

Not on the fetched cover page: the **0.375"** spine top/bottom inset. That figure is the 2026-08-18 quality notice on *Stoic Journal for Men* (PRI-8T0CVEAGEY5), enforced here as a Collection lock. G201953020 states **0.0625"** from the spine edge (the fold), not 0.375" from the top and bottom of the cover.

Fetch failures: none on the pages above. Ebook cover rules are N/A for this print-only package. No ebook file was supplied.

---

## 0. TITLE UNDER AUDIT

| Field | Value |
| --- | --- |
| Book / SKU | Book 1 — *Stoic Foundations* |
| Interior PDF | `03_WORKING/Other_Working_Materials/production/output/Stoic_Foundations_Book1_INTERIOR.pdf` |
| Cover PDF | `03_WORKING/Other_Working_Materials/production/output/Stoic_Foundations_Book1_COVER.pdf` |
| Listing spec | `02_APPROVED/Product_Specifications/BOOK 1 — KDP LISTING SETUP.md` |
| Manuscript | `02_APPROVED/Manuscripts/BOOK 1 — STOIC FOUNDATIONS — MANUSCRIPT.md` |
| Cover source | `cover_book1.py` (`SPINE_TB = 0.375"`, `FOLD_SAFE = 0.0625"`, empty barcode rect) |
| Page count (even) | **124** |
| Trim / interior / paper | 6×9, black-and-white, white paper, no interior bleed |
| Auditor | Presubmit rerun against current files. Not the KDP UI |
| Audit date | 2026-11-04 |
| Overall verdict | **HOLD** — no FAIL. Do not upload this PDF as the final interior. |

---

## 1. VERDICT

| Gate | Result | Blocker if not PASS |
| --- | --- | --- |
| A. Metadata | **PASS** (listing copy) | FAIL or HOLD |
| B. Listing / product type | **HOLD** (ISBN, live nodes, price, AI form, series enrollment) | FAIL or HOLD |
| C. Interior file | **HOLD** (pen test only) | FAIL or HOLD |
| D. Cover / spine | **PASS** (local files and measured ink) | FAIL or HOLD |
| E. Collection / content identity | **PASS** | FAIL or HOLD |
| F. Previewer / proof (human) | **HOLD** | HOLD until done in KDP |
| **OVERALL** | **HOLD** | Any FAIL or open HOLD |

No **FAIL**. Do not click Publish while the HOLDs are open.

---

## A. METADATA

Strings as written in the listing spec, checked against cover text and the copyright page.

| ID | Check | Result |
| --- | --- | --- |
| A1 | Title field = cover title only | **PASS** — *Stoic Foundations*. Front and spine read STOIC FOUNDATIONS. |
| A2 | Cover title / spine title / KDP title identical | **PASS** (files). KDP form not opened. |
| A3 | Author / imprint identical | **PASS** — UnlovedProductions on cover, copyright page, and listing. No spaced “Unloved Productions”. |
| A4 | Series name = series only | **PASS** — listing splits name *The Stoic Collection* and number `1`. |
| A5 | Title + subtitle under 200 characters | **PASS** — 17 + 50 = **67**. The listing’s “68” is off by one. Still under 200. |
| A6 | No sales-rank / promo words | **PASS** |
| A7 | No other-author / other-title stuffing | **PASS** |
| A8 | Generic format-word repeat | **PASS** — *workbook* is in the subtitle only. |
| A9 | Generic format-word once in title | **PASS** — title has none. *Stoic Foundations Journal* is not the title. |
| A10 | Subtitle is a real subtitle | **PASS** — *A Guided Workbook on Judgment, Control, and Assent*. |

| Token | Title | Subtitle | Series | Repeat? |
| --- | --- | --- | --- | --- |
| journal | 0 | 0 | 0 | No |
| notebook | 0 | 0 | 0 | No |
| workbook | 0 | 1 | 0 | No |
| books / gifts / diary / planner / log / coloring | 0 | 0 | 0 | No |

---

## B. LISTING / PRODUCT TYPE

| ID | Check | Result |
| --- | --- | --- |
| B1 | Low-content unchecked | **PASS** (spec). Interior is a sequenced workbook, not a lined-paper product. KDP can still reclassify; that decision is not visible from the files. |
| B2 | AI-generated content | **HOLD**. Guidelines require disclosure of AI-generated text even after edits, and do not require disclosure of AI-assisted text. The files do not show which one this manuscript is. Answer the live form honestly. |
| B3 | Language | **PASS** (spec) — English. |
| B4 | Categories | **HOLD** — nodes are proposals. Confirm the live names. Do not lead with Journaling. |
| B5 | Keywords (7) | **PASS** (spec). No competitor names, “bestselling,” or “free.” |
| B6 | Description | **PASS** (spec). No URL, review, price, or keyword pile. |
| B7 | Description vs title | **PASS** — opens on *Stoic Foundations*. |
| B8 | ISBN | **HOLD** — free ISBN not assigned. |
| B9 | Print options match files | **PASS** — 124 even pages, 432×648 pt, black-and-white, white, no interior bleed. |
| B10 | Price | **HOLD** — set after KDP shows the 124-page print cost. Do not reuse the 116-page Book 2 guess. |
| B11 | Rights | **PASS** (spec) — UnlovedProductions. |
| B12 | Series enrollment | **HOLD** — create *The Stoic Collection* in the KDP UI. |

---

## C. INTERIOR FILE

| ID | Check | Result |
| --- | --- | --- |
| C1 | Print-ready PDF, fonts embedded | **PASS** — six Liberation faces, all embedded subsets (`pdffonts`). |
| C2 | Trim 6×9, no interior bleed | **PASS** — media box 432×648 pt. |
| C3 | Even page count | **PASS** — 124. |
| C4 | Margins / gutter | **PASS** (measured). Body text is about 0.60" on the outer edge and 0.75" on the gutter. Top of body text is about 0.72" from the trim. Footer baseline clearance is 0.357". Official no-bleed minimums for 24–150 pages are 0.25" outside and 0.375" gutter. |
| C5 | No placeholder / template text | **PASS** — re-export has no “insert the number” sentence and no low-content checkbox instruction. |
| C6 | Copyright ISBN matches listing | **PASS** — no ISBN is printed. G201834230 makes that optional. If you later print one, it must match the assigned `978-X-XXXX-XXXX-X` and you must re-export. |
| C7 | Not a blank-grid product | **PASS**. Continuation pages are write-in spreads tied to a named exercise. PDF page 124 is an end leaf (footer only). One end leaf is not an excessive blank-page run. The typesetter’s pad loop (`while n < 116`) did not have to fire: the export is already 124. |
| C8 | Write-in usable with a pen | **HOLD** — physical proof. |

Series page (PDF page ii) lists Book 1, Book 2, and “Later — external blows” with **no retail title**. End matter says the later title is not locked and there are no fake ASINs. No *Stoic Adversity*.

---

## D. COVER / SPINE

Media box **902.106 × 666 pt**. Expected wrap: bleed 0.125" + 6" + spine 0.279248" + 6" + bleed 0.125" = **12.529248" × 9.250"**. Match.

| ID | Check | Result |
| --- | --- | --- |
| D1 | Single wrap, 0.125" bleed | **PASS** |
| D2 | Spine width | **PASS** (formula). 124 × 0.002252" = **0.279248"**. Cover Calculator was not opened. Confirm there before upload; that confirmation sits in F1. |
| D3 | Spine text only if ≥79 pages | **PASS** — 124. |
| D4 | Spine fold inset ≥ 0.0625" | **PASS** (glyph ink). 9 pt Liberation Sans Bold, baseline 3 pt off center. Highest ink in the printed spine string clears the nearer fold by **0.089"**. The other side clears by **0.097"**. |
| D5 | Spine top/bottom ≥ 0.375" | **PASS** (measured). Full spine line is 197 pt wide, centered on the 9" trim. Clearance to the cover edge is **3.13"**. `SPINE_TB = 0.375"`. |
| D6 | Front/back text inside 0.125" | **PASS** (script `SAFE = 0.125"`). Previewer still has to confirm. |
| D7 | Barcode box empty | **PASS** (text extract). No `KDP BARCODE ZONE`. White rect is 2" × 1.2", inset **0.125"** from the back-cover trim (`SAFE`), not the 0.25" Book 2 uses. Empty either way. |
| D8 | Cover metadata match | **PASS** — STOIC FOUNDATIONS, locked subtitle, UnlovedProductions, Book 2 named *Stoic Avoidance*. |
| D9 | Separate fold vs top/bottom constants | **PASS** — `FOLD_SAFE` and `SPINE_TB` are different. |

Spine text is 9 pt, above the 7 pt minimum.

---

## E. COLLECTION / CONTENT IDENTITY

| ID | Check | Result |
| --- | --- | --- |
| E1 | Product type honest | **PASS** — method-install workbook. |
| E2 | Clinical / mystical boundary | **PASS** — disclaimers present. Not trauma treatment, not Jungian shadow. |
| E3 | Series page accurate | **PASS** — no uncommissioned retail title. |
| E4 | Not the rejected *Stoic Journal for Men* SKU | **PASS** |
| E5 | Clone test vs Book 2 | **PASS** — ordinary-incident method install, not the avoidance spine. |

---

## F. PREVIEWER / PROOF

| ID | Result |
| --- | --- |
| F1 Online Previewer | **HOLD** |
| F2 Quality notice | **HOLD** — none can exist until upload |
| F3 Author proof | **HOLD** |
| F4 Content Review mail | **HOLD** — 5-day window if they write |
| F5 Do not resubmit a known metadata fail | **PASS** (guidance). This title is not *Stoic Foundations Journal*. |

---

## Required before Book 1 upload

1. Create the paperback and take the free ISBN in KDP. This interior does not print an ISBN. Leave it that way, or paste the assigned `978-X-XXXX-XXXX-X` and re-export before upload. Do not put the old “insert the number” sentence back.
2. Leave low-content unchecked. Answer the AI form from what actually happened, not from this audit.
3. Confirm live categories. Set the price from the 124-page print cost.
4. Series name field: *The Stoic Collection*. Series number: `1`.
5. Run the Cover Calculator at 124 pages, then Print Previewer, then an author proof.
6. Watch Content Review mail.

---

## Sign-off

| Role | Name | Date | Verdict |
| --- | --- | --- | --- |
| Auditor | Presubmit rerun | 2026-11-04 | **HOLD** — no FAIL |
| Publisher (upload authorized) | | | |

Upload is authorized only if Overall = **PASS** and F1–F3 are **PASS**.
