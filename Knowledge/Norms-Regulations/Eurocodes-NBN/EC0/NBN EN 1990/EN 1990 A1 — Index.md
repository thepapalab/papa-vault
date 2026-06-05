---
title: EN 1990 A1 — Annexe A2 Application aux ponts — Index
type: index
source: "NBN EN 1990/A1 — Eurocode : Bases de calcul des structures — Annexe A2 : Application aux ponts (+ AC:2010), NBN, mars 2006"
norms: [EN 1990:2002/A1:2005, EN 1990:2002/A1:2005/AC:2010, NBN EN 1990/A1]
authority: "CEN/TC 250 — Bureau de Normalisation (NBN)"
date: 2006-03
tags: [EN1990, Eurocode, ponts, combinaisons-actions, ELU, ELS, ferroviaire, routier, passerelle, belge]
related: ["[[_Norms-Regulations — README]]", "[[_Knowledge — Index]]", "[[PTR CE01 — Index — FR]]"]
created: 2026-06-05
---

# EN 1990 A1 — Annexe A2 Application aux ponts — Index

Amendement 1 à l'EN 1990:2002, introduisant l'**Annexe A2 (normative)** : règles de combinaison d'actions et valeurs de calcul des coefficients partiels pour les ponts routiers, passerelles et ponts ferroviaires. Inclut les corrigenda AC:2008 et AC:2010.

> [!important] Cadre d'application
> L'Annexe A2 couvre les **états-limites ultimes et de service** (sauf fatigue) pour les ponts. Elle s'applique aussi en phase d'exécution. Là où elle est silencieuse, les règles générales de l'EN 1990:2002 et les Annexes nationales s'appliquent.

## Fichiers de la norme

| Fichier | Sections | Contenu |
|---------|----------|---------|
| [[EN 1990 A1 — 00 — Avant-Propos et Annexe Nationale]] | Avant-Propos, AN | Contexte normatif, liste des clauses à choix national |
| [[EN 1990 A1 — 01 — A2.1-A2.2 — Domaine et Combinaisons]] | A2.1–A2.2 | Domaine d'application, symboles, règles de combinaison par type de pont, **Tableaux A2.1–A2.3** (coefficients ψ) |
| [[EN 1990 A1 — 02 — A2.3 — États-Limites Ultimes]] | A2.3 | Valeurs de calcul ELU : approches 1/2/3, **Tableaux A2.4(A)(B)(C)** (γ EQU/STR/GEO), **Tableau A2.5** (accidentel/sismique) |
| [[EN 1990 A1 — 03 — A2.4 — États-Limites de Service]] | A2.4 | Combinaisons ELS (**Tableau A2.6**), critères déformation/vibration ponts routiers, passerelles, ponts ferroviaires |
| [[EN 1990 A1 — 04 — Corrigenda AC2008 et AC2010]] | AC:2008, AC:2010 | Modifications de clauses et tableaux (A1.2, A1.3, A1.4, A2.2.5, A2.2.6, A2.3.1) |

## Coefficients ψ — Valeurs clés (Tableaux A2.1–A2.3)

### Ponts routiers (Tableau A2.1)

| Action | ψ₀ | ψ₁ | ψ₂ |
|--------|----|----|-----|
| Trafic gr1a (LM1 + TS) | 0,75 | 0,75 | 0 |
| Trafic gr1a (UDL) | 0,40 | 0,40 | 0 |
| Trafic gr1b (essieu) | 0 | 0,75 | 0 |
| Trafic gr2 (forces horiz.) | 0 | 0 | 0 |
| Vent F_Wk (situations durables) | 0,6 | 0,2 | 0 |
| Température T_k | 0,6 | 0,6 | 0,5 |

### Ponts ferroviaires (Tableau A2.3)

| Action | ψ₀ | ψ₁ | ψ₂ |
|--------|----|----|-----|
| LM71 / SW/0 (1 voie) | 0,80 | 0,80 | 0 |
| LM71 / SW/0 (2 voies) | 0,70 | — | 0 |
| HSLM | 1,00 | 1,00 | 0 |
| Train non chargé | 1,00 | — | — |
| Forces de lacet | 1,00 | 0,80 | 0 |
| Vent F_Wk | 0,75 | 0,50 | 0 |
| Température T_k | 0,60 | 0,60 | 0,50 |

## Coefficients partiels γ — ELU (Tableaux A2.4)

### Tableau A2.4(A) — EQU (équilibre statique)

| Situation | γ_G,sup | γ_G,inf | γ_Q routier | γ_Q ferroviaire | γ_Q autres |
|-----------|---------|---------|-------------|-----------------|-----------|
| Durable/transitoire | 1,05 | 0,95 | 1,35 | 1,45 | 1,50 |
| Construction (contrôlée) | 1,05 | 0,95 | 1,35 (charg. constr.) | — | 1,50 |

### Tableau A2.4(B) — STR/GEO Ensemble B

| Coeff. | Valeur |
|--------|--------|
| γ_G,sup | 1,35 |
| γ_G,inf | 1,00 |
| ξ (réduction perm. défav.) | 0,85 → ξγ_G,sup ≅ 1,15 |
| γ_Q (trafic routier/piétons) | 1,35 |
| γ_Q (trafic ferroviaire gr.11–31, LM71, SW/0, HSLM) | 1,45 |
| γ_Q (trafic ferroviaire gr.16–17, SW/2) | 1,20 |
| γ_Q (autres actions variables) | 1,50 |

### Tableau A2.4(C) — STR/GEO Ensemble C

| Coeff. | Valeur |
|--------|--------|
| γ_G,sup / γ_G,inf | 1,00 / 1,00 |
| γ_Q (trafic routier/piétons) | 1,15 |
| γ_Q (trafic ferroviaire) | 1,25 |
| γ_Q (poussée horizontale variable) | 1,30 |

## Limites déformation/vibration — Ponts ferroviaires (A2.4.4)

| Critère | Limite |
|---------|--------|
| Flèche verticale max. sous trafic | **L/600** |
| Accélération max. tablier (voie ballastée) | γ_bt = **3,5 m/s²** |
| Accélération max. tablier (voie directe) | γ_df = **5,0 m/s²** |
| Gauche t (V ≤ 120 km/h) | t₁ = **4,5 mm/3m** |
| Gauche t (120 < V ≤ 200 km/h) | t₂ = **3,0 mm/3m** |
| Gauche t (V > 200 km/h) | t₃ = **1,5 mm/3m** |
| Gauche total t_T | **7,5 mm/3m** |
| Fréquence propre latérale min. | f_h0 = **1,2 Hz** |

## Confort des passagers — Ponts ferroviaires (Tableau A2.9)

| Niveau | Accélération b_v |
|--------|-----------------|
| Très bon | 1,0 m/s² |
| Bon | 1,3 m/s² |
| Acceptable | 2,0 m/s² |

## Confort piétons — Passerelles (A2.4.3.2)

| Direction | Limite |
|-----------|--------|
| Vibrations verticales | 0,7 m/s² |
| Vibrations horizontales (normal) | 0,2 m/s² |
| Conditions exceptionnelles foule | 0,4 m/s² |

Vérification requise si : f_fondamentale < 5 Hz (vertical) ou < 2,5 Hz (horizontal/torsion).

---

Liens : [[_Norms-Regulations — README]] · [[PTR CE01 — Index — FR]] · [[_Knowledge — Index]]
