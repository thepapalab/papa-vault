---
title: Concrete — README
type: index
status: living
created: 2026-06-05
---

# Concrete — README

FEBELCEM guidance bulletins on concrete specification according to Belgian norms (NBN EN 206 + NBN B 15-001). Each bulletin is split into a dedicated subfolder following the structure described below.

## Splitting convention

Each bulletin is split by logical section into standalone Obsidian notes. Every split produces:

| File | Role |
|------|------|
| `BulletinID — Index.md` | Master entry point: summary tables, all chapter links, key constraints at a glance |
| `BulletinID — 00 — ….md` | Preface / normative context / scope |
| `BulletinID — 01 … N — ….md` | One file per main section (numbered in document order) |

Frontmatter fields used in every split file:

```yaml
title:      # descriptive
type:       norm-guide
source:     # full document title, publisher, date
norms:      # list of norms referenced
authority:  # author / publisher
date:       # YYYY-MM
sections:   # list of covered section numbers (where applicable)
tags:       # [béton, …, T7]
related:    # wikilinks to adjacent files
created:    # YYYY-MM-DD
```

## Documents available

### T7 — Prescription des bétons courants (FEBELCEM, Janvier 2020)

Covers: prescription of standard concretes with specified properties per **NBN EN 206:2013+A1:2016** & **NBN B 15-001:2018**.

Source file: `T7-FR-SpecificationBetons.md` (original OCR)
Split folder: `T7-FR-SpecificationBetons/`

| File | Sections | Key content |
|------|----------|-------------|
| [[T7 — Index]] | — | Quick-reference tables: resistance classes, environment classes vs. min. resistance, chloride limits |
| [[T7 — 00 — Avant-Propos et Normes]] | Avant-Propos | Context, scope (NBN EN 206 + NBN B 15-001), related norms table |
| [[T7 — 01 — Résistance et Durabilité]] | §1.1–1.3 | Resistance classes A, domain of use B1, 13 environment classes B2, **Table 1** (durability per class), **Table 2** (concrete types T) |
| [[T7 — 02 — Consistance Dmax et Données E]] | §1.4–1.6 | Consistency classes C, D_max selection D, complementary data E, **Table 3** (WAI), **Tables 5–6** (RAS prevention) |
| [[T7 — 03 — Comment Prescrire]] | §2 | **Tableau 7** — full prescription form: all A/B/C/D/E values in one place |
| [[T7 — 04 — Exemples]] | §3 | 5 annotated specification examples (Tableau 8) |
| [[T7 — 05 — Texte CdC et BENOR]] | §4 | Model contract clause, conformity control procedure, BENOR certification (TRA 550) |
| [[T7 — 06 — Bétons Spéciaux et Bibliographie]] | Annex | Special concretes covered / not covered by NBN B 15-001:2018, bibliography |

---

### EN 1990/A1 — Annexe A2 : Application aux ponts (NBN EN 1990/A1, mars 2006)

Covers: EN 1990:2002/A1:2005 + AC:2008 + AC:2010 — combination rules, partial factors (γ and ψ), deformation and vibration limits for road bridges, footbridges and railway bridges.

Source file: `NBN EN 1990_A1-2006-1_F.md` (original OCR)
Split folder: `NBN EN 1990/` (files alongside source)

| File | Sections | Key content |
|------|----------|-------------|
| [[EN 1990 A1 — Index]] | — | Quick-reference tables: ψ coefficients (A2.1–A2.3), γ factors (EQU/STR/GEO), railway deformation limits, comfort criteria |
| [[EN 1990 A1 — 00 — Avant-Propos et Annexe Nationale]] | AN | Context, full list of nationally-determined parameters (clauses générales, ponts routiers, passerelles, ponts ferroviaires) |
| [[EN 1990 A1 — 01 — A2.1-A2.2 — Domaine et Combinaisons]] | A2.1–A2.2 | Scope, symbols, combination rules by bridge type, **Tableaux A2.1–A2.3** (ψ coefficients) |
| [[EN 1990 A1 — 02 — A2.3 — États-Limites Ultimes]] | A2.3 | ULS design values: approaches 1/2/3, **Tableaux A2.4(A)(B)(C)** (γ EQU/STR/GEO), **Tableau A2.5** (accidental/seismic) |
| [[EN 1990 A1 — 03 — A2.4 — États-Limites de Service]] | A2.4 | SLS combinations (**Tableau A2.6**), deformation/vibration checks: footbridges, railway bridges (acceleration, twist, deflection, transverse), passenger comfort |
| [[EN 1990 A1 — 04 — Corrigenda AC2008 et AC2010]] | AC | Clause and table modifications (A1.2, A1.3, A1.4, A2.2.5, A2.2.6, A2.3.1); revised Tables A1.2(A)(B)(C), A1.3, A1.4 |

---

### NBN EN 1990 ANB:2021 — Annexe Nationale Belge à l'EN 1990 (NBN, mars 2021)

Covers: NDP belges pour Annexes A1 (bâtiments) et A2 (ponts) — coefficients ψ normatifs, γ ELU normatives, Approche 1 géotechnique, tableau L/δ ferroviaire A2.10 ANB, classes de conséquences coordonnées (tableaux B.6/B.7/B.8 ANB).

Source file: `NBN EN 1990 ANB-2021-1_F.md` (original OCR)
Split folder: `NBN EN 1990 ANB/` (files alongside source)

| File | Sections | Key content |
|------|----------|-------------|
| [[EN 1990 ANB — Index]] | — | Quick-reference: ψ bâtiments (A1.1 ANB), γ ELU bâtiments & ponts, L/δ ferroviaire (A2.10 ANB), classes CC ponts (B.7 ANB) |
| [[EN 1990 ANB — 00 — Avant-Propos et Introduction]] | Avant-propos, Intro, NDP non fixés | Historique 3 éditions, rôle ANB, synonymes FR/BE, liste des NDP laissés au projet individuel |
| [[EN 1990 ANB — 01 — A1 Bâtiments — ψ et ELU]] | A1.1–A1.4 | **Tableau A1.1 ANB** (ψ bâtiments, règle belge 0,3 courte durée), γ normatives EQU/STR/GEO, Approche 1, critères ELS (NBN B 03-003) |
| [[EN 1990 ANB — 02 — A2 Ponts — Combinaisons et ψ]] | A2.1–A2.2 | Durée 100 ans, F*_W et F**_W non applicables (Belgique), **Tableaux A2.1/A2.2/A2.3 ANB** (ψ normatifs ponts routiers, passerelles, ponts ferroviaires) |
| [[EN 1990 ANB — 03 — A2 Ponts — ELU et ELS]] | A2.3–A2.4 | γ normatives CC2 (Approche 1), **Tableau A2.5 ANB** (accidentel/sismique), **Tableau A2.10 ANB** (L/δ ferroviaire étendu), gauche/accélérations/α_i r_i/f_h0 normatives |
| [[EN 1990 ANB — 04 — Annexes B C D — Fiabilité et Classes]] | Annexes B, C, D | Gestion fiabilité K_FI, **Tableaux B.6/B.7/B.8 ANB** (classes CC coordonnées EN 1990 / EN 1991-1-7 / EN 1998-1) |

---

Links: [[_Norms-Regulations — README]] · [[_Knowledge — Index]]
