---
title: PTR CE01 Ch09 — SLS (Serviceability)
type: norm-extract
source: "PTR CE01 Fascicule 1 v1 (Avis 15 I-AM/2022)"
chapters: [9]
tags: [PTR CE01, Infrabel, SLS, deflection, rotation, twist, L-over-F, railway-bridges, EC0]
related: ["[[PTR CE01 — Index]]", "[[PTR CE01 — Ch03 — Actions]]", "[[_Knowledge — Index]]"]
created: 2026-06-02
---

# PTR CE01 Ch09 — Serviceability Limit States

NBN EN 1990 and its Annex A2 (bridges) apply unless derogated below.

> **Key rule:** Per NBN EN 1990 ANB §A2.4.1 and NBN EN 1991-2 ANB §2.2 — **non-frequent combinations are not used for bridge design. Only frequent combinations are considered.**

---

## 9.1 Civil Engineering Structures

### 9.1.1 Definitions

**Vertical deflections (Figure 9.1):**

| Symbol | Meaning |
|---|---|
| y_t | Theoretical longitudinal profile (ideal alignment) |
| y_p | Deflection under permanent loads (including camber if applied). For rail bridges: rail position under permanent loads. Deferred effects at commissioning and at end of service life. |
| y_s | Deflection of stringers/track under variable loads. For rail bridges: rail position under variable loads + extreme temperature gradient. |
| y_1 | Deflection of main girders under variable loads |
| y_2 | Deflection of cross-girders under variable loads |

**Maximum deflection F:** maximum vertical distance between the deformed profile y_s and any straight line joining two arbitrary points on y_s.

**Maximum relative deflection F/L:** ratio of F to the horizontal distance between the corresponding points (Figure 9.2).

**Camber (*contre-flèche*):** Required so that the bridge does not appear to sag in service. Value must exist after completion and application of all permanent loads.

**Twist t:** difference in cant measured over a 3 m base length for s = 1.435 m gauge (Figure 9.3). Limits twist of the deck affecting wheel-rail contact.

**End rotation θ:** angle between tangent to deformed profile y_s and the theoretical profile y_t at the end of a deck.

---

### 9.1.2 Road bridges — deflection limits

Under **frequent combination:**

$$F/L \leq 1/700$$

(deflection w₃ per NBN EN 1990 §A1.4.3)

---

### 9.1.3 Footbridges — deflection limits

Under **frequent combination:**

$$F/L \leq 1/300$$

For pedestrian bridges: check resonance risk. If fundamental frequency f₀ > 5 Hz, no vibration problem. If f₀ < 5 Hz: perform vibration assessment per SETRA or HiVoSS methodology.

---

### 9.1.4 Railway bridges — deflection limits

Applicable when V ≤ 220 km/h and fundamental frequency is within limits of Figure 6.10 of NBN EN 1991-2.

#### 9.1.4.1 Vertical deflection — L/F limits

Load: **characteristic LM71** (+ SW/0 and SW/2 where required) × **Φ × α**.

**Minimum L/F ratios (Table 9.1 — lower bounds):**

| L (m) | Ballasted track: L/F | Direct fastening: L/F |
|---|---|---|
| ≤ 20 | 600 | 900 |
| 25–30 | (linear interpolation) | (linear interpolation) |
| ≥ 30 | 500 | 800 |
| — | — | — |

*(Exact intermediate values by linear interpolation between 25 m and 30 m. Full table: NBN EN 1990 Annex A2, Table A2.7 — check PTR Table 9.1 for Infrabel-specific lower bounds.)*

**Camber for rail bridges:** in principle **L/1000** under permanent loads (self-weight + permanent loads + ballast + track). For very long spans (≥ 100 m): limited to **L/2000** (absolute value must not be excessive).

**Maximum differential displacement at deck end** (vs. adjacent structure): per §6.5.4.5.2 of NBN EN 1991-2.

**For direct fastening (no ballast):** minimum camber = **40% of the admissible L/F value** (permanent + temperature effects).

#### 9.1.4.2 End rotation limits

Load: **characteristic LM71** (+ SW/0 and SW/2) × **Φ × α** + temperature.

**Admissible end rotations (measured at track axis):**

| Track type | Deck-to-open-track | Two successive decks |
|---|---|---|
| Ballasted | **θ⁻ = 0.0065 rad** | **θ⁺ = 0.0100 rad** |
| Direct fastening | **θ⁻ = 0.0050 rad** | **θ⁺ = 0.0050 rad** |

**Initial counter-rotation (camber rotation)** must be compatible with admissible camber. For direct fastening: counter-rotation ≤ **40% of admissible rotation θ⁻** (permanent + temperature).

#### 9.1.4.3 Twist limits

Load: **characteristic LM71 × Φ × α** (+ SW/0 and SW/2 where required).

For straight track, maximum twist over 3 m wheelbase:

| Speed V (km/h) | Max twist |
|---|---|
| V < 120 | **4.5 mm / 3 m** |
| 120 ≤ V < 200 | **3 mm / 3 m** |
| V ≥ 200 | **1.5 mm / 3 m** |

For switches/crossings or parabolic transitions near deck ends: determine maximum admissible twist case-by-case.

For two successive skew decks: find worst-case bogie position straddling both decks. Total twist t_T ≤ **7.5 mm / 3 m**.

> **Minimum skew angle: > 45°** for ballasted and direct-fastening decks (to limit twist). Exception requires project owner agreement.

#### 9.1.4.4 Horizontal deflection limits

Load: **LM71 (+ SW/0) × Φ × α + temperature effects**.

Horizontal deck deformation must not cause:
- Angular variation exceeding Table A2.8 of NBN EN 1990/A1.
- Horizontal radius of curvature below limits of Table A2.8 of NBN EN 1990/A1.

Longitudinal displacement limits (braking/acceleration and vertical load effects): per §6.5.4.5.2 of NBN EN 1991-2.

---

### 9.1.5 Movable bridges

Examined case-by-case according to specific requirements.

---

## 9.2 Buildings — SLS Deflection Limits

| Element | Deflection limit |
|---|---|
| General | L/300 |
| Cantilever | L/200 |
| Elements supporting components sensitive to deflection (cladding, etc.) | L/500 |

---

Links: [[PTR CE01 — Index]] · [[PTR CE01 — Ch03 — Actions]] · [[PTR CE01 — Ch05 — RC and Prestressed Concrete]] · [[PTR CE01 — Ch08-10-12-14 — Remaining Provisions]] · [[_Knowledge — Index]]
