---
title: PTR CE01 Ch05 — RC and Prestressed Concrete
type: norm-extract
source: "PTR CE01 Fascicule 1 v1 (Avis 15 I-AM/2022)"
chapters: [5]
tags: [PTR CE01, Infrabel, RC, prestressed, concrete, fyk, partial-factors, cover, anchorage, fatigue, EC2]
related: ["[[PTR CE01 — Index]]", "[[EC2 — ULS material design values]]", "[[_Knowledge — Index]]"]
created: 2026-06-02
---

# PTR CE01 Ch05 — RC and Prestressed Concrete

NBN EN 1992 applies unless derogated below.

---

## 5.1 Verifications Required

In addition to ULS, the following SLS checks are mandatory:

- Stress limitation.
- Crack control.
- Deflection control (considering cracking, shrinkage, creep).
- Fatigue resistance of passive and prestressing reinforcement.

---

## 5.2 Data for Calculations

### 5.2.1 Section geometry (homogenised sections)

For SLS verification, homogenised sections may be used (bonded or equivalent-bonded reinforcement). Equivalence factor α_e:

| Load duration | α_e |
|---|---|
| Short-term | E_s / E_c |
| Long-term | E_s / [E_c · (1 + φ(t,t₀))] |

**Simplified values (no detailed calculation):**
- Reinforced concrete: α_e = 15 for all loads.
- Prestressed concrete: α_e = 15 for long-term; α_e = 6 for short-term.

### 5.2.2 Partial material factors (ULS)

Per NBN EN 1992-1-1 Table 2.1N:

| Situation | γ_c (concrete) | γ_s (passive steel) | γ_s (prestressing steel) |
|---|---|---|---|
| Persistent and transient | **1.50** | **1.15** | **1.15** |
| Accidental | 1.20 | 1.00 | 1.00 |

Reduced γ_c may be used with justified quality control procedures:

| Control level | γ_c |
|---|---|
| Factory-monitored inspection | 1.40 |
| Own inspection | 1.50 |
| Restricted inspection | 1.60 |

### 5.2.3 Prestress effects

Only fully bonded prestressing (post-tensioned grouted tendons or pre-tensioned) is permitted. Unbonded and other systems are prohibited unless the CSC specifically permits them.

Consider: local effects at anchorage zones and deviation points; statically determinate effects in isostatic structures; statically determinate + parasitic effects in hyperstatic structures. Local problems (anchors, deviators): use characteristic ultimate resistance of the prestressing steel as the prestress force.

### 5.2.4 Deferred effects (creep and shrinkage)

Deferred effects need be considered only at SLS unless second-order effects are significant. Creep and shrinkage both contribute to prestress losses and must be accounted for alongside relaxation.

---

## 5.3 Concrete

Self-weights: 24 kN/m³ (plain), 25 kN/m³ (reinforced and prestressed).

### 5.3.1 Compressive strength

Characterised by resistance class (f_ck cylinder / f_ck,cube cube at 28 days, cured in water at 20±2°C per NBN EN 12390-2).

> **For civil engineering structures (bridges):**  
> Minimum class: **C30/37**  
> Maximum class: **C90/105**

### 5.3.2 Creep

ε_cc(t,t₀) = φ(t,t₀) · σ_c / E_c, with E_c = 1.05 E_cm (tangent modulus at 28 days).
Detailed φ formula: Annex B1 of NBN EN 1992-1-1.

### 5.3.3 Shrinkage

Total shrinkage ε_cs = ε_cd + ε_ca (drying + autogenous). Per Table 3.2 and Annex B2 of NBN EN 1992-1-1.

---

## 5.4 Passive Reinforcement

### 5.4.1 Permitted grades

> **Only B500B (PTV 302 of OCAB, designation BE 500…) is permitted for civil engineering structures.**  
> B500A (DE 500 BS, PTV 303) is prohibited.

> **Critical design rule:**  
> **f_yk = 400 N/mm²** must be used in all resistance calculations, regardless of the actual grade (BE500 treated as BE400).

### 5.4.2 Design assumptions

- Density: 7 850 kg/m³.
- Design modulus: E_s = 200 000 N/mm².

### 5.4.3 Geometry

Preferred bar diameters: **6 – 8 – 10 – 12 – 14 – 16 – 20 – 25 – 32 mm**. Diameters > 32 mm to be avoided (crack control).

---

## 5.5 Prestressing Steel

Per PTV 311 or European Technical Agreement. No welding permitted on wires, strands, or bars. Classified by f_p0.1k, f_pk, ε_uk.

**Design moduli:** E_p = 205 000 N/mm² (wires and bars); E_p = 195 000 N/mm² (strands).

**Relaxation (prestress loss):** forfait 15% (exterior conditions) or 20% (interior conditions) of initial prestress force.

---

## 5.6 Durability and Cover

**Crack width limits for structures in permanent contact with groundwater (e.g. culverts):** w_k ≤ **0.20 mm** (§5.8.4 — ensures watertightness).

For other crack width limits: see NBN EN 1992-2 ANB Table 7.101N-ANB.

**Concrete specifications and cover — most common cases:**

| Description | Specification | c_nom / c_min |
|---|---|---|
| Blinding concrete (non-aggressive) | C16/20 – BNA – E0 | — |
| Unreinforced, frost, no rain | C25/30 – BNA – EE2 | — |
| Unreinforced, frost + rain | C30/37 – BNA – EE3 | — |
| RC, frost, no rain | C25/30 – BA – EE2 – WAI(0.50) | 40/30 mm |
| RC, frost + rain | C30/37 – BA – EE3 – WAI(0.50) | 45/35 mm |
| RC, frost + de-icing agents | C35/45 – BA – EE4 – WAI(0.45) | 60/50 mm |
| **Structural bridge elements** | **C35/45 – BA – EE4 – WAI(0.45)** | **60/50 mm** |
| Prestressed, buildings | C50/60 – BP – EE3 – WAI(0.50) | 35/25 mm |
| **Prestressed, bridges** | **C50/60 – BP – EE4 – WAI(0.45) – Cl 0.10** | **50/40 mm** |
| Piles (no rain contact) | C30/37 – BA – EE2, EA1 – cement ≥ 375 kg/m³ | **75 mm** |

*(If specifications conflict, the more demanding applies.)*

---

## 5.7 Reinforcement Detailing

### 5.7.1 Anchorage

$$l_{bd} = \alpha_1 \alpha_2 \alpha_3 \alpha_4 \alpha_5 \cdot l_{b,rqd} \geq l_{b,min}$$

With α-factors per Table 8.2 of NBN EN 1992-1-1. Anchorage lengths calculated using BE500 resistance.

Default table conditions: maximum bar stress (σ_sd = f_yk/1.15), poor bond conditions, all α = 1.

**Anchorage length l_bd (mm) — BE500, poor bond, all α=1 (Table 5.1):**

| φ (mm) | f_ck 25 | f_ck 30 | f_ck 35 | f_ck 40 | f_ck 50 |
|---|---|---|---|---|---|
| 10 | 580 | 510 | 460 | 420 | 360 |
| 12 | 690 | 610 | 550 | 510 | 440 |
| 16 | 920 | 820 | 740 | 670 | 580 |
| 20 | 1150 | 1020 | 920 | 840 | 730 |
| 25 | 1440 | 1280 | 1150 | 1050 | 910 |
| 32 | 1840 | 1630 | 1470 | 1350 | 1160 |

*(Full table for f_ck 20–70 in PTR §5.7.2.1, Table 5.1. Values for f_ck ≥ 55 plateau at f_ck 55 values.)*

> **Note:** This table does not apply to adhesive (chemically bonded) rebar connections drilled into existing concrete. Use EOTA TR 023 method for post-installed rebar.

### 5.7.2 Lap lengths

$$l_0 = \alpha_1 \alpha_2 \alpha_3 \alpha_4 \alpha_5 \alpha_6 \cdot l_{b,rqd} \geq l_{0,min}$$

α_6 depends on percentage of bars lapped in the section. Laps in high-stress zones and in the same section should be avoided. Transverse reinforcement is required in the lap zone per §8.7.4 of NBN EN 1992-1-1.

**Lap length l_0 (mm) — BE500, poor bond, all α₁₋₅=1 (Table 5.2 extract, f_ck 30 and 40):**

| φ (mm) | f_ck 30, <25% | f_ck 30, 50% | f_ck 40, <25% | f_ck 40, 50% |
|---|---|---|---|---|
| 12 | 610 | 860 | 510 | 710 |
| 16 | 820 | 1140 | 670 | 940 |
| 20 | 1020 | 1430 | 840 | 1180 |
| 25 | 1280 | 1790 | 1050 | 1480 |
| 32 | 1630 | 2290 | 1350 | 1890 |

*(Full tables for f_ck 20–60 and all percentages: PTR §5.7.2.2, Table 5.2.)*

### 5.7.3 Welding

Structural welds on reinforcement: **prohibited** (site conditions inadequate).

Tack welds (technological cords) are permitted only for elements that do not require fatigue verification: footbridges (except wind-sensitive elements), foundations, piers/columns not rigidly connected to deck, road/rail bridge abutments not rigidly connected to deck (except hollow abutment slabs).

Welded mesh: same fatigue exemption rule applies.

### 5.7.4 Corner reinforcement

At all re-entrant angles (beams, columns, slabs, walls), bar bends must not follow the inner face of the angle — this would generate concrete spalling ("poussée au vide"). Applies even when the inner angle is chamfered, and applies to precast elements.

---

## 5.8 Section Calculations

### 5.8.1 Flexure at ULS

Concrete tensile strength is ignored in computing the moment of resistance.

### 5.8.2 Prestressed elements

Under all load combinations in the final state, **all concrete fibres must remain in compression.**

For elastic design of prestressed elements, normal stresses are limited to:

| Load combination | σ_c,adm | σ_ct,adm |
|---|---|---|
| G + P (at time of prestressing) | 0.5 f_ck(t) | f_ct0.05 |
| Permanent loads only | 0.45 f_ck | 0 |
| Frequent combination | 0.5 f_ck | 0 |

> Per NBN EN 1990 ANB §A2.4.1 and NBN EN 1991-2 ANB §2.2: **non-frequent combinations are not used for bridge design. Only frequent combinations are considered.**

### 5.8.3 Deflection control

Required when deflections could affect appearance, function, or attached non-structural elements. See Chapter 9 for limits.

### 5.8.4 Crack control

Measures to prevent premature cracking (especially C60/75+ and self-compacting concrete): controlled demoulding after cooling to ambient; cement type and content; aggregate nature; w/c ratio; temperature control during hardening.

> **Structures in permanent contact with groundwater (e.g. culverts/cadres): w_k ≤ 0.20 mm** to ensure watertightness.

---

## 5.9 Fatigue Resistance

### 5.9.1 General

Fatigue verification is required for structures subject to regular load fluctuations. Calculation assumes cracked sections, ignoring concrete tensile resistance, with deformation compatibility.

**Fatigue verification not required for:**
- Footbridges (except wind-sensitive structural elements).
- Buried arch or frame structures with ≥ 1.00 m cover (road) or ≥ 1.50 m cover (rail).
- Foundations.
- Piers and columns not rigidly connected to deck.
- Road/rail bridge abutments not rigidly connected to deck (except hollow abutment slabs).
- Reinforcement in zones where, under frequent combination with P_k, extreme concrete fibres remain in compression.

### 5.9.3 Verification method

Damage accumulation using S-N curves from Figure 6.30 and Tables 6.3N / 6.4N of NBN EN 1992-1-1 (Palmgren-Miner rule). Alternatively, equivalent damage stress range per §6.8.5 of NBN EN 1992-1-1.

**Mechanical couplers:** must demonstrate tensile resistance ≥ continuous bar of the same nominal diameter, plus fatigue resistance (admissible stress range) for ≥ 2×10⁶ cycles. Require approval certificate. If no certificate: experimental testing on minimum 3 specimens per coupler type per bar diameter.

### 5.9.4 Simplified method (NBN EN 1992-2 Annex NN)

**Railway bridges:**

$$\Delta\sigma_{s,equ} = \lambda_s \cdot \Phi \cdot \Delta\sigma_{s,71}$$

where Δσ_s,71 = stress range from LM71 on max. 2 tracks, **without α**, with Φ. λ_s = λ_s1 · λ_s2 · λ_s3 · λ_s4 per NN.3.1 of NBN EN 1992-2.

**Road bridges (FLM3 modified):**

$$\Delta\sigma_{s,equ} = \Delta\sigma_{s,EC} \cdot \lambda_s$$

FLM3 axle loads multiplied by:
- 1.75 at intermediate supports of continuous bridges.
- 1.40 elsewhere.

λ_s = φ_fat · λ_s1 · λ_s2 · λ_s3 · λ_s4 per NN.2.1. φ_fat = 1.2 (good surface) or 1.4 (average surface).

---

Links: [[PTR CE01 — Index]] · [[PTR CE01 — Ch04 — Foundations]] · [[PTR CE01 — Ch06 — Steel]] · [[PTR CE01 — Ch09 — SLS]] · [[EC2 — ULS material design values]]
