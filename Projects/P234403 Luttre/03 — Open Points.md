---
title: 03 — Open Points
project: P234403 Luttre
project_number: P234403
location: Luttre (Wallonia)
phase: suivi d'exécution
role: Ingénieur structures — vérification as-built
client: Infrabel
contractor: DW (Dubois Dawance)
status: active
tags: [P234403, luttre, blocages, radiers, TFO, bardage, closure]
updated: 2026-06-04
---

# P234403 — Open Points

**Total blocages: 15** (6 radiers + 6 TFO + 3 bardage). As-built file cannot close until all resolved.

## Summary

| ID | Domain | Issue | Responsible | Status |
|----|--------|-------|-------------|--------|
| A1 | Radiers | fyk documentation | DW | BLOCKING |
| A2 | Radiers | Normative references (SIA 162 → EC2) | BEM | BLOCKING |
| A3 | Radiers | Cover cnom = 45 mm as-built | DW/BEM | BLOCKING |
| A4 | Radiers | SLS verifications | BEM | BLOCKING |
| A5 | Radiers | Kz derivation (conditional on Els Voet report) | BEM + Els Voet | BLOCKING |
| A6 | Radiers | Load combinations EC0 Belgian NA | BEM | BLOCKING |
| B1 | TFO | Demountable concept not justified | BEM | BLOCKING |
| B2 | TFO | Wind tableau 7.6 vs 7.3 (wrong) | BEM | BLOCKING |
| B3 | TFO | Steel sheeting ELS undersized | BEM | BLOCKING |
| B4 | TFO | Section change HEA 160/UPN 160 unjustified | BEM | BLOCKING |
| B5 | TFO | Auvent structural note missing | BEM + Raphaëlle | BLOCKING |
| B6 | TFO | Wind load qp reference note missing | BEM | BLOCKING |
| C1 | Bardage B03 | SKR8100 edge/cmin calculation | Charpente Habitat/BEM | BLOCKING |
| C2 | Bardage B03 | EXE plans ventilation/downpipes | Charpente Habitat | BLOCKING |
| C3 | Bardage B03 | FT 36 Roosens signed | Charpente Habitat | BLOCKING |

---

## Domain A: Radiers (B01/B02/B03)

### A1 — fyk documentation (BLOCKING)

**Problem:** BEM calculations cite steel grade without confirming as-built steel matches PTR CE01 limit (fyk ≤ 400 MPa).

**Exigence:** PTR CE01 §5.6.1 | **Responsible:** DW

**Closure requires:** Steel delivery documentation confirming fyk ≤ 400 MPa (mill certificate or delivery ticket)

### A2 — Normative references (BLOCKING)

**Problem:** BEM references SIA 162 (Swiss code) instead of EC2 with Belgian NBN.

**Exigence:** CSC & PTR CE01 — Eurocodes with Belgian NA required | **Responsible:** BEM

**Closure requires:** Revised S13 citing only EC2 + Belgian NA

### A3 — Cover cnom = 45 mm as-built (BLOCKING)

**Problem:** BEM must verify as-built cover matches 45 mm. Concrete class must be documented.

**Exigence:** PTR CE01 §5.6.1 (cnom = 45 mm, EE3) | **Responsible:** DW (on-site) + BEM (verification)

**Closure requires:** Concrete class confirmed (cube test reports); cover survey (min. 3 points/area) showing cnom ≥ 45 mm; if cnom < 45 mm observed → structural justification or remediation plan

### A4 — SLS verifications (BLOCKING)

**Problem:** SLS calculations missing or incomplete in S13.

**Exigence:** EN 1992-1-1: wk ≤ 0.3 mm, concrete stress < 0.6 f_ck, deflection limits (cl. 7.4.3) | **Responsible:** BEM

**Closure requires:** Revised S13 with full SLS (crack width, stress, deflection)

### A5 — Kz derivation (BLOCKING — conditional on geotechnical report)

**Problem:** BEM used Kz = 15,000 kN/m³. Justified range per Vesic formula on Luttre CPT profiles: 2,000–5,000 kN/m³. BEM's value overestimated by factor 3–7.5. However, it is structurally conservative (M ∝ Kz^0.25 → higher Kz = larger moments).

**Exigence:** PTR CE01 — defensible geotechnical assumptions required | **Responsible:** BEM + Els Voet

**Closure requires:** Final geotechnical report from Els Voet (critical) + Kz derived from CPT via explicit formula (Vesic, Terzaghi, or equivalent) OR numerical sensitivity demonstrating 15,000 kN/m³ is conservative bound

### A6 — Load combinations EC0 Belgian NA (BLOCKING)

**Problem:** Must verify load combinations follow EN 1990 + Belgian NA partial factors (γ_G, γ_Q) and ψ values.

**Exigence:** EN 1990 Annex A1 + Belgian NA | **Responsible:** BEM

**Closure requires:** Revised S13 showing all load combinations with correct partial factors & ψ values per Belgian NA

---

## Domain B: TFO Building

### B1 — Demountable concept (BLOCKING)

**Problem:** Chemical anchors shown as permanent (figures 3.2.3, 3.3.3). No demountable zone plan or disassembly sequence.

**Responsible:** BEM

**Closure requires:** Explicit demountable zone plan (which connections removable, disassembly sequence, temporary support) OR confirmation roof is permanent with permanent anchor design

### B2 — Wind tableau 7.6 vs 7.3 (BLOCKING)

**Problem:** BEM applied tableau 7.6 (open building). TFO is enclosed → tableau 7.3 required. Net pressure w = qp × [cpe + cpi] must include internal pressure cpi.

**Exigence:** EN 1991-1-4 | **Responsible:** BEM

**Closure requires:** Revised TFO design using tableau 7.3 (closed building) with correct cpe + cpi combinations

### B3 — Steel sheeting ELS combination (BLOCKING)

**Problem:** ELS characteristic combination missing ψ0,snow = 0.5 factor. Sheeting likely undersized.

**Exigence:** EN 1990 Table A1.1 | **Responsible:** BEM

**Closure requires:** Revised sheeting design with G_k + 0.5 × Q_k,snow ELS combination

### B4 — Section change HEA 160/UPN 160 (BLOCKING)

**Problem:** Original TUC Rail design: IPE 240 + UPN 240. BEM revised to HEA 160 + UPN 160. Lcr inconsistent. Section adequacy not justified.

**Exigence:** EN 1993-1-1 | **Responsible:** BEM

**Closure requires:** Revised section verification (bending, shear, buckling, Lcr consistency) OR revert to original IPE 240/UPN 240

### B5 — Auvent structural note missing (BLOCKING)

**Problem:** Infrabel-requested canopy between B02 and TFO. Structural note not received.

**Responsible:** BEM + Raphaëlle (drawings)

**Closure requires:** Auvent structural note + revised architectural detail drawing

### B6 — Wind load qp reference note (BLOCKING)

**Problem:** Wind load reference note qp = 670 N/m² (22/12/2025) referenced but not provided.

**Responsible:** BEM

**Closure requires:** BEM to provide note (verify 670 N/m² is correct for site + building height)

---

## Domain C: Bardage B03

### C1 — SKR8100 edge/cmin calculation (BLOCKING)

**Problem:** WKF120 bracket + SKR8100 anchor edge conditions (rim-of-slab, ring beam) require project-specific supplementary calculation. Committed by Charpente Habitat 04/05/2026 — not delivered.

**Exigence:** CSC, ETA 20/0363 | **Responsible:** Charpente Habitat / BEM

**Closure requires:** Supplementary calculation note for SKR8100 edge/cmin on RC rim-of-slab & ring beam

### C2 — EXE plans (ventilation, downpipes) (BLOCKING)

**Problem:** Not addressed in Charpente Habitat response 04/05/2026.

**Responsible:** Charpente Habitat

**Closure requires:** EXE plans issued for ventilation grilles & downpipes

### C3 — FT 36 Roosens signed datasheet (BLOCKING)

**Problem:** Not addressed in Charpente Habitat response 04/05/2026.

**Responsible:** Charpente Habitat

**Closure requires:** Signed FT 36 datasheet (Roosens cellular concrete blocks)

---

## Master Closure Checklist

1. [ ] Obtain final geotechnical report (Els Voet) → enables A5
2. [ ] BEM revise S13 (radiers A1–A6)
3. [ ] Nicolas finalize S18 reply (TFO B1–B6 direction)
4. [ ] BEM issue TFO auvent note + revised TFO design (B1–B5)
5. [ ] Charpente Habitat issue SKR8100 calc + EXE plans + FT 36 (C1–C3)
6. [ ] DW provide steel certificates (A1) + cover survey (A3) + concrete cube reports (A3)
7. [ ] Raphaëlle coordinate auvent detail drawing + décompte
8. [ ] Final review & approval of all as-built documentation

---

Links: [[00 — Overview]] · [[02 — Document Register]] · [[05 — Journal]]
