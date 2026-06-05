---
title: Calculation Instructions
type: doctrine
status: living
created: 2026-06-04
related: ["[[_Tools — README]]", "[[_Knowledge — Index]]", "[[_Python — README]]", "[[CLAUDE]]"]
---

# Calculation Instructions

Governing doctrine for every executable engineering artifact: scripts and calculation notebooks. This note defines **what must be true** of the output — structure, references, verification, gates. It does **not** restate Python idioms; those live in [[_Python — README]] (handcalcs cell layout, `nbconvert --to webpdf`, `pandoc --reference-doc`). It does **not** restate engineering method; that is sourced from `Knowledge/Methodology/` and `Knowledge/Formulas/` and is never duplicated here.

Reference framework, without exception: **Eurocodes + Belgian NBN ANB + Infrabel PTR CE01**. Metric only. `f_yk ≤ 400 MPa` (PTR CE01) wherever reinforcement steel appears. When a parameter is uncertain, **ask — never fill in**.

> [!warning] Read before coding
> No code is written before the planning phase (§0) is complete and any open question is answered. Maximum reasoning is spent on the plan, not recovered after a wrong implementation.

---

## 0. Planning phase — mandatory, before any code

Coding never starts cold. Before the first cell or line:

1. **State the objective in one sentence** — what is designed, verified, or compared, and against which limit state.
2. **Identify the governing references.** Resolve each one to a vault note: norm citation → domain index (`_EC2 — Index`, `_EC7 — Index`, …) → the Methodology / Formulas note. List them explicitly. If a required method or formula has **no vault coverage**, say so in plain words and flag it as a gap to verify — do not silently proceed from memory.
3. **List every input** and its source (geometry, materials, loads, partial factors, NDPs).
4. **List every check** the artifact will perform, each tied to its reference.
5. **Surface every engineering choice** that changes the result — α coefficients, bracket of a bilinear law, favourable/unfavourable factor selection, hooked vs. straight anchorage, etc. (see §7). Each must be a documented, visible decision, never a buried constant.
6. **List open questions.** Anything uncertain is asked **before** coding, not assumed.

Output the plan, get open questions resolved, then code. The plan becomes the skeleton of the notebook's description section (§N-3).

---

## Routing — which artifact, where

- **Script** — does one function: a specific control, a diagram, a single computation. → lives in `Tools/`, governed by **Part A** below. Methodology, if any is needed, is sourced from `Knowledge/`, never copied into the script's folder.
- **Calculation notebook** (`.ipynb`) — a complete, self-contained engineering note that designs or verifies an element in full. → governed by **Part B** below. Its methodology is pulled from `Knowledge/Methodology/` + `Knowledge/Formulas/`; it is built and stored per the conventions here.

Theory stays in `Knowledge/`. Execution lives in `Tools/`. The two are never merged.

---

# PART A — Scripts

A script performs one function and is trusted for reuse only once validated. Rules:

1. **Single responsibility.** One script, one job (a control, a diagram, one computation). If it grows a second engineering responsibility, it is two scripts.
2. **No hardcoded engineering values.** Every parameter that could change — material strength, partial factor, geometry, NDP, α coefficient — is an explicit, named input with units in the name or an adjacent comment (engineering notation: `f_ck_MPa`, `gamma_c`, `d_eff_mm`). A hardcoded value is a latent error the moment a parameter changes. The only literals permitted are true mathematical constants.
3. **Traceable references.** Every formula carries a comment citing its norm in human-readable form — e.g. `# EN 1992-1-1 §6.2.2 eq.(6.2.a)`. The citation must be resolvable to a vault note via the relevant domain index. If no vault note backs it, the comment says so: `# ref: NOT IN VAULT — verify`.
4. **Choices are surfaced, not hidden.** Where the engineer must choose a parameter (e.g. α for anchorage length, hooked vs. straight), the script exposes it as an input and the comment states each option and when it applies (§7). The script never silently picks one.
5. **Math integrity is absolute.** When correcting or refactoring a script, the mathematics is never altered. Architecture, naming, comments, performance — all open to change; the equations are not.
6. **Comment for teaching.** Advanced or non-obvious code is commented to explain the software-architecture or optimisation technique, not just the engineering.
7. **Validation before promotion.** A script enters `Tools/` only after its result has been verified against a known reference (a worked example, a hand calc, or a prior trusted tool). Drafts and unvalidated scripts stay out (CLAUDE.md §2).

---

# PART B — Calculation notebooks

A calculation notebook is a complete, self-explanatory engineering note that designs or verifies one element in full detail. It is built to be read by a reviewer and exported as a PDF annex to the formal calculation file. **Precision and explicitness are the governing qualities** — the note explains itself completely; nothing is left implicit.

The notebook follows a fixed nine-part structure. Order is not optional.

### N-1. Library and tool loading
Python cells, **before everything else**. All imports (`handcalcs`, `numpy`, `pandas`, plotting, export helpers) and any tool setup live here. Cell-layout idioms and the `%%render` mechanics are in [[_Python — README]].

### N-2. Title block
Project number, element, engineer, verificator, company, date. If any of these is missing from the request, **complete it by asking** — do not invent a verificator or a date. Markdown.

### N-3. Description and basis
Built directly from the §0 plan. Contains: a brief description of the element; the norm references (resolved to vault notes, with any gap flagged); a clear statement of what is verified / compared / designed; the hypotheses and assumptions; the limit state(s) considered. A reader must understand the scope before any number appears.

### N-4. Input
A Python cell holding **all** input. If the input set is large, break it into typed cells — geometry, materials, loads, partial factors, etc. Every value carries units in its name or an adjacent comment, engineering notation throughout. **No input is hardcoded downstream** — if a value is used in a calculation, it is defined here, once. A parameter that changes must change in exactly one place.

### N-5. Section / geometry
The element's geometry, normally as a diagram (section, elevation, load layout). A reader should see what is being analysed, not infer it from numbers.

### N-6. Calculations
The core. For **each** step:
- **Markdown first** — explain what is being computed, define every parameter, state the governing clause in human-readable form (resolvable to a vault note).
- **Then the live calculation** — rendered through **handcalcs** so the substituted numbers and the result are shown transparently, not hidden behind an opaque assignment. Maximum transparency is the reason handcalcs is mandatory for the calculation body.
- handcalcs renders the *computation line*. Surrounding explanation, derivation, and parameter definitions are markdown/LaTeX in the preceding cell — the two are separate cells, never forced into one.

Tables, diagrams, and the recap (§N-7) are **not** handcalcs output — they are built separately (pandas / styled HTML / plotting) from the variables already computed.

### N-7. Final verification table
A single recap table presenting, for **every** control: the calculated limit, the actual (demand) value, and the utilisation check (UC = demand / capacity). Every check performed in §N-6 appears as a row. The table is built from the computed variables — never re-typed, never hardcoded.

**Colour coding** — subtle, applied to each row by UC:

| UC band | State | Colour |
|---|---|---|
| UC < 0.60 | underutilised | grey |
| 0.60 ≤ UC < 0.80 | comfortable | green |
| 0.80 ≤ UC < 1.00 | tight | yellow / orange |
| UC ≥ 1.00 | **fails** | red |

The colour is a visual signal of margin, not a substitute for the number — the UC value is always shown.

### N-8. Conclusion
A short closing statement: does the element verify, where are the margins, what governs, any caveat or follow-up. Plain prose.

### N-9. HTML export function
A no-argument function that renders the notebook to HTML (code hidden) for PDF export and annexing to the formal calc file. Export mechanism per [[_Python — README]] (`nbconvert --to webpdf`).

> [!important] Hard gate
> The export **must refuse to produce the file if any control is not OK** — i.e. if any `UC ≥ 1.00`. The function checks every UC before writing; on any failure it raises / aborts with a clear message naming the failing control, and writes nothing. A failing design is never silently exported as if it passed.

---

## Self-check against the reference — mandatory before finalising

Before a notebook is considered done, a dedicated step re-checks it against the source material for transcription errors:

1. For each formula and value used, the agent resolves the citation → domain index → the vault Formulas / Methodology note, and **compares the notebook against the source** — coefficients, exponents, signs, units, partial factors.
2. Any divergence, any value with no vault backing, and any unresolved NDP (e.g. α_cc) is flagged explicitly.
3. This is the agent's pass. **The engineer performs the final manual verification against the norm as the last line of defence** — the self-check assists it, it does not replace it.

A single transcription error (a wrong exponent, a dropped factor, a sign) invalidates the note. This step exists because precision is the entire point.

---

# Cross-cutting rules (scripts and notebooks)

## No hardcoding of anything that can change
This is the single most consequential rule. Any value that could differ between projects, elements, or norm revisions — material strengths, partial factors, NDPs, geometry, coefficients — is defined **once**, as a named input, and referenced everywhere else. A hardcoded result is wrong the instant a parameter shifts, and the error is silent. The only literals allowed are genuine mathematical constants (π, integer exponents fixed by the formula itself). When in doubt, parametrise.

## Surface every engineering choice
Where the engineer must select a parameter, the artifact does not choose silently. It exposes the choice and documents each option and the condition under which it applies. The reader sees the decision and can confirm it.

> [!example] Anchorage length α coefficients (EN 1992-1-1 §8.4.4)
> Computing a design anchorage length `l_bd` from the basic length `l_b,rqd` applies coefficients α₁–α₅, several of which depend on a choice the engineer must make and confirm. The artifact must state them, not bury them:
> - **α₁ — bar shape / effect of form:** `1.0` for a **straight** bar; for a bar in tension with a **standard hook/bend/loop** and adequate cover, `0.7`. The artifact exposes the bar form as an input and applies the matching value — it never assumes straight or hooked.
> - **α₂ — concrete cover:** depends on `c_d` and bar diameter; a choice of cover geometry, not a constant.
> - **α₃ — transverse reinforcement** not welded; **α₄ — welded transverse bars; α₅ — transverse pressure.**
> - Product constraint `α₂·α₃·α₅ ≥ 0.7`, and `l_bd ≥ l_b,min`.
>
> The exact values and the Belgian ANB position are sourced from the vault note, not from memory. If that note does not yet exist, the gap is flagged (`# ref: NOT IN VAULT — verify`). The point of the example is the *pattern*: a coefficient that hinges on an engineering decision is always an explicit, documented input.

## Reference traceability
Every formula — in a script comment or a notebook markdown cell — cites its norm in human-readable form, resolvable to a vault note through the domain index. Where the vault has no coverage, the artifact says so plainly so the engineer knows to double-check. Silence is not permitted; an uncited formula is treated as unverified.

## Math integrity
When correcting, refactoring, or optimising any artifact, the mathematics is never touched. Naming, structure, comments, and performance are all open to change. The equations are not.

## Ask, never assume
If a parameter is uncertain, a reference cannot be found, or a hypothesis is unstated, the question is raised **before** the artifact is produced. A plausible-looking assumption that turns out wrong is worse than a question.

---

Links: [[_Tools — README]] · [[_Knowledge — Index]] · [[_Python — README]] · [[CLAUDE]]
