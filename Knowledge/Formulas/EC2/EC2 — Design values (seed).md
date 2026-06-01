---
title: EC2 — Design values (seed)
eurocode: EC2
domain: Concrete
clause: EN 1992-1-1 §3.1.6, §3.2.7
status: seed
created: 2026-06-01
tags: [formula, EC2, material, design-value]
---

# EC2 — Design values

Seed note showing the Formulas/ format. Each block is one atomic, cited relationship.

## Concrete design compressive strength

$$f_{cd} = \alpha_{cc} \cdot \frac{f_{ck}}{\gamma_c}$$

- `f_cd` — design compressive strength [MPa]
- `f_ck` — characteristic cylinder compressive strength at 28 days [MPa]
- `α_cc` — coefficient for long-term effects and unfavourable loading effects. EC2 recommended value **1.0**; the value can differ by National Annex.
  > [!warning] Belgian NBN ANB
  > Confirm the α_cc value in the Belgian NBN EN 1992-1-1 ANB before use — it is a Nationally Determined Parameter and may differ from the recommended 1.0. Do not assume; check the annex (see `Norms-Regulations/Eurocodes-NBN`).
- `γ_c` — partial safety factor for concrete. Persistent & transient: **1.5**; accidental: **1.2** (EC2 Table 2.1N; confirm against NBN ANB).

## Steel design yield strength

$$f_{yd} = \frac{f_{yk}}{\gamma_s}$$

- `f_yd` — design yield strength of reinforcement [MPa]
- `f_yk` — characteristic yield strength [MPa]
  > [!important] PTR CE01 cap
  > **f_yk ≤ 400 MPa** for Infrabel work (PTR CE01). This overrides the common 500 MPa (B500) assumption. Hard cap.
- `γ_s` — partial safety factor for reinforcing steel. Persistent & transient: **1.15**; accidental: **1.0** (confirm against NBN ANB).

---

Links: [[_Formulas — README]] · [[_Knowledge — Index]]
