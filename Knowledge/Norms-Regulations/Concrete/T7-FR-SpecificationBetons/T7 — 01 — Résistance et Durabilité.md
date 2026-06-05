---
title: T7 — §1.1–1.3 Résistance et Durabilité (Données de base A, B1, B2)
type: norm-guide
source: "T7 — Prescription des bétons selon NBN EN 206:2013+A1:2016 & NBN B 15-001:2018, FEBELCEM, Janvier 2020"
norms: [NBN EN 206:2013+A1:2016, NBN B 15-001:2018]
authority: "FEBELCEM — Ir J.-F. Denoël"
date: 2020-01
sections: [1.1, 1.2, 1.3]
tags: [béton, résistance, durabilité, classe-environnement, domaine-utilisation, T7]
related: ["[[T7 — Index]]", "[[T7 — 00 — Avant-Propos et Normes]]", "[[T7 — 02 — Consistance Dmax et Données E]]"]
created: 2026-06-05
---

# T7 — §1.1–1.3 — Résistance et Durabilité (Données de base A, B1, B2)

## §1.1 Exigence générale

> Le béton doit satisfaire aux normes **NBN EN 206:2013+A1:2016** & **NBN B 15-001:2018**.

C'est la première donnée de base, toujours obligatoire.

---

## §1.2 Donnée de base A : Classe de résistance

La résistance à la compression est la caractéristique la plus importante d'un béton durci. Elle sert de base au calcul et au dimensionnement des structures.

La norme définit **16 classes de résistance**, de **C8/10 à C100/115**. Chaque classe est désignée par la lettre C suivie de :
- **f_ck,cyl** : résistance caractéristique sur cylindre (300 × Ø150 mm) → utilisé pour le calcul
- **f_ck,cube** : résistance caractéristique sur cube (150 mm) → utilisé pour le contrôle qualité

> La prescription d'un béton à performances spécifiées exige **toujours** la fixation d'une classe de résistance parmi les 16 classes de la norme.

### Remarques

- Pour le **béton léger**, les classes de résistance sont désignées par **LC** (au lieu de C).
- f_ck représente la résistance dépassée par au moins **95 %** des résultats d'essais.
- Les éprouvettes cubiques sont conservées sous eau pendant **28 jours à (20 ± 2) °C** (ou HR ≥ 95 %).
- La classe de résistance **A** (dimensionnement structural) doit être **≥** à la classe de résistance minimale résultant de la classe d'environnement **B2** (pour ne pas sous-estimer le pourcentage minimal d'armature et la largeur des fissures).

### Classes de résistance normalisées

C8/10 · C12/15 · C16/20 · C20/25 · C25/30 · C30/37 · C35/45 · C40/50 · C45/55 · C50/60 · C55/67 · C60/75 · C70/85 · C80/95 · C90/105 · C100/115

---

## §1.3 Donnée de base B : Durabilité — Domaine d'utilisation (B1) et Classe d'environnement (B2)

> La prescription d'un béton à performances spécifiées exige **toujours** de préciser le domaine d'utilisation (B1) et la classe d'environnement (B2).

### B1 — Domaine d'utilisation

| Symbole | Désignation | Teneur max. en ions Cl |
|---------|-------------|------------------------|
| **BNA** | Béton non armé | 1,00 % |
| **BA** | Béton armé | 0,40 % |
| **BP** | Béton précontraint | 0,20 % |

*(% par rapport au poids du ciment, incluant additions de type II. Interdit : chlorure de calcium ou adjuvants chlorés dans BA/BP)*

Pour le BA en environnement avec risque d'apport en ions chlore, une classe Cl 0,20 peut être exigée comme donnée complémentaire E.

### B2 — Classes d'environnement (NBN B 15-001:2018)

L'approche belge simplifie l'approche européenne basée sur les classes d'exposition en définissant **13 classes d'environnement**. Une seule classe suffit sauf pour les environnements agressifs (EA), où deux classes doivent être spécifiées simultanément (ex. : EA1 + EE2).

**Correspondances :** XA1/XA2/XA3 (classes d'exposition NBN EN 206) ↔ EA1/EA2/EA3 (classes d'environnement).

---

## Tableau 1 — Exigences de durabilité par classe d'environnement

*(BNA = béton non armé, BA = béton armé, BP = béton précontraint)*

| Symbole | Description | Type BNA | Exig. compl. BNA | Type BA/BP | Exig. compl. BA/BP |
|---------|-------------|----------|-----------------|------------|-------------------|
| **E0** | Environnement non agressif (BNA uniquement) | T(1,00) | (b) | *N/A* | — |
| **EI** | Environnement intérieur sec | T(1,00) | — | T(0,65) | — |
| **EE1** | Extérieur/intérieur humide — Pas de gel | T(1,00) | — | T(0,60) | — |
| **EE2** | Gel, pas de contact eau de pluie ou projetée | T(0,55) | — | T(0,55) | — |
| **EE3** | Gel + contact eau de pluie et/ou eau projetée | T(0,50) ou T(0,55)A | (c) | T(0,50) ou T(0,50)A | (c) |
| **EE4** | Gel + agents de déverglaçage | T(0,45) ou T(0,50)A | (c) | T(0,45) ou T(0,45)A | (c) |
| **ES1** | Air marin (≤ 3 km côte)/eau saumâtre — Pas de gel | T(0,60) | — | T(0,50) | — |
| **ES2** | Air marin (≤ 3 km côte)/eau saumâtre — Gel | T(0,50) ou T(0,55)A | (c) | T(0,50) ou T(0,50)A | (c) |
| **ES3** | Contact direct eau de mer — Immergé | T(0,55) | — | T(0,45) | — |
| **ES4** | Zone de marnage et d'éclaboussures | T(0,45) ou T(0,50)A | (c) | T(0,45) ou T(0,45)A | (c) |
| **EA1** | Chimiquement peu agressif (tableau 2 NBN EN 206) | T(0,55) | — | T(0,55) | — |
| **EA2** | Chimiquement moyennement agressif | T(0,50) | (a) | T(0,50) | (a) |
| **EA3** | Chimiquement très agressif | T(0,45) | (a) | T(0,45) | (a) |

**Notes :**

**(a)** Ciment à haute résistance aux sulfates (NBN B 12-108) ou combinaison ciment + laitier granulé moulu (LMA ≥ 66 %) si teneur en sulfates > 600 mg/l dans l'eau ou > 3000/2000 mg/kg dans le sol. La haute résistance aux sulfates du LMA doit être démontrée selon l'ATG.

**(b)** T(1,50) peut être utilisé exceptionnellement dans des applications BNA telles que les **bétons de propreté** pour fondations.

**(c)** Béton sans air entraîné sauf si le prescripteur l'impose explicitement.

> **EA toujours en combinaison avec une autre classe** — un environnement chimiquement agressif s'ajoute toujours à une classe EE, ES ou EI existante.

---

## Tableau 2 — Types de béton

| Désignation | T(1,50) | T(1,00) | T(0,65) | T(0,60) | T(0,55) | T(0,55)A | T(0,50) | T(0,50)A | T(0,45) | T(0,45)A |
|-------------|:-------:|:-------:|:-------:|:-------:|:-------:|:--------:|:-------:|:--------:|:-------:|:--------:|
| Rapport max. eau/ciment | 1,50 | 1,00 | 0,65 | 0,60 | 0,55 | 0,55 | 0,50 | 0,50 | 0,45 | 0,45 |
| Teneur min. ciment (kg/m³) | — | — | 260 | 280 | 300 | 300 | 320 | 320 | 340 | 340 |
| Classe résistance min. (a) | C8/10 | C12/15 | C16/20 | C20/25 | C25/30 | C20/25 | C30/37 | C25/30 | C35/45 | C30/37 |

**Teneur en air du béton frais (types A uniquement) :**

| D_max | T(0,55)A | T(0,50)A | T(0,45)A |
|-------|----------|----------|----------|
| 20 mm ≤ D_max ≤ 31,5 mm | 4,0–8,0 % | 4,0–8,0 % | 4,0–8,0 % |
| 14 mm ≤ D_max ≤ 16 mm | 5,0–9,0 % | 5,0–9,0 % | 5,0–9,0 % |
| 5,6 mm ≤ D_max ≤ 12 mm | 6,0–10,0 % | 6,0–10,0 % | 6,0–10,0 % |

**(a)** S'applique à 28 jours, sauf pour les compositions à développement de résistance très lent (voir tableau 4 de la NBN B 15-400:2015) — un âge plus élevé peut être fixé en accord avec le prescripteur.

> **ATTENTION :** Le type de ciment utilisable, les éventuelles additions de type II et l'augmentation du dosage minimal sont donnés dans les **Tableaux 3-ANB, 4-ANB et 5-ANB** de la NBN B 15-001:2018 (tableaux d'aptitude spécifique à l'emploi des liants par classes d'exposition et d'environnement).

### Ciments à haute résistance aux sulfates (NBN B 12-108:2015)

- CEM I-SR 0 et CEM I-SR 3 (ciments Portland)
- CEM III/B-SR et CEM III/C-SR (ciments de haut-fourneau)
- CEM V/A (S-V) HSR (ciment composé)
- SSC HSR (ciment sursulfaté, NBN EN 15743+A1:2015)

### Classes d'exposition équivalentes (nbN EN 206 ↔ NBN B 15-001)

| Classe d'exposition | ↔ Classe d'environnement | Teneur en SO₄²⁻ (eau) |
|---------------------|--------------------------|----------------------|
| XA1 | EA1 | 200–600 mg/l |
| XA2 | EA2 | 600–3 000 mg/l |
| XA3 | EA3 | 3 000–6 000 mg/l |

Au-delà de **600 mg/l** de sulfates dans l'eau (ou 3 000 mg/kg dans le sol), un ciment SR/HSR ou une combinaison ciment + LMA ≥ 66 % est nécessaire → à mentionner comme exigence complémentaire **E**.

---

Liens : [[T7 — Index]] · [[T7 — 00 — Avant-Propos et Normes]] · [[T7 — 02 — Consistance Dmax et Données E]]
