---
title: PTR CE01 Ch04 — Foundations
type: norm-extract
source: "PTR CE01 Fascicule 1 v1 (Avis 15 I-AM/2022)"
chapters: [4]
tags: [PTR CE01, Infrabel, foundations, EC7, geotechnical, piles, settlements, slopes]
related: ["[[PTR CE01 — Index]]", "[[_Knowledge — Index]]"]
created: 2026-06-02
---

# PTR CE01 Ch04 — Foundations

NBN EN 1997-1 and NBN EN 1997-2 apply unless derogated below.

---

## 4.1 General

Geotechnical reports provided by Infrabel are for information only — the contractor bears full responsibility for understanding site conditions.

Both stability (bearing capacity, overturning, sliding) and deformation (settlement) must be verified for all foundations.

---

## 4.2 Corrosion Protection of Geotechnical Structures

**Permanent structures:** additional material thickness (not coating) for parts in direct soil contact.

| Condition | Additional thickness |
|---|---|
| Near electrified tracks, 100-year service life | **3.0 mm** on radius for round sections |

**Temporary structures:** guaranteed service life ≥ 12 months.

**Permanent soil anchors** near electrified tracks: in principle prohibited (stray currents). Exceptions require a separate agreement between Infrabel and the contractor. If used: passive type only, transverse to tracks, f_yk < 500 N/mm², failure must not cause structure collapse.

---

## 4.3 Geotechnical Investigation

Reference level: DNG (second general levelling). Location in Lambert coordinates.

### 4.3.2 CPT (cone penetration tests)

Electric cone 15 cm², per NBN EN ISO 22476-1:2012. Measurements at maximum 2 cm intervals. Parameters: q_c (cone resistance), f_s (sleeve friction), cone inclination from vertical. If test cannot reach required depth, supplementary boreholes are required.

### 4.3.3 Boreholes

Dry drilling without flushing, with continuous casing (hydraulic tripod). Disturbed samples every 50 cm; undisturbed samples at every change in soil type and at designated depths (diameter ≈ 100 mm, length ≥ 30 cm, static push-in method).

### 4.3.4 Laboratory tests

Per BS 1377-1990 and ASTM. On undisturbed samples (non-exhaustive): bulk density, water content, dry density, void ratio, specific gravity; triaxial CU tests (ASTM D2850, D4767, BS 1377) with measurement of pore pressures and deformations → derive φ' and c' from minimum 4 tests; permeability; compressibility. On disturbed/undisturbed samples at 0.5 m intervals: grading (NBN 933.2, ASTM D1140, D422), Atterberg limits (DIN 18122-1, ASTM D2487), organic content, calcium carbonate content.

### 4.3.5 Piezometric measurements

Minimum duration: **1 year** unless otherwise agreed. Minimum frequency: 2×/month. Apply a 50 cm safety margin above the measured level.

### 4.3.6 Pressuremeter tests

Determine deformation modulus, creep pressure, and limit pressure.

### 4.3.7 Pumping tests

Determine in-situ permeability, drawdown curve, and influence on settlements. All tests by accredited laboratories (Infrabel reserves the right to reject others).

---

## 4.4 Foundation Bearing Capacity

### 4.4.1 Loads

Variable loads for foundation design are taken **without dynamic factor**.

### 4.4.2 Shallow foundations

Per NBN EN 1997-1 §6. Where excavation is performed adjacent to an existing foundation, verify that the existing foundation retains adequate bearing capacity without inadmissible settlement.

### 4.4.3 Deep foundations (piles)

Per NBN EN 1997-1 §7. For axially loaded piles in compression: use CSTC report 20-2020 (EC7 Belgium — ULS of piles and micropiles under axial compression from CPT).

For cast-in-place piles without permanent casing: use design diameters per NBN EN 1992-1-2 §2.3.4.2.

**Large-diameter bored piles:** significant flexural stiffness. Horizontal forces primarily resisted by bending of the pile shaft. Assume continuous soil reaction (linear, parabolic, or semi-parabolic increasing with depth, depending on soil quality). Bending calculation must include moments from force distribution among pile group.

**Diaphragm walls / sheet pile walls with one-sided excavation:** only the stabilising effect at the lowest level can be relied upon.

### 4.4.4 Settlement limits

| Foundation type | Total settlement | Individual pile/footing |
|---|---|---|
| Shallow foundations | 0.05 m | 0.02 m |
| Pile foundations | 2–3% of pile diameter or wall thickness | 1–2% of pile diameter |

Additional criteria: no damage to adjacent installations, no visible damage to other structural parts, no distortion to drainage, cladding, or finishes.

---

## 4.5 Foundation Stability

Global stability must be checked for overturning, horizontal displacement, sliding, and deep sliding per NBN EN 1997-1.

---

## 4.6 Slope Stability

**Global safety factor for slope stability (analytical method, e.g. Bishop): 1.25**

In slope stability checks, design approach DA1/1 is never governing (gravity loads dominate). DA1/2 controls.

For an existing stable slope with no historical instability: the model may be calibrated with a safety factor of 1.0 for the existing slope verification. A disturbed slope must be assessed from scratch per the 1.25 criterion.

**Zone of influence of the track:** from the sleeper head under a slope of 4/4.

**Works in the track influence zone:**
- Under control and with Infrabel approval.
- Mandatory shoring.

**Works in the slope influence zone only (outside track influence zone):**
- Under control and with Infrabel approval.
- Phasing: 5 m sections maximum.

> Geotechnical stability of the slope must be checked for any excavation deeper than **4 m below rail level**.

---

## 4.7 Execution

### 4.7.1 Design assumptions for railway embankments (default values)

| Parameter | Value | Application |
|---|---|---|
| Friction angle | 27° | — |
| Cohesion | 0 kPa | Excavation stability calculation |
| Cohesion | 2 kPa | Retaining wall displacement calculation |

Railway traffic loads: LM71 **without dynamic factor**. For temporary shoring: α = 1 (classification factor).

Maximum allowable horizontal displacement of shoring: **15 mm**. Effect on adjacent track must also be checked (uniform or differential settlement of track).

### 4.7.2 Shoring design by contractor

Where shoring is not shown on plans, the contractor selects the type (sheet piles, Berlin wall, sprayed concrete, bored piles, etc.) and execution method. **Pile driving is prohibited.** All shoring plans and calc notes must be submitted for prior approval by the directing officer.

---

Links: [[PTR CE01 — Index]] · [[PTR CE01 — Ch03 — Actions]] · [[PTR CE01 — Ch05 — RC and Prestressed Concrete]] · [[_Knowledge — Index]]
