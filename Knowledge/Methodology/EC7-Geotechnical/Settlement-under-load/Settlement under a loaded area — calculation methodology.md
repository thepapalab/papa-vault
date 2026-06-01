---
title: Settlement under a loaded area — calculation methodology
eurocode: EC7
domain: Geotechnical
check_type: Serviceability — settlement under applied load
method: Newmark (4-corner) stress distribution n=3 Boussinesq / n=4 Buisman; Terzaghi log compression; Terzaghi U(Tv) consolidation with De Beer stress-dependent cv
groundwater: Phreatic (water table before/after load)
status: validated
maturity: predesign
tags: [methodology, EC7/geotechnical, settlement, load-induced, terzaghi, boussinesq, buisman, consolidation, validated]
related: ["[[Dewatering-induced settlement — methodology]]", "[[Settlement under a loaded area — methodology]]", "[[_EC7 — Index]]", "[[_Methodology — Index]]"]
script: EC7_Tassement_Charge (handcalc notebook, validated to <0.1 mm)
created: 2026-05-31
---

# Settlement under a loaded area — calculation methodology

> [!abstract] One line
> Settlement of a point in the ground under an **applied load** spread over a rectangular area — final magnitude and time course. Driver is the load (fill, footing, embankment, track), not water removal. Load-induced counterpart to [[Dewatering-induced settlement — methodology]]. This is the **validated** methodology (engine matched to a solved reference to <0.1 mm); it supersedes the earlier tutorial note [[Settlement under a loaded area — methodology]].

> [!success] Validation
> Engine validated against a solved reference case: per-layer final settlement exact to four decimals, total 521.1 mm within 0.1 mm; time-dependent settlement reproduced exactly. Surface influence factor I(0) = 1.000 as required.

---

## 1. Governing idea

A load on the ground compresses the soil beneath. Two quantities are needed: (1) **how much the vertical effective stress increases at each depth** under the point of interest, given the load acts on a finite surface area (stress spreads and attenuates with depth) — the **stress-distribution** problem; (2) **how much each layer compresses** under that increase and **how fast** — the **compression + consolidation** problem.

Stress distribution is solved with the **Newmark four-corner superposition** (closed-form Boussinesq n=3 or Buisman n=4). Magnitude is solved with the **Terzaghi logarithmic compression law**, time course with **Terzaghi one-dimensional consolidation**.

Two settlements result: the **final** settlement (consolidation complete) and the **time-dependent** settlement (fraction reached at time t via U(Tv)).

---

## 2. Scope and assumptions

**Conditions for validity:** (1) soil homogeneous and isotropic per layer; (2) grains and pore water incompressible (settlement = water expulsion + rearrangement); (3) load uniform over its area; (4) compressibility constant C and permeability k constant over a layer and during consolidation; (5) the entered load is the **net additional** load (pre-existing surcharge handled separately).

**Strong fit:** settlement under a fill/embankment; under a footing, raft or slab (rectangular footprint); under railway/road loading represented as a loaded rectangle; predesign magnitude + time; differential settlement between two points (run at each point).

**Poor fit:** settlement from lowering the water table (no load) → [[Dewatering-induced settlement — methodology]]; bearing capacity / ULS → a resistance check; >4 distinct layers → group or extend; strongly over-consolidated clay where the load crosses the pre-consolidation pressure → a Cc/Cr refinement beyond the single-C log law.

> [!tip] Relationship to the dewatering note
> Both end in the same Terzaghi compression and consolidation machinery. They differ only in what generates Δσ′: an applied surface load via Newmark superposition (here) versus loss of buoyancy from drawdown (dewatering). Pick by mechanism.

---

## 3. Inputs

> [!warning] Never assume a parameter — flag if missing
> Geometry: depth step Δz; water table depth (before and after load); influence depth (rigid base below). Per layer (≤4): thickness, γ_dry, γ_sat (γ_nat), compressibility constant **C**, permeability **k**, drainage factor (0.5 double / 1.0 single). Load: rectangle sides LARZ × LORZ, net pressure before and after, stress-law exponent n (3 or 4). Elapsed time for the time-dependent result. γ_w = **10 kN/m³** (source-tool convention).

---

## 4. Effective stress

Initial effective vertical stress σ′v0(z) is integrated downward: γ_dry above the water table, submerged (γ_sat − γ_w) below. The load is the **net additional** pressure Δp; before/after surcharges are tracked separately so the stress *change* is correct. Per sub-layer the mid-depth effective stress before (σ′o) and after (σ′n) is used.

---

## 5. Step 1 — Stress distribution (Newmark four-corner)

The stress increase at depth z under a point is the superposition of **four uniformly-loaded rectangles sharing that point as a common corner**. The footprint influence factor is therefore:

$$I(z) = 4\,I_{corner}(z), \qquad I(0) = 1.0$$

**I(0) = 1 is the correctness check** — directly under the load, surface stress equals the full applied pressure.

> [!danger] Convention that must be used
> The corner factor is the **complete Newmark/Boussinesq expression with arctan branch correction**. A reduced single-term corner formula gives only ≈0.10 at the surface and yields a settlement **≈half** the correct value. Always verify I(0) = 1.

**n = 3 — Boussinesq corner factor**, with m = a/z, n = b/z:

$$I_{corner}=\frac{1}{4\pi}\left[\frac{2mn\sqrt{m^{2}+n^{2}+1}}{m^{2}+n^{2}+1+m^{2}n^{2}}\cdot\frac{m^{2}+n^{2}+2}{m^{2}+n^{2}+1}+\arctan\!\frac{2mn\sqrt{m^{2}+n^{2}+1}}{m^{2}+n^{2}+1-m^{2}n^{2}}\right]$$

**Branch correction:** add π to the arctangent when $m^{2}+n^{2}+1 < m^{2}n^{2}$ (argument crosses π/2 at shallow depth). Without it the shallow-depth factor is wrong.

**n = 4 — Buisman corner factor** (normally consolidated, modulus increasing with depth):

$$I_{corner,4}=\frac{a\,z}{4\pi(z^{2}+a^{2})}\left[\frac{3z^{2}+2a^{2}}{z\sqrt{z^{2}+a^{2}}}\arctan\!\frac{b}{\sqrt{z^{2}+a^{2}}}+\frac{a\,b}{z^{2}+a^{2}+b^{2}}\right]$$

The stress increase is `Δσ(z) = Δp · I(z)`. Effective stress at depth = geostatic + load term, in the before (Δp_before) and after (Δp_after) states.

> [!note] Meaning of n
> Larger n → stress stays more concentrated under the load. n=3 spreads more (elastic half-space); n=4 concentrates more (modulus growing with depth). Chosen per layer by soil behaviour.

**Figure A:** σ′ before/after versus depth. The gap between curves is the Δσ′ driving settlement; it concentrates near the surface and decays toward the influence depth.

---

## 6. Step 2 — Settlement magnitude (Terzaghi compression)

Per sub-layer of thickness Δh, using mid-depth effective stresses:

$$\Delta h = \frac{\Delta h_{layer}}{C}\,\ln\!\frac{\sigma'_{n}}{\sigma'_{o}}$$

**Loading** (σ′n > σ′o) uses the compression constant C. **Unloading** (σ′n < σ′o, e.g. excavation) uses a **recompression constant supplied by the user** — it is *not* derived from compression data, and the calculation must refuse to proceed if it is missing rather than assume one. Total final settlement = sum over sub-layers to the influence depth.

> [!note] Why logarithmic; what C is
> Settlement depends on the *ratio* σ′n/σ′o, not the absolute difference — a given increment compresses a lightly-stressed shallow layer more than a deep, already-compressed one. C is the constrained compressibility constant (higher C = stiffer = less settlement); here entered directly per layer rather than derived from cone resistance.

**Figure B:** cumulative settlement versus depth — locates the compressible layers.

---

## 7. Step 3 — Time-dependent settlement (Terzaghi consolidation)

Pore water must drain, so settlement develops over time. Fraction reached at time t is U(Tv).

> [!important] Stress-dependent consolidation coefficient (validated)
> The time factor uses a **De Beer stress-dependent coefficient**, NOT the textbook cv = k·E/γw:
> $$T_v = \frac{c_{v,eff}\,t}{H_{dr}^{2}}, \qquad c_{v,eff} = \frac{k\,C\,\sigma'_{o,mid}}{10}, \qquad H_{dr} = f_{drain}\cdot h$$
> with σ′ in kPa, f_drain = 0.5 (double drainage, permeable above and below) or 1.0 (single). σ′_o,mid is the mid-layer initial effective stress.

Average degree of consolidation, Terzaghi series (7 terms ample):

$$U(T_v)=1-\frac{8}{\pi^{2}}\sum_{m=0}^{6}\frac{1}{(2m+1)^{2}}\exp\!\left[-\frac{(2m+1)^{2}\pi^{2}}{4}T_v\right]$$

Settlement at time t per layer = U(Tv) · (final settlement of that layer), summed.

**Figure C:** settlement versus time on a log-time axis, asymptotic to the final settlement. Early slope and time-to-90% inform surcharge/waiting decisions.

---

## 8. Calculation path

1. **Inputs & grid** — geometry, layers, load, n, time; depth grid at Δz; water table on a grid node; γ_w = 10.
2. **Effective stress** — σ′v0(z) (γ_dry above WT, γ_sat − γ_w below); net load Δp.
3. **Stress distribution** — I(z) = 4·I_corner with branch correction (verify I(0)=1); Δσ = Δp·I; σ′ before/after → Figure A.
4. **Magnitude** — per sub-layer Δh = (Δh/C)·ln(σ′n/σ′o); C for loading, user recompression constant for unloading; sum → Figure B.
5. **Time** — per layer cv,eff = k·C·σ′o,mid/10; Tv = cv,eff·t/(f_drain·h)²; U(Tv) 7-term series; settlement(t) = ΣU·Δh_final → Figure C.
6. **Synthesis** — final settlement, settlement at t, differential between points vs serviceability criteria.

---

## 9. Diagrams (what to look for)

- **Figure A — stress with depth (before/after):** confirms load placement and depth of influence; gap = Δσ′.
- **Figure B — cumulative settlement with depth:** locates compressible layers.
- **Figure C — settlement versus time:** consolidation curve; early slope and time-to-90% drive surcharge/waiting decisions.

> [!important] Differential settlement governs structures
> Total settlement rarely damages a structure — **differential** settlement does. Run at the relevant points (two corners of a slab, or track at two chainages) and compare the difference to the applicable distortion limit. Railway limits are tighter than building limits and speed-dependent — use the Infrabel specification, not a generic value.

---

## 10. Limits

- **Single C** per layer (no Cc/Cr split): for strongly over-consolidated clay where the load crosses the pre-consolidation pressure, a recompression/virgin refinement may be needed.
- **Unloading/heave** is structurally supported but requires a user-supplied recompression constant; it could not be validated against the reference (loading-only case).
- **≤4 layers** in the source; group or extend if more.
- **Predesign maturity:** direct-entry C and layer averaging make this order-of-magnitude / comparative; validate C and k against site oedometer/CPT data for project use.

---

## 11. Standards and basis

- **Compression:** Terzaghi one-dimensional logarithmic law (constrained compressibility constant C).
- **Stress distribution:** elastic stress under a uniformly loaded rectangle — Boussinesq (n=3) and Buisman (n=4), superposed by Newmark's four-corner method.
- **Consolidation:** Terzaghi one-dimensional theory; average degree U(Tv) via the Fourier series; stress-dependent (De Beer) consolidation coefficient.
- **Framework:** Eurocode 7 (EN 1997-1) + Belgian NBN annexes; distortion criteria per the applicable (Infrabel) specification.

---

## 12. Status

**Validated; notebook built** — `EC7_Tassement_Charge` (handcalcs, French calc-note prose, three figures, loading + unloading, code hidden on HTML→PDF export). Validated against a solved reference case to <0.1 mm.

Links: [[Dewatering-induced settlement — methodology]] · [[Settlement under a loaded area — methodology]] (earlier tutorial) · [[_EC7 — Index]] · [[_Methodology — Index]]
