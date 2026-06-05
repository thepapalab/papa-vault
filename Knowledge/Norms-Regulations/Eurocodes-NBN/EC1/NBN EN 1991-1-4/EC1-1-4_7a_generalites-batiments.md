---
title: "7a — Coefficients de pression — Généralités et bâtiments (§7.1–7.2)"
source: "NBN EN 1991-1-4:2005 (F) — Eurocode 1: Actions du vent (+ AC:2010)"
norm: EC1-1-4
section: "7a"
chapter: "7"
tags: [EC1-1-4, coefficients-pression, batiments, toitures, murs-verticaux]
language: fr
jupyter_ref: "EC1-1-4/7a"
created: 2026-06-05
---

# 7a — Coefficients de pression et de force — Généralités et bâtiments (§7.1–7.2)

> Ce fichier couvre les §7.1 (Généralités) et §7.2 (Coefficients de pression pour les bâtiments). Suite : [[EC1-1-4_7b_toitures-isolees-murs]] (§7.3–7.4) et [[EC1-1-4_7c_elements-structuraux]] (§7.5–7.13).

Contenu extrait directement du texte normatif. Les tableaux de coefficients (Tableaux 7.1 à 7.7) et figures de zones (Figures 7.1 à 7.16) sont référencés mais ne peuvent être reproduits intégralement — consulter le PDF source pour les valeurs numériques complètes.

**Note PDF :** Les tableaux de coefficients de pression de cette section comportent des cellules fusionnées complexes qui ne se transcrivent pas fidèlement en markdown. Les valeurs numériques de référence sont indiquées dans le texte ; pour le calcul, se référer au PDF NBN EN 1991-1-4:2005.

## 7.1 Généralités

### 7.1.1 Choix du coefficient aérodynamique

(1) Il convient d'utiliser les coefficients de force pour les effets globaux et les coefficients de pression pour les effets locaux.

Les coefficients de pression sont décomposés en :
- coefficients de pression extérieure `c_pe` pour les surfaces chargées > 10 m² (coefficients globaux)
- coefficients de pression extérieure `c_pe` pour les surfaces chargées ≤ 1 m² (coefficients locaux)

$$c_{pe} = c_{pe,1} \quad \text{pour } A \leq 1\ \text{m}^2$$

$$c_{pe} = c_{pe,10} \quad \text{pour } A \geq 10\ \text{m}^2$$

Interpolation logarithmique pour 1 m² < A < 10 m² :
$$c_{pe} = c_{pe,1} - (c_{pe,1} - c_{pe,10}) \cdot \log_{10}(A)$$

NOTE NDP — Les valeurs des coefficients de pression peuvent être définies dans l'ANB.

### 7.1.2 Pressions et forces asymétriques ou en opposition

(1) Lorsque des valeurs asymétriques de charge sont définies dans le texte, il convient de les prendre en compte dans les cas appropriés.

(2) Si les effets du vent sont de nature à produire des forces s'opposant à la stabilité de la structure, il convient de les prendre en compte.

NOTE NDP — Les situations où les pressions intérieure et extérieure sont en opposition peuvent être définies dans l'ANB.

### 7.1.3 Effets de la glace et de la neige

(1) En présence de glace ou de neige, les coefficients de pression peuvent être modifiés.

NOTE NDP.

## 7.2 Coefficients de pression pour les bâtiments

### 7.2.1 Généralités

(1) Les coefficients de pression extérieure pour les bâtiments dépendent de la taille et de la forme du bâtiment. Le flux de vent autour d'un bâtiment crée une pression sur la face au vent et des dépressions sur les faces latérales, la face sous le vent et sur les toitures.

La **hauteur de référence** pour la pression extérieure `z_e` dépend du rapport h/b :
- Si h ≤ b : `z_e = h`
- Si b < h ≤ 2b : `z_e` varie de b (bas) à h (haut)
- Si h > 2b : zone basse `z_e = b`, zone haute `z_e = h`

NOTE NDP — L'ANB peut fournir des procédures simplifiées.

### 7.2.2 Murs verticaux des bâtiments à plan rectangulaire

(1) Les coefficients de pression extérieure `c_pe` pour les murs verticaux sont donnés dans le **Tableau 7.1** en fonction des zones A, B, C, D, E (Figure 7.5).

La face au vent : zone D (pression positive, `c_pe,10 = +0,8` typ.)
La face sous le vent : zone E (succion, `c_pe,10 = −0,5` typ.)
Les faces latérales : zones A, B, C (forte succion près des bords)

NOTE NDP — L'ANB peut modifier les valeurs.

(2) Lorsque le rapport h/d > 5 : utiliser les coefficients du Tableau 7.1 avec les valeurs pour h/d > 5.

(3) Le **manque de corrélation** de la pression entre la face au vent (zone D) et la face sous le vent (zone E) peut être pris en compte selon la méthode suivante :
- Pour 0,25 ≤ h/d ≤ 1 : la résultante des forces dans la direction du vent peut être multipliée par **0,85**.

### 7.2.3 Toitures-terrasses

Coefficients de pression extérieure `c_pe` selon les zones F, G, H, I (Figure 7.6) en fonction de l'angle de la corniche ou de la forme du bord. Voir **Tableau 7.2**.

### 7.2.4 Toitures à un seul versant

Coefficients selon l'angle de pente α du versant. Voir **Tableau 7.3**.

Pour α ≥ 15° et vent en direction θ = 0° : zone F peut atteindre `c_pe,10 = +0,7`.

NOTE 2 Pour les angles intermédiaires, interpolation linéaire entre valeurs de même signe. Les valeurs = 0,0 sont données à fins d'interpolation.

### 7.2.5 Toitures à deux versants

Coefficients selon l'angle de pente α du versant. Voir **Tableau 7.4**.

Pour α = −45° (toiture à versants relevés) à +75° (toiture pentue). Distinctions pour θ = 0° et θ = 90°.

NOTE 2 Pour les angles intermédiaires, interpolation linéaire entre valeurs de même signe. Les valeurs égales à 0,0 sont données à cette fin d'interpolation.

### 7.2.6 Toitures à quatre versants

Coefficients selon l'angle de pente α. Voir **Tableau 7.5** et Figure 7.9.

Pour θ = 0° et θ = 90°.

### 7.2.7 Toitures multiples (shed)

Coefficients selon le nombre de travées et l'angle de pente. Pour une travée : utiliser les toitures mono-versant. Pour plusieurs travées : voir Figure 7.10 et Tableau.

| Travée | Facteur multiplicateur |
|--------|----------------------|
| Travée d'extrémité | 1,0 (au vent) / 0,8 (sous vent) |
| Deuxième travée | 0,9 (au vent) / 0,7 (sous vent) |

### 7.2.8 Toitures en voûte et dômes

Coefficients de pression extérieure `c_pe,10` en fonction de f/d (flèche relative) et h/d. Voir **Tableau 7.6** et Figure 7.11.

NOTE NDP — L'ANB peut fournir des règles supplémentaires.

### 7.2.9 Pression intérieure

(1) Les coefficients de pression intérieure `c_pi` dépendent de la taille et de la distribution des ouvertures sur l'ensemble de l'enveloppe du bâtiment.

(2) Lorsque les ouvertures de la face la plus exposée représentent plus de **30%** de la surface totale des ouvertures : coefficients de pression intérieure selon Tableau 7.1 zones D ou E.

La pression intérieure et la pression extérieure doivent être prises en compte simultanément sur toutes les surfaces.

**Coefficient de rapport d'ouverture µ :**
Si µ < 0,25 : `c_pi = −0,3`
Si µ ≥ 0,25 (ou incertain) : utiliser la valeur la plus défavorable parmi `c_pi = +0,2` et `c_pi = −0,3`.

NOTE NDP.

### 7.2.10 Pression exercée sur les murs ou les toitures comportant plusieurs parois

(1) Pour les constructions avec plusieurs enveloppes (toiture double peau, etc.) : la pression nette sur chaque paroi est calculée en fonction de la perméabilité des parois.

NOTE 1, 2 NDP.

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_5_actions-vent]] · [[EC1-1-4_6_coefficient-cscd]] · [[EC1-1-4_7b_toitures-isolees-murs]]
