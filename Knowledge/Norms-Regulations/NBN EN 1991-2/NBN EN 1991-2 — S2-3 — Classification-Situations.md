---
title: "NBN EN 1991-2 S2-3 — Classification et Situations de projet"
type: norm-extract
source: "NBN EN 1991-2:2004 (+ ANB 2011 + AC:2010)"
norm: EC1-2
section: "2-3"
chapter: "2"
tags: [EC1-2, NBN, classification, actions-variables, situations-projet, combinations, fatigue, groupes-charges]
related: ["[[NBN EN 1991-2 — Index]]", "[[NBN EN 1991-2 — S4 — Trafic-Routier]]", "[[NBN EN 1991-2 — S6 — Trafic-Ferroviaire]]"]
language: fr
jupyter_ref: "EC1-2/2-3"
created: 2026-06-05
---

# Section 2 — Classification des actions

## 2.1 Généralités

- Les actions de trafic se classifient selon **EN 1990 §4**.
- Elles consistent en **actions variables** et **actions accidentelles**.
- Toutes les actions de trafic sont des **actions libres** (dans les limites des sections 4 à 6).
- Les actions de trafic sont des **actions à composantes multiples**.

## 2.2 Actions variables

**(1)** En conditions normales d'utilisation : les charges roulantes et celles dues aux piétons sont **variables** (majoration dynamique incluse).

**(2)** Valeurs représentatives :
- **Valeurs caractéristiques** : probabilité limitée de dépassement sur la durée d'utilisation du projet (ou nominales)
- **Valeurs fréquentes** : correspondant à une période de retour courte (~1 semaine sur routes principales)
- **Valeurs quasi-permanentes** : généralement égales à zéro pour les charges de trafic

### Tableau 2.1 — Bases de calibrage des modèles principaux (hors fatigue)

| Modèle | Valeur caractéristique | Valeur fréquente | Valeur quasi-permanente |
|--------|------------------------|------------------|------------------------|
| **LM1** | Période retour 1 000 ans (trafic routes princ. d'Europe, α = 1) | Période retour 1 semaine | Selon EN 1990 |
| **LM2** | Période retour 1 000 ans (β = 1) | Période retour 1 semaine | Sans objet |
| **LM3** | Valeurs nominales (Annexe A, synthèse réglements nationaux) | Sans objet | Sans objet |
| **LM4** | Valeur nominale (foule) | Sans objet | Sans objet |
| **q_fk passerelles** | Valeur nominale (foule, normes nationales) | Force statique éq. à 2 piétons/m² | Selon EN 1990 |
| **Qfwk passerelles** | Valeur nominale (normes nationales) | Sans objet | Sans objet |

> [!note] ANB Belgique
> Des valeurs non-fréquentes (période retour ~1 an) peuvent être imposées pour les ponts routiers — voir EN 1992-2, EN 1994-2 et EN 1990 A2.

**(3)** Pour la fatigue : modèles distincts définis en **4.6** (routier) et **6.9** (ferroviaire).

## 2.3 Actions pour situations de projet accidentelles

**(1)** Les véhicules et trains peuvent engendrer des actions par **collision** ou **présence accidentelle** — à prendre en compte en l'absence de protection appropriée.

**(2)** Représentées par des **charges statiques équivalentes** (valeurs de calcul).

**(3)** Forces d'impact des bateaux/navires : voir EN 1991-1-7 (valeurs recommandées) ; peut être défini dans l'ANB.

Résumé des clauses accidentelles :
- **4.7.2** : impact véhicule sous pont routier
- **4.7.3** : véhicule sur pont routier (trottoirs, barrières, éléments structuraux)
- **5.6** : impacts sur passerelles
- **6.7** : déraillement train sur ou sous ouvrage ferroviaire

---

# Section 3 — Situations de projet

**(1)P** Les situations de projet retenues doivent être prises en compte et les cas de charge critiques identifiés.

**(2)** Les groupes de charges (combinaisons d'actions composantes) sont définis dans les sections 4 à 6. Chaque groupe doit être pris en compte lorsqu'il y a lieu.

**(3)P** Les règles de combinaison doivent être conformes à l'**EN 1990**.

> [!info] Combinaisons pour ponts
> Les règles spécifiques de simultanéité et les coefficients ψ applicables aux ponts routiers et ferroviaires sont donnés dans **EN 1990, Annexe A2**.

**(4)** Pour les ponts mixtes (routier + ferroviaire) : la simultanéité des actions et les vérifications particulières doivent être spécifiées (ANB ou projet individuel).

> [!note] Sismique
> Pour les combinaisons sismiques sur ponts, voir **EN 1998-2**.

---

Links: [[NBN EN 1991-2 — Index]] · [[NBN EN 1991-2 — S1 — Généralités]] · [[NBN EN 1991-2 — S4 — Trafic-Routier]] · [[NBN EN 1991-2 — S6 — Trafic-Ferroviaire]]
