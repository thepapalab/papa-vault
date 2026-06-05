---
title: EN 1990 ANB — 04 — Annexes B, C, D — Fiabilité structurale et Classes de conséquences
type: norm-guide
source: "NBN EN 1990 ANB:2021 — Eurocode 0 : Bases de calcul des structures — Annexe nationale belge, NBN, 23-03-2021"
norms: [NBN EN 1990 ANB:2021, NBN EN 1990:2002, EN 1991-1-7, EN 1998-1]
authority: "Commission E250/E25001 — CSTC/SECO — Bureau de Normalisation (NBN)"
date: 2021-03
sections: [Annexe B, Annexe C, Annexe D]
tags: [EN1990, ANB, fiabilité, classes-conséquences, CC1, CC2, CC3, K_FI, ponts, bâtiments, structures-industrielles, belge]
related: ["[[EN 1990 ANB — Index]]", "[[EN 1990 ANB — 03 — A2 Ponts — ELU et ELS]]", "[[PTR CE01 — Index — FR]]"]
created: 2026-06-05
---

# EN 1990 ANB — 04 — Annexes B, C, D — Fiabilité structurale et Classes de conséquences

## Annexe B — Gestion de la fiabilité structurale pour les constructions

L'annexe B de l'EN 1990:2002 est **normative** pour l'application nationale en Belgique.

### Principe

Les coefficients γ_F utilisés pour les combinaisons fondamentales (situations durables) sont multipliés par un **coefficient K_{FI}** déterminé suivant le tableau B.3 de l'EN 1990.

Les constructions en RC_i sont associées avec :
- une classe de conséquence **CC_i**,
- une supervision de conception et de calcul **DSL_i**,
- un niveau d'inspection **IL_i**.

Pour une construction en **classe RC3** :
- les coefficients de sécurité sont augmentés suivant le Tableau B3,
- le contrôle de la conception doit satisfaire à la classe **DSL3**,
- l'inspection de l'exécution doit satisfaire à la classe **IL3**.

> Exception : les classes DSL3 et IL3 peuvent être évitées pour une construction RC3 si on applique K_{FI} = **1,2** pour les actions variables et K_{FI} = **1,1** pour les actions permanentes (au lieu de la valeur unique K_{FI} = 1,1). Cette approche alternative n'est pas la méthode privilégiée.

### Note sur la notion de classes de conséquences

La notion de classes de conséquences est définie dans l'EN 1990 (CC), l'EN 1991-1-7 (CCA), et sous le nom de catégories d'importance dans l'EN 1998-1. Ces classifications sont **distinctes** :
> Il n'est pas illogique qu'une habitation unifamiliale soit CC2 selon l'EN 1990 et CC1 selon l'EN 1991-1-7.

Pour éviter la confusion, les classes de conséquences définies dans l'EN 1991-1-7 (charges accidentelles) ont été renommées dans les ANB belges : **Classes de Conséquences en cas d'Accident (CCA)**.

---

### Tableau B.6 ANB — Classes de conséquences coordonnées des bâtiments

| Types de bâtiment | EN 1990 (tableau B.1) | EN 1991-1-7 (tableau A.1) | EN 1998-1 (tableau 4.3) |
|-------------------|-----------------------|---------------------------|------------------------|
| Bâtiments agricoles ou normalement inoccupés | CC1 | CCA1 | I |
| Maisons unifamiliales ou bâtiments < 2 niv. et < 100 m² total | CC2 | CCA1 | II |
| Bâtiments à conséquences moyennes, n'appartenant pas aux autres catégories, avec occupation simultanée max. < 500 personnes | CC2 | CCA2a | II |
| Bâtiments à conséquences importantes (école, salle de réunion, centre culturel, centre commercial) : < 15 niv. et occupation max. < 5000 personnes | CC2 | CCA2b | III |
| Bâtiments à conséquences importantes (école, salle de réunion, etc.) : > 15 niveaux | CC2 | CCA3 | III |
| Bâtiments à conséquences très importantes, occupation simultanée > 5000 personnes (salles de concert, tribunes) | CC3 | CCA3 | III |
| Bâtiments abritant des substances ou produits dangereux | CC3 | CCA3 | IV |
| Centrales électriques, hôpitaux, casernes, et autres bâtiments vitaux pour la protection civile | CC3 | CCA3 | IV |

---

### Tableau B.7 ANB — Classes de conséquences coordonnées des ponts et ouvrages d'art assimilés

| Types de ponts / ouvrages d'art assimilés (passerelles, viaducs, tunnels, etc.) | EN 1990 (tableau B.1) | EN 1991-1-7 (*) | EN 1998-1 (tableau 4.3) |
|----------------------------------------------------------------------------------|-----------------------|-----------------|------------------------|
| Éléments secondaires (selon définition A1.1(1) ANB) | **CC1** | — | I |
| Passerelle sur voie d'eau | **CC2** | (*) | II |
| Ouvrage non compris dans les autres catégories | **CC2** | (*) | III |
| Pont-route sur itinéraire important (TMJ > 50 000 veh/j) dont le remplacement rapide est problématique (travée(s) > 30 m, accessibilité pour le remplacement gênée par une autre infrastructure) | **CC3** | (*) | III |
| Pont-rail sur une ligne ferroviaire importante (LGV ou autre ligne fixée par l'organisme responsable de l'infrastructure ferroviaire — Infrabel) | **CC3** | (*) | III |
| Pont-canal (d'une voie navigable au-dessus d'un obstacle) | **CC3** | (*) | III |

> (*) Le tableau A.1 de l'EN 1991-1-7, destiné aux bâtiments, n'est pas directement applicable aux ponts. Par type de pont, il y a lieu d'appliquer les principes du chapitre 3.3 de l'EN 1991-1-7 avec les prescriptions relatives à chaque ouvrage individuel (vérification que la défaillance locale d'un élément structural n'entraîne pas la ruine générale : ex. accrochage d'une poutre de rive, défaillance d'une suspente de pont à haubans, défaillance d'un piston de pont mobile).

> **Conséquence pour les ponts ferroviaires Infrabel :** Tous les ponts-rails sur lignes ferroviaires importantes (désignées par Infrabel, y compris la LGV) sont en **CC3**. Ceci est également imposé par le PTR CE01 (voir [[PTR CE01 — Index — FR]]).

---

### Tableau B.8 ANB — Classes de conséquences coordonnées des structures industrielles

| Types de structures industrielles | EN 1990 (tableau B.1) | EN 1991-1-7 (**) | EN 1998-1 (tableau 4.3) |
|-----------------------------------|-----------------------|-----------------|------------------------|
| Structure industrielle à 1 seul niveau < 100 m² ; éléments secondaires d'autres structures | CC1 | CCA1 | I |
| Structure industrielle « à risque ordinaire » | CC2 | CCA2a | II |
| Structure industrielle « à haut risque » (pertes de vie importantes, ou conséquences économiques/sociales/environnementales très importantes) | CC3 | CCA3 | III |
| Parties vitales de centrales électriques et structures couvertes par la Directive Seveso (***) | CC3 | CCA3 | IV |

> Le choix de la classe de conséquence est du ressort du maître d'ouvrage sauf dans les cas prévus par la loi.

> (***) Directive 96/82/CE et ses modificatrices (notamment 2003/105/CE), transposée en Belgique par Accord de Coopération (21/06/1999, modifié 01/06/2006) et loi du 22/05/2001. Voir [www.seveso.be](http://www.seveso.be).

---

## Annexe C — Base pour la méthode des coefficients partiels et l'analyse de la fiabilité

L'annexe C de l'EN 1990:2002 conserve en Belgique un **caractère informatif**.

- Son utilisation pour **différencier la fiabilité** (concevoir des structures de fiabilité différente de l'Annexe A) est soumise à l'approbation du client et de l'autorité compétente, sauf si la norme produit concernée prévoit cette utilisation.
- Son utilisation pour **concevoir des structures de même fiabilité** que celles conçues selon l'Annexe A est également soumise à l'approbation du client et de l'autorité compétente.

---

## Annexe D — Dimensionnement assisté par l'expérimentation

L'annexe D de l'EN 1990:2002 conserve en Belgique un **caractère informatif**.

---

Liens : [[EN 1990 ANB — Index]] · [[EN 1990 ANB — 03 — A2 Ponts — ELU et ELS]] · [[PTR CE01 — Index — FR]]
