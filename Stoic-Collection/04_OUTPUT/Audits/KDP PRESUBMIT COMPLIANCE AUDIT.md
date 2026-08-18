# KDP PRESUBMIT COMPLIANCE AUDIT

**Document type:** Collection publish gate  
**Status:** ACTIVE for every KDP upload (paperback first; eBook rows N/A if print-only)  
**Does not override:** Master AI Role → Series Bible → Book Brief → MDS  
**Does block:** Upload / Publish while any **FAIL** or unresolved **HOLD** remains  

**Copy this file per title** into `04_OUTPUT/Audits/` as `BOOK N — KDP PRESUBMIT COMPLIANCE AUDIT.md` (or fill §0–§1 here for a single in-progress title). Evidence stay in the lessons file; this file is the checklist.

**Authorities (read before scoring):**

| Source | What it governs |
| --- | --- |
| [Metadata Guidelines for Books](https://kdp.amazon.com/en_US/help/topic/G201097560) | Title, subtitle, series, description, author, keywords, cover/metadata match |
| [Create a Paperback Cover](https://kdp.amazon.com/en_US/help/topic/G201953020) | Wrap, bleed, spine width, fold inset 0.0625", ≥79 pp for spine text |
| [Content Guidelines](https://kdp.amazon.com/help/topic/G200672390) | Account-level content rules |
| [KDP CONTENT REVIEW LESSONS — STOIC JOURNAL FOR MEN.md](KDP%20CONTENT%20REVIEW%20LESSONS%20%E2%80%94%20STOIC%20JOURNAL%20FOR%20MEN.md) | Live enforcement: `Journal` as title descriptor; spine **0.375"** top/bottom; 5-day review window |
| Series Bible §3.4, §22, §23 | Medium-content workbook; 6×9 B&W; no low-content notebook path |
| Book Brief + Production Locks + Listing Setup | Title/imprint/ISBN/print options for that book |
| Book MDS + Previewer checklist | Interior/cover files, proof |

**Scoring**

| Mark | Meaning | Publish? |
| --- | --- | --- |
| **PASS** | Verified against files / listing copy / KDP UI | Allowed for this row |
| **FAIL** | Violates KDP or a Collection lock | **No upload** |
| **HOLD** | Human decision or KDP UI action still required | **No upload** until cleared or explicitly accepted in writing |
| **N/A** | Does not apply (e.g. no spine text, eBook-only) | Ignore |

Generic format words for metadata scans (KDP examples plus siblings used in this catalog): **journal, notebook, gifts, books, workbook, diary, planner, log, coloring**. Count in title, subtitle, and series name separately.

---

## 0. TITLE UNDER AUDIT

| Field | Value |
| --- | --- |
| Book / SKU | |
| Interior PDF | |
| Cover PDF | |
| Listing spec | |
| Page count (even) | |
| Trim / interior / paper | |
| Auditor | |
| Audit date | |
| Overall verdict | **PASS / FAIL / HOLD** |

---

## 1. VERDICT

| Gate | Result | Blocker if not PASS |
| --- | --- | --- |
| A. Metadata | | FAIL or HOLD |
| B. Listing / product type | | FAIL or HOLD |
| C. Interior file | | FAIL or HOLD |
| D. Cover / spine | | FAIL or HOLD |
| E. Collection / content identity | | FAIL or HOLD |
| F. Previewer / proof (human) | | HOLD until done in KDP |
| **OVERALL** | | Any FAIL or open HOLD |

Do not click Publish on a FAIL. Do not “fix it after they reject it.” Case `#51158280` unpublished a title for a missed 5-day window and warned that repeat noncompliance can hit the **account**.

---

## A. METADATA (KDP title / subtitle / series)

Scan strings exactly as they will be pasted into KDP Details.

| ID | Check | Spec | Result |
| --- | --- | --- | --- |
| A1 | Title field = actual cover title only | No extra descriptors, no keyword lists, no HTML. G201097560. | |
| A2 | Cover title / spine title / KDP title identical | Print: title on front or spine; must match metadata. | |
| A3 | Author / imprint identical on cover, copyright, KDP | Collection lock: **UnlovedProductions** (not “Unloved Productions”). | |
| A4 | Series name = series only | “The Stoic Collection”. No book title, no “Book 2”, no format words inside the series name field. | |
| A5 | Title + subtitle under 200 characters | Official subtitle cap. | |
| A6 | No sales-rank / promo words | Ban: bestselling, #1, free, on sale, limited time. | |
| A7 | No other-author / other-title / trademark stuffing | No “for fans of…”, competitor names, Amazon/KDP/Kindle in publisher field. | |
| A8 | Generic format-word **repeat** | Same generic word (journal, notebook, books, …) in **more than one** of {title, subtitle, series} → **FAIL**. | |
| A9 | Generic format-word **once in title** | If title contains journal/notebook/workbook/etc. as a format descriptor, **HOLD**. Content Review case `#51158280` ordered `"Journal "` removed from the title field as extra descriptive content. Human must accept residual risk or retitle before upload. Format language belongs in description / keywords if it is not the true cover title. | |
| A10 | Subtitle is a real subtitle | Additional information about content — not a second keyword dump. Same prohibitions as title. | |

**Word scan (fill counts):**

| Token | Title | Subtitle | Series | Repeat? |
| --- | --- | --- | --- | --- |
| journal | | | | |
| notebook | | | | |
| workbook | | | | |
| books | | | | |
| gifts | | | | |
| diary / planner / log / coloring | | | | |

---

## B. LISTING / PRODUCT TYPE

| ID | Check | Spec | Result |
| --- | --- | --- | --- |
| B1 | Low-content **unchecked** | Collection: medium-content guided workbook. Never the low-content notebook path. ISBN rules differ. | |
| B2 | AI-generated content | Answer the KDP form honestly for this title. | |
| B3 | Language / primary marketplace | English; marketplace where sales are expected. | |
| B4 | Categories | Live browse nodes; relevant to the book. Not a dump of unrelated nodes. Collection neighborhood: Self-Help / Personal Transformation + Philosophy / Stoicism (verify live). | |
| B5 | Keywords (≤7 boxes) | 2–3 word phrases; accurate. **Allowed:** stoic journal, workbook, etc. **Forbidden:** other authors, other titles, bestselling, free, clinical trauma bait, unrelated tags. | |
| B6 | Description | Pitch the book. No URLs, reviews, testimonials, prices, ads, spoiler dumps, keyword-tag piles. HTML only if KDP-supported. | |
| B7 | Description vs title | Do not repeat a banned title pattern inside the opening line as if it were the Amazon title string. | |
| B8 | ISBN | Free KDP ISBN → paste on copyright → re-export interior → re-upload. Free ISBN ≈ Amazon-only; confirm Expanded Distribution. | |
| B9 | Print options match files | B&W, white (unless Brief says otherwise), 6×9, interior no bleed, page count = PDF page count (even). | |
| B10 | Price | After KDP shows print cost. ≥ print cost + minimum margin. Do not guess from an old page count. | |
| B11 | Rights | You hold publishing rights (UnlovedProductions). | |
| B12 | Series enrollment | Enroll in **The Stoic Collection** only when KDP series rules allow (low-content/public-domain ineligible). Do not stuff series metadata into subtitle as a workaround if it trips A8/A9. | |

---

## C. INTERIOR FILE

| ID | Check | Spec | Result |
| --- | --- | --- | --- |
| C1 | Print-ready PDF | Current KDP interior specs; fonts embedded. | |
| C2 | Trim 6×9; no interior bleed | Unless this Brief overrides. | |
| C3 | Even page count | KDP paperback. | |
| C4 | Margins / gutter | ≥0.5" outer; inside per KDP chart for **this** page count `[[VERIFY KDP]]`. | |
| C5 | No placeholder / template text | KDP rejects lorem, “insert title”, sample ISBN mismatches. | |
| C6 | Copyright / ISBN match listing | After assignment, interior regenerated. | |
| C7 | Not a blank-grid product | Series Bible: sequenced workbook, not lined-paper spine. | |
| C8 | Write-in usable | Line height / fields usable with a pen (proof confirms). | |

---

## D. COVER / SPINE

| ID | Check | Spec | Result |
| --- | --- | --- | --- |
| D1 | Single wrap PDF | Back + spine + front; 0.125" bleed. | |
| D2 | Spine width | White B&W: `pages × 0.002252"`. Recalc after any page-count change. Confirm vs KDP Cover Calculator. | |
| D3 | Spine text only if ≥79 pages | Else no spine text. | |
| D4 | Spine **fold** inset | ≥ **0.0625" (1.6 mm)** from left and right spine edges. G201953020. | |
| D5 | Spine **top/bottom** inset | ≥ **0.375" (9.6 mm)** from top and bottom of the cover. Live KDP quality notice 2026-08-18 (PRI-8T0CVEAGEY5). **0.0625" is not enough on this axis.** | |
| D6 | Front/back text | ≥0.125" inside trim; no text into spine or barcode zone. | |
| D7 | Barcode clearance | Bottom-right back; empty; KDP places barcode. | |
| D8 | Cover metadata match | Title, subtitle (if on cover), author, series match KDP fields. Cover must not mimic another book’s layout to mislead. | |
| D9 | Cover generator vs notice | If the script uses one `SPINE_SAFE` for both fold and top/bottom, treat D5 as **FAIL** until top/bottom is 0.375". | |

---

## E. COLLECTION / CONTENT IDENTITY

| ID | Check | Spec | Result |
| --- | --- | --- | --- |
| E1 | Product type honest | Guided workbook / medium-content — not a quote book, not a blank journal SKU. | |
| E2 | Clinical / mystical boundary | No trauma-treatment claims; no Jungian-mystical positioning; no “man up” / sigma scripts. | |
| E3 | Series page (if present) | Lists Collection titles accurately; no fake scarcity. | |
| E4 | Not the ignored low-content *Stoic Journal for Men* SKU | Architecture: existing SKU is not catalog authority. A new book of that name is Expansion-only after complete redesign. | |
| E5 | Clone test | Not a retitle of a sibling with the same job. | |

---

## F. PREVIEWER / PROOF / SUBMIT PROTOCOL

Human-only in KDP. Agent cannot pass these.

| ID | Check | Spec | Result |
| --- | --- | --- | --- |
| F1 | Online Previewer | No red flags: margins, images, fonts, spine, barcode, even pages. | |
| F2 | Quality notice | If KDP emails “Attention needed”, fix and re-upload. Do not Publish past a red notice. | |
| F3 | Author proof | Physical proof before live (Collection lock for workbooks). | |
| F4 | Watch Content Review mail | Inbox `unlovedproducts@gmail.com`. Reply inside the stated window (was **5 days**). Check spam. One reply thread. | |
| F5 | Do not resubmit a known metadata fail | If they require a new book after a guidelines fail, create a new listing — do not loop the same title string. | |

---

## 2. BOOK 2 RUN — Stoic Shadow Work Journal (2026-08-18)

Filled against current locks and files. Not an upload. Previewer/proof remain human.

| Field | Value |
| --- | --- |
| Book / SKU | Book 2 — *Stoic Shadow Work Journal* |
| Interior | `03_WORKING/Other_Working_Materials/production/output/Stoic_Shadow_Work_Journal_Book2_INTERIOR.pdf` (116 pp) |
| Cover | `03_WORKING/Other_Working_Materials/production/output/Stoic_Shadow_Work_Journal_Book2_COVER.pdf` |
| Listing spec | `02_APPROVED/Product_Specifications/BOOK 2 — KDP LISTING SETUP.md` |
| Cover source | `03_WORKING/Other_Working_Materials/production/cover_book2.py` (`SPINE_SAFE = 0.0625"`) |
| **OVERALL** | **HOLD** (A9 open) **and FAIL** (D5) — **do not upload** |

### Word scan

| Token | Title | Subtitle | Series | Repeat? |
| --- | --- | --- | --- | --- |
| journal | 1 (*Stoic Shadow Work Journal*) | 0 (*A Guided Journey Through Self-Reflection, Virtue & Personal Growth*) | 0 (*The Stoic Collection*) | No |
| notebook | 0 | 0 | 0 | No |
| workbook | 0 | 0 | 0 | No |
| books / gifts / diary / planner / log / coloring | 0 | 0 | 0 | No |

### Scores

| ID | Result | Evidence |
| --- | --- | --- |
| A1–A7, A10 | **PASS** (on listing copy) | Title is a single phrase; subtitle is not a keyword dump; series name clean; imprint lock UnlovedProductions; no bestseller/free/competitor stuffing in listing spec. |
| A8 | **PASS** | Journal is not repeated across title+subtitle+series. This is **not** the dead SKU pattern (*Stoic Journal for Men* + *A Daily Reflection Journal…*). |
| A9 | **HOLD** | Title contains **Journal**. Case `#51158280` ordered that descriptor out of the Amazon title field. Human must retitle or accept residual Content Review risk **in writing** before upload. Keywords may keep “stoic journal”. |
| B1 | **PASS** (spec) | Listing/Production Locks: do not check low-content. |
| B2–B7, B9–B12 | **PASS** (spec) / **HOLD** (B2, B4, B10 until KDP UI) | Categories/nodes and price must be confirmed live. AI form unanswered until upload. |
| B8 | **HOLD** | Free ISBN not yet assigned / not on copyright. |
| C1–C7 | **PASS** (local locks) | 116 pp even; 6×9 B&W white; no bleed; medium-content manuscript. C4/C8 still `[[VERIFY KDP]]` / proof. |
| D4 | **PASS** (intent) | Script keeps 0.0625" at spine folds. |
| D5 / D9 | **FAIL** | `max_spine_text = TRIM_H - 2 * SPINE_SAFE` with `SPINE_SAFE = 0.0625"`. Required top/bottom = **0.375"**. Same class of defect as PRI-8T0CVEAGEY5. |
| D1–D3, D6–D8 | **PASS** (spec) pending Previewer | Wrap + bleed; 116 ≥ 79; barcode zone in script. |
| E1–E5 | **PASS** | Workbook identity; not the ignored blank SKU; Brief/MDS differentiation. |
| F1–F5 | **HOLD** | Not run in KDP. |

### Required before Book 2 upload

1. Fix cover generator: spine text ≥0.375" from top and bottom; keep ≥0.0625" from folds; regenerate wrap; confirm vs Cover Calculator.  
2. Human lock on A9: keep *Stoic Shadow Work Journal* (accept Content Review risk) **or** retitle so the Amazon title field has no generic format descriptor. Do not add Journal/Workbook to the subtitle either way.  
3. Assign ISBN → copyright → re-export interior.  
4. Previewer + author proof.  
5. Watch Content Review mail for 5 days after submit.

Book 1 Option 1 (*Stoic Foundations Journal*) inherits the same A9 HOLD if used as the Amazon title.

---

## 3. SIGN-OFF

| Role | Name | Date | Verdict |
| --- | --- | --- | --- |
| Auditor | | | |
| Publisher (upload authorized) | | | |

Upload is authorized only if Overall = **PASS** and F1–F3 are **PASS**.
