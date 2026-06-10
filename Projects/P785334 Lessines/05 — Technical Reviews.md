---
title: 05 — Technical Reviews
project: P785334 Lessines
project_number: P785334
location: Lessines
phase: suivi d'exécution
role: Ingénieur structures principal — validation exécution
client: Infrabel
contractor: SM Wanty / De Cock
status: active
tags:
  - P785334
  - lessines
  - technical
  - design
  - csv
  - joint
  - armatures
updated: 2026-06-05
---

# P785334 — Technical Reviews

Engineering content: design concept evolution, key technical decisions with reasoning, review articles.

---

## CSV Design Concept Evolution

The project went through four successive design stages before reaching the current execution solution.

### Stage 1 — Base design (tender)

CSV monolithic pushed in place. Ramps cast in place. Solution abandoned for cost reasons.

### Stage 2 — Client variant (CSC AT 4.991)

Modular prefabrication: elements of 2–3 m installed by crane. Joints compressed by post-tensioning (interlocking) to ensure watertightness. This solution constitutes the contractual basis.

### Stage 3 — Contractor proposal (deviation)

CSV reduced to two large prefabricated elements installed by 750T crane. Post-tensioning removed. Joint proposed by mortar (Groutex / SikaGrout 234). **Rejected** on three independent grounds:

1. **Structural:** Without active compression (post-tensioning), the joint is neither monolithic nor watertight. Passive mortar joints will crack under railway vibration and differential settlement.
2. **Durability (RAS):** Mortar products with granulat additions present an alkali-silica reaction risk. RAS qualification testing (Oberholster modified) requires 2+ months minimum — not feasible within the project timeline. Neither SikaGrout 234 nor Groutex could be qualified in time. See RAS analysis section below.
3. **Operational:** Installation of 20+ heavy elements in 4 days with a single 750T crane; missing soil bearing capacity study under crane supports.

The contractor conditioned compliance with the CTL deadline on immediate approval of this concept — a timeline pressure tactic that was noted and did not alter the technical position.

### Stage 4 — Retained solution (execution design)

Two large prefabricated elements with a full cast-in-place joint in C35/45 concrete with overlap reinforcement. The joint behaves as a monolithic structure. Proposed by Bart De Pauw (expert structural engineer) as the path forward: full concrete joint, no *clavetage*, 40 cm minimum joint width. This is the current contractual solution.

**Why this solution:**
- Mortar-type solutions rejected on two independent grounds: structural (no compression) and durability (RAS non-qualification within timeline)
- C35/45 cast-in-place joint with overlap reinforcement ensures full moment continuity
- Concrete expert (Level 7, specialization confirmed) validated the solution as appropriate for site conditions
- The 50 cm joint space is tight but achievable with adapted reinforcement

---

## Key Design Decisions Log

| Date | Decision | Justification | Status |
|------|----------|--------------|--------|
| 28/01/2026 | Technical brief to design team | Full concept evolution documented; mortar solutions refused on structural + durability grounds | FINAL |
| Jan 2026 | Groutex / SikaGrout joint rejected | Not monolithic (structural) + RAS non-qualification within timeline (durability) | FINAL — irrevocable |
| ~10/02/2026 | RAS analysis — Maida CIMIC | Mortar solutions with granulat additions cannot be RAS-qualified within CTL timeline | CONFIRMED |
| Feb 2026 | Global rejection of 7 documents | NC PTR01: handwritten, incomplete, opaque assumptions | MAINTAINED for new submission |
| 13/02/2026 | Hard reset documentation | Submission level degraded to handwritten drafts | CLOSED — baseline reset |
| 16/03/2026 | Concrete maturation analysis — Maxime | CEM I required for early strength; 20 MPa at 24h confirmed; CEM III/A not suitable | CONFIRMED |
| 17/02/2026 | Stop-work Zone 2 | Armature layer inversion detected — -85% steel deficit voile côté voies | CLOSED — resolved |
| COCHT item 08/26 G | Works without approved NdC | All works undertaken without approved note are at contractor's responsibility | TO MAINTAIN in all future minutes |

---

## CSV Joint — Durability: RAS Analysis (~10/02/2026)

Analysis by Maida CIMIC (QHSE senior engineer) establishing that mortar solutions cannot be qualified for RAS compliance within the project timeline.

### RAS mechanism

Alkali-silica reaction (RAS) is a concrete pathology where alkali gel forms within reactive granulats and causes swelling in hardened concrete — typically manifesting 5–10 years after placement. It is a known failure mode in railway infrastructure (catenary foundations with untraced granulat additions).

### Why mortar solutions fail the RAS requirement

- **NBN EN 1504-6** (standard for sealing mortars) does not address RAS prevention — unlike the concrete standard (NBN B 15-001).
- When granulats (kift, Dmax 8 mm) are added to Groutex or SikaGrout to improve workability, the product becomes a micro-concrete. The granulat reactivity cannot be controlled via the commercial product datasheet.
- **SikaGrout 234:** Not BENOR certified. No CE or AFNOR report provided. RAS non-reactivity of Sika Charge C not demonstrated by an accredited body.
- **Groutex type 608:** BENOR certified but only without granulat additions. Addition of kift reintroduces the RAS risk.

### Qualification path and timeline

To use a mortar with granulat additions, the granulats must be demonstrated non-reactive via one of:
1. Documented declaration of non-reactivity (geological, petrographic, chemical evidence)
2. Oberholster modified accelerated gonflement test — **duration: ~2 months minimum**; if inconclusive, the longer test runs 3–12 months

Both paths are incompatible with the CTL timeline. Conclusion: **no mortar solution with granulat additions can be qualified for this project.** A solution without granulat additions (pure grout) was noted as theoretically possible but very expensive and not chosen by the contractor.

### Consequence

The RAS argument constitutes an independent and parallel basis for the rejection of all mortar-type joint solutions, separate from the structural monolithism argument. Both grounds are on record.

---

## CSV Joint — Concrete Maturation for Joint (16/03/2026)

Analysis by Maxime (concrete technologist) on the feasibility of C35/45 cast-in-place joint reaching sufficient strength before train passage at end of CTL.

### Constraint

The joint concrete must reach adequate strength before the first train passes. Vibration risk during early hydration is the primary concern.

### Finding

- **CEM I at 24h:** ~20 MPa demonstrated from CCB central — considered sufficient for initial load given the concrete has already achieved significant set.
- **CEM III/A N (standard evolution):** Inadequate for early-strength requirement. CEM III does not have an "R" (rapid) variant — only CEM I exists in the R and R HES configurations.
- **CEM I availability:** Less common but confirmed available from CCB suppliers in the region (precedent: other projects in the programme).
- The contractor's phrase "strongest possible concrete" was interpreted as "deliverable by their preferred supplier" rather than a technical specification — this does not constitute a technical requirement and was not accepted as such.

### Conclusion

CEM I is the required cement type for the joint. The concrete recipe must be confirmed by the supplier's concrete technologist and submitted for approval ahead of execution.

---

## Armature Layer Inversion — Technical Analysis

### Finding (17/02/2026)

Vertical bars (carrying flexural stress) placed in 2nd layer instead of 1st layer. The reduction in effective lever arm causes a drop in flexural resistance (M_Rd).

**Zone 2 (voile côté voies):** structural steel deficit of **-85%** relative to required.
**Intermediate voile:** deficit of **-56%**.

### Consequence

With reduced lever arm d', M_Rd = A_s × f_yd × d' is reduced by the ratio d'/d. At -85% deficit, the section is structurally inadequate for the design combination.

### Status

Stop-work order issued 17/02/2026. Any submission including Zone 2 elements must demonstrate structural stability with reduced lever arms. See [[Projects/P785334 Lessines/03 — Open Points]] NC-1.

---

## FEM Symmetry Sensitivity — Lifting Anchor Element 21

### Issue

The contractor proposed manual symmetry assumptions for element 21 lifting anchor calculation (no FEM). TUC RAIL conducted parallel SCIA analysis on comparable ramp elements.

**Finding:** max/avg ratio of +15% on comparable elements. Manual symmetry assumption understates peak anchor force.

### Technical Position

The +15% max/avg ratio observed on ramp elements constitutes the benchmark for rejecting manual symmetry on element 21. The contractor must provide SCIA output showing load distribution on element 21 explicitly.

---

## Double Coefficient Risk — Lifting Verification

### Issue

The dynamic lifting coefficient must not be applied simultaneously:
1. Inside the calculation note (applied to the structural force model)
2. In the loads submitted to PROFIS (the anchor verification software)

### Consequence

Double application results in a squared safety factor — unconservatively designed in some load paths, over-conservative in others. A correct treatment applies the dynamic coefficient once, at the structural model level, and submits factored loads to PROFIS without re-amplification.

---

## HERMES Dossier Review — 04/06/2026 (inventory NCs)

Inventory-level findings on the 163-document dossier. Review strategy, effort estimate, and element priority are in [[Projects/P785334 Lessines/03 — Open Points]] (NC-D).

- **NC-D1:** XLSX bordereaux without corresponding PDF (EF30, EF31&32) — cannot be approved.
- **NC-D2:** Index inconsistencies between coffrage and ferraillage plans (Él. 30: EC.B/EF.A; Él. 124, 125: EC.A/EF.0) — ferraillage potentially based on obsolete geometry.
- **NC-D3:** Filename element-numbering errors (EF031, EF032 labelled "30"; EF101 "63&63"; EF172 "132&132").
- **NC-D4:** Non-standard nomenclature (Quai 2 recap plan, no project plan number).
- **Prerequisite not met:** Zone 2 reinforcement plans (EF110–113) cannot be approved without validated CSV calculation note Indice B.

---

Links: [[Projects/P785334 Lessines/00 — Overview]] · [[Projects/P785334 Lessines/02 — Document Register]] · [[Projects/P785334 Lessines/03 — Open Points]]
