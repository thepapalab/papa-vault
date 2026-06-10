---
title: 03 — Open Points
project: P101581 Boitsfort Bardage
project_number: P101581
location: Boitsfort (Brussels), Station, Line 161
phase: suivi d'exécution
role: Ingénieur structures — revue technique bardage ventilé
client: Infrabel
contractor: Equans / De Raedt Ivan / Etanco-Marcovis
status: active
tags:
  - P101581
  - boitsfort
  - blocages
  - NC
  - issues
updated: 2026-06-09
---

# P101581 — Open Points


## Summary

| ID | Type | Responsible | Status |
|----|------|-------------|--------|
| **A** | Un-recomputed verification | Equans | BLOCKING |
| **B** | Wind methodology incomplete | Equans | BLOCKING |
| **C** | Pull-out test non-representative | Equans/De Raedt/Etanco | BLOCKING |
| **D** | SLS verification missing | Equans | BLOCKING |
| **E** | ETA 19/0245 absent | Etanco/Equans | BLOCKING |
| **F** | Substrate grade unknown | Equans/Raphaël Verraghen | BLOCKING |
| **G** | TF-022 vD alignment (internal, De Raedt) | De Raedt | NON-BLOCKING |
| **H** | Project-specific Marcovis NdC — clarification needed | Equans/Etanco | NON-BLOCKING |
| **I** | Gevelfolie perforations at NU5 — re-waterproofing | Equans/De Raedt | OPEN (raised by Equans) |
| **J** | Druipneus above ventilation grilles | Equans/De Raedt | OPEN (raised by Equans) |
| **NC03** | Workmanship non-conformities | Equans/De Raedt | BLOCKING |

---

## Structural Blocages (Technical Review Nicolas)

### A — Un-recomputed verification (BLOCKING)

**Problem:** TF-2100 v3.0 → v4.0 (35×46 → 70×45 mm). Section area +96%, moment of inertia +86%, self-weight +16%. All utilization ratios remain identical: UR_flex 0.86, UR_shear 0.94, M_d/(W·f_m,d) 283/317. Calculation was not recomputed.

**Exigence:** PTR CE01, CSC §07.04.10

**Responsible:** Equans (Tim Witvoet) | **Deadline:** TBD

**Closure requires:** Full recomputation TF-2100 v4.1 for 70×45 section (new resistances, deflections, UR)

---

### B — Wind methodology incomplete (BLOCKING)

**Problem:** Single forfaitaire value 67.5 daN/m² without qp(z), cpe (zones A–E), cpi derivation per EN 1991-1-4 fig. 7.11.

**Exigence:** EN 1991-1-4 (Belgian NA) + CSC TA 5.07.04 §07.04.10

**Responsible:** Equans | **Deadline:** TBD

**Closure requires:** Separate wind document per building height with qp(z), cpe zones (A–E), worst-case net pressure w = qp × [cpe + cpi]; plug resistance verified against worst-case net pressure.

---

### C — Pull-out test non-representative (BLOCKING)

**Problem:** Test DER 262602-1: 70 mm embedment in concrete (grade unknown). Design: 80 mm embedment in AAC (type unknown). Both embedment depth and substrate differ.

**Exigence:** CSC §07.04.15, ETA 19/0245, PTR CE01

**Responsible:** Equans / De Raedt / Etanco | **Deadline:** TBD

**Closure requires:** Option A — retest FM-X3 at 80 mm in AAC (type documented), OR Option B — supplementary calculation justifying capacity at 80 mm in AAC per as-built substrate documentation + ETA 19/0245 scope confirmation.

---

### D — SLS verification missing (BLOCKING)

**Problem:** No eccentricity treatment (75 mm keper-to-wall offset = moment on plug), no horizontal deflection, no proper ULS/SLS split. Only declaration "2 mm vertical deflection acceptable" without derivation.

**Exigence:** EN 1995-1-1, PTR CE01

**Responsible:** Equans | **Deadline:** TBD

**Closure requires:** Vertical deflection check; eccentricity moment treatment (M = F_wind × 75 mm offset) → keper compression stress, plug moment capacity; horizontal deflection (wind-induced sway).

---

### E — ETA 19/0245 absent (BLOCKING)

**Problem:** FM-X3 10/10×80 plug product approval absent. DIBt Z-9.1-897 cited in rekennota expired 23 July 2025.

**Exigence:** PTR CE01 (valid technical approval required for all components)

**Responsible:** Etanco / Equans | **Deadline:** TBD

**Closure requires:** ETA 19/0245 provided and confirmed applicable to AAC at 80 mm embedment; system approval confirmed post-DIBt expiry.

---

### F — Substrate grade unknown (BLOCKING)

**Problem:** Test substrate: concrete grade unspecified, age unknown. Design substrate: AAC type unknown, no compressive strength class documented.

**Exigence:** PTR CE01, CSC §07.04.15

**Responsible:** Equans / Raphaël Verraghen (GC field) | **Deadline:** TBD

**Closure requires:** Concrete grade & age at testing (DER 262602-1); AAC type & compressive strength (EN 12602) at all 11 buildings at fixation points; block thicknesses; confirmation design embedment (80 mm) achievable.

---

### G — TF-022 vD alignment (NON-BLOCKING)

**Problem:** De Raedt internal TF-022 vD still references old 35×46 mm section.

**Responsible:** De Raedt

**Closure requires:** TF-022 updated to align with TF-2101 v2.0 (70×45 section).

---

### H — Marcovis template vs. project-specific (NON-BLOCKING)

**Problem:** Rekennota embedded in TF-2100 v4.0 dated 12/05/2025 (generic Etanco template). Clarification: does project-specific NdC dated 12/05/2026 exist?

**Responsible:** Equans / Etanco

**Closure requires:** Confirmation whether revised project-specific NdC exists.

---

### I — Gevelfolie perforations at NU5 (OPEN — raised by Equans)

**Problem:** During the April workmanship issues the façade film (gevelfolie) at NU5 was perforated (random support holes). Equans (email 08/06/2026) acknowledges a technical solution is needed to make these perforations watertight again. Site / watertightness item, not a structural blocage, but tied to NC03 and to restart authorization.

**Exigence:** UP-4044 (watertightness of the façade film), CSC §07.04 ventilated-cavity build-up

**Responsible:** Equans / De Raedt

**Closure requires:** Technical proposal for re-sealing the gevelfolie perforations at NU5, to be reviewed before cladding is reinstated.

---

### J — Druipneus above ventilation grilles (OPEN — raised by Equans)

**Problem:** Equans (email 08/06/2026) proposes to provide a technical detail for a druipneus (drip edge) above the ventilation grilles. Detailing item to confirm water is shed clear of the grilles and the cavity.

**Exigence:** UP-4044 / detail drawings; CSC §07.04 ventilation provisions (perforated L-profile, 10 mm/m openings, insect mesh)

**Responsible:** Equans / De Raedt

**Closure requires:** Drip-edge detail above ventilation grilles submitted and checked against the ventilation/water-shedding requirements; to appear on the adapted gevelplannen / IP3371.

---

## Meeting Request (Equans, 08/06/2026)

Equans asked for a (preferably live) expert meeting to align on the remaining administration for TF-2100 and TF-2101, calling some remarks "buitensporig" (excessive). Proposed dates: 15/06 (≥10h), 18/06, 19/06.

- Raphaëlle: available all three; questions whether a visio is needed since the outstanding items are already written down.
- Nicolas: available 18/06 & 19/06; FR/EN only (translation needed if NL); position unchanged — remarks are CSC/Eurocode compliance requirements, not administrative formalities. Burden of proof stays with the contractor.

Date to be confirmed. See [[05 — Journal]] entry 09/06/2026.

---

## Workmanship Non-Conformity (NC03, April 2026)

**NC03 (Remco Desmet/CCM, transmitted by Raphaëlle, April 2026):**
- Latte-to-insulation distances > 5 mm (CSC requires ≤ 5 mm)
- Enduit (base coat) incomplete before cladding placement
- Fixation holes placed randomly (non-coordination)
- Screws hammered instead of properly screwed (pre-drilling required per CSC §07.04.15)

**Works stopped April 2026** on NU5 and subsequent buildings.

**Closure requires:**
- Revised workmanship procedure (Equans / De Raedt)
- Quality inspection (Raphaël Verraghen site follow-up)
- Compliance verification before restart authorization

---

Links: [[Projects/101581 Boitsfort/00 — Overview]] · [[Projects/101581 Boitsfort/02 — Document Register]] · [[05 — Journal]]