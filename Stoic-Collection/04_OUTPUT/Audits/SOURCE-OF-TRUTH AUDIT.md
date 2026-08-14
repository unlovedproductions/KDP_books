# SOURCE-OF-TRUTH AUDIT — Stoic Collection

**Scope:** Inspection only. No files modified. No Series Architecture produced.  
**Missing requested file:** `PROJECT_FILE_ORGANIZATION_MANIFEST.md` — **not present** anywhere under `/home/unloved/KDP_books` (including `Stoic-Collection/`).

**Declared conflict-resolution order** (same in Series Bible §24.6 and Book 2 Brief):

1. Master AI Role Prompt → 2. Master Series Bible → 3. Book Project Brief → 4. MDS Prompt → 5. Book MDS

---

## A. Document-by-document audit

| Document | Version / date | Status (from content) | Authority level | Current? | Supersedes? | Conflicts? | Use for Series Architecture? | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `MASTER AI ROLE PROMPTv1.1.md` | v1.1; mtime 2026-08-10 | Unlabeled beyond version; role/framework prompt | **Governing instruction** (hierarchy #1) | Yes, as role/decision framework | No | No material catalog conflict | **Yes — governing** | Both Bible and Brief name it as top of hierarchy; defines role, decision hierarchy, series-thinking rules. Does not lock catalog titles/count. |
| `MASTER SERIES BIBLE PROMPTv1.1.md` | v1.1; mtime 2026-08-10 | Creation/maintenance prompt for Series Bible | **Governing instruction** (how to build/maintain Bible) | Yes as process prompt; **not** the living series SoT | No | No | **Yes — governing process**; not catalog facts | Instructs creation of permanent systems + long-term catalog strategy; does not itself lock Book 1–N titles. Living product is the Bible document. |
| `THE STOIC COLLECTION — MASTER SERIES BIBLE.md` | **v1.0**; Status: **ACTIVE**; mtime 2026-08-13 | Permanent series source of truth | **Current series SoT** (hierarchy #2) | **Yes** | Explicitly supersedes prior Practice-Series bible for naming/catalog/brand; supersedes prior Book 2=*Adversity* | Soft tensions with legacy docs + Book 2 manuscript Book 1 title string (see §C) | **Yes — primary series SoT** | Self-declares ACTIVE; parents Role + Series Bible Prompt; Book 2 MDS/Brief inherit it. |
| `MASTER PUBLISHING DESIGN SPECIFICATION PROMPTv1.1.md` | v1.1; mtime 2026-08-10 | Book MDS creation prompt | **Governing instruction** (hierarchy #4) | Yes for book architecture process | No | No | **Secondary** — book-level process, not series catalog SoT | Operates under Series Bible + Brief; does not define collection catalog. |
| `BOOK 2 — PROJECT BRIEF & BOOK INFORMATIONv1.1.md` | **v1.1**; mtime 2026-08-10 | Book-specific controlling facts | **Book-level controlling source** (hierarchy #3) | Yes for Book 2 identity/requirements | Does not claim to supersede Bible; Bible §0.2 adopts its Book 2 identity | States it does **not** override Series Bible | **Yes for Book 2 position/title**; not for full-collection redesign | Locks Book 2 as *Stoic Shadow Work Journal* within The Stoic Collection; Bible explicitly defers Book 2 identity to this Brief. |
| `cursorexecutioninstructionsv1.1.md` | v1.1; mtime 2026-08-10 | Phase instructions: create Bible + Book 2 MDS; **STOP before manuscript** | **Historical governing execution brief** for that phase | **Not current operational SoT** for a new Series Architecture pass | No | Its STOP (“do not write manuscript”) is **historically superseded by later work** (manuscript + audits exist) | **No as catalog authority**; optional as provenance of how Bible/MDS were generated | Phase deliverables already exist. Using it as live instruction would conflict with completed later stages. |
| `PROJECT_FILE_ORGANIZATION_MANIFEST.md` | — | **ABSENT** | Unknown | N/A | N/A | N/A | **Cannot use** | **REQUIRES HUMAN CONFIRMATION:** expected by this audit request but not in the repo. Folder placement alone is not authority. |

### Related approved / working / archive (material to Series Architecture only where they assert catalog facts)

| Document | Version / date | Status | Authority level | Current? | Supersedes? | Conflicts? | Use for Series Architecture? | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Book 2 MDS | v1.0; “Architecture complete…” | Book blueprint; inherits Bible + Brief | **Approved book SoT** (hierarchy #5) | Current for Book 2 architecture | Resolves legacy Adversity→Shadow at Book 2 | Audience emphasis tension with Bible noted and resolved in MDS §0.1 | **Yes as Book 2 evidence**; must not outrank Bible on series Permanents | Documents catalog conflict resolution already applied; assumes Book 1 foundations/method exists or will. |
| Book 2 Manuscript | Editorial Pass 1 complete; production locks 2026-08-12 | Approved manuscript (folder); unstaged working edits may exist | **Approved book product text** | Current for Book 2 interior content | No | Series page names Book 1 title string not locked in Bible §3.6 | **Evidence only** for what Book 2 currently publishes about the catalog | Not series SoT; may encode catalog claims that exceed Bible locks. |
| Book 2 Production Locks / KDP Listing / Previewer checklist | 2026-08-12 locks | Product/ops specs | Approved / working ops | Current for Book 2 production | No | Paths still say `stoic_series/...` (stale path strings) | **No** for series architecture | Production/listing, not catalog strategy. |
| Source Verification Report / Editorial Audit | 2026-08-10 / Pass 1 | Completed audits | Output/audit | Current as QC record | No | No catalog authority conflict | **No** as SoT; optional evidence of compliance | Do not govern series structure. |
| `SERIES_BIBLE.md` (archive) | Provisional “Stoic Practice Series”; 2026-08-08 | Explicitly **SUPERSEDED** by active Bible §0.2 | Archive / superseded | **No** | Was prior series SoT | Conflicts with active series name, Book 2 identity, fixed 5-volume spine | **No** (except historical contrast) | Active Bible forbids using “Stoic Practice Series” as published name. |
| `VOLUME_1_MPDS.md` (archive) | Inherits old bible; “1 of 5 founding spine” | **PROVISIONAL LEGACY** per active Bible §0.2 | Archive / provisional legacy | **Not current** under active Collection | No | Series name, imprint unspecified, 5-spine, Book 2=*Adversity* order logic | **No** until realigned; do not treat as live Book 1 lock | Active Bible requires realignment before manuscript finalization/reprint. |

---

## B. What the **current Series Bible (v1.0 ACTIVE)** already establishes about catalog structure

Report only — **no recommendation on whether these may be changed.**

| Element | Locked by active Series Bible? | What is established |
| --- | --- | --- |
| **Series name / structure model** | **Yes (PERMANENT / resolution)** | Published series = **The Stoic Collection**. Shared method family (SSOCR), Permanent signatures/frameworks, MDS-before-manuscript, medium-content guided workbook posture. |
| **Catalog order** | **Partially** | **Founding domain order** for Book 1 then Book 2 is stated as founding logic (§3.6). Numbering Book 1, Book 2, … is PERMANENT (§20.1). **Order after Book 2 may shift** (§3.6). Recommended “Book 1 before examination-heavy titles” is **ADAPTABLE recommendation** (§20.3), not a hard purchase gate. |
| **Book count** | **No fixed total** | Catalog is **open-ended** (“Book 3+”). No “exactly N books” lock in active Bible. (Legacy archive locked a **5**-volume founding spine — superseded/not restated.) |
| **Book titles** | **Mixed** | **Book 2 title:** locked via Brief, adopted in Bible §0.2 → *Stoic Shadow Work Journal*. **Titles after Book 2:** **ADAPTABLE until locked by their Project Brief** (§3.6). **Book 1:** Bible locks the **domain job** (“Install core method: impression, judgment, control, assent, review”), **not** an explicit permanent title string in §3.6. |
| **Book positions** | **Partial** | Position 1 = method install domain; Position 2 = self-examination / hidden patterns domain. Later positions = distinct domains (examples only: adversity, emotion under fire, virtue in action, relationships). |
| **Existing products** | **Not as a published catalog list** | Bible assumes Book 1 foundations/method role and Book 2 Shadow Work identity; does not claim live Amazon ASINs or a closed published list. Book 2 MDS/manuscript treat Book 1 as exists-or-will-exist. |
| **Series structure (systems)** | **Yes (extensive PERMANENT)** | SSOCR, signatures, reference integrity, brand, editorial/visual systems, governance, future-book rules — these are locked as series architecture systems, separate from a fixed title list. |

---

## C. Material conflicts (Series Bible vs other documents)

1. **Series name**
   - Archive `SERIES_BIBLE.md`: “The Stoic Practice Series” (provisional).
   - Active Bible: **The Stoic Collection** (official; Practice Series superseded).
   - **Resolution already stated in active Bible.**

2. **Book 2 identity**
   - Archive founding spine: Book 2 = *Adversity…*.
   - Brief + active Bible §0.2 + Book 2 MDS: Book 2 = *Stoic Shadow Work Journal*; Adversity (if any) later.
   - **Resolution already stated in active Bible / MDS §0.1.**

3. **Fixed 5-book founding spine**
   - Archive Series Bible + `VOLUME_1_MPDS.md`: Volume 1 of **5**.
   - Active Bible: Book 1, Book 2, **Book 3+** (no count lock).
   - **Active Bible does not restate a 5-book lock.**

4. **Book 1 title string**
   - Active Bible §3.6: domain job only.
   - Archive Volume 1 MPDS + Book 2 manuscript series page: *Foundations: Judgment, Control, and Assent*.
   - **Tension:** manuscript/product text treats that Book 1 title as catalog fact; active Series Bible does **not** explicitly lock that string as PERMANENT.
   - **REQUIRES HUMAN CONFIRMATION** before treating Book 1’s exact title as series-locked.

5. **Audience framing**
   - Brief: primary “men interested in…”.
   - Bible: adults, often men but not exclusively; brand forbids artificial masculinity.
   - **MDS §0.1 documents resolution** (marketing may emphasize buyer; interior follows Bible). Not an open silent conflict.

6. **`cursorexecutioninstructions` STOP vs later manuscript**
   - Instructions forbid manuscript in that phase.
   - Manuscript + audits exist.
   - Treat instructions as **completed/historical phase brief**, not live ban on existing manuscript authority.

7. **Authority hierarchy vs MDS wording**
   - MDS says “Project Brief wins for Book 2 identity.”
   - Brief says it does not override Bible.
   - **Effectively aligned** because Bible §0.2 itself adopts the Brief’s Book 2 identity. No open fight if Bible remains #2 and Brief #3.

---

## D. Classification summary

| Class | Documents |
| --- | --- |
| **Governing instructions** | Master AI Role Prompt v1.1; Series Bible Prompt v1.1; MDS Prompt v1.1; `cursorexecutioninstructionsv1.1.md` (**historical phase only**) |
| **Current source-of-truth** | **THE STOIC COLLECTION — MASTER SERIES BIBLE v1.0 ACTIVE**; Book 2 Project Brief v1.1 (Book 2 facts); Book 2 MDS v1.0 (Book 2 architecture) |
| **Approved project documents** | Book 2 MDS; Book 2 Manuscript (editorial Pass 1); Production Locks; KDP Listing Setup; audits in `04_OUTPUT/Audits/` |
| **Working/draft** | Previewer/proof checklist; production scripts/PDFs; any unstaged manuscript edits |
| **Superseded / provisional legacy** | `SERIES_BIBLE.md`; `VOLUME_1_MPDS.md` |
| **Missing / unconfirmed** | `PROJECT_FILE_ORGANIZATION_MANIFEST.md` → **REQUIRES HUMAN CONFIRMATION** |

---

## E. Flags requiring human confirmation

1. **`PROJECT_FILE_ORGANIZATION_MANIFEST.md` is missing** — confirm whether it was never created, lives outside this repo, or should be generated later (not created in this audit).
2. **Book 1 exact title** (*Foundations: Judgment, Control, and Assent*) — used in Book 2 manuscript/series page and legacy Volume 1 MPDS, but **not explicitly locked** as a Permanent title string in active Series Bible §3.6.
3. **Whether a closed founding catalog (e.g., fixed N books / full title list) is intended** — active Bible currently establishes **open-ended Book 3+** with adaptable later titles.
4. **Authority of folder labels alone** — organization places files under `01_SOURCE_OF_TRUTH` / `02_APPROVED` / `05_ARCHIVE`; this audit treated **in-document status + hierarchy clauses**, not folder names, as authority.

---

**STOP.** Source-of-Truth Audit complete. No Series Architecture written or revised. No files modified during the audit pass that produced this record.
