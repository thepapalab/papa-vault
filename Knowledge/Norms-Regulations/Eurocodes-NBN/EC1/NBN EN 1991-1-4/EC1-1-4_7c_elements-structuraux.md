---
title: "7c — Coefficients de pression — Éléments structuraux (§7.5–7.13)"
source: "NBN EN 1991-1-4:2005 (F) — Eurocode 1: Actions du vent (+ AC:2010)"
norm: EC1-1-4
section: "7c"
chapter: "7"
tags: [EC1-1-4, elements-structuraux, cylindres, treillis, drapeaux, elancement]
language: fr
jupyter_ref: "EC1-1-4/7c"
created: 2026-06-05
---

# 7c — Coefficients de pression — Éléments structuraux (§7.5–7.13)

> Précédent : [[EC1-1-4_7b_toitures-isolees-murs]] (§7.3–7.4).

## 7.5 Coefficients de frottement

(1) Les coefficients de frottement `c_fr` pour les surfaces parallèles à la direction du vent :

| Type de surface | c_fr |
|----------------|------|
| Surface lisse (acier, béton lisse) | 0,01 |
| Surface rugueuse (béton rugueux, lattes) | 0,02 |
| Surface très rugueuse (nervures, cannelures) | 0,04 |

Les forces de frottement peuvent être négligées si A_totale_parallèle ≤ 4 × A_totale_perpendiculaire au vent.

## 7.6 Éléments structuraux de section rectangulaire

(1) Les coefficients de force `c_{f,0}` (sans effet d'extrémités) pour les éléments de section rectangulaire dépendent du rapport d'allongement `d/b` et de la rugosité de surface.

NOTE NDP — L'ANB peut définir la procédure. La procédure recommandée est basée sur la Figure 7.23 et le Tableau 7.13.

Pour les profils allongés (d/b > 5) :
- `c_{f,0} = 1,4 + 0,5·(d/b − 1)` environ

Le coefficient de force avec effet d'extrémités :
$$c_f = c_{f,0} \cdot \psi_\lambda$$

## 7.7 Profilés à angles vifs

(1) Pour les profilés à angles vifs (profils en L, T, +, etc.) :

NOTE NDP — La valeur de `c_{f,0}` peut être donnée dans l'ANB.

Valeur recommandée pour profils à angles vifs : `c_{f,0} = 2,0` (direction du vent perpendiculaire à l'un des bras).

## 7.8 Éléments structuraux de section polygonale régulière

(1) Pour les sections polygonales régulières (hexagonale, octogonale, etc.) :

| Section | c_f,0 |
|---------|-------|
| Carré, toutes surfaces | 2,10 |
| Carré, angles arrondis (r/b = 0,3) | 1,50 |
| Pentagone, toutes surfaces | 1,80 |
| Hexagone, toutes surfaces | 1,60 |
| Octogone, toutes surfaces | 1,40 |
| Dodécagone, toutes surfaces | 1,30 |

NOTE NDP.

## 7.9 Cylindres à base circulaire

### 7.9.1 Coefficients de pression extérieure

(1) La distribution de pression autour d'un cylindre circulaire dépend du **nombre de Reynolds Re** :

$$Re = \frac{v \cdot b}{\nu} \quad \text{avec } \nu = 15 \times 10^{-6}\ \text{m}^2/\text{s}$$

- Régime subcritique (Re < 5×10⁵) : `c_f,0 ≈ 1,2`
- Régime critique (5×10⁵ < Re < 5×10⁶) : transition
- Régime supercritique (Re > 5×10⁶) : `c_f,0 ≈ 0,5` (pour surface lisse)

L'effet de la rugosité de surface k/b modifie significativement `c_f,0` dans le régime critique. Voir Figure 7.28.

### 7.9.2 Coefficients de force

$$c_f = c_{f,0} \cdot \psi_\lambda \tag{7.15}$$

**Rugosité équivalente k pour cylindres :**

| Matériau / finition | k (mm) |
|--------------------|--------|
| Acier galvanisé | 0,2 |
| Acier peint ou bitumé | 0,006 |
| Béton lisse | 0,2–0,5 |
| Béton rugueux | 1,0–3,0 |
| Fibre renforcée de fibres ou verre | 0,04–0,08 |
| Fils parallèles | 0,006 |
| Câbles en torons | 0,020 |

### 7.9.3 Coefficients de force applicables aux cylindres verticaux disposés en file

Prise en compte de l'effet d'interférence entre cylindres disposés en file dans la direction du vent.

## 7.10 Sphères

Coefficient de force `c_f` selon le nombre de Reynolds et la rugosité de surface. Pour Re > 10⁶ (sphère lisse) : `c_f ≈ 0,2`.

## 7.11 Structures en treillis et échafaudages

(1) Le coefficient de force pour les structures en treillis plans :

$$c_f = c_{f,0} \cdot \psi_\lambda$$

où `c_{f,0}` est tiré de la Figure 7.33 en fonction du **taux de remplissage φ** :
- φ = A_solide / A_contour

Pour φ → 0 (treillis très ouvert) : `c_{f,0} → 2,0`
Pour φ = 1 (face pleine) : `c_{f,0} → 1,3`

NOTE NDP — Facteur de réduction pour les échafaudages non équipés de bâches.

## 7.12 Drapeaux

Coefficient de force `c_f` pour les drapeaux libres en tissu souple, en fonction de la masse surfacique et de la pression dynamique.

## 7.13 Élancement effectif λ et facteur d'effet d'extrémités ψ_λ

(1) L'élancement effectif λ et le facteur d'effet d'extrémités ψ_λ tiennent compte de la réduction de la force due aux écoulements en bout de structure.

**Élancement effectif λ :**

| Situation | λ |
|-----------|---|
| Structure de longueur infinie (sans extrémités libres) | λ = l/b |
| Bâtiment (au sol) | λ = 2·h/b |
| Cheminée circulaire libre en bout | λ = l/b avec l ≤ 70 m |

Facteur `ψ_λ` en fonction de λ : Figure 7.36.
- Pour λ < 5 : `ψ_λ ≈ 0,6`
- Pour λ = 10 : `ψ_λ ≈ 0,7`
- Pour λ ≥ 70 : `ψ_λ ≈ 1,0`

NOTE 1, 2 NDP — Les valeurs de ψ_λ peuvent être définies dans l'ANB.

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_7b_toitures-isolees-murs]] · [[EC1-1-4_8_actions-ponts]]
