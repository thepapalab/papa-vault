---
title: "EC1 Seminar — EN 1991-1-2 Fire Actions: Basic Design Methods & Worked Examples (Vassart)"
type: seminar-note
domain: Fire Actions
eurocode: EC1
source: "Prof. Vassart Olivier (ArcelorMittal R&D) — Workshop 'Structural Fire Design of Buildings according to the Eurocodes', Brussels, 27-28 November 2012"
language: en
status: complete
tags: [EC1, EN-1991-1-2, fire-actions, natural-fire, OZone, HASEMI, HESKESTAD, parametric-fire, localized-fire]
related: [en-1991-1-1-genikes-draseis-draseis-kata-ti-diar, _EC1-Seminar-Index]
created: 2026-06-07
---

# EN 1991-1-2 — Fire Actions: Basic Design Methods & Worked Examples

**Source:** Prof. Vassart Olivier (Chairman CEN/TC250 EC1/Fire E.G., ArcelorMittal R&D)
Brussels Workshop "Structural Fire Design of Buildings according to the Eurocodes", 27-28 November 2012 (142 pp.)

---

## 1. Fire Resistance — European Classes

Three functional criteria define fire resistance (EN 13501):

| Criterion | Symbol | Function |
|---|---|---|
| Load-bearing capacity | **R** | Mechanical resistance under fire |
| Integrity | **E** | Separating function — hot gas barrier |
| Thermal insulation | **I** | Max temperature rise ≤ 140 K (average), ≤ 180 K (max) under standard fire |

Criteria may apply individually or in combination: R, E, I, RE, REI, etc.

Fire resistance = time [min] during which the required function is maintained (e.g. R60, REI90).

### Chain of Events

$$\text{Ignition} \to \underbrace{\text{Thermal action}}_{\text{fire model}} \to \underbrace{\text{Thermal response}}_{\text{material}} \to \underbrace{\text{Mechanical response}}_{\text{structure}} \to \text{Possible collapse}$$

---

## 2. Design Approach: Prescriptive vs. Performance-Based

| Approach | Thermal Input | Data Needed |
|---|---|---|
| **Prescriptive** | Nominal fire curve (ISO 834) | None — only fire rating class |
| **Performance-based** | Physically based fire model | RHR, fire load, geometry, boundaries |

The EN 1991-1-2 framework supports both, with a hierarchy of fire models:

> 🖼️ **[Figure — Fire model hierarchy]** Nominal → Simplified (parametric, localized) → Advanced (OZone, CFD) — `_assets/03a-vassart-ec-firedesign-ws/p013.png`

---

## 3. Nominal Fire Curves

### 3.1 ISO 834 Standard Fire Curve

$$\theta_g = 20 + 345 \cdot \log_{10}(8t + 1) \quad [°C], \quad t \text{ in minutes}$$

Key values: ~842°C at 30 min, ~945°C at 60 min, ~1006°C at 90 min, ~1049°C at 120 min, ~1110°C at 180 min.

**Limitations of the ISO curve:**
- Does not consider pre-flashover phase
- Does not depend on fire load or ventilation
- Applies to entire compartment (even very large ones)
- Never decreases with time

> 🖼️ **[Figure — ISO 834 curve]** θ[°C] vs time [min], 0–180 min — `_assets/03a-vassart-ec-firedesign-ws/p014.png`

### 3.2 Natural Fire vs. Standard Fire

A real fire has three phases: ignition/smouldering → pre-flashover heating → post-flashover (1000–1200°C) → **cooling phase** (absent in ISO curve).

> 🖼️ **[Figure — Natural vs. standard fire]** Comparison of natural fire curve with ISO 834 — `_assets/03a-vassart-ec-firedesign-ws/p015.png`

---

## 4. Physical Parameters for Natural Fire Models

### 4.1 Geometry

- Compartment dimensions (floor area $A_f$, total surface area $A_t$)
- Ceiling height $H$
- Opening area and position (windows, doors)
- Boundary material properties (c, ρ, λ)

### 4.2 Fire Load Density

Design fire load density accounting for active fire safety measures:

$$q_{f,d} = q_{f,k} \cdot m \cdot \delta_{q1} \cdot \delta_{q2} \cdot \prod_i \delta_{ni}$$

**Table — Characteristic fire load qf,k (80th percentile) and RHR:**

| Occupancy | Fire Growth Rate | RHRf (kW/m²) | qf,k (MJ/m²) |
|---|---|---|---|
| Dwelling | Medium | 250 | 948 |
| Hospital (room) | Medium | 250 | 280 |
| Hotel (room) | Medium | 250 | 377 |
| Library | Fast | 500 | 1824 |
| Office | Medium | 250 | 511 |
| School | Medium | 250 | 347 |
| Shopping centre | Fast | 250 | 730 |
| Theatre (cinema) | Fast | 500 | 365 |
| Transport (public) | Slow | 250 | 122 |

**Danger of fire activation δq1** (floor area Af):

| Af (m²) | ≤25 | 250 | 2500 | 5000 | 10000 |
|---|---|---|---|---|---|
| δq1 | 1,10 | 1,50 | 1,90 | 2,00 | 2,13 |

**Danger of fire activation δq2** (occupancy type):

| δq2 | Occupancy examples |
|---|---|
| 0,78 | Art gallery, museum, swimming pool |
| 1,00 | Residence, hotel, office |
| 1,22 | Factory for machinery & engines |
| 1,44 | Chemical laboratory, painting workshop |
| 1,66 | Fireworks / paints factory |

**Active fire safety measures δni:**

| Measure | δni values |
|---|---|
| Automatic water extinguishing system δn1 | 0,61 |
| Independent water supplies δn2 | 0,87 or 0,73 |
| Automatic fire detection (heat) δn3 | 0,87 |
| Automatic fire detection (smoke) δn4 | 0,73 |
| Automatic alarm to fire brigade δn5 | 1,0 / 0,87 / 0,7 |
| Work fire brigade δn6 | 0,61 or 0,78 |
| Off-site fire brigade δn7 | 0,9 or 1,0 |
| Safe access routes δn8 | 1,5 |
| Fire-fighting devices δn9 | 1,0 |
| Smoke exhaust system δn10 | 1,5 |

### 4.3 Rate of Heat Release (RHR) Curve

Fire growth rates (t² fire): $\text{RHR} = \alpha \cdot t^2$

| Fire Growth Rate | Time to reach 1 MW |
|---|---|
| Ultra-fast | 75 s |
| Fast | 150 s |
| Medium | 300 s |
| Slow | 600 s |

> 🖼️ **[Figure — RHR curves]** Growing phase for ultra-fast/fast/medium/slow; stationary and decay phases — `_assets/03a-vassart-ec-firedesign-ws/p024.png`

---

## 5. Simplified Fire Models

### 5.1 Fully Engulfed Compartment — Parametric Fire (Annex A)

Temperature-time curve depends on:
- Opening factor $O = A_v \sqrt{h_v} / A_t$ [m^½]
- Thermal inertia of boundaries $b = \sqrt{\rho c \lambda}$ [J/(m² s^½ K)]
- Design fire load density $q_{f,d}$

> 🖼️ **[Figure — Parametric fire curves]** θ vs time for various O (0.04–0.20 m^½); compared against ISO 834 — `_assets/03a-vassart-ec-firedesign-ws/p035.png`

### 5.2 Localized Fire — HESKESTAD Method (Annex C, case 1: Lf < H)

Applied when flame does not impact the ceiling.

**Flame length:**
$$L_f = -1{,}02 D + 0{,}0148 Q^{2/5}$$

**Gas temperature along flame axis:**
$$\theta(z) = 20 + 0{,}25 (0{,}8 Q_c)^{2/3} (z - z_0)^{-5/3} \leq 900°C$$

where $z_0 = -1{,}02 D + 0{,}0052 Q^{2/5}$ (virtual origin of the flame axis).

### 5.3 Localized Fire — HASEMI Method (Annex C, case 2: Lf ≥ H)

Applied when flame impacts the ceiling. Heat flux on ceiling/beam depends on parameter $y$:

| y range | Heat flux ḣ″ |
|---|---|
| y ≤ 0.30 | ḣ″ = 100,000 W/m² |
| 0.30 < y < 1.0 | ḣ″ = 136,300 − 121,000·y |
| y ≥ 1.0 | ḣ″ = 15,000·y^−3.7 |

$$y = \frac{r + H + z'}{L_h + H + z'}, \quad L_h = 2{,}9 H \left(\frac{Q_H^*}{H}\right)^{0{,}33} - H$$

> 🖼️ **[Figure — HASEMI geometry]** Localised fire impacting ceiling: beam at height H, flame axis, horizontal length Lh — `_assets/03a-vassart-ec-firedesign-ws/p029.png`

---

## 6. Advanced Fire Models — OZone (Two-Zone Model)

### 6.1 Theory

Two-zone model splits compartment into:
- **Lower (cold) zone** — uncontaminated air, T ≈ ambient
- **Upper (hot) zone** — combustion products, TU >> ambient

Transition to one-zone (fully engulfed) when any of:
- T_hot gases > 500°C
- Combustible material in smoke AND T_smoke > 300°C
- Localised fire > 25% of compartment surface
- Smoke height > 80% of compartment height

### 6.2 Software: OZone V2.2

Free software by University of Liège (Cadorin-Franssen). Inputs: compartment geometry, boundary properties, opening factors, RHR curve. Outputs: gas temperature-time curve, zone heights, steel temperatures.

> 🖼️ **[Figure — OZone validation]** OZone vs test data (BRE Test 4, Ulster large compartment test) — `_assets/03a-vassart-ec-firedesign-ws/p062.png`, `p066.png`

---

## 7. Mechanical Actions in Fire — Combination Rules (EN 1990)

### 7.1 Normal Design (Ultimate Limit State)

$$E_d = 1{,}35 G + 1{,}5 Q + 0{,}6 \times 1{,}5 W + 0{,}5 \times 1{,}5 S \quad \text{(offices, Q leading)}$$

### 7.2 Fire Design (Accidental Situation)

$$E_{fi,d} = G + \psi_{1,1} Q_1 + \sum_{i>1} \psi_{2,i} Q_i$$

For offices: $\psi_{1} = 0{,}5$, $\psi_{2} = 0{,}3$ → $E_{fi,d} = G + 0{,}5 Q$ (or $G + 0{,}3 Q$ with $\psi_2$)

**ψ factor table (from EN 1990, key values):**

| Action | ψ0 | ψ1 | ψ2 |
|---|---|---|---|
| Cat A (residential) | 0,7 | 0,5 | 0,3 |
| Cat B (offices) | 0,7 | 0,5 | 0,3 |
| Cat C (congregation) | 0,7 | 0,7 | 0,6 |
| Cat D (shopping) | 0,7 | 0,7 | 0,6 |
| Cat E (storage) | 1,0 | 0,9 | 0,8 |
| Cat F (≤30 kN) | 0,7 | 0,7 | 0,6 |
| Cat G (30–160 kN) | 0,7 | 0,5 | 0,3 |
| Cat H (roofs) | 0 | 0 | 0 |
| Snow (H ≤ 1000 m, non-Nordic) | 0,50 | 0,20 | 0 |
| Wind | 0,6 | 0,2 | 0 |
| Temperature (non-fire) | 0,6 | 0,5 | 0 |

---

## 8. Worked Example 1 — Office Building R+5 (OZone Analysis)

**Building:** 14 m × 30 m floor plan, ceiling height 3.05 m (floor-to-floor 3.4 m), 5 storeys above ground.

**Boundaries:** External walls and slab: 20 cm normal concrete; ceiling: 15 cm normal concrete.

**Occupancy:** Offices → Medium fire growth, RHRf = 250 kW/m², qf,k = 511 MJ/m²

**Three opening scenarios analysed:**

| Scenario | Opening height | Max gas temp | IPE450 steel temp |
|---|---|---|---|
| Ex. 1 | 0.8 m all around | ~850°C | ~800°C |
| Ex. 2 | 1.5 m all around | ~750°C | ~700°C |
| Ex. 3 | Full glazing façade | ~450°C | ~450°C |

> Note: larger openings → lower peak temperature (more ventilation → faster cooling, fuel-controlled rather than ventilation-controlled).

> 🖼️ **[Figure — Ex.1 results]** Gas temperature and oxygen mass for 0.8 m windows; IPE450 steel temperature — `_assets/03a-vassart-ec-firedesign-ws/p099.png`, `p100.png`, `p101.png`

> 🖼️ **[Figure — Ex.3 results]** Full glazing: lower gas temp ~450°C, higher oxygen mass — `_assets/03a-vassart-ec-firedesign-ws/p107.png`, `p109.png`

---

## 9. Worked Example 2 — Localised Fire: Underground Car Park (HASEMI)

**Building:** Underground car park, Auchan Luxembourg

**Parameters:**

| Parameter | Value |
|---|---|
| Ceiling height H | 2.7 m |
| Distance from flame axis to beam r | 0.0 m (directly above) |
| Fire diameter D | 2.0 m |
| Steel beam | IPE 550 |
| Section factor Am/V | 140.1 /m |
| Unit mass ρa | 7850 kg/m³ |
| Surface emissivity εm | 0.7 |
| Emissivity of flame εf | 1.0 |
| Configuration factor Φ | 1.0 |
| Convective heat transfer αc | 25.0 W/(m²K) |

**RHR:** Based on ECSC project — one car fire curve (peak ~4–6 MW).

**Flame length check:**
$$L_f = -1{,}02 \times 2{,}0 + 0{,}0148 Q^{2/5}$$

If Lf ≥ H = 2.7 m → use HASEMI method (flame impacting ceiling).

**Result:** For unprotected IPE 550 directly below flame axis:
$$\theta_{a,\max} = 770°C \quad \text{at } t = 31{,}07 \text{ min}$$

> 🖼️ **[Figure — Steel temperature curve]** IPE550 temperature vs time (localised fire, car park) — `_assets/03a-vassart-ec-firedesign-ws/p122.png`

**Tool:** CaPaFi Excel spreadsheet (University of Liège) implements HASEMI calculation.

---

## 10. Real-World NFSC Applications

European projects where the Natural Fire Safety Concept (NFSC) replaced prescriptive fire rating:

| Building | Country | Type |
|---|---|---|
| Braun Building, Crissier | Switzerland | Medical production |
| BOBST Building, Lausanne | Switzerland | Offices + production |
| Congress centre EPFL, Lausanne | Switzerland | Conference |
| Airbus building | France | Industrial |
| Car park Toulouse Blagnac Airport | France | Parking |
| Greich Office Building, Liège | Belgium | Offices |
| Barreiro Retail Park | Portugal | Retail |
| Exhibition Centre | Portugal | Exhibition |
| IKEA, Lefkosia | Cyprus | Retail |
| Heron Tower (Arup Fire) | UK | High-rise |
| Chambre de Commerce Luxembourg | Luxembourg | Offices |
| ArcelorMittal Office Building, Esch | Luxembourg | Offices |

> 🖼️ **[Figures pp.127–141]** Photo gallery of NFSC projects — `_assets/03a-vassart-ec-firedesign-ws/p127.png` … `p141.png`

---

## 11. Key Takeaways

1. **Performance-based fire design** (natural fire) generally less conservative than ISO 834 for well-ventilated compartments.
2. **Opening factor** is critical: more openings → lower peak temperatures but faster oxygen supply; trade-off between fuel-controlled and ventilation-controlled regimes.
3. **HESKESTAD** applies when flame axis temperature along plume is needed (Lf < H); **HASEMI** applies when flame hits ceiling (Lf ≥ H).
4. **OZone** (free, from ULiège) is the standard tool for two-zone natural fire analysis; validated against multiple large-scale tests.
5. In fire (accidental) combinations: **ψ2 = 0.3** for offices, so effective mechanical load is significantly reduced vs. ULS.

---

## Links

- [[en-1991-1-1-genikes-draseis-draseis-kata-ti-diar]] — ψ-table for fire combination (reference Cat A–H)
- [[_EC1-Seminar — Index]] — EC1 seminar index
