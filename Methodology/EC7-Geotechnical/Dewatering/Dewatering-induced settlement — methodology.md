---
title: Dewatering-induced settlement — methodology
eurocode: EC7
domain: Geotechnical
check_type: Serviceability — settlement of third-party assets
method: De Beer / Sanglerat compressibility + Terzaghi compression; Dupuit + Sichardt drawdown
guideline: Richtlijn Bemalingen 2009
groundwater: Phreatic (single water table)
status: draft
maturity: predesign
tags: [methodology, EC7/geotechnical, dewatering, settlement, bemaling, predesign]
related: ["[[_EC7 — Index]]", "[[_Methodology — Index]]"]
script: EC7_Rabattement_Tassement (handcalc notebook)
created: 2026-05-31
---

# Dewatering-induced settlement — methodology

> [!abstract] One line
> Predicts how much the ground around a dewatered excavation settles, and how far that influence reaches, so you can judge whether **nearby existing assets** (buildings, tracks, abutments, utilities) are at risk. The settlement driver is **loss of buoyancy** when the water table is lowered — not any applied load.

---

## 1. What this calculation is — and is not

When you excavate below the water table you must pump to work dry. Pumping lowers the water table not only inside the pit but in a **cone** around it. Below the water table, soil grains are partly floated by pore-water pressure (Archimedes). Lower the water, you remove that buoyancy; the full weight of the soil now bears on the layers beneath, they compress, and the surface settles. If an existing structure sits inside the cone, it settles too — and if one side settles more than the other (**differential settlement**), it can crack.

This method therefore answers two coupled questions:
1. **How far does the pumping influence reach?** → the drawdown cone and its influence radius (hydraulics).
2. **How much does the ground settle, especially at the nearest existing asset?** → the settlement integration.

> [!warning] What it does NOT do
> - It does **not** assess settlement of the structure you are *building* (e.g. the culvert) under its own loads — that is a foundation bearing/settlement check (Winkler springs), a different calculation.
> - It does **not** take any surface load. There is **no LM71, no traffic, no fill input**, because the only mechanism modelled is water removal. Load-induced settlement is the job of the *settlement-under-load* tool (De Beer with an influence factor for rectangle/embankment/strip), not this one.
> - It does **not** cover excavation base stability, heave, or piping — separate failure modes.

See [[#7 Scope, limits and open items|§7]] for the honest limits.

---

## 2. When to use it (and when not)

> [!tip] Mental model
> This is a **"what does my hole do to the neighbours"** tool, restricted to the **water-lowering** mechanism. It is a construction-phase, third-party-impact check. The moment the question is about a *load*, or about the *structure being built*, you are in a different tool.

**Strong fit:**
- Dewatering next to an **existing building** — classic predesign risk check before committing to a dewatering scheme.
- Dewatering next to a **live railway track or platform** — same logic, but compared against railway distortion limits (much stricter than building limits). Highly relevant for Infrabel/TUC RAIL work where excavations sit beside live track.
- Dewatering next to an existing **bridge abutment, retaining wall, or buried utility**.
- **Comparing dewatering schemes** — does 1.5 m vs 3 m drawdown push the neighbour past its limit? Does a smaller pit help? Fast what-if.
- **Independently checking a contractor's dewatering note** — reproduce their influence radius and settlement claims with the same Belgian methodology. (High-value use in a design-validation role.)
- **Demonstrating that no asset is within the influence radius** — a clean "no dewatering settlement risk" on paper.

**Poor fit (use another method):**
- Settlement of the new structure under its own loads → foundation settlement / bearing capacity.
- Settlement under train (LM71), road, or fill → settlement-under-load (Boussinesq/De Beer with influence factor).
- New embankment / approach fill over soft soil → settlement-under-load + time consolidation.
- Time-dependent consolidation ("how long to wait") → not in this method (no time axis).
- Heave, base stability, piping → separate checks.

---

## 3. The role of "x" — read this before trusting any result

In this method **x is the horizontal distance from the excavation edge to a *separate, pre-existing* asset you are trying to protect** (building, track, abutment, utility). It is **not** the structure being built. The structure you are building (e.g. the culvert) sits *inside* the pit, at the bottom, at x = 0 — it is the pit's reason for existing, not a neighbour at distance x.

Two cases:
- **There is a neighbour to protect** → x = its real offset; the settlement-vs-distance curve and the differential at x are the deliverable.
- **There is nothing within the influence radius** → the method has nothing to say; the analysis is moot, and the honest conclusion is "no third-party dewatering risk." Do not dress up a moot calculation.

---

## 4. Method and formulas

### 4.1 Inputs
Geometry: pit width B, length L, depth; ground level; **piezometric water level** (single, phreatic); target dewatering level (commonly ~0.5 m below pit bottom); impermeable base level. Distance x to nearest asset. Soil layers entered **manually** (predesign): per layer a representative cone resistance q_c, unit weights γ_d / γ_n, permeability k_h, Sanglerat α. (See [[#6 Context|§6]] on parameters.)

### 4.2 Hydraulics (phreatic — Dupuit + Sichardt)
- **Drawdown** `s = z_w0 − z_bem`.
- **Influence radius (Sichardt):** `R_Sichardt = 3000 · s · √k_h` — empirical, depends on √k. The reach is governed by the permeability of the **layer being dewatered**.
- **Equivalent pit radius:** `r_eq = √(B·L/π)` (rectangular pit replaced by a circle of equal area, so radial-flow formulas apply). For a trench, a half-width form is used instead.
- **Total influence radius:** `R_tot = R_Sichardt + r_eq`.
- **Dupuit drawdown line** at distance x (with x_r = x + r_eq), for x_r ≤ R_tot:
  `s_x = H − √( H² − (H² − h0²)·(R_tot − x_r)/(R_tot − r_eq) )`
  giving the local drawdown that feeds the settlement at each distance.

### 4.3 Settlement (De Beer / Sanglerat + Terzaghi)
Soil sliced in Δh = 0.20 m sub-layers. Per sub-layer, at mid-depth:
- **Initial effective stress** σ′v0, cumulative — γ_d above the water table, submerged (γ_n − γ_w) below.
- **Constrained modulus (De Beer / Sanglerat):** `C = β·α·q_c / σ′v0` (with β = 1 for quaternary "C" soils; β only applies to tertiary "A" soils).
- **Effective-stress increase from drawdown:** removing buoyancy over the lowered band raises σ′ by `(γ_d − (γ_n − γ_w))` per metre of the band; this increment **persists with depth** below the band.
- **Sub-layer settlement:** `z_i = (Δh / C)·ln((σ′v0 + Δσ′)/σ′v0)·1000` [mm].
- **Cut-off:** sub-layer ignored when `Δσ′/σ′v0 < 0.10` (added stress negligible vs in-situ; avoids integrating a meaningless tail).

The total settlement is the sum over all sub-layers, evaluated at the asset location using the **local** drawdown there.

> [!note] Why the law is logarithmic
> Settlement depends on the *ratio* of final to initial stress, not the absolute difference. A given stress increase produces more settlement in a lightly-loaded shallow layer (low σ′v0) than in a deep, already heavily-compressed one.

---

## 5. The diagrams — what to look for

Four figures reproduce the reference tool's charts. Generic reading guidance:

**Figure 1 — drawdown cone (vertical section).** Three water lines: initial table (horizontal), the lowered table (the cone), and the target level in the pit. Look for: (a) **where the cone rejoins the initial table** = influence radius, telling you if the asset is inside the affected zone; (b) **the slope of the cone under the asset** — a steep cone means large differential across the asset's width (tilt); a flat cone settles it more uniformly; (c) the **drawdown depth at the asset**, which feeds the settlement.

**Figure 2 — depth profiles (σ′v0, C, cumulative settlement).** Depth runs downward (CPT convention). Look for: (a) the **kink in σ′v0 at the water table** — confirms the table is correctly placed; (b) the **stiffness profile C on a log scale** — each layer a distinct band; soft layers (low C) are where settlement can develop; this is the most diagnostic plot; (c) **where the cumulative-settlement line steps** — that locates which layers actually generate the settlement. Settlement appearing in a layer you think is stiff signals an error to check.

**Figures 3 & 4 — settlement and differential vs distance.** Fig 3 has the settlement axis inverted (curve "sags" like the ground). Fig 4 is the **slope** of Fig 3, in mm/m. Look for: in Fig 3, max settlement at the wall, decaying to zero at the influence radius, with the asset's value marked. In Fig 4, read the differential **at the asset** and compare to the distortion criterion.

> [!important] Differential is what damages structures
> Total settlement rarely cracks a building — **differential** settlement does. Typical angular-distortion limits: **~1/500 (≈ 2 mm/m)** serviceability for ordinary buildings, **~1/300** before visible cracking, stricter for sensitive structures. **Railway track limits are much tighter** and speed-dependent — check the applicable Infrabel specification, do not reuse the building value. The differential is always worst near the wall (steepest cone); watch the transition at the edge of the influence zone, where settled meets unsettled ground.

---

## 6. Context — soil type and permeability (why results swing)

The parameters act on **two different axes**, and confusing them is a common error:

- **Permeability k_h governs the *reach* of the cone, not its depth.** Because `R = 3000·s·√k`, a clean sand (k ≈ 10⁻³–10⁻⁴ m/s) gives an influence radius of hundreds of metres; a silty/fine soil (k ≈ 10⁻⁶) gives only metres, for the *same* drawdown. The reach can therefore change by two orders of magnitude purely from the soil type of the dewatered layer.
- **Unit weights (γ) and stiffness (q_c, α) govern the *magnitude* of settlement, not its reach.** Settlement is proportional to the buoyancy term `γ_d − (γ_n − γ_w)` and inversely proportional to the modulus C.

> [!caution] Sensitivity to *which* layer is dewatered
> The result is extremely sensitive to where the water table sits relative to a permeable layer. If a high-k layer (e.g. gravel) lies within the drawn-down band, R explodes. Always confirm which layer actually transmits the drawdown.

> [!caution] Method validity at low permeability
> Dupuit/Sichardt assume clean radial groundwater flow in a permeable aquifer (k ≳ 10⁻⁴). In a tight soil (k ≈ 10⁻⁶) you do not get classical well flow; the formulas still compute a number, but its reliability drops, and the predicted (small) influence radius may understate reality. Flag this when the dewatered layer is fine-grained.

---

## 7. Scope, limits and open items

- **Phreatic groundwater only.** Confined/artesian (Tessendorf) is deliberately excluded — the standard project case is a single piezometric level.
- **Predesign maturity.** Manual layer-averaging smooths out thin stiff/soft bands that a full CPT profile would capture. Adequate for order-of-magnitude and go/no-go; not a substitute for a detailed rabattement study.
- **Validation status.** The engine reproduces the reference tool's formulas cell-for-cell. Intermediate quantities (σ′v0, C, R, the Dupuit line) are hand-checkable and verified. The one piece **faithful-to-formula but not yet validated against a solved reference** is the Δσ′ propagation below the drawdown band — the source workbook was a blank template with no solved numbers. **Action:** run one real solved case through the original Excel and diff the totals to lock this down.
- **γ_w convention:** this method uses γ_w = 10 kN/m³ for the buoyancy term, matching the source workbook (the companion settlement tool used 9.81 — do not mix them).
- **Not covered, get elsewhere:** base stability/heave/piping; time-rate of consolidation; settlement under applied loads; the structure's own foundation settlement.

---

## 8. FAQ

**Is it safe to use for tracks?** Yes — to assess **dewatering impact on a nearby track** (track = neighbour at distance x), read against railway distortion limits. No — it does **not** assess train-load (LM71) settlement; that is load-induced, a different method.

**Where is the load input?** There isn't one, by design. The only mechanism is buoyancy loss from water removal. See §1.

**Pit or trench?** Both supported; only the equivalent-radius term differs (circle-of-equal-area for a pit, half-width for a trench).

**What if nothing is nearby?** Then there is no asset to settle and the analysis is moot — state that rather than report a meaningless curve. See §3.

**Why does my influence radius seem tiny?** Almost certainly a low-permeability dewatered layer (√k term). Check §6 — and whether Dupuit is even valid for that soil.

**Can I get the total settlement of my culvert from this?** No. This is third-party dewatering impact. Culvert settlement under its own loads is a foundation check (Winkler springs).

---

## 9. Links

- Script / deliverable: `EC7_Rabattement_Tassement` (handcalc `.ipynb`, exports to no-code HTML → PDF).
- Index: [[_EC7 — Index]] · [[_Methodology — Index]]
- Future (to be added): contractor execution rules for dewatering (what to do / what not to do), and full concept-note / predesign approach articles.
