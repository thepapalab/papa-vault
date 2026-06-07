---
title: "NBN EN 1997-2:2007 — Annexe E Essai pressiométrique (PMT)"
type: norm-extract
source: "NBN EN 1997-2:2007 + ANB:2013 + AC:2010 — Eurocode 7 — Calcul géotechnique — Partie 2 : Reconnaissance des terrains et essais, Bureau de Normalisation, 2e éd. août 2007, version française"
norm: EC7-2
section: "Annexe E"
chapter: "Essai pressiométrique Ménard (PMT) — corrélations et exemples"
tags: [EC7-2, eurocode-7, PMT, pressiometre, Menard, portance, tassement, pieux, facteur-rheologique]
related: ["[[EC7-2_index]]", "[[EC7-2_4_essais-en-place]]", "[[EC7-2_D_CPT-CPTU]]", "[[EC7-2_F_SPT]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# NBN EN 1997-2:2007 — Annexe E Essai pressiométrique (PMT)

## Annexe E (informative) — Essai pressiométrique (PMT)

### E.1 Exemple de méthode de calcul de la portance des fondations superficielles (méthode Ménard)

(1) La portance est calculée par l'expression suivante :

$$R/A' = \sigma_{v0} + k (p_{LM} - p_0)$$

où :
- $R$ = portance de la fondation sous des charges normales
- $A'$ = surface effective de la fondation (définie dans EN 1997-1:2004)
- $\sigma_{v0}$ = contrainte verticale totale initiale au niveau de la base de la fondation
- $p_{LM}$ = valeur représentative des pressions limites Ménard à la base
- $p_0 = K_0 (\sigma_{v0} - u) + u$ avec $K_0 = 0{,}5$ par convention
- $k$ = facteur de portance (Tableau E.1)

**Tableau E.1 — Valeurs du facteur de portance empirique $k$ pour fondations superficielles**

| Type de sol | Catégorie $p_{LM}$ | $p_{LM}$ [MPa] | $k$ |
|---|---|---|---|
| Argile et limon | A | < 0,7 | $0{,}8 [1 + 0{,}25 (0{,}6 + 0{,}4 B/L) D_e/B]$ |
| | B | 1,2 – 2,0 | $0{,}8 [1 + 0{,}35 (0{,}6 + 0{,}4 B/L) D_e/B]$ |
| | C | > 2,5 | $0{,}8 [1 + 0{,}50 (0{,}6 + 0{,}4 B/L) D_e/B]$ |
| Sable et gravier | A | < 0,5 | $[1 + 0{,}35 (0{,}6 + 0{,}4 B/L) D_e/B]$ |
| | B | 1,0 – 2,0 | $[1 + 0{,}50 (0{,}6 + 0{,}4 B/L) D_e/B]$ |
| | C | > 2,5 | $[1 + 0{,}80 (0{,}6 + 0{,}4 B/L) D_e/B]$ |
| Craie | — | — | $1{,}3 [1 + 0{,}27 (0{,}6 + 0{,}4 B/L) D_e/B]$ |
| Marne et roche altérée | — | — | $[1 + 0{,}27 (0{,}6 + 0{,}4 B/L) D_e/B]$ |

> [!note] NOTE
> Source : Ministère de l'Équipement, du Logement et des Transports Français (1993). Voir X.3.2.

### E.2 Exemple de méthode de calcul du tassement des fondations superficielles (méthode Ménard)

(1) Tassement $s$ d'une fondation superficielle :

$$s = (q - \sigma_{v0}) \left[ \frac{\alpha}{9 E_c} \cdot 2B_0 \left(\frac{B}{B_0}\right)^{\alpha} + \frac{\lambda_d}{9 E_d} \cdot B \cdot \lambda_c \right]$$

où :
- $B_0$ = largeur de référence = 0,6 m
- $B$ = largeur de la fondation
- $q$ = pression normale transmise par la fondation
- $\sigma_{v0}$ = contrainte verticale totale initiale au niveau de la base
- $\alpha$ = facteur rhéologique (Tableau E.3)
- $\lambda_d$, $\lambda_c$ = facteurs de forme (Tableau E.2)
- $E_c$ = valeur pondérée de $E_M$ immédiatement en dessous de la fondation
- $E_d$ = moyenne harmonique de $E_M$ dans les couches entre le niveau de fondation et $8B$ sous celui-ci

**Tableau E.2 — Facteurs de forme $\lambda_d$ et $\lambda_c$ pour le calcul du tassement**

| L/B | Circulaire | Carré | 2 | 3 | 5 | 20 |
|---|---|---|---|---|---|---|
| $\lambda_d$ | 1 | 1,12 | 1,53 | 1,78 | 2,14 | 2,65 |
| $\lambda_c$ | 1 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5 |

**Tableau E.3 — Facteur rhéologique $\alpha$ pour fondations superficielles**

| Type de terrain | Description | $E_M / p_{LM}$ | $\alpha$ |
|---|---|---|---|
| Tourbe | — | — | 1 |
| Argile | Surconsolidée | > 16 | 1 |
| | Normalement consolidée | 9 – 16 | 0,67 |
| | Remaniée | 7 – 9 | 0,5 |
| Limon | Surconsolidé | > 14 | 0,67 |
| | Normalement consolidé | 5 – 14 | 0,5 |
| Sable | — | > 12 | 0,5 |
| | — | 5 – 12 | 0,33 |
| Sable et gravier | — | > 10 | 0,33 |
| | — | 6 – 10 | 0,25 |
| Roche | Très fissurée | — | 0,33 |
| | Non altérée | — | 0,5 |
| | Altérée | — | 0,67 |

> [!note] NOTE
> Source : Ministère de l'Équipement, du Logement et des Transports Français (1993). Voir X.3.2.

### E.3 Exemple de méthode de calcul de la capacité portante d'un pieu (méthode Ménard)

(1) Capacité portante d'un pieu isolé :

$$Q = A (k p_{LM} - p_0) + P \sum q_{si} z_i$$

où :
- $A$ = aire de la base du pieu
- $p_{LM}$ = pression limite représentative au niveau de la base (corrigée pour couches molles sous-jacentes)
- $p_0 = K_0 (\sigma_v - u) + u$ avec $K_0 = 0{,}5$
- $k$ = facteur de portance (Tableau E.4)
- $P$ = périmètre du pieu
- $q_{si}$ = contrainte de résistance par frottement sur le fût pour la couche $i$ (Figure E.1 + Tableau E.5)
- $z_i$ = épaisseur de la couche $i$

**Tableau E.4 — Facteurs de portance $k$ pour pieux chargés axialement**

| Sol | Catégorie $p_{LM}$ | $p_{LM}$ [MPa] | Pieux forés / faible refoulement | Pieux avec refoulement total |
|---|---|---|---|---|
| Argile et limon | A | < 0,7 | 1,1 | 1,4 |
| | B | 1,2 – 2,0 | 1,2 | 1,5 |
| | C | > 2,5 | 1,3 | 1,6 |
| Sable et gravier | A | < 0,5 | 1,0 | 4,2 |
| | B | 1,0 – 2,0 | 1,1 | 3,7 |
| | C | > 2,5 | 1,2 | 3,2 |
| Craie | A | < 0,7 | 1,1 | 1,6 |
| | B | 1,0 – 2,5 | 1,4 | 2,2 |
| | C | > 3,0 | 1,8 | 2,6 |
| Marne | A | 1,5 – 4,0 | 1,8 | 2,6 |
| | B | > 4,5 | 1,8 | 2,6 |
| Roche altérée | A | 2,5 – 4,0 | a) | a) |
| | B | > 4,5 | a) | a) |

a) Choisir $k$ pour la catégorie de sol la plus proche.

**Tableau E.5 — Choix des courbes de frottement latéral (Figure E.1)** — index de courbes 1 à 7 selon type de pieu et catégorie de sol. La Figure E.1 donne $q_{si}$ en MPa en fonction de $p_{LM}$ en MPa pour chaque courbe.

> [!note] NOTE
> Source : Ministère de l'Équipement, du Logement et des Transports Français (1993). Voir X.3.2.

---

Liens : [[EC7-2_index]] · [[EC7-2_D_CPT-CPTU]] · [[EC7-2_F_SPT]] · [[_Knowledge — Index]] · [[CLAUDE]]
