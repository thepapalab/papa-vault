---
title: PTR CE01 Ch06 — Steel
type: norm-extract
source: "PTR CE01 Fascicule 1 v1 (Avis 15 I-AM/2022)"
chapters: [6]
tags: [PTR CE01, Infrabel, steel, bridges, fatigue, lambda, welding, bolts, EC3]
related: ["[[PTR CE01 — Index]]", "[[_Knowledge — Index]]"]
created: 2026-06-02
---

# PTR CE01 Ch06 — Steel Structures

NBN EN 1993 applies unless derogated below.

---

## 6.1 Scope

All steel bridges and buildings on the Infrabel network.

---

## 6.2 Imposed Concepts for Bridge Construction

All railway steel bridges must in principle be fitted with a **ballast trough** (coffre à ballast) to allow ballasted track. Exception: movable bridges.

The ballast trough may form part of the structural deck (e.g. orthotropic plate) or be a non-load-bearing structure. If a concrete element contributes to bridge resistance, the structure is treated as a composite bridge (Chapters 5, 6, and 7 apply jointly).

**Permitted main girder types:**
- Plate girders, with or without web stiffeners, simply supported.
- Box girders, simply supported.
- Warren or Pratt trusses, simply supported.
- Arches with independent upper deck.
- Stiffened tied arches with vertical or inclined hangers and lower deck.

For cable-stayed bridges: stability under quasi-permanent combination must be guaranteed with any single cable removed.

**Minimum web thickness:** 10 mm for welded plate main girders, cross-girders, and stringers.

**Section classes:** Classes 1, 2, or 3 per Table 5.2 of NBN EN 1993-1-1. For Class 4, reduced resistance accounting for local buckling must be used.

---

## 6.3 Steel Grades

### 6.3.1 Bridge construction

**Maximum yield strength:** f_y ≤ **460 N/mm²**.

Standards: NBN EN 10025, NBN EN 10027.

**Grade selection per element type:**

| Grade class | Elements |
|---|---|
| J2, K2, M, N, ML, NL (+N) | All welded principal elements of all thicknesses; principal compressed elements t ≥ 15 mm. Includes: main girders, cross-girders, stringers; orthotropic deck plates; all welded truss/arch/box elements; all welded load-bearing profiles. |
| J0 | Welded compressed elements t < 15 mm; non-welded plates and profiles. Includes: bracing profiles (welded, t < 15 mm); cold-formed elements with 2.5–5% elongation; non-welded main girder plates; non-welded profiles t ≥ 15 mm for main girders/cross-girders/stringers. |
| JR | Plates and profiles in non-welded bracing; footbridges connected to the superstructure. |

**Lamellar tearing (Z-quality):** per NBN EN 1993-1-10 and Fascicule 34.4.

### 6.3.2 Building construction

Guidance table (Table 6.1):

| Case | Grade |
|---|---|
| Handrails, chequer plate, non-loaded elements | S235JR |
| Metalwork, riveted construction | S235JR |
| Welded light trusses (roof, etc.) | S235JR |
| Welded, no crane, profiles t ≤ 30 mm / plates t ≤ 25 mm | S235JR |
| Welded, no crane, profiles t > 30 mm / plates t > 25 mm | S235J0 |
| Heavy static loads, light dynamic loads | S235J0 |
| Heavy dynamic loads, all elements t ≤ 10 mm | S235J0 |
| Heavy dynamic loads, elements t > 10 mm | S235J2 / S355K2 |
| Crane runway girder | E295 |

---

## 6.4 Connections

### 6.4.1 General

Connections are by welding or bolting (no other method unless CSC specifies). Designed per NBN EN 1993-1-8.

**Permitted bolt categories:**
- Shear: Category A (bearing) or Category C (slip-resistant at ULS) per Table 3.2 EN 1993-1-8.
- Tension: Category D (non-preloaded) or Category E (preloaded). Category D bolts prohibited in connections subject to variable tension.
- Non-calibrated bolts: only for minor non-structural elements in shear.

### 6.4.2 Welds

**Prescribed weld types (default, unless CSC or detail drawings specify otherwise):**

| Location | Weld type |
|---|---|
| Web-to-flange of stringers, cross-girders, deck plates to stiffeners, main girders | K-weld, full penetration |
| Closed sections (box girders) | Fillet weld with preparation and back-pass; if interior inaccessible after closure: single-side fillet |
| Butt joints | Full X-weld with post-weld grinding |
| Perpendicular connections | Fillet welds |

Throat dimension "a" = height of largest triangle inscribable between weld faces, measured perpendicular to the outer side. Deep-penetration increase of throat is not permitted in resistance calculations (§4.5.2 EN 1993-1-8).

Butt weld locations: chosen to minimise stress variation and total stress. Commercial plate lengths are not a valid primary criterion for placement.

**Site welding:** minimised. All site joints, assembly welds, and necessary field welds must be submitted for prior approval.

### 6.4.3 Erection joints

Number limited to strict minimum. Placed where stress range and total stress are lowest. In principle, joints must have equal resistance to the connected cross-section (full-strength joint). If erection joints are not shown on plans or are insufficient, the contractor adds them (no additional payment) and submits calc notes for approval.

---

## 6.5 Fatigue — Special Requirements for Bridges

Fatigue sizing may govern and **must not be treated as a post-hoc check**. It must be integrated from the early design stages.

Per NBN EN 1993-1-9, using detail categories from Tables 8.1–8.10 for Δσ_c at 2×10⁶ cycles.

### 6.5.1 Road bridges

For FLM1 and FLM2, the inequality F_f · Δσ_E,2 ≤ Δσ_c / γ_Mf may be reduced to:

$$\Delta\sigma_D \leq 0.74 \cdot \Delta\sigma_c / \gamma_{Mf}$$

Equivalent damage factor for FLM3:

$$\lambda = \lambda_1 \cdot \lambda_2 \cdot \lambda_3 \cdot \lambda_4 \leq \lambda_{max}$$

(Figure 9.6 of NBN EN 1993-2 for λ_max)

| Factor | Governs |
|---|---|
| λ_1 | Influence length L (Figure 9.5 EN 1993-2) |
| λ_2 | Traffic composition and frequency (Table 4.7 EN 1991-2 — specified by project owner) |
| λ_3 | Design service life (100 years → **λ_3 = 1.0**) |
| λ_4 | Number of traffic lanes (NBN EN 1993-2 §9.5.2) |

Annual truck volume per slow lane per Table 4.5 of NBN EN 1991-2.

### 6.5.2 Railway bridges

$$\lambda = \lambda_1 \cdot \lambda_2 \cdot \lambda_3 \cdot \lambda_4 \leq \lambda_{max} = \mathbf{1.4}$$

| Factor | Governs |
|---|---|
| λ_1 | Influence length L (EC-mix traffic, Table 9.3 EN 1993-2) |
| λ_2 | Annual transported tonnage (specified by Infrabel) |
| λ_3 | Design service life (100 years → **λ_3 = 1.0**) |
| λ_4 | Two-track decks: reduced probability of simultaneous worst-case loading (NBN EN 1993-2 §9.5.3) |

---

Links: [[PTR CE01 — Index]] · [[PTR CE01 — Ch05 — RC and Prestressed Concrete]] · [[PTR CE01 — Ch07 — Composite Steel-Concrete]] · [[_Knowledge — Index]]
