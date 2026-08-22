# BOOK 1 — KDP PRESUBMIT COMPLIANCE AUDIT

**Document type:** Collection publish gate (this title)  
**Copied from:** `04_OUTPUT/Audits/KDP PRESUBMIT COMPLIANCE AUDIT.md`  
**Does not override:** Master AI Role → Series Bible → Book 1 Brief → Book 1 MDS  
**Does block:** Upload / Publish while any **FAIL** or unresolved **HOLD** remains  

**Authorities scored this pass:** [Metadata Guidelines G201097560](https://kdp.amazon.com/en_US/help/topic/G201097560) (fetched 2026-08-21); [Paperback cover G201953020](https://kdp.amazon.com/en_US/help/topic/G201953020); `KDP CONTENT REVIEW LESSONS — STOIC JOURNAL FOR MEN.md`; Book 1 Brief v1.0; Production Locks 2026-08-21; `BOOK 1 — KDP LISTING SETUP.md`; interior/cover PDFs this export.

---

## 0. TITLE UNDER AUDIT

| Field | Value |
| --- | --- |
| Book / SKU | Book 1 — *Stoic Foundations* |
| Interior PDF | `03_WORKING/Other_Working_Materials/production/output/Stoic_Foundations_Book1_INTERIOR.pdf` |
| Cover PDF | `03_WORKING/Other_Working_Materials/production/output/Stoic_Foundations_Book1_COVER.pdf` |
| Listing spec | `02_APPROVED/Product_Specifications/BOOK 1 — KDP LISTING SETUP.md` |
| Cover source | `cover_book1.py` (`SPINE_TB = 0.375"`, `FOLD_SAFE = 0.0625"`) |
| Page count (even) | **124** |
| Trim / interior / paper | 6×9, B&W, white, no interior bleed |
| Auditor | Editorial/production pass (files + listing copy; not KDP UI) |
| Audit date | 2026-08-21 |
| Overall verdict | **HOLD** — no FAIL on local files/listing. Do not upload until HOLDs below clear. |

---

## 1. VERDICT

| Gate | Result | Blocker if not PASS |
| --- | --- | --- |
| A. Metadata | **PASS** (listing copy) | FAIL or HOLD |
| B. Listing / product type | **HOLD** (ISBN, live nodes, price, AI form) | FAIL or HOLD |
| C. Interior file | **HOLD** (ISBN placeholder; Previewer) | FAIL or HOLD |
| D. Cover / spine | **PASS** (script + wrap math) pending Previewer / Cover Calculator | FAIL or HOLD |
| E. Collection / content identity | **PASS** | FAIL or HOLD |
| F. Previewer / proof (human) | **HOLD** | HOLD until done in KDP |
| **OVERALL** | **HOLD** | Any FAIL or open HOLD |

No **FAIL**. Do not click Publish on open HOLDs. Case `#51158280` unpublished a title for a missed 5-day window.

---

## A. METADATA (KDP title / subtitle / series)

Scan strings exactly as they will be pasted into KDP Details.

| ID | Check | Spec | Result |
| --- | --- | --- | --- |
| A1 | Title field = actual cover title only | No extra descriptors. G201097560. | **PASS** — *Stoic Foundations* |
| A2 | Cover title / spine title / KDP title identical | Front + spine: STOIC FOUNDATIONS | **PASS** (files) |
| A3 | Author / imprint identical | **UnlovedProductions** | **PASS** (cover, copyright, listing) |
| A4 | Series name = series only | “The Stoic Collection” | **PASS** (listing spec) |
| A5 | Title + subtitle under 200 characters | 68 characters combined | **PASS** |
| A6 | No sales-rank / promo words | No bestselling / free / on sale | **PASS** |
| A7 | No other-author / other-title stuffing | No competitor names | **PASS** |
| A8 | Generic format-word **repeat** | Same generic word in more than one of {title, subtitle, series} | **PASS** — *workbook* in subtitle only |
| A9 | Generic format-word **once in title** | Journal/notebook/workbook in the **title** field | **PASS** — title has none. Locked against Book 1 Option 1 (*Stoic Foundations Journal*). |
| A10 | Subtitle is a real subtitle | Not a keyword dump | **PASS** — locked domain subtitle; *Workbook* is format-honest once |

**Word scan (listing copy):**

| Token | Title | Subtitle | Series | Repeat? |
| --- | --- | --- | --- | --- |
| journal | 0 | 0 | 0 | No |
| notebook | 0 | 0 | 0 | No |
| workbook | 0 | 1 (*A Guided Workbook…*) | 0 | No |
| books | 0 | 0 | 0 | No |
| gifts | 0 | 0 | 0 | No |
| diary / planner / log / coloring | 0 | 0 | 0 | No |

---

## B. LISTING / PRODUCT TYPE

| ID | Check | Spec | Result |
| --- | --- | --- | --- |
| B1 | Low-content **unchecked** | Medium-content guided workbook | **PASS** (spec) |
| B2 | AI-generated content | Honest KDP form | **HOLD** — unanswered until upload |
| B3 | Language / marketplace | English | **PASS** (spec) |
| B4 | Categories | Philosophy / Stoicism + Self-Help / Personal Transformation; not Journaling-led | **HOLD** — confirm live nodes in KDP |
| B5 | Keywords (≤7) | Brief-allowed; no shadow-work identity; no competitor titles | **PASS** (spec) |
| B6 | Description | Pitch; no URLs/reviews/prices | **PASS** (spec) |
| B7 | Description vs title | Opening uses *Stoic Foundations*, not a banned title pattern | **PASS** |
| B8 | ISBN | Free KDP ISBN → copyright → re-export | **HOLD** — not assigned |
| B9 | Print options match files | B&W, white, 6×9, no bleed, **124** even | **PASS** (files) |
| B10 | Price | After KDP shows print cost for **124** pp | **HOLD** |
| B11 | Rights | UnlovedProductions | **PASS** (spec) |
| B12 | Series enrollment | Create *The Stoic Collection* on this title | **HOLD** — KDP UI |

---

## C. INTERIOR FILE

| ID | Check | Spec | Result |
| --- | --- | --- | --- |
| C1 | Print-ready PDF | 6×9 (432×648 pt); fonts embedded (Liberation subset) | **PASS** (local) |
| C2 | Trim 6×9; no interior bleed | Matches Brief | **PASS** |
| C3 | Even page count | 124 | **PASS** |
| C4 | Margins / gutter | Script: gutter 0.75", outer 0.60" (≥0.5" outer) | **HOLD** — `[[VERIFY KDP]]` in Previewer for 124 pp |
| C5 | No placeholder / template text | Copyright still says insert KDP ISBN | **HOLD** — B8 path; not lorem |
| C6 | Copyright / ISBN match listing | After assignment | **HOLD** |
| C7 | Not a blank-grid product | Sequenced workbook; no end-of-book filler logs this export | **PASS** |
| C8 | Write-in usable | Line fields present | **HOLD** — physical proof |

---

## D. COVER / SPINE

| ID | Check | Spec | Result |
| --- | --- | --- | --- |
| D1 | Single wrap PDF | Back + spine + front; 0.125" bleed; wrap 12.529248" × 9.25" | **PASS** (file + sidecar) |
| D2 | Spine width | 124 × 0.002252" = **0.279248"** | **PASS** (math) **HOLD** confirm Cover Calculator |
| D3 | Spine text only if ≥79 pages | 124 ≥ 79 | **PASS** |
| D4 | Spine **fold** inset | `FOLD_SAFE = 0.0625"` | **PASS** (script) |
| D5 | Spine **top/bottom** inset | `SPINE_TB = 0.375"`; `max_spine_text = TRIM_H - 2 * SPINE_TB` | **PASS** (script) — unlike Book 2 `cover_book2.py` |
| D6 | Front/back text | `SAFE = 0.125"` inside trim | **PASS** (script) pending Previewer |
| D7 | Barcode clearance | Bottom-right back white zone | **PASS** (script) |
| D8 | Cover metadata match | STOIC FOUNDATIONS + locked subtitle + UnlovedProductions + Book 1 | **PASS** |
| D9 | Cover generator vs notice | Separate fold vs top/bottom constants | **PASS** |

---

## E. COLLECTION / CONTENT IDENTITY

| ID | Check | Spec | Result |
| --- | --- | --- | --- |
| E1 | Product type honest | Method-install guided workbook | **PASS** |
| E2 | Clinical / mystical boundary | Disclaimers + listing; no trauma/Jung positioning | **PASS** |
| E3 | Series page | Book 1 *Stoic Foundations*; Book 2 *Stoic Shadow Work Journal*; no fake ASINs | **PASS** |
| E4 | Not the ignored *Stoic Journal for Men* SKU | Different title, job, and metadata pattern | **PASS** |
| E5 | Clone test | Ordinary-incident method install; not Book 2 avoidance spine | **PASS** |

---

## F. PREVIEWER / PROOF / SUBMIT PROTOCOL

Human-only in KDP. Agent cannot pass these.

| ID | Check | Result |
| --- | --- | --- |
| F1 | Online Previewer | **HOLD** |
| F2 | Quality notice | **HOLD** |
| F3 | Author proof | **HOLD** |
| F4 | Watch Content Review mail | **HOLD** — inbox; 5-day window if they write |
| F5 | Do not resubmit a known metadata fail | **PASS** (guidance) — this title is not Option 1 *Stoic Foundations Journal* |

---

## Required before Book 1 upload

1. Create the KDP paperback title. Paste listing fields exactly. Confirm live category nodes (B4).  
2. Assign free ISBN → copyright page → `typeset_book1.py` → re-upload interior (B8/C5/C6).  
3. Confirm 124-page spine in KDP Cover Calculator (D2).  
4. Online Previewer: margins, fonts, spine 0.375″ top/bottom, barcode (C4, D6, F1).  
5. Set price from **this** print cost, not Book 2’s 116-page guess (B10).  
6. Physical proof (F3).  
7. Answer the AI-content form honestly (B2).  
8. Watch Content Review mail for 5 days after submit (F4).

Do not upload on this HOLD. Do not “fix it after they reject it.”

---

## 3. SIGN-OFF

| Role | Name | Date | Verdict |
| --- | --- | --- | --- |
| Auditor | Files + listing copy (2026-08-21) | 2026-08-21 | **HOLD** — no FAIL |
| Publisher (upload authorized) | | | |

Upload is authorized only if Overall = **PASS** and F1–F3 are **PASS**.
