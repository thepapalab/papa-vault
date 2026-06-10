---
title: 06 — Technical Reviews
project: P101581 Boitsfort Bardage
project_number: P101581
location: Boitsfort (Brussels), Station, Line 161
phase: suivi d'exécution
role: Ingénieur structures — revue technique bardage ventilé
client: Infrabel
contractor: Equans / De Raedt Ivan / Etanco-Marcovis
status: active
tags: [P101581, boitsfort, technical, review, bardage, findings, TF-2100]
updated: 2026-06-04
---

# P101581 — Technical Reviews

Engineering content: design phases, technical findings analysis, review decisions with reasoning.

---

## Project Background

**Scope:** Ventilated timber cladding (Marcovis Eisys A4 screw system + lattage 70×45 C18 + MORA cladding 21 mm) on 11 emergency-exit buildings (*bâtiments de sortie d'urgence*) above the covered trench: NU2–NU8, LS-lokaal A + battery, MS-lokaal A, LS-lokaal B + battery, MS-lokaal B. Pilot: NU5.

**Fixing system:** Marcovis Eisys A4 façade screws in FM-X3 10/10×80 plugs anchored in AAC (*cellenbetonblokken*) at 80 mm embedment above the trench.

**Contractor responsibility model:** Following Luttre P234403 precedent — external contractor (Equans) bears full design responsibility; TUC Rail T-STR reviews against CSC, PTR CE01, Eurocodes with Belgian NA.

---

## Phase 1: Project Handover & Initiation (October 2025)

Raphaëlle Ciuch takes over as dossier owner from Dimitri. Nicolas Papalabros brought in for structural review.

**Principle established:** Internal TUC Rail calculation notes will never be transmitted externally. Only PTR CE01, CSC, and Eurocodes are valid references in external correspondence.

---

## Phase 2: Initial Submissions & Section Change (March–May 2026)

### 11/03/2026 — UP-4044 v2.0 (execution procedure)

References multiple TF documents not yet provided. Procedure structure received; supporting TFs outstanding.

### 04/05/2026 — Critical Hermes submissions (TF-2100 v4.0, TF-2101 v2.0)

**TF-2100 v4.0** — Marcovis Eisys A4 screw system on new 70×45 mm section (vs. prior 35×46 mm v3.0). Includes embedded Marcovis rekennota (Etanco template, dated 12/05/2025, generic 10×4×3 m building envelope), DIBt Z-9.1-897 (system approval), and pull-out test report DER 262602-1.

**TF-2101 v2.0** — Updated lattage specification: 70×45 mm C18 (Cras), ATG S143 Tanalith A3/S2, on-site bitumen coating Tenco Houtcoat.

### Primary Finding: Section Changed, Results Identical

Nicolas analyzes TF-2100 v4.0. Key finding:

> **Section changed from 35×46 to 70×45 mm, yet all utilization ratios remain identical.** The calculation note was not recomputed.

Section area: +96%. Moment of inertia: +86%. Self-weight: +16%. UR_flex = 0.86 (unchanged). UR_shear = 0.94 (unchanged). M_d/(W·f_m,d) = 283/317 (unchanged).

**This is the primary blocking argument** — not a technical opinion, but a factual defect in the submission itself.

---

## Phase 3: Works Stoppage (April 2026)

NC03 non-conformité (Remco Desmet/CCM) on first buildings (NU5 pilot):
- Latte-to-insulation distances > 5 mm (CSC requires ≤ 5 mm)
- Enduit incomplete before cladding placement
- Holes placed randomly
- Screws hammered instead of screwed (pre-drilling required, CSC §07.04.15)

Works stopped. **NC03 addresses workmanship; structural calculation deficiencies are separate ground.**

---

## Phase 4: Technical Review — Findings A–F (June 2026)

### Finding A — Un-recomputed verification (BLOCKING)

**Problem:** Section change 35×46 → 70×45 mm, +96% area, +86% inertia, +16% self-weight. All utilization ratios remain identical. Calculation not recomputed.

**Contractual basis:** PTR CE01, CSC §07.04.10 (preliminary structural stability calculations required).

**Why it is blocking:** A calculation note in which results do not change when inputs change is not a structural verification — it is a template with unchanged placeholder values. The contractor cannot claim compliance with this document.

**Closure requires:** Full recomputation of TF-2100 v4.1 for 70×45 mm section (new resistance, deflections, UR).

### Finding B — Incomplete wind methodology (BLOCKING)

**Problem:** Marcovis rekennota gives single forfaitaire value 67.5 daN/m² without qp(z), cpe (zones A–E), cpi derivation.

**Contractual basis:** EN 1991-1-4 (Belgian NA) + CSC TA 5.07.04 §07.04.10.

**Why it is blocking:** The design wind pressure on cladding is w = qp × [cpe + cpi], where cpe varies by zone (worst at corners/edges, fig. 7.11). A single value without zone analysis cannot demonstrate adequacy for all building locations and heights.

**Closure requires:** Separate wind document per building height with qp(z) derivation, cpe zones (A–E), worst-case net pressure, plug resistance vs. worst-case net pressure.

### Finding C — Non-representative pull-out test (BLOCKING)

**Problem:** Test DER 262602-1 at 70 mm embedment in concrete (grade unknown). Design: 80 mm embedment in AAC (type unknown). Test → N_Rd,s = 846 N (84.6 daN). Design value cited as 80 daN (source unclear).

**Why it is blocking:** Both the embedment depth (70 ≠ 80 mm) and the substrate (concrete ≠ AAC) differ. AAC is weaker than concrete in pull-out — a test in concrete cannot conservatively bound a design in AAC.

**Closure requires:** Option A (retest at 80 mm in AAC), Option B (supplementary calculation with as-built AAC class confirmed), or Option C (justification that test conservatively bounds design — highly unlikely).

### Finding D — Missing SLS verification (BLOCKING)

**Problem:** No treatment of eccentricity (75 mm keper-to-wall offset = moment on plug), no horizontal deflection, no ULS/SLS split.

**Why it is blocking:** EN 1995-1-1 requires SLS verification separate from ULS. The 75 mm offset creates a moment at the plug connection; horizontal wind-induced sway must be bounded for the screw-plug engagement to remain functional.

**Closure requires:** Vertical deflection check, eccentricity moment treatment (M = F_wind × 75 mm), horizontal deflection (wind sway).

### Finding E — ETA 19/0245 missing (BLOCKING)

**Problem:** FM-X3 plug product approval absent from dossier. DIBt Z-9.1-897 cited in rekennota expired 23 July 2025.

**Why it is blocking:** PTR CE01 requires a valid technical approval for all components. An expired approval provides no valid basis for design resistance claims.

**Closure requires:** ETA 19/0245 provided and confirmed applicable to AAC at 80 mm embedment; system approval confirmed post-DIBt expiry.

### Finding F — Substrate grade unknown (BLOCKING)

**Problem:** Test substrate: concrete grade unspecified, age unspecified. Design substrate: AAC type unknown, compressive strength not documented.

**Why it is blocking:** Pull-out resistance is substrate-dependent. Without knowing the substrate quality at both test and design, no valid comparison is possible.

**Closure requires:** Concrete grade & age at test (DER 262602-1); AAC type & compressive strength (EN 12602) at all 11 buildings at fixation points.

---

## Argument Discipline Established (04/06/2026)

- Lead with finding A (primary, factual, unanswerable)
- Follow with contractual bases (CSC §07.04.10 / §07.04.15, PTR CE01)
- No coaching on remediation (burden stays with contractor)
- Frame as compliance verification, not technical debate

---

## Precedent: Luttre P234403

Same T-STR team (Raphaëlle, Nicolas, Claudio) — same approach: contractor-driven design, TUC Rail compliance review, formal memo structure, no internal calcs transmitted externally.

---

Links: [[Projects/101581 Boitsfort/00 — Overview]] · [[Projects/101581 Boitsfort/02 — Document Register]] · [[Projects/101581 Boitsfort/03 — Open Points]]
