---
title: Tools — README
type: index
status: living
created: 2026-06-04
related: ["[[_Calculation-Instructions]]", "[[_Knowledge — Index]]", "[[CLAUDE]]"]
---

# Tools — README

Confirmed, reusable engineering execution: **scripts and calculation notebooks**. This is the execution layer. Theory does not live here — it lives in `Knowledge/`. The two are never merged.

> [!important] Read before producing anything
> [[_Calculation-Instructions]] is the governing doctrine for every artifact in this folder — planning phase, structure, references, verification, gates, no-hardcoding. Read it first, every time.

## What belongs here
- **Scripts** — a single-function tool: a specific control, a diagram, one computation. Validated before it lands here.
- **Calculation notebooks** (`.ipynb`) — complete engineering notes that design or verify an element in full, following the nine-part structure in the instructions note.

Only **validated** artifacts. Drafts and unverified work stay out (CLAUDE.md §2).

## Where method comes from
Methodology and formulas are **sourced from `Knowledge/`** — `Knowledge/Methodology/` and `Knowledge/Formulas/` — and never copied into this folder. A notebook cites its norm in human terms; the citation resolves to a vault note through the domain index (`_EC2 — Index`, `_EC7 — Index`, …). If the vault has no coverage, the artifact flags the gap.

## Where Python idioms come from
The *how* — handcalcs cell layout, `nbconvert --to webpdf`, `pandoc --reference-doc`, the docx workflow — lives in [[_Python — README]]. The instructions note governs *what must be true*; the Python README governs *how to implement it*.

## Status note
This folder is the temporary home for confirmed code while `eurocode-lib` is walled off from work and not yet the live reference. Once `eurocode-lib` is online, library functions are referenced from there, not stored here.

---

Links: [[_Calculation-Instructions]] · [[_Knowledge — Index]] · [[_Python — README]] · [[CLAUDE]]
