---
title: Knowledge — Index
type: index
status: living
created: 2026-06-01
---

# Knowledge — Index

Map of the durable knowledge base. Start here when searching `Knowledge/`. This is the curated engineering layer — timeless, rewritten as understanding improves, never a dated log (that is `Projects/`).

> [!note] Naming note
> This index replaces the earlier empty `_Methodology — Index`. Some older methodology notes still carry `[[_Methodology — Index]]` and `[[_EC7 — Index]]` links in their text/frontmatter. `_EC7 — Index` exists (see EC7 section). A redirect stub `_Methodology — Index` is kept so no link dangles — it points here. When you next edit one of those notes, update its links to point to this index and to the relevant domain index directly.

---

## Sections

### Methodology
Synthesised methods — one note per check type or method. Dense, curated, no fluff.

- **EC7 — Geotechnical** → [[_EC7 — Index]]
  - [[Settlement under a loaded area — calculation methodology]] — *validated* (load-induced, Newmark + Terzaghi)
  - [[Settlement under a loaded area — methodology]] — *tutorial* (superseded by the validated note above; kept for the reverse-engineering walkthrough)
  - [[Dewatering-induced settlement — methodology]] — *draft* (drawdown-induced, De Beer + Dupuit/Sichardt)

*(Other Eurocode domains — EC2, EC0, EC1, EC3 — added as methodology notes are written.)*


- **EC2 — Concrete** → [[_EC2 — Index]]
  - [[M-N interaction diagram — methodology]] — *draft* (combined N+M, five-domain sweep, closed envelope; asymmetric-capable)

### Formulas
Atomic, self-contained, cited formula units. One relationship per section: symbols defined, units stated, clause cited, Belgian-annex divergence flagged. Source of truth for notebook-building once `eurocode-lib` is walled off. **Algorithms do not go here — only formulas and short derivations** (see CLAUDE.md §6).

- _(empty — populate by Eurocode: EC2/, EC7/, EC0/ …)_


- **EC2** → [[EC2 — ULS material design values]] — *draft; α_cc open* (partial factors, f_cd, concrete strain limits, f_yd, E_s, constitutive laws)

### Norms-Regulations
The *map* to normative sources — which clause, which annex, which Infrabel rule governs what, and where the PDF lives. Not a restatement of method.

- **Eurocodes-NBN**
  - **EC2 (EN 1992-1-1:2004)** → [[EC2_index]] — Sections 2, 5, 9, 10, 12 (partial); see index for detail
- **Infrabel-PTR** — PTR CE01 (fyk ≤ 400 MPa) and related. _(populate)_

### Worked-Examples
Good solved reference cases to emulate. Each clearly dated and sourced. Distinct from Methodology (general method) and Salvage (legacy files awaiting conversion).

- _(empty — populate)_

### Python
Patterns and idioms only — handcalcs note structure, pandoc/nbconvert invocations, the docx `w14:paraId` rule. **Not library functions** (those live in `eurocode-lib`).

- _(empty — populate)_

### Salvage
Inventories of legacy spreadsheet tools assessed for conversion into validated notebooks.

- [[_Pile foundations toolbox — salvage map]] — pile & foundation design checks (A–K), incl. the Bovenleidingspaal catenary tool
- [[_Settlement & ground-improvement toolbox — salvage map]] — settlement, consolidation, ground improvement

---

Links: [[CLAUDE]] · [[_Dashboard]]
