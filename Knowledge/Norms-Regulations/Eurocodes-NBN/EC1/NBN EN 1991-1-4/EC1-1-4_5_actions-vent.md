---
title: "5 Actions du vent"
source: "NBN EN 1991-1-4:2005 (F) — Eurocode 1: Actions du vent (+ AC:2010)"
norm: EC1-1-4
section: "5"
chapter: "5"
tags: [EC1-1-4, pression-aerodynamique, forces-vent, surfaces]
created: 2026-06-05
---

# 5 Actions du vent

## 5.1 Généralités

(1)P Les actions du vent sur les constructions doivent être déterminées en tenant compte tant de la **pression extérieure** que de la **pression intérieure** du vent.

**Résumé de la procédure de calcul :**

| Étape | Paramètre | Article |
|-------|-----------|---------|
| 1 | Vitesse de référence `v_b` | §4.2(2)P |
| 2 | Catégorie de terrain | Tableau 4.1 |
| 3 | Coefficient de rugosité `c_r(z)` | §4.3.2 |
| 4 | Coefficient orographique `c_o(z)` | §4.3.3 |
| 5 | Vitesse moyenne `v_m(z)` | §4.3.1 |
| 6 | Intensité de turbulence `I_v` | §4.4 |
| 7 | Pression dynamique de pointe `q_p(z_e)` | §4.5(1) |
| 8 | Coefficients de pression `c_pe`, `c_pi` | Section 7 |
| 9 | Coefficient structural `c_s·c_d` | Section 6 |
| 10 | Pressions aérodynamiques `w_e`, `w_i` | §5.2 |
| 11 | Forces exercées par le vent `F_w` | §5.3 |

## 5.2 Pression aérodynamique sur les surfaces

**Pression extérieure :**

$$w_e = q_p(z_e) \cdot c_{pe} \tag{5.1}$$

**Pression intérieure :**

$$w_i = q_p(z_i) \cdot c_{pi} \tag{5.2}$$

(3) La **pression nette** sur un mur, toit ou élément = différence entre les pressions sur faces opposées (avec signe). Convention de signe : pression dirigée vers la surface = **positive** ; succion s'éloignant de la surface = **négative**.

## 5.3 Forces exercées par le vent

(1) Les forces exercées par le vent sont déterminées :
- soit à partir des **coefficients de force** (méthode directe) ;
- soit à partir des **pressions de surface** (sommation vectorielle).

**Méthode par coefficients de force :**

$$F_w = c_s c_d \cdot c_f \cdot q_p(z_e) \cdot A_{ref} \tag{5.3}$$

ou par sommation sur les éléments :

$$F_w = c_s c_d \cdot \sum_{\text{éléments}} c_f \cdot q_p(z_e) \cdot A_{ref} \tag{5.4}$$

**Méthode par pressions de surface :**

Forces extérieures :
$$F_{w,e} = c_s c_d \cdot \sum_{\text{surfaces}} w_e \cdot A_{ref} \tag{5.5}$$

Forces intérieures :
$$F_{w,i} = \sum_{\text{surfaces}} w_i \cdot A_{ref} \tag{5.6}$$

Forces de frottement :
$$F_{fr} = c_{fr} \cdot q_p(z_e) \cdot A_{fr} \tag{5.7}$$

(4) Les effets de frottement peuvent être **négligés** si l'aire totale des surfaces parallèles au vent ≤ 4 × l'aire totale des surfaces perpendiculaires au vent.

NOTE 2 NDP — La prise en compte du manque de corrélation au-delà des murs verticaux est déterminé par l'ANB. La valeur recommandée est de n'appliquer ce manque de corrélation qu'aux murs (§7.2.2(3)).

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_4_vitesse-pression]] · [[EC1-1-4_6_coefficient-cscd]] · [[_Knowledge — Index]] · [[CLAUDE]]
