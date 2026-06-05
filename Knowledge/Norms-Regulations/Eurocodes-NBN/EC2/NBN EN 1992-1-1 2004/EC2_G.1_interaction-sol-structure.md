---
title: "G.1 Fondations superficielles — Interaction sol-structure"
source: "EN 1992-1-1:2004 (F)"
norm: EC2
section: "G.1"
chapter: "Annexe G"
part: "Informative"
tags: [EC2, interaction-sol-structure, tassements, fondations, rigidité-relative]
language: fr
jupyter_ref: "EC2/G.1"
---

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
