# Governance Rules
_Projects_Rules.md | Last updated: 2026-06-05

---

## 1. Purpose

This vault stores project information to support AI-assisted engineering workflows and personal project management. Each file serves one purpose. Content placed in one file is not reproduced elsewhere.

---

## 2. Language

Body content: English only.

Exceptions: French terms with no direct English equivalent (e.g. *suivi d'exécution*, *cahier de charges*, *ordre permanent*), official document titles, and regulatory references (e.g. EN 1990 NA belge).

French terms appear in italics with an English gloss on first use. No mixing within sections.

**Rationale:** Cross-project search must work in one language. Consistency reduces friction when sharing with non-bilingual colleagues.

---

## 3. File Structure

Each project folder contains exactly these files:

| File | Name | Role |
|------|------|------|
| 00 | Overview | Live project status — current situation and next steps |
| 01 | History | Milestone timeline + full operational log |
| 02 | Document Register | Full document inventory |
| 03 | Open Points | Pending issues and blockers |
| 04 | Strategic Context | Non-obvious interpretation, positioning, normative framework |
| 06 | Technical Reviews | Design decisions, concept evolution, technical notes |
| README | — | Vault exceptions and loose file explanations |

No additional files without a README entry explaining the exception.

---

## 4. File Rules

### 00 — Overview

**Purpose:** Live document answering "what is the situation right now?" Must be short, factual, and immediately readable. Aim for a single screen. No bloat, no narrative padding, no redundant detail.

**Critical rule — facts only:** 00 contains only confirmed facts. No gut feelings, no rumors, no interpretations. If something requires strategic framing or interpretation, it goes in 04 — Strategic Context. If it requires detail, it goes in 03 — Open Points. If it already lives in another file, do not reproduce it here — reference it instead.

**Contains:**

**Project Scope & Design** — What is this project? Structure type, geometry, defining parameters, location. One short paragraph maximum.

**Phase** — Current project phase using TUC Rail terminology (*faisabilité*, *cahier de charges*, *suivi d'exécution*) and a one-line description of the current execution state (e.g. *start of excavations*, *pouring of columns*, *documentation closeout*).

**Contacts** — Key parties, roles, and organisations. No email addresses or phone numbers — those belong in a personal address book. For TUC Rail contacts: check the live contact list; if found only in the archive, move to live and update. Include involvement level (e.g. approver / reviewer / contractor PM).

**Current Situation** — Short bullet list. One bullet per active topic. Each bullet references 03 — Open Points for detail. Format: `**TOPIC:** One-line factual summary. Status.` No narrative paragraphs. No speculation. Remove resolved items immediately — move closure to 01 — History.

**Next Steps** — Table of upcoming milestones. Format: `Milestone | Target | Status`. Include only actionable items with a known horizon. Remove rows when complete and add a line to 01 — History.

---

### 01 — History

**Purpose:** Complete factual record of the project — both at the milestone level and the operational detail level. Split into two parts.

**Part 1 — Project Timeline**
High-level view of the project's evolution. Forward chronological (oldest to newest). One row per milestone: `Date | Milestone`. Updated when a major phase, decision, or event is reached. Easy to read at a glance. Does not duplicate the log — one line maximum per milestone.

**Part 2 — Project Log**
Complete record of all actions, communications, reviews, and meetings. Reverse chronological. Each entry: `YYYY-MM-DD [HH:MM] — Event.` Include time when relevant (emails, calls). Updated after every session. Append only — entries are never edited or deleted.

**Log belongs here:** Emails sent/received (with timestamps), meetings (with attendees and outcomes), site visits, formal submissions, review decisions, verbal instructions confirmed in writing.

**Does not belong here:** Reasoning, strategic framing (→ 04), pending action lists (→ 03).

---

### 02 — Document Register

**Purpose:** Readable inventory of all project documents — quickly shows volume and confirms what exists.

**Format:** Table. Fields: Document ID | Title | Author | Date received | Date answered | Type.

- No status, no issues, no flags — those belong in 03
- Normative references belong in 04 under "Normative Framework"
- Documents are never removed; mark superseded rows with `[superseded by DOC-ID]`
- Dates received and dates answered are mandatory fields

---

### 03 — Open Points

**Purpose:** Single source of truth for all pending issues. Strategic first read — answers "how serious is this project's situation and who needs to act?"

**Structure (in order):**

1. **Document Status** — Table showing volume of documents by category: received, under review, refused, approved, blocked by prerequisite, as-built pending. Facts only — no estimates.
2. **Situation Assessment** — 3–5 factual sentences on the severity of the overall situation. Permissible descriptors: *large dossier unreviewed*, *work executed without approved documentation*, *prerequisite unmet*, *deadline imminent*, *documentation quality poor throughout*. Not permissible: feelings, rumors, speculation.
3. **Action Required** — Bullet list grouped by party (Contractor / TUC RAIL / Client). One line per action. Names a specific deliverable and who owns it.
4. **Open Items Summary** — Table: ID | Description | Responsible | Status — the quick-scan section.
5. **Detail sections** — One subsection per active open item, with technical content, documents referenced, and closing condition.
6. **Closed Items** — Table retained until next update cycle, then moved to 01 — History.

**Status tags:** `BLOCKING` | `TO CONFIRM` | `PENDING` | `CLOSED`

- Only open or recently closed items. Closed items are removed after one update cycle; move closure to 01 — History
- 00 — Overview references this file; it does not reproduce content from it
- All action tracking lives here — not in 05

---

### 04 — Strategic Context

**Purpose:** What cannot be inferred from any other file. Non-obvious interpretation, political framing, positioning, management pressure context, normative framework.

**Scope test:** Before adding anything, ask: *can this be found in another file?* If yes, do not add it here.

**Belongs here:**
- Company or management-level dynamics
- Contractor posture and anticipated behaviour
- Client priorities and timeline pressure
- Interpretation lines to hold under pressure
- Normative framework: applicable standards, Belgian NA specifics, approved derogations
- Edge cases and deliberate conservative assumptions

**Does not belong here:** Summaries of 03, duplicates of contacts, vault how-to notes.

---

### 05 — Technical Reviews

**Purpose:** Engineering content — design decisions, concept evolution, review articles, technical notes authored or validated by TUC Rail.

**Belongs here:**
- Summaries of technical review articles linked to this project
- Design concept notes: what was decided and why (reasoning is appropriate here — this is engineering record, not operational status)
- Concept evolution: changes from original design, trigger, what was approved
- References to specific calculation notes in 02

**Note:** This file answers "what are we actually designing?" It complements 00 — which answers "what is the situation?" — by providing engineering substance.

---

## 5. Frontmatter Standard

Every file uses this frontmatter. No additions, no personal notes in frontmatter fields.

```
---
title: [File name]
project: [Project name]
project_number: [e.g. P785334]
location: [e.g. Lessines]
phase: [faisabilité | cahier de charges | suivi d'exécution]
role: [TUC Rail role on this project]
client: Infrabel
contractor: [Contractor name or N/A]
status: [active | on-hold | closed]
tags: [project-specific tags]
updated: YYYY-MM-DD
---
```

- `client` is always Infrabel (or the actual client — never the engineering bureau)
- `role` describes TUC Rail's contractual role, not a personal name
- `updated` is the only field that changes regularly — update it when content changes

---

## 6. Redundancy Rule

The same factual content must not appear in more than one file. When in doubt:

| Question | Answer lives in |
|----------|----------------|
| What is it? | 05 — Technical Reviews |
| What is the situation? | 00 — Overview |
| What has happened? | 01 — History (Project Log) |
| What documents exist? | 02 — Document Register |
| What is blocking progress? | 03 — Open Points |
| What do I need to know that isn't written elsewhere? | 04 — Strategic Context |

---

## 7. Maintenance Protocol

- **After every significant event:** Add one line to 01 — History (Project Log)
- **When a blocker changes status:** Update 03, update the 00 summary line, add one line to 01 — History
- **Monthly / per phase milestone:** Check 00 — Overview is still accurate, close resolved items in 03, verify frontmatter updated dates
- **Before a Claude session:** Load 00, 03, and 04 as primary context. Load 01, 02, 05 on demand
