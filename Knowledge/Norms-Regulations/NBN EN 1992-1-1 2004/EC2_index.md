# EN 1992-1-1:2004 (F) — Eurocode 2: Design of concrete structures

**Document:** Eurocode 2, Part 1-1: General rules and rules for buildings  
**Language:** French  
**Status:** Processing — Sections 5, 9 & 10 processed (2024-06-03)

---

## Section Index

### Main Sections (Planned)

| Section | Title | File | Status |
|---------|-------|------|--------|
| 1 | Généralités | `EC2_1_generalites.md` | Pending |
| **2** | **Bases de calcul** | `EC2_2_bases-calcul.md` | **✅ Partial** |
| 3 | Matériaux | `EC2_3_materiaux.md` | Pending |
| 4 | Durabilité et enrobage des armatures | `EC2_4_durabilite-enrobage.md` | Pending |
| **5** | **Analyse structurale** | `EC2_5_analyse-structurale.md` | **✅ Partial** |
| 6 | États-limites ultimes (ELU) | `EC2_6_elu-etats-limites.md` | Pending |
| 7 | États-limites de service (ELS) | `EC2_7_els-etats-limites.md` | Pending |
| 8 | Dispositions constructives — armatures | `EC2_8_dispositions-armatures.md` | Pending |
| **9** | **Dispositions constructives — éléments** | `EC2_9_dispositions-elements.md` | **✅ Complete** |
| **10** | **Éléments et structures préfabriqués** | `EC2_10_elements-prefabriques.md` | **✅ Complete** |
| 11 | Béton de granulats légers | `EC2_11_beton-granulats-legers.md` | Pending |
| **12** | **Béton non armé ou faiblement armé** | `EC2_12_beton-non-arme.md` | **✅ Partial** |

### Annexes (Planned)

| Annex | Title | File | Type | Status |
|-------|-------|------|------|--------|
| A | Modification des coefficients partiels | `EC2_A_modification-coefficients.md` | Informative | Pending |
| B | Déformations — fluage et retrait | `EC2_B_deformations-fluage.md` | Informative | Pending |
| C | Propriétés des armatures | `EC2_C_proprietes-armatures.md` | Normative | Pending |
| D | Pertes de précontrainte — relaxation | `EC2_D_pertes-precontrainte.md` | Informative | Pending |
| E | Classes de résistance pour durabilité | `EC2_E_classes-resistance.md` | Informative | Pending |
| F | Expressions pour armatures tendues | `EC2_F_expressions-armatures.md` | Informative | Pending |
| G | Interaction sol-structure | `EC2_G_interaction-sol.md` | Informative | Pending |
| H | Effets globaux du second ordre | `EC2_H_effets-second-ordre.md` | Informative | Pending |
| I | Analyse des planchers-dalles et voiles | `EC2_I_analyse-planchers.md` | Informative | Pending |
| J | Dispositions constructives — cas particuliers | `EC2_J_dispositions-particuliers.md` | Informative | Pending |

---

## Processing Summary

**Sections completed:**
- **Section 2 (Bases de calcul):** 2.2–2.7 (Eq. none, Table 2.1N) — ✅ Partial
- **Section 5 (Analyse structurale):** 5.1–5.8.8.2 (Eq. 5.13N–5.34) — ⚠️ Partial
- **Section 9 (Dispositions constructives):** 9.1–9.10.3 (Eq. 9.1N–9.18, Table 9.6N) — ✅ Complete
- **Section 10 (Éléments préfabriqués):** 10.1–10.9.7 (Eq. 10.1–10.6, Tables 10.1–10.5) — ✅ Complete
- **Section 12 (Béton non armé):** 12.1–12.9.3 (Eq. 12.1–12.13, Table 12.1) — ✅ Partial

**Total equations extracted:** 50+ (2.1N, 5.13N–5.34, 9.1N–9.18, 10.1–10.6, 12.1–12.13)

**Figures referenced:** 9.1–9.15, 10.1–10.7, 12.1–12.2 (visual content omitted, noted in files)

**Tables extracted:** 2.1N, 9.6N, 10.1–10.5, 12.1 (partial safety factors, minimum reinforcement, bearing depths, tolerances, slenderness factors)

---

## Section 2 — Subsections Processed

| Subsection | Title | File | Status |
|------------|-------|------|--------|
| 2.2 | Principes du calcul aux états-limites | `EC2_2.2_principes-calcul-elu.md` | ✅ |
| 2.3 | Variables de base | `EC2_2.3_variables-base.md` | ✅ |
| 2.3.1 | Actions et influences de l'environnement | `EC2_2.3.1_actions-influences.md` | ✅ |
| 2.3.1.1 | Généralités (Actions) | `EC2_2.3.1.1_generalites-actions.md` | ✅ |
| 2.3.1.2 | Effets thermiques | `EC2_2.3.1.2_effets-thermiques.md` | ✅ |
| 2.3.1.3 | Tassements / mouvements différentiels | `EC2_2.3.1.3_tassements-mouvements.md` | ✅ |
| 2.3.1.4 | Précontrainte | `EC2_2.3.1.4_precontrainte.md` | ✅ |
| 2.3.2 | Propriétés des matériaux et produits | `EC2_2.3.2_proprietes-materiaux.md` | ✅ |
| 2.3.2.1 | Généralités (Matériaux) | `EC2_2.3.2.1_generalites-materiaux.md` | ✅ |
| 2.3.2.2 | Retrait et fluage | `EC2_2.3.2.2_retrait-fluage.md` | ✅ |
| 2.3.3 | Déformations du béton | `EC2_2.3.3_deformations-beton.md` | ✅ |
| 2.3.4 | Données géométriques | `EC2_2.3.4_donnees-geometriques.md` | ✅ |
| 2.3.4.1 | Généralités (Géométrie) | `EC2_2.3.4.1_generalites-geometrie.md` | ✅ |
| 2.3.4.2 | Exigences pieux coulés en place | `EC2_2.3.4.2_pieux-coules-place.md` | ✅ |
| 2.4 | Vérification par coefficients partiels | `EC2_2.4_verification-coefficients-partiels.md` | ✅ |
| 2.4.1 | Généralités (Vérification) | `EC2_2.4.1_generalites-verification.md` | ✅ |
| 2.4.2 | Valeurs de calcul | `EC2_2.4.2_valeurs-calcul.md` | ✅ |
| 2.4.2.1 | Coefficient partiel retrait | `EC2_2.4.2.1_coefficient-retrait.md` | ✅ |
| 2.4.2.2 | Coefficients partiels précontrainte | `EC2_2.4.2.2_coefficients-precontrainte.md` | ✅ |
| 2.4.2.3 | Coefficient partiel fatigue | `EC2_2.4.2.3_coefficient-fatigue.md` | ✅ |
| 2.4.2.4 | Coefficients partiels matériaux | `EC2_2.4.2.4_coefficients-materiaux.md` | ✅ |
| 2.4.2.5 | Coefficients partiels fondations | `EC2_2.4.2.5_coefficients-fondations.md` | ✅ |
| 2.4.3 | Combinaisons d'actions | `EC2_2.4.3_combinaisons-actions.md` | ✅ |
| 2.4.4 | Équilibre statique EQU | `EC2_2.4.4_equilibre-statique-equ.md` | ✅ |
| 2.5 | Dimensionnement assisté expérimentation | `EC2_2.5_dimensionnement-experience.md` | ✅ |
| 2.6 | Exigences complémentaires fondations | `EC2_2.6_exigences-fondations.md` | ✅ |
| 2.7 | Exigences relatives aux fixations | `EC2_2.7_exigences-fixations.md` | ✅ |

## Section 12 — Subsections Processed

| Subsection | Title | File | Status |
|------------|-------|------|--------|
| 12.1 | Généralités | `EC2_12.1_generalites.md` | ✅ |
| 12.3 | Matériaux | `EC2_12.3_materiaux.md` | ✅ |
| 12.3.1 | Béton : hypothèses de calcul complémentaires | `EC2_12.3.1_beton-hypotheses-calcul.md` | ✅ |
| 12.5 | Analyse structurale : états-limites ultimes | `EC2_12.5_analyse-structurale-elu.md` | ✅ |
| 12.6 | États-limites ultimes (ELU) | `EC2_12.6_etats-limites-ultimes.md` | ✅ |
| 12.6.1 | Résistance de calcul aux forces axiales et aux moments | `EC2_12.6.1_resistance-forces-axiales-moments.md` | ✅ |
| 12.6.2 | Rupture locale | `EC2_12.6.2_rupture-locale.md` | ✅ |
| 12.6.3 | Effort tranchant | `EC2_12.6.3_effort-tranchant.md` | ✅ |
| 12.6.4 | Torsion | `EC2_12.6.4_torsion.md` | ✅ |
| 12.6.5 | États-limites ultimes provoqués par déformation structurale | `EC2_12.6.5_deformation-structurale-flambement.md` | ✅ |
| 12.6.5.1 | Élancement des poteaux et des voiles | `EC2_12.6.5.1_elancement-poteaux-voiles.md` | ✅ |
| 12.6.5.2 | Méthode de calcul simplifiée pour voiles et poteaux | `EC2_12.6.5.2_methode-simplifiee-voiles-poteaux.md` | ✅ |
| 12.7 | États-limites de service (ELS) | `EC2_12.7_etats-limites-service.md` | ✅ |
| 12.9 | Dispositions constructives relatives aux éléments | `EC2_12.9_dispositions-constructives.md` | ✅ |
| 12.9.1 | Éléments structuraux | `EC2_12.9.1_elements-structuraux.md` | ✅ |
| 12.9.2 | Joints de construction | `EC2_12.9.2_joints-construction.md` | ✅ |
| 12.9.3 | Semelles isolées et semelles filantes superficielles | `EC2_12.9.3_semelles-fondations.md` | ✅ |

## Next Steps

1. **Complete Section 5:** Finish 5.8.8.3 (Courbure) and sections 5.9–5.11 (awaiting content)
2. **Remaining main sections:** 1–4, 6–8, 11 (awaiting content)
3. **Section 12:** Missing subsections 12.2, 12.4, 12.8 (awaiting content if applicable)
4. **Annexes:** A–J (awaiting content)

**Processing mode:** Chunked (Option A) — content pasted section-by-section. Files created as content arrives.

---

**Vault location:** `Knowledge/Norms-Regulations/Eurocodes-NBN/EC2/NBN EN 1992-1-1 2004/`  
**Created:** 2024-06-03  
**Last updated:** 2026-06-03 — Sections 2 and 12 added (Bases de calcul, Béton non armé)  
**Tool:** obsidian-pdf-splitter (Option A — chunked processing)
