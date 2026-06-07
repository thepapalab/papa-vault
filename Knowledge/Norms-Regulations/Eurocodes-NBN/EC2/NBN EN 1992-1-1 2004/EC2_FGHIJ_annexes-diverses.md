---
title: "NBN EN 1992-1-1:2004 — Annexes diverses"
type: norm-extract
source: "NBN EN 1992-1-1:2004"
norm: EC2
section: "FGHIJ"
chapter: "Annexes diverses"
tags: [EC2, eurocode-2, annexes-diverses]
related: ["[[EC2_index]]", "[[EC2_E_durabilite.md]]", "[[]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# F.1 Généralités

## (1) Limitation : pas de calcul pour armatures comprimées

La présente annexe **ne contient pas d'expressions de calcul** pour les **armatures comprimées**.

---

## (2) Domaine d'application

Les armatures de béton armé **tendues** dans un élément soumis à des **contraintes planes orthogonales** $\sigma_{Edx}$, $\sigma_{Edy}$ et $\tau_{Edxy}$ peuvent être calculées en utilisant la méthode présentée ci-après.

### Conventions
Il convient de prendre :
- Des **valeurs positives** pour les contraintes de **compression**
- $\sigma_{Edx} > \sigma_{Edy}$
- Les directions des armatures **coïncident** avec les axes x et y

### Résistances à la traction des armatures

Il convient de déterminer les résistances à la traction apportées par les armatures à partir des expressions suivantes :

$$f_{tdx} = \rho_x f_{yd} \quad f_{tdy} = \rho_y f_{yd} \quad (F.1)$$

où :
- $\rho_x$, $\rho_y$ : ratios géométriques d'armature le long des axes x et y respectivement
- $f_{yd}$ : limite d'élasticité de calcul de l'acier

---

## (3) Cas sans armatures

Il n'y a pas lieu de prévoir des armatures lorsque **simultanément** :
- $\sigma_{Edx}$ et $\sigma_{Edy}$ sont **toutes deux des contraintes de compression**
- $\sigma_{Edx} \cdot \sigma_{Edy} > 2\tau_{Edxy}^2$

**Cependant**, la contrainte de compression maximale ne doit pas dépasser $f_{cd}$ (voir [[EC2_3.1.6_limites-compression.md|3.1.6]]).

---

## (4) Cas avec armatures requises

Lorsque **soit** :
- $\sigma_{Edy}$ est une **traction**
- **Soit** $\sigma_{Edx} \cdot \sigma_{Edy} \leq 2\tau_{Edxy}^2$

des **armatures sont à prévoir**.

### Armatures optimales : approche des directions principales

Les armatures de béton armé **optimales** (indice supérieur ′) et la **contrainte dans le béton** correspondante sont déterminées par :

#### Cas 1 : $\sigma_{Edx} \leq |\tau_{Edxy}|$

$$f'_{tdx} = |\tau_{Edxy}| - \sigma_{Edx} \quad (F.2)$$

$$f'_{tdy} = |\tau_{Edxy}| - \sigma_{Edy} \quad (F.3)$$

$$\sigma'_{cd} = 2|\tau_{Edxy}| \quad (F.4)$$

#### Cas 2 : $\sigma_{Edx} > |\tau_{Edxy}|$

$$f'_{tdx} = 0 \quad (F.5)$$

$$f'_{tdy} = \frac{\sigma_{Edy} - \sigma_{Edx}}{2\tau_{Edxy}} \quad (F.6)$$

$$\sigma'_{cd} = \sigma_{Edx} + \sqrt{\left(\frac{\sigma_{Edx}}{\tau_{Edxy}}\right)^2 + 1} \quad (F.7)$$

### Vérification de la contrainte de compression du béton

Il convient de vérifier que la contrainte dans le béton, $\sigma_{cd}$ n'excède pas $\nu f_{cd}$ avec une modélisation réaliste des sections fissurées (voir l'EN 1992-2).

Le coefficient $\nu$ peut être obtenu à partir de l'[[EC2_6.5_compression.md|Expression (6.5)]].

---

## (5) Approche alternative : directions quelconques

### Cas général

À défaut, dans le cas général, les armatures qui sont nécessaires, ainsi que la contrainte dans le béton, peuvent être déterminées par :

$$f_{tdx} = |\tau_{Edxy}|\cot\theta - \sigma_{Edx} \quad (F.8)$$

$$f_{tdy} = \frac{|\tau_{Edxy}|}{\cot\theta} - \sigma_{Edy} \quad (F.9)$$

$$\sigma_{cd} = \tau_{Edxy}\left(\cot\theta + \frac{1}{\cot\theta}\right) \quad (F.10)$$

où $\theta$ est l'**angle de la contrainte principale de compression** dans le béton par rapport à l'axe des x.

**Note :** Il convient de choisir $\cot\theta$ de façon à **éviter des valeurs de compression** pour $f_{td}$.

### Optimisation de la quantité d'armatures

Afin d'**éviter des fissures inacceptables aux ELS** et d'**assurer la capacité de déformation requise aux ELU**, il convient de limiter les sections des armatures obtenues pour chaque direction à partir des Expressions (F.8) et (F.9) dans la **fourchette de la moitié à deux fois** les sections d'armatures données par les Expressions (F.2) et (F.3) ou (F.5) et (F.6) :

$$\frac{1}{2}f'_{tdx} \leq f_{tdx} \leq 2f'_{tdx}$$

$$\frac{1}{2}f'_{tdy} \leq f_{tdy} \leq 2f'_{tdy}$$

### Minimum d'armatures

**Note :** On obtient la **quantité minimale d'armatures** si les **directions** de celles-ci sont **parallèles aux directions des contraintes principales**.

---

## (6) Ancrage aux bords libres

Il convient d'**ancrer totalement** les armatures de béton armé au droit de **tous les bords libres**, par exemple au moyen de **barres en U** ou similaires.

---

## Voir aussi

- [[EC2_6.5_compression.md|6.5]] — Treillis de bielles-tirants
- [[EC2_8.1_armatures.md|8.1]] — Généralités sur les armatures
- [[EC2_8.8_ancrage.md|8.8]] — Ancrage des armatures

# G.1 Interaction sol-structure — Fondations superficielles

## G.1.1 Généralités

### (1) Définition du problème

Il convient de prendre en compte l'**interaction entre le sol, les fondations et la structure**. La :
- **Distribution des pressions de contact** sur les fondations
- **Efforts dans les poteaux**

sont tous deux **dépendants des tassements différentiels**.

### (2) Approche générale

En général, le problème peut être traité en s'assurant de la **compatibilité** entre :
- Les **déplacements** et 
- Les **réactions correspondantes** du sol et de la structure

### (3) Incertitudes et niveaux d'analyse

Bien que le procédé général ci-dessus soit satisfaisant, des **incertitudes** continuent d'exister en raison de :
- L'**ordre d'application des charges**
- Les **effets du fluage**

Pour cette raison, **différents niveaux d'analyse** sont habituellement définis, selon le degré d'idéalisation des modèles mécaniques.

### (4) Hypothèse de structure souple

Si la structure est considérée comme **souple**, alors :
- Les charges transmises **ne dépendent pas des tassements différentiels** (pas de rigidité)
- Les charges **ne sont plus inconnues**
- Le problème se réduit à l'**analyse d'une fondation sur sol compressible**

### (5) Hypothèse de structure rigide

Si la structure est considérée comme **rigide**, alors :
- Les charges transmises par les fondations **sont inconnues**
- Elles peuvent être obtenues par la condition que les **tassements demeurent dans un plan**
- Il convient de **contrôler que cette rigidité persiste jusqu'à l'ELU**

### (6) Procédure simplifiée

Une procédure simplifiée peut être adoptée si :
- Le système de fondation peut être supposé **rigide**, ou
- Le sol porteur est **très rigide**

Dans ces cas, les **tassements différentiels peuvent être ignorés** et aucune **modification des charges** n'est requise.

### (7) Rigidité relative — Critère KR

Pour déterminer de manière approximative la **rigidité du système structural**, on peut comparer la rigidité combinée de la fondation, de l'ossature et des voiles de contreventement à la rigidité du sol.

La **rigidité relative** $K_R$ peut être estimée pour des structures de bâtiments par :

$$K_R = \frac{(EJ)_S}{E l^3} \quad (G.1)$$

où :
- $(EJ)_S$ : rigidité en flexion par unité de largeur de la structure (somme des rigidités en flexion : fondation + ossature + voiles)
- $E$ : module de déformation du sol
- $l$ : longueur de la fondation

**Interprétation :**
- $K_R > 0,5$ : système structural **rigide**
- $K_R < 0,5$ : système structural **souple**

---

## G.1.2 Niveaux d'analyse

### Niveau 0 — Distribution linéaire (simplifiée)

À ce niveau, on peut admettre une **distribution linéaire** de la pression de contact.

**Conditions préalables :**
- La pression de contact ne dépasse pas les valeurs de calcul **aux ELS et aux ELU**
- Aux ELS, le système structural **n'est pas affecté** par les tassements, ou les tassements différentiels **ne sont pas significatifs**
- Aux ELU, le système structural **possède une capacité de déformation plastique suffisante**

### Niveau 1 — Rigidité relative (déformations vérifiées)

La pression de contact peut être déterminée en tenant compte de la **rigidité relative** de la fondation et du sol; les déformations qui en résultent peuvent être évaluées.

**Conditions préalables :**
- Une **expérience suffisante** existe, prouvant que l'aptitude au service n'est pas affectée
- Aux ELU, le système structural a un **comportement ductile adéquat**

### Niveau 2 — Influence de la déformation du sol

À ce niveau, l'**influence des déformations du sol sur la structure** est prise en compte. La structure est analysée sous la **déformation imposée par la fondation** pour déterminer les **redistributions des charges**.

**Critique :** Si les redistributions sont **significatives (> 10 %)**, adopter le **Niveau 3**.

### Niveau 3 — Analyse interactive complète

**Méthode interactive complète**, prenant en compte :
- La structure
- Ses fondations
- Le sol

---

## G.2 Fondations sur pieux

### (1) Semelle rigide sur pieux

Si la semelle sur pieux est **rigide**, on peut faire l'hypothèse d'une **variation linéaire des tassements individuels** des pieux, dépendant de la **rotation de la semelle**.

Si cette rotation est **nulle ou peut être négligée**, un **tassement identique** de tous les pieux peut être admis.

À partir des **équations d'équilibre**, on peut calculer :
- Les **charges sur les pieux**
- La **valeur du tassement du groupe de pieux**

### (2) Radier sur pieux — Interactions complexes

Cependant, dans le cas d'un **radier sur pieux**, une **interaction** se produit :
- Entre les différents pieux
- Entre le radier et les pieux

Il **n'existe pas de méthode simple** pour traiter cette interaction.

### (3) Réponse du groupe sous charges latérales

La **réponse d'un groupe de pieux** à des **charges horizontales** implique :
- Les **rigidités latérales** des pieux et du sol
- La **rigidité axiale** (ex : charge latérale crée traction/compression aux pieux de rive)

---

## Voir aussi

- [[EC2_6_fondations.md|6]] — Calcul des fondations (EN 1992-1-1)
- [[EC2_11_beton-leger.md|11]] — Béton de granulats légers
- EN 1997-1 — Géotechnique (Calcul géotechnique)

---

Liens : [[EC2_index]] · [[EC2_E_durabilite.md]] · [[_Knowledge — Index]] · [[CLAUDE]]
