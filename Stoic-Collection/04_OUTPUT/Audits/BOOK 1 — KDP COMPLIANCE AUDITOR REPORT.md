# BOOK 1 — KDP COMPLIANCE AUDITOR REPORT

**Title:** Stoic Foundations  
**Format audited:** Paperback (no ebook file supplied)  
**Auditor:** kdp-compliance-auditor skill  
**Date accessed (official Help):** 2026-08-21  
**Interior:** `Stoic-Collection/03_WORKING/Other_Working_Materials/production/output/Stoic_Foundations_Book1_INTERIOR.pdf`  
**Cover:** `Stoic-Collection/03_WORKING/Other_Working_Materials/production/output/Stoic_Foundations_Book1_COVER.pdf`  
**Listing:** `Stoic-Collection/02_APPROVED/Product_Specifications/BOOK 1 — KDP LISTING SETUP.md`  
**Manuscript (content/IP):** `Stoic-Collection/02_APPROVED/Manuscripts/BOOK 1 — STOIC FOUNDATIONS — MANUSCRIPT.md`

A compliance audit cannot guarantee KDP approval.

---

## 0. Compliance Doc Brief

Mandatory pages fetched 2026-08-21 (official `kdp.amazon.com/help` only):

| Source | URL | Material points | Fetch |
| --- | --- | --- | --- |
| Content Guidelines | https://kdp.amazon.com/help/topic/G200672390 | Illegal/infringing; offensive; **AI-generated must be disclosed** (edits after generation still count as generated); AI-assisted need not be disclosed; poor CX / misleading metadata; undifferentiated PD reprints restricted | OK |
| Metadata Guidelines for Books | https://kdp.amazon.com/help/topic/G201097560 | Title = cover title only; no repeating generic keywords (notebook, journal, gifts, books, etc.) in **title field**; subtitle follows **same** title rules; title+subtitle &lt; 200 chars; PD/low-content ineligible for series; description bans URLs, reviews, keyword stuffing, promo; cover title/subtitle/author/series must match metadata; paperback needs ISBN except low-content | OK |
| Cover Image Guidelines | https://kdp.amazon.com/help/topic/G6GTK3T3NUHKLEFX | **Ebook marketing cover** specs (2560×1600 rec, RGB, no price, title+author). Not the print wrap spec | OK |
| Guide to Kindle Content Quality | https://kdp.amazon.com/help/topic/G200952510 | Duplicate text, missing content, wrong content, journals/coloring unsuited to **Kindle**; placeholder/unfinished content | OK |

Paperback siblings followed from those pages:

| Source | URL | Material points | Fetch |
| --- | --- | --- | --- |
| Create a Paperback Cover | https://kdp.amazon.com/en_US/help/topic/G201953020 | Single PDF wrap; spine text only if ≥79 pp; white paper spine = page count × **0.002252"**; add **0.125"** bleed all outside edges; front/back text ≥ **0.125"** inside trim; spine text ≥ **0.0625"** from spine edge; 0.0625" fold variance; KDP can place barcode | OK |
| Set Trim Size, Bleed, and Margins | https://kdp.amazon.com/help/topic/GVBQ3CMEQW3W2VL6 | 6×9 allowed; no-bleed outside/top/bottom min **0.25"**; 24–150 pp gutter min **0.375"** | OK |
| Paperback and Hardcover Manuscript Templates | https://kdp.amazon.com/en_US/help/topic/G201834230 | Remaining **placeholder text** may error on upload or reject on review; ISBN on copyright if present must match assigned number; 7-pt min; embed fonts; proof copy recommended | OK |
| Paperback Submission Guidelines | https://kdp.amazon.com/help/topic/G201857950 | Same margin table; PDF preferred | OK |
| Low-Content Books | https://kdp.amazon.com/help/topic/GGE5T76TWKA85DJM | Minimal/repetitive fill-in; **prompt journals** listed as low-content; if it **is** low-content and the box is not checked, KDP says it will be rejected; low-content cannot use free KDP ISBN or create a series | OK |
| Intellectual Property Rights FAQ | https://kdp.amazon.com/help/topic/G200672400 | Must hold publishing rights; copyright page is **not** proof of rights; KDP may request docs | OK |
| Publishing Public Domain Content | https://kdp.amazon.com/help/topic/G200743940 | Undifferentiated PD reprints restricted; PD **product** must mark (Translated)/(Annotated)/(Illustrated) **in title** — this applies to publishing a PD **work**, not quoting PD in an original book; rights radio: own copyright vs “this is a public domain work” | OK |
| Paperback Fonts | https://kdp.amazon.com/help/topic/G202145450 | Min **7 pt**; embed all fonts; publisher responsible for font licenses | **Timeout** on full page; min-size/embed taken from official URL snippet. Fonts topic = **Verification required** for anything beyond that |
| Keywords help | https://kdp.amazon.com/help/topic/G201298500 | Accurate descriptors; up to 7 phrases | OK (search + metadata page) |

Fetch failures (do not invent those rules): `G201647230` 404, `G201920040` 404, `G202145450` timeout (partial).

No prior skill snapshot existed. Live pull is the source for this run.

---

## 1. Overall Assessment

**Publish readiness:** Do Not Submit Yet  

**Overall risk:** High  

**Materials actually reviewed:**
- Approved manuscript (content, quotes, disclaimers)
- Interior PDF (124 pp, 6×9, fonts, placeholders, TOC vs pagination)
- Print cover wrap PDF (one page, dimensions, extracted text)
- Listing setup (title/subtitle/series/keywords/description/print options)
- Production locks / typesetter behavior as reflected in those PDFs

**Materials not reviewed:**
- Live KDP title-setup form / Previewer
- KDP Cover Calculator PNG for this ISBN/page count
- Physical proof
- Ebook/EPUB (not supplied)
- Font license files on disk
- Live Amazon category nodes
- Assigned ISBN (does not exist yet)

**Top 5 Issues**

1. Interior copyright still contains ISBN **placeholder** (“insert the number Amazon assigns…”). Official template help: leftover placeholder text can fail upload or review.
2. Cover prints visible **“KDP BARCODE ZONE”** in the barcode box. Placeholder / template text on a print cover.
3. Printed **TOC page numbers do not match** chapter starts (off by 1–5 arabic pages). Quality / CX / “missing or wrong content” risk.
4. Manuscript text was produced with an AI-based tool. Current Content Guidelines: disclose as **AI-generated** (edits after generation still count). Cover/interior art is code-drawn, not AI image — disclose **text** honestly.
5. KDP Print Previewer + Cover Calculator + physical proof not run. Trim/margin/spine cannot be declared live-compliant from this workstation.

---

## 2. Critical Issues

**Risk:** Critical  
**Type:** Publication / Quality  
**Finding:** Copyright page still contains unfinished ISBN instructions.  
**Evidence:** Interior PDF p. iv: `ISBN: Free KDP ISBN — insert the number Amazon assigns when the paperback title is created, then re-export the interior before final upload.`  
**Why it matters:** G201834230 — remaining placeholder/template text may error on upload or be rejected on review. G201097560 — if an ISBN is printed, it must match title setup. This string is not a valid ISBN.  
**Status:** Observed  
**Recommended action:** Create the KDP paperback, accept the free ISBN, paste it on the copyright page, re-run `typeset_book1.py`, re-export interior, then upload. Do not upload this PDF as final.  
**Confidence:** High  

No other Critical issues in the supplied files. Barcode-zone label is High (next section), not Critical, because KDP states it will overprint a barcode in that rectangle.

---

## 3. High-Risk Issues

**Risk:** High  
**Type:** Publication / Quality  
**Finding:** Cover barcode rectangle contains the printed words `KDP BARCODE ZONE`.  
**Evidence:** `cover_book1.py` draws that string; cover PDF text extract includes it.  
**Why it matters:** Template/placeholder text. G201953020 — KDP will place a barcode in a 2" × 1.2" box and cover objects there; Previewer/reviewers can still see the label before overprint.  
**Status:** Observed  
**Recommended action:** Remove the label. Keep an empty white 2" × 1.2" box. Re-export cover.  
**Confidence:** High  

**Risk:** High  
**Type:** Quality / Publication  
**Finding:** Table of contents arabic numbers do not match printed chapter starts.  
**Evidence:** TOC (interior p. viii) vs first “Chapter N” pages:

| TOC line | TOC # | Actual arabic start |
| --- | ---: | ---: |
| Introduction | 1 | 1 (body starts; no matching heading) |
| 1. Start With the Method | 6 | **7** |
| 2. What Hits the Mind | 16 | **17** |
| 3. Facts and Additions | 26 | **28** |
| 4. Up to You | 36 | **38** |
| 5. Before You Assent | 46 | **48** |
| 6. Ownership Without Abuse | 56 | **59** |
| 7. Virtue Tests the Next Act | 66 | **69** |
| 8. Review Until It Is Ordinary | 76 | **79** |
| Integration | 86 | ~**90** (no matching section title on the page) |
| Stoic Terminology | 94 | ~**99** |
| Sources & Citations | 101 | ~**105** |
| Further Reading | 106 | ~**110** |
| The Stoic Collection | 109 | **113** |

**Why it matters:** G200952510 missing/wrong content; G201834230 says details in the file must match. Customers using the TOC will land on the wrong page. Returns / Content Quality complaints.  
**Status:** Observed  
**Recommended action:** Rebuild TOC from typeset page numbers; re-export. Do not upload with this TOC.  
**Confidence:** High  

**Risk:** High  
**Type:** KDP Policy  
**Finding:** Text content of this title was created with an AI-based tool.  
**Evidence:** Production history of the approved manuscript in this repo; listing currently says only “Answer honestly per KDP form.”  
**Why it matters:** G200672390 — AI-generated = content created by an AI tool, **even after substantial edits**. Disclosure is required at publish/republish. AI-assisted (human-wrote, AI-edited) is different and need not be disclosed. Treating this manuscript as “assisted only” would be inaccurate. Cover/interior images are reportlab-drawn, not AI artwork.  
**Status:** Observed (text generation process); Unverified (exact KDP form wording at click-time — confirm the live checkbox)  
**Recommended action:** At title setup, disclose **AI-generated text**. Do not disclose AI-generated **images** unless you add some. You are not required to disclose AI-assisted editing.  
**Confidence:** High  

**Risk:** High  
**Type:** Technical / Publication  
**Finding:** Print Previewer, Cover Calculator, and a physical proof have not been run.  
**Evidence:** Not in supplied materials.  
**Why it matters:** G201953020 tells you to use the calculator; G201834230 recommends a proof. Workstation math can match the published formula and still fail Previewer.  
**Status:** Unverified  
**Recommended action:** After ISBN + TOC + barcode-label fixes, upload as draft, pass Previewer, order proof, then publish.  
**Confidence:** High  

---

## 4. Medium/Low-Risk Issues

**Risk:** Medium  
**Type:** Metadata  
**Finding:** Keyword `stoic journal` is a weak / possibly inaccurate descriptor for this product.  
**Evidence:** Listing keyword 4; cover copy: “Not a blank journal.”; G201097560 / G201298500 — keywords must accurately describe the book; prohibited to mislead. Interior is a method workbook with substantial instructional chapters, not a blank/prompt-only journal.  
**Why it matters:** Search mismatch and CX. Also feeds a “this is a journal / low-content” read.  
**Status:** Observed (keyword present); Inferred (reviewer reaction)  
**Recommended action:** Replace with an accurate phrase already in the book (e.g. keep `stoic workbook` / `guided stoic practice`). Do not drop Workbook from the **subtitle** — that string is on the cover and must match metadata.  
**Confidence:** Medium  

**Risk:** Medium  
**Type:** Publication (inferred)  
**Finding:** KDP’s low-content table lists **prompt journals**. This book contains worksheets plus long original lessons.  
**Evidence:** GGE5T76TWKA85DJM table; interior chapters are instructional, not empty/repetitive fill-in; copyright and listing say do not check low-content.  
**Why it matters:** If Amazon **classifies** it as low-content and the box is unchecked, their help text says rejection. Checking the box anyway costs free ISBN and **series** eligibility (G201097560).  
**Status:** Inferred  
**Recommended action:** Do **not** check low-content. Do not put Journal in the Amazon **title** field. Keep instructional density. Watch Content Review mail.  
**Confidence:** Medium  

**Risk:** Medium  
**Type:** Metadata  
**Finding:** Subtitle contains `Workbook`. Title-field rules also apply to subtitle (G201097560). Prohibited examples name notebook/journal/gifts/books — not “workbook.” Cover subtitle matches listing.  
**Why it matters:** Format word in subtitle is the locked identity. Stripping it would **mismatch** the cover (also a metadata violation). Residual review risk from a sibling SKU that put Journal in the **title**.  
**Status:** Observed (string); Inferred (review risk)  
**Recommended action:** Leave title = `Stoic Foundations` only; leave subtitle as locked. Do not also put Workbook in series name.  
**Confidence:** Medium  

**Risk:** Low  
**Type:** Quality  
**Finding:** Last interior page (arabic 116 / PDF 124) is essentially empty except running header.  
**Evidence:** Extracted text is only `116` + `Stoic Foundations`. Even page count is required for print.  
**Why it matters:** Trailing near-blank pages annoy some reviewers/customers; usually tolerated to keep even count.  
**Status:** Observed  
**Recommended action:** Prefer a real closer line on 116, or accept the even-count pad after proof.  
**Confidence:** High  

**Risk:** Low  
**Type:** Copyright-IP  
**Finding:** Font license files were not opened this run. Fonts are Liberation family, all **embedded** (`pdffonts`: emb=yes). G202145450 full page timed out.  
**Status:** Unverified (license); Observed (embedding)  
**Recommended action:** Confirm SIL OFL (or equivalent) for Liberation before upload.  
**Confidence:** Medium  

---

## 5. Ebook Audit

Not supplied. No EPUB/KPF. G6GTK3T3NUHKLEFX (ebook marketing cover) does not apply to this paperback wrap.

Guide to Kindle Content Quality: journals/workbooks meant to be written in are **unsuited to Kindle**. Do not ship this interior as a Kindle ebook without a separate, non-fill-in edition.

---

## 6. Paperback/Hardcover Audit

Hardcover not supplied.

**Trim / pages (Observed):** Interior MediaBox 432×648 pt = 6×9 in. 124 pages, even. No-bleed page size matches trim (not 6.125×9.25).

**Spine (Observed vs G201953020):** White B&W: `124 × 0.002252" = 0.279248"`. Cover MediaBox width 902.1059 pt = **12.529248 in**, height 666 pt = **9.25 in**. Formula: `0.125 + 6 + 0.279248 + 6 + 0.125` = 12.529248; height `9 + 0.25` = 9.25. **Matches the fetched cover equation.** Still Unverified against the live Cover Calculator PNG.

**Spine text eligibility (Observed):** 124 ≥ 79. Spine text allowed.

**Margins (Inferred from typesetter / Unverified in Previewer):** Gutter 0.75" and outer 0.60" exceed the 24–150 pp floor (gutter 0.375" / no-bleed outer 0.25"). Footer sits ~0.38" from trim (> 0.25"). Previewer is the authority.

**Fonts (Observed):** Liberation Sans/Serif (regular/bold/italic/bold-italic) embedded and subsetted. Body well above 7 pt. Full fonts Help page timed out.

**Placeholders (Observed):** ISBN instruction on p. iv; barcode-zone label on cover. TOC numbers stale.

**Blank / junk pages:** No 31-page pad. Last page is a thin even-count leaf.

**Print options to select in KDP:** B&W, white paper, 6×9, no interior bleed, do not check low-content.

---

## 7. Metadata Audit

| Field | Listing | Cover / interior | Verdict |
| --- | --- | --- | --- |
| Title | Stoic Foundations | Front: STOIC FOUNDATIONS; spine: STOIC FOUNDATIONS | Match. No journal/workbook/notebook in **title field**. |
| Subtitle | A Guided Workbook on Judgment, Control, and Assent | Front wrap matches | Match. 68 chars combined (&lt; 200). |
| Series | The Stoic Collection / #1 | Cover: THE STOIC COLLECTION — BOOK 1 | Series **name** field must be name only (no “Book 1”). Number goes in series number. Cover may show Book 1. |
| Author / imprint | UnlovedProductions | Cover + copyright | Match. |
| ISBN | Free KDP, not assigned | Placeholder on p. iv | **Not ready.** |
| Description | Method workbook; names SSOCR as publishing method; points to Book 2 by **your** title | Consistent with contents | No URLs, reviews, “bestselling,” or “free.” Mentions Book 2 *Stoic Shadow Work Journal* (own series, not a competitor keyword). |
| Categories | Philosophy/Stoicism + Self-Help/Personal Transformation; not Journaling-led | Matches book job | Live nodes Unverified. |
| Keywords | 7 Brief-allowed phrases including `stoic journal` | — | See Medium finding. |
| Low-content | Do not check | Substantial original chapters | Correct for this file set. |
| Rights radio | Own copyright (listing) | Original workbook quoting US PD Long 1890 / Stewart 1889 | Choose **I own the copyright…** Do **not** select “This is a public domain work.” This is not a PD reprint of Enchiridion. |
| AI form | “Answer honestly” | AI-generated **text** | Must disclose generated text. |

---

## 8. Cover Audit

**Ebook cover:** Not supplied / N/A.

**Print cover:**

- Single-page PDF wrap: back + spine + front. Observed.
- Title / subtitle / UnlovedProductions / series line present and consistent with listing. Observed.
- No price, no “bestselling,” no watermark. Observed.
- Wrap size matches G201953020 white-paper formula for 124 pp. Observed.
- Official **text inset** on that page is **0.125"** inside trim, not 0.375". Book 1 uses a tighter house 0.375" top/bottom (from a prior Support case, **not** on the fetched Help page). That is more conservative than the Help minimum. Status: house extra; Unverified as a current Help requirement.
- Fold/spine clearance 0.0625" is on G201953020. Unverified in Previewer.
- **KDP BARCODE ZONE** printed in the barcode rectangle. High. Remove label.
- Cover is code-filled (no stock photo, no AI image). Observed.

---

## 9. Copyright / IP Audit

**Observed**

- Original instructional workbook under © 2026 UnlovedProductions.
- Direct quotations attributed to George Long (1890) Epictetus/Marcus and Aubrey Stewart (1889) Seneca *De Ira*; copyright page states US public domain.
- SSOCR / Control Sort labeled as publishing-created, not ancient.
- Disclaimer: not therapy/medical/legal advice; 988 for crisis.
- No Hard/Hays/Graver & Long *Letters* as quotation sources in the copyright translations list.
- Interior/cover have no photographic stock that we could inspect.

**Requires verification (not claimed as infringement)**

- Confirm quote blocks still match the Source Verification Report after typesetting.
- Font license for Liberation (embedding observed; license file not read).
- Do not upload copyrighted modern translations later without a license.
- G200672400: copyright page is not proof of rights if KDP asks.

**Not a PD title under G200743940.** Do not put `(Annotated)` in the Amazon title or pick the PD rights radio.

---

## 10. AI Content Audit

| Asset | Classification | Disclose? |
| --- | --- | --- |
| Manuscript / interior text | **AI-generated** (created by an AI-based tool; later edits do not reclassify it under G200672390) | **Yes — text** |
| Cover art | Not AI-generated image (reportlab geometry/type) | No image disclosure unless you add AI art |
| Interior diagrams/lines | Code-drawn | No |
| Typesetting | Software, not generative AI content | No |

Do not claim “AI-assisted only” for this manuscript. Confirm the live KDP wording when you click the boxes.

---

## 11. Required Changes Before Submission

**Priority 1 — Must Resolve**

1. Assign free KDP ISBN → put the real number on p. iv → re-typeset interior.  
2. Delete cover text `KDP BARCODE ZONE`; keep empty white barcode box; re-export cover.  
3. Rebuild TOC to match typeset arabic pages; re-export.  
4. On the KDP form: disclose **AI-generated text**; do **not** check low-content; rights = own copyright.  
5. Title field = `Stoic Foundations` only. Subtitle as locked. Series name = `The Stoic Collection`, number `1`.

**Priority 2 — Should Resolve**

6. Replace keyword `stoic journal` with an accurate non-journal phrase.  
7. Run KDP Cover Calculator at 124 pp, B&W white, 6×9; confirm wrap.  
8. Pass Print Previewer; fix any margin/spine/barcode flags.  
9. Confirm Liberation font license.

**Priority 3 — Verify/Consider**

10. Physical proof.  
11. Live category nodes (Stoicism + Personal Transformation).  
12. Price from **124-pp** print cost, not a 116-pp guess.  
13. Watch Content Review mail (~5 days). A compliance audit cannot predict that outcome.  
14. Last-page near-blank (arabic 116).

---

## 12. Final Pre-Submission Checklist

- [x] Content reviewed for KDP policy risks (no hate, porn, scams, illegal how-to; disclaimers present)
- [ ] Copyright/IP ownership verified (quotes PD-cited; fonts license Unverified; KDP may still request docs)
- [ ] AI-generation requirements checked against current KDP guidance — **disclose generated text at setup**
- [x] Metadata matches the actual book (title/subtitle/author/series) **except ISBN still placeholder**
- [x] Title/subtitle/author consistent cover ↔ listing
- [ ] Categories and keywords appropriate (`stoic journal` should change; live nodes Unverified)
- [x] Description accurately represents the book
- [ ] Cover requirements verified (formula OK; **barcode label must go**; Previewer Unverified)
- [x] Ebook file validated where applicable — N/A
- [ ] Paperback interior validated where applicable (**ISBN placeholder + TOC fail**; trim/fonts OK locally)
- [ ] Print cover validated where applicable (size OK; label fail; calculator Unverified)
- [x] Images meet applicable quality requirements (no photos; vector/type)
- [ ] No placeholder or unfinished content remains — **FAIL until ISBN + barcode label + TOC**
- [x] No obvious duplicated/reused chapters in this interior
- [ ] Final proofread completed (human)
- [ ] Final physical/digital proof reviewed
- [x] Current official KDP requirements fetched 2026-08-21 (fonts page timeout)

---

## Additional Materials Needed

- Assigned ISBN
- KDP Cover Calculator output for 124 pp / 6×9 / B&W white
- Print Previewer pass/fail
- Physical proof
- Liberation font license confirmation
- Live browse-node names as shown in your KDP account

---

## Closing

This is a skeptical pre-publication audit of supplied files against Help pages fetched 2026-08-21. Amazon/KDP makes the final decision. **A compliance audit cannot guarantee KDP approval.**
