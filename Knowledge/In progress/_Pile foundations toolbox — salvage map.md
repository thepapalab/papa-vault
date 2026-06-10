---
title: Pile foundations toolbox — salvage map
eurocode: EC7
domain: Geotechnical
type: memo / index
status: reference
context: catenary pile foundations (upcoming), also bridges/culverts
tags: [memo, EC7/geotechnical, piles, pieux, bearing-capacity, micropile, lateral-load, salvage, toolbox]
related: ["[[_EC7 — Index]]", "[[_Settlement & ground-improvement toolbox — salvage map]]"]
created: 2026-05-31
---

# Pile foundations toolbox — salvage map

Inventory of a legacy pile-design spreadsheet folder, assessed for conversion into validated handcalc notebooks. Immediate driver: **catenary mast pile foundations** (upcoming). Each entry: method, solved-case status (validation anchor), and relevance. More files expected — this memo will grow.

> [!important] Catenary demand profile shapes the priority
> A catenary mast foundation carries **low vertical load but high moment + horizontal load** (wire tension + wind on the mast). The governing checks are therefore **lateral resistance and overturning**, with axial bearing usually secondary. This reorders the usual pile priority: lateral/structural checks come first, bearing second.

> [!warning] Possible gap — short-pile overturning (Broms)
> Catenary foundations are often **moment/rotation-governed**. A lateral *soil-resistance* check (Brinch Hansen) plus a *section shear* check (dwarskracht) may not fully capture the **overturning/rotation of a short rigid pile under moment**, which classically needs a **Broms-type short-pile analysis**. No Broms/short-pile tool is present in this folder. **To confirm:** whether catenary design relies on Broms (or equivalent) and whether that tool exists elsewhere. Flagged pending clarification.

---

## Build backlog by function

### Tier 1 — governing for catenary (build first)

**Brinch Hansen — lateral soil resistance (`Brinch-Hansen`)**
Increase of soil resistance with depth for a laterally loaded pile (K0q, K0c factors; c′, φ′, D, B inputs). The lateral pile-soil resistance check — governing for catenary. Solved. *(legacy .xls → convert)*

**Lateral / shear capacity of pile section (`dwarskracht_palen`)**
Structural shear/lateral resistance of the pile cross-section per EC2 (fc,k, γc, CRd,c, section geometry). Pairs with Brinch Hansen: soil side + structural side of the lateral check. Solved.

**De Beer 2016 — axial bearing from CPT (`2016_De_Beer_-_Richtlijnen_paalberekening_2016`)**
The current Belgian directive for ultimate axial bearing (grensdraagvermogen) from CPT: base + shaft, pile coefficients, per pile type. *The* primary Belgian pile-bearing method. Solved (KO-10, real project). Needed even when not governing.

### Tier 2 — axial bearing by pile type (build the one matching the chosen pile)

> Pile type not yet decided — all options retained.

**Driven precast piles (`draagvermogen_DTU-heipalen`)** — battu préfabriqué béton, base + shaft from CPT (DTU/French method). Solved.

**Bored piles from pressuremeter (`draagvermogen_DTU-boorpalen-pressiometer`)** — foré tubé, from pressuremeter limit pressure pl. Solved.

**Bored + shaft-grouted piles (`draagvermogen_DTU-boorpalen_schachtinjectie`)** — bored with shaft injection. Solved.

**Micropiles — NAD, latest (`Bearing_capacity_micropile_NAD-rapport_20`)** — Belgian NAD micropile bearing, multi-sounding (S01/S02/S03) + EC7 partial factors. The most complete micropile file; prefer over the older revs. Solved.

**Micropiles — NF P94-282 (`draagvermogen_micropaal-NF-P94-282`)** — French code micropile route. Solved.

**Sheet piles / I-H / box sections (`draagvermogen_DTU_damwand-I-H-koker`)** — bearing of steel sheet-pile / H / box sections. Solved. Low catenary relevance; relevant for retaining/abutment works.

### Tier 3 — load combinations & safety

**Fascicule 62 partial factors (`fascicule_62-partiële_veiligheden`)** — converts ultimate (Ql breuk) and creep (Qc kruip) to ELU/ELS design loads; includes **rail and wind load categories** (hoofdbelasting trein/verkeer, nevenbelasting wind/sneeuw). Supporting tool for any pile calc note. Solved.

### Tier 4 — load-test interpretation (verification phase)

**Chin (`Chin`)** — extrapolate ultimate load from a static load test (s/Q linear fit). Construction/verification. Solved.

### Tier 5 — driveability / hammer prediction (construction phase, not design)

- **`heivoorspelling`** — drive prediction, vibratory hammers (MRZV). Solved.
- **`heivoorspelling-dieselen`** — drive prediction, diesel hammers. Solved.
- **`drukspanning_heien`** — driving stress / impact velocity. Solved.
- **`controle_vooruitgangssnelheid_palen`** — penetration-rate control during driving. Template. *(legacy .xlt → convert)*

---

## Skip / supersede

- **`2008_De_Beer_-richtlijnen_paalberekening_2008`** — superseded by the 2016 directive. Keep only for legacy-project back-checks.
- **`draagvermogen_micropaal-NAD`, `-NAD-rev1`, `draagvermogen-micropaal`** — earlier revisions/variants of the NAD micropile tool; keep only `-NAD-rapport_20` (most complete) and `NF-P94-282`.

---

## Suggested catenary calc-note set (when building)

A complete catenary pile verification would compose:
1. **Axial bearing** — De Beer 2016 (or the pile-type-specific tool) → ultimate + design axial resistance.
2. **Lateral soil resistance** — Brinch Hansen → lateral capacity from soil.
3. **Structural section** — dwarskracht_palen → shear/lateral capacity of the pile.
4. **Overturning/rotation** — Broms short-pile check → **gap, to confirm** (see warning above).
5. **Load combinations** — Fascicule 62 → ELU/ELS with rail + wind.

Items 1–3 and 5 are covered by this folder; item 4 is the open question.

---

## Notes

- **Mostly solved files** — real project data or worked examples throughout, so each carries a validation anchor; reverse-engineering will be faster and verifiable, as with the settlement set.
- **Two code frameworks coexist:** the **Belgian De Beer / NAD** route and the **French DTU / NF P94 / Fascicule 62** route. Confirm which applies per project (Infrabel context → Belgian De Beer + NAD likely primary; French methods for micropiles or where specified).
- This memo complements [[_Settlement & ground-improvement toolbox — salvage map]] — together they cover the geotechnical design families: settlement, consolidation, ground improvement, and (here) pile capacity.

Links: [[_EC7 — Index]] · [[_Settlement & ground-improvement toolbox — salvage map]]


---

# Addendum — Batch 2 (2026-05-31)

Second tranche of pile files. This batch is heavy on the **lateral / moment** side and **largely closes the Broms gap** flagged above. 13 more files still expected — memo continues to grow.

> [!success] Update to the Broms gap
> The lateral/moment family is now well covered. Several tools address the laterally-loaded and moment-loaded pile directly — see Tier 1-bis below. The remaining question is only *which* lateral method to standardise on (subgrade-reaction kh / p-y, passive-wedge Vandepitte, or moment methods Tschebotarioff), not whether a tool exists.

## Tier 1-bis — lateral & moment behaviour (catenary-governing) — NEW

**Subgrade reaction kh vs depth (`kh-paal_ifv_diepte`)**
Horizontal modulus of subgrade reaction kh as a function of depth, split sand/clay (khc, Dc). This is the **p-y / elastic-foundation input** for a laterally loaded pile. Feeds the moment/deflection analysis. Solved.

**Pile moment & deflection (`Paalmoment`)**
Laterally loaded pile: moment, shear, deflection along the pile from horizontal load V, using pile EI and (with kh above) the elastic-foundation solution. **Directly the catenary lateral-deflection/moment check.** Solved (V, l, φ, I, E inputs).

**Clamped pile — passive resistance, Vandepitte (`ingeklemde_paal-Vandepitte`)**
Laterally loaded pile via passive earth resistance (λa/δa, γ′, embedment d, width b, φ). A **short-pile / passive-wedge approach** — the practical equivalent of a Broms-type ultimate-lateral check. Solved.

**Clamped pile with horizontal load — active/passive (`ingeklemde_paal_met_horizontale_last`)**
Active and passive earth-pressure coefficients for a pile under horizontal load (φ, δ, wall/ground inclination). Companion to Vandepitte for the soil-pressure side. Solved. *(legacy .xlt → converted)*

**Tschebotarioff pile moments (`Methode_Tschebotarioff-paalmomenten`)**
Maximum bending moments induced in piles by **lateral soil movement** (e.g. embankment surcharge beside piles) — Tschebotarioff method per Philipponnat. Relevant where a catenary/abutment pile sits near a fill. Solved (Mmax field/support formulas). *(legacy .xlt → converted)*

> [!note] How the lateral tools fit together
> For a catenary pile under horizontal load + moment, the natural composition is: **kh-paal** (soil stiffness input) → **Paalmoment** (deflection + moment of the pile) for serviceability/structural, with **Vandepitte** / **ingeklemde_paal-horizontale_last** giving the **ultimate passive-resistance** (Broms-equivalent) check. **Tschebotarioff** is a separate case (moments from lateral soil movement, not from applied head load). Decide which is the primary lateral check when building.

## Tier 1-ter — axial bearing, EC7 route — NEW

**Pile bearing EC7 (`paaldraagvermogen_EC7-rev1`)** — ultimate + design axial bearing to **Eurocode 7** (γRD, ξ3/ξ4 correlation factors, γb/s, Rc,d, Fc,d), multi-sounding (S1–S4). This is the **EC7-format** bearing calc (vs the De Beer-directive format). Solved. **Strong candidate** — likely the cleanest base for an EC7-compliant pile-bearing note. Prefer the latest rev.
- Variants/revs to consolidate: `paaldraagvermogen_EC7`, `paaldraagvermogen_EC7-rev1__2_` (data 26.1/26.2). Keep the most complete rev; others are back-checks.

**De Beer method (full) (`methode_De_Beer.xltm`)** — the complete De Beer pile-bearing workbook with multiple soundings (SP01–SP04), project input, pile coefficients, dg-graph. Fuller sibling of the 2016 directive file. Solved (multi-sounding). The `.xlsm` / `_26_2` files are reduced/working copies.

## Tier 2-bis — settlement & group effects — NEW

**Pile-head settlement, De Cock (`Paalkopzakking_methode_DeCock`)**
Settlement of the pile head (base Rbu + shaft Rsu load-transfer, segment by segment). The **pile-settlement (serviceability) check** — complements bearing capacity. Solved. Relevant for any pile note needing a settlement (ELS) verification.

**Pile group reactions 3×3 (`paalreacties-3x3_groep`)**
Group response: axial response + **Flemming/Poulos** elastic group method (shear modulus G profile). For a **pile group under load** (e.g. a catenary foundation on a small group, or a bridge pier). Solved. Relevant if catenary uses a group rather than a single pile.

## Tier 3-bis — structural / load capacity — NEW

**Critical load / pile stresses (`Paalbelastingen_-kritieke_last-rev1`)** — ELS/ELU stress limits per pile diameter (concrete max 5 MPa ELS, grout 2 MPa ELS), tabulated allowable loads for φ400–900. Quick **structural capacity reference** by diameter. Solved. *(legacy .xls → converted)*

## Tier 4-bis — downdrag & load-test — NEW

**Negative skin friction, Zeevaert / De Beer (`negatieve_kleef`)** — downdrag (negatieve kleef) on a pile from settling fill, Zeevaert-De Beer slip method. Solved. **Important for culvert/bridge approach piles** through fill over soft soil — adds downdrag load.

**Negative skin friction, Philipponnat (`negatieve_kleef_palen`)** — downdrag via Philipponnat, with real project context (proj. 109308, sounding S92, E19 underpass). Solved. *(legacy .xlt → converted)* Sibling method to the above.

**Pile load tests — Chin + Van der Veen (`Paalproeven_Chin_-_Van_Der_Veen_Eurostation`)** — load-test interpretation by **two** methods (Chin and Van der Veen), Eurostation project. Fuller than the standalone `Chin` file. Solved. *(legacy .xlt → converted)*

## Tier 5-bis — driveability (vibratory) — NEW

- **`Hypervib-I` / `Hypervib-I_2012_10_09` / `Hypervib-II_Z-AZ18-24VM`** — vibratory drive prediction (Hypervib method; sheet-pile/profile driving with vibrator mass, frequency, eccentric moment). Construction-phase. Solved. Consolidate to the latest (Hypervib-II) + keep Hypervib-I as reference.

---

## Revised catenary calc-note set (after batch 2)

1. **Axial bearing** — `paaldraagvermogen_EC7-rev1` (EC7 route) or `methode_De_Beer.xltm` (Belgian directive).
2. **Axial settlement (ELS)** — `Paalkopzakking_methode_DeCock`.
3. **Lateral — ultimate** — `ingeklemde_paal-Vandepitte` (passive resistance, Broms-equivalent).
4. **Lateral — deflection/moment (ELS + structural)** — `kh-paal_ifv_diepte` → `Paalmoment`.
5. **Structural section** — `dwarskracht_palen` (shear) + `Paalbelastingen_-kritieke_last` (axial stress).
6. **Load combinations** — `fascicule_62` (rail + wind).
7. **If group foundation** — `paalreacties-3x3_groep`.
8. **If through fill** — `negatieve_kleef` (downdrag).

The earlier Broms gap is now covered by items 3–4. Open decision: standardise the lateral method (passive-wedge vs subgrade-reaction p-y).

> [!note] Consolidation needed
> Several methods now have multiple files/revs (EC7 bearing ×3, De Beer ×3, micropile NAD ×4, negative friction ×2, load-test ×2, Hypervib ×3). When building, pick the most complete/solved rev per method; the rest are back-checks. Two code routes still coexist (Belgian De Beer/NAD vs French DTU/NF-P94/Fascicule 62 + Philipponnat) — confirm per project.


---

# Addendum — Batch 3 (2026-05-31) + master organizing table

Final tranche (12 files). With this, the pile collection is **complete for Belgian practice** — no remaining method gaps. Below: batch-3 entries, then a **master table** organizing the whole collection by design check (exhaustive — all distinct methods retained as separate future notebooks; revisions consolidated).

## Batch 3 — new entries

### Pile groups & caps
**Sokkel op 3 micropalen (`sokkel_op_3_palen-V1`)** — stress distribution in a **3-micropile cap (sokkel)** under load + moment. *Directly a catenary/mast footing on a small pile group.* Solved. **High catenary relevance.**

**Pile group reactions, 8-pile (`paalreacties-8_groep`)** — group axial response + Flemming-Poulos, 8-pile configuration. Solved. Companion to the earlier 3×3.

**Pile group, general (`palengroep`)** — group settlement (S vs 3B rule) + Fascicule 62 group check, variable rows/spacing. Solved.

**Shear distribution in a pile group (`verdeling_dwarskracht_palengroep`)** — distribution of horizontal load (dwarskracht) and moments across piles in a group, **DIN 1054 Annex E** + Flemming. Solved. *Relevant for catenary/mast group under horizontal load.*

### Pile settlement (more methods — exhaustive set retained)
**Thomlinson (`paalzakking_Thomlinson`)** — pile settlement, Flemming-K formulation, worked examples. Solved.
**Flemming (`paalzakking_Flemming`)** — pile settlement, Flemming method, with real project (viaduct KW03 pijlers) + examples. Solved. *(test variant `paalzakking_Flemming-test` = back-check.)*
**NEN (`Paalzakking_volgens_NEN-v1`)** — pile settlement to **NEN** (Dutch code), iterative point/shaft interpolation. Solved (template, Maekelberg).

### Axial bearing (more routes)
**Totaal DV Paal (`Totaal_DV_Paal`)** — total bearing from **experience + CPT**, with separate Qpu (base), Qsu (shaft) from skin-friction measurement and from experience, clay approximation. Solved (proj. 7305, real). A fuller "ervaring"-based bearing route.
**TA62 pressuremeter (`paal-TA62`)** — bearing from pressuremeter (pl, qs), point-fit. Solved. Pressuremeter route, companion to DTU-pressiometer.

### Special loads
**Uplift / tension piles (`zwelbelasting_voor_trekpalen`)** — **swell load on tension piles**, CUR 77. Solved. *The tension/uplift case — relevant where catenary or buoyant structures put piles in tension.*

### Shallow foundation
**Punching — footing on layered soil (`pons_draagvermogen_fundering_op_staal`)** — bearing/**punching** of a shallow footing, dense sand over loose, drained + undrained. Solved. Shallow-foundation check (not a pile method) — belongs with the Brinch Hansen / Meyerhof family in the settlement folder.

---

## MASTER TABLE — pile & foundation design checks (exhaustive)

All distinct methods kept as separate future notebooks. **Primary = build first** (Belgian where both frameworks exist); **Alternate = build if project requires**; revisions consolidated to the most complete solved file. Validation anchor = solved case present unless noted.

### A. Pile axial bearing capacity
- **Primary (Belgian):** De Beer 2016 directive (`2016_De_Beer...`) and the full multi-sounding `methode_De_Beer.xltm`.
- **Primary (Belgian, EC7 format):** `paaldraagvermogen_EC7-rev1` — for EC7-compliant deliverables.
- **Belgian, experience+CPT:** `Totaal_DV_Paal`.
- **Alternate (French DTU) by pile type:** driven `DTU-heipalen`; bored `DTU-boorpalen-pressiometer`; shaft-grouted `DTU-boorpalen_schachtinjectie`; sheet/H/box `DTU_damwand-I-H-koker`.
- **Pressuremeter:** `paal-TA62`.
- **Superseded:** De Beer 2008.

### B. Micropile bearing
- **Primary (Belgian NAD):** `Bearing_capacity_micropile_NAD-rapport_20` (most complete).
- **Alternate (French):** `draagvermogen_micropaal-NF-P94-282`.
- **Older revs (back-check):** `-NAD`, `-NAD-rev1`, `draagvermogen-micropaal`.

### C. Pile settlement (ELS)
- **Primary (Belgian):** De Cock (`Paalkopzakking_methode_DeCock`).
- **Alternates:** Flemming (`paalzakking_Flemming`), Thomlinson (`paalzakking_Thomlinson`), NEN (`Paalzakking_volgens_NEN-v1`).
- (All four are distinct methods — keep as separate notebooks per the exhaustive choice.)

### D. Lateral resistance & moment (catenary-governing)
- **Ultimate lateral (passive):** Vandepitte (`ingeklemde_paal-Vandepitte`); earth-pressure companion `ingeklemde_paal_met_horizontale_last`.
- **Deflection/moment (subgrade reaction):** `kh-paal_ifv_diepte` (kh input) → `Paalmoment`.
- **Moment from lateral soil movement:** Tschebotarioff (`Methode_Tschebotarioff-paalmomenten`).
- **Structural section (shear):** `dwarskracht_palen`; axial-stress limits `Paalbelastingen_-kritieke_last`.

### E. Pile groups
- **Cap on few piles (catenary/mast):** `sokkel_op_3_palen-V1` (3-pile cap, load+moment).
- **Group axial response:** `paalreacties-3x3_groep`, `paalreacties-8_groep` (Flemming-Poulos).
- **Group settlement + Fascicule 62:** `palengroep`.
- **Horizontal-load distribution in group:** `verdeling_dwarskracht_palengroep` (DIN 1054).

### F. Special loads
- **Negative skin friction (downdrag):** Zeevaert-De Beer (`negatieve_kleef`) [primary], Philipponnat (`negatieve_kleef_palen`) [alternate].
- **Uplift / tension piles:** `zwelbelasting_voor_trekpalen` (CUR 77).
- **Critical/buckling load:** `Paalbelastingen_-kritieke_last`.

### G. Load combinations & safety
- **Fascicule 62 partial factors** (`fascicule_62-partiële_veiligheden`) — ELU/ELS, rail + wind.

### H. Pile load-test interpretation (verification)
- **Chin + Van der Veen** (`Paalproeven_Chin_-_Van_Der_Veen_Eurostation`) [fuller]; standalone `Chin` [back-check].

### I. Driveability (construction)
- **Vibratory:** Hypervib-II (`Hypervib-II_Z-AZ18-24VM`) [latest]; Hypervib-I [reference].
- **Diesel/impact:** `heivoorspelling-dieselen`, `drukspanning_heien`, `heivoorspelling`.
- **Penetration-rate control:** `controle_vooruitgangssnelheid_palen`.

### J. Shallow foundations (cross-ref — belongs with settlement folder)
- **Punching, layered soil:** `pons_draagvermogen_fundering_op_staal`.
- See [[_Settlement & ground-improvement toolbox — salvage map]] for Brinch Hansen, Meyerhof, Schmertmann, Steinbrenner.

---

## Overall status (after 3 batches)

- **Coverage: complete for Belgian practice.** Checks A–J cover all foundation cases — single piles, groups, caps, lateral/moment, settlement, downdrag, uplift, punching, load tests, driveability. No remaining method gap; the earlier Broms gap is closed (group D).
- **Redundancy is the only issue, and it is now catalogued:** revisions consolidated (keep most-complete solved rev), multiple methods per check retained deliberately (exhaustive choice).
- **Framework rule:** Belgian (De Beer / NAD) is primary; French (DTU / NF-P94 / Fascicule 62 / Philipponnat) is alternate, used for micropiles or where a project specifies.
- **Build approach:** notebooks produced on demand from the table, each validated against its solved case. Most files are solved → fast, verifiable builds.
- **Catenary-specific path:** B or A (bearing) + C (settlement) + D (lateral, the governing set) + E `sokkel_op_3_palen` (if 3-pile cap) + F uplift (if tension) + G (combinations). All present.

Links: [[_EC7 — Index]] · [[_Settlement & ground-improvement toolbox — salvage map]]


---

# Addendum — Batch 4: Direct (shallow) foundations + the dedicated catenary tool (2026-05-31)

This batch is pivotal for the catenary work. It contains the **purpose-built catenary-mast foundation tool** with its official description document, plus the general shallow-foundation (fundering op staal) suite. **The catenary tool changes the build priority entirely** — see below.

## ★★★ THE catenary foundation tool — USE THIS

**`Bovenleidingspaal_-_V1-2.xltm`** + description doc `beschrijving_berekeningsfile_bovenleidingspalen_9B(x).docx`

This is the **dedicated TUC RAIL calculation file for overhead-line (catenary) mast foundations** — the official intended replacement for the obsolete CONSTRUCT application, EC7-compliant, destined for consolidation into the ISAAC program. It is built for *exactly* your upcoming project. Solved (real cases: Noendelle, proj. 8505).

**What it does (from the description doc):**
- Handles all catenary foundation types: **prismatic** (type C, CR, D — rectangular section) and **tubular pile** (type R, PB — circular section), in flat terrain or near an embankment crest (talud).
- Standard massive dimensions built in (`Lijst met massieven`: C0–C…, types listed) — copy-paste a standard foundation into the input.
- Three stability controls, the catenary-governing set:
  1. **Bearing (evenwichtsdraagvermogen)** — qult via De Beer / Vesić / Meyerhof; EC7 Annex D shallow formula when D<B; depth factors (Meyerhof B<D<2B, Brinch Hansen D<5B) for the intermediate regime; deep when D>5B. **Talud reduction** (Brinch Hansen) when an embankment is near.
  2. **Sliding (glijden)** — passive horizontal resistance + base friction vs active earth pressure + mast horizontal force.
  3. **Overturning (kantelen)** — resisting vs driving moments about the toe.
- **Elastoplastic soil-reaction model** with a *schelfactor* (spreading factor): passive side spreads to 3× foundation width, active side reduced to 1/3. Passive resistance is **progressively mobilised** until all SLS controls reach safety ≥ 1; that mobilisation level gives an **estimate of foundation-top displacement** per EC7 Annex B — directly relevant to catenary functionality (tilt limit).
- **8 load cases** (parallel + perpendicular sets), fixed/mobile load split for DA1.1 / DA1.2 / classical method. Vertical load on the mast axis + foundation self-weight (22 kN/m³ plain / 25 kN/m³ reinforced); horizontal force at the base plate.
- 6 soil types (T-CNT geologists assign them).

> [!important] This resolves the earlier "catenary gap" completely
> Earlier batches flagged uncertainty about short-pile overturning (Broms). **This tool answers the catenary foundation question directly and officially** — it is the in-house method, EC7-based, with bearing + sliding + overturning + displacement estimate, for both prismatic and tubular foundations. For the catenary project, **this is the primary deliverable to reproduce as a calc note.** The generic pile tools (batches 1–3) become supporting/alternate, used only if the foundation is a slender pile rather than a prismatic/tubular massive.

> [!note] Build note — the doc flags unfinished parts
> The description states the **SLS vs ULS (gebruik/breuk) write-up still needs completion** and the breuk (failure) state is an artificial progressive-mobilisation construct. When reproducing, validate against the solved Noendelle/8505 cases and treat the ULS mobilisation logic carefully — it is the subtle part. Bearing formulas (De Beer/Vesić/Meyerhof + talud reduction) and the equilibrium equations are fully described.

## General shallow-foundation suite (fundering op staal) — supporting

These are generic direct-foundation tools — for footings/rafts generally (radier buildings, abutments), and the bearing engines behind the catenary tool.

**`fundering_op_staal-E25007`** (.xlsx solved / .xltx template) — **most complete generic shallow-foundation tool.** Rectangular (drained + undrained), circular, punching (pons), squeezing, multiple layers; computes qmax/qmin under the footing, bearing. Solved (V=790 kN case). **Primary generic shallow-foundation method** → serves radier/raft buildings and footings.

**`Fundering_op_staal_7`** (.xltx) — bearing via De Beer / Brinch Hansen / Meyerhof / **Vesić**, stress distribution under footing, shallow vs deep. Template (proj. 8505 context). The four-method bearing comparison; sibling engine to the catenary tool's bearing sheet.

**`fundering_op_staal_Hansen-Bowles`** (.xltx) — bearing per **Hansen + Bowles** (full Nc/Nq/Nγ tables, shape/depth/inclination/talud factors), drained, from CPT. Template. Classic textbook bearing route.

**`Fondations_directes`** (.xlsx) — **EC7 bearing capacity, French**, full design approaches **DA1-1 / DA1-2 / DA2** + slope (pente/talus) case + resultant position. Solved. The clean EC7-DA structured bearing note (French route).

**`PrismaticFoundation_V00`** (2020-10-13 and Copy_2021-07-29) — **OCL (overhead contact line) prismatic foundation, EN1997-1 DA1 + DA2**, French ("Charges GC", "Capacité portante standard / ancrage"). Solved. This is an **alternate/earlier catenary-foundation tool** (OCL = overhead line) in the French EC7-DA format — predecessor or parallel to the Bovenleidingspaal tool. Keep `2021-07-29` (latest); `2020-10-13` and the Copy are revs.

---

## Updated master picture — direct foundations added

Add to the master table:

### K. Direct (shallow) foundation bearing & stability
- **Catenary mast foundation (PRIMARY for catenary):** `Bovenleidingspaal_-_V1-2` — bearing + sliding + overturning + displacement, prismatic & tubular, talud. The dedicated EC7 tool.
- **Alternate catenary (French OCL):** `PrismaticFoundation_V00` (2021-07-29) — EN1997-1 DA1/DA2.
- **Generic shallow foundation (PRIMARY for radier/footings):** `fundering_op_staal-E25007` — rect/circ/punching/multi-layer.
- **Bearing-method engines (alternates):** `Fundering_op_staal_7` (De Beer/Vesić/Meyerhof/Brinch Hansen), `fundering_op_staal_Hansen-Bowles` (Hansen+Bowles).
- **EC7-DA structured (French):** `Fondations_directes` (DA1-1/DA1-2/DA2 + slope).
- Cross-ref punching also in `fundering_op_staal-E25007` (pons sheet) and the settlement folder's `pons_draagvermogen_fundering_op_staal`.

---

## ⭐ Files we WILL use (flagged per request)

**For the catenary project (primary path):**
1. **`Bovenleidingspaal_-_V1-2.xltm`** — THE catenary foundation calc note. Primary deliverable. Covers bearing + sliding + overturning + tilt for prismatic & tubular massives.
2. Supporting, only if a slender *pile* foundation is chosen instead of a massive: the pile set — bearing (`paaldraagvermogen_EC7-rev1` / De Beer / NAD micropile), lateral (`Vandepitte` + `kh-paal` → `Paalmoment`), `sokkel_op_3_palen` (3-pile cap).
3. **`fascicule_62`** — load combinations (rail + wind), already flagged.

**For general structures (radier buildings, abutments, footings):**
4. **`fundering_op_staal-E25007`** — primary generic shallow-foundation tool.

Everything else in batch 4 = alternates / bearing-engine references / revisions.

> [!note] Important consequence
> For the **catenary** specifically, the build is now simpler and more focused than the multi-step pile composition sketched in earlier addenda: **reproduce `Bovenleidingspaal` as the calc note**, validated against its solved cases, since it already integrates bearing + sliding + overturning + displacement for the actual foundation types used. The pile toolbox remains the fallback for pile-type catenary foundations and for all other (bridge/culvert) pile work.

Links: [[_EC7 — Index]] · [[_Settlement & ground-improvement toolbox — salvage map]]


---

# Addendum — Batch 5: General shallow-foundation tool with rigorous slope (talud) influence (2026-06-01)

**`Algemene_berekeningsfile_voor_funderingen_op_staal_met_invloed_van_talud_3.xlsx`**

A general shallow-foundation bearing/stability tool with a **rigorous, geometry-based slope-reduction method** — more advanced than the other `fundering_op_staal` files, and the standalone talud-reduction engine in the same family as the catenary tool. **Solved** (real project: 101303 — Overdekte sleuf Watermael-Bosvoorde, "valse put middenkolom" — a **covered-trench / culvert central-column foundation**). Project type matters: a **culvert** foundation, so this tool is relevant to culvert and catenary work, and to footings near railway embankments generally.

## What it does

Bearing capacity + sliding + overturning of a shallow footing (prefab or cast-in-place), with the **influence of a nearby slope** treated rigorously. Distinctive vs the other shallow-foundation files:

- **Three bearing methods side by side:** Eurocode 7 shallow (Annex D, D/B≈), **Brinch Hansen** (D/B<…), **Meyerhof** (deeper, D/B<5) — qult, Qu, and a utilisation ratio S for each, with NOK/OK verdicts.
- **Rigorous slope (talud) reduction via the actual failure surface.** Instead of a tabulated reduction factor, it constructs the **breukfiguur** geometrically — a triangular wedge plus a **logarithmic spiral** (opening angle, radius vector, spiral) — for both the Hansen and Meyerhof mechanisms. When a slope truncates the spiral (distance from footing edge to crest + slope angle), the mobilisable passive zone shrinks and bearing is reduced accordingly. The two ~10,000-row sheets (`Gegevens Hanssen`, `Gegevens Meyerhof`) are the **computed slip-surface geometry tables** driving this (Kpmin/Kpmax; limitation in 1 or 2 directions).
- **Stress distribution under the footing** (`Spanningsverdeling onder zool`): drukspanning left/right, effective ("meewerkende") width under eccentric load, point + distributed loads, moments about the toe, eccentricity → effective b′·l′.
- **EC7 design approaches:** Classical, DA1 (1.35/1.5 loads), DA2 (γφ=γc=1.25 on soil) — global safety per approach. Fixed/mobile load split (vaste = mean of min/max; mobiele = half the range).
- Sliding (glijden) and overturning (kantelen) equilibrium checks (attacking vs resisting forces/moments).
- Water table, surcharge (nevenbelasting), 6 soil types, slope distance + angle inputs.

## Catalogue placement — master table section K

Add as the **most rigorous talud-reduction variant** of direct-foundation bearing:

- **Generic shallow foundation, simple:** `fundering_op_staal-E25007` (rect/circ/punching/multi-layer) — primary for routine footings/rafts.
- **Generic shallow foundation, near a slope (RIGOROUS):** `Algemene_berekeningsfile...talud_3` (THIS) — when a footing sits near an embankment crest and slope reduction governs. Geometry-based (log-spiral) reduction, three bearing methods.
- **Bearing-method engines (alternates):** `Fundering_op_staal_7`, `fundering_op_staal_Hansen-Bowles`.
- **EC7-DA structured (French):** `Fondations_directes`.
- **Catenary mast (dedicated):** `Bovenleidingspaal_-_V1-2` — shares this talud-bearing family.

> [!note] Relationship to the catenary tool
> `Bovenleidingspaal` and this file share the **same talud-reduction approach** (Brinch Hansen failure-surface reduction near a slope, three bearing methods). This file is the more complete, standalone shallow-foundation+slope engine; the catenary tool wraps a similar engine with mast-specific load cases, sliding/overturning, and the displacement estimate. When building either notebook, the log-spiral slip-surface + talud-reduction logic can be developed once and shared conceptually.

## Use / priority

- **WILL use** for: footings and culvert/abutment foundations **near railway embankments** (the talud case), where slope reduction governs bearing — a common Infrabel situation. Real solved anchor present (proj. 101303, a culvert column foundation).
- **Build-complexity flag:** the log-spiral failure-surface geometry and the two ~10,000-row lookup tables are the non-trivial part. The bearing formulas (EC7/Hansen/Meyerhof) are standard, but the **talud reduction via constructed slip surface** needs careful reproduction and validation against the solved case — analogous to the ULS-mobilisation caution on the catenary tool.

Links: [[_EC7 — Index]] · [[_Settlement & ground-improvement toolbox — salvage map]]
