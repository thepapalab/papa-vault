---
title: "A — Annexe A — Effets du terrain (informative)"
source: "NBN EN 1991-1-4:2005 (F) — Eurocode 1: Actions du vent (+ AC:2010)"
norm: EC1-1-4
section: "A"
chapter: "A"
tags: [EC1-1-4, terrain, orographie, rugosité, hauteur-deplacement, changement-rugosite]
created: 2026-06-05
---

# Annexe A — Effets du terrain (informative)

> Annexe informative. Les procédures présentées ici sont les procédures recommandées par l'EN. L'ANB belge peut adopter des procédures différentes.

## A.1 Catégories de terrain et paramètres

Illustrations des cinq catégories de terrain (Figure A.1) correspondant au Tableau 4.1.

## A.2 Transition entre catégories de terrain

(1) La distance au vent minimale `x_min` pour que la rugosité d'une nouvelle catégorie de terrain soit pleinement effective à la hauteur z est :

$$x_{min} = \max\left(\frac{z}{0{,}09},\ 2000\ \text{m}\right) \quad \text{(passage à terrain plus rugueux)}$$

La distance de fetch nécessaire pour passer à un terrain moins rugueux est plus courte.

## A.3 Orographie — Coefficient c_o

Pour les collines et escarpements, le coefficient orographique `c_o(z)` est calculé à partir du facteur d'amplification `s` :

$$c_o(z) = 1 + 2 \cdot s \cdot \Phi \quad \text{pour 0,05 ≤ tan(Φ) ≤ 0,3}$$

où :
- `Φ` = pente du versant au vent (rad)
- `s` = facteur d'amplification dépendant de la position sur le versant (Figure A.2)

Zones d'influence :
- En amont du sommet : jusqu'à distance `L_u` du pied du versant au vent
- En aval du sommet : jusqu'à distance `L_d = 1,5·L_u`

Pour `tan(Φ) > 0,3` (escarpements abrupts) : procédure spéciale.

## A.4 Constructions avoisinantes de grande hauteur

Lorsqu'une construction est proche d'une autre de hauteur > 2 fois la hauteur moyenne, une augmentation locale de `v_m` peut se produire. Procédure approximative en A.4.

## A.5 Hauteur de déplacement et bâtiments rapprochés

Sur terrains de catégorie IV (zones urbaines denses), la hauteur de déplacement `h_dis` peut être prise en compte :

$$h_{dis} = 0{,}8 \cdot h_{ave} \leq h - 0{,}6 \cdot d$$

où `h_ave` est la hauteur moyenne des bâtiments environnants dans un secteur de rayon 2 km.

Cette hauteur `h_dis` est soustraite de la hauteur `z` dans les expressions de `c_r(z)` et `I_v(z)`.

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_8_actions-ponts]] · [[EC1-1-4_B_procedure1-cscd]] · [[_Knowledge — Index]] · [[CLAUDE]]
