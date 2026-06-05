---
title: 06 — Technical Reviews
project: P234403 Luttre
project_number: P234403
location: Luttre (Wallonia)
phase: suivi d'exécution
role: Ingénieur structures — vérification as-built
client: Infrabel
contractor: DW (Dubois Dawance)
status: active
tags: [P234403, luttre, technical, review, radiers, tfo, bardage, kz, winkler]
updated: 2026-06-04
---

# P234403 — Technical Reviews

Engineering content: design phases, as-built verification decisions with reasoning, technical analysis.

---

## Phase 1: Design & Preliminary Studies (2023–2024)

TUC Rail conducts full structural design:
- Nicolas PAPALABROS designs and calculates all buildings (B01–B03, TFO)
- Two main calculation notes: BAT 5565 (transformer chamber) + BAT 5296 (utility building)
- Full geotechnical study conducted by Els Voet (preliminary; final report delivery unclear)

**Key design parameters established:**
- Raft foundations: nominal cover cnom = 45 mm (PTR CE01 §5.6.1, EE3)
- Masonry walls (cellular concrete blocks) with RC ring beams
- Prestressed hourdis roofs with in-situ shear keys
- TFO as permanent utility building (demountable intent introduced later by Infrabel)
- Transformer load 30 kN/m² applies to TFO only, not to B01 raft

**These designs are contractually binding on DW.**

---

## Phase 2: Construction & As-Built Documentation (2024–2025)

Construction substantially complete. DW submits as-built documentation to BEM for verification and compliance with TUC Rail design.

---

## Phase 3: As-Built Structural Review — Radiers (April–May 2025)

### BEM Raft Submission S13 — Six Blocking Points (Nicolas response S16)

BEM (Bureau d'Étude Mosan, ref. 25/0805) submits as-built raft studies for B01, B02, B03.

**Finding A1 — fyk documentation:** BEM calculations cite steel grade without confirming as-built steel matches PTR CE01 cap (fyk ≤ 400 MPa). DW must provide delivery documentation (mill certificate).

**Finding A2 — Normative references:** BEM may cite SIA 162 (Swiss code) instead of EC2 with Belgian NBN. SIA 162 is not acceptable for Belgian infrastructure.

**Finding A3 — Cover cnom = 45 mm:** As-built cover survey required. Concrete class must be documented. PTR CE01 §5.6.1 specifies cnom = 45 mm for permanently buried elements (exposure class EE3).

**Finding A4 — SLS verifications:** EN 1992-1-1 requires wk ≤ 0.3 mm, concrete stress < 0.6 f_ck, and deflection limits — incomplete or missing in S13.

**Finding A5 — Kz derivation (Winkler coefficient):**

BEM used Kz = 15,000 kN/m³. This is unjustified. Vesic formula applied to Luttre CPT profiles (S55.6a, S55.6b) gives justified range 2,000–5,000 kN/m³ — BEM's value is overestimated by factor 3–7.5.

**Structural consequence analysis:** M ∝ Kz^0.25 → at Kz = 5,000 vs 15,000, moment reduction ~30–40%. **BEM's higher Kz is structurally conservative** (larger moments). It is not unsafe, but it is unjustified. BEM must either:
- Derive Kz from CPT using explicit formula, OR
- Demonstrate via numerical sensitivity that 15,000 kN/m³ is a conservative upper bound

**Critical enabler:** final geotechnical report from Els Voet (provides CPT profiles and soil classification for Vesic derivation).

**Finding A6 — Load combinations:** EN 1990 + Belgian NA partial factors and ψ values must be applied. Common error: using generic Annex A instead of Belgian-specific coefficients.

---

## Phase 3B: TFO Building Design (April 2026)

### BEM Submission 25/0805 — Six Blocking Points (Nicolas reply S18)

**Finding B1 — Demountable concept not justified:**

BEM shows chemical anchors for purlins (HEA 160, UPN 160) as **permanent** in structural drawings (figures 3.2.3, 3.3.3). No demountable zone plan or disassembly sequence provided.

**Design intent ambiguity:** Original TUC Rail design: TFO as permanent utility building. Infrabel intent (implied): demountable roof for equipment access during operation. BEM current: contradictory (permanent anchors + demountable claim).

**Why this must be resolved:** If the roof is demountable, structural design must justify which connections are removable, the disassembly sequence, and temporary supports. If permanent, the anchor design stands as-is. Ambiguity is not acceptable.

**Finding B2 — Wind load methodology (tableau 7.6 vs 7.3):**

BEM applied EN 1991-1-4 tableau 7.6 (open building — external pressure only). TFO is an enclosed utility building → tableau 7.3 (closed building, net pressure w = qp × [cpe + cpi]) must apply. BEM's approach underestimates outward pull on anchors by ignoring internal pressure cpi.

**Finding B3 — Steel sheeting ELS combination undersized:**

Bac 1.0 mm thickness load combination likely undersized. ELS characteristic combination missing ψ0,snow = 0.5 factor per EN 1990 Table A1.1. Sheeting must be verified under G_k + 0.5 × Q_k,snow.

**Finding B4 — Section change HEA 160/UPN 160 vs IPE 240/UPN 240:**

Original TUC Rail design: IPE 240 + UPN 240. BEM revised to HEA 160 + UPN 160. Lcr (buckling length) for UPN inconsistent relative to HEA. Section adequacy not demonstrated.

**Finding B5 — TFO canopy (*auvent*) note missing:**

Infrabel requested canopy addition between B02 and TFO. Standalone structural note required (geometry, bracing, wind loads, load transfer, connection details). Not yet received.

**Finding B6 — Wind load reference (qp = 670 N/m², 22/12/2025) missing:**

Referenced but not provided. Must be obtained from BEM to validate qp assumption.

---

## Phase 3C: Bardage B03 — Cladding System Compliance

### Charpente Habitat Response 04/05/2026 — Three Remaining Open Points

**Finding C1 — SKR8100 edge conditions (announced, not delivered):**

WKF120 bracket + SKR8100 works in solid RC field conditions. Edge conditions (rim-of-slab, ring beam edge) require project-specific supplementary calculation per ETA 20/0363 scope. Charpente Habitat committed; note not yet produced.

**Finding C2 — EXE plans (ventilation grilles, downpipes):** Not addressed in response. Still outstanding.

**Finding C3 — FT 36 Roosens block:** Signed datasheet not addressed. Still outstanding.

---

## Key Technical Principles Established (Luttre Pattern)

1. TUC Rail design is binding; contractor verifies compliance — does not re-design
2. CSC, PTR CE01, Eurocodes with Belgian NA — not internal TUC Rail opinions — cited in correspondence
3. Kz sensitivity insight: overestimate is conservative (M ∝ Kz^0.25); require defensible derivation
4. "Announced ≠ delivered" — commitments tracked separately from receipt
5. Blocking items non-negotiable until resolved; as-built file cannot close before all 15 blocages resolved

**Boitsfort P101581 adopted this Luttre model exactly** — same team, same argument discipline.

---

Links: [[00 — Overview]] · [[02 — Document Register]] · [[03 — Open Points]]
