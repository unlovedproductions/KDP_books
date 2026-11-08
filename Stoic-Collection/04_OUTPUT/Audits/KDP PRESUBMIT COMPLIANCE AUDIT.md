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

## 2. LATEST TITLE RUNS

Score each book in its own file. Do not treat the 2026-11-02 Book 2 block as current. That run marked spine-fold clearance PASS at 0.096". The 2026-11-04 measurement of the printed lowercase ascenders is 0.0602", under the 0.0625" rule.

| Book | File | Date | Overall |
| --- | --- | --- | --- |
| 1 *Stoic Foundations* | [BOOK 1 — KDP PRESUBMIT COMPLIANCE AUDIT.md](BOOK%201%20%E2%80%94%20KDP%20PRESUBMIT%20COMPLIANCE%20AUDIT.md) | 2026-11-04 | **HOLD** — no FAIL |
| 2 *Stoic Avoidance* | [BOOK 2 — KDP PRESUBMIT COMPLIANCE AUDIT.md](BOOK%202%20%E2%80%94%20KDP%20PRESUBMIT%20COMPLIANCE%20AUDIT.md) | 2026-11-05 | **HOLD** — title is *Stoic Avoidance*; KDP Previewer, price, ISBN, and proof remain |

Book 1 Option 1 (*Stoic Foundations Journal*) inherits the A9 HOLD if anyone uses it as the Amazon title.

---

## 3. SIGN-OFF

| Role | Name | Date | Verdict |
| --- | --- | --- | --- |
| Auditor | | | |
| Publisher (upload authorized) | | | |

Upload is authorized only if Overall = **PASS** and F1–F3 are **PASS**.
