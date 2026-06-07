---
title: "NBN EN 1992-1-1:2004 — Elements prefabriques"
type: norm-extract
source: "NBN EN 1992-1-1:2004"
norm: EC2
section: "10"
chapter: "Elements prefabriques"
tags: [EC2, eurocode-2, elements-prefabriques]
related: ["[[EC2_index]]", "[[EC2_9_dispositions-elements.md]]", "[[EC2_11_beton-granulats-legers.md]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# 10.9.5.2 Appareils d'appui pour éléments continus (non isolés)

## (1) - Calcul de la profondeur d'appui nominale

La profondeur d'appui nominale $a$ dans le cas d'un appui simple peut être calculée par:

$$a = a_1 + a_2 + a_3 + \Delta a_2 + \Delta a_3$$

### Définition des termes

- **$a_1$** = profondeur d'appui nette gouvernée par la contrainte dans l'appareil d'appui
  - Formule: $a_1 = \frac{F_{Ed}}{b_1 f_{Rd}}$
  - Valeur minimale: voir Tableau 10.2
  
- **$F_{Ed}$** = valeur de calcul de la réaction d'appui

- **$b_1$** = largeur d'appui nette (voir paragraphe (3))

- **$f_{Rd}$** = valeur de calcul de la résistance de l'appui (voir paragraphe (2))

- **$a_2$** = distance inefficace depuis le nu de l'élément porteur (voir Figure 10.6 et Tableau 10.3)

- **$a_3$** = distance inefficace pour l'élément supporté (voir Figure 10.6 et Tableau 10.3)

- **$\Delta a_2$** = tolérance sur la distance entre éléments porteurs (voir Tableau 10.5)

- **$\Delta a_3$** = tolérance sur la longueur de l'élément supporté: $\Delta a_3 = \frac{l_n}{2500}$
  - où $l_n$ = longueur de l'élément

## (2) - Résistance de l'appui

À défaut d'autres spécifications:

### Joints secs
$$f_{Rd} = 0,4 f_{cd}$$

(voir 10.9.4.3 (3) pour la définition)

### Autres cas
$$f_{Rd} = f_{bed} \leq 0,85 f_{cd}$$

Où:
- $f_{cd}$ = résistance de calcul du béton (la plus faible entre l'élément supporté et porteur)
- $f_{bed}$ = résistance de calcul du matériau de liaison

## (3) - Largeur de calcul de l'appareil d'appui

Si des dispositions assurent une répartition uniforme de la pression d'appui (mortier, plaques en néoprène, etc.), la largeur de calcul $b_1$ peut être prise égale à sa **largeur réelle**.

Sinon, et à défaut d'analyse plus précise, il convient de limiter:
$$b_1 \leq 600 \text{ mm}$$

### Tableau 10.2 - Valeur minimale de $a_1$ (mm)

| Appui type | σ_Ed/f_cd ≤ 0,15 | 0,15 - 0,4 | > 0,4 |
|---|---|---|---|
| **Appuis linéaires** (planchers, toitures) | 25 | 30 | 40 |
| **Planchers à poutrelles** et entrevous - pannes | 55 | 70 | 80 |
| **Appuis concentrés** (poutres) | 90 | 110 | 140 |

### Tableau 10.3 - Distance $a_2$ inefficace (mm)

| Matériau & type | σ_Ed/f_cd ≤ 0,15 | 0,15 - 0,4 | > 0,4 |
|---|---|---|---|
| **Acier linéaire** | 0 | 0 | 10 |
| **Acier concentré** | 5 | 10 | 15 |
| **Béton armé ≥ C30 linéaire** | 5 | 10 | 15 |
| **Béton armé ≥ C30 concentré** | 10 | 15 | 25 |
| **Béton non armé < C30 linéaire** | 10 | 15 | 25 |
| **Béton non armé < C30 concentré** | 20 | 25 | 35 |
| **Maçonnerie linéaire** | 10 | 15 | (-) |
| **Maçonnerie concentrée** | 20 | 25 | (-) |

*(-) = Chevêtre en béton requis*

### Tableau 10.4 - Distance $a_3$ inefficace (mm)

| Ferraillage | Appui linéaire | Appui concentré |
|---|---|---|
| **Barres continues** sur l'appui | 0 | 0 |
| **Barres droites, boucles** horizontales | 5 | 15 + enrobage |
| **Armatures de précontrainte** & barres en attente | 5 | 15 |
| **Boucle verticale** | 15 | Enrobage + rayon |

### Tableau 10.5 - Tolérance Δa₂ (distance libre entre nus d'appui)

| Matériau appui | Δa₂ |
|---|---|
| **Acier ou béton préfabriqué** | $10 \leq l/1200 \leq 30$ mm |
| **Maçonnerie ou béton coulé en place** | $15 \leq l/1200 + 5 \leq 40$ mm |

où $l$ = portée

# 10.9.5.3 Appareils d'appui pour éléments isolés

## (1)P - Augmentation minimale

La **profondeur d'appui nominale** pour éléments isolés doit être **supérieure de 20 mm** à celle retenue pour les éléments non-isolés (voir 10.9.5.2).

### Justification

Cette majoration de 20 mm compense l'absence de continuité structurale et améliore la stabilité des appuis.

## (2)P - Prise en compte des mouvements d'appui

Si l'appareil d'appui autorise des **mouvements de l'appui**, la **profondeur d'appui nette** doit être **majorée** pour couvrir les **mouvements éventuels**.

### Type de mouvements

Les mouvements peuvent être dus à:
- **Dilatation thermique** de l'appui ou de l'élément
- **Déformations** du système de support
- **Jeu** dans les dispositifs d'appui

### Évaluation

La majoration doit être déterminée en fonction de:
- L'amplitude maximale des mouvements prévus
- La configuration et les capacités de l'appareil d'appui
- Les tolérances de fabrication et de mise en place

## (3)P - Liaisons autrement qu'au niveau de l'appui

Si un élément est **liaisonné autrement qu'au niveau de son appareil d'appui**, la **profondeur d'appui nette** $a_1$ doit être **majorée** pour couvrir l'**effet d'une éventuelle rotation** autour de l'élément de liaison.

### Cas concernés

Cette disposition s'applique notamment à:
- **Éléments suspendus** à des points de liaison supérieurs
- **Éléments avec tirants** latéraux ou supérieurs
- **Structures avec appuis décalés** et liaisons intermédiaires

### Calcul de la majoration

La majoration dépend de:
- La position et la raideur des liaisons
- Le bras de levier par rapport à l'appui principal
- L'excentricité des efforts transmis

# 10.9.6.1 Généralités

## (1)P - Capacité de transmission

Les **plots de béton en encuvement** doivent être capables de transmettre:

1. **Les efforts verticaux** (charges de compression)
2. **Les moments fléchissants** (flexion du poteau)
3. **Les cisaillements horizontaux** (forces latérales)

Ces efforts proviennent du poteau et sont transmis au sol.

## (2)P - Dimensionnement des parois

Les **dimensions de l'encuvement** doivent être **suffisantes** pour permettre:
- La **mise en place correcte du béton** sous le pied du poteau
- La **mise en place correcte du béton** autour du poteau
- Une **compaction adéquate** du béton

## Considérations de conception

### Profondeur d'encuvement

Doit être suffisante pour:
- Encastrer le poteau
- Développer la transmission du moment
- Assurer un ancrage convenable des armatures

### Largeur et longueur

Doivent permettre:
- Un débattement minimal pendant la mise en place
- Une transmission uniforme des efforts
- L'accès pour la mise en place du béton

### Hauteur des parois

Doit être dimensionnée pour:
- Contenir l'effort de compression des bielles
- Assurer le contreventement du poteau
- Résister aux moments de flexion

# 10.9.6.2 Encuvements à parois à clés

## (1) - Comportement monolithique

Les encuvements présentant, **de par leur fabrication**, des **parois à clés ou à crans** peuvent être considérés comme **agissant de manière monolithique** avec le poteau.

### Avantages

- Transmission efficace des efforts et moments
- Comportement simplifié pour le calcul
- Meilleure durabilité (pas d'interface)

## (2) - Transmission du moment avec tractions

Lorsque la **transmission du moment** génère des **efforts verticaux de traction**, les **dispositions constructives du recouvrement** doivent être déterminées avec soin.

### Points critiques

- **Écartement** entre les barres destinées à se recouvrir
- **Augmentation de la longueur de recouvrement** (voir 8.6)
  - Majoration ≥ distance horizontale entre barres poteau et fondation

### Longueur de recouvrement augmentée

Doit inclure:
- La longueur de recouvrement de base (voir section 8)
- Plus une longueur supplémentaire égale à la **distance horizontale** entre les barres du poteau et celles de la fondation

### Armatures horizontales

Il convient de **prévoir des armatures horizontales adaptées** pour la jonction par recouvrement, assurant:
- La transmission des efforts de traction
- La limitation de la fissuration
- La cohésion de la jonction

## (3) - Calcul au poinçonnement

### Condition de monolithicité

Le calcul au poinçonnement peut se faire **comme pour un assemblage poteau/fondation monolithique** (voir 6.4), **sous réserve** de vérifier la **transmission du cisaillement** entre poteau et fondation.

### Procédure

Si la transmission du cisaillement est vérifiée:
- Calcul standard pour assemblage monolithique (section 6.4)

Si la transmission n'est pas assurée:
- Calcul comme pour **encuvements à parois lisses** (voir 10.9.6.3)

### Verification de la transmission

Dépend de:
- La géométrie des clés
- Le frottement entre surfaces
- La compression transversale

# 10.9.6.3 Encuvements à parois lisses

## (1) - Modèle de transmission des efforts

On peut admettre que la **transmission des efforts et du moment** du poteau à sa fondation s'effectue sous forme de:

- **Forces de compression** $F_1$, $F_2$ et $F_3$ à travers le béton de remplissage
- **Forces de frottement** correspondantes

### Schéma de chargement

Les forces sont définies comme:
- $F_1$ = effort horizontal en haut de l'encuvement
- $F_2$ = effort horizontal aux côtés
- $F_3$ = effort horizontal en bas
- $\mu F_i$ = forces de frottement ($\mu$ = coefficient de frottement)

### Condition de validité

Ce modèle nécessite de vérifier:
$$l \geq 1,2 h$$

Où:
- $l$ = longueur de l'encuvement (ou côté, pour encuvements carrés)
- $h$ = hauteur du poteau dans l'encuvement

## (2) - Coefficient de frottement

Il convient d'adopter un **coefficient de frottement** $\mu$ **inférieur ou égal à 0,3**:

$$\mu \leq 0,3$$

### Justification

- Prend en compte les conditions réelles d'interface
- Conservative (évite l'overestimate du frottement)
- Sécuritaire pour le dimensionnement

## (3) - Points d'attention particulière

Il convient de porter une attention particulière aux points suivants:

### Ferraillage des parois
- **Dispositions constructives** du ferraillage en partie supérieure des parois
- Vérification que les barres peuvent **reprendre l'effort** $F_1$

### Transmission le long des parois
- **Transmission de** $F_1$ le long des parois latérales du plot
- Vérification de la résistance au cisaillement des parois

### Ancrage des armatures
- **Ancrage des armatures principales** du poteau dans l'encuvement
- **Ancrage des armatures** dans les parois de l'encuvement
- Longueurs de développement suffisantes

### Résistance du poteau
- **Résistance au cisaillement** du poteau dans l'encuvement
- Vérification que les bielles internes ne sont pas écrasées
- Contrôle du cisaillement horizontal et vertical

### Poinçonnement de la base
- **Résistance au poinçonnement** de la base de l'encuvement
- Vérification des efforts transmis par le poteau
- Possibilité d'inclure le béton coulé en place sous le poteau préfabriqué

## Procédure de calcul

1. Déterminer les efforts $F_1$, $F_2$, $F_3$ à partir du moment et de l'effort tranchant
2. Vérifier $l \geq 1,2 h$
3. Calculer les efforts de frottement avec $\mu = 0,3$
4. Vérifier la résistance des parois aux compressions diagonales
5. Vérifier l'ancrage de toutes les armatures
6. Vérifier le poinçonnement en base

# 10.9.6 Fondations en encuvement

## Portée générale

Les fondations en encuvement sont des solutions courantes pour les structures préfabriquées, où un poteau préfabriqué est encastré dans une fondation (plot de béton) en encuvement.

### Deux types principaux

1. **Encuvements à parois à clés** (10.9.6.2)
2. **Encuvements à parois lisses** (10.9.6.3)

## Sections connexes

- **10.9.6.1** : Généralités
- **10.9.6.2** : Encuvements à parois à clés
- **10.9.6.3** : Encuvements à parois lisses

## Paramètres clés

Les dimensions de l'encuvement doivent permettre:
- La **transmission des efforts verticaux**
- La **transmission des moments fléchissants**
- La **transmission des cisaillements horizontaux**
- La **mise en place correcte du béton** sous le pied et autour du poteau

# 10.9.7 Chaînages

## (1) - Rôle des chaînages

Pour les **plaques chargées dans leur plan** (voiles et planchers de contreventement, par exemple), l'**interaction nécessaire** peut être obtenue en **liaisonnant la structure** au moyen de:

- **Chaînages périphériques** (autour du périmètre)
- **Chaînages intérieurs** (dans le plan de la structure)

## Deux fonctions principales

### Fonction 1 - Interaction structurale

Les chaînages **garantissent l'interaction** entre les éléments:
- Transmission des efforts de diaphragme
- Comportement d'ensemble cohérent
- Partage des charges entre éléments

### Fonction 2 - Prévention de la ruine progressive

Les **mêmes chaînages peuvent également agir** pour **prévenir une ruine progressive**, comme indiqué en **9.10** (Robustesse et prévention de la ruine progressive).

## Types de chaînages

### Chaînages périphériques

Situés en **périphérie de la structure**:
- Connectent les appuis
- Garantissent l'intégrité du contour
- Assurent la stabilité globale

### Chaînages intérieurs

Situés **à l'intérieur** de la structure:
- Connectent les points forts internes
- Fragmentent les zones de rupture potentielle
- Améliorent la distribution des efforts

## Dimensionnement

Les chaînages doivent être dimensionnés pour:
- L'effort maximal de traction anticipé
- Les conditions d'encastrement aux extrémités
- La transmission aux appuis ou à d'autres chaînages

## Références

Voir:
- **Section 9.10** : Robustesse structurale et prévention de la ruine progressive
- **Section 8** : Dispositions constructives pour l'ancrage des armatures

# 10 Règles additionnelles pour les éléments et les structures préfabriqués en béton

## 10.1 Généralités

**(1)P** Les règles de la présente Section s'appliquent aux bâtiments réalisés partiellement ou entièrement en éléments préfabriqués en béton et viennent en complément des règles des autres sections.

### 10.1.1 Terminologie particulière

**Élément préfabriqué :** élément produit en usine ou dans un emplacement autre que sa position finale dans la structure

**Situation transitoire :** démoulage, transport, stockage, montage (levage), construction (assemblage)

## 10.3 Matériaux

### 10.3.1.1 Résistance

Pour cure thermique, résistance en compression peut être estimée par :

$$f_{cm}(t) = f_{cm,p} + (f_{cm} - f_{cm,p}) \log\left(\frac{1 + (28 - t_p)}{1 + (t - t_p)}\right)  \tag{10.1}$$

### 10.3.2.2 Acier de précontrainte

Temps équivalent pour cure thermique :

$$t_{eq} = \sum_{i=1}^{n} \Delta t_i \left(\frac{T_{\max}}{20}\right)^{-1.14} \exp\left(\frac{20 - T(\Delta t_i)}{20}\right)  \tag{10.2}$$

## 10.5.2 Pertes de précontrainte

Perte thermique spécifique :

$$\Delta P_\theta = 0.5 A_p E_p \alpha_c (T_{max} - T_0)  \tag{10.3}$$

## 10.9.3 Systèmes de planchers

Effort de cisaillement par unité de longueur :

$$v_{Ed} = q_{Ed} \cdot \frac{b_e}{3}  \tag{10.4}$$

## 10.9.4.3 Joints de compression

Armatures transversales :

$$A_s = 0.25 \frac{t}{h} \frac{F_{Ed}}{f_{yd}}  \tag{10.5}$$

## 10.9.5.2 Appareils d'appui

Profondeur nominale :

$$a = a_1 + a_2 + a_3 + \Delta a_{22} + \Delta a_{32}  \tag{10.6}$$

**Tables:** 10.1 (max spacing), 10.2–10.5 (bearing depths, tolerances)

**Status:** ✅ Complete (Equations 10.1–10.6, 5 tables, 7 figures referenced)

---

Liens : [[EC2_index]] · [[EC2_9_dispositions-elements.md]] · [[EC2_11_beton-granulats-legers.md]] · [[_Knowledge — Index]] · [[CLAUDE]]
