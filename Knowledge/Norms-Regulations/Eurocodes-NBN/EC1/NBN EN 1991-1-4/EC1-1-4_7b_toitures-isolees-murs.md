---
title: "7b — Coefficients de pression — Toitures isolées et murs (§7.3–7.4)"
source: "NBN EN 1991-1-4:2005 (F) — Eurocode 1: Actions du vent (+ AC:2010)"
norm: EC1-1-4
section: "7b"
chapter: "7"
tags: [EC1-1-4, toitures-isolees, acroteres, clotures, panneaux]
language: fr
jupyter_ref: "EC1-1-4/7b"
created: 2026-06-05
---

# 7b — Coefficients de pression — Toitures isolées et murs (§7.3–7.4)

> Précédent : [[EC1-1-4_7a_generalites-batiments]] (§7.1–7.2). Suite : [[EC1-1-4_7c_elements-structuraux]] (§7.5–7.13).

**Note PDF :** Les tableaux de cette section comportent des valeurs numériques pour des combinaisons d'angle/zone complexes. Pour le calcul, se référer au PDF source.

## 7.3 Toitures isolées

Les coefficients de pression nette `c_p,net` pour les toitures isolées (sans murs, hangars ouverts, auvents) dépendent de :
- l'angle de pente α de la toiture
- le taux de remplissage φ (obstruction sous la toiture : φ = 0 pour toiture totalement dégagée, φ = 1 pour toiture avec obstruction totale)
- la direction du vent θ = 0° ou θ = 180°

**Toitures mono-versant isolées** (Tableau 7.6 / Figure 7.13) :
- α de 0° à +30°, pour φ = 0 et φ = 1
- Valeurs `c_p,net` variant de −2,5 (succion max) à +1,8 (pression max)

**Toitures deux versants isolées** (Tableau 7.8 / Figure 7.14) :
- α de −20° à +20°, pour φ = 0 et φ = 1
- La valeur la plus défavorable parmi les deux directions de vent doit être retenue

**Toitures en appentis sur plusieurs travées** (Figure 7.15) :
- Travée d'extrémité au vent : appliquer coefficients de toiture mono-versant
- Travée d'extrémité sous le vent : multiplier par facteurs de réduction

**Conditions d'application :**
- La longueur de la toiture est supposée suffisamment grande devant sa largeur
- Pour les zones d'extrémité (zones transversales de largeur = d/10 ou 2h selon le minimum), les coefficients locaux de bord peuvent être plus élevés

## 7.4 Murs isolés, acrotères, clôtures et panneaux de signalisation

### 7.4.1 Murs isolés et acrotères

(1) Le coefficient de force net pour les murs isolés et les acrotères est donné par l'expression :

$$c_{f,net} = c_{p,net}$$

où `c_{p,net}` est le coefficient de pression nette (différence de pression entre les deux faces).

**Valeurs recommandées :**
- Pour les murs de longueur infinie (`l/h → ∞`) : `c_{f,net} = 1,3` (côtés courts) ou `c_{f,net} = 1,1` (côtés longs)
- Pour les acrotères en toiture : voir coefficients de la Section 7.2 combinés avec les pressions intérieures

La force exercée par le vent sur un mur isolé est calculée à partir de :

$$F_w = c_s c_d \cdot c_{f,net} \cdot q_p(z_e) \cdot A_{ref}$$

**Zones de pression sur mur isolé (Figure 7.19) :**

| Zone | Position | Coefficient c_p,net recommandé |
|------|----------|-------------------------------|
| A | Extrémités (0 ≤ x ≤ l/4) | Valeur élevée (succion forte) |
| B | Zone courante (l/4 < x ≤ 3l/4) | Valeur réduite |
| C | Côté sous le vent (3l/4 < x ≤ l) | Valeur faible |

NOTE NDP.

### 7.4.2 Facteurs de protection applicables aux murs et aux clôtures

Si un mur ou une clôture se trouve à l'abri d'un obstacle de hauteur similaire en amont, un facteur de protection `ψ_s` peut réduire les coefficients de force :

- Pour un espacement entre les constructions de 2h à 5h : `ψ_s = 0,8`
- Pour un espacement > 5h : `ψ_s = 1,0` (pas de réduction)

### 7.4.3 Panneaux de signalisation

(1) Le coefficient de force pour les panneaux de signalisation est :

$$c_f = 1{,}8$$

NOTE NDP — L'ANB peut donner des valeurs alternatives.

L'aire de référence est l'aire du panneau. La hauteur de référence `z_e` est la distance entre le niveau du sol et le bord supérieur du panneau.

Pour les panneaux avec une excentricité de la force latérale : l'excentricité est de `e = ±0,25·b` (b = largeur du panneau).

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_7a_generalites-batiments]] · [[EC1-1-4_7c_elements-structuraux]]
