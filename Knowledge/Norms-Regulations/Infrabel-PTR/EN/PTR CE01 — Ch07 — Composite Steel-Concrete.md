---
title: PTR CE01 Ch07 — Composite Steel-Concrete
type: norm-extract
source: "PTR CE01 Fascicule 1 v1 (Avis 15 I-AM/2022)"
chapters: [7]
tags: [PTR CE01, Infrabel, composite, steel-concrete, preflex, shear-connection, EC4]
related: ["[[PTR CE01 — Index]]", "[[PTR CE01 — Ch05 — RC and Prestressed Concrete]]", "[[PTR CE01 — Ch06 — Steel]]", "[[_Knowledge — Index]]"]
created: 2026-06-02
---

# PTR CE01 Ch07 — Composite Steel-Concrete Structures

NBN EN 1994 applies unless derogated below. Chapters 5 and 6 fully apply to these structures.

---

## 7.1 Scope

Structures where both concrete and steel contribute to element resistance and act together through a strong interface. Steel may be rolled sections or welded/bolted built-up sections.

---

## 7.2 Section Classification

Per NBN EN 1994-2 §5.5. Two main classes of composite cross-section (see Figure 7.1 in PTR — one or both flanges partially or fully encased in concrete). Behaviour differs fundamentally between classes.

---

## 7.3 Standard Bridge Deck Concepts

### 7.3.1 Encased beam decks (*tabliers à poutres enrobées*)

Steel sections fully or partially encased in concrete. Natural adhesion between steel and concrete is relied upon under conditions of §6.3 of NBN EN 1994-2 (no shear connectors required when rules are met). Transverse reinforcement and threaded rods ensure transverse continuity at the web level.

**Steel section holes** for transverse bars: must be positioned high enough that stresses at SLS ≤ **f_yk / 3** (stress concentration factor of 3 around hole).

Threaded rods spacing: approximately L/4, minimum 3 m.

**Minimum transverse reinforcement (lower zone):** 3 bars × φ16 per metre over the full deck area.
**Upper zone:** minimum half the lower reinforcement, with minimum 5 bars × φ10 per metre.

### 7.3.2 Pre-flexed and prestressed beam decks (*poutres préfléchies et précontraintes*)

Applies to steel beams where at least the bottom flange is encased in concrete in the factory (Phase 1 concrete). The steel beam is loaded in bending (pre-flexed) or combined bending (prestressed) during concreting. After concrete hardening (minimum C35/45), the force is released, inducing compression in the concrete.

**Steel grade:** minimum **S355J2** (high ductility required).

**Pre-flexion forces:** applied at L/4 from the nearest support on a simply-supported beam. Do not contribute to ULS resistance.

**Execution phases (Table 7.1):**
1. Elastification of steel beam (residual stress elimination; load to ≥ SLS stress level, repeated until Δdeflection < 3% between cycles).
2. Pre-flexion with two point loads.
3. Phase 1 concreting (bottom flange — includes bonded prestressing strands).
4. Release of pre-flexion and cutting of strands → compression introduced into concrete.
5. Phase 2 concreting (if post-tensioned: fully supported so Phase 2 concrete weight does not load the beam).
6. Post-tensioning of Phase 2 cables → beam lifts off formwork, rests on final supports.
7. Final phase concreting: compression slab on top; passive reinforcement required in Phase 2 concrete in tension zone.

**Anti-buckling precautions during elastification:** minimum 3 lateral restraint forks; check web buckling under concentrated forces; add transverse stiffeners if needed.

**Winter precautions for cable grouting (01 Nov – 15 Mar):** before grouting, flush with compressed air then fill with non-corrosive antifreeze fluid (freeze point < −20°C). Before final grouting, remove fluid with compressed air. Alternatively, maintain concrete at ≥ 5°C throughout grouting and hardening, or use antifreeze admixture. All measures require prior approval.

**Typical application: preflex or "pont en auge"** — fully prefabricated trough deck ≈ 4 m wide (rail gauge clearance). The Phase 1 concrete at the bottom flange must remain permanently in compression in service to contribute to section resistance and ensure durability.

---

## 7.4 Project Elaboration

### 7.4.1 ULS

Chapters 5 and 6 apply.

### 7.4.2 SLS

Elastic calculation method with corrections for non-linear effects (concrete cracking) using homogenised sections. Equivalent modular ratio:

$$n_L = n_0 (1 + \psi \cdot \varphi)$$

where:
- n₀ = E_a / E_cm (short-term modular ratio)
- φ = creep coefficient of concrete
- ψ = reduction coefficient depending on A_s/A_c (ratio of steel area in the considered flange to net concrete area of the same flange)

**Simplified ψ values (t → ∞, exterior exposure):**

| A_s/A_c | ψ |
|---|---|
| 0.03 | 1.25 |
| 0.05 | 1.00 |
| ≥ 0.10 | 0.65 |

(Linear interpolation for intermediate values.)

**Pre-flexion stress limits:**
- Steel: σ ≤ **0.75 f_yk** during pre-flexion.
- Concrete at release: σ_c ≤ **0.8 f_ck** at the relevant concrete age (to limit cracking).

---

## 7.5 Steel-Concrete Interface

### 7.5.1 Shear connectors

Natural adhesion is neglected. Longitudinal shear must be explicitly transferred by connectors + transverse reinforcement.

**Ductile connectors (headed studs):** diameter d ≤ 22 mm, height ≥ 4d. Ductility condition: minimum degree of connection must be met. Fatigue verification per NBN EN 1994-2 §6.8.

**Rigid connectors:** Very stiff behaviour — treated as brittle. Design resistance:

$$V_{Rd} = \eta \cdot A_{f1} \cdot f_{ck} / \gamma_c$$

where A_f1 = front face area (Figure 7.5); η = A_f2/A_f1 ≤ 2.5 (normal concrete) or 2.0 (lightweight), A_f2 = projected area with 1:5 slope on rear face.

Welds for rigid connectors sized to resist **1.2 V_Rd**.

### 7.5.2 Degree of shear connection

Full connection: additional connectors beyond N_f do not increase M_Rd (steel-concrete composite resistance governs before interface capacity).

Partial connection degree: η = N/N_f, where N_f = connectors for full M_Rd and N = connectors actually provided.

Partial connection only allowed within limits of Figure 7.6 (ensures connector ductility and minimum connection degree).

All connections verified at ULS.

---

Links: [[PTR CE01 — Index]] · [[PTR CE01 — Ch05 — RC and Prestressed Concrete]] · [[PTR CE01 — Ch06 — Steel]] · [[PTR CE01 — Ch09 — SLS]] · [[_Knowledge — Index]]
