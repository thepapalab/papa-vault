---
title: Formulas — README
type: index
status: living
created: 2026-06-01
---

# Formulas — README

Atomic, self-contained, cited formula units. This is the code-bearing engineering layer that survives once `eurocode-lib` is removed from work projects — so treat it as source of truth, not convenience (CLAUDE.md §6).

**Rules for a formula note:**
- One relationship per section. Every symbol defined. Units stated. Clause cited.
- Flag any Belgian NBN ANB divergence from the EC-recommended value.
- Short derivations are fine. **No algorithms** — no loops, solvers, envelope extraction, iterative mobilisation. Those are functions and live in `eurocode-lib`.
- fyk ≤ 400 MPa (PTR CE01) wherever reinforcement steel appears.

Organise by Eurocode in subfolders: `EC2/`, `EC7/`, `EC0/`, `EC1/`, `EC3/` …

See [[EC2 — Design values (seed)]] for the format.

---

Links: [[_Knowledge — Index]]
