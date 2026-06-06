---
title: "NBN EN 1997-2:2007 — Annexe D CPT et CPTU"
type: norm-extract
source: "NBN EN 1997-2:2007 + ANB:2013 + AC:2010 — Eurocode 7 — Calcul géotechnique — Partie 2 : Reconnaissance des terrains et essais, Bureau de Normalisation, 2e éd. août 2007, version française"
norm: EC7-2
section: "Annexe D"
chapter: "Essais de pénétration statique au cône et au piézocône — corrélations et exemples"
tags: [EC7-2, eurocode-7, CPT, CPTU, correlation-qc, angle-frottement, module-oedometrique, tassement, capacite-portante, pieux]
related: ["[[EC7-2_index]]", "[[EC7-2_4_essais-en-place]]", "[[EC7-2_F_SPT]]", "[[EC7-2_G_DP]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# NBN EN 1997-2:2007 — Annexe D CPT et CPTU

## Annexe D (informative) — Essais de pénétration statique au cône et au piézocône

### D.1 Exemple de détermination de $\varphi'$ et $E'$ à partir de $q_c$ — sables quartzeux

(1) Le Tableau D.1 donne un exemple de détermination, à partir de $q_c$, des valeurs de $\varphi'$ et du module d'Young drainé $E'$ pour les sables quartzeux et feldspathiques (fondations superficielles).

**Tableau D.1 — Corrélations $q_c \to \varphi'$ et $E'$ pour sables quartzeux et feldspathiques**

| Indice de densité (CPT) | $q_c$ [MPa] | $\varphi'$ [°] | $E'$ [MPa] |
|---|---|---|---|
| Très lâche | 0,0 – 2,5 | 29 – 32 | < 10 |
| Lâche | 2,5 – 5,0 | 32 – 35 | 10 – 20 |
| Moyennement dense | 5,0 – 10,0 | 35 – 37 | 20 – 30 |
| Dense | 10,0 – 20,0 | 37 – 40 | 30 – 60 |
| Très dense | > 20,0 | 40 – 42 | 60 – 90 |

> [!note] NOTE
> Pour les sols limoneux, réduire $\varphi'$ de 3°. Pour les graviers, ajouter 2°. $E'$ est le module sécant correspondant à des tassements à 10 ans ; réduire de 50 % dans les limons, augmenter de 50 % dans les graviers. Pour des contraintes transmises > 2/3 de la capacité portante ultime, prendre $E' / 2$. Source : Bergdahl et al. (1993).

### D.2 Exemple de corrélation $q_c \to \varphi'$ par formule directe

(1) Pour les sables mal gradués ($C_U \leq 3$) au-dessus de la nappe (domaine de validité : $5 \leq q_c \leq 28$ MPa) :

$$\varphi' = 13{,}5 \log q_c + 23$$

où $\varphi'$ est en degrés et $q_c$ en MPa.

> [!note] NOTE
> Établie à partir de pénétromètres à pointe électrique et d'essais triaxiaux. Source : Stenzel et al. (1978), DIN 4094-1:2002.

### D.3 Exemple de méthode de calcul du tassement des fondations superficielles (méthode Schmertmann)

(1) Module d'Young dérivé du CPT à utiliser dans la méthode :

$$E' = 2{,}5 q_c \quad \text{(fondations axisymétriques : circulaires, carrées)}$$

$$E' = 3{,}5 q_c \quad \text{(fondations filantes — déformation plane)}$$

(2) Tassement $s$ sous pression de chargement $q_l$ :

$$s = C_1 C_2 (q_l - \sigma'_{v0}) \int_0^z \frac{I_z}{C_3 E'} \, dz$$

avec :
- $C_1 = 1 - 0{,}5 \sigma'_{v0} / (q_l - \sigma'_{v0})$
- $C_2 = 1{,}2 + 0{,}2 \log t$ où $t$ = temps en années
- $C_3$ = facteur de forme : 1,25 (carré) ou 1,75 (filante $L > 10B$)
- $\sigma'_{v0}$ = contrainte verticale effective initiale au niveau de la fondation
- $I_z$ = facteur d'influence des déformations (voir Figure D.1)

> [!note] NOTE
> $q_c$ mesuré avec pénétromètre à pointe électrique. Source : Schmertmann (1970), Schmertmann et al. (1978).

### D.4 Valeurs de $\alpha_{OED}$ pour déterminer $E_{oed} = \alpha_{OED} \cdot q_c$

**Tableau D.2 — Exemples de valeurs de $\alpha$ pour $E_{oed} = \alpha \cdot q_c$ (Sanglerat 1972)**

| Sol | $q_c$ [MPa] | $\alpha$ |
|---|---|---|
| Argile peu plastique | $q_c \leq 0{,}7$ | $3 < \alpha < 8$ |
| | $0{,}7 < q_c < 2$ | $2 < \alpha < 5$ |
| | $q_c \geq 2$ | $1 < \alpha < 2{,}5$ |
| Limon peu plastique | $q_c < 2$ | $3 < \alpha < 6$ |
| | $q_c \geq 2$ | $1 < \alpha < 2$ |
| Argile ou limon très plastique | $q_c < 2$ | $2 < \alpha < 6$ |
| | $q_c > 2$ | $1 < \alpha < 2$ |
| Limon très organique | $q_c < 1{,}2$ | $2 < \alpha < 8$ |
| Tourbe et argile très organique | $q_c < 0{,}7$ | varie avec $w$ |
| (tourbe) | $50 < w \leq 100$ | $1{,}5 < \alpha < 4$ |
| | $100 < w \leq 200$ | $1 < \alpha < 1{,}5$ |
| | $w > 300$ | $\alpha < 0{,}4$ |
| Craies | $2 < q_c \leq 3$ | $2 < \alpha < 4$ |
| | $q_c > 3$ | $1{,}5 < \alpha < 3$ |
| Sables | $q_c < 5$ | $\alpha = 2$ |
| | $q_c > 10$ | $\alpha = 1{,}5$ |

> [!note] NOTE
> Correspond à l'Équation 4.3 de la Section 4. Source : Sanglerat (1972). Voir aussi X.3.1.

### D.5 Détermination de $E_{oed}$ en fonction de la contrainte verticale

(1) Module œdométrique dépendant de la contrainte, méthode Stenzel/Biedermann/DIN 4094-1:

$$E_{oed} = w_1 \cdot p_a \left( \frac{\sigma'_v + 0{,}5 \Delta\sigma'_v}{p_a} \right)^{w_2}$$

avec $w_2 = 0{,}5$ (sables $C_U \leq 3$) ou $w_2 = 0{,}6$ (argiles peu plastiques, $I_p \leq 10$, $w_L \leq 35$).

Valeurs du coefficient de raideur $w_1$ à partir de $q_c$ :

| Sol | Formule | Domaine de validité |
|---|---|---|
| Sable mal gradué ($C_U \leq 3$) au-dessus de la nappe | $w_1 = 167 \log q_c + 113$ | $5 \leq q_c \leq 30$ |
| Sable bien gradué ($C_U > 6$) au-dessus de la nappe | $w_1 = 463 \log q_c - 13$ | $5 \leq q_c \leq 30$ |
| Argile peu plastique (ferme, $0{,}75 \leq I_c \leq 1{,}30$) | $w_1 = 15{,}2 q_c + 50$ | $0{,}6 \leq q_c \leq 3{,}5$ |

où $p_a$ = pression atmosphérique (≈ 0,1 MPa).

### D.6 Corrélation entre la capacité portante d'un pieu et $q_c$ (méthode DIN 1054)

**Tableau D.3 — Résistance en pointe $p_b$ de pieux coulés en place (sable, peu de fines)**

| Tassement normalisé $s/D_s$ ; $s/D_b$ | $q_c = 10$ MPa | $q_c = 15$ MPa | $q_c = 20$ MPa | $q_c = 25$ MPa |
|---|---|---|---|---|
| 0,02 | 0,70 | 1,05 | 1,40 | 1,75 |
| 0,03 | 0,90 | 1,35 | 1,80 | 2,25 |
| 0,10 (= $s_g$) | 2,00 | 3,00 | 3,50 | 4,00 |

Valeurs en MPa. Interpolation linéaire pour valeurs intermédiaires.

**Tableau D.4 — Frottement latéral unitaire $p_s$ sur le fût de pieux coulés en place**

| $q_c$ [MPa] | $p_s$ [MPa] |
|---|---|
| 0 | 0 |
| 5 | 0,040 |
| 10 | 0,080 |
| ≥ 15 | 0,120 |

> [!note] NOTE
> Source : DIN 1054 (2003-01). Voir X.3.1.

### D.7 Exemple de méthode de détermination de la capacité portante d'un pieu (méthode NEN 6743)

(1) Portance en compression d'un pieu :

$$F_{max} = F_{max;base} + F_{max;f\hat{u}t}$$

avec :

$$F_{max;base} = A_{base} \cdot p_{max;base}$$

$$F_{max;f\hat{u}t} = C_p \int_0^{\Delta L} p_{max;f\hat{u}t} \, dz$$

(2) Pression résistante sous la base :

$$p_{max;base} = 0{,}5 \alpha_p \beta s \left( \frac{q_{c;I;moy} + q_{c;II;moy}}{2} + q_{c;III;moy} \right) \leq 15 \text{ MPa}$$

où :
- $\alpha_p$ = facteur de catégorie de pieu (Tableau D.5)
- $\beta$ = facteur de forme de la pointe (Figure D.3, entre 0,6 et 1,0)
- $s$ = facteur de forme de la base = $\frac{1 + \sin\varphi'}{1 + \sin\varphi'} \cdot \frac{1}{r}$ (avec $r = L/B$)
- $q_{c;I;moy}$ = moyenne de $q_c$ sur $0{,}7 D_{eq}$ à $4 D_{eq}$ sous la pointe
- $q_{c;II;moy}$ = moyenne des valeurs les plus basses entre la profondeur critique et la base
- $q_{c;III;moy}$ = moyenne de $q_c$ sur une hauteur de $8 D_{eq}$ au-dessus de la base

(3) Frottement latéral unitaire maximal :

$$p_{max;f\hat{u}t} = \alpha_s \cdot q_{c;z;a}$$

**Tableau D.5 — Facteurs $\alpha_p$ et $\alpha_s$ pour sables et sables graveleux**

| Classe de pieu | $\alpha_p$ | $\alpha_s$ |
|---|---|---|
| Pieux avec refoulement — battus façonnés à l'avance | 1,0 | 0,010 |
| Pieux avec refoulement — coulés en place (tube récupéré) | 1,0 | 0,012 |
| Pieux sans refoulement — à la tarière | 0,8 | 0,006 |
| Pieux sans refoulement — forés (boue de forage) | 0,6 | 0,005 |

**Tableau D.6 — Facteurs $\alpha_s$ pour argile, limon et tourbe**

| Type de sol | $q_c$ [MPa] | $\alpha_s$ max |
|---|---|---|
| Argile | > 3 | < 0,030 |
| Argile | < 3 | < 0,020 |
| Limon | — | < 0,025 |
| Tourbe | — | 0 |

> [!note] NOTE
> Source : NEN 6743:2004. Voir X.3.1.

---

Liens : [[EC7-2_index]] · [[EC7-2_4_essais-en-place]] · [[EC7-2_E_PMT]] · [[_Knowledge — Index]] · [[CLAUDE]]
