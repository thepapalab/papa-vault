---
title: PTR CE01 Ch01-02 — General and Project Guidelines
type: norm-extract
source: "PTR CE01 Fascicule 1 v1 (Avis 15 I-AM/2022)"
chapters: [1, 2]
tags: [PTR CE01, Infrabel, scope, project-guidelines, calc-notes, CC2]
related: ["[[PTR CE01 — Index]]", "[[_Knowledge — Index]]"]
created: 2026-06-02
---

# PTR CE01 Ch01-02 — General and Project Guidelines

## Ch1 — Introduction

### 1.1 Scope

PTR CE01 Fascicule 1 replaces Chapter 30.2.0 of Fascicule 30.2. It sets out general dispositions, design principles, and technical prescriptions for the construction of civil engineering structures (*ouvrages d'art*) and buildings managed by Infrabel.

It is treated as a document attached to the Eurocodes. It **complements or replaces** the corresponding Eurocode prescriptions.

**Applicability:**
- All structures managed by Infrabel.
- All structures and works liable to affect the stability of the track or buildings.
- Specifically: structures under tracks within the zone of influence (§2.3.2), structures overhanging tracks, or structures adjacent to tracks whose height exceeds their distance from the nearest track.

**Hierarchy rule:** Where a Belgian National Annex (ANB) exists, the Eurocode applies with its ANB. Where no ANB is published, the Eurocode applies alone and nationally determined parameters are fixed per project.

### 1.3 Reference documents

**Key Eurocodes (Table 1.1):**

| Eurocode | Standards |
|----------|-----------|
| EC0 | NBN EN 1990 + A2 (bridges) |
| EC1 | NBN EN 1991-1-1 to -1-7, NBN EN 1991-2 (traffic) |
| EC2 | NBN EN 1992-1-1, -1-2, -2, -3 |
| EC3 | NBN EN 1993-1-1 to -1-11, -2, -5 |
| EC4 | NBN EN 1994-1-1, -1-2, -2 |
| EC5 | NBN EN 1995-1-1, -1-2, -2 |
| EC7 | NBN EN 1997-1, -2 |
| EC8 | NBN EN 1998-1, -2, -4 |

Other references: NBN EN 1337 (bearings), CEN/TR 17231 (track-bridge interaction), CSTC report 20-2020 (EC7 pile design from CPT), Standaardbestek 250 (Flanders), Qualiroutes (Wallonia).

---

## Ch2 — Design and Study Guidelines

### 2.1 General

The contractor is responsible for all surveying and setting-out, including for prefabricated elements. Measurements on tracks are only possible during possessions. Preliminary and final designs are produced by Infrabel unless otherwise stated in the CSC.

Detailed rebar drawings and bar schedules are **not** produced by Infrabel — the contractor must provide them unless included in the CSC.

### 2.2 Project Elaboration

#### 2.2.1 Preliminary design (*avant-projet*)

Defines the overall concept: superstructure, infrastructure, foundation type, architectural finish, construction method. Must include:

- General plans (plan + elevation), min. 1/100, with materials list.
- Cross-sections and longitudinal sections, min. 1/50 (or 1/20).
- Location plan at 1/1000 or 1/10000 with north arrow.
- General calculation note: main assumptions on structural behaviour, justification of principal dimensions.

No divergence is permitted between these documents and the overall concept fixed by Infrabel.

#### 2.2.2 Final design (*projet définitif*)

Must enable actual construction and reflect the works as faithfully as possible. Particular attention to durability (drainage, corrosion protection, inspection access, replaceability of components with service life < 100 years).

Must include (non-exhaustive):
- Location plan, cadastral plan, general plan (min. 1/100), implantation plan.
- Formwork drawings for superstructure (min. 1/20) and infrastructure (min. 1/20–1/50).
- Rebar drawings for superstructure, infrastructure and foundations (with bar numbers, diameters, shapes, laps, couplers, grades).
- Plans for prefabricated prestressed or composite beams.
- Phasing plans.
- Global assumption note, to be approved before calc notes.
- Calculation notes (ULS + SLS).
- Descriptive or summary bill of quantities.

#### 2.2.3 Integrated 3D models

Infrabel may require a 3D-based study (DWG, RVT, IFC). The model must be georeferenced in Lambert coordinates with a digital terrain model. 2D principle drawings are provided as annexes. The contractor must update the model at each design change and submit it for approval before proceeding.

### 2.3 Documents to Provide

Infrabel has **30 calendar days** to approve submitted documents. If deemed incomplete, a new 30-day review period starts from receipt of the complements.

**After approval of the preliminary or final design:** digital files (DXF/DWG/RVT + CTB plots) + other documents in electronic format.

**Before works start:**
- All execution drawings.
- Particular construction and detail drawings with corresponding calc notes.
- Workshop drawings and calc notes from subcontractors/fabricators.
- 3 paper copies + 1 digital copy of plans.
- 3 copies + 1 digital copy of other documents.

**During works:** particular construction plans, calc notes, deformation/stress study for bridge tests (if design by contractor).

**For provisional reception:** post-intervention dossier (AR on temporary/mobile sites).

### 2.4 Principles for Structural Studies

#### 2.4.1 Structural calculations

NBN EN 1990 and its Annexes A1 and A2 apply unless derogated. The following effects must be considered where significant:
- Shrinkage and creep.
- Second-order effects (imperfections, geometry changes under load).
- Local effects at bearings, load concentration zones, anchorage zones, or geometric discontinuities.
- Load fluctuations and fatigue.
- Cracking or non-cracking of concrete.

**No plastic redistribution exceeding 25%** is permitted at ULS.

Global stability must be checked for the undeformed system and, where necessary, the deformed system.

Test-based design is permitted but must be validated against calculation models accounting for main parameters.

#### 2.4.2 Consequence class

> **CC2 (normal safety)** applies to all civil engineering structures (bridges, retaining walls, etc.) unless otherwise stated in the CSC.

#### 2.4.3 Structural modelling

Simplified models are accepted if their domain of application is clearly defined. Acceptable element types: linear elements (beams, columns), 2D elements (slabs, walls), shells, and combinations thereof. Other element types require specific justification.

#### 2.4.4 Use of calculation codes

Computer codes are permitted. Each use requires an explanatory note covering:
- Limits of use.
- Element types and degrees of freedom used.
- Sketches of the model, boundary conditions, load application points and values per load case, logical model construction.
- How special load cases are handled (prestress, temperature, deferred deformations).
- Account for non-constant flexural stiffness EI of concrete (cracked vs. uncracked).

**Output:** Results must be presented clearly and synthetically, preferably graphically. Computer output is only an annex to the accompanying calc note.

**Minimum check:** Results from computer codes must be verified using classical hand calculation methods (statics, compatibility, virtual work) for the most critical load cases and sections.

#### 2.4.5 Minimum content of calc notes

1. Table of contents, structure description, author signature, date.
2. Assumptions, preconditions, references, notation, standards.
3. Load summary (load models, classification factors, dynamic coefficients, material grades).
4. Setting-out, skew angle, road/track alignment, span determination.
5. Superstructure: calculation method, material/section choice with commentary, modelling, calculations and results, optimisation. Computer code summary, graphical output, comparison with minimum check. Detail calculations, connections, deformations, fatigue, safety/serviceability/durability assessment.
6. Infrastructure (bearings, crossbeams, piers, abutments, foundations, retaining walls): same as item 5.
7. Geotechnical study including implantation plan.

> **All civil engineering calculations must be signed by a Master in Civil Engineering (construction orientation) with at least 5 years of experience in bridge design and construction.**

---

Links: [[PTR CE01 — Index]] · [[PTR CE01 — Ch03 — Actions]] · [[_Knowledge — Index]]
