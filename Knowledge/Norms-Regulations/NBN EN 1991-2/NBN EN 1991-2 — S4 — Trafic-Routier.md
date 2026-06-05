---
title: "NBN EN 1991-2 S4 — Actions du trafic routier"
type: norm-extract
source: "NBN EN 1991-2:2004 (+ ANB 2011 + AC:2010)"
norm: EC1-2
section: "4"
chapter: "4"
tags: [EC1-2, NBN, trafic-routier, LM1, LM2, LM3, LM4, groupes-charges, fatigue, accidentel, ponts-routiers, tandem]
related: ["[[NBN EN 1991-2 — Index]]", "[[NBN EN 1991-2 — S2-3 — Classification-Situations]]", "[[PTR CE01 — Ch03 — Actions]]"]
language: fr
jupyter_ref: "EC1-2/4"
created: 2026-06-05
---

# Section 4 — Actions du trafic routier et autres actions spécifiques sur les ponts routiers

## 4.1 Domaine d'application

Longueur chargée ≤ **200 m** (LM1 calibré pour cette longueur — reste conservateur au-delà).  
Pour longueurs > 200 m : modèles complémentaires définis dans l'ANB ou le projet individuel.

## 4.2 Représentation des actions

### 4.2.3 Découpage de la chaussée en voies conventionnelles

**Tableau 4.1 — Nombre et largeur des voies conventionnelles**

| Largeur chaussée w | Nombre de voies n_l | Largeur voie w_l | Aire résiduelle |
|-------------------|---------------------|------------------|-----------------|
| w < 5,4 m | 1 | 3 m | w − 3 m |
| 5,4 m ≤ w < 6 m | 2 | w/2 | 0 |
| 6 m ≤ w | Int(w/3) | 3 m | w − 3×n_l |

Exemples : w = 11 m → n_l = 3, aire résiduelle = 2 m.

> [!note]
> - Terre-plein central permanent : découpage séparé par chaussée.
> - Terre-plein central amovible : découpage sur l'ensemble de la chaussée (terre-plein compris).

### 4.2.4 Numérotation des voies

La voie n°1 est positionnée de manière à produire l'effet **le plus défavorable** sur l'élément étudié.

## 4.3 Charges verticales — Valeurs caractéristiques

### 4.3.1 Aperçu des modèles de charge

| Modèle | Description | Usage |
|--------|-------------|-------|
| **LM1** | Tandems TS + UDL | Effets généraux et locaux |
| **LM2** | Essieu unique β_Q × 400 kN | Éléments courts (portées 3–7 m) |
| **LM3** | Convois exceptionnels | Itinéraires autorisés, avec AN |
| **LM4** | Foule 5 kN/m² | Situations transitoires en milieu urbain |

LM1, LM2, LM3 : situations durables **et** transitoires.  
LM4 : uniquement situations transitoires.

### 4.3.2 Modèle de charge 1 (LM1)

Deux systèmes partiels :

**(a) Tandem TS** — charge d'essieu par voie i :

$$F_{TS} = \alpha_{Qi} \cdot Q_{ik}$$

- Un seul tandem par voie.
- Chaque essieu = 2 roues identiques : charge par roue = $0{,}5\,\alpha_{Qi}\,Q_{ik}$.
- Surface de contact roue : **carré 0,40 m × 0,40 m**.
- Entraxe des essieux du tandem : **1,20 m**.

**(b) Charge uniformément répartie UDL** — intensité par voie i :

$$q_{UDL} = \alpha_{qi} \cdot q_{ik}$$

Appliquée uniquement sur les **parties défavorables** de la surface d'influence.

**Tableau 4.2 — LM1 : Valeurs caractéristiques (α = 1)**

| Emplacement | Charge d'essieu Q_ik [kN] | UDL q_ik [kN/m²] |
|-------------|--------------------------|-------------------|
| Voie n°1 | **300** | **9** |
| Voie n°2 | **200** | **2,5** |
| Voie n°3 | **100** | **2,5** |
| Autres voies | 0 | 2,5 |
| Aire résiduelle | 0 | 2,5 |

> [!important] ANB Belgique
> Coefficients d'ajustement : **α_Qi = α_qi = α_qr = 1,00** pour routes principales.  
> Minimum imposé par l'EN : α_Qi ≥ 0,8 pour voie 1 ; α_Qi ≥ 1 pour i ≥ 2.

**Règles simplifiées pour effets généraux (portées > 10 m) :**
- Remplacer chaque tandem par un essieu unique de poids = somme des deux essieux :
  - Voie 1 : 600 α_Q1 kN ; Voie 2 : 400 α_Q2 kN ; Voie 3 : 200 α_Q3 kN.

**Vérifications locales :** deux tandems adjacents peuvent être rapprochés — distance entre essieux ≥ **0,50 m**.

### 4.3.3 Modèle de charge 2 (LM2)

Charge d'essieu unique :

$$F_{LM2} = \beta_Q \cdot Q_{ak} = \beta_Q \times 400 \text{ kN}$$

(majoration dynamique incluse). Une roue seule : $200\,\beta_Q$ kN.

> [!important] ANB Belgique
> **β_Q = 1,00**. Surface de contact par roue : 0,35 m × 0,60 m (axe dans sens de circulation).

### 4.3.4 Modèle de charge 3 (LM3) — Véhicules spéciaux

- Séries d'ensembles de charges d'essieu pour convois exceptionnels.
- Modèle de base défini dans l'**Annexe A** (convoi 900 kN avec essieux de 150 kN par défaut en Belgique).
- Circuler uniquement sur les itinéraires autorisés.

### 4.3.5 Modèle de charge 4 (LM4) — Foule

$$q_{LM4} = 5 \text{ kN/m}^2$$

Sur toute la surface de la chaussée.

### 4.3.6 Diffusion des charges concentrées

- Surface de contact du tandem : 0,40 × 0,40 m (sous revêtement).
- Diffusion à 45° à travers les couches non structurales.

## 4.4 Forces horizontales — Valeurs caractéristiques

### 4.4.1 Forces de freinage et d'accélération

Force longitudinale par voie chargée :

$$Q_{lk} = 0{,}6 \left( \alpha_{Q1} \cdot Q_{1k} + \alpha_{Q2} \cdot Q_{2k} + \ldots \right) \times 2 + 0{,}10 \left( \alpha_{q1} \cdot q_{1k} \cdot w_1 + \alpha_{qi} \cdot q_{ik} \cdot w_i + \ldots \right) \cdot L_{adj}$$

Formule complète (valeur caractéristique sur tablier entier) :

$$Q_{lk} = 0{,}6\,\alpha_{Q1}\,(2 Q_{1k}) + 0{,}10\,q_{1k}\,\alpha_{q1}\,w_1\,L \quad \leq 900\,\text{kN (pour LM1 avec } \alpha = 1)$$

> [!note] Règle pratique
> Sur voie 1 seule : Q_lk = min(0,6 × 2×300 + 0,10 × 9 × 3 × L ; limite ANB).  
> La limite supérieure peut être définie dans l'ANB.

- La force est appliquée à la **surface de roulement** (= niveau supérieur du tablier sous revêtement).
- Elle est répartie sur la **longueur chargée**.

### 4.4.2 Forces centrifuges et transversales

$$Q_{trk} = 0{,}025\,\alpha_{Qi}\,Q_{ik}\,n_{tk}$$

où n_tk = nombre de voies chargées. La valeur maximale est indiquée dans l'ANB.

## 4.5 Groupes de charges de trafic sur les ponts routiers

### 4.5.1 Groupes — Valeurs caractéristiques (Tableau 4.4a)

| Groupe | LM1 (TS+UDL) | LM2 | LM3 | LM4 | Freinage/Accél. | Centrifuge | Trottoirs/pistes |
|--------|-------------|-----|-----|-----|-----------------|------------|-----------------|
| **gr1a** | Valeur caract. | — | — | — | (a) | (a) | Valeur comb. b |
| **gr1b** | — | Valeur caract. | — | — | — | — | — |
| **gr2** | Valeurs fréquentes b | — | — | — | Valeur caract. | Valeur caract. | — |
| **gr3** | — | — | — | — | — | — | Valeur caract. c |
| **gr4** | — | — | — | Valeur caract. | — | — | Valeur caract. b |
| **gr5** | Voir Annexe A | — | Valeur caract. | — | — | — | — |

(a) Peut être défini dans l'ANB.  
(b) Valeur recommandée : 3 kN/m² (ou valeur définie dans l'ANB).  
(c) Un seul trottoir si effet plus défavorable ; gr3 sans objet si gr4 pris en compte.

> [!important] Usage pratique
> - **gr1a** : cas général (vérification globale avec LM1 dominant)
> - **gr1b** : vérification éléments courts avec LM2 dominant
> - **gr2** : vérification avec forces horizontales dominantes
> - **gr5** : vérification avec convois exceptionnels LM3

### 4.5.2 Valeurs fréquentes

Les valeurs fréquentes de l'action ne comprennent que la valeur fréquente de LM1 **ou** de LM2 **ou** des charges trottoirs — sans autres composantes.

### 4.5.3 Situations transitoires

Le poids des tandems est réduit : $0{,}8\,\alpha_{Qi}\,Q_{ik}$. Toutes autres composantes (UDL, horizontales) restent inchangées.

## 4.6 Modèles de charges de fatigue

### 4.6.1 Généralités — Choix du modèle

| Modèle | Usage | Applicabilité |
|--------|-------|---------------|
| **FLM1** (= LM1 avec ψ_fat) | Limite de fatigue — vérification que durée illimitée | Acier (contrôle limite fatigue) |
| **FLM2** (ensemble camions fréquents) | Limite de fatigue — précis si 1 camion à la fois | Acier (1 seul camion) |
| **FLM3** (véhicule unique 480 kN) | Durée de vie — méthode simplifiée avec λ | Tous matériaux (méthode λ) |
| **FLM4** (ensemble camions standard) | Durée de vie — précis | Tous matériaux (1 camion) |
| **FLM5** (données trafic réel) | Durée de vie — le plus général | Cas complexes |

### Tableau 4.5 — Nombre indicatif de poids lourds par an et par voie lente

| Catégorie | Route | N_obs [véh/an] |
|-----------|-------|----------------|
| 1 | Routes/autoroutes ≥ 2 voies, trafic camions élevé | 2,0 × 10⁶ |
| 2 | Routes/autoroutes, trafic camions moyen | 0,5 × 10⁶ |
| 3 | Routes principales, faible trafic camions | 0,125 × 10⁶ |
| 4 | Routes locales, faible trafic camions | 0,05 × 10⁶ |

> [!note]
> PTAC > 100 kN = véhicule lourd. Ajouter 10% de N_obs par voie rapide.

### 4.6.3 FLM2 — Ensemble de 5 camions fréquents

| Camion | Poids total [kN] | Espacement essieux [m] | Charge/essieu [kN] |
|--------|-----------------|----------------------|-------------------|
| 1 | 200 | 4,5 | 50 / 130 / — |
| 2 | 310 | 4,5 + 1,3 | 70 / 120 / 120 |
| 3 | 490 | 4,5 + 1,3 + ... | 70 / 150 / 150 / 60 / 60 |
| 4 | 390 | — | 70 / 140 / 90 / 90 |
| 5 | 450 | — | 70 / 130 / 90 / 90 / 70 |

### 4.6.4 FLM3 — Véhicule unique

Poids de référence : **480 kN** (4 essieux × 120 kN), espacés 1,2 m / 6 m / 1,2 m.  
Largeur de contact : 0,40 m × 0,40 m par roue.

### 4.6.5 FLM4 — Ensemble de 5 camions standard

Voir Tableau 4.7 de l'EN (5 types de camions avec distribution de poids).

## 4.7 Actions pour situations de projet accidentelles

### 4.7.2 Forces d'impact des véhicules sous le pont

**(a) Impact sur piles et éléments porteurs :**

| Type de véhicule | F_dx (longitudinal) | F_dy (transversal) | Hauteur h₀/h₁ |
|-----------------|---------------------|-------------------|---------------|
| Route normal | 1 000 kN | 500 kN | 1,25 m / 1,5 m |
| Défini dans l'ANB (Belgique) | voir ANB | voir ANB | h₀ = 1,25 m |

> [!important] ANB Belgique
> Forces d'impact sur piles (hors protection) selon EN 1991-1-7 §4.3.1 : F_dx = 1 000 kN, F_dy = 500 kN, hauteur h₀ = 1,25 m, h₁ = 1,5 m.

**(b) Impact sur tabliers** (hauteur libre h₀ ≤ 5 m) :

| Véhicule | F_dx [kN] | F_dy [kN] | Zone hauteur |
|----------|-----------|-----------|-------------|
| Poids lourd | 500 | 250 | 0,25 m × 2 m, à 1–3 m des bords |

### 4.7.3 Actions de véhicules sur le pont

**(a) Véhicules sur trottoirs :** Charge verticale = LM1 réduit (voie n°1 seule, α_Q1 = 0,8).

**(b) Impact sur bordures :**

| Type bordure | F horizontale [kN] | Hauteur application |
|-------------|-------------------|---------------------|
| Classe A (normal) | 100 | 0,1 m sous-face barrière ou 1,0 m plancher |
| Classe B (élevé) | 200 | idem |

**(c) Impact sur dispositifs de retenue :** défini dans l'ANB (classe selon EN 1317).

**(d) Impact sur éléments structuraux :** selon EN 1991-1-7 (réservoirs sous-jacents).

## 4.8 Actions sur les garde-corps

Force horizontale appliquée à la main courante : définie dans l'ANB ou le projet individuel.  
Valeur recommandée : **1,0 kN/m** horizontal + **1,0 kN** ponctuel horizontal/vertical.

## 4.9 Charges de trafic sur culées et murs adjacents

### 4.9.1 Charges verticales

Charge uniformément répartie équivalente sur remblai (diffusion 1:1 à partir de la chaussée) :

$$q_{eq} = \alpha_{q1}\,q_{1k} + \frac{\alpha_{Q1}\,Q_{1k}}{A}$$

### 4.9.2 Force horizontale

$$H = \frac{q_{eq}}{2} \cdot K_a \cdot z$$

où K_a = coefficient de poussée active, z = profondeur dans le remblai.

> [!note] Pas de majoration dynamique pour les culées
> Les charges sur remblais et murs adjacents sont utilisées sans correction pour effets dynamiques.

---

Links: [[NBN EN 1991-2 — Index]] · [[NBN EN 1991-2 — S2-3 — Classification-Situations]] · [[NBN EN 1991-2 — S5 — Passerelles]] · [[PTR CE01 — Ch03 — Actions]]
