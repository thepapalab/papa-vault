---
title: "D — Annexe D — Valeurs cscd pour divers types de constructions (informative)"
source: "NBN EN 1991-1-4:2005 (F) — Eurocode 1: Actions du vent (+ AC:2010)"
norm: EC1-1-4
section: "D"
chapter: "D"
tags: [EC1-1-4, cscd, types-structures, valeurs, abaques]
language: fr
jupyter_ref: "EC1-1-4/D"
created: 2026-06-05
---

# Annexe D — Valeurs c_s·c_d pour divers types de constructions (informative)

> Annexe informative fournissant des **valeurs enveloppes** (sécuritaires) de `c_s·c_d` calculées conformément à la Procédure 1 (Annexe B). Utilisable directement sans calcul détaillé lorsque la structure entre dans l'une des catégories suivantes.

## Figures disponibles

| Figure | Type de structure |
|--------|------------------|
| D.1 | Bâtiments à section carrée en plan |
| D.2 | Bâtiments à section rectangulaire en plan (b/d = 2) |
| D.3 | Bâtiments à section rectangulaire en plan (b/d = 5) |
| D.4 | Cheminées circulaires (béton) |
| D.5 | Cheminées circulaires (acier) |
| D.6 | Bâtiments trapézoïdaux |

Chaque figure donne `c_s·c_d` en fonction de :
- la hauteur h de la construction
- la largeur de la base b (ou diamètre d pour les cheminées)

## Conditions d'utilisation

- Les valeurs sont des enveloppes conservatrices calculées pour les paramètres les moins favorables parmi les différentes catégories de terrain (II à IV) et selon une distribution logarithmique de la vitesse.
- Le coefficient d'amortissement retenu est δ_s = 0,05 (sauf indication contraire).
- Ces valeurs ne s'appliquent qu'aux structures dont la géométrie correspond aux figures.
- Pour les ponts : utiliser §8.2 plutôt que cette annexe.

## Utilisation pratique

Pour les bâtiments courants (h < 100 m, h < 4b dans direction du vent) entrant dans les cas c) du §6.2 : `c_s·c_d = 1,0` est directement applicable sans consulter cette annexe.

Cette annexe est utile pour les structures plus élancées ou de géométrie particulière, avant d'engager un calcul complet via l'Annexe B.

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_C_procedure2-cscd]] · [[EC1-1-4_6_coefficient-cscd]]
