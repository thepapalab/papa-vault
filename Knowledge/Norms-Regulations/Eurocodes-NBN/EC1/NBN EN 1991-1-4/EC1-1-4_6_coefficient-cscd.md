---
title: "6 Coefficient structural cscd"
source: "NBN EN 1991-1-4:2005 (F) — Eurocode 1: Actions du vent (+ AC:2010)"
norm: EC1-1-4
section: "6"
chapter: "6"
tags: [EC1-1-4, coefficient-structural, cscd, reponse-dynamique, aptitude-service]
created: 2026-06-05
---

# 6 Coefficient structural c_s·c_d

## 6.1 Généralités

(1) Le coefficient structural `c_s·c_d` tient compte :
- de `c_s` : l'effet de l'**absence de simultanéité** des pointes de pression à la surface (réduction) ;
- de `c_d` : les **vibrations de la structure** engendrées par la turbulence (majoration).

NOTE NDP — Le découpage `c_s`/`c_d` peut être précisé par l'ANB.

## 6.2 Détermination de c_s·c_d

`c_s·c_d = 1,0` peut être adopté dans les cas suivants :

| Cas | Condition |
|-----|-----------|
| a | Bâtiments h < **15 m** |
| b | Éléments de façade/toiture avec fréquence propre > **5 Hz** |
| c | Bâtiments en charpente avec cloisons, h < **100 m** et h < 4 × largeur dans direction du vent |
| d | Cheminées circulaires h < **60 m** et h < 6,5 × diamètre |

Pour les ouvrages de génie civil (autres que ponts), cheminées et bâtiments hors limites c) et d) : calculer `c_s·c_d` via §6.3 ou Annexe D.

NOTE 2 Les figures de l'Annexe D donnent des valeurs enveloppes (sécuritaires) de `c_s·c_d` pour différents types de constructions.

> [!tip] Ponts railway courants (< 40 m)
> Selon §8.2 NOTE 3, pour les ponts normaux (acier, béton, mixte) d'une travée < 40 m, `c_s·c_d` peut être pris égal à **1,0**.

## 6.3 Procédure détaillée

### 6.3.1 Coefficient structural c_s·c_d

$$c_s c_d = \frac{1 + 2 \cdot k_p \cdot I_v(z_s) \cdot \sqrt{B^2 + R^2}}{1 + 7 \cdot I_v(z_s)} \tag{6.1}$$

avec :

$$c_s = \frac{1 + 7 \cdot I_v(z_s) \cdot \sqrt{B^2}}{1 + 7 \cdot I_v(z_s)} \tag{6.2}$$

$$c_d = \frac{1 + 2 \cdot k_p \cdot I_v(z_s) \cdot \sqrt{B^2 + R^2}}{1 + 7 \cdot I_v(z_s) \cdot \sqrt{B^2}} \tag{6.3}$$

où :
- `z_s` = hauteur de référence (Figure 6.1) : `z_s = 0,6·h ≥ z_min` pour constructions verticales
- `k_p` = facteur de pointe
- `B²` = coefficient de réponse quasi-statique
- `R²` = coefficient de réponse résonante

NOTE 3 NDP — La procédure pour `k_p`, `B` et `R` est donnée dans l'ANB. Procédure recommandée : Annexe B. Alternative : Annexe C (écart ≤ 5%).

(2)P L'expression (6.1) n'est applicable que si :
- la construction correspond aux formes générales de la Figure 6.1 ;
- seules les vibrations dans la direction du vent selon le **mode fondamental** sont significatives, avec une déformée de signe constant.

### 6.3.2 Évaluation de l'aptitude au service

(1) Utiliser le déplacement maximal dans la direction du vent et l'écart type de l'accélération à la hauteur z. Méthode recommandée : Annexe B. Alternative : Annexe C.

### 6.3.3 Excitation par la turbulence de sillage

(1) Pour les bâtiments élancés (h/d > 4) et les cheminées (h/d > 6,5) en paires ou groupes : prendre en compte l'excitation par la turbulence de sillage.

(2) Négligeable si au moins une condition est satisfaite :
- distance > 25 × dimension perpendiculaire au vent de la construction amont ;
- fréquence propre de la construction aval > **1 Hz**.

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_5_actions-vent]] · [[EC1-1-4_7a_generalites-batiments]] · [[_Knowledge — Index]] · [[CLAUDE]]
