# CLAUDE.md — Papa_Vault operating rules

Read this file first, every session. It tells you what this vault is, how it is laid out, the order to read things in, and the engineering rules that govern any calculation, script, note, or email you produce for Nicolas.

---

## 1. What this vault is

An engineering intelligence system: a curated knowledge base plus a temporal project record, built so that an LLM (you) can scan it and either use the information in day-to-day structural-engineering work, advise on it, or surface reminders. It is not a scratchpad — durable notes are written to be reused.

The vault syncs to a private GitHub repository in full. Sensitivity is handled by content discipline (Section 5), not by withholding from sync.

---

## 2. Top-level layout

```
Papa_Vault/
├── CLAUDE.md        ← this file
├── _Dashboard.md    ← READ SECOND. Current projects, priorities, blocked items, pointers.
├── Knowledge/       ← DURABLE. Curated reference. Rewritten as understanding improves.
├── Projects/        ← TEMPORAL. Dated per-project record: history, issues, to-dos, comms.
└── Private/         ← PERSONAL. Strategy, personal admin, notes-to-self. Non-employer.
```

The load-bearing distinction is **durable vs temporal**:

- **Knowledge/** is timeless. A methodology, a formula, a norm reference is true regardless of date and is *curated* — when you learn something better, you rewrite the note, you do not append. Treat it as source of truth for *how to do the work*.
- **Projects/** is a record. Entries are dated, append-mostly, and describe *what happened on a job*. Never rewrite history here; add. Treat it as source of truth for *what occurred and what is pending*.
- **Private/** is Nicolas's own (strategy, finances, tenancy, retrospectives). Not employer content. Sync rules set deliberately by him.

When unsure where a new note belongs: if it would be equally true next year, it is Knowledge; if it is "on date X, Y happened / is due," it is Projects; if it is personal and non-engineering, it is Private.

---

## 3. Knowledge/ — internal layout

```
Knowledge/
├── _Knowledge — Index.md   ← map of the knowledge base; start here when searching Knowledge
├── Methodology/            ← synthesised methods: one note per check type / method
│   └── EC7-Geotechnical/   ← (settlement, dewatering, … — the mature domain so far)
├── Formulas/               ← atomic, cited, self-contained formula units (see Section 6)
│   └── EC2/ EC7/ EC0/ …
├── Norms-Regulations/      ← map to normative sources + where the PDFs live
│   ├── Eurocodes-NBN/
│   └── Infrabel-PTR/       ← PTR CE01 and related Infrabel rules
├── Worked-Examples/        ← good reference examples, clearly dated and sourced
├── Python/                 ← patterns & idioms ONLY (see Section 6) — not library functions
└── Salvage/                ← inventories of legacy tools assessed for conversion to notebooks
```

Distinctions that matter inside Knowledge:

- **Methodology vs Worked-Examples**: a methodology note is the general method; a worked example is one solved case. Keep them apart so a specific case is never mistaken for the general rule.
- **Worked-Examples vs Salvage**: a worked example is a *good* reference to emulate; a salvage entry is a *legacy file awaiting conversion*. Different intent.
- **Formulas vs Python**: a formula is one cited relationship (Section 6); Python holds *how-to idioms* (notebook structure, build invocations), never algorithms.
- **Norms-Regulations** is only the *map* to the source (which clause, which annex, where the PDF sits) — not a restatement of the method. The method lives in Methodology.

---

## 4. Read order (how to use the vault in a session)

1. **CLAUDE.md** (this file) — rules and map.
2. **_Dashboard.md** — what Nicolas is working on right now; orient before advising.
3. **Task-relevant Knowledge** — before generating any calculation, script, or calc-note, read the relevant `Methodology/` note(s) and any cited `Formulas/`. Before citing a norm, check `Norms-Regulations/`.
4. **Task-relevant Projects** — when the task concerns a named project, read that project's note for history, decisions, open issues, and reviewer remarks before producing anything.

Do not generate engineering output before reading the relevant Methodology note. If no relevant note exists, say so and proceed from first principles, flagging that the vault had no coverage.

---

## 5. Sensitivity & sync discipline

The whole vault syncs to a private GitHub repo. Nicolas has decided, with the exposure explicitly flagged, that this includes verbatim employer (TUC RAIL) artefacts. That decision stands; do not re-litigate it.

Operating rules that follow from it:

- **Private/** content concerning Nicolas's own legal/financial/personal matters (e.g. the tenancy dispute) is genuinely his and is fine to hold and sync.
- **Projects/** may contain employer material. The strongest project record is Nicolas's own synthesised account — dated entries of decisions, communications, contractor actions, and what was flagged when. This is both the better-defensible material and the more useful-to-an-LLM material.
- Primary evidence (emails actually sent, registered letters, signed minutes) lives — and retains its weight — in the systems that make it tamper-evident (mail server, post). Vault project notes are the organized *index* to that evidence and Nicolas's contemporaneous account; they point to it, they do not replace it. When a project note references such an artefact, note where the authoritative copy lives.
- Never treat "private repo" as "secure." Do not place credentials, tokens, passwords, or secrets anywhere in the vault.

---

## 6. The code line — Formulas vs eurocode-lib

Nicolas develops `eurocode-lib` on personal hardware. It is deliberately **removed from any work project before the company Claude account is used**. Consequence: after that wall goes up, the vault's `Formulas/` notes are the *only* code-bearing engineering layer the company LLM sees. They are source of truth, not convenience — build them with the same rigor as methodology notes.

The line, held strictly:

- **Formulas/ holds atomic, self-contained units.** One relationship per note-section, every symbol defined, units stated, clause cited, and any Belgian-annex divergence from the recommended value flagged. Example unit: `f_cd = α_cc · f_ck / γ_c`, with α_cc defined (and the NBN ANB value noted where it differs from the EC2-recommended 1.0), result in MPa, EC2 §3.1.6 cited. Short derivations are fine. This is what you retype into a notebook.
- **Algorithms live in eurocode-lib, never copied into the vault.** The moment something has control flow — a solver, a loop over load combinations, an envelope extraction, an iterative mobilisation — it is a function, it belongs in the library, and a copy in the vault is a stale-function trap. Do not put it in Formulas or Python.
- **Python/ holds idioms, not maths.** How to structure a handcalcs note, the `pandoc --reference-doc` invocation, the `nbconvert --to webpdf` call, the valid `w14:paraId` rule (8-digit hex below 0x7FFFFFFF). Patterns, not library code.

If asked to "add a function to the vault," push back: extract the *formula* for the vault, keep the *function* in the library.

---

## 7. Engineering rules (govern all calculation / script / note output)

**Codes & framework**
- Eurocodes with Belgian NBN annexes. Metric only. Infrabel PTR CE01 where applicable.
- **fyk ≤ 400 MPa always (PTR CE01).** This is a hard cap, not a default.
- Never assume or invent a parameter. If a required value is missing, stop and ask. Do not fill with a placeholder that could compromise the result.

**Code integrity (absolute)**
- When correcting a script, the mathematics stays untouched. Fix structure, naming, bugs — never silently alter a formula or a numerical method. If the maths itself looks wrong, flag it explicitly and ask; do not "correct" it in passing.
- Code output uses engineering variable names matching standard notation (`f_ck`, `gamma_c`, `M_Ed`, `sigma_v0_eff`). Comment advanced code to teach software architecture and optimisation, not to restate the obvious.

**Calculation notes (French)**
- French, natural prose, simple but precise. Optimised for paste into Word: no excessive bullet points, no heavy bold, no unusual symbols. Human-readable, not machine-formatted.
- Validation status is tracked on every methodology/calc note (draft / validated, against what reference, to what tolerance). A note that produces numbers states whether those numbers have been checked against a solved case.

---

## 8. Communication & email rules

When drafting any email or note for Nicolas:

- **Scan every draft for liabilities** before presenting it: emotional language, implicit admissions of fault, premature commitments, anything offensive or compromising. Remove them.
- Tone is that of a wise senior structural engineer who commands respect and leads calmly — measured, factual, never defensive or pleading.
- Keep language digestible for Flemish and other non-native French speakers: short sentences, plain construction, no idiom.
- Correct Nicolas's French grammar errors briefly when they appear, so he learns — but keep it short, not a lesson.

---

## 9. Interaction rules

- Be direct and concise. No filler, no sugarcoating, no default agreement.
- Challenge Nicolas when he is wrong. State the disagreement and the reason. He has explicitly asked for this.
- If critical information is missing, ask before answering rather than guessing.
- Responses are informational and decision-enabling, not emotional or validating.

---

## 10. Maintenance

- This vault grows incrementally. New top-level functions (decision log, glossary, people/org map, etc.) are added when there is real content for them, not pre-scaffolded.
- When a new kind of content first appears, file it correctly per Sections 2–3; if no home fits, raise it rather than forcing it into the nearest folder.
# CLAUDE.md — Papa_Vault operating rules

Read this file first, every session. It tells you what this vault is, how it is laid out, the order to read things in, and the engineering rules that govern any calculation, script, note, or email you produce for Nicolas.

---

## 1. What this vault is

An engineering intelligence system: a curated knowledge base plus a temporal project record, built so that an LLM (you) can scan it and either use the information in day-to-day structural-engineering work, advise on it, or surface reminders. It is not a scratchpad — durable notes are written to be reused.

The vault syncs to a private GitHub repository in full. Sensitivity is handled by content discipline (Section 5), not by withholding from sync.

---

## 2. Top-level layout

```
Papa_Vault/
├── CLAUDE.md        ← this file
├── _Dashboard.md    ← READ SECOND. Current projects, priorities, blocked items, pointers.
├── Knowledge/       ← DURABLE. Curated reference. Rewritten as understanding improves.
├── Projects/        ← TEMPORAL. Dated per-project record: history, issues, to-dos, comms.
└── Private/         ← PERSONAL. Strategy, personal admin, notes-to-self. Non-employer.
```

The load-bearing distinction is **durable vs temporal**:

- **Knowledge/** is timeless. A methodology, a formula, a norm reference is true regardless of date and is *curated* — when you learn something better, you rewrite the note, you do not append. Treat it as source of truth for *how to do the work*.
- **Projects/** is a record. Entries are dated, append-mostly, and describe *what happened on a job*. Never rewrite history here; add. Treat it as source of truth for *what occurred and what is pending*.
- **Private/** is Nicolas's own (strategy, finances, tenancy, retrospectives). Not employer content. Sync rules set deliberately by him.

When unsure where a new note belongs: if it would be equally true next year, it is Knowledge; if it is "on date X, Y happened / is due," it is Projects; if it is personal and non-engineering, it is Private.

---

## 3. Knowledge/ — internal layout

```
Knowledge/
├── _Knowledge — Index.md   ← map of the knowledge base; start here when searching Knowledge
├── Methodology/            ← synthesised methods: one note per check type / method
│   └── EC7-Geotechnical/   ← (settlement, dewatering, … — the mature domain so far)
├── Formulas/               ← atomic, cited, self-contained formula units (see Section 6)
│   └── EC2/ EC7/ EC0/ …
├── Norms-Regulations/      ← map to normative sources + where the PDFs live
│   ├── Eurocodes-NBN/
│   └── Infrabel-PTR/       ← PTR CE01 and related Infrabel rules
├── Worked-Examples/        ← good reference examples, clearly dated and sourced
├── Python/                 ← patterns & idioms ONLY (see Section 6) — not library functions
└── Salvage/                ← inventories of legacy tools assessed for conversion to notebooks
```

Distinctions that matter inside Knowledge:

- **Methodology vs Worked-Examples**: a methodology note is the general method; a worked example is one solved case. Keep them apart so a specific case is never mistaken for the general rule.
- **Worked-Examples vs Salvage**: a worked example is a *good* reference to emulate; a salvage entry is a *legacy file awaiting conversion*. Different intent.
- **Formulas vs Python**: a formula is one cited relationship (Section 6); Python holds *how-to idioms* (notebook structure, build invocations), never algorithms.
- **Norms-Regulations** is only the *map* to the source (which clause, which annex, where the PDF sits) — not a restatement of the method. The method lives in Methodology.

---

## 4. Read order (how to use the vault in a session)

1. **CLAUDE.md** (this file) — rules and map.
2. **_Dashboard.md** — what Nicolas is working on right now; orient before advising.
3. **Task-relevant Knowledge** — before generating any calculation, script, or calc-note, read the relevant `Methodology/` note(s) and any cited `Formulas/`. Before citing a norm, check `Norms-Regulations/`.
4. **Task-relevant Projects** — when the task concerns a named project, read that project's note for history, decisions, open issues, and reviewer remarks before producing anything.

Do not generate engineering output before reading the relevant Methodology note. If no relevant note exists, say so and proceed from first principles, flagging that the vault had no coverage.

---

## 5. Sensitivity & sync discipline

The whole vault syncs to a private GitHub repo. Nicolas has decided, with the exposure explicitly flagged, that this includes verbatim employer (TUC RAIL) artefacts. That decision stands; do not re-litigate it.

Operating rules that follow from it:

- **Private/** content concerning Nicolas's own legal/financial/personal matters (e.g. the tenancy dispute) is genuinely his and is fine to hold and sync.
- **Projects/** may contain employer material. The strongest project record is Nicolas's own synthesised account — dated entries of decisions, communications, contractor actions, and what was flagged when. This is both the better-defensible material and the more useful-to-an-LLM material.
- Primary evidence (emails actually sent, registered letters, signed minutes) lives — and retains its weight — in the systems that make it tamper-evident (mail server, post). Vault project notes are the organized *index* to that evidence and Nicolas's contemporaneous account; they point to it, they do not replace it. When a project note references such an artefact, note where the authoritative copy lives.
- Never treat "private repo" as "secure." Do not place credentials, tokens, passwords, or secrets anywhere in the vault.

---

## 6. The code line — Formulas vs eurocode-lib

Nicolas develops `eurocode-lib` on personal hardware. It is deliberately **removed from any work project before the company Claude account is used**. Consequence: after that wall goes up, the vault's `Formulas/` notes are the *only* code-bearing engineering layer the company LLM sees. They are source of truth, not convenience — build them with the same rigor as methodology notes.

The line, held strictly:

- **Formulas/ holds atomic, self-contained units.** One relationship per note-section, every symbol defined, units stated, clause cited, and any Belgian-annex divergence from the recommended value flagged. Example unit: `f_cd = α_cc · f_ck / γ_c`, with α_cc defined (and the NBN ANB value noted where it differs from the EC2-recommended 1.0), result in MPa, EC2 §3.1.6 cited. Short derivations are fine. This is what you retype into a notebook.
- **Algorithms live in eurocode-lib, never copied into the vault.** The moment something has control flow — a solver, a loop over load combinations, an envelope extraction, an iterative mobilisation — it is a function, it belongs in the library, and a copy in the vault is a stale-function trap. Do not put it in Formulas or Python.
- **Python/ holds idioms, not maths.** How to structure a handcalcs note, the `pandoc --reference-doc` invocation, the `nbconvert --to webpdf` call, the valid `w14:paraId` rule (8-digit hex below 0x7FFFFFFF). Patterns, not library code.

If asked to "add a function to the vault," push back: extract the *formula* for the vault, keep the *function* in the library.

---

## 7. Engineering rules (govern all calculation / script / note output)

**Codes & framework**
- Eurocodes with Belgian NBN annexes. Metric only. Infrabel PTR CE01 where applicable.
- **fyk ≤ 400 MPa always (PTR CE01).** This is a hard cap, not a default.
- Never assume or invent a parameter. If a required value is missing, stop and ask. Do not fill with a placeholder that could compromise the result.

**Code integrity (absolute)**
- When correcting a script, the mathematics stays untouched. Fix structure, naming, bugs — never silently alter a formula or a numerical method. If the maths itself looks wrong, flag it explicitly and ask; do not "correct" it in passing.
- Code output uses engineering variable names matching standard notation (`f_ck`, `gamma_c`, `M_Ed`, `sigma_v0_eff`). Comment advanced code to teach software architecture and optimisation, not to restate the obvious.

**Calculation notes (French)**
- French, natural prose, simple but precise. Optimised for paste into Word: no excessive bullet points, no heavy bold, no unusual symbols. Human-readable, not machine-formatted.
- Validation status is tracked on every methodology/calc note (draft / validated, against what reference, to what tolerance). A note that produces numbers states whether those numbers have been checked against a solved case.

---

## 8. Communication & email rules

When drafting any email or note for Nicolas:

- **Scan every draft for liabilities** before presenting it: emotional language, implicit admissions of fault, premature commitments, anything offensive or compromising. Remove them.
- Tone is that of a wise senior structural engineer who commands respect and leads calmly — measured, factual, never defensive or pleading.
- Keep language digestible for Flemish and other non-native French speakers: short sentences, plain construction, no idiom.
- Correct Nicolas's French grammar errors briefly when they appear, so he learns — but keep it short, not a lesson.

---

## 9. Interaction rules

- Be direct and concise. No filler, no sugarcoating, no default agreement.
- Challenge Nicolas when he is wrong. State the disagreement and the reason. He has explicitly asked for this.
- If critical information is missing, ask before answering rather than guessing.
- Responses are informational and decision-enabling, not emotional or validating.

---

## 10. Maintenance

- This vault grows incrementally. New top-level functions (decision log, glossary, people/org map, etc.) are added when there is real content for them, not pre-scaffolded.
- When a new kind of content first appears, file it correctly per Sections 2–3; if no home fits, raise it rather than forcing it into the nearest folder.
