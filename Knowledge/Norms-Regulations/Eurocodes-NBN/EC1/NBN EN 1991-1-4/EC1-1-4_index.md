---
title: NBN EN 1991-1-4:2005 — Index (EC1 Vent)
type: index
source: "NBN EN 1991-1-4:2005 (F) — Eurocode 1: Actions sur les structures — Partie 1-4: Actions du vent (+ AC:2010)"
norm: EC1-1-4
date: 2005-10
replaces: "NBN ENV 1991-2-4 (2002), NBN B 03-002-1 (1988), NBN B 03-002-2 (1988)"
status: en vigueur
tags: [EC1-1-4, eurocode-1, vent, actions-vent, ponts, batiments, index]
related: ["[[_Norms-Regulations — README]]", "[[_Knowledge — Index]]"]
created: 2026-06-05
---

# NBN EN 1991-1-4:2005 — Eurocode 1 : Actions du vent

Actions du vent naturel sur les bâtiments, ouvrages de génie civil et ponts. S'utilise avec son ANB belge (NBN EN 1991-1-4 ANB) qui fixe les NDP, notamment la valeur de `v_b,0` par région et les catégories de terrain applicables en Belgique.

> [!important] Utilisation Infrabel
> Le PTR CE01 §3.1.10 autorise une pression de vent forfaitaire de **2,0 kN/m²** pour les constructions rigides de petite hauteur (v_ref = 28 m/s, terrain catégorie I). Pour les cas courants de ponts-rails, c'est la valeur à appliquer sans calcul détaillé selon EC1-1-4.
> Pour les ponts plus complexes ou hors catégorie, appliquer la procédure complète de la Section 8 avec `c_s·c_d = 1,0` (ponts < 40 m, voir §8.2 NOTE 3).

## Structure du document

| Fichier | Section | Titre |
|---------|---------|-------|
| [[EC1-1-4_00_avant-propos]] | 00 | Avant propos |
| [[EC1-1-4_1_generalites]] | 1 | Generalites |
| [[EC1-1-4_2_situations-projet]] | 2 | Situations projet |
| [[EC1-1-4_3_modelisation]] | 3 | Modelisation |
| [[EC1-1-4_4_vitesse-pression]] | 4 | Vitesse pression |
| [[EC1-1-4_5_actions-vent]] | 5 | Actions vent |
| [[EC1-1-4_6_coefficient-cscd]] | 6 | Coefficient cscd |
| [[EC1-1-4_7a_generalites-batiments]] | 7a | Generalites batiments |
| [[EC1-1-4_7b_toitures-isolees-murs]] | 7b | Toitures isolees murs |
| [[EC1-1-4_7c_elements-structuraux]] | 7c | Elements structuraux |
| [[EC1-1-4_8_actions-ponts]] | 8 | Actions ponts |
| [[EC1-1-4_A_effets-terrain]] | A | Effets terrain |
| [[EC1-1-4_B_procedure1-cscd]] | B | Procedure1 cscd |
| [[EC1-1-4_C_procedure2-cscd]] | C | Procedure2 cscd |
| [[EC1-1-4_D_valeurs-cscd]] | D | Valeurs cscd |
| [[EC1-1-4_Ea_detachement-tourbillonnaire]] | Ea | Detachement tourbillonnaire |
| [[EC1-1-4_Eb_galop-divergence-flottement]] | Eb | Galop divergence flottement |
| [[EC1-1-4_F_dynamique]] | F | Dynamique |
| [[EC1-1-4_Bibliographie]] |  | Bibliographie |
| [[EC1-1-4_AC-2010]] |  | Ac 2010 |

## Paramètres clés (EN — valeurs recommandées)

| Paramètre | Valeur recommandée | Article | Note |
|-----------|-------------------|---------|------|
| `c_dir` | 1,0 | §4.2 | NDP — valeur ANB belge à vérifier |
| `c_season` | 1,0 | §4.2 | NDP |
| `v_b,0` | NDP | §4.2 | Fixé par l'ANB belge selon la région |
| `c_s·c_d` ponts < 40 m | 1,0 | §8.2 NOTE 3 | Applicable aux ponts normaux EN + BA |
| `ρ` (densité air) | 1,25 kg/m³ | §4.5 | NDP |
| Vitesse pour trafic routier simultané | `v*_b,0 = 23 m/s` | §8.1(4) NOTE | NDP |
| Vitesse pour trafic ferroviaire simultané | `v**_b,0 = 25 m/s` | §8.1(5) NOTE | NDP |

## Catégories de terrain (Tableau 4.1)

| Catégorie | Description | z₀ (m) | z_min (m) |
|-----------|-------------|--------|-----------|
| 0 | Mer ou zone côtière | 0,003 | 1 |
| I | Lacs ou zones plates sans obstacles | 0,01 | 1 |
| II | Rase campagne avec haies, maisons isolées | 0,05 | 2 |
| III | Zones suburbaines, forêts | 0,3 | 5 |
| IV | Zones urbaines dense | 1,0 | 10 |

## Section 8 — Ponts : formules principales

**Direction x (transversale) :**
$$F_{w,x} = \frac{1}{2} \cdot \rho \cdot v_b^2 \cdot c_s c_d \cdot c_{f,x} \cdot A_{ref,x}$$

**Hauteur de référence pour ponts :**
`z_e = z_g + d/2` où `z_g` = hauteur du centre de gravité du tablier.

**Coefficient de force `c_f,x` :** fonction du rapport `b/d_tot` (largeur/épaisseur totale tablier + garde-corps), voir Tableau 8.1 / Figure 8.3.

---

Liens : [[_Norms-Regulations — README]] · [[_Knowledge — Index]] · [[CLAUDE]]
