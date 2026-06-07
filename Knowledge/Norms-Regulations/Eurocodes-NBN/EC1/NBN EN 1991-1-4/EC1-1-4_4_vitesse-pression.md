---
title: "4 Vitesse du vent et pression dynamique"
source: "NBN EN 1991-1-4:2005 (F) — Eurocode 1: Actions du vent (+ AC:2010)"
norm: EC1-1-4
section: "4"
chapter: "4"
tags: [EC1-1-4, vitesse-vent, pression-dynamique, rugosité, orographie, turbulence]
created: 2026-06-05
---

# 4 Vitesse du vent et pression dynamique

## 4.1 Base de calcul

(1) La vitesse du vent et la pression dynamique comprennent une composante moyenne et une composante fluctuante. La vitesse moyenne `v_m` dépend de la vitesse de référence `v_b`, de la rugosité du terrain et de l'orographie (§4.3). La composante fluctuante est caractérisée par l'intensité de turbulence `I_v` (§4.4). La pression dynamique de pointe est déterminée en §4.5.

NOTE NDP — L'Annexe Nationale peut fournir des informations climatiques nationales (cartes de vent, tableaux `v_m(z)`, `q_p(z)`).

## 4.2 Valeurs de référence

(1)P `v_b,0` est la vitesse moyenne sur **10 min** caractéristique, indépendamment de la direction du vent et de la période de l'année, à une hauteur de **10 m** au-dessus du sol en terrain dégagé de type « rase campagne » (catégorie II, Tableau 4.1).

NOTE 2 NDP — `v_b,0` est donné dans l'Annexe Nationale belge.

(2)P Vitesse de référence du vent :

$$v_b = c_{dir} \cdot c_{season} \cdot v_{b,0} \tag{4.1}$$

| Paramètre | Valeur recommandée | NDP |
|-----------|-------------------|-----|
| `c_dir` | 1,0 | Oui |
| `c_season` | 1,0 | Oui |

Coefficient de probabilité pour période de retour ≠ 50 ans :

$$c_{prob} = \left(\frac{1 - K \cdot \ln(-\ln(1-p))}{1 - K \cdot \ln(-\ln(0{,}98))}\right)^n \tag{4.2}$$

Valeurs recommandées : K = 0,2 ; n = 0,5 (NDP).

## 4.3 Vent moyen

### 4.3.1 Variation avec la hauteur

$$v_m(z) = c_r(z) \cdot c_o(z) \cdot v_b \tag{4.3}$$

où `c_r(z)` = coefficient de rugosité (§4.3.2), `c_o(z)` = coefficient orographique (§4.3.3, valeur recommandée = 1,0 si orographie ignorée).

### 4.3.2 Rugosité du terrain

Profil logarithmique :

$$c_r(z) = k_r \cdot \ln\!\left(\frac{z}{z_0}\right) \quad \text{pour } z_{min} \leq z \leq z_{max} \tag{4.4}$$

$$c_r(z) = c_r(z_{min}) \quad \text{pour } z < z_{min}$$

$$k_r = 0{,}19 \cdot \left(\frac{z_0}{z_{0,II}}\right)^{0{,}07} \quad \text{avec } z_{0,II} = 0{,}05\ \text{m} \tag{4.5}$$

**Tableau 4.1 — Catégories de terrain**

| Catégorie | Description | z₀ (m) | z_min (m) |
|-----------|-------------|--------|-----------|
| 0 | Mer ou zone côtière exposée | 0,003 | 1 |
| I | Lacs ou zone plate sans obstacles | 0,01 | 1 |
| II | Rase campagne avec obstacles isolés (≥ 20h d'écart) | 0,05 | 2 |
| III | Couverture végétale régulière, villages, forêts | 0,3 | 5 |
| IV | Zones urbaines ≥ 15% surface de bâtiments h_moy > 15 m | 1,0 | 10 |

(2) La rugosité à utiliser pour une direction du vent dépend de la rugosité du sol et de la distance au vent. Secteur angulaire recommandé : ±15° (total 30°). Zones < 10% peuvent être ignorées.

(4) Si le choix laisse deux catégories possibles, utiliser celle avec la **plus faible longueur de rugosité** (approche conservative).

### 4.3.3 Orographie du terrain

(1) Si l'orographie (collines, falaises) augmente les vitesses de plus de **5%**, prendre en compte `c_o(z)` via la procédure recommandée en Annexe A.3.

(2) Les effets d'orographie peuvent être **négligés** si la pente moyenne du terrain au vent est inférieure à **3°**.

### 4.3.4 Constructions avoisinantes de grande hauteur

(1) Si une construction voisine a une hauteur ≥ 2 fois la hauteur moyenne des constructions environnantes, des vitesses augmentées peuvent apparaître. Voir procédure en A.4.

### 4.3.5 Bâtiments et obstacles rapprochés

(1) Sur terrain rugueux, les bâtiments rapprochés modifient l'écoulement comme si le niveau du sol était élevé à la hauteur de déplacement `h_dis`. Voir A.5.

## 4.4 Turbulence du vent

Écart type de la turbulence :

$$\sigma_v = k_r \cdot v_b \cdot k_I \tag{4.6}$$

Intensité de turbulence :

$$I_v(z) = \frac{\sigma_v}{v_m(z)} = \frac{k_I}{c_o(z) \cdot \ln(z/z_0)} \quad \text{pour } z_{min} \leq z \leq z_{max} \tag{4.7}$$

$$I_v(z) = I_v(z_{min}) \quad \text{pour } z < z_{min}$$

où `k_I` = coefficient de turbulence (NDP, valeur recommandée = **1,0**).

## 4.5 Pression dynamique de pointe

$$q_p(z) = \left[1 + 7 \cdot I_v(z)\right] \cdot \frac{1}{2} \cdot \rho \cdot v_m^2(z) = c_e(z) \cdot q_b \tag{4.8}$$

avec :

$$q_b = \frac{1}{2} \cdot \rho \cdot v_b^2 \tag{4.10}$$

$$c_e(z) = \frac{q_p(z)}{q_b} \tag{4.9}$$

NOTE 2 NDP — `ρ` peut être donné dans l'ANB. Valeur recommandée : **ρ = 1,25 kg/m³**.

NOTE 3 Le facteur 7 dans (4.8) est fondé sur un facteur de pointe de **3,5**, cohérent avec les coefficients de pression et de force de la Section 7.

> Pour terrain plat (`c_o = 1,0`), le coefficient d'exposition `c_e(z)` est représenté en Figure 4.2 en fonction de la hauteur et de la catégorie de terrain.

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_3_modelisation]] · [[EC1-1-4_5_actions-vent]] · [[_Knowledge — Index]] · [[CLAUDE]]
