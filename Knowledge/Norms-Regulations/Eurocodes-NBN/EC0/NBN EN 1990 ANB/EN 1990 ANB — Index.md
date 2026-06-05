---
title: EN 1990 ANB — Annexe Nationale Belge — Index
type: index
source: "NBN EN 1990 ANB:2021 — Eurocode 0 : Bases de calcul des structures — Annexe nationale belge, NBN, 23-03-2021 (remplace ANB:2013)"
norms: [NBN EN 1990 ANB:2021, NBN EN 1990:2002, NBN EN 1990/A1:2006]
authority: "Commission E250/E25001 — CSTC/SECO — Bureau de Normalisation (NBN)"
date: 2021-03
tags: [EN1990, ANB, belge, NDP, coefficients-partiels, coefficients-psi, classes-consequence, fiabilite, bâtiments, ponts]
related: ["[[EN 1990 A1 — Index]]", "[[_Norms-Regulations — README]]", "[[PTR CE01 — Index — FR]]", "[[_Knowledge — Index]]"]
created: 2026-06-05
---

# EN 1990 ANB — Annexe Nationale Belge — Index

Annexe nationale normative belge à l'EN 1990:2002 (Eurocode 0) et à son amendement EN 1990/A1:2006. Fixe les **paramètres déterminés nationalement (NDP)** pour les Annexes A1 (bâtiments) et A2 (ponts). Valable à partir du 23-03-2021.

> [!important] Caractère normatif en Belgique
> La NBN EN 1990 ne peut être utilisée en Belgique **qu'en combinaison avec cette ANB**. Les valeurs des tableaux marquées « normatives » ou « recommandées = normatives » sont des NDP à valeur de norme nationale belge.

## Fichiers de la norme

| Fichier | Sections | Contenu |
|---------|----------|---------|
| [[EN 1990 ANB — 00 — Avant-Propos et Introduction]] | Avant-propos, Intro, NDP non fixés | Historique éditions, rôle de l'ANB, liste des NDP laissés au projet individuel |
| [[EN 1990 ANB — 01 — A1 Bâtiments — ψ et ELU]] | A1.1–A1.4 | Durée de vie, **Tableau A1.1 ANB** (ψ bâtiments), γ EQU/STR/GEO pour bâtiments, combinaisons accidentelles, critères ELS (NBN B 03-003) |
| [[EN 1990 ANB — 02 — A2 Ponts — Combinaisons et ψ]] | A2.1–A2.2 | Durée 100 ans, **Tableaux A2.1/A2.2/A2.3 ANB** (ψ pour ponts routiers, passerelles, ponts ferroviaires), remarques belges sur F*_W et F**_W |
| [[EN 1990 ANB — 03 — A2 Ponts — ELU et ELS]] | A2.3–A2.4 | γ normatives (approche 1), **Tableau A2.5 ANB** (accidentel/sismique), **Tableau A2.10 ANB** (L/δ ferroviaire), gauche, accélérations, déformations transversales |
| [[EN 1990 ANB — 04 — Annexes B C D — Fiabilité et Classes]] | Annexes B, C, D | Gestion fiabilité (K_FI), **Tableaux B.6/B.7/B.8 ANB** (classes de conséquences coordonnées EN 1990 / EN 1991-1-7 / EN 1998-1) |

---

## Coefficients ψ bâtiments — Tableau A1.1 ANB (valeurs normatives)

| Action | ψ₀ | ψ₁ | ψ₂ |
|--------|----|----|-----|
| Cat. A — Habitation / résidentiel | 0,7 | 0,5 | 0,3 |
| Cat. B — Bureaux | 0,7 | 0,5 | 0,3 |
| Cat. C — Lieux de réunion | 0,7 | 0,7 | 0,6 |
| Cat. D — Commerces | 0,7 | 0,7 | 0,6 |
| Cat. E — Aires de stockage | 1,0 | 0,9 | 0,8 |
| Cat. F — Véhicules légers (≤ 30 kN) | 0,7 | 0,7 | 0,6 |
| Cat. G — Véhicules moyens (30–160 kN) | 0,7 | 0,5 | 0,3 |
| Cat. H — Toitures | 0 | 0 | 0 |
| Neige (Belgique H ≤ 1000 m) | 0,5 (→0,3) ¹⁾ | 0 | 0 |
| Vent | 0,6 (→0,3) ¹⁾ | 0,2 | 0 |
| Température (hors incendie) | 0,6 | 0,5 | 0 |
| Tassements (EN 1997) | 1,0 | 1,0 | 1,0 |
| Charges d'exécution | 1,0 | — | 0,2 |

¹⁾ Règle belge : si une action de courte durée (< 1 mois) accompagne une autre action de courte durée, ψ₀ = 0,3 pour la seconde action si c'est neige, vent ou température.

---

## Coefficients γ ELU — Bâtiments (valeurs normatives CC2)

| Tableau | γ_G,sup | γ_G,inf | γ_Q | ξ |
|---------|---------|---------|-----|---|
| A1.2(A) — EQU | **1,10** | **0,90** | **1,50** | — |
| A1.2(B) — STR/GEO | **1,35** | **1,00** | **1,50** | **0,85** (→ ξγ ≅ 1,15) |
| A1.2(C) — GEO | **1,00** | **1,00** | **1,30** | — |

> **Géotechnique (Belgique)** : Approche 1 uniquement. ξ = **1,00** pour les applications géotechniques (dérogation à ξ = 0,85).

---

## Coefficients γ ELU — Ponts (valeurs normatives CC2)

| Tableau | γ_G,sup | γ_G,inf | γ_Q routier/piétons | γ_Q ferroviaire général | γ_Q ferroviaire lourd (SW/2) | γ_Q autres | ξ |
|---------|---------|---------|---------------------|------------------------|------------------------------|-----------|---|
| A2.4(B) — STR/GEO | **1,35** | **1,00** | **1,35** | **1,45** | **1,20** | **1,50** | **0,85** |
| A2.4(C) — GEO | 1,00 | 1,00 | 1,15 | 1,25 | 1,25 | 1,30 | — |

> **Approche 1** seulement en Belgique. ξ = **1,00** pour les applications géotechniques.

---

## Tableau A2.10 ANB — Rapport minimal L/δ (ponts ferroviaires)

| Vitesse V | 1–2 tabliers, L ≤ 25 m | 1–2 tabliers, L ≥ 30 m | 3–5 tabliers, L ≤ 25 m | 3–5 tabliers, L ≥ 30 m |
|-----------|------------------------|------------------------|------------------------|------------------------|
| V ≤ 120 km/h | 600 | 600 | 600 | 900 |
| 120 < V ≤ 200 km/h | 600 | 800 | 1000 | 2200 |
| V > 200 km/h | 800 | 1000 | 1200 | 2200 |

---

## Classes de conséquences — Ponts (Tableau B.7 ANB)

| Classe | Type de pont |
|--------|-------------|
| **CC1** | Éléments secondaires (selon A1.1 ANB) |
| **CC2** | Passerelle sur voie d'eau ; ouvrage non classé ailleurs |
| **CC3** | Pont-route sur itinéraire > 50 000 veh/j (TMJ) avec remplacement problématique (travée > 30 m, accessibilité gênée) |
| **CC3** | Pont-rail sur ligne ferroviaire importante (LGV ou désignée par Infrabel) |
| **CC3** | Pont-canal |

> Tous les ponts-rails Infrabel sont **CC3** (PTR CE01 §1.x).

---

Liens : [[EN 1990 A1 — Index]] · [[PTR CE01 — Index — FR]] · [[_Norms-Regulations — README]] · [[_Knowledge — Index]]
