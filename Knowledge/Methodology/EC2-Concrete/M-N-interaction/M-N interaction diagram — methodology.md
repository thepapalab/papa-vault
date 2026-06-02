---
title: M-N interaction diagram — methodology
eurocode: EC2
domain: Concrete
check_type: ULS — combined bending and axial force (resistance domain)
method: Strain-domain sweep (five EC2 domains); parabola-rectangle concrete + bilinear steel; (N,M) couples taken about the geometric mid-height; closed envelope, hogging = sagging of the section reflected about mid-height
groundwater: n/a
status: draft
maturity: method standard; implementation internal-validated, external cross-check pending
tags: [methodology, EC2/concrete, ULS, M-N-interaction, interaction-diagram, axial-bending]
related: ["[[EC2 — ULS material design values]]", "[[_EC2 — Index]]", "[[_Knowledge — Index]]"]
script: eurocode-lib — EC2 M-N interaction module (thepapalab/eurocode-lib). Not hosted in the vault (CLAUDE.md §6 — algorithm with control flow).
validation: axial caps vs closed-form OK (tension ΣAs·f_yd; compression f_cd·b·h + ΣAs·f_yd); symmetric hogging branch mirrors sagging to zero residual; independent cross-check (SCIA section check) pending
created: 2026-06-02
---

# M-N interaction diagram — methodology

> [!abstract] One line
> Builds the **resistance envelope** of a rectangular reinforced-concrete section under combined axial force and uniaxial bending, following the EC2 ULS strain-compatibility method. Every point on the curve is an (N, M) couple that brings the section to failure; a design demand is verified by lying inside the closed envelope. Material design values are deferred to [[EC2 — ULS material design values]].

> [!info] Pure methodology
> This note is the general method, independent of any one section or script. It produces no numbers itself .Numerical design values (γ, α_cc, strain limits, f_yk cap) are not restated here; they are the cited Formulas unit linked above.

---

## 1. Objective and governing idea

A section under an axial force N and a bending moment M fails when its strain profile reaches a material limit (concrete crushing or steel exhausted). Because concrete carries no tension, the part of the section that resists depends on where the neutral axis sits, so the resistance is not a single pair but a **locus** of (N, M) couples — the interaction envelope. The ULS criterion is `S_d ≤ R_d`: the demand (N_Ed, M_Ed) must fall inside that locus.

The envelope is traced by sweeping every failure strain profile, computing the internal forces it generates, and reducing them to one (N, M) couple per profile.

---

## 2. Conventions

- Tensile force and strain **positive**; compressive **negative**.
- Bending moment **positive (sagging)** when it stretches the bottom fibre.
- Neutral-axis depth `y_n` measured from the **top face**, downward positive.
- Internal forces are reduced to the **section geometric centroid (mid-height, h/2)**.

> [!important] Reference axis — must match the demand
> Moments are taken about the geometric centroid of the concrete, which for a rectangular section is always mid-height, irrespective of reinforcement asymmetry. The envelope is therefore exact — **provided the demand (N_Ed, M_Ed) is referenced to the same axis.** This is a deliberate choice of reference axis, not an approximation of the plastic-centroid offset. Confirm the FE model reports section forces at the geometric centre (SCIA does for a rectangular member); a demand referenced to a different axis cannot be read against this diagram.

---

## 3. Assumptions

1. Plane sections remain plane (shear deformation ignored).
2. Perfect bond — steel strain equals the adjacent concrete strain.
3. Concrete in tension contributes nothing to resistance.
4. Material partial factors are embedded in f_cd and f_yd; the envelope is a **design-resistance** envelope.
5. Rectangular cross-section, two reinforcement layers (top and bottom).

---

## 4. Constitutive laws (shape only — values in the Formulas unit)

- **Concrete:** parabola-rectangle law — a parabolic branch from zero to ε_c2, then a constant plateau at −f_cd to ε_cu2. Compression negative. EC2 §3.1.7, Fig. 3.3.
- **Steel:** bilinear, horizontal top branch at ±f_yd beyond the yield strain ε_y, design strain capped at the adopted ε_ud. EC2 §3.2.7, Fig. 3.8.

The numerical parameters (f_cd, f_yd, ε_c2, ε_cu2, ε_y, ε_ud, and their validity range) are the cited Formulas unit [[EC2 — ULS material design values]].

---

## 5. The five strain domains

The failure profiles are partitioned into five domains by which material governs and where the neutral axis lies. Coordinate from the top face, downward positive.

- **Domain I — whole section in tension.** Neutral axis above the section; the bottom (tension) steel is pinned at ε_ud. Concrete contributes nothing. Spans pure tension toward the first appearance of compression.
- **Domain II — neutral axis enters the section.** Pivot between the bottom steel at ε_ud and the top concrete fibre reaching ε_cu2. Part of the section is now in compression.
- **Domain III — concrete-controlled, steel yielding.** Top fibre fixed at ε_cu2; the neutral axis descends until the bottom steel reaches its yield strain ε_y.
- **Domain IV — concrete-controlled, steel below yield.** Top fibre at ε_cu2; neutral axis travels down to the bottom face.
- **Domain V — whole section in compression.** Neutral axis below the section; the strain profile rotates about the pivot where ε = ε_c2, located at `3/7·h` from the most-compressed face (3/7 = 1 − ε_c2/ε_cu2 for f_ck ≤ 50 MPa). Spans toward pure compression.

---

## 6. Constructing one (N, M) point

For an assumed neutral-axis position within a domain:

1. Build the **linear strain profile** from the domain's pivot.
2. Map strains to **stresses** through the two constitutive laws.
3. **Integrate the concrete compression block** over its depth → resultant N_c and its line of action y_Gc.
4. Add the two **steel forces** A_s,i·σ_s,i (each at its own depth y_i — the layers need not be symmetric).
5. Reduce to a couple about mid-height, every force carrying its sign:

$$N_{Rd}=N_c+\sum_i A_{s,i}\,\sigma_{s,i}$$
$$M_{Rd}=N_c\left(y_{Gc}-\tfrac{h}{2}\right)+\sum_i A_{s,i}\,\sigma_{s,i}\left(y_i-\tfrac{h}{2}\right)$$

Sweeping the neutral axis across all five domains traces one continuous half of the envelope.

> [!note] Asymmetric reinforcement
> The single moment expression above places each steel layer at its true depth y_i, so unequal top/bottom area **and** unequal cover are handled directly. For equal cover it reduces to the familiar `+A_s1·σ_s1·(h/2−c) − A_s2·σ_s2·(h/2−c)`.

---

## 7. Positive and negative bending — the closed envelope

The construction above (tension on the bottom layer) gives the **sagging** branch, M ≥ 0. The **hogging** branch is the same construction applied to the section **reflected about mid-height** (the two reinforcement layers swapped), with the resulting moment negated. The axial response is unchanged by the reflection.

- For **symmetric** reinforcement the hogging branch is the exact mirror of the sagging branch.
- For **asymmetric** reinforcement the two branches differ, and both are needed.

The two branches share the pure-tension and pure-compression caps, so together they form a single **closed domain** in the (N, M) plane.

---

## 8. Verification

A demand (N_Ed, M_Ed), referenced to mid-height, is satisfied when it lies **inside the closed domain**. For a given axial force there are generally **two** moment capacities — one sagging, one hogging — so the relevant capacity is the one on the side of the demand's moment sign. Reading a single capacity per axial level by nearest-point lookup is unsafe near the envelope's noses, where the curve folds; containment in the closed domain is the robust test.

---

## 9. Validation status

- **Method:** standard EC2 strain-compatibility; no open theoretical items.
- **Implementation (eurocode-lib EC2 module):** axial caps reproduce the closed-form values (pure tension ΣA_s·f_yd; pure compression f_cd·b·h + ΣA_s·f_yd); for symmetric reinforcement the hogging branch mirrors the sagging branch to zero residual.
- **Open:** no cross-check yet against an independent tool (e.g. a SCIA section check) on an asymmetric section. Treat as predesign until that anchor exists.

---

## 10. Standards and basis

- **Constitutive laws:** EN 1992-1-1 §3.1.7 (concrete, parabola-rectangle, Fig. 3.3) and §3.2.7 (reinforcement, bilinear, Fig. 3.8).
- **Concrete strain limits:** EN 1992-1-1 Table 3.1 (constant for f_ck ≤ 50 MPa; reduce above).
- **Design strengths and partial factors:** [[EC2 — ULS material design values]] (f_cd, f_yd, γ_c, γ_s; α_cc per annex; f_yk ≤ 400 MPa per Infrabel PTR CE01).
- **Framework:** Eurocodes with Belgian NBN annexes; Infrabel PTR CE01 where applicable.

---

## 11. Status / next step

Methodology captured. Implementation exists in `eurocode-lib`; next anchor is an independent cross-check on an asymmetric section before the diagram is used for validation work. The α_cc value feeding f_cd is an open item in the Formulas unit — see [[EC2 — ULS material design values]].

Links: [[EC2 — ULS material design values]] · [[_EC2 — Index]] · [[_Knowledge — Index]] · [[CLAUDE]]
