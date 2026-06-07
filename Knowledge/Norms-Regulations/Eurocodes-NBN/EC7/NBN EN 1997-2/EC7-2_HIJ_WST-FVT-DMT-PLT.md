---
title: "NBN EN 1997-2:2007 — Annexes H I J K WST, FVT, DMT, PLT"
type: norm-extract
source: "NBN EN 1997-2:2007 + ANB:2013 + AC:2010 — Eurocode 7 — Calcul géotechnique — Partie 2 : Reconnaissance des terrains et essais, Bureau de Normalisation, 2e éd. août 2007, version française"
norm: EC7-2
section: "Annexes H, I, J, K"
chapter: "WST, FVT, DMT, PLT — corrélations et exemples"
tags: [EC7-2, eurocode-7, WST, FVT, DMT, PLT, sondage-poids, scissometre, dilatometre-plat, plaque, correction-mu, module-oedometrique]
related: ["[[EC7-2_index]]", "[[EC7-2_4_essais-en-place]]", "[[EC7-2_G_DP]]", "[[EC7-2_LMN_details-sol-classification]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# NBN EN 1997-2:2007 — Annexes H I J K WST, FVT, DMT, PLT

## Annexe H (informative) — Essai de sondage par poids (WST)

(1) Exemple de corrélations entre la résistance au sondage par poids (nombre de demi-rotations/0,2 m) et les paramètres géotechniques des sables quartzeux et feldspathiques naturels, d'après l'expérience suédoise.

**Tableau H.1 — Corrélations WST $\to \varphi'$ et $E'$ pour sables de quartz et feldspath**

| Indice de densité | Résistance WST [demi-rot./0,2 m] | $\varphi'$ [°] | $E'$ [MPa] |
|---|---|---|---|
| Très lâche | 0 – 10 | 29 – 32 | < 10 |
| Lâche | 10 – 30 | 32 – 35 | 10 – 20 |
| Moyennement dense | 20 – 50 | 35 – 37 | 20 – 30 |
| Dense | 40 – 90 | 37 – 40 | 30 – 60 |
| Très dense | > 80 | 40 – 42 | 60 – 90 |

> [!note] NOTE (a)
> Avant la détermination de l'indice de densité, diviser par un facteur 1,3 la résistance au sondage par poids des sols limoneux.

> [!note] NOTE (b)
> Pour les sols limoneux, réduire $\varphi'$ de 3°. Pour les graviers, ajouter 2°. $E'$ est un module sécant correspondant à des tassements à 10 ans. Réduire de 50 % dans les limons, augmenter de 50 % dans les graviers. Pour des contraintes > 2/3 de la capacité portante ultime, prendre $E'/2$.

(2) Lorsque seuls des résultats WST sont disponibles, choisir la valeur la plus faible dans chaque intervalle du Tableau H.1.

(3) Lors de l'analyse, ne pas prendre en compte les valeurs extrêmes dues à des pierres ou des galets.

> [!note] NOTE
> Source : Bergdahl et al. (1993). Voir X.3.5.

---

## Annexe I (informative) — Essai au scissomètre de chantier (FVT)

### I.1 Procédures de correction $c_{fv} \to c_u$

(1) Différentes procédures (I.2 à I.5) permettent de déterminer le facteur de correction $\mu$ à appliquer aux résultats de l'essai au scissomètre pour obtenir la résistance au cisaillement non drainée $c_{fu}$ du terrain :

$$c_u = \mu \cdot c_{fv}$$

où $c_{fv}$ = résistance mesurée au scissomètre et $\mu$ = facteur de correction.

> [!note] NOTE
> Utiliser la procédure fondée sur l'expérience locale pour le type d'argile concerné. Tenir compte du fait que la résistance drainée peut être inférieure à la résistance non drainée. Voir X.3.6.

### I.2 Facteur de correction $\mu$ à partir de la limite de liquidité $w_L$

(1) Pour les argiles molles normalement consolidées, $\mu$ est lié à la limite de liquidité (Figure I.1). Ne pas utiliser de facteur $\mu > 1{,}2$ sans reconnaissance plus poussée.

(2) Dans les argiles fissurées, $\mu$ peut être aussi faible que 0,3. Dans ces cas, utiliser d'autres méthodes pour déterminer $c_u$ (par exemple PLT).

Formule (Larsson et al. 1984 / Hansbo 1957) :

$$\mu = \frac{0{,}43}{w_L^{0{,}45}} \geq 0{,}5$$

> [!note] NOTE
> Voir X.3.6.

### I.3 Facteur de correction $\mu$ à partir de $I_P$ et de l'état de consolidation

(1) $\mu$ en fonction de l'indice de plasticité $I_P$ et de la contrainte verticale effective $\sigma'_{v0}$ (Figure I.2 — courbes selon Aas 1979).

### I.4 Procédure tenant compte de la surconsolidation (Aas et al. 1986)

(1) Évaluer d'abord si l'argile est surconsolidée ou non à partir de la relation $c_{fv}/\sigma'_{v0}$ vs $I_P$ (Figure I.3). Frontières : courbe «Jeune» et courbe «Âgée». Argile normalement consolidée (NC) entre les deux courbes ; surconsolidée (OC) au-dessus de la courbe «Âgée».

(2) Corriger selon la courbe NC ou OC de la Figure I.4.

### I.5 Formule directe (Larsson & Ahnberg 2003)

Pour les argiles normalement consolidées et légèrement surconsolidées :

$$\mu = \frac{0{,}43}{w_L^{0{,}45}} \geq 0{,}5$$

Pour $R_{OC} > 1{,}3$ :

$$\mu = \frac{0{,}43}{w_L^{0{,}45}} \left(\frac{R_{OC}}{1{,}3}\right)^{0{,}45}$$

Lorsque $R_{OC}$ non déterminé, estimer via $c_{fv} = 0{,}45 w_L \sigma'_p$ :

$$\mu = \frac{0{,}43}{w_L^{0{,}585}} \left(\frac{c_{fv}}{w_L \sigma'_{v0}}\right)^{0{,}15}$$

---

## Annexe J (informative) — Essai au dilatomètre plat (DMT)

(1) Détermination du module tangentiel unidimensionnel $E_{oed}$ à partir des résultats DMT :

$$E_{oed} = R_M \cdot E_{DMT}$$

où $R_M$ est estimé par expérience locale ou par les relations suivantes :

| Condition | Formule |
|---|---|
| $I_{DMT} \leq 0{,}6$ | $R_M = 0{,}14 + 2{,}36 \log K_{DMT}$ |
| $0{,}6 < I_{DMT} < 3{,}0$ | $R_M = R_{M0} + (2{,}5 - R_{M0}) \log K_{DMT}$ avec $R_{M0} = 0{,}14 + 0{,}15 (I_{DMT} - 0{,}6)$ |
| $3 \leq I_{DMT} \leq 10$ | $R_M = 0{,}5 + 2 \log K_{DMT}$ |
| $K_{DMT} > 10$ | $R_M = 0{,}32 + 2{,}18 \log K_{DMT}$ |

Si $R_M < 0{,}85$ d'après ces formules : prendre $R_M = 0{,}85$.

où :
- $I_{DMT}$ = indice de matériau déterminé lors de l'essai DMT
- $K_{DMT}$ = coefficient de contrainte horizontale dilatométrique déterminé lors de l'essai DMT

> [!note] NOTE
> Source : Marchetti (2001). Voir X.3.7.

---

## Annexe K (informative) — Essai de chargement à la plaque (PLT)

### K.1 Exemple de détermination de $c_u$ à partir du PLT

(1) La résistance au cisaillement non drainée est obtenue par :

$$c_u = \frac{p_u - \gamma z}{N_c}$$

où :
- $p_u$ = pression de contact ultime tirée du PLT
- $\gamma z$ = contrainte totale au niveau de la plaque (poids volumique × profondeur), applicable lorsque l'essai est réalisé dans un forage de diamètre < 3 fois le diamètre/largeur de la plaque
- $N_c$ = facteur de capacité portante :
  - $N_c = 6$ : essai PLT à la surface du terrain
  - $N_c = 9$ : essai PLT à la base d'un forage de profondeur > 4 fois le diamètre/largeur de la plaque

> [!note] NOTE
> Source : Marsland (1972). Voir X.3.8.

---

Liens : [[EC7-2_index]] · [[EC7-2_G_DP]] · [[EC7-2_LMN_details-sol-classification]] · [[_Knowledge — Index]] · [[CLAUDE]]
