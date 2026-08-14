# THE STOIC COLLECTION — SERIES ARCHITECTURE DOCUMENT

**Publisher:** UnlovedProductions  
**Series:** The Stoic Collection  
**Document type:** Series Architecture (catalog / reader-development roadmap)  
**Version:** 1.0  
**Status:** PROPOSED — not Source of Truth; does not outrank the Master Series Bible  
**Authority parents:** MASTER AI ROLE PROMPT v1.1; THE STOIC COLLECTION — MASTER SERIES BIBLE v1.0 ACTIVE; BOOK 2 PROJECT BRIEF v1.1; BOOK 2 MDS v1.0  
**Process prompt:** STOIC COLLECTION SERIES ARCHITECTURE — MASTER PROMPT (canonical)  
**Not:** a manuscript, book MDS, Series Bible rewrite, or production file  

**Human instruction (this pass):** Ignore the existing low-content journal SKU files as catalog authority. Evaluate a *new* Collection-aligned *Stoic Journal for Men* only under Potential Future Books if it can meet Collection standards.

---

# SOURCE-OF-TRUTH STATUS

### SOURCE STATUS: PARTIALLY VERIFIED

Authority is established for series identity, Book 2 identity, Book 1 *domain job*, shared method (SSOCR), signatures, and open-ended catalog logic. Material gaps remain on Book 1’s exact Permanent title string and on whether any closed founding catalog beyond Book 1–2 is intended.

### Authoritative sources used

| Source ID | Document | Version | Date / status | Authority | Current? | Used? | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ROLE-SRC | MASTER AI ROLE PROMPTv1.1.md | v1.1 | Process prompt | Hierarchy #1 | Yes | Yes | Decision hierarchy, series thinking, quality rules |
| BIBLE-SRC | THE STOIC COLLECTION — MASTER SERIES BIBLE.md | v1.0 ACTIVE | ACTIVE | Hierarchy #2 | Yes | Yes | Primary series SoT |
| BRIEF2-SRC | BOOK 2 — PROJECT BRIEF & BOOK INFORMATIONv1.1.md | v1.1 | Controlling Book 2 facts | Hierarchy #3 | Yes | Yes | Book 2 title, format, boundaries |
| MDSPROMPT-SRC | MASTER PUBLISHING DESIGN SPECIFICATION PROMPTv1.1.md | v1.1 | Process prompt | Hierarchy #4 | Yes | Secondary | Book-level process; not catalog SoT |
| MDS2-SRC | BOOK 2 — … MASTER PUBLISHING DESIGN SPECIFICATION.md | v1.0 | Architecture complete | Hierarchy #5 | Yes | Yes | Book 2 architecture evidence |
| MS2-SRC | BOOK 2 manuscript + PRODUCTION LOCKS / KDP LISTING | 2026-08-12 locks | Approved product text | Evidence only | Yes for Book 2 print claims | Yes (evidence) | Book 1 title string appears here; not Bible-locked |
| AUDIT-SRC | SOURCE-OF-TRUTH AUDIT.md | 2026-08-14 | Inspection record | Audit | Yes | Yes | Inventory reused; not catalog law |
| ARCHPROMPT-SRC | Series Architecture Master Prompt | Canonical | Process only | How to architect | Yes | Yes | Does not override Bible |

### Material quarantined sources

| Document | Status | Why quarantined |
| --- | --- | --- |
| `05_ARCHIVE/Superseded/SERIES_BIBLE.md` | SUPERSEDED | “Stoic Practice Series”; fixed 5-volume spine; Book 2 = Adversity |
| `05_ARCHIVE/Superseded/VOLUME_1_MPDS.md` | PROVISIONAL LEGACY | Foundations under old series name; must realign before reprint |

### Ignored this pass (human instruction)

| Artifact | Instruction | Architectural effect |
| --- | --- | --- |
| Existing *Stoic Journal for Men* / mismatched cover PDFs | **Ignore completely** as catalog/product authority | Not placed in Approved Series Books; not treated as Book 1; not treated as Collection companion. A *new* Collection-fit title of that name may appear only under Potential Future Books. |

### Unverified / missing

| Item | Classification |
| --- | --- |
| `PROJECT_FILE_ORGANIZATION_MANIFEST.md` | EXPECTED SOURCE NOT FOUND — non-material to catalog architecture |
| Exact Permanent Book 1 title string | REQUIRES HUMAN CONFIRMATION |
| Closed founding catalog (fixed N books / full title list) | OPEN — Bible establishes open-ended Book 3+ |

### Material conflicts (summary)

1. Series name Practice Series → Collection — **resolved** (Bible §0.2).  
2. Book 2 Adversity → Shadow Work — **resolved** (Brief + Bible §0.2).  
3. Fixed 5-book spine — **not restated** in active Bible; quarantined.  
4. Book 1 title *Foundations: Judgment, Control, and Assent* in manuscript/locks vs Bible domain-job-only — **unresolved title lock**.  

---

# SUPERSEDED SOURCE QUARANTINE

The following must **not** be used as current evidence for Approved Series Books:

- Stoic Practice Series naming  
- Book 2 = Adversity as founding position  
- Exactly five founding volumes as locked catalog  
- Legacy Volume 1 MPDS as live Book 1 lock without realignment  

Consult only for historical comparison and change detection.

---

# VERSION CONFLICT RECORD

### Document: Book 1 title string

**Version A — Active Series Bible §3.6**  
- Status: ACTIVE  
- Requirement: Book 1 domain job = install core method (impression, judgment, control, assent, review). Exact title **not** locked as PERMANENT.

**Version B — Book 2 manuscript / Production Locks / KDP Listing**  
- Status: Approved product text  
- Requirement: Series page lists Book 1 as *Foundations: Judgment, Control, and Assent*.

**Conflict:** Product text treats a specific title as catalog fact; series SoT locks only the domain job.

**Architectural Impact:** Book 1 placement and job are usable; Permanent title branding is not.

**Authority Assessment:** Bible outranks product text on series Permanents. Title string = DOCUMENTED working title.

**Confidence:** High on conflict; Medium on final title wording.

**Required Action:** REQUIRES HUMAN CONFIRMATION

---

# REQUIREMENTS REGISTER

| ID | Source | Version | Section | Requirement | Classification | Priority | Flexibility | Decisions Affected |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ROLE-001 | ROLE-SRC | v1.1 | Decision hierarchy | Prioritize transformation → instruction → usability → premium → series → brand → production → discoverability | MANDATORY | P0 | None | All architecture trade-offs |
| ROLE-002 | ROLE-SRC | v1.1 | Series thinking | Distinguish Permanent / Adaptable / Book-Specific; scalable systems over one-offs | MANDATORY | P0 | None | Governance states |
| ROLE-003 | ROLE-SRC | v1.1 | Design principles | No filler; every page/exercise justifies existence; progression over volume | MANDATORY | P0 | None | Book count, formats |
| BIBLE-001 | BIBLE-SRC | v1.0 | §0.2 | Official series name = **The Stoic Collection**; Practice Series superseded | MANDATORY | P0 | None | Series identity |
| BIBLE-002 | BIBLE-SRC | v1.0 | §0.2 | Book 2 = *Stoic Shadow Work Journal* per Brief; prior Adversity Book 2 superseded | MANDATORY | P0 | None | Book 2 position |
| BIBLE-003 | BIBLE-SRC | v1.0 | §1–2 | Medium-content guided workbooks; completable programs; not blank journals / quote anthologies / mystical shadow products | MANDATORY | P0 | None | Format strategy; future Journal for Men fit |
| BIBLE-004 | BIBLE-SRC | v1.0 | §3.6 | Book 1 domain = install method; Book 2 = self-examination of hidden patterns; Book 3+ distinct domains; titles after Book 2 adaptable until Brief-locked; order after Book 2 may shift | MANDATORY / STRATEGIC | P0 | Titles after B2 adaptable | Catalog map |
| BIBLE-005 | BIBLE-SRC | v1.0 | §15 | Shared engine SSOCR: SEE→SORT→OWN→CHOOSE→REVIEW | MANDATORY | P0 | Domain application only | Progression |
| BIBLE-006 | BIBLE-SRC | v1.0 | §11–12 | Permanent signatures: Control Sort, Assent Pause, Evening Examination, Practice Commitment, Progress Mark, Personal Standard Card, Re-entry, Principle, Terminology Guide, Citations, Collection page | MANDATORY | P0 | Content evolves by domain | Recurring elements |
| BIBLE-007 | BIBLE-SRC | v1.0 | §19 | Clone test: >30% prompt-function overlap after noun swap = redesign | MANDATORY | P0 | None | Differentiation |
| BIBLE-008 | BIBLE-SRC | v1.0 | §20 | Numbered Book 1, 2…; independence via Method Primer after Book 1; recommend Book 1 before examination-heavy titles (adaptable recommendation, not hard gate) | MANDATORY / STRATEGIC | P0 | Order recommendation adaptable | Navigation, cross-sell |
| BIBLE-009 | BIBLE-SRC | v1.0 | §13.2 | Prohibited: chapters that are only lined paper; undated infinite prompt grids as spine | MANDATORY | P0 | None | Future daily-journal fit |
| BIBLE-010 | BIBLE-SRC | v1.0 | §4.2 | Brand must never become artificially masculine / stereotype-driven | MANDATORY | P0 | None | Audience framing; future “for Men” titles |
| BRIEF2-001 | BRIEF2-SRC | v1.1 | ID | Book 2 title *Stoic Shadow Work Journal*; subtitle as Brief; Book Number 2 | MANDATORY | P0 | None | Book 2 identity |
| BRIEF2-002 | BRIEF2-SRC | v1.1 | Concept | Shadow work via Stoic framework; not mystical/Jungian/trauma/clinical | MANDATORY | P0 | None | Book 2 boundaries |
| BRIEF2-003 | BRIEF2-SRC | v1.1 | Specs | 6×9, B&W, white, no bleed, ~120 pp, premium guided workbook, KDP | DESIGN GUIDANCE | P1 | Page count architectural | Book 2 format |
| MDS2-001 | MDS2-SRC | v1.0 | §1 | Book 2 domain = unexamined patterns / avoidance / self-deception; must not steal Book 1 method-install job or future adversity external-blow job | MANDATORY | P0 | None | Differentiation Book 1/2/3 |
| MDS2-002 | MDS2-SRC | v1.0 | A1 | Method Primer enables late entry at Book 2 | STRATEGIC | P1 | None | Independence |
| ARCH-001 | ARCHPROMPT | — | §27 | Collection must contain genuine Foundations as official starting point | MANDATORY | P0 | Title open | Book 1 |
| ARCH-002 | ARCHPROMPT | — | §47 | Do not treat prior target book count as binding unless Bible locks it | MANDATORY | P0 | None | Book count |
| OPEN-001 | — | — | — | Exact Permanent Book 1 title | OPEN | P0 | Human | Branding |
| OPEN-002 | — | — | — | Approved Book 3+ titles and order | OPEN | P1 | Briefs | Future catalog |

---

# A. SERIES NORTH STAR

| Element | Statement | Evidence type | Governance |
| --- | --- | --- | --- |
| **Series Mission** | Design each title as a complete, completable training sequence: short classical teaching, honest self-examination, practical commitment, and review—so the reader leaves with a portable personal standard. | Direct Requirement — BIBLE-SRC §2 | LOCKED |
| **Series Promise** | By the last page, the reader can examine what they usually avoid, separate judgment from event, own what is theirs to control, and choose one reasoned next act aligned with virtue—in ordinary life. | Direct Requirement — BIBLE-SRC §2 | LOCKED |
| **Ideal Reader** | Adults (~25–55), often men but not exclusively, wanting Stoicism, discipline, emotional mastery, accountability, character—rational reflection over mystical or purely theoretical approaches. | Direct Requirement — BIBLE-SRC §3.2 | LOCKED (core) |
| **Entry State** | Reactive or quote-aware but method-weak; journals that vent without changing behavior; unclear fact vs judgment; no portable standard. | Strategic Requirement — BIBLE-SRC §3.3 + Book 1 job | CURRENT |
| **Midpoint State** | Can run SSOCR on concrete incidents; has begun owning assent; can examine avoidance/self-deception without mysticism (after Book 2). | Inference from BIBLE-005 + MDS2-001 | RECOMMENDED |
| **Completion State (core journey)** | Holds Personal Standard Card(s); can apply method under a second pressure domain beyond inner avoidance; seeks next Collection domain without needing a new method. | Strategic Requirement — BIBLE-SRC §15, §20.5 | RECOMMENDED |
| **Core Philosophy** | Structured character training through accurate Stoic mechanics; classical vs modern labeled; practice over information; no therapy claims. | Direct Requirement — BIBLE-SRC §3.1 | LOCKED |
| **Collection Identity** | Premium medium-content guided workbooks/journals; recognizable SSOCR + Permanent signatures; distinct problem domain per title. | Direct Requirement — BIBLE-SRC §1, §11–12, §19 | LOCKED |

---

# B. MASTER SERIES MAP

| # | Title | Subtitle | Format | Governance State | Primary Job | Core Capability | Builds From | Prepares For |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | *Foundations: Judgment, Control, and Assent* (**working title**) | TBD at Project Brief / MDS | Foundations guided workbook | Domain job **LOCKED**; exact title **REQUIRES HUMAN CONFIRMATION** | Install core Stoic method | Run SSOCR + Permanent tools from zero | Entry (no prior Collection book) | Book 2 examination under method literacy |
| 2 | *Stoic Shadow Work Journal* | A Guided Journey Through Self-Reflection, Virtue & Personal Growth | Guided shadow-examination journal / workbook | **LOCKED** (Brief + Bible) | Examine hidden patterns, avoidance, self-deception | Apply SSOCR to inner avoidance; Personal Standard for named pattern | Book 1 method (or Method Primer) | Later application domains (adversity, emotion, virtue-in-action, relationships) |

**Not on this map:** Any legacy low-content daily journal SKU (ignored per human instruction). Future *Stoic Journal for Men* — see Potential Future Books only.

---

# C. FOUNDATIONS — BOOK 1

### Identity

- **Title:** *Foundations: Judgment, Control, and Assent* — **working / documented title only**  
- **Subtitle:** OPEN (not locked by Bible)  
- **Format:** Foundations workbook (medium-content guided program)  
- **Audience:** Entry Collection reader; adults seeking a usable Stoic method  
- **Governance State:** Domain job LOCKED; title DOCUMENTED / REQUIRES HUMAN CONFIRMATION  

### Purpose

Install the minimum conceptual and practical foundation required for the rest of the Collection: impression → judgment → dichotomy of control → assent → review, expressed as SSOCR and Permanent signatures.

### Why It Must Be Book 1

Bible §3.6 founding logic places method install first. Architecture prompt §27 requires a genuine Foundations book as official starting point. Examination-heavy titles without method literacy collapse into mood diaries (strategic inference from Bible §20.3 + MDS2 independence via Primer).

### What It Teaches / Practices / Assumes / Prepares

| Lens | Content |
| --- | --- |
| Teaches | What Stoicism is/is not (practice boundaries); virtues as action tests; control sort; judgment vs fact; assent; responsibility without self-abuse; initial Evening Examination |
| Practices | Control Sort, Assent Pause, Evening Examination, Practice Commitment, Progress Mark, draft Personal Standard Card |
| Assumes | Adult literacy; willingness to write concrete incidents; no clinical need |
| Prepares | Method literacy so Book 2 can spend pages on unexamined patterns rather than rebuilding the engine |
| Later books must not duplicate | Full zero-to-one method install as the *only* focus; long primer-as-book |

### Decision Record — Book 1 placement

**Decision:** Book 1 is the Foundations / method-install title; official starting point of the numbered Collection.

**Evidence:**  
[ARCH-001] — ARCHPROMPT — §27  
[BIBLE-004] — BIBLE-SRC — §3.6  
[MDS2-001] — MDS2-SRC — §1 (must not steal Book 1’s job)

**Reasoning:** Without a method book, every later title must either strand late entrants or become a foundations clone. Bible founding order and MDS differentiation both require a dedicated Book 1.

**Inference:** Exact marketing subtitle and chapter count are book-level (Bible §27 remaining decisions).

**Decision Type:** Direct Requirement (placement/domain); Open Decision (exact Permanent title).

**Governance State:** LOCKED (job/position); REQUIRES HUMAN CONFIRMATION (exact title string).

**Confidence:** High (placement); Medium (title wording).

**Conflict Check:** Title string conflict recorded above — product text vs Bible.

---

# D. STOIC JOURNAL FOR MEN (EXISTING SKU)

**Human instruction:** Ignore completely for this architecture pass.

| Field | Determination |
| --- | --- |
| Strategic position | **Not analyzed as live catalog evidence** |
| Product role | **Ignored** — do not treat as Core, Companion, Entry, Expansion, or Advanced based on existing PDFs |
| Numbered Collection | **No** |
| Action this document | Do not discard/rename/redesign here; do not enroll in series metadata via this architecture |

A **new** Collection-aligned product that may reuse the commercial name *Stoic Journal for Men* is evaluated only under **Potential Future Books**.

---

# E. STOIC SHADOW WORK JOURNAL

| Field | Determination |
| --- | --- |
| Book number | **Book 2** — LOCKED |
| Purpose | Stoic self-examination of hidden patterns, avoidance, self-deception, character weakness |
| Starting reader state | Unaware of recurring avoidances; may know quotes; may enter via Method Primer without Book 1 |
| Ending reader state | Can name patterns in concrete incidents; Control Sort + Assent Pause on uncomfortable truths; ownership without self-abuse; finalized Personal Standard + continuation plan |
| Concepts assumed | Impression, judgment, control, assent, review (via Book 1 or Primer) |
| Concepts introduced / emphasized | Avoidance, self-deception, hidden patterns, Character Audit / Virtue Mirror under examination pressure |
| Skills developed | Unexamined-pattern training; book-specific drills (Hidden Pattern Log, Avoidance Map, Self-Deception Interrogation, Character Audit) |
| Deliberately does not cover | Full method install from zero as sole spine; mystical Jungian shadow; clinical trauma processing; external-blow adversity as primary pressure |
| Previous-book dependency | Soft — Method Primer required if Book 1 not completed |
| Next-book relationship | Prepares reader for application domains (e.g., adversity, emotion under fire) with clearer self-honesty |
| Why position is correct | Bible §3.6 domain order; Brief Book Number 2; MDS differentiation vs Book 1 and future adversity |

### Decision Record — Book 2 placement

**Decision:** *Stoic Shadow Work Journal* is Book 2 of The Stoic Collection.

**Evidence:**  
[BIBLE-002] — BIBLE-SRC — §0.2  
[BRIEF2-001] — BRIEF2-SRC — Project Identification  
[MDS2-001] — MDS2-SRC — §0.1 / §1  

**Reasoning:** Active authoritative sources explicitly adopt Brief identity and supersede Adversity-as-Book-2.

**Inference:** None required for position.

**Decision Type:** Direct Requirement.

**Governance State:** LOCKED.

**Confidence:** High.

**Conflict Check:** Legacy Adversity conflict resolved; do not restore.

---

# BOOK-BY-BOOK BLUEPRINTS

## Book 1 — Foundations (method install)

### Identity

- Title: *Foundations: Judgment, Control, and Assent* (working)  
- Subtitle: OPEN  
- Format: Foundations workbook  
- Audience: Entry / method-seeking adults  
- Governance State: Job LOCKED; title pending confirmation  

### Strategic Role

| Field | Content |
| --- | --- |
| Primary job | Install core Stoic method |
| Secondary job | Establish Collection vocabulary and Permanent tool literacy |
| Reader problem | Knows Stoic slogans; cannot run a repeatable examination→action loop |
| Core promise | Leave able to SEE/SORT/OWN/CHOOSE/REVIEW on ordinary incidents |
| Primary transformation | From quote-consumer to method practitioner |

### Capability Development

- Core concepts: impression, judgment, dichotomy of control, assent, virtue as action test, responsibility  
- Primary skills: Control Sort, Assent Pause, Evening Examination, Practice Commitment  
- Required prior knowledge: none Collection-specific  
- New capability: portable SSOCR  
- Expected post-book capability: ready for examination-heavy Book 2 without stranding  

### Experience

- Beginning: curious / skeptical / method-hungry  
- During: Band I→II teaching then drills; no Band III open  
- Completion: draft Personal Standard; Progress Marks habit  
- Unique activities: method install arc (not shadow drills)  

### Sequence

- Builds on: none  
- Prepares for: Book 2  
- Why correct: founding logic BIBLE-004  

### Boundaries

- Must not become Stoic sampler / quote book  
- Must not absorb Book 2’s avoidance/self-deception as primary domain  
- Mystical/clinical content forbidden  

### Distinctiveness Test

Only title whose *sole* primary job is zero-to-one method install. Without it, Collection lacks an official start.

### Decision Evidence

See Decision Record — Book 1 placement.

---

## Book 2 — Stoic Shadow Work Journal

### Identity

- Title: *Stoic Shadow Work Journal*  
- Subtitle: A Guided Journey Through Self-Reflection, Virtue & Personal Growth  
- Format: Guided journal / workbook (medium-content)  
- Audience: Men-emphasized marketing OK; inclusive interior voice (MDS §0.1)  
- Governance State: LOCKED  

### Strategic Role

| Field | Content |
| --- | --- |
| Primary job | Self-examination of hidden patterns / avoidance / self-deception |
| Secondary job | Prove Collection can handle charged self-honesty without woo/clinical |
| Reader problem | Repeats faults; avoids hard truths; “discipline” without motive exam |
| Core promise | Name what you avoid, own your share, virtue-test next act, hold a standard |
| Primary transformation | Unawareness → named pattern + Personal Standard |

### Capability Development

- Concepts: judgment under avoidance; responsibility; virtue mirror; character  
- Skills: Hidden Pattern Log, Avoidance Map, Self-Deception Interrogation, Character Audit  
- Prior knowledge: SSOCR via Book 1 or Primer  
- New capability: pattern-level ownership under inner pressure  
- Post-book: prepared for external or emotion domains without method rebuild  

### Experience

- Beginning: possibly defensive / curious about “shadow”  
- During: SSOCR on inner avoidance; mid Character Audit; difficulty ramp  
- Completion: Personal Standard Card + 7-day plan  
- Unique: shadow reframed as unexamined judgments/patterns  

### Sequence

- Builds on: Book 1 / Primer  
- Prepares for: Book 3+ application domains  
- Why correct: BIBLE-002, BRIEF2-001, MDS2-001  

### Boundaries

- Not Book 1 clone  
- Not adversity-external primary  
- Not Jungian / trauma / clinical  

### Distinctiveness Test

Only Collection title whose primary pressure source is *inner* unexamined patterns under Stoic mechanics.

### Decision Evidence

See Decision Record — Book 2 placement.

---

# BOOK-TO-BOOK TRANSITION MATRIX

| From | To | Existing Capability | New Capability | Why the Transition Works |
| --- | --- | --- | --- | --- |
| Entry | Book 1 | Curiosity / quote familiarity | SSOCR + Permanent tools | Method must exist before hard examination |
| Book 1 | Book 2 | Method literacy | Pattern detection under avoidance/self-deception | Tools stay constant; pressure domain changes (BIBLE-004, MDS2-001) |
| Book 2 (late entry via Primer) | Book 2 completion | Primer-level tool labels | Same pattern capability | Independence rule BIBLE-008 |
| Book 2 | Future application domain (e.g., Adversity) | Pattern honesty + SSOCR | Apply method when plans break / externals hit | Self-honesty reduces self-deception under setback; domain not duplicated |

---

# DIFFERENTIATION SYSTEM

| Pair | Overlap type | Classification | Note |
| --- | --- | --- | --- |
| Book 1 ↔ Book 2 | Shared SSOCR / signatures | COMPLEMENTARY / SUPPORTING | Domain jobs distinct; clone test required at MDS |
| Book 2 ↔ Future Adversity | Both may use control/assent | COMPLEMENTARY if adversity = external blows | MDS2 forbids Book 2 stealing adversity job |
| Book 2 ↔ Future Emotion-under-fire | Emotional content | COMPLEMENTARY if emotion = disturbance under fire, not avoidance-as-spine | |
| Low-content daily grid ↔ Collection core | Format | REDUNDANT as core title | Forbidden as Collection spine (BIBLE-003, BIBLE-009) |
| Prospective *Stoic Journal for Men* (guided) ↔ Book 1 | Method/practice | OVERLAPPING risk if it reteaches Foundations | Allowed only as Expansion with distinct daily-transfer job |

---

# CONTENT OWNERSHIP MODEL

| Concept / Practice | Primary Book | Secondary Reinforcement | Deepest Treatment | Allowed Repetition |
| --- | --- | --- | --- | --- |
| SSOCR method install | Book 1 | Primer in later books | Book 1 | Labels + short primer only after Book 1 |
| Control Sort | Book 1 (teach) | All later | Domain-labeled reuse | Domain change required |
| Assent Pause | Book 1 (teach) | All later | Cue-type evolution | Not five worded clones |
| Dichotomy of control | Book 1 | Later apply | Book 1 framework | Application, not re-lecture |
| Avoidance / self-deception patterns | Book 2 | Later if domain needs | Book 2 | Not full re-teach in adversity |
| Character Audit / Virtue Mirror | Book 2 (heavy) | Character/virtue titles | Examination titles | Adaptable density |
| External setback / obstacle | Future Adversity | — | Future Adversity | Not Book 2 primary |
| Emotion under live heat | Future Emotion title | — | Future Emotion | Not Book 1 open Band III |
| Personal Standard Card | Each title finalizes | Series continuity | Per-book extra line | Card evolves, not replaced wholesale |
| Terminology Guide / Citations | Each title’s load-bearing set | Series glossary forms | Book-specific selection | Shared forms; unique lists |

---

# RECURRING COLLECTION ELEMENTS

| Element | Across collection? | Books | Evolves? | Purpose | Recognition without monotony |
| --- | --- | --- | --- | --- | --- |
| Control Sort | Yes | All | Domain labels | Dichotomy skill | Same 3-column; new situations |
| Assent Pause | Yes | All | Cue type | Interrupt reactivity | Same 3-step; new triggers |
| Evening Examination | Yes | All | Q3 domain focus | Review | Fixed skeleton; domain Q3 |
| Practice Commitment | Yes | All instructional chapters | Difficulty | Transfer | Same 4 fields; harder acts |
| Progress Mark | Yes | All | Optional 4th check | Completability | Same squares |
| Personal Standard Card | Yes | All | Book-specific line | Integration | Shared frame; unique rule |
| Re-entry Page | Yes | All | Copy | Restart after lapse | One per book |
| Principle Callout | Yes | All instructional chapters | Wording | Encoding | ≤40 words; book-specific |
| Character Audit / Virtue Mirror | Adaptable | Heavy in exam/character titles | Rows/scenarios | Pattern + virtue test | Not every chapter spam |
| Terminology Guide + Citations | Yes | All | Term lists | Trust / literacy | Shared method; unique content |
| Collection page + next-book invite | Yes | All | Titles listed | Cross-sell | Restrained; value-first |
| Method Primer | Yes after Book 1 | Book 2+ | Length adaptable | Independence | Short; not Foundations clone |

**Not adopted:** “Four Stoic Questions,” “Stoic Verdict,” or other Architecture-prompt examples absent from current Bible.

---

# FORMAT STRATEGY

| Format | Role in progression | Status |
| --- | --- | --- |
| Foundations workbook | Book 1 — method install | REQUIRED for Collection |
| Guided examination journal | Book 2 — shadow/pattern work | LOCKED (Book 2) |
| Application-domain guided workbook | Book 3+ — adversity, emotion, virtue, relationships | RECOMMENDED expansion when Brief-locked |
| Habit tracker / blank daily grid as *primary* product | — | **Rejected as Collection core** (BIBLE-003, BIBLE-009) |
| Collection-aligned daily practice companion | Optional Expansion — only if SSOCR-bearing, sequenced, not lined-paper spine | PROPOSED future (*Stoic Journal for Men* candidate) |
| 30/60/90-day challenge | Possible Expansion format if distinct capability | OPEN — not approved |
| Leadership / finance planners | Possible Advanced/Expansion | OPEN — must pass overlap gate |

Every format must serve a distinct reader function. Variety alone is not a reason.

---

# CROSS-SELLING ARCHITECTURE

| Book | Best preceding | Best next | Companions | Back-of-book recommendation | Why |
| --- | --- | --- | --- | --- | --- |
| Book 1 | — | Book 2 | None approved | Shadow Work Journal | Method → examination (BIBLE-004, §20.5) |
| Book 2 | Book 1 (recommended, not gated) | First approved application domain when exists | None approved | Soft bridge to next domain + reinforce method if started here | MDS2 end bridge; Bible cross-sell restrained |

Do not auto-promote an entire speculative catalog. Until Book 3 is Brief-locked, Book 2’s next invite remains domain-level, not a false ASIN list.

---

# COLLECTION DEPTH

## CORE COLLECTION (essential)

1. Book 1 — Foundations (method)  
2. Book 2 — Stoic Shadow Work Journal  

## EXPANSION COLLECTION (not approved)

- Adversity / obstacle domain  
- Emotion under fire  
- Virtue in ordinary action  
- Relationships / roles / justice  
- Prospective Collection-aligned *Stoic Journal for Men* (daily transfer companion) — **only if redesigned to medium-content Collection standards**

## ADVANCED COLLECTION (not approved)

- Specialized deep domains (e.g., mortality, work/ambition, wealth/desire) only after core + at least one expansion application title prove method continuity  

### MINIMUM VIABLE COMPLETE COLLECTION

**Book 1 + Book 2.** Delivers method install + self-examination under Stoic mechanics — the smallest coherent founding journey locked by current sources.

### RECOMMENDED CORE COLLECTION (practical)

**Book 1 + Book 2 + one Brief-locked application domain (e.g., Adversity).**  
**Decision Type:** Creative Recommendation. **Governance:** RECOMMENDED — not approved until Project Brief exists.

---

# BOOK COUNT FLEXIBILITY

Active Bible: Book 1, Book 2, **Book 3+** — no fixed N. Legacy five-volume spine quarantined. Architecture does **not** add books to hit a number.

---

# FUTURE BOOK OPPORTUNITIES

| Working title | Format | Target reader | Problem solved | Proposed position | Dependencies | Class | Why not approved |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Adversity (obstacle / endurance / reframing) | Guided workbook | Post-Book-2 practitioners | Externals break plans; futile struggle | Book 3+ (order flexible) | Book 1 method; Book 2 honesty useful | Expansion | No Project Brief; was wrongly Book 2 in legacy |
| Emotion: Impressions Under Fire | Guided workbook | Readers under anger/fear heat | Pre-emotion / assent delay | Book 3+ | Method + preferably pattern honesty | Expansion | Example only in Bible §3.6 |
| Character: Virtues in Ordinary Action | Virtue practice workbook | Readers ready for virtue-as-choice | Abstract virtue theater | Book 3+ | Method | Expansion | Example only |
| Relationships: Duty, Boundaries, Social Virtue | Guided workbook | Role/conflict pressure | Other people’s judgments | Later | Method; justice/roles subset | Expansion | Example only |
| **Stoic Journal for Men** (new) | Collection-aligned **guided daily practice companion** — not a blank 120-page grid | Adults (men-emphasized marketing allowed if brand boundaries held) | Need for day-to-day transfer of SSOCR between domain books | Expansion (outside numbered spine **or** optional unnumbered companion) | Book 1 method installed or Primer; must inherit Permanent signatures; must pass clone test vs Book 1 | Expansion | No Brief; existing ignored SKU is not evidence; **only fits if** it is medium-content, sequenced, and not lined-paper-as-spine |

### Prospective *Stoic Journal for Men* — fit gate (this pass)

| Test | Result |
| --- | --- |
| Distinct purpose vs Book 1 | Only if job = **daily transfer / maintenance**, not method install |
| Distinct vs Book 2 | Must not become avoidance/self-deception examination |
| Format vs BIBLE-003/009 | Pure repeating daily template = **FAIL** Collection membership |
| Brand vs BIBLE-010 | “For Men” marketing OK; interior must not become stereotype-driven |
| Preliminary verdict | **Eligible as Potential Future Book** under redesign constraints; **not** Approved Series Book |

---

# ANTI-REPETITION SYSTEM

### Concepts

- Teach once at depth in Primary Book (ownership map).  
- Later books **apply** under new pressure; do not re-lecture identical doctrine blocks.

### Exercises

- Permanent signatures may recur every title.  
- Book-specific drills (Avoidance Map, etc.) stay owned by their title unless SERIES-LEVEL CHANGE.

### Prompts

- Taxonomy L1–L7: one primary function per prompt (Bible §14).  
- Same function tag twice only if domain changed **and** difficulty rose **and** prior artifact required.

### Framework evolution

- SSOCR stages map across chapters; never skip SORT/OWN/CHOOSE/REVIEW.  
- Evening Examination Q3 and Standard Card extra line carry domain specificity.

**Goal:** Recognition without redundancy.

---

# CONTENT OVERLAP TEST (operating rule for future titles)

Every future book must answer:

1. Unique reader problem?  
2. Distinct capability?  
3. Closest existing book?  
4. Why insufficient?  
5. Exclusive content?  
6. Content to remove (belongs elsewhere)?  
7. Gain not available by combining existing books?  
8. Strengthens sequence?  
9. Cannibalization risk?  
10. Collection materially weaker without it?  

If #10 = no → **REDUNDANT** (cannot approve without corrective change).

---

# FUTURE BOOK APPROVAL GATE

Enter official architecture only if: distinct purpose, distinct problem, distinct capability, fits philosophy/brand, justified format, builds on existing capability, useful next step, avoids unnecessary duplication, independent value, traceable reasoning, passes Overlap Test.

---

# EVIDENCE COVERAGE AUDIT

| Major Decision | Supporting Requirement | Source ID | Source | Version | Section | Evidence Type | Governance State | Confidence | Source Gap? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Series name = The Stoic Collection | BIBLE-001 | BIBLE-SRC | Series Bible | v1.0 | §0.2 | Direct Requirement | LOCKED | High | No |
| Book 1 = Foundations domain / start | ARCH-001, BIBLE-004 | ARCHPROMPT + BIBLE | — / v1.0 | §27 / §3.6 | Direct Requirement | LOCKED (job) | High | No |
| Book 1 exact title string | MS2 series page | MS2-SRC | Manuscript/locks | 2026-08-12 | Series page | Inference / Documented claim | REQUIRES HUMAN CONFIRMATION | Medium | Soft gap vs Bible |
| Book 2 = Shadow Work Journal | BIBLE-002, BRIEF2-001 | BIBLE + Brief | v1.0 / v1.1 | §0.2 / ID | Direct Requirement | LOCKED | High | No |
| Not restore Adversity as Book 2 | BIBLE-002 | BIBLE-SRC | v1.0 | §0.2 | Direct Requirement | LOCKED | High | No |
| Open-ended book count | BIBLE-004, ARCH-002 | BIBLE + ARCH | v1.0 | §3.6 / §47 | Direct Requirement | CURRENT | High | No |
| MVCC = Book 1 + Book 2 | BIBLE-004 | BIBLE-SRC | v1.0 | §3.6 | Strategic Requirement | RECOMMENDED | High | No |
| Progression = SSOCR (+ Brief exam arc) | BIBLE-005 | BIBLE-SRC | v1.0 | §15 | Direct Requirement | LOCKED | High | No |
| Ignore existing Journal-for-Men SKU | Human instruction this pass | — | — | — | Creative / process | DOCUMENTED | High | N/A |
| Future *Stoic Journal for Men* as Expansion candidate | BIBLE-003, BIBLE-009, BIBLE-010 | BIBLE-SRC | v1.0 | §1, §13.2, §4.2 | Creative Recommendation | PROPOSED | Medium | Needs Brief |
| Recommended third application title | Bible examples §3.6 | BIBLE-SRC | v1.0 | §3.6 | Creative Recommendation | PROPOSED | Medium | SOURCE GAP until Brief |
| Recurring signatures list | BIBLE-006 | BIBLE-SRC | v1.0 | §11–12 | Direct Requirement | LOCKED | High | No |

---

# SOURCE CONFLICT AUDIT

## Resolved Conflicts

1. Series name Practice Series → Collection.  
2. Book 2 Adversity → Shadow Work.  
3. Audience men-primary Brief vs inclusive Bible — MDS §0.1: marketing may emphasize; interior follows Bible.  
4. Fixed 5-book spine — not carried into active Bible.

## Unresolved Conflicts

1. **Book 1 exact Permanent title** — manuscript/locks vs Bible §3.6 domain-only.  

## VERSION CONFLICTS

See Version Conflict Record (Book 1 title string).

---

# FINAL SOURCE AUDIT (checklist)

- Newest identifiable authoritative series SoT used: Bible v1.0 ACTIVE — **Yes**  
- Authority established rather than assumed — **Yes** (with PARTIALLY VERIFIED status)  
- Superseded sources quarantined — **Yes**  
- Draft/archive not treated as current — **Yes**  
- Version-sensitive decisions cite correct versions — **Yes**  
- Missing metadata disclosed — **Yes**  
- Material ambiguity identified — **Yes** (Book 1 title; Book 3+)  
- No quarantined source used as current evidence for Approved books — **Yes**  
- No silent version mixing — **Yes**  
- Filename/folder alone not treated as authority — **Yes**  
- Legacy decisions not restored — **Yes**  
- Existing journal SKU ignored per human instruction — **Yes**  

---

# FINAL DECISION AUDIT

| Decision | Source support? | Version correct? | Authoritative? | Explicit / inference / recommendation? | Conflict? | Human confirmation? |
| --- | --- | --- | --- | --- | --- | --- |
| Series name | Yes | Yes | Yes | Explicit | Resolved | No |
| Book 1 position/job | Yes | Yes | Yes | Explicit | No | No |
| Book 1 title string | Product only | Product ≠ Bible Permanent | Partial | Documented claim | Yes | **Yes** |
| Book 2 identity | Yes | Yes | Yes | Explicit | Resolved | No |
| MVCC = 1+2 | Yes | Yes | Yes | Strategic | No | No |
| Ignore legacy journal SKU | Human instruction | — | Process | Instruction | No | Documented |
| Future Journal for Men candidate | Bible format rules | Yes | Yes | Creative Recommendation | Fit conditional | Brief required later |
| Book 3 = Adversity | Example only | — | Not locked | Creative Recommendation | No | **Yes** before approval |

---

# FINAL ARCHITECTURE INTEGRITY CHECK

| Check | Result |
| --- | --- |
| SOURCE INTEGRITY | PASS (PARTIALLY VERIFIED disclosed) |
| VERSION INTEGRITY | PASS |
| DECISION INTEGRITY | PASS with labeled open items |
| SERIES INTEGRITY | PASS for founding journey |
| BOOK INTEGRITY | PASS for approved Book 1 job + Book 2 |
| SEQUENCE INTEGRITY | PASS Book 1 → Book 2 |
| DIFFERENTIATION INTEGRITY | PASS pending Book 1 MDS clone test at production |
| CATALOG INTEGRITY | PASS — no false 5-book lock |
| GOVERNANCE INTEGRITY | PASS — human list below |

---

# REQUIRES HUMAN CONFIRMATION

### 1. Exact Permanent Book 1 title

- **Decision:** Lock *Foundations: Judgment, Control, and Assent* as Permanent series title, or choose another string.  
- **Why unresolved:** Bible §3.6 locks domain job only; Book 2 product text already prints the Foundations title.  
- **Sources:** BIBLE-SRC §3.6; MS2-SRC series page / Production Locks / KDP Listing.  
- **Current recommendation:** Keep *Foundations: Judgment, Control, and Assent* as working title for architecture and Book 2 cross-sell until confirmed; then either Bible-lock via SERIES-LEVEL CHANGE or revise product text.  
- **Exact question:** **Do you permanently lock Book 1’s published title as *Foundations: Judgment, Control, and Assent*?**

### 2. Whether to Brief-lock a third founding application title now

- **Decision:** Approve Adversity (or other) as next numbered book.  
- **Why unresolved:** Bible lists domains as examples; no Project Brief.  
- **Sources:** BIBLE-SRC §3.6.  
- **Current recommendation:** Defer; ship/finish Book 1 + Book 2 first; then Brief Adversity as leading Expansion candidate.  
- **Exact question:** **Should Adversity (or another domain) be commissioned as Book 3 now?**

### 3. Prospective *Stoic Journal for Men* (new)

- **Decision:** Whether to commission a Collection-aligned guided daily companion under that name.  
- **Why unresolved:** No Brief; existing SKU ignored; fit only if medium-content / non-grid-spine.  
- **Sources:** BIBLE-003, BIBLE-009, BIBLE-010; human instruction.  
- **Current recommendation:** Keep as Potential Future Book; do not approve until Brief proves daily-transfer job distinct from Book 1 and Book 2.  
- **Exact question:** **Commission a new Collection-standard *Stoic Journal for Men* Project Brief (yes/no)?**

---

# FINAL COMPLIANCE AUDIT

- Mandatory requirements identified — Yes  
- No mandatory silently ignored — Yes  
- Major decisions traceable — Yes  
- Correct source versions — Yes  
- Superseded quarantined — Yes  
- Inferences / recommendations labeled — Yes  
- Unsupported market claims excluded — Yes  
- Foundations justified as Book 1 — Yes  
- Stoic Journal for Men: existing ignored; new candidate under Future — Yes  
- Shadow Work positioned as Book 2 — Yes  
- Distinct jobs / transitions / ownership / conflicts / version conflicts — Yes  
- Future concepts separated from approved — Yes  
- Evidence audit + SoT status + human list + governance states — Yes  
- No historical decision silently restored — Yes  

---

# FINAL COLLECTION

## APPROVED SERIES BOOKS

| # | Title | Format | Primary Job | Builds From | Prepares For |
| --- | --- | --- | --- | --- | --- |
| 1 | *Foundations: Judgment, Control, and Assent* (**working title**) | Foundations workbook | Install core Stoic method | Entry | Book 2 |
| 2 | *Stoic Shadow Work Journal* | Guided examination journal/workbook | Examine hidden patterns / avoidance / self-deception | Book 1 or Method Primer | Future application domains |

## POTENTIAL FUTURE BOOKS

- Adversity (external blows / obstacle) — Expansion / likely next numbered candidate  
- Emotion: Impressions Under Fire — Expansion  
- Character: Virtues in Ordinary Action — Expansion  
- Relationships: Duty, Boundaries, Social Virtue — Expansion  
- **Stoic Journal for Men (new)** — Expansion companion **only if** Collection-standard guided daily transfer (not blank grid); brand-safe “for Men” framing  

## REJECTED / REDUNDANT CONCEPTS

| Concept | Classification | Reason | Existing book that makes it unnecessary | Reconsider if |
| --- | --- | --- | --- | --- |
| Restore “Stoic Practice Series” name | Rejected | Bible §0.2 | Active Collection branding | Newer authoritative source explicitly restores |
| Adversity as Book 2 | Rejected | Brief + Bible lock Shadow Work as Book 2 | Book 2 Shadow Work | Never as Book 2; ok as later book via Brief |
| Fixed permanent 5-book spine | Rejected as lock | Not in active Bible | Open Book 3+ model | Bible SERIES-LEVEL CHANGE locks a count |
| Low-content repeating daily grid as Collection core title | Redundant / forbidden spine | BIBLE-003, BIBLE-009 | None — wrong product type | Redesigned as medium-content sequenced companion with distinct job |
| Mystical shadow / Jungian / trauma workbook in Collection | Rejected | Brief + Bible boundaries | Book 2 is Stoic examination instead | Never under Collection brand |

---

## READER JOURNEY NARRATIVE

The reader enters The Stoic Collection needing a usable method, not another quote stack. **Book 1 (Foundations)** installs impression, judgment, control, assent, and review as SSOCR and teaches the Permanent tools until they are boringly familiar. That capability is what later books assume.

**Book 2 (Stoic Shadow Work Journal)** keeps the same engine and aims it at what the reader usually avoids seeing—patterns, avoidance, self-deception—without mysticism or clinical promises. The Method Primer lets a late entrant start here, but the developmental ideal remains Book 1 first.

After Book 2, the reader holds a Personal Standard and can examine inner falsehoods. The Collection then expands—when Briefs lock titles—into distinct pressure domains (adversity, emotion under fire, virtue in action, relationships), each applying the same method to a new failure mode. A future *Stoic Journal for Men* may join only as a guided daily-transfer companion that strengthens practice between domain books—not as a blank journal and not as a substitute Foundations title.

The smallest strong journey already approved by current sources is **Foundations → Shadow Work**. Everything else remains proposed until a Project Brief and MDS make it real.

---

# DOCUMENT CONTROL

| Field | Value |
| --- | --- |
| Path | `Stoic-Collection/04_OUTPUT/Series_Architecture/THE STOIC COLLECTION — SERIES ARCHITECTURE.md` |
| Status | PROPOSED |
| Supersedes | None (first Series Architecture document in this folder) |
| Must not override | MASTER SERIES BIBLE v1.0 ACTIVE |
| Next step | Human confirmation list → then Book 1 Project Brief / MDS (separate execution) |

**VERIFY THE SOURCES. ESTABLISH THE TRUTH SET. EXTRACT THE REQUIREMENTS. GOVERN THE UNCERTAINTY. PROVE THE ARCHITECTURE.**

# END OF STOIC COLLECTION SERIES ARCHITECTURE DOCUMENT
