---
title: "D.1 Généralités — Méthode de calcul des pertes par relaxation"
source: "EN 1992-1-1:2004 (F)"
norm: EC2
section: "D.1"
chapter: "Annexe D"
part: "Informative"
tags: [EC2, précontrainte, relaxation, temps-équivalent, pertes-contrainte]
language: fr
jupyter_ref: "EC2/D.1"
---

# D.1 Généralités

## (1) Contexte et méthode du temps équivalent

Lorsque les pertes par relaxation sont calculées pour **différents intervalles de temps (étapes)** où la contrainte dans l'armature de précontrainte **n'est pas constante** (en raison, par exemple, du raccourcissement élastique du béton), il convient d'adopter une **méthode basée sur le principe du temps équivalent**.

---

## (2) Concept de la méthode du temps équivalent

Le concept est présenté sur la Figure D.1 (voir source originale). Au temps $t_i$ il y a une **déformation instantanée** de l'armature de précontrainte, avec :

| Symbole | Signification |
|---------|---------------|
| $\sigma_{p,i}^-$ | Contrainte de traction dans l'armature de précontrainte **juste avant** $t_i$ |
| $\sigma_{p,i}^+$ | Contrainte de traction dans l'armature de précontrainte **juste après** $t_i$ |
| $\sigma_{p,i-1}^+$ | Contrainte de traction dans l'armature de précontrainte à l'**étape précédente** |
| $\Delta\sigma_{pr, i-1}$ | Valeur absolue de la perte par relaxation pendant l'**étape précédente** |
| $\Delta\sigma_{pr,i}$ | Valeur absolue de la perte par relaxation de l'**étape considérée** |

---

## (3) Calcul du temps équivalent

Soit $\sum_{j=1}^{i-1} \Delta\sigma_{pr,j}$ la somme de toutes les pertes par relaxation des étapes précédentes.

**Le temps équivalent** $t_e$ (en heures) est défini comme le temps qui vérifie les expressions des pertes par relaxation en fonction du temps définies en **3.3.2 (7)**, avec :

- **Contrainte initiale équivalente :** $\sigma_{p,i}^+ + \sum_{j=1}^{i-1}\Delta\sigma_{pr,j}$

- **Rapport de contrainte normalisée :** $\mu = \frac{\sigma_{p,i}^+ + \sum_{j=1}^{i-1}\Delta\sigma_{pr,j}}{f_{pk}}$

où $f_{pk}$ est la résistance caractéristique en traction de l'armature de précontrainte.

---

## (4) Application pour armatures de classe 2

Par exemple, pour une armature de précontrainte de la **Classe 2**, $t_e$ est donné par l'Expression (3.31), qui s'écrit :

$$\Delta\sigma_{pr,j} = 10^{0.75(1-\rho) - 9.09 e^{-t_e/1000}} \cdot \mu^{0.66} \quad (D.1)$$

où :
- $\rho$ : coefficient dépendant du type de ciment
- $\mu$ : rapport de contrainte normalisée (voir D.1 (3))
- $t_e$ : temps équivalent (heures)

---

## (5) Calcul de la perte à l'étape considérée

Après résolution de l'équation ci-dessus pour $t_e$, la même formule peut être appliquée afin d'estimer la **perte par relaxation de l'étape considérée**, $\Delta\sigma_{pr, i}$ (où le temps équivalent $t_e$ est ajouté à l'intervalle de temps considéré) :

$$\Delta\sigma_{pr,i} = 10^{0.75(1-\rho) - 9.09 e^{-(t_e + \Delta t_i)/1000}} \cdot \mu^{0.66} - 10^{0.75(1-\rho) - 9.09 e^{-t_e/1000}} \cdot \mu^{0.66} \quad (D.2)$$

où $\Delta t_i$ est la durée de l'étape considérée.

---

## (6) Généralisation aux trois classes

Le même principe s'applique pour chacune des **trois classes d'armature de précontrainte** (classe 1, 2 et 3), avec des coefficients numériques adaptés.

---

## Voir aussi

- [[EC2_3.3.2_relaxation.md|3.3.2]] — Expressions de relaxation (Classe 1, 2, 3)
- [[EC2_3.3_precontrainte.md|3.3]] — Acier de précontrainte
- [[EC2_5.10_elements-precontraints.md|5.10]] — Éléments précontraints
