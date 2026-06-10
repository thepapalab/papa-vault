---
title: 04 — Strategic Context
project: P522 — Atelier de Cuesmes
project_number: P522
location: Cuesmes (Hainaut)
phase: cahier de charges
role: Ingénieur structures — conception et plans d'exécution
client: SNCB / Infrabel
contractor: N/A
status: active
tags: [P522, cuesmes, strategy, scope, normative, ec7, caténaire]
updated: 2026-06-09
---

# P522 — Strategic Context

## Confirmed Structural Scope (as of 09/06/2026)

Four structural items retained following scope definition meeting with Laurent Vercammen and Koen Depreitere:

1. **Encuvement (Laborex system)** — supporting slab + *espace technique* (vide aéré underground box for pipes/impétrants)
2. **Dalle de déraillement** — derailment containment slab, *traverse bi-bloque* section
3. **Heurtoir** — buffer stop structure at dead-end track
4. **Fondations de portiques caténaires** — RC pad foundations for catenary portals

Items removed from scope: dalles d'enraillement rail-route, dalles de circulation en entrevoie, socles de loge signalisation.

## Scope Discipline

Engineering decisions are TUC Rail's own responsibility. The following are **not client data requests** — they are the structural engineer's job:
- Design groundwater level (derived from geotechnical report)
- Soil bearing capacity and design parameters (derived from CPT/boreholes)
- Exposure classes and concrete grades
- Load model selection for slabs and foundations

Client data requests must be limited to: system-imposed geometry (track centres, clearance envelopes), actual equipment loads (maintenance vehicles, catenary portal reactions), existing foundation details, anchor patterns, and canalization routing (SNCB to provide). Do not delegate engineering judgement upstream.

## Catenary Foundations — Precedent and Scope

Jeremy Precel (T-ELE) is adapting the Melle precedent study for the steel structure. TUC Rail T-STR scope is strictly: foundation design (EC7 bearing capacity + sliding, EC2 RC pad sizing), AT, métré, and CAD execution drawings. Steel portal sizing is T-ELE's scope — do not encroach.

Three separate foundation configurations are expected. Portal geometry and base reactions drive the foundation design entirely — calculations cannot begin without them. **Senior input anticipated for foundation type selection** (flagged in 09/06 meeting).

**EC7 load combination approach (confirmed from Melle precedent, verify ratio before reuse):**
- ELU (bearing capacity and sliding): ULS design loads directly
- ELS quasi-permanente: settlement verification only
- Do not use ELS caractéristique for settlement without checking the project-specific ELU/ELS ratio from Melle

**Interaction check with existing structures:** Before positioning foundations, confirm existence and location of existing underground structures (other foundations, drainage, cable ducts). Dalle de déraillement may also generate clash — coordinate early.

**Clash with dalle de déraillement:** The *traverse bi-bloque* section of the dalle de déraillement must be positioned in plan relative to catenary portal foundations. This clash check must happen before drawings are frozen.

## Encuvement (Laborex System) — Concept Strategy

The Laborex system is a container housing tanks and other machinery. The structural scope comprises two elements: (1) a **supporting slab** for the Laborex container, and (2) an **encuvement / espace technique** — a *vide aéré* (underground box) through which pipes and impétrants pass.

The *espace technique* is not a retention pit; it is a technical access void. Structural design is governed by:
- External groundwater pressure (once geotechnical data available — OP-01)
- Pipe penetrations and routing (once canalization *plan de principe* received from Reginald — OP-05)
- Possible *puit de terre* requirement (to be investigated — OP-06)

Do not freeze structural dimensions before canalization routing is confirmed. A premature freeze risks costly late-stage revisions for pipe clashes.

## Normative Framework

| Standard | Scope |
|----------|-------|
| EN 1990 (EC0) + Belgian NA | Load combinations, partial factors |
| EN 1992-1-1 (EC2) + Belgian NA | Concrete design — foundations, cuve, dalles, socles |
| EN 1997-1 (EC7) + Belgian NA | Geotechnical design — bearing capacity, settlement, sliding |
| EN 1991-1-1 + Belgian NA | Imposed loads — slabs, traffic |
| PTR CE01 (Infrabel) | fyk ≤ 400 MPa, cnom per exposure class |
| CSC P522 | Tender spec — contractual reference once issued |

## Commercial / Offer Strategy

When drafting hour estimates:
- CAD hour ranges are deliberately widened to absorb draughtsperson variability
- No explicit senior/junior hour splits in client-facing documents
- Senior input on catenary foundation type should be scoped internally if needed
- Informal collaboration arrangements (Arnaud/Melle reuse) are kept off contract

## Client & Institutional Context

- Project involves two clients (SNCB and Infrabel) — scope attribution between them on certain items (notably direct orders on Infrabel framework contracts) is not fully resolved
- TEF Lot 3 approval status: not confirmed
- Voies 49/50 are on the critical path to Q2 2027 service entry — these elements likely have priority over lower-urgency structural items

---

Links: [[Projects/P522001 Cuesmes/00 — Overview]] · [[Projects/P522001 Cuesmes/03 — Open Points]]
