---
title: Settlement & ground-improvement toolbox — salvage map
eurocode: EC7
domain: Geotechnical
type: memo / index
status: reference
tags: [memo, EC7/geotechnical, settlement, consolidation, ground-improvement, salvage, toolbox]
related: ["[[Dewatering-induced settlement — methodology]]", "[[Settlement under a loaded area — calculation methodology]]", "[[_EC7 — Index]]"]
created: 2026-05-31
---

# Settlement & ground-improvement toolbox — salvage map

Inventory of a legacy spreadsheet folder ("Settlements, consolidations and ground improvement"), assessed for conversion into validated handcalc notebooks. Each entry: method, whether the source contains a solved case (validation anchor), overlap with already-built notebooks, and relevance to the three recurring structure types — **culvert**, **building on radier (raft)**, **catenary foundation**.

> [!note] How to use this memo
> This is the build backlog. Notebooks are produced one at a time on request, each validated against the solved case in its source. Already built and validated: [[Settlement under a loaded area — calculation methodology]] (De Beer/Terzaghi + Newmark, load-induced) and [[Dewatering-induced settlement — methodology]] (drawdown-induced). The tools below are *distinct methods*, not duplicates of those.

## Relevance by structure type (summary)

- **Culvert** (excavation + box on soil/improved ground): CPT→C input; vertical drains / preload if soft soil; heave-reload for the excavate-then-reload net movement; rigid inclusions / ASIRI if ground is improved.
- **Building on radier / raft**: Steinbrenner (elastic raft settlement) and Schmertmann (raft on sand from CPT) are the core; rigid inclusions / stone columns / ASIRI for rafts on improved soft ground; CPT→C input.
- **Catenary foundation**: only marginally served by this folder. Catenary masts are small footings governed by **overturning / lateral load / bearing**, not area settlement. Schmertmann/Steinbrenner give vertical settlement of a small footing, but the governing checks (moment equilibrium, horizontal displacement, bearing) are **not** in these tools — flagged as a gap to cover elsewhere.

---

## Build backlog (priority order)

### Tier 1 — foundational / highest value

**1. CPT → compression constants (`samendrukkingsconstanten_uit_sonderingen_V1`)**
Derives the De Beer compression constants C from a CPT sounding. *Upstream of every settlement calc* — closes the chain raw sounding → C → settlement. Solved (real sounding, GSMR Olen). Serves: all structure types (it is the input layer).

**2. Heave / reload — Steinbrenner with reloading (`zetting_fundering_staal-Steinbrenner-herbelast`)**
Elastic settlement (Steinbrenner) with an unload-reload branch. This is the **third settlement control** (excavation heave then reload) done the proper elastic way using Eoed/Eur, *with a solved reference*. Preferred over forcing a recompression-C into the De Beer log law. Solved. Serves: **culvert** (excavate-then-reload net movement), raft on deep excavation.

### Tier 2 — consolidation acceleration (soft-soil embankments / approach fills)

**3. Vertical drains (`zettingen_-_verticale_drains`)**
Settlement + radial consolidation (Barron) with vertical drains under an embankment. Accelerated consolidation of soft soil. Solved (Ophoging KW39, real). Serves: **culvert** approach embankments on soft soil.

**4. Accelerated consolidation / preload + surcharge (`versnelde_consolidatie`)**
Preload and surcharge design — how much surcharge, how long, residual settlement after removal; equivalent cv. Solved. Serves: any soft-soil platform/embankment predesign.

### Tier 3 — ground improvement (a distinct domain; high value for soft-soil rail works)

**5. ASIRI — rigid inclusions (`ASIRI-Maaiveld_zakking_3`)**
Surface settlement and load transfer over rigid inclusions per the ASIRI guideline (the reference standard for inclusions rigides). Load-transfer platform (qtip/wtip). Solved. Serves: **culvert** / **raft** on improved soft ground.

**6. Stone columns — LCPC 2011 (`grindkernen-LCPC-2011`)**
Stone-column (grindkern) design, LCPC 2011 method, with acceptance criteria. Solved. Serves: **raft** / **culvert** on improved soft ground.

**7. Stone columns — Priebe (`grindkernen-Priebe`)**
Classic Priebe stone-column method. Solved. Serves: as above (older method; pair with LCPC).

**8. Settlement reduction by rigid inclusions (`zettingsreductie-inclusion_rigides`)**
Analytical settlement-reduction factor for rigid inclusions with load-transfer mattress. Solved. Serves: **raft** / **culvert** on inclusions.

### Tier 4 — distinct settlement methods (raft / shallow foundation)

**9. Schmertmann (`zetting_fundering_staal-Schmertmann`)**
Schmertmann strain-influence (Iz) settlement from CPT + Meyerhof bearing. Standard CPT settlement method for sands. Solved (textbook examples 13.9, 13-13 — built-in validation). Serves: **raft** / shallow footing on sand.

**10. Steinbrenner (`zetting_fundering_staal-Steinbrenner`)**
Elastic (Steinbrenner) settlement of a rectangular foundation, Eoed-based. The elastic counterpart to the De Beer method already built. Solved. Serves: **raft**.

### Tier 5 — monitoring / back-analysis (construction phase, not predesign)

**11. Asaoka (`zettingsmeting_Asoaka`)**
Asaoka graphical method — extrapolate final settlement from field monitoring readings. Observational, used during construction to confirm consolidation progress. Solved. Serves: any monitored embankment/structure.

---

## Skip (duplicates or fragments)

- **`Zetting_onder_rechtoekige_fundering.xlt`** — blank twin of the De Beer/Terzaghi tool already built ([[Settlement under a loaded area — calculation methodology]]). No new content.
- **`zettingen.xlsx`** — same De Beer method, solved; useful only as a second validation anchor for the existing load notebook, not a new build.
- **`Spanningsverdeling_puntlast.xlt`** — Boussinesq stress under point loads (n=3/4); a stress-distribution fragment, not a full settlement tool. Could fold into the load notebook as a point-load variant if ever needed.
- **`rigid_inclusions.xlsx`** — post-processing sheet for a Plaxis FE export (σ′yy values), not a self-contained analytical method.

---

## Notes

- **Most sources are solved** (real project data or textbook examples) — unlike the earlier blank templates, each carries a built-in validation anchor, making reverse-engineering faster and more reliable.
- **Two method philosophies coexist** here: the *logarithmic* De Beer/Terzaghi family (constant C) already built, and the *elastic* family (Steinbrenner/Schmertmann, Eoed/Eur). They are different constitutive laws — not interchangeable by swapping a parameter. The characteristics table (NBN EN 1997-1 ANB-2014 Tabel 2.1) carries both C (Cp′/Cs′) and the elastic set (Eoed/E50/Eur), so either family can be fed from it.
- **Catenary foundations gap:** none of these tools cover the governing catenary checks (overturning, lateral displacement, bearing under eccentric load). Note for a separate EC7 entry.

Links: [[_EC7 — Index]] · [[Settlement under a loaded area — calculation methodology]] · [[Dewatering-induced settlement — methodology]]
