---
title: "Index — Annexes A & B"
source: "EN 1992-1-1:2004 (F)"
norm: EC2
tags: [EC2, index, annexes]
language: fr
---

# Annexes A & B — Index

## Annexe A : Modification des coefficients partiels relatifs aux matériaux

Annexe informative pour réduire les coefficients partiels de sécurité en fonction du niveau de contrôle et du type de construction.

### Navigation

| Section | Titre | Tags |
|---------|-------|------|
| [[EC2_A.1_generalites-coefficients.md\|A.1]] | Généralités | coefficients-partiels, imperfections |
| [[EC2_A.2.1_tolerance-reduite.md\|A.2.1]] | Réduction basée sur le contrôle de la qualité | tolérances, contrôle-qualité |
| [[EC2_A.2.2_donnees-geometriques.md\|A.2.2]] | Réduction basée sur données géométriques | hauteur-utile, mesure |
| [[EC2_A.2.3_resistance-in-situ.md\|A.2.3]] | Réduction basée sur la résistance in situ | résistance-béton, mesure-in-situ |
| [[EC2_A.3.1_prefabriques-generalites.md\|A.3.1]] | Produits préfabriqués — Généralités | produits-préfabriqués, conformité |
| [[EC2_A.3.2_coefficients-prefab.md\|A.3.2]] | Coefficients partiels — Produits préfabriqués | coefficients-partiels, contrôle-production |
| [[EC2_A.4_elements-prefabriques.md\|A.4]] | Éléments préfabriqués | éléments-préfabriqués, coefficients-partiels |

---

## Annexe B : Déformations dues au fluage et au retrait

Annexe informative fournissant les équations de base pour calculer les déformations liées au fluage et au retrait de dessiccation.

### Navigation

| Section | Titre | Tags |
|---------|-------|------|
| [[EC2_B.1_coefficient-fluage.md\|B.1]] | Coefficient de fluage | fluage, coefficient-fluage, temps, humidité-relative |
| [[EC2_B.2_retrait-dessiccation.md\|B.2]] | Retrait de dessiccation | retrait, déformation, humidité-relative |

---

## Résumé des contenus

### Annexe A
**Objectif :** Fournir les conditions et recommandations pour réduire les coefficients partiels de sécurité (γ) du béton et des armatures en fonction :
- Du niveau de contrôle de la qualité
- De la qualité des données géométriques
- De mesures de résistance effectuées sur la structure finie
- Du type de construction (coulée en place vs préfabriqué)

**Coefficients traités :**
- $\gamma_{s,\text{red1}}$, $\gamma_{c,\text{red1}}$ (contrôle qualité)
- $\gamma_{s,\text{red2}}$, $\gamma_{c,\text{red2}}$, $\gamma_{c,\text{red3}}$ (données géométriques)
- $\gamma_{c,\text{red4}}$ (résistance mesurée)
- $\gamma_{c,\text{pcred}}$, $\gamma_{s,\text{pcred}}$ (produits préfabriqués)

### Annexe B
**Objectif :** Fournir des équations pratiques pour le calcul des déformations différées :

**B.1 — Fluage :** Coefficient $\varphi(t, t_0)$ basé sur :
- Humidité relative (RH)
- Résistance du béton ($f_{cm}$)
- Âge au chargement ($t_0$)
- Durée du chargement ($t - t_0$)
- Type de ciment et température

**B.2 — Retrait de dessiccation :** Déformation $\varepsilon_{cd,0}$ basée sur :
- Résistance du béton ($f_{cm}$)
- Type de ciment ($\alpha_{ds1}$, $\alpha_{ds2}$)
- Humidité relative (RH)

---

## Voir aussi

- [[EC2_3.1.2_types-ciment.md|3.1.2]] — Types de ciment
- [[EC2_3.1.4_fluage.md|3.1.4]] — Fluage du béton
- [[EC2_3.1.5_retrait.md|3.1.5]] — Retrait du béton
- [[EC2_2.4_coefficients-partiels.md|2.4]] — Coefficients partiels généraux
