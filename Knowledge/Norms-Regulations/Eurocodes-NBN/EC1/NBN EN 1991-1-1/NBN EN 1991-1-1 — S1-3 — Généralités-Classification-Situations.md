---
title: "NBN EN 1991-1-1 S1-3 — Généralités, Classification, Situations de projet"
type: norm-extract
source: "NBN EN 1991-1-1:2002 (+ AC:2009)"
norm: EC1-1
section: "1-3"
tags: [EC1-1, NBN, généralités, définitions, symboles, classification-actions, situations-projet, charges-permanentes, charges-exploitation]
related: ["[[NBN EN 1991-1-1 — Index]]", "[[NBN EN 1991-1-1 — S4-5 — Poids-Volumiques-Poids-Propre]]", "[[NBN EN 1991-1-1 — S6 — Charges-Exploitation]]"]
language: fr
jupyter_ref: "EC1-1/1-3"
created: 2026-06-07
---

# Sections 1 à 3 — Généralités, Classification, Situations de projet

## Section 1 — Généralités

### 1.1 Domaine d'application

**(1)** L'EN 1991-1-1 définit des actions pour la conception structurale des bâtiments et ouvrages de génie civil :
- poids volumiques des matériaux de construction et stockés ;
- poids propre des constructions ;
- charges d'exploitation pour les bâtiments.

**(4)** Les charges d'exploitation (section 6) sont définies par catégorie d'usage : résidentiel/social/commercial/administratif ; garages et circulation de véhicules ; stockage et activités industrielles ; toitures ; hélistations.

**(5)** Aires de circulation : véhicules de **PTAC ≤ 160 kN**. Au-delà → accord avec l'autorité concernée + EN 1991-2.

**(6)** Barrières / murs faisant fonction de barrière : forces horizontales en section 6 ; parkings → Annexe B.

> [!note] Renvois
> - Chocs de véhicules → EN 1991-1-7 et EN 1991-2.
> - Eau et autres matériaux dans silos/réservoirs → EN 1991-4.
> - Pression des terres → EN 1997.

### 1.2 Références normatives

Citées dans les clauses normatives : EN 1990, EN 1991-1-7, EN 1991-2, EN 1991-3, EN 1991-4.
Citées dans les notes : EN 1991-1-3 (neige), EN 1991-1-4 (vent), EN 1991-1-6 (exécution).

### 1.3 Principes et Règles d'Application

- **Principes (P)** : énoncés généraux, définitions et modèles sans alternative ; identifiés par le numéro suivi de **P**.
- **Règles d'Application** : règles reconnues conformes aux Principes ; identifiées par un numéro entre parenthèses.
- Une règle alternative est admissible si la conformité aux Principes est démontrée à niveau de sécurité, d'aptitude au service et de durabilité au moins équivalent.

> [!warning] Conformité et marquage CE
> Si une Règle d'Application est remplacée par une autre règle, le dimensionnement ne peut être déclaré pleinement conforme à l'EN 1991-1-1. Pour une propriété relevant de l'Annexe Z d'une norme produit, une règle de calcul différente peut être inacceptable pour le marquage CE.

### 1.4 Termes et définitions

| Terme | Définition |
|-------|-----------|
| **poids volumique apparent** | Poids d'un matériau par unité de volume, pour une distribution normale de micro-vides, vides et pores. (angl. abrégé « density ») |
| **angle de talus naturel φ** | Angle formé naturellement avec l'horizontale par les côtés d'un tas de matériaux en vrac. |
| **poids total autorisé en charge (PTAC)** | Poids propre du véhicule + charge utile autorisée. |
| **éléments structuraux** | Ossature et structures d'appui (ponts : poutres principales, dalles, haubans…). |
| **éléments non structuraux** | Finitions, décorations, revêtements de chaussée, garde-corps non structuraux, équipements et réseaux fixés en permanence. |
| **cloisons** | Murs non porteurs. |
| **cloisons mobiles** | Cloisons déplaçables, ajoutables, supprimables ou reconstructibles ailleurs. |

### 1.5 Symboles

**Majuscules latines** — A : aire chargée ; A₀ : aire de référence (= 10 m²) ; Qk : valeur caractéristique d'une charge concentrée variable.

**Minuscules latines** — gk : poids par unité de surface ou de longueur ; n : nombre d'étages ; qk : valeur caractéristique d'une charge uniformément répartie ou linéique.

**Minuscules grecques** — αA : coefficient de réduction (aire) ; αn : coefficient de réduction (étages) ; γ : poids volumique apparent ; φ (φ majuscule dyn.) : coefficient de majoration dynamique ; ψ₀ : coefficient de combinaison (EN 1990, Tableau A.1.1) ; φ : angle de talus naturel [°].

---

## Section 2 — Classification des actions

### 2.1 Poids propre

**(1)** Classer le poids propre comme **action permanente fixe** (EN 1990, 1.5.3 et 4.1.1).

**(2)** Si le poids propre peut varier dans le temps : considérer valeurs caractéristiques supérieure et inférieure (EN 1990, 4.1.2). S'il est libre (ex. cloisons mobiles, voir 6.3.1.2(8)) : le traiter comme charge d'exploitation supplémentaire.

**(3)P** Les charges dues au **ballast** sont des actions permanentes ; tenir compte d'une redistribution éventuelle (voir 5.2.2).

**(4)P** Le poids des **terres** sur toits et terrasses est une action permanente.

**(5)** Tenir compte des variations de teneur en eau et d'épaisseur (accumulation incontrôlée) sur la durée de vie de calcul.

### 2.2 Charges d'exploitation

**(1)P** Sauf indication contraire, classer les charges d'exploitation comme **actions variables libres** (EN 1990, 1.5.3 et 4.1.1). Ponts → EN 1991-2.

**(2)** Choc de véhicules ou charges accidentelles de machines → EN 1991-1-7.

**(3)** Considérer les charges d'exploitation comme **quasi-statiques**. Risque de résonance (mouvements rythmés, danse, sauts) → modèle pour analyse dynamique particulière. *(PDN : procédure en Annexe Nationale.)*

**(4)** Chariots élévateurs et hélicoptères : tenir compte des forces d'inertie via le coefficient de majoration dynamique φ appliqué aux charges statiques (expression 6.3).

**(5)P** Les actions provoquant une accélération significative sont des **actions dynamiques** à traiter par analyse dynamique.

---

## Section 3 — Situations de projet

### 3.1 Généralités

**(1)P** Charges permanentes et d'exploitation à déterminer pour chaque situation de projet (EN 1990, 3.2).

### 3.2 Charges permanentes

**(1)** Considérer le poids propre total (éléments structuraux + non structuraux) comme **une action unique** (EN 1990, Tableau A.1.2(B) note 3).

**(2)** Surfaces avec retrait/ajout possible d'éléments : prendre en compte les cas de charge critiques.

**(3)** Tenir compte des revêtements et canalisations ajoutés après exécution (voir 5.2).

**(4)P** Le niveau de l'eau est pris en compte dans les situations concernées (EN 1997).

**(5)** Stockage : tenir compte de la provenance et teneur en eau des matériaux en vrac. *(Les poids volumiques de l'Annexe A concernent les matériaux à l'état sec.)*

### 3.3 Charges d'exploitation

#### 3.3.1 Généralités

**(1)P** Surfaces supportant différentes catégories : dimensionner pour le **cas de charge le plus critique**.

**(2)P** Charges d'exploitation simultanées avec d'autres actions variables (vent, neige, grues, machines) : la charge d'exploitation totale du cas de charge est traitée comme **une action unique**.

**(3)** Risque de fatigue (variations / vibrations) : établir un modèle de charge de fatigue.

**(4)** Structures sensibles aux vibrations : envisager des modèles dynamiques (EN 1990, 5.1.3).

#### 3.3.2 Dispositions complémentaires pour les bâtiments

**(1)** [AC:2009 — texte révisé]

> [!info] AC:2009 — réécriture du 3.3.2(1)
> Texte d'origine 2002 : « Sur les toitures, il convient de ne pas appliquer simultanément les surcharges d'exploitation et les charges dues à la neige ou au vent. »
> **Remplacé par :** « Sur les toitures (en particulier de catégorie H), il n'est pas nécessaire d'appliquer les charges d'exploitation combinées aux charges dues à la neige et/ou au vent. »

> [!note] Précision ANB belge
> L'avant-propos national (commission NBN E25001) lève la contradiction avec 3.3.1(1)P : la non-combinaison s'applique **uniquement aux états-limites de service des toitures de catégorie H**.

**(2)P** Lorsque la charge d'exploitation est action d'accompagnement (EN 1990), **un seul** des deux facteurs ψ₀ (EN 1990, Tableau A.1.1) et αn (6.3.1.2(11)) est appliqué.

**(3)** Charges dynamiques de machines → EN 1991-3.

**(4)** Spécifier les charges d'exploitation pour les vérifications ELS selon les conditions de service et exigences de performance.

---

Links: [[NBN EN 1991-1-1 — Index]] · [[NBN EN 1991-1-1 — S4-5 — Poids-Volumiques-Poids-Propre]] · [[NBN EN 1991-1-1 — S6 — Charges-Exploitation]]
