---
title: 04 — Strategic Context
project: P234403 Luttre
project_number: P234403
location: Luttre (Wallonia)
phase: suivi d'exécution
role: Ingénieur structures — vérification as-built
client: Infrabel
contractor: DW (Dubois Dawance)
status: active
tags: [P234403, luttre, strategy, argument-discipline, kz, winkler, protocol]
updated: 2026-06-04
---

# P234403 — Strategic Context

## Contractor Responsibility Model

DW (Dubois Dawance) and BEM (Bureau d'Étude Mosan) bear **full responsibility** for as-built calculations and closing deficiencies. TUC Rail's original design (Nicolas Papalabros) is contractually binding on DW. TUC Rail conducts compliance review — not re-design.

**TUC Rail internal calculation notes are never transmitted externally.** Only CSC, PTR CE01, and Eurocodes are cited in formal correspondence.

---

## Argument Discipline

Same pattern as Boitsfort P101581:
1. Lead with contractual basis: CSC, PTR CE01, Eurocodes with Belgian NA — not internal TUC Rail opinions
2. No coaching on remediation — burden of proof on contractor
3. "Announced ≠ delivered" — track document commitments separately from actual receipt
4. Blocking items non-negotiable until resolved

---

## Winkler Coefficient (Kz) — Strategic Position

**BEM used Kz = 15,000 kN/m³.** This is unjustified by CPT data and overestimated by factor of 3–7.5.

**Structural consequence:**
- Moments scale as M ∝ Kz^0.25 (weak nonlinear dependency)
- Kz = 5,000 vs 15,000 kN/m³ → moment reduction ~30–40%
- **BEM's higher Kz is conservative** (safer side) — not unsafe, but unjustified

**Justified Kz range for Luttre soil (Vesic formula):** 2,000–5,000 kN/m³ per CPT profiles S55.6a, S55.6b (Els Voet preliminary study, Annexe_06).

**Strategic position:**
1. Do not coach BEM toward correct answer — require defensible derivation from CPT
2. BEM must cite explicit formula (Vesic 1978, Terzaghi, or equivalent)
3. If BEM insists on 15,000 kN/m³, require numerical Winkler sensitivity study proving conservative bound
4. Critical enabler: **final geotechnical report from Els Voet** — must be obtained

---

## TFO Wind Load — Tableau 7.3 vs 7.6

**EN 1991-1-4 distinction:**
- Tableau 7.3 (closed buildings): net pressure w = qp(z) × (cpe + cpi), cpi = ±0.2 to ±0.3
- Tableau 7.6 (open-sided structures): external pressure only

**TFO is an enclosed utility building → tableau 7.3 applies.** BEM used tableau 7.6 → underestimated outward pull on anchors. Bi-directional wind envelope (inward + outward) governs anchor design.

---

## TFO Demountable Roof — Design Intent Ambiguity

BEM structural drawings (figures 3.2.3, 3.3.3) show chemical anchors for purlins as **permanent** connections. No demountable zone plan or disassembly sequence provided.

**Strategic position:** Require BEM to either:
- Provide detailed demountable zone plan (which connections are removable, disassembly sequence, temporary support), OR
- Confirm roof is permanent (anchors designed as permanent fixings)

Do not allow ambiguous middle ground.

---

## SKR8100 Anchor Edge Conditions

WKF120 bracket + SKR8100 anchor works in solid RC slab field conditions (ETA 20/0363 covers standard cases). **Edge conditions are different:** rim-of-slab and ring beam configurations require project-specific supplementary calculation. Charpente Habitat committed but has not delivered (announced-but-not-delivered).

---

## Communication Protocol

**Primary route:** Raphaëlle Ciuch (dossier owner) as intermediary — Nicolas drafts technical opinion as internal memo; Raphaëlle transmits to DW (Youssef Sridi); DW/BEM respond; Raphaëlle relays back to Nicolas.

**Site communications (Claudio Lamotta):** Concise, action-list format. Field verification: cover measurements, concrete class, workmanship inspection.

**Escalation:** François Lapy (T-STR management) — only if Raphaëlle explicitly requests.

**Tone & register:** Formal responses (S16, S18) structured, numbered, non-confrontational. Internal with Raphaëlle: direct, conversational, French. Field: action-oriented.

---

## Normative Framework

| Standard | Scope |
|----------|-------|
| EN 1990 (EC0) + Belgian NA | Load combinations, partial factors |
| EN 1992-1-1 (EC2) + Belgian NA | Concrete design — rafts, ring beams |
| EN 1993-1-1 (EC3) + Belgian NA | Steel design — TFO purlins |
| EN 1991-1-4 + Belgian NA | Wind loading |
| PTR CE01 | Infrabel standard: fyk ≤ 400 MPa, cnom = 45 mm |
| CSC P234403 | Tender spec — contractual reference |
| ETA 20/0363 | WKF120 bracket (bardage system) |
| EOTA TR 029 | Pull-out testing method |

---

Links: [[00 — Overview]] · [[03 — Open Points]]
