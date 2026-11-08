# BOOK 2 — KDP PRESUBMIT COMPLIANCE AUDIT

**Document type:** Collection publish gate (this title)  
**Copied from:** `04_OUTPUT/Audits/KDP PRESUBMIT COMPLIANCE AUDIT.md`  
**Does not override:** Master AI Role → Series Bible → Book 2 Brief → Book 2 MDS  
**Does block:** Upload / Publish while any **FAIL** or unresolved **HOLD** remains  

**This run:** 2026-11-04, after the file fixes. Spine ink was remeasured on the new cover. The practice-log pad is gone. Page count is the manuscript’s natural length.

Same official-doc pull as [BOOK 1 — KDP PRESUBMIT COMPLIANCE AUDIT.md](BOOK%201%20%E2%80%94%20KDP%20PRESUBMIT%20COMPLIANCE%20AUDIT.md). Not repeated here.

A compliance audit cannot guarantee KDP approval.

---

## 0. TITLE UNDER AUDIT

| Field | Value |
| --- | --- |
| Book / SKU | Book 2 — *Stoic Avoidance* |
| Interior PDF | `03_WORKING/Other_Working_Materials/production/output/Stoic_Shadow_Work_Journal_Book2_INTERIOR.pdf` |
| Cover PDF | `03_WORKING/Other_Working_Materials/production/output/Stoic_Shadow_Work_Journal_Book2_COVER.pdf` |
| Listing spec | `02_APPROVED/Product_Specifications/BOOK 2 — KDP LISTING SETUP.md` |
| Manuscript | `02_APPROVED/Manuscripts/BOOK 2 — STOIC SHADOW WORK JOURNAL — MANUSCRIPT.md` |
| Cover source | `cover_book2.py` (7 pt spine text, `SPINE_TB = 0.375"`, `FOLD_SAFE = 0.0625"`, empty barcode box inset 0.25") |
| Page count (even) | **102** |
| Trim / interior / paper | 6×9, black-and-white, white paper, no interior bleed |
| Auditor | Presubmit rerun against current files. Not the KDP UI |
| Audit date | 2026-11-04 |
| Overall verdict | **HOLD** — no remaining file FAIL. Do not publish until the HOLDs below are cleared. |

---

## 1. VERDICT

| Gate | Result | Blocker if not PASS |
| --- | --- | --- |
| A. Metadata | **PASS** (listing copy) | FAIL or HOLD |
| B. Listing / product type | **HOLD** | FAIL or HOLD |
| C. Interior file | **HOLD** (pen test only) | FAIL or HOLD |
| D. Cover / spine | **PASS** (measured on this export) | FAIL or HOLD |
| E. Collection / content identity | **PASS** | FAIL or HOLD |
| F. Previewer / proof (human) | **HOLD** | HOLD until done in KDP |
| **OVERALL** | **HOLD** | Any FAIL or open HOLD |

No **FAIL** on the files from this export.

---

## A. METADATA

| ID | Check | Result |
| --- | --- | --- |
| A1 | Title field = cover title only | **PASS** — *Stoic Avoidance*. Front reads STOIC / AVOIDANCE. No format word. |
| A2 | Cover / spine / KDP title | **PASS** (files). Spine text is `STOIC AVOIDANCE · UnlovedProductions`. KDP form not opened. |
| A3 | Author / imprint | **PASS** — UnlovedProductions on cover, copyright page, and listing. |
| A4 | Series name = series only | **PASS** — listing now splits name *The Stoic Collection* and number `2`. |
| A5 | Title + subtitle under 200 | **PASS** — 15 + 55 = **70**. |
| A6 | No sales-rank / promo words | **PASS** |
| A7 | No competitor stuffing | **PASS** |
| A8 | Generic format-word repeat | **PASS** — *workbook* is in the subtitle only. |
| A9 | Generic format-word in the title | **PASS** — *Stoic Avoidance* has none. Retitled 2026-11-05 off *Stoic Shadow Work Journal*. |
| A10 | Subtitle is a real subtitle | **PASS** — *A Guided Workbook on Hidden Patterns and Self-Deception*. |

| Token | Title | Subtitle | Series | Repeat? |
| --- | --- | --- | --- | --- |
| journal | 0 | 0 | 0 | No |
| notebook | 0 | 0 | 0 | No |
| workbook | 0 | 1 | 0 | No |
| books / gifts / diary / planner / log / coloring | 0 | 0 | 0 | No |

The listing no longer tells you to park the series name in the subtitle.

---

## B. LISTING / PRODUCT TYPE

| ID | Check | Result |
| --- | --- | --- |
| B1 | Low-content unchecked | **PASS** (spec). The title no longer contains Journal, and the identical end-page pad is gone. Leave the box unchecked. |
| B2 | AI form | **HOLD** — same rule as Book 1. The files do not prove generated versus assisted. |
| B3 | Language | **PASS** (spec) — English. |
| B4 | Categories | **HOLD** — live node names still have to be confirmed in KDP. The listing no longer leads with Journaling. It now matches Book 1: Philosophy › Stoicism, then Self-Help › Personal Transformation. |
| B5 | Keywords | **PASS** (spec). “Journal” inside a keyword box is allowed. No competitor names, “bestselling,” or “free.” |
| B6 | Description | **PASS** (spec). No URL, review, or price. |
| B7 | Description vs title | **PASS** — the opening uses the real title, then calls the book a guided workbook. |
| B8 | ISBN | **HOLD** — free ISBN not selected in KDP yet. The interior does not print a placeholder. |
| B9 | Print options match the file | **PASS** — 102 even pages, 432×648 pt, black-and-white, white, no interior bleed. |
| B10 | Price | **HOLD** — set it from the live 102-page print cost. |
| B11 | Rights | **PASS** (spec) |
| B12 | Series enrollment | **HOLD** — KDP UI, and only if KDP does not class the book as low-content. |

---

## C. INTERIOR FILE

| ID | Check | Result |
| --- | --- | --- |
| C1 | Fonts embedded | **PASS** — Liberation subsets embedded. |
| C2 | 6×9, no interior bleed | **PASS** — 432×648 pt. |
| C3 | Even page count | **PASS** — 102. |
| C4 | Margins | **PASS** (measured on body pages). Outer about 0.60", gutter about 0.75", top of text about 0.72", footer clearance 0.357". Above the 24–150 page no-bleed minimums (0.25" outside, 0.375" gutter). |
| C5 | Placeholder text | **PASS** — no “insert the number” sentence and no low-content checkbox instruction. |
| C6 | ISBN matches listing | **PASS** — no ISBN is printed. That is optional under G201834230. A later printed number must match the assigned one. |
| C7 | Not lined-paper padding | **PASS**. The post-build PRACTICE LOG loop is gone. Text extract has no “PRACTICE LOG”. PDF page 102 is one blank leaf so the count is even. The manuscript’s own end leaf is page 101 and still carries its sentence. |
| C8 | Pen test | **HOLD** — proof. |

Series pages name Book 1 as *Stoic Foundations* and this book. The later domain is “External blows and endurance. No title until a Project Brief.” No *Stoic Adversity*. No fake ASIN. SSW-1 from 2026-11-02 holds in the PDF.

Contents spot-check, not a full TOC proof: the contents list Chapter 1 at printed page 6, and the chapter opening is labeled “Page 6 — Opening.”

Further Reading tells the reader to verify a later Seneca *Letters* translation before quoting it. That is reader-facing, not a typesetter TODO. It is not the C5 hold.

---

## D. COVER / SPINE

Media box **898.539 × 666 pt**. Expected wrap at 102 pages: **12.479704" × 9.250"**. Match. Spine formula 102 × 0.002252" = **0.229704"** (16.54 pt). Text extract has no `KDP BARCODE ZONE`. Back cover names Book 1 as *Stoic Foundations*.

| ID | Check | Result |
| --- | --- | --- |
| D1 | Single wrap, 0.125" bleed | **PASS** |
| D2 | Spine width vs formula | **PASS** (math). Cover Calculator not opened. |
| D3 | ≥79 pages for spine text | **PASS** — 102. |
| D4 | ≥ 0.0625" from each spine edge | **PASS** (measured on this PDF). |
| D5 | ≥ 0.375" from top and bottom cover edges | **PASS**. The full spine line is 193.7 pt wide and centered on the 9" trim. Clearance to the cover edge is **3.16"**. |
| D6 | Front/back text inset | **PASS** (script). Previewer still required. |
| D7 | Barcode box empty | **PASS**. White 2" × 1.2" rect, inset 0.25" from the spine and the bottom trim. No label text. |
| D8 | Metadata match | **PASS** (files) — subject to A4/A9 on the KDP form. |
| D9 | Fold constant separate from top/bottom | **PASS** — the script has both. The drawn baseline does not use the fold budget. See D4. |

### D4 evidence

The cover script centers the Liberation Sans Bold em-box on the spine instead of putting the baseline on the center line. On the exported PDF, every spine word’s ink box is x 445.98–452.55 pt. The spine runs x 441.00–457.54 pt.

- Clearance to the left fold: **0.0692"**
- Clearance to the right fold: **0.0693"**
- Required: **0.0625"**

7 pt is still the type size. Top and bottom clearance is unchanged: the same line, centered on the 9" trim, is several inches inside the 0.375" cover-edge lock.

---

## E. COLLECTION / CONTENT IDENTITY

| ID | Check | Result |
| --- | --- | --- |
| E1 | Workbook, not a quote book | **PASS** on the body. The pad pages are C7, not a second identity. |
| E2 | No trauma-treatment or Jungian claim | **PASS** — cover and series page say so. |
| E3 | Series page | **PASS** — *Stoic Foundations* plus this book. No locked Book 3 title. |
| E4 | Not the rejected men’s-journal file | **PASS** — different interior and cover. The shared risk is the word Journal, scored at A9. |
| E5 | Not a Book 1 clone | **PASS** — avoidance and pattern-naming, not the method-install spine. |

---

## F. PREVIEWER / PROOF

| ID | Result |
| --- | --- |
| F1–F4 | **HOLD** — not run. Run them on this 102-page export. |
| F5 | **PASS** (guidance). Do not resubmit *Stoic Journal for Men*. |

---

## Required before Book 2 upload

1. Title is *Stoic Avoidance*. Do not put Journal back in the Amazon title field.
2. Take the free ISBN in KDP. Do not put a placeholder sentence back on the copyright page.
3. Cover Calculator at 102 pages, then Print Previewer, then an author proof. Set the price from that print cost. Answer the AI form. Leave low-content unchecked.
4. Series name *The Stoic Collection*, series number `2`.

The MDS still says 116–124. This export is 102 because that is the manuscript once the pad is removed. Do not add lined pages to close the gap.

---

## Sign-off

| Role | Name | Date | Verdict |
| --- | --- | --- | --- |
| Auditor | Presubmit rerun | 2026-11-04 | **HOLD** — no file FAIL |
| Publisher (upload authorized) | | | |

Upload is authorized only if Overall = **PASS** and F1–F3 are **PASS**.
