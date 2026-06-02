---
title: EC2 — ULS material design values
type: formulas
eurocode: EC2
domain: Concrete
status: draft
tags: [formulas, EC2/concrete, ULS, design-values, material-properties]
related: ["[[M-N interaction diagram — methodology]]", "[[_EC2 — Index]]", "[[_Knowledge — Index]]"]
created: 2026-06-02
---

# EC2 — ULS material design values

Atomic, cited design values for EC2 ULS section design of reinforced concrete. One relationship per section; symbols defined, units stated, clause cited, Belgian-annex / PTR divergence flagged. Source of truth for notebook-building (CLAUDE.md §6). Framework: EN 1992-1-1 + NBN EN 1992-1-1 ANB + Infrabel PTR CE01.

> [!warning] Open parameter — α_cc (see §3 below)
> α_cc is **not resolved**. EC2 recommends 1.0; the working M-N script uses 0.85 with unverified provenance (carried over from a non-Belgian source). It scales f_cd — and therefore every resistance — linearly. The governing value (NBN ANB / PTR CE01) must be confirmed before any number derived from these values is used. Do not treat 0.85 as confirmed.

---

## 1. Partial factors (persistent & transient situations)

- γ_c = 1.5 — concrete.
- γ_s = 1.15 — reinforcing steel.

Dimensionless. EN 1992-1-1 §2.4.2.4, Table 2.1N. Belgian ANB: confirm no divergence from the recommended values (these are the EC2-recommended figures).

---

## 2. Concrete strain limits (f_ck ≤ 50 MPa)

- ε_c2 = −0.0020 — strain at peak compressive stress (onset of the plateau in the parabola-rectangle law). **Not** a "yield" strain.
- ε_cu2 = −0.0035 — ultimate compressive strain.

Dimensionless, compression negative. EN 1992-1-1 Table 3.1.

> [!note] Validity ceiling
> These two values are constant **only up to C50/60**. For f_ck > 50 MPa both reduce (EN 1992-1-1 Table 3.1: ε_c2 rises in magnitude toward −0.0026, ε_cu2 falls toward −0.0026 at C90). A class-general implementation must compute them from f_ck, not hardcode −0.0020 / −0.0035.

---

## 3. Design compressive strength of concrete

$$f_{cd}=\alpha_{cc}\,\frac{f_{ck}}{\gamma_c}$$

- f_cd, f_ck in MPa; γ_c dimensionless (§1); α_cc dimensionless.
- EN 1992-1-1 §3.1.6(1)P, eq. (3.15).

**α_cc** — coefficient for long-term effects on compressive strength and unfavourable effects from load application. Nationally Determined Parameter; EC2-recommended value **1.0** (§3.1.6(1)P). **Belgian NBN ANB / PTR CE01 value: TO CONFIRM** (see top-of-note warning). Until confirmed, f_cd is parametric in α_cc.

---

## 4. Parabola-rectangle law for concrete (design)

$$\sigma_c(\varepsilon)=\begin{cases}0 & \varepsilon\ge 0\\[4pt]-f_{cd}\left(2-\dfrac{\varepsilon}{\varepsilon_{c2}}\right)\dfrac{\varepsilon}{\varepsilon_{c2}} & \varepsilon_{c2}<\varepsilon<0\\[8pt]-f_{cd} & \varepsilon_{cu2}\le\varepsilon\le\varepsilon_{c2}\end{cases}$$

- σ_c in MPa; ε dimensionless, compression negative.
- The parabolic exponent is n = 2 for f_ck ≤ 50 MPa (reduces above; EN 1992-1-1 Table 3.1).
- EN 1992-1-1 §3.1.7(1), Fig. 3.3.

---

## 5. Design yield strength of reinforcement

$$f_{yd}=\frac{f_{yk}}{\gamma_s}$$

- f_yd, f_yk in MPa; γ_s dimensionless (§1).
- EN 1992-1-1 §3.2.7(2).

> [!important] f_yk cap — Infrabel PTR CE01
> **f_yk ≤ 400 MPa** on all Infrabel work. Hard cap, not a default. (PTR CE01; see [[_Knowledge — Index]] → Norms-Regulations / Infrabel-PTR.)

---

## 6. Reinforcement modulus and strains

- E_s = 200 000 MPa (200 GPa) — design modulus. EN 1992-1-1 §3.2.7(4).
- ε_y = f_yd / E_s — design yield strain (dimensionless).
- ε_ud — design ultimate strain limit. EC2-recommended ε_ud = 0.9·ε_uk (NDP, §3.2.7(2)). With the **horizontal** top branch (option (B), Fig. 3.8) no strain ceiling is required; the working M-N model adopts ε_ud = 0.01 as a conservative cap, which limits only the extent of the pure-tension domain, not the stress.

---

## 7. Bilinear law for reinforcement (design, horizontal top branch)

$$\sigma_s(\varepsilon)=\begin{cases}-f_{yd} & -\varepsilon_{ud}\le\varepsilon\le-\varepsilon_{y}\\[4pt]E_s\,\varepsilon & -\varepsilon_{y}<\varepsilon<\varepsilon_{y}\\[4pt]+f_{yd} & \varepsilon_{y}\le\varepsilon\le\varepsilon_{ud}\end{cases}$$

- σ_s in MPa; ε dimensionless, tension positive.
- EN 1992-1-1 §3.2.7, Fig. 3.8 (option B, horizontal top branch). The inclined-branch alternative (top branch rising to k·f_yk at ε_uk) is not used here.

---

## 8. Auxiliary concrete properties (as needed)

- f_cm = f_ck + 8 (MPa) — mean compressive strength. EN 1992-1-1 Table 3.1.
- f_ctm = 0.30·f_ck^(2/3) for f_ck ≤ 50; f_ctm = 2.12·ln(1 + f_cm/10) for f_ck > 50 (MPa). EN 1992-1-1 Table 3.1.

---

## Open items

- **α_cc** — confirm NBN ANB / PTR CE01 value (blocks numerical use; §3).
- **Belgian ANB partial factors** — confirm γ_c, γ_s carry no national divergence (§1).
- Source PDFs and exact clause/annex locations to be mapped under `Norms-Regulations/` (Eurocodes-NBN, Infrabel-PTR).

---

Links: [[M-N interaction diagram — methodology]] · [[_EC2 — Index]] · [[_Knowledge — Index]] · [[CLAUDE]]
