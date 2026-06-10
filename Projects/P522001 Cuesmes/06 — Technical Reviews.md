---
title: 06 — Technical Reviews
project: P522 — Atelier de Cuesmes
project_number: P522001
location: Cuesmes (Hainaut)
phase: études détaillées / CSC
role: Ingénieur structures — conception et CSC
client: SNCB / Infrabel
contractor: N/A
status: active
tags: [P522, cuesmes, technical, catenary, foundations, encuvement, heurtoir, deraillement, ec7, ec2]
updated: 2026-06-09
---

# P522001 — Technical Reviews

Engineering content: structural concepts, design decisions, scope definitions, and reasoning.

Scope confirmed in meeting 09/06/2026 with Laurent Vercammen and Koen Depreitere.

---

## Structural Scope Overview

### 1. Fondations de portiques caténaires

**Concept:** Three separate RC pad foundations for catenary portals. Configuration details (span, portal type) are input data from T-ELE (Jeremy Precel) — not yet received.

**Previous context from Réunions Reprise:** Two configurations were initially discussed: two large portals (~22.5 m clear span) and six smaller individual portals (~7.5 m span). Whether this scope has evolved is not confirmed — Jeremy's input will settle it.

**Design method:**
- Bearing capacity and sliding: EC7 ELU envelope (ULS)
- Settlement: EC7 ELS quasi-permanente only
- Foundation geometry: sized to keep eccentricity within kern, satisfying q_Ed ≤ q_Rd per EN 1997-1
- RC socle: EC2 design for punching, bending, and tie reinforcement at base plate interface

**Precedent:** Melle study (Arnaud). Steel portal adapted by Jeremy from Melle. Foundation methodology to be adapted similarly — verify ELU/ELS ratio from Melle before reuse.

**Calculation tool:** Python / Jupyter notebook with `handcalcs` for rendered output.

**Senior input:** May be required for foundation type selection — anticipated in 09/06 meeting. Plan this in advance once OP-01 and OP-02 are resolved.

**Clash with dalle de déraillement:** Position of *traverse bi-bloque* sections must be coordinated with catenary foundation positions in plan before drawings are frozen.

**Key open risk:** Interaction with existing underground structures. If as-built documentation for the Cuesmes yard is incomplete, a survey phase may be required before foundations can be positioned.

---

### 2. Encuvement (Laborex System)

**Architecture:** The Laborex system is a container housing tanks and other machinery. It sits on a supporting slab. Beneath or adjacent to the Laborex installation is an *espace technique* (vide aéré) — an underground box through which various pipes and impétrants (canalisations) pass. These are two distinct structural elements within the same scope item.

**Element 2a — Supporting slab:**
A reinforced concrete slab sized to carry the Laborex container loads. Geometry and load data to be derived from Laborex supplier documentation and SNCB canalization plan.

**Element 2b — Espace technique (vide aéré):**
An underground RC box providing access to pipe networks. Not a retention pit — it is a technical void. Structural design governed by:
- External groundwater pressure (requires OP-01 — geotechnical data)
- Pipe penetrations and wall openings (requires OP-05 — SNCB canalization plan de principe from Reginald)
- Possible earthing pit (*puit de terre*) adjacent to slab (requires OP-06 — check SNCB template)

**Waterproofing strategy:** Two options — (a) perimeter drainage system eliminating net water pressure, or (b) full structural waterproofing. To be fixed once geotechnical data is available.

**Do not freeze dimensions** before OP-05 is resolved. Pipe routing governs wall opening positions.

---

### 3. Dalle de Déraillement

**Concept:** Derailment containment slab placed between rails. Prevents train wheels from travelling away from the track in the event of a derailment. Not to be confused with *dalle d'enraillement* (embedded track slab).

**Selected section type:** *Traverse bi-bloque* — confirmed as best option in 09/06 meeting. Reference example received (REF-DER-001).

**Key design actions:**
- Implement section in execution drawings
- Coordinate position in plan against catenary portal foundation locations — clash management required (OP-07)
- Verify structural design approach against reference example and applicable norms

**Status:** Example received 09/06. Design to be developed.

---

### 4. Heurtoir

**Concept:** Buffer stop structure at the end of a dead-end track. Arrests a train that overruns the end of a siding. This is a structural item: the heurtoir must be founded and anchored, and the structural slab/foundation must resist the impact/braking loads transmitted by the buffer stop equipment.

**Reference material received (09/06):** Example drawing + handwritten calculation note (REF-HEUR-001). Must review to understand:
- Load case (impact/braking force magnitude and application point)
- Foundation type in example
- Applicable norms (Infrabel PTR references for buffer stop loading, if any)

**Status:** Example and calc note received 09/06. Review and design approach to be developed (OP-08).

---

## Design Schedule Context (revised 09/06/2026)

Original T0–T6 gates have all passed. Revised submission deadlines:

| Milestone | Date |
|-----------|------|
| First submission (*1ère remise*) | Early September 2026 |
| Final submission | End September 2026 |

All four structural items must be included in the first submission. Priority sequence based on dependencies:
1. Retrieve geotechnical data (OP-01) — unblocks catenary foundations and encuvement
2. Receive catenary base reactions (OP-02) — unblocks foundation calculations
3. Receive SNCB canalization plan (OP-05) — unblocks encuvement dimensioning
4. Dalle de déraillement and heurtoir can proceed with reference examples in parallel (OP-07, OP-08)

---

Links: [[Projects/P522001 Cuesmes/00 — Overview]] · [[Projects/P522001 Cuesmes/03 — Open Points]] · [[Projects/P522001 Cuesmes/02 — Document Register]]
