---
title: 04 — Strategic Context
project: P101581 Boitsfort Bardage
project_number: P101581
location: Boitsfort (Brussels), Station, Line 161
phase: suivi d'exécution
role: Ingénieur structures — revue technique bardage ventilé
client: Infrabel
contractor: Equans / De Raedt Ivan / Etanco-Marcovis
status: active
tags: [P101581, boitsfort, strategy, argument-discipline, protocol]
updated: 2026-06-04
---

# P101581 — Strategic Context

## Contractor Responsibility Model

Equans bears **full design accountability** (PTR CE01). TUC Rail T-STR reviews for compliance against CSC, PTR CE01, and Eurocodes with Belgian NA. TUC Rail does not co-design remediation.

**TUC Rail internal calculation notes are never transmitted externally.** Only PTR CE01, CSC, and Eurocodes are cited in formal correspondence.

---

## Argument Discipline

### Lead with the strongest, most objectively defensible argument

Finding A (un-recomputed calculation) is the primary blocking point because it is **factual and unanswerable** — not a technical opinion, but a calculation state fact: section changed, results identical, calculation was not recomputed.

### Contractual argument before technical debate

When both a contractual hook (CSC / PTR CE01) and a technical classification debate are available, lead with the contractual hook to avoid unnecessary disputes.

### No coaching on remediation

Standing formulation: *"the submitted calculation note does not constitute a valid structural verification for the approved configuration"* — not *"the calculation note was absent."* Do not detail a path to the correct answer — that risks shifting design responsibility to TUC Rail.

### Category of framing

Deficiencies are presented as **compliance requirements per CSC / PTR CE01**, not technical preferences.

---

## "Announced ≠ Delivered"

Track document commitments separately from actual delivery. See [[Projects/101581 Boitsfort/02 — Document Register]] / "Announced ≠ Delivered" tracker.

---

## Technical Vigilance Points

### Manufacturer template notes — invalid if results don't move with inputs

Marcovis rekennota is an Etanco generic template (dated 12/05/2025, hardcoded 10×4×3 m). Section change v3.0 → v4.0 (35×46 → 70×45 mm): all utilization ratios remain identical despite section area +96%, moment of inertia +86%, self-weight +16%. **Calculation was not recomputed.**

### Test embedment must match design embedment

Pull-out test DER 262602-1: 70 mm embedment in concrete (grade unknown). Design: 80 mm embedment in AAC (type unknown). Test is not representative. Both the support-side capacity and plug-side capacity must be checked against their respective design embedments.

### Wind methodology baseline (EN 1991-1-4 + Belgian NA)

- Boitsfort parameters: Terrain category III (suburbs), vb,0 = 25 m/s (Belgium), building height ~3–4 m
- Method: qp(z) per EN 1991-1-4 → zone-specific cpe (A–E per fig. 7.11) combined with worst-case cpi → net cladding pressure w = qp × [cpe + cpi]
- The Buildwise table value 0.675 kN/m² (67.5 daN/m²) is plausible as qp(z) for similar low buildings but is **not** the design wind on cladding — it is only qp(z). Single forfaitaire pressures unacceptable per CSC TA 5.07.04 §07.04.10.
- Working reference: EN1991-1-4.xlsx spreadsheet (with cpi sign convention fix: `cpi = IF(cpe < 0; cpi_max; cpi_min)`) — not transmitted externally.

### Stainless steel discipline

- Marcovis Eisys A4 screw → OK (primary fixation, exposed)
- Friulsider VBU-PRO INOX 4.5×60 A2-50 (AISI 304) → acceptable for lath-to-keper secondary fixings in ventilated cavity

---

## Communication Protocol

### External correspondence (Equans / De Raedt / Etanco)

**Primary route:** Raphaëlle Ciuch as intermediary — Nicolas drafts technical opinion as internal memo; Raphaëlle reviews and transmits to Equans (Tim Witvoet); Raphaëlle relays Equans response to Nicolas.

**Escalation:** François Lapy (T-STR management) — only if Raphaëlle explicitly requests.

**Direct contact rule:** Prohibited unless Raphaëlle explicitly requests. All technical issues routed through Equans project lead.

### Site communications (Raphaël Verraghen)

Concise, action-list format. Topics: concrete verification, AAC specification, as-built dimensions, workmanship inspection.

### Tone & register

- **Formal Hermes responses:** Structured, numbered, non-confrontational, framed as compliance requirements per CSC / PTR CE01
- **Internal discussion with Raphaëlle:** Direct, conversational, French
- **Field communications:** Conversational, action-oriented, Dutch or French

---

## Normative Framework

| Standard | Scope |
|----------|-------|
| EN 1991-1-4 (Belgian NA) | Wind loading |
| EN 1995-1-1 (Belgian NA) | Timber design |
| EN 12602 | AAC design |
| EN 14081-1 | Structural timber grading |
| EN 14915 | Solid wood cladding |
| EN 14592 | Self-driving wood screws |
| CSC TA 5.07.04 §07.04.10 / §07.04.15 | Cladding requirements (contractual) |
| PTR CE01 | Infrabel design standard (contractual) |
| STS 04.1 / 04.2 / 04.3 | Timber grading & treatment |
| TVN/NIT 243 / 247 | Wood protection & ventilation reference |
| ETA 19/0245 | FM-X3 plug product approval (missing from dossier) |
| DIBt Z-9.1-897 | Marcovis Eisys system (expired 23 July 2025) |

---

Links: [[Projects/101581 Boitsfort/00 — Overview]] · [[Projects/101581 Boitsfort/03 — Open Points]]
