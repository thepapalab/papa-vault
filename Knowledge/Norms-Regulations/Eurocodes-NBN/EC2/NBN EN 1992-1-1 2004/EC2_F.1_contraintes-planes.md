---
title: "F.1 Généralités — Expressions pour le calcul des armatures en contraintes planes"
source: "EN 1992-1-1:2004 (F)"
norm: EC2
section: "F.1"
chapter: "Annexe F"
part: "Informative"
tags: [EC2, contraintes-planes, armatures-tendues, béton-armé, orthogonal]
language: fr
jupyter_ref: "EC2/F.1"
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
