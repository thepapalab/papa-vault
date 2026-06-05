---
title: EN 1990 ANB — 01 — Annexe A1 : Bâtiments — Coefficients ψ et ELU
type: norm-guide
source: "NBN EN 1990 ANB:2021 — Eurocode 0 : Bases de calcul des structures — Annexe nationale belge, NBN, 23-03-2021"
norms: [NBN EN 1990 ANB:2021, NBN EN 1990:2002, NBN B 03-003, EN 1997]
authority: "Commission E250/E25001 — CSTC/SECO — Bureau de Normalisation (NBN)"
date: 2021-03
sections: [A1.1, A1.2, A1.2.1, A1.2.2, A1.3, A1.3.1, A1.3.2, A1.4, A1.4.2]
tags: [EN1990, ANB, bâtiments, coefficients-psi, ELU, ELS, coefficients-partiels, gamma, géotechnique, fiabilité-CC2]
related: ["[[EN 1990 ANB — Index]]", "[[EN 1990 ANB — 00 — Avant-Propos et Introduction]]", "[[EN 1990 ANB — 02 — A2 Ponts — Combinaisons et ψ]]"]
created: 2026-06-05
---

# EN 1990 ANB — 01 — Annexe A1 : Bâtiments — Coefficients ψ et ELU

## A1.1 Domaine d'application

(1) Les principes et exigences de l'EN 1990 s'appliquent aux **éléments structuraux**. Les valeurs des coefficients et critères fixés par cette annexe ne s'appliquent qu'aux éléments structuraux.

Pour les **éléments secondaires** (éléments dont le mode de remplacement est prévu lors de la construction et dont la défaillance n'affecte que leur propre stabilité et les éléments de remplissage qu'ils supportent), un niveau de fiabilité plus faible est admis, avec des coefficients de sécurité et de combinaison différents.

Peuvent être considérés comme éléments secondaires :
- les façades rideaux, ensembles menuisés et châssis utilisés en façades ;
- en toiture, les châssis (si aucune charge d'exploitation particulière autre que catégorie H) ;
- les cloisons, faux-planchers et faux-plafonds.

> Les éléments supportant des charges de circulation de personnes (marches d'escalier), et les éléments de protection des éléments structuraux (protection résistante au feu), font **partie intégrante des éléments structuraux**.

(2) La durée d'utilisation du projet est de préférence fixée par le maître de l'ouvrage. Pour les bâtiments : entre **50 ans** (structures courantes — catégorie 4) et **100 ans** (structures monumentales — catégorie 5).

---

## A1.2 Combinaisons d'actions

### A1.2.1 Généralités

(1) La note 1 (projet individuel selon accord du client et de l'autorité compétente) est d'application conditionnelle en Belgique.

### A1.2.2 Valeurs des coefficients ψ

#### Tableau A1.1 ANB — Coefficients ψ pour les bâtiments (normative)

| Action | ψ₀ | ψ₁ | ψ₂ |
|--------|----|----|-----|
| **Charges d'exploitation (EN 1991-1-1)** | | | |
| Catégorie A : habitation, usage résidentiel | 0,7 | 0,5 | 0,3 |
| Catégorie B : bureaux | 0,7 | 0,5 | 0,3 |
| Catégorie C : lieux de réunion (sauf A, B, D) | 0,7 | 0,7 | 0,6 |
| Catégorie D : commerces | 0,7 | 0,7 | 0,6 |
| Catégorie E : aires de stockage | 1,0 | 0,9 | 0,8 |
| Catégorie F : trafic/stationnement véhicules légers (poids ≤ 30 kN, < 8 places) | 0,7 | 0,7 | 0,6 |
| Catégorie G : trafic/stationnement véhicules moyens (30 kN < poids ≤ 160 kN) | 0,7 | 0,5 | 0,3 |
| Catégorie H : toitures | 0 | 0 | 0 |
| **Actions de la neige et de la glace (EN 1991-1-3)** | | | |
| Pour toute la Belgique (altitude H ≤ 1000 m) | 0,5 ³⁾ | 0 ⁴⁾ | 0 |
| **Actions du vent sur les bâtiments (EN 1991-1-4)** | 0,6 ³⁾ | 0,2 ⁵⁾ | 0 |
| **Actions de la température — hors incendie (EN 1991-1-5)** | 0,6 | 0,5 | 0 |
| **Tassements (EN 1997)** | 1,0 | 1,0 | 1,0 |
| **Actions particulières pendant l'exécution ²⁾ (EN 1991-1-6)** | 1,0 | — | 0,2 |

> ¹⁾ Pour les machines, les coefficients ψ sont à déterminer au cas par cas. Pour les pressions de fluides, voir l'Annexe A4 de l'EN 1990 ou utiliser les coefficients de la catégorie E en attendant l'ANB complétée.

> ²⁾ Les coefficients ψ pour les charges d'exécution sont à déterminer si nécessaire au cas par cas.

> ³⁾ **Règle belge spécifique** : Lorsqu'une action de courte durée (< 1 mois : par ex. charge de neige, action du vent) accompagne dans une combinaison une autre action de courte durée, **ψ₀ = 0,3** pour la seconde action variable lorsque celle-ci est une charge de neige, une action du vent ou une action due à la température. Justification : l'effet simultané d'actions de courte durée est extrêmement improbable (issue de la NBN B03-101:1994 et de l'article D'Havé & Spehl, Annales des Travaux Publics, 1984).

> ⁴⁾ La valeur fréquente de la charge de neige est quasiment nulle selon les calculs de l'Institut Royal Météorologique.

> ⁵⁾ Pour les ELS, les valeurs de ψ₀ et ψ₁ peuvent dépendre du critère de service (voir A1.4.2(2)).

---

## A1.3 États-limites ultimes

### A1.3.1 Valeurs de calcul des actions dans les situations de projet durables et transitoires

(1) NOTE : Les valeurs recommandées des tableaux A1.2(A) à (C) sont **normatives** en Belgique.

**Informations non contradictoires :**
- La pression de l'eau ou d'un autre fluide est en général à considérer comme action variable. γ_Q peut être réduit à γ_{G,sup} si la présence du liquide est limitée par des conditions géométriques ou hydrauliques et si sa masse volumique est relativement stable.
- Dans les cas courants, le niveau de sécurité normal correspond à la **classe de conséquence CC2** (β = 3,8 pour 50 ans).
- CC1 (sécurité réduite) : mât d'éclairage en zone inhabitée, brise-lame, etc.
- CC3 (sécurité renforcée) : barrage, réservoirs de produits toxiques, etc.

#### NOTE 1 du Tableau A1.2(A) — EQU (valeurs normatives, CC2)

| Coefficient | Valeur normative |
|-------------|-----------------|
| γ_{G,j,sup} | **1,10** |
| γ_{G,j,inf} | **0,90** |
| γ_{Q,1} | **1,50** si non favorable (0 si favorable) |
| γ_{Q,i} | **1,50** si non favorable (0 si favorable) |

> La NOTE 2 du Tableau A1.2(A) (vérification combinée optionnelle) n'est **pas d'application** en Belgique.

#### NOTE 1 du Tableau A1.2(B) — STR/GEO

Autant l'application de l'équation 6.10 que celle des équations 6.10a et 6.10b sont autorisées.

#### NOTE 2 du Tableau A1.2(B) — STR/GEO (valeurs normatives, CC2)

| Coefficient | Valeur normative |
|-------------|-----------------|
| γ_{G,j,sup} | **1,35** |
| γ_{G,j,inf} | **1,00** |
| γ_{Q,1} | **1,50** si non favorable (0 si favorable) |
| γ_{Q,i} | **1,50** si non favorable (0 si favorable) |
| ξ | **0,85** → ξγ_{G,j,sup} = 0,85 × 1,35 ≅ **1,15** |

> **Exception géotechnique** : ξ = **1,00** est toujours utilisé pour les applications géotechniques.

#### NOTE 4 du Tableau A1.2(B) — γ_{Sd} (incertitude de modélisation)

Applicable uniquement si l'approche probabiliste détaillée (Annexe C) est autorisée. Dans ce cas, γ_G ou γ_Q peut être remplacé par γ_g (ou γ_q) × γ_{Sd}. Valeurs suggérées :
- γ_{Sd} = **1,05** — modèles à faible incertitude (charges sur constructions isostatiques)
- γ_{Sd} = **1,10** — modèles intermédiaires
- γ_{Sd} = **1,15** — constructions à haut degré d'hyperstaticité

#### NOTE du Tableau A1.2(C) — GEO (valeurs normatives, toutes classes)

| Coefficient | Valeur normative |
|-------------|-----------------|
| γ_{G,j,sup} | **1,00** |
| γ_{G,j,inf} | **1,00** |
| γ_{Q,1} | **1,30** si non favorable (0 si favorable) |
| γ_{Q,i} | **1,30** si non favorable (0 si favorable) |

#### (5) Calculs STR/GEO — Approche géotechnique en Belgique

**L'Approche 1** est applicable en Belgique :
> Application, dans des calculs séparés, de valeurs de calcul provenant du tableau A1.2(C) et du tableau A1.2(B) aux actions géotechniques ainsi qu'aux autres actions appliquées à la structure. Dans les cas courants, le **dimensionnement des fondations** est régi par le tableau A1.2(C) et la **résistance structurale** est régie par le tableau A1.2(B).

### A1.3.2 Valeurs de calcul des actions dans les situations de projet accidentelles et sismiques

#### Tableau A1.3 ANB — Valeurs de calcul pour les combinaisons accidentelles et sismiques

| Situation | Actions permanentes | Action acc./sismique | Action variable principale | Autres |
|-----------|--------------------|--------------------|---------------------------|--------|
| Accidentelle (*) (Éq. 6.11a/b) | G_{k,j,sup}, G_{k,j,inf} | A_d | ψ_{1,1} Q_{k,1} | ψ_{2,i} Q_{k,i} |
| Sismique (Éq. 6.12a/b) | G_{k,j,sup}, G_{k,j,inf} | γ_I A_{Ek} ou A_{Ed} | — | ψ_{2,i} Q_{k,i} |

> (*) L'action variable principale est prise avec sa **valeur fréquente** ψ_{1,1} Q_{k,1}.
> Exception incendie (NBN EN 1991-1-2 ANB) : l'action variable d'accompagnement principale Q₁ est prise avec sa **valeur quasi-permanente** (coefficient ψ₂), sauf pour l'action du vent (valeur fréquente ψ₁).

> NOTE : γ = **1,0** pour toutes les actions non sismiques, y compris la précontrainte.

---

## A1.4 États-limites de service

### A1.4.2 Critères d'aptitude au service

(2) Les critères applicables en Belgique :

**Pour les ELS liés au comportement des matériaux structuraux** (ouvertures de fissure, etc.) : les Eurocodes « matériaux » sont applicables.

**Pour les ELS de déformation :**
- Incidence sur les parachèvements et l'utilisation des bâtiments : **NBN B 03-003** (répond aux prescriptions de A1.4.3).
- NOTE : Au tableau 3 de la NBN B 03-003, remplacer les valeurs limites pour le cas 12 (pont roulant) par celles du tableau 7.1 de la **NBN EN 1993-6**, quel que soit le matériau de structure.

**Pour les ELS de résistance et de service sous l'effet des vibrations :**
- A1.4.4(1) complété : critères = **NBN B 03-003 (article 8)**.
- A1.4.4(2) complété : l'amplification par résonance peut être négligée si les fréquences propres sont supérieures aux valeurs critiques :
  - Effets du vent : **EN 1991-1-4 (article 6.2)** (condition c_s · c_d = 1)
  - Mouvements synchronisés de personnes dans les bâtiments : **NBN B 03-003 (tableau 6)**
  - Passerelles pour piétons :
    - Vibrations verticales : **4,5 Hz**
    - Vibrations horizontales : **3,5 Hz**

---

Liens : [[EN 1990 ANB — Index]] · [[EN 1990 ANB — 00 — Avant-Propos et Introduction]] · [[EN 1990 ANB — 02 — A2 Ponts — Combinaisons et ψ]]
