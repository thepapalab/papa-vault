---
title: PTR CE01 Ch03 — Actions
type: norm-extract
source: "PTR CE01 Fascicule 1 v1 (Avis 15 I-AM/2022)"
chapters: [3]
tags: [PTR CE01, Infrabel, actions, LM71, SW0, dynamic-factor, alpha, loads, railway, soil]
related: ["[[PTR CE01 — Index]]", "[[PTR CE01 — Ch09 — SLS]]", "[[_Knowledge — Index]]"]
created: 2026-06-02
---

# PTR CE01 Ch03 — Actions

NBN EN 1991 parts 1-1 to 1-7 and NBN EN 1991-2 apply unless derogated below.

---

## 3.1 Actions on Civil Engineering Structures

### 3.1.2 Self-weight

Material densities per NBN EN 1991-1-1. For structural steel elements: multiply self-weight by **1.03** (accounts for welds, surface treatment, etc.).

### 3.1.3 Permanent actions

**Road surfacing reserve:** 0.5 kN/m² forfait at most unfavourable locations over the full bridge deck surface (sum of profiling reserve + local adjustment reserve).

**Ballast and track:**
- Track (2 rails + sleepers + fasteners): **3 kN/m** linear load.
- Ballast: minimum **10 kN/m²** over full width. If ballast depth under sleeper > 30 cm (see Figure 3.1), the extra depth is added (ballast unit weight = **20 kN/m³**).
- **Design ballast depth = nominal + 30%** (mandatory increase for dimensioning).

**Cable troughs:** minimum 2 kN/m for the trough, plus actual cable load with minimum 1 kN/m.

### 3.1.4 Variable actions — road traffic

Load models per NBN EN 1991-2. Uniformly distributed loads applied only on adverse parts of the influence line.

| Model | Description | Adaptation factors |
|-------|-------------|-------------------|
| LM1 | Tandems + UDL | α_Q1=α_Q2=α_Q3=α_q1=α_q2=α_q3=α_qr = **1.0** |
| LM2 | Single heavy axle 400 kN (§4.3.3 EN 1991-2) | α_Q = 1 (single wheel 200 kN may govern locally) |
| LM3 | Exceptional convoy 900/150 (ANB default for all structures) | Per CSC + Annex A of EN 1991-2 |
| LM4 | Crowd load | To be considered |

### 3.1.5 Variable actions — pedestrians

| Surface type | UDL | Point load |
|---|---|---|
| Public footbridges and walkways | 5 kN/m² | 10 kN on 0.10×0.10 m |
| Service walkways (non-public) | 3.5 kN/m² | 2 kN on 0.20×0.20 m |
| Platforms (*quais*) | 5 kN/m² | 20 kN on 0.20×0.20 m |
| Fixed inspection platforms | 2 kN/m² (class 3 NBN EN 12811-1) | 1 kN on 0.20×0.20 m |
| Mobile inspection platforms | 1.5 kN/m² or 1.2 kN/m linear | — |

**Parapets:** 1.0 kN/m horizontal applied to top rail (at 1.2 m above running surface), either horizontal or vertical. Plus 1 kN point horizontal at any point on top rail; 0.5 kN on intermediate rails.

### 3.1.6 Variable actions — railway traffic

#### 3.1.6.1 Load models

New railway bridges are designed for the combination:

**LM71** — Vertical effect of normal railway traffic. Applied on both rails of one track. Characteristic values: 4 × 250 kN point loads + 80 kN/m UDL (see Figure 3.2 of PTR). Applied per §6.8 NBN EN 1991-2.

> For adverse influence lines with positive and negative regions, the UDL (q_vk) is applied on one track; point loads (Q_vk) up to 4 times on one track.

**SW/0** — Static effect for continuous bridges (multi-span) only.

**SW/2** — Not considered unless specified in the CSC.

**Empty train:** q_vk = 10 kN/m (for specific checks only).

**Simplified equivalent UDL for simply-supported spans (LM71, Table 3.1 — extract):**

| Span L (m) | Q_m (kN/m) | Q_t (kN/m) |
|---|---|---|
| 5.0 | 172.1 | 208.0 |
| 10 | 148.8 | 167.5 |
| 20 | 121.5 | 129.5 |
| 30 | 109.3 | 114.3 |
| 40 | 102.6 | 106.2 |
| 50 | 98.4 | 101.2 |
| 100 | 89.5 | 90.8 |

*(Without dynamic coefficient or classification factor. Full table in PTR §3.1.6.1.)*

Lateral track displacement of **25 mm** must be considered in the design.

#### 3.1.6.3 Classification factor α

> **α = 1.20** for LM71 and SW/0.  
> α = 1.00 for SW/2 and high-speed lines (per STI definition).

α is applied for: **ULS, elastic design of sections, bearing/infrastructure loads, deflections (camber, rotation).**

α is **not** applied for: passenger comfort, fatigue, crack width.

#### 3.1.6.4 Dynamic magnification factor Φ

Accounts for dynamic stress and vibration amplification. Same value for RC, prestressed concrete, steel, and composite structures.

Applies only to vertical loads of LM71 — not to centrifugal forces, braking/starting forces, or hunting forces.

Foundations, piers, and abutments are calculated **without** dynamic factor.

For well-maintained track:

$$\Phi_2 = \frac{1.44}{\sqrt{L_\Phi} - 0.2} + 0.82 \quad \text{with } 1.00 \leq \Phi_2 \leq 1.67$$

where L_Φ is the characteristic length (m) per Table 6.2 of NBN EN 1991-2.

**Reduced dynamic factor** for arch bridges and concrete bridges with cover > 1 m:

$$\Phi_{2,\text{red}} = \Phi_2 - \frac{h - 1.00}{10} \geq 1.0$$

where h = cover thickness including ballast, from top of deck to top of sleeper (m).

### 3.1.7 Horizontal loads

- **Centrifugal forces:** per NBN EN 1991-2 §6.5.1.
- **Hunting (nosing) force:** per NBN EN 1991-2 §6.5.2.
- **Braking and starting forces:** per NBN EN 1991-2 §6.5.3.

### 3.1.8 Track-structure interaction (continuous welded rail)

Where CWR extends beyond one or both ends of the bridge, a fraction of braking/starting forces is transmitted beyond the abutments via the rail. Thermal deformations of the deck generate longitudinal rail forces.

**Braking/starting:** simplified model for single-span deck per §6.5.4.6.1(3) NBN EN 1991-2, with reduction factor ρ from Table 6.9.

**Thermal effects:** For decks with fixed + sliding bearings, characteristic longitudinal force F_Tk = P2 − P1 per track, calculated per §6.5.4.6(4) with k = 20 kN/m (unloaded, normally compacted track).

For decks with elastomeric bearings only: F_Tk = 0 by symmetry.

Detailed calculation: UIC 774-3:2001.

### 3.1.10 Other variable actions

**Wind:** NBN EN 1991-1-4. Reference wind speed v_ref = 28 m/s, terrain category I. For small rigid structures: forfait 2.0 kN/m² allowed. Effective wind area includes deck height + traffic height (road: 2 m above carriageway; rail: 4 m above top of rail), plus shadow effects for multiple girders (Figure 7.42 NBN EN 1991-1-4 ANB).

**Thermal:** NBN EN 1991-1-5.

**Snow:** Not considered for fixed bridges in service. Considered during construction only. For mobile bridges: considered when inclination ≤ 45°.

**Differential settlements:** 10 mm between any two support points (default, unless CSC specifies otherwise). All supports are elastomeric bearings by default.

**Shrinkage and creep:** may be modelled as an equivalent temperature decrease ΔT = ε_cs + 0.50 φ(t,t₀). The factor 0.5 accounts for mutual interaction between shrinkage and creep.

**Friction forces at sliding bearings** (as % of reaction under permanent + variable loads, no dynamic factor):
- Steel-on-steel: 0.15–0.30
- PTFE, contact pressure > 16 N/mm²: 0.01–0.02
- PTFE, contact pressure < 2 N/mm²: 0.03–0.06
- Roller bearings: 0.03–0.05

### 3.1.11 Accidental actions

**Road vehicle impact on deck (superstructure):** h₀ = 4 m, h₁ = 5 m (b = 1 m). Contact surface: 0.25 m high × 2 m wide. Per NBN EN 1991-1-7 §4.3.2.

**Collision force via rigid barriers on deck:** 100 kN horizontal, perpendicular to traffic, at 100 mm below top of barrier or 1.0 m above carriageway/pavement (lowest governs), on a 0.5 m long line. Class A per Table 4.9 of NBN EN 1991-2 ANB.

**Railway derailment on bridge — Class B structures** (rail bridges, road bridges, pedestrian bridges, PX crossings, single-storey uninhabited technical buildings): per NBN EN 1991-1-7 ANB §4.5 Class B. Forces may be reduced by 50% if maximum train speed ≤ 50 km/h. Force application height: 1.8 m above track level.

Zone d < 3 m from track axis (Zone 1): avoid structural elements. Where unavoidable, exceptional load per UIC 777-2:2002 Annex D applies.

**Derailment on the bridge deck (Case I only):** equivalent loads Q_A1d and q_A1d equal to LM71 values, placed parallel to track within a width of 1.5 × track gauge on one side. For ballasted decks, point loads may be assumed to act on a 450 mm × 450 mm area on the deck surface. Check for global stability only (not cantilevers or independent walkways).

**Catenary rupture:** 20 kN per catenary. Number of simultaneous ruptures: 1 catenary for 1 track, 2 for 2–6 tracks, 3 for > 6 tracks.

### 3.1.12 Fatigue

**Partial factor γ_Ff = 1.00**

**Resistance factor γ_Mf:**

| Inspection | Damage-tolerant | Non-damage-tolerant |
|---|---|---|
| Periodic, accessible detail | 1.00 | 1.20 |
| Periodic, poor access | 1.10 | 1.25 |

**Railway bridges — fatigue load model:** LM71 at the most unfavourable position (+ SW/0 if required). Detailed traffic models (standard, heavy, light) per Annex D of NBN EN 1991-2 may be used. Centrifugal and longitudinal forces are excluded from fatigue checks; hunting forces also excluded.

**Road bridges — fatigue load models:** FLM1 and FLM2 for cut-off limit check. FLM3, FLM4, FLM5 for life calculation (100-year service life). FLM5 is not applicable.

### 3.1.13 Soil actions on retaining structures

**At-rest pressure:** apply when the wall cannot move, or when recompaction (e.g. by rail traffic or repeated surcharges) prevents reduction to active pressure.

**Surcharges generating horizontal pressure:**

| Traffic type | Surcharge | Depth | Width |
|---|---|---|---|
| Road | 20 kN/m² | 30 cm below carriageway | Road width |
| Rail | 62.5 kN/m² (α included) | 70 cm below rail level | 3 m |

> A reduced rail surcharge of 50 kN/m² (α included) may be used if the designer can demonstrate it is justified (e.g., massive wall > 10 m long, ≥ 3.5 m from track axis).

---

Links: [[PTR CE01 — Index]] · [[PTR CE01 — Ch01-02 — General and Project Guidelines]] · [[PTR CE01 — Ch04 — Foundations]] · [[PTR CE01 — Ch09 — SLS]]
