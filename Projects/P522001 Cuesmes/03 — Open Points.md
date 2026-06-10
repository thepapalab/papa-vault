---
title: 03 — Open Points
project: P522 — Atelier de Cuesmes
project_number: P522001
location: Cuesmes (Hainaut)
phase: études détaillées / CSC
role: Ingénieur structures — conception et CSC
client: SNCB / Infrabel
contractor: N/A
status: active
tags: [P522, cuesmes, open-points, blockers, geotechnique, caténaire, encuvement, heurtoir, deraillement]
updated: 2026-06-09
---

# P522001 — Open Points

## Situation Assessment (as of 09/06/2026)

Scope definition meeting held on 09/06 with Laurent Vercammen and Koen Depreitere. Structural scope is now frozen to four items. Previous items (dalles d'enraillement, dalles de circulation en entrevoie, socles de loge signalisation) are out of scope.

Key remaining blockers: geotechnical data (path known, not yet retrieved), catenary base reactions (Jeremy Precel), and SNCB canalization plan for encuvement (Reginald committed). Two new design items launched from meeting: dalle de déraillement (example received, traverse bi-bloque section) and heurtoir (example + handwritten calc note received).

## Action Required

### TUC Rail (Nicolas):
- Retrieve geotechnical report from server path (path confirmed 09/06)
- Chase base reactions and base plate geometry from Jeremy Precel (T-ELE)
- Implement dalle de déraillement (*traverse bi-bloque* section) in drawings; manage clash with catenary foundations
- Review heurtoir example + calc note; develop design approach
- Investigate *puit de terre* requirement near Laborex slab (check SNCB template first)
- Confirm catenary foundation type with senior input once geo data available

### Koen Depreitere (Design Manager):
- Facilitate receipt of SNCB canalization *plan de principe* from Reginald
- Confirm whether senior input is organised for catenary foundation type decision

### Reginald / SNCB:
- Provide canalization *plan de principe* for Laborex encuvement (committed 09/06)

### Jeremy Precel (T-ELE):
- Transmit column base reactions and base plate geometry for catenary portal foundations

## Open Items Summary

| ID | Description | Responsible | Status |
|----|-------------|-------------|--------|
| OP-01 | Geotechnical data — retrieve from server path | Nicolas | TO DO — path known |
| OP-02 | Catenary base reactions + base plate geometry | Jeremy Precel | BLOCKING |
| OP-03 | Catenary foundation type (senior input may be needed) | Koen + Nicolas | PENDING |
| OP-04 | ~~Scope split dalles (Nicolas vs Rose)~~ | — | CLOSED — scope redefined 09/06 |
| OP-05 | Encuvement: canalization *plan de principe* from Reginald (SNCB) | Reginald / SNCB | BLOCKING — committed |
| OP-06 | Encuvement: *puit de terre* near Laborex slab — investigate | Nicolas | TO DO — check template |
| OP-07 | Dalle de déraillement: implement *traverse bi-bloque* in drawings + clash with caténaire | Nicolas | TO DO — example received |
| OP-08 | Heurtoir: review example + calc note; develop design approach | Nicolas | TO DO — example received |
| OP-09 | Meeting with Jeremy (catenary + encuvement coordination) | Nicolas | PENDING — Jeremy away |
| OP-10 | Imputation code | — | CLOSED — E01134 0522.001.GA1 |
| OP-11 | Location of voie d'essais 3 kV/25 kV | SNCB/Infrabel | PENDING |

---

## OP-01 — Geotechnical Data (TO DO — path known)

**Problem:** No geotechnical data retrieved yet. Soil parameters, design groundwater level, borehole logs, and CPT profiles are required for: catenary foundation bearing capacity checks (EC7), encuvement design (water table, lateral pressure), and heurtoir foundation.

**Server path confirmed 09/06:**
`T:\TR-SHARED\I-PR\P522_Atelier_de_Cuesmes\02. TR_Engineering\02. Etudes détaillées\01. Input\[SNCB] Etudes géotechniques`

**Note:** Design groundwater level and soil parameters are the structural engineer's own responsibility to derive from geotechnical data — not values to request from the client. The client provides raw data; TUC Rail derives design parameters.

**Closure requires:** Report retrieved from server; CPT profiles and/or borehole logs reviewed; design parameters extracted.

---

## OP-02 — Catenary Base Reactions + Base Plate Geometry (BLOCKING)

**Problem:** Jeremy Precel (T-ELE) is responsible for the steel portal design, adapting the Melle precedent study. Column base reactions (ULS envelope: N, Vy, Vz, My, Mz, Mx) and base plate geometry (plate dimensions, anchor bolt pattern, bolt diameter, edge distances) are required before foundation calculations can begin.

**Closure requires:** Formal transmission of load cases and base plate geometry by Jeremy, sufficient to run EC7 and EC2 foundation calculations.

---

## OP-03 — Catenary Foundation Type (PENDING)

**Problem:** Foundation type not yet selected. May require senior input before design begins. Note from 09/06 meeting: senior review should be anticipated for this item. Once geotechnical data is available (OP-01) and base reactions received (OP-02), foundation type can be assessed.

**Preferred process:** OP-01 + OP-02 resolved → T-STR evaluates feasible foundation types → senior input if needed → type confirmed before calculations begin.

**Closure requires:** Foundation type confirmed, with senior sign-off if applicable.

---

## OP-05 — Encuvement: Canalization *Plan de Principe* from Reginald (BLOCKING)

**Problem:** SNCB must provide a canalization *plan de principe* showing pipe routing and impétrants passing through the *espace technique* (vide aéré under Laborex). Reginald (SNCB) has committed to provide this. Without it, the structural layout of the encuvement box cannot be frozen — pipe penetrations govern wall opening positions, slab thickness, and embedment depth.

**Closure requires:** Plan de principe received from Reginald; pipe locations and sizes confirmed; structural slab/box can then be dimensioned.

---

## OP-06 — Encuvement: *Puit de Terre* Near Laborex Slab (TO DO)

**Problem:** Possible requirement for a *puit de terre aux abords de la dalle Laborex*. Mentioned in 09/06 meeting as a possibility. Action: check whether this is covered in the SNCB Laborex installation template before designing from scratch.

**Closure requires:** SNCB template checked; either confirmed covered (with reference) or confirmed as additional structural item requiring separate design.

---

## OP-07 — Dalle de Déraillement: Drawing Implementation + Clash with Caténaire (TO DO)

**Problem:** Example provided by Laurent (09/06). *Traverse bi-bloque* section selected as best option. Must now be implemented in drawings and checked against catenary portal foundation positions to manage clashes.

**Reference:** REF-DER-001 (received 09/06) — see [[02 — Document Register]].

**Closure requires:** Dalle de déraillement drawn in project DWGs; clash with catenary foundations identified and resolved; section detail with *traverse bi-bloque* included.

---

## OP-08 — Heurtoir: Design Approach Review (TO DO)

**Problem:** Heurtoir (buffer stop structure at dead-end track) confirmed as new structural item. Example drawing and handwritten calculation note provided by Laurent (09/06). Design approach not yet reviewed; applicable standards and load cases to be identified.

**Reference:** REF-HEUR-001 (received 09/06) — see [[02 — Document Register]].

**Closure requires:** Example and calc note reviewed; design approach documented; applicable norms identified; calculation started.

---

## OP-09 — Meeting with Jeremy (Catenary + Encuvement Coordination) (PENDING)

**Problem:** Jeremy Precel is the key interface for catenary foundations (base reactions, base plate geometry — OP-02). Currently away; meeting to be organised.

**Closure requires:** Meeting held; base reactions and base plate geometry received (OP-02).

---

## OP-11 — Location of Voie d'Essais 3 kV/25 kV (PENDING)

**Problem:** Location of the 3 kV/25 kV test track not confirmed. Structural implications for catenary elements depend on chosen track.

**Closure requires:** Decision by SNCB/Infrabel, transmitted via Koen.

---

Links: [[Projects/P522001 Cuesmes/00 — Overview]] · [[Projects/P522001 Cuesmes/02 — Document Register]] · [[Projects/P522001 Cuesmes/01 — History]]
