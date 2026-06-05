---
title: "8 Actions du vent sur les ponts"
source: "NBN EN 1991-1-4:2005 (F) — Eurocode 1: Actions du vent (+ AC:2010)"
norm: EC1-1-4
section: "8"
chapter: "8"
tags: [EC1-1-4, ponts, tabliers, piles, coefficients-force, direction-vent, ferroviaire]
language: fr
jupyter_ref: "EC1-1-4/8"
created: 2026-06-05
---

# 8 Actions du vent sur les ponts

> [!important] Usage railway
> La Section 8 est la référence principale pour les ponts-rails. Pour les ponts normaux (acier, béton, mixte) d'une travée < 40 m, `c_s·c_d = 1,0` (§8.2 NOTE 3). Pour la combinaison avec trafic ferroviaire, la vitesse de vent est limitée à `v**_b,0 = 25 m/s` (NDP, §8.1(5)).

## 8.1 Généralités

(1) La présente section s'applique aux ponts d'épaisseur constante avec des sections transversales courantes (Figure 8.1), comprenant un tablier unique avec une ou plusieurs travées.

NOTE 1 NDP — Pour les ponts en arc, ponts à câbles, ponts couverts, ponts mobiles, ponts à tabliers multiples ou en courbe prononcée : règles dans l'ANB.

(2) Forces en direction x (transversale) et z (verticale) : §8.3. Forces sur piles : §8.4.

Forces simultanées sur les différentes parties du pont dues à un même vent : à prendre en compte simultanément si défavorables.

(3) **Système d'axes pour les ponts :**

| Direction | Définition |
|-----------|-----------|
| x | Parallèle à la largeur du tablier, perpendiculaire à la travée |
| y | Dans le sens de la travée (longitudinal) |
| z | Perpendiculaire au tablier (vertical) |

Les forces x et y sont dues à des vents de directions différentes → normalement **non simultanées**. Les forces z peuvent être simultanées aux forces dans toute autre direction.

(4) **Trafic routier simultané au vent** : limiter `v_b,0` à `v*_b,0`. Valeur recommandée NDP : **23 m/s**.

(5) **Trafic ferroviaire simultané au vent** : limiter `v_b,0` à `v**_b,0`. Valeur recommandée NDP : **25 m/s**.

## 8.2 Choix de la procédure de calcul de réponse dynamique

NOTE 2 Si une procédure dynamique n'est pas nécessaire : `c_s·c_d = 1,0`.

NOTE 3 Procédure dynamique **généralement non nécessaire** pour :
- tabliers de ponts routiers et ferroviaires normaux, travée < **40 m** ;
- ponts en acier, béton, aluminium, bois, mixtes, de section couverte par Figure 8.1.

## 8.3 Coefficients de force

### 8.3.1 Coefficients de force dans la direction x (méthode générale)

$$c_{f,x} = c_{fx,0} \tag{8.1}$$

où `c_{fx,0}` est le coefficient de force sans écoulement de contournement aux extrémités (§7.13).

NOTE 2 Pour les **ponts normaux** : `c_{fx,0}` peut être pris égal à **1,3**. Sinon, utiliser Figure 8.3 en fonction de `b/d_tot`.

**Corrections :**
- Face au vent inclinée sur la verticale d'un angle α : réduction de `c_{fx,0}` de **0,5% par degré**, max **−30%**.
- Pente transversale du tablier : majoration de `c_{fx,0}` de **3% par degré**, max **+25%**.

**Aire de référence A_ref,x :**

| Situation | Hauteur à prendre en compte pour A_ref,x |
|-----------|------------------------------------------|
| Tablier à poutres à âmes pleines, sans trafic | Voir Tableau 8.1 (poutre de rive + saillies + garde-corps) |
| Tablier à poutres en treillis, sans trafic | Corniche + proj. des poutres + garde-corps |
| Pont-route, avec trafic | Tableau 8.1 puis remplacer si plus grand par **2 m** depuis niveau chaussée |
| **Pont-rail, avec trafic** | Tableau 8.1 puis remplacer si plus grand par **4 m** depuis dessus des rails, sur longueur totale du pont |

**Tableau 8.1 — Hauteur pour A_ref,x selon type de dispositif de retenue**

| Dispositif de retenue | Un côté | Deux côtés |
|----------------------|---------|-----------|
| Garde-corps ajouré ou glissière de sécurité | d + 0,3 m | d + 0,6 m |
| Garde-corps plein ou barrière pleine | d + d₁ | d + 2·d₁ |
| Garde-corps ajouré + glissière de sécurité | d + 0,6 m | d + 1,2 m |

(6) **Hauteur de référence z_e :** distance entre le sol le plus bas et le centre de la structure du tablier (sans garde-corps ni équipements).

### 8.3.2 Force dans la direction x — Méthode simplifiée

Applicable si réponse dynamique non nécessaire :

$$F_w = \frac{1}{2} \cdot \rho \cdot v_b^2 \cdot C \cdot A_{ref,x} \tag{8.2}$$

avec `C = c_e · c_{f,x}` (coefficient de force du vent).

**Tableau 8.2 — Valeurs recommandées du coefficient C (NDP)**

| b/d_tot | z_e ≤ 20 m | z_e = 50 m |
|---------|-----------|-----------|
| ≤ 0,5 | **6,7** | **8,3** |
| ≥ 4,0 | **3,6** | **4,5** |

Hypothèses du Tableau 8.2 : catégorie de terrain II, `c_o = 1,0`, `k_I = 1,0`. Interpolation linéaire pour valeurs intermédiaires.

### 8.3.3 Forces dans la direction z (portance)

$$A_{ref,z} = b \cdot L \tag{8.3}$$

NOTE 1 NDP — Valeur recommandée de `c_{f,z}` : **±0,9** (en l'absence d'essais en soufflerie). Cette valeur prend en compte la pente transversale éventuelle du tablier, la pente du terrain et les fluctuations de l'angle d'incidence.

(5) Excentricité de la force dans la direction x : `e = b/4` (sauf spécification contraire).

### 8.3.4 Forces dans la direction y (longitudinal)

NOTE NDP — Valeurs recommandées :
- Ponts à poutres pleines : **25%** des forces direction x
- Ponts à poutres en treillis : **50%** des forces direction x

## 8.4 Piles de ponts

### 8.4.1 Directions du vent et situations de projet

(1) Identifier la direction la plus défavorable pour l'ensemble de la structure.

(2) Calculs distincts à effectuer pour les **situations transitoires** (phases de construction) lorsque le tablier ne permet aucune transmission horizontale. Prendre en compte les asymétries (éléments en console, échafaudages).

### 8.4.2 Effets du vent sur les piles

(1) Utiliser les dispositions des §7.6, §7.8 ou §7.9.2 pour les charges globales sur les piles.

NOTE 2 NDP — Procédure recommandée : supprimer la charge de calcul du vent sur les parties où elle a un effet bénéfique (voir §7.1.2(1)).

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_6_coefficient-cscd]] · [[EC1-1-4_7c_elements-structuraux]] · [[EC1-1-4_A_effets-terrain]] · [[PTR CE01 — Ch03 — Actions — FR]]
