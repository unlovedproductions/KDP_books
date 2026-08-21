# PROJECT FILE ORGANIZATION MANIFEST

**Project:** UnlovedProductions — The Stoic Collection  
**Root:** `Stoic-Collection/`  
**Manifest path:** `Stoic-Collection/PROJECT_FILE_ORGANIZATION_MANIFEST.md` (project root)  
**Manifest status:** APPROVED — living document  
**Organization date:** 2026-08-13  
**Manifest drafted:** 2026-08-14  
**Approved:** 2026-08-14  

**Change control:** Living document. Agents may propose updates; **do not apply substantive changes without explicit human approval.** Location, inventory, and organization decisions in this file are under human control.

**Rules encoded by this manifest**

1. This file records **where files were placed** after organization. It does **not** by itself establish document authority.
2. Authority is determined by in-document status, version, and the declared conflict-resolution hierarchy (see `04_OUTPUT/Audits/SOURCE-OF-TRUTH AUDIT.md`).
3. No filenames were changed during organization unless separately approved.
4. Prior root folder `stoic_series/` was emptied and removed after migration.

---

## 1. Target folder structure

```text
Stoic-Collection/
├── 00_MASTER_INSTRUCTIONS/
├── 01_SOURCE_OF_TRUTH/
│   ├── Master_AI_Role_Prompt/
│   ├── Series_Bible/
│   ├── Series_Architecture/
│   ├── Design_Specification/
│   └── Other_Controlling_Sources/
├── 02_APPROVED/
│   ├── Book_Blueprints/
│   ├── Manuscripts/
│   ├── Product_Specifications/
│   └── Other_Approved_Materials/
├── 03_WORKING/
│   ├── Book_Blueprints/
│   ├── Manuscripts/
│   ├── Product_Specifications/
│   └── Other_Working_Materials/
├── 04_OUTPUT/
│   ├── Series_Architecture/
│   ├── Decision_Records/
│   ├── Audits/
│   └── Other_Outputs/
├── 05_ARCHIVE/
│   ├── Superseded/
│   ├── Obsolete/
│   ├── Rejected/
│   └── Historical/
├── 06_REFERENCE/
│   ├── Research/
│   ├── General_Reference/
│   └── External_Materials/
└── 99_REVIEW_REQUIRED/
```

**Out of scope (repo root, not under Stoic-Collection):** `.venv-kdp/`, `.git/`, `.vscode/`

---

## 2. File inventory (current paths)

### 00_MASTER_INSTRUCTIONS

| Current path | Prior path (pre-organization) | Notes |
| --- | --- | --- |
| `00_MASTER_INSTRUCTIONS/cursorexecutioninstructionsv1.1.md` | `stoic_series/cursorexecutioninstructionsv1.1.md` | Historical phase execution brief (Bible + Book 2 MDS generation) |

### 01_SOURCE_OF_TRUTH

| Current path | Prior path | Notes |
| --- | --- | --- |
| `01_SOURCE_OF_TRUTH/Master_AI_Role_Prompt/MASTER AI ROLE PROMPTv1.1.md` | `stoic_series/MASTER AI ROLE PROMPTv1.1.md` | Governing role prompt |
| `01_SOURCE_OF_TRUTH/Series_Bible/MASTER SERIES BIBLE PROMPTv1.1.md` | `stoic_series/MASTER SERIES BIBLE PROMPTv1.1.md` | Series Bible creation prompt |
| `01_SOURCE_OF_TRUTH/Series_Bible/THE STOIC COLLECTION — MASTER SERIES BIBLE.md` | `stoic_series/THE STOIC COLLECTION — MASTER SERIES BIBLE.md` | Active Series Bible v1.1 (self-declared); §0.2 lag fix 2026-08-18 |
| `01_SOURCE_OF_TRUTH/Design_Specification/MASTER PUBLISHING DESIGN SPECIFICATION PROMPTv1.1.md` | `stoic_series/MASTER PUBLISHING DESIGN SPECIFICATION PROMPTv1.1.md` | MDS creation prompt |
| `01_SOURCE_OF_TRUTH/Other_Controlling_Sources/BOOK 1 — PROJECT BRIEF & BOOK INFORMATIONv1.0.md` | *(created 2026-08-18)* | Book 1 controlling brief; title locked 2026-08-18: *Stoic Foundations* |
| `01_SOURCE_OF_TRUTH/Other_Controlling_Sources/BOOK 2 — PROJECT BRIEF & BOOK INFORMATIONv1.1.md` | `stoic_series/BOOK 2 — PROJECT BRIEF & BOOK INFORMATIONv1.1.md` | Book 2 controlling brief |
| `01_SOURCE_OF_TRUTH/Series_Architecture/THE STOIC COLLECTION — SERIES ARCHITECTURE.md` | `04_OUTPUT/Series_Architecture/…` (promoted 2026-08-17) | CURRENT working catalog roadmap; subordinate to Series Bible |

### 02_APPROVED

| Current path | Prior path | Notes |
| --- | --- | --- |
| `02_APPROVED/Book_Blueprints/BOOK 1 — STOIC FOUNDATIONS — MASTER PUBLISHING DESIGN SPECIFICATION.md` | `03_WORKING/Book_Blueprints/…` (promoted 2026-08-20) | Book 1 MDS v1.0 — **Approved** |
| `02_APPROVED/Book_Blueprints/BOOK 2 — STOIC SHADOW WORK JOURNAL — MASTER PUBLISHING DESIGN SPECIFICATION.md` | `stoic_series/BOOK 2 — STOIC SHADOW WORK JOURNAL — MASTER PUBLISHING DESIGN SPECIFICATION.md` | Book 2 MDS v1.0 |
| `02_APPROVED/Manuscripts/BOOK 2 — STOIC SHADOW WORK JOURNAL — MANUSCRIPT.md` | `stoic_series/BOOK 2 — STOIC SHADOW WORK JOURNAL — MANUSCRIPT.md` | Book 2 manuscript |
| `02_APPROVED/Manuscripts/BOOK 1 — STOIC FOUNDATIONS — MANUSCRIPT.md` | `03_WORKING/Manuscripts/…` (promoted 2026-08-21) | Book 1 manuscript — **Approved** |
| `02_APPROVED/Product_Specifications/BOOK 2 — PRODUCTION LOCKS.md` | `stoic_series/BOOK 2 — PRODUCTION LOCKS.md` | Production locks (2026-08-12) |
| `02_APPROVED/Product_Specifications/BOOK 2 — KDP LISTING SETUP.md` | `stoic_series/BOOK 2 — KDP LISTING SETUP.md` | KDP listing fields |
| `02_APPROVED/Other_Approved_Materials/` | — | Empty placeholder |

### 03_WORKING

| Current path | Prior path | Notes |
| --- | --- | --- |
| `03_WORKING/Other_Working_Materials/BOOK 2 — KDP PREVIEWER & PROOF CHECKLIST.md` | `stoic_series/BOOK 2 — KDP PREVIEWER & PROOF CHECKLIST.md` | Operator checklist |
| `03_WORKING/Other_Working_Materials/production/` | `stoic_series/production/` | Intact toolchain: scripts, fonts, output PDFs |
| `03_WORKING/Other_Working_Materials/production/typeset_book2.py` | `stoic_series/production/typeset_book2.py` | Interior typesetter |
| `03_WORKING/Other_Working_Materials/production/typeset_book1.py` | *(created 2026-08-21)* | Book 1 interior typesetter (Liberation house stack) |
| `03_WORKING/Other_Working_Materials/production/cover_book2.py` | `stoic_series/production/cover_book2.py` | Cover generator |
| `03_WORKING/Other_Working_Materials/production/cover_book1.py` | *(created 2026-08-21)* | Book 1 cover generator; spine 0.375″ top/bottom |
| `03_WORKING/Other_Working_Materials/production/fonts/*` | `stoic_series/production/fonts/*` | Liberation font symlinks (6) |
| `03_WORKING/Other_Working_Materials/production/output/Stoic_Shadow_Work_Journal_Book2_INTERIOR.pdf` | same under `stoic_series/` | Generated interior |
| `03_WORKING/Other_Working_Materials/production/output/Stoic_Shadow_Work_Journal_Book2_COVER.pdf` | same under `stoic_series/` | Generated cover |
| `03_WORKING/Other_Working_Materials/production/output/cover_dimensions.txt` | same under `stoic_series/` | Cover math sidecar |
| `03_WORKING/Other_Working_Materials/production/output/interior_page_count.txt` | same under `stoic_series/` | Book 2 page-count sidecar |
| `03_WORKING/Other_Working_Materials/production/output/Stoic_Foundations_Book1_INTERIOR.pdf` | *(created 2026-08-21)* | Book 1 interior, 124 pp, 6×9 B&W |
| `03_WORKING/Other_Working_Materials/production/output/Stoic_Foundations_Book1_COVER.pdf` | *(created 2026-08-21)* | Book 1 cover wrap |
| `03_WORKING/Other_Working_Materials/production/output/book1_interior_page_count.txt` | *(created 2026-08-21)* | Book 1 page-count sidecar |
| `03_WORKING/Other_Working_Materials/production/output/book1_cover_dimensions.txt` | *(created 2026-08-21)* | Book 1 cover math sidecar |
| `03_WORKING/Book_Blueprints/README.md` | stub after 2026-08-20 promotion | Points to Approved Book 1 MDS |
| `03_WORKING/Manuscripts/README.md` | stub after 2026-08-21 promotion | Points to Approved Book 1 manuscript |
| `03_WORKING/Product_Specifications/BOOK 1 — PRODUCTION LOCKS.md` | *(created 2026-08-21)* | First typeset locks; ISBN pending KDP |

### 04_OUTPUT

| Current path | Prior path | Notes |
| --- | --- | --- |
| `04_OUTPUT/Audits/BOOK 2 — SOURCE VERIFICATION REPORT.md` | `stoic_series/BOOK 2 — SOURCE VERIFICATION REPORT.md` | Source verification audit |
| `04_OUTPUT/Audits/BOOK 1 — SOURCE VERIFICATION REPORT.md` | *(created 2026-08-20)* | Book 1 citation pack + Brief source-verification PASS |
| `04_OUTPUT/Audits/BOOK 2 — MANUSCRIPT EDITORIAL AUDIT.md` | `stoic_series/BOOK 2 — MANUSCRIPT EDITORIAL AUDIT.md` | Editorial Pass 1 audit |
| `04_OUTPUT/Audits/BOOK 1 — MANUSCRIPT EDITORIAL AUDIT.md` | *(created 2026-08-21)* | Book 1 manuscript Editorial Pass 1 — PASS WITH FIXES APPLIED |
| `04_OUTPUT/Audits/SOURCE-OF-TRUTH AUDIT.md` | *(created post-organization)* | Controlling-document authority audit |
| `04_OUTPUT/Series_Architecture/README.md` | stub after 2026-08-17 promotion | Points to CURRENT architecture under SoT |
| `04_OUTPUT/Audits/SERIES ARCHITECTURE — COMPLIANCE AUDIT.md` | *(created post-organization)* | Architecture compliance audit (open-list superseded 2026-08-18) |
| `04_OUTPUT/Audits/SERIES BIBLE AND ARCHITECTURE AUDIT.md` | *(created 2026-08-18)* | Dual Bible + Architecture currency/fidelity audit |
| `04_OUTPUT/Decision_Records/` | — | Empty placeholder |
| `04_OUTPUT/Other_Outputs/` | — | Empty placeholder (PDFs kept with production toolchain under Working) |

### 05_ARCHIVE

| Current path | Prior path | Notes |
| --- | --- | --- |
| `05_ARCHIVE/Superseded/SERIES_BIBLE.md` | `stoic_series/SERIES_BIBLE.md` | “Stoic Practice Series” bible; superseded by active Collection Bible |
| `05_ARCHIVE/Superseded/VOLUME_1_MPDS.md` | `stoic_series/VOLUME_1_MPDS.md` | Retired non-live 2026-08-17; do not use as Book 1 MDS |
| `05_ARCHIVE/Obsolete/` | — | Empty placeholder |
| `05_ARCHIVE/Rejected/` | — | Empty placeholder |
| `05_ARCHIVE/Historical/` | — | Empty placeholder |

### 06_REFERENCE

| Path | Notes |
| --- | --- |
| `06_REFERENCE/Research/` | Empty placeholder |
| `06_REFERENCE/General_Reference/` | Empty placeholder |
| `06_REFERENCE/External_Materials/` | Empty placeholder |

### 99_REVIEW_REQUIRED

| Path | Notes |
| --- | --- |
| `99_REVIEW_REQUIRED/` | Items needing human confirmation before placement elsewhere |

---

## 3. Organization decisions recorded

| Decision | Choice |
| --- | --- |
| New root name | `Stoic-Collection/` (replaced flat `stoic_series/`) |
| Filename renames | None |
| Document content edits during organization | None |
| Production tree | Kept intact under `03_WORKING/Other_Working_Materials/production/` (scripts + fonts + PDFs together) |
| Duplicate PDFs into `04_OUTPUT/Other_Outputs/` | Not done (avoid duplication; regenerate path stays with scripts) |
| Architecture document location | Promoted 2026-08-17 from `04_OUTPUT/Series_Architecture/` to `01_SOURCE_OF_TRUTH/Series_Architecture/` (human approved) |
| VOLUME_1_MPDS | Retired as non-live 2026-08-17; remains in `05_ARCHIVE/Superseded/` with retirement banner |

---

## 4. Known stale path references (content not updated during organization)

These files still mention `stoic_series/production/...` in body text:

- `02_APPROVED/Product_Specifications/BOOK 2 — PRODUCTION LOCKS.md`
- `03_WORKING/Other_Working_Materials/BOOK 2 — KDP PREVIEWER & PROOF CHECKLIST.md`
- (and related listing/ops docs if they hardcode the old path)

**Follow-up:** path-string update pass (separate from organization).

---

## 5. Approval & living-document control

| Field | Value |
| --- | --- |
| Status | **APPROVED** |
| Approved by | Project owner |
| Approved date | 2026-08-14 |
| Canonical location | `Stoic-Collection/PROJECT_FILE_ORGANIZATION_MANIFEST.md` |
| Change policy | Living document — **human approval required** before substantive edits (path moves, inventory changes, decision revisions). Editorial typos may be proposed but still require confirmation if unclear. |

When the tree changes: propose a manifest update → wait for approval → then edit this file and relocate materials as approved.
