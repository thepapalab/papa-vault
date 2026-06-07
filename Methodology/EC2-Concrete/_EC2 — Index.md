---
title: EC2 — Index
type: index
domain: Concrete
eurocode: EC2
status: living
created: 2026-06-02
---

# EC2 — Index

Domain index for Eurocode 2 (concrete). Sits under [[_Knowledge — Index]]. Section-design methodology for reinforced concrete under the EC2 ULS framework with Belgian NBN annexes and Infrabel PTR CE01.

## Methodology notes

**Combined bending + axial force**
- [[M-N interaction diagram — methodology]] — *draft; implementation internal-validated*. Strain-domain sweep (five EC2 domains), parabola-rectangle concrete + bilinear steel, (N,M) couples about mid-height. Closed envelope including hogging (= sagging of the section reflected about mid-height); verification by containment. Asymmetric reinforcement supported. External cross-check pending.

## Reference material

- [[_EC2-Seminar — Index]] — Greek-language EC2 seminar slides (Penelis / Kappos, Α.Π.Θ., 2009), converted to Markdown with rendered page images. Commentary/teaching material spanning chapters 1–7 and Part 2 (bridges); not a binding norm extract.

## Related Formulas

- [[EC2 — ULS material design values]] — partial factors, f_cd (α_cc **open**), concrete strain limits, f_yd, E_s, ε_y, ε_ud, and the two constitutive laws. Cited source-of-truth for the methodology above.

## Open threads / gaps noted

- **α_cc (f_cd) unresolved.** EC2 recommends 1.0; the working script uses 0.85 with unverified provenance. The governing value (NBN EN 1992-1-1 ANB / PTR CE01) must be confirmed before any number from the M-N module is used. Tracked in the Formulas unit.
- **No worked example yet.** Once an asymmetric section is cross-checked against SCIA, capture it under `Worked-Examples/` and lift the methodology maturity from predesign.
- **Shear interaction** (V-N-M, struts/ties) is a separate check, not covered by the interaction diagram — its own methodology note when needed.

---

Links: [[_Knowledge — Index]] · [[CLAUDE]]
