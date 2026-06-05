---
title: Settlement under a loaded area — methodology
eurocode: EC7
domain: Geotechnical
check_type: Serviceability — settlement under applied load
method: Terzaghi compression + triangle (Newmark) stress distribution; n=3 Boussinesq / n=4 Buisman; Terzaghi U(Tv) consolidation
groundwater: Phreatic (water table before/after load)
status: draft
maturity: predesign / tutorial
tags: [methodology, EC7/geotechnical, settlement, load-induced, terzaghi, boussinesq, buisman, consolidation]
related: ["[[Dewatering-induced settlement — methodology]]", "[[_EC7 — Index]]", "[[_Methodology — Index]]"]
script: to be built when a project requires it
created: 2026-05-31
---

# Settlement under a loaded area — methodology

> [!abstract] One line
> Computes the settlement of a point in the ground caused by an **applied load** spread over a rectangular area — both the final settlement and how it builds up over time. The driver is the **load** (fill, footing, embankment, track), not water removal. This is the load-induced counterpart to [[Dewatering-induced settlement — methodology]].

> [!info] This note is a tutorial
> It reverse-engineers a settlement spreadsheet so the calculation can be reproduced from scratch without the original file. Every step below maps to a formula the future notebook must implement. Standards are named where the method derives from them; values follow Eurocode 7 + Belgian NBN annexes, fyk ≤ 400 MPa (PTR CE01) where reinforcement is involved (not here).

---

## 1. What it computes, and the governing idea

Put a load on the ground and the soil beneath compresses. Two things must be quantified:

1. **How much does the vertical stress increase at each depth** under the point of interest, given that the load sits on a finite area at the surface? Stress spreads and attenuates with depth — directly under the load it is largest, and it decays laterally and with depth. This is the **stress-distribution** problem.
2. **How much does each soil layer compress** under that stress increase, and **how fast**? This is the **compression + consolidation** problem.

The method answers (1) with the **triangle method** (a Newmark-type superposition of uniformly loaded rectangles) and (2) with **Terzaghi** compression for magnitude and **Terzaghi one-dimensional consolidation** for the time course.

> [!note] Two settlements are produced
> - **Time-independent (final) settlement** — the total settlement once consolidation is complete.
> - **Time-dependent settlement** — the fraction of that total reached after a given elapsed time, via the consolidation degree U(Tv).

---

## 2. Scope, assumptions and when to use it

**Application conditions (must hold for the result to be meaningful):**
1. Soil is homogeneous and isotropic within each layer.
2. Grains and pore water are incompressible (settlement = expulsion of water / rearrangement, not compression of solids/water).
3. The applied load is uniform over its area (each sub-area may carry a different uniform pressure).
4. The compressibility constant C and permeability k are constant over a layer's thickness and throughout consolidation.
5. The surface load entered is the **net additional** load only — the pre-existing infinite surcharge is subtracted (see §4).

**Strong fit:**
- Settlement under a **fill or embankment** over compressible soil.
- Settlement under a **footing, raft, or slab** (rectangular footprint).
- Settlement under **railway or road loading** represented as a loaded strip/rectangle.
- Predesign estimate of settlement magnitude and time, and differential settlement between two points (run the calculation at each point).

**Poor fit (use another method):**
- Settlement from **lowering the water table** (no applied load) → [[Dewatering-induced settlement — methodology]].
- **Bearing capacity / ULS** of a foundation → a bearing-resistance check, not this.
- Layered profiles with **more than 4 distinct layers** → group layers, or extend the method.
- Where the stress increase is large in an overconsolidated clay and the pre-consolidation pressure matters → the simple single-C log law may need a Cc/Cr (recompression/virgin) refinement.

> [!tip] How this sits next to the dewatering note
> Both end in the same Terzaghi compression and the same consolidation-degree machinery. They differ only in **what generates the stress increase Δσ′**: an applied surface load via the triangle method (this note) versus loss of buoyancy from drawdown (dewatering note). Pick by mechanism.

---

## 3. Inputs the notebook will need

> [!warning] Never assume a parameter — flag if missing
> Geometry: ground level (m TAW); **depth step** Δz for the calculation grid; water table level **before** and **after** loading; influence depth (below which the ground is treated as a rigid base). Per soil layer (max 4): thickness, dry unit weight γ_d, saturated unit weight γ_n, compressibility constant **C**, permeability **k**, drainage factor (single/double drainage). Load: the loaded rectangle(s) — adjacent side LARZ and opposite side LORZ relative to the point of interest — and the net pressure Δp on each, before and after. Stress-law exponent **n** (3 or 4) per layer. Elapsed **time** for the time-dependent result.

The depth grid is generated automatically from Δz; layer boundaries are snapped onto the grid. The water table should be placed on a grid depth so it coincides with a calculation point.

---

## 4. Effective stress and the "net load" convention

Settlement is driven by the **change** in effective vertical stress, so the calculation tracks effective stress with depth in two states — before and after the load.

- **Initial effective stress** σ′v0(z), cumulative from the surface: dry unit weight γ_d above the water table, submerged (γ_n − γ_w) below it.
- The applied load is entered as the **net additional** pressure: the infinite/pre-existing surcharge p₀ is removed, leaving only Δp, the new load that actually causes settlement (condition 5). The "before" and "after" surcharges (p₀ basis and Δp on the area, then pₙ basis and Δpₙ on the area) are carried separately so the stress *change* is correct even if the background surcharge changes.

The settlement at a point uses, per sub-layer, the mid-layer effective stress before (σ′o) and after (σ′n) loading.

---

## 5. Step 1 — Stress distribution with depth (the triangle method)

The vertical stress increase at depth z under the corner of a uniformly loaded rectangle (sides a and b, here LARZ and LORZ) is a closed-form **influence factor** I(z); any footprint and any point are handled by superposing such corner rectangles (Newmark's principle of superposition). The factor depends on the stress-law exponent n:

**n = 3 — Boussinesq stress law.** Use for saturated, over-consolidated soils (clay, loam) and small load increments. The influence factor for a loaded rectangle, evaluated at depth z (with sides a, b):

$$I_{3}(z)=\frac{1}{2\pi}\left[\arctan\!\frac{b}{z}-\arctan\!\frac{b\,z}{\,a\sqrt{z^{2}+a^{2}+b^{2}}\,}+\frac{a\,b\,z}{(z^{2}+a^{2})\sqrt{z^{2}+a^{2}+b^{2}}}\right]$$

*(In the source grid, z is the running depth, a = adjacent side, b = opposite side; the bracket reduces to the standard Boussinesq corner factor.)*

**n = 4 — Buisman stress law.** Use for normally consolidated soils (sandy character, soft clays) where the elastic modulus increases roughly linearly with depth:

$$I_{4}(z)=\frac{a\,z}{4\pi\,(z^{2}+a^{2})}\left[\frac{3z^{2}+2a^{2}}{z\sqrt{z^{2}+a^{2}}}\arctan\!\frac{b}{\sqrt{z^{2}+a^{2}}}+\frac{a\,b}{z^{2}+a^{2}+b^{2}}\right]$$

> [!note] Physical meaning of n
> The larger the exponent n, the more the stress stays concentrated directly beneath the load (less lateral spread). n = 3 spreads more (elastic half-space); n = 4 concentrates more (modulus growing with depth). Choosing n is a soil-behaviour decision, made per layer.

The stress increase at depth is then `Δσ(z) = Δp · I(z)` for each loaded rectangle, summed over all rectangles (and over the before/after states). The product `σ′ · I · Δz` accumulated down the column gives the stress profile the settlement step consumes.

**Output of this step — Figure A (to reproduce):** vertical profiles of σ′ before and after loading versus depth, on the generated depth grid. Look for the stress increase concentrated in the upper layers and decaying toward the influence depth.

---

## 6. Step 2 — Settlement magnitude (Terzaghi compression)

With the before/after effective stresses known at each sub-layer mid-depth, the compression of a sub-layer of thickness Δh follows the **Terzaghi logarithmic compression law** with the compressibility constant C:

$$\Delta h \;=\; \frac{\Delta h_{\text{layer}}}{C}\,\ln\!\frac{\sigma'_{n}}{\sigma'_{o}}$$

where σ′o and σ′n are the mid-layer effective stresses before and after the load. The **total final settlement** is the sum over all sub-layers down to the influence depth.

> [!note] Why logarithmic, and what C is
> Settlement depends on the *ratio* σ′n/σ′o, not the absolute difference — a given increment compresses a lightly-stressed shallow layer more than a deep, already-compressed one. C is the constrained compressibility constant of the layer (higher C = stiffer = less settlement). It plays the same role as the De Beer modulus in the dewatering note, but here it is entered directly per layer rather than derived from cone resistance.

**Output of this step — Figure B (to reproduce):** cumulative settlement versus depth, showing which layers contribute most.

---

## 7. Step 3 — Time-dependent settlement (Terzaghi 1-D consolidation)

The final settlement is not instantaneous in low-permeability soils; pore water must drain. The fraction reached at time t is the **average degree of consolidation U(Tv)**, with the dimensionless time factor

$$T_{v}=\frac{c_{v}\,t}{H_{dr}^{2}}\,,\qquad c_{v}\ \text{from } C,\,k\ \text{(and }\gamma_w);\quad H_{dr}=\text{drainage path}$$

The drainage path depends on the **drainage factor**: single drainage → H_dr = layer thickness; double drainage (permeable above and below) → H_dr = half thickness. A coefficient (here called the time-dependent settlement coefficient / mCt) sets this from the permeability contrast with the neighbouring layers.

U(Tv) uses the Terzaghi series solution (Fourier expansion); the spreadsheet truncates at seven terms, which is ample:

$$U(T_v)=1-\frac{8}{\pi^{2}}\sum_{m=0}^{6}\frac{1}{(2m+1)^{2}}\exp\!\left[-\frac{(2m+1)^{2}\pi^{2}}{4}\,T_v\right]$$

The settlement at time t for each layer is `U(Tv) · (final settlement of that layer)`, summed over layers. The drainage degree of a layer also depends on the consolidation state of the layers above and below it (sequential drainage), which is why the calculation proceeds layer by layer.

**Output of this step — Figure C (to reproduce):** settlement versus time, typically on a log-time axis, asymptotically approaching the final settlement.

---

## 8. Calculation path (summary the notebook follows)

1. **Inputs & grid** — read geometry, layers, load, n per layer, time; generate the depth grid at Δz; snap layer boundaries; place the water table on the grid.
2. **Effective stress** — build σ′v0(z) before loading (γ_d above WT, γ_n − γ_w below); subtract the pre-existing surcharge so only the net load Δp remains.
3. **Stress distribution (Step 1)** — for each depth, each loaded rectangle, compute I(z) with the n=3 or n=4 closed form; Δσ(z) = Δp·I(z); superpose rectangles; assemble σ′ before/after profiles → Figure A.
4. **Settlement magnitude (Step 2)** — per sub-layer, Δh = (Δh_layer/C)·ln(σ′n/σ′o); sum to influence depth = final settlement → Figure B.
5. **Time consolidation (Step 3)** — per layer, Tv = cv·t/H_dr² (H_dr from drainage factor); U(Tv) via the 7-term Terzaghi series; settlement(t) = ΣU·Δh_final → Figure C.
6. **Synthesis** — final settlement, settlement at time t, and (if two points are run) differential settlement, against project serviceability criteria.

---

## 9. Diagrams to reproduce (what to look for)

- **Figure A — stress with depth (before/after):** confirms the load is correctly placed and shows the depth of significant influence. The gap between the two curves is the Δσ′ driving settlement.
- **Figure B — cumulative settlement with depth:** locates the compressible layers; settlement should develop where soft layers coincide with significant Δσ′.
- **Figure C — settlement versus time:** the consolidation curve; its early slope and the time to (say) 90% settlement inform surcharge/waiting decisions. Read against the project's allowable residual settlement.

> [!important] Differential settlement governs structures
> As with dewatering, total settlement rarely damages a structure — **differential** settlement does. Run the calculation at the relevant points (e.g. two corners of a slab, or under track at two chainages) and compare the difference against the applicable distortion limit. Railway limits are tighter than building limits and speed-dependent — use the Infrabel specification, not a generic value.

---

## 10. Validation and limits

- **Validation anchor:** the source spreadsheet contained a fully solved case (non-zero settlements per layer). The future notebook must be checked against those numbers to the millimetre before use — unlike the dewatering note, a solved reference exists here.
- **γ_w convention:** confirm the value used for the submerged unit weight (9.81 vs 10 kN/m³) and keep it consistent within the note.
- **Single C (no Cc/Cr split):** the method uses one compressibility constant per layer. For strongly over-consolidated clays where the load crosses the pre-consolidation pressure, a recompression/virgin-compression refinement may be warranted.
- **Max 4 layers** in the source; group or extend if more.
- **Predesign maturity:** layer-averaged C and direct-entry parameters make this an order-of-magnitude / comparative tool, not a substitute for a detailed consolidation analysis with oedometer data.

---

## 11. Standards and basis

- **Settlement law:** Terzaghi one-dimensional compression (logarithmic, constrained compressibility constant C).
- **Stress distribution:** elastic stress distribution under a uniformly loaded rectangle — Boussinesq (n = 3) and Buisman (n = 4) formulations, superposed by Newmark's method.
- **Consolidation:** Terzaghi one-dimensional consolidation theory; average degree of consolidation U(Tv) via the Fourier series solution.
- **Framework:** Eurocode 7 (EN 1997-1) + Belgian NBN annexes for geotechnical serviceability; project distortion criteria per the applicable (e.g. Infrabel) specification.

---

## 12. Status / next step

**Methodology captured; notebook deferred until a project requires it.** When built, the notebook mirrors [[Dewatering-induced settlement — methodology]] (handcalcs, prose, inline figures, French calc-note prose, code hidden on HTML→PDF export) and is validated against the solved reference case.

Links: [[Dewatering-induced settlement — methodology]] · [[_EC7 — Index]] · [[_Methodology — Index]]
