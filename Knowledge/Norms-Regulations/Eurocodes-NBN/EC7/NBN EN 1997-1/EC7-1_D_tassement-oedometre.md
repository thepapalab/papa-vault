---
title: "NBN EN 1997-1:2004 — Annexe D (informative) — Tassement : méthode œdométrique"
type: norm-extract
source: "NBN EN 1997-1:2004 (EN 1997-1:2004+AC:2009) — Eurocode 7: Calcul géotechnique, Partie 1: Règles générales, édition française"
norm: EC7-1
section: "D"
chapter: "Annexe D (informative) — Exemple de méthode analytique de calcul de la charge limite des fondations superficielles"
tags: [EC7-1, eurocode-7, geotechnique, tassement, methode-oedometre, fondations-superficielles]
related: ["[[EC7-1_index]]", "[[EC7-1_C_capacite-portante]]", "[[EC7-1_EF_resistance-pieux]]", "[[_Knowledge — Index]]"]]", "[[EC7-1_C_capacite-portante]]", "[[EC7-1_EF_resistance-pieux]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# NBN EN 1997-1:2004 — Annexe D (informative) — Tassement : méthode œdométrique

> *Annexe informative*

## Annexe D (informative) — Exemple de méthode analytique de calcul de la capacité portante

### D.1 Symboles utilisés dans l'annexe D

(1) Les symboles suivants sont utilisés dans l'annexe D :

- $A' = B' L'$ valeur de calcul de la surface effective de la fondation ;
- $b$ valeur de calcul des facteurs pour l'inclinaison de la base de la fondation, avec les indices $c$, $q$ et $\gamma$ ;
- $B$ largeur de la fondation ;
- $B'$ largeur effective de la fondation ;
- $D$ profondeur d'encastrement ;
- $e$ excentricité de la résultante des actions, avec les indices $B$ ou $L$ ;
- $i$ facteurs d'inclinaison de la charge, avec les indices $c$ pour la cohésion, $q$ pour la surcharge et $\gamma$ pour le poids volumique ;
- $L$ longueur de la fondation ;
- $L'$ longueur effective de la fondation ;
- $m$ exposant dans les formules de calcul du facteur d'inclinaison $i$ ;
- $N$ facteurs de capacité portante, avec les indices $c$, $q$ et $\gamma$ ;
- $q$ pression due au poids des terres ou pression de surcharge au niveau de la base de la fondation ;
- $q'$ valeur de calcul de la pression effective due au poids des terres au niveau de la base de la fondation ;
- $s$ facteurs de forme de la base de la fondation, avec les indices $c$, $q$ et $\gamma$ ;
- $V$ charge verticale ;
- $\alpha$ inclinaison de la base de la fondation sur l'horizontale ;
- $\gamma'$ valeur de calcul du poids volumique effectif du sol sous le niveau de la fondation ;
- $\theta$ angle donnant la direction de $H$.

(2) Les notations utilisées dans cette méthode sont données sur la figure D.1.

*Figure D.1 — Notations*

### D.2 Généralités

(1) Les équations approximatives déduites de la théorie de la plasticité et de résultats expérimentaux peuvent être utilisées pour déterminer la valeur de calcul de la capacité portante verticale. Il convient de tenir compte des effets suivants :

- la résistance du sol, généralement représentée par les valeurs de calcul $c_u$, $c'$ et $\phi'$ ;
- l'excentricité et l'inclinaison des charges de calcul ;
- la forme, la profondeur et l'inclinaison de la fondation ;
- l'inclinaison de la surface du terrain ;
- les pressions de l'eau souterraine et les gradients hydrauliques ;
- la variabilité du sol, particulièrement la stratification.

### D.3 Conditions non drainées

(1) La valeur de calcul de la capacité portante peut être déduite de la formule :

$$R/A' = (\pi + 2) \, c_u \, b_c \, s_c \, i_c + q \tag{D.1}$$

avec les facteurs adimensionnels pour :

- l'inclinaison de la base de la fondation : $b_c = 1 - 2\alpha / (\pi + 2)$ ;
- la forme de la fondation :
  - $s_c = 1 + 0{,}2 \, (B'/L')$, pour une forme rectangulaire ;
  - $s_c = 1{,}2$, pour une forme carrée ou circulaire ;
- l'inclinaison de la charge, provoquée par une charge horizontale $H$ :

$$i_c = \frac{1}{2}\left(1 + \sqrt{1 - \frac{H}{A' c_u}}\right)$$

avec $H \leq A' c_u$.

### D.4 Conditions drainées

(1) La valeur de calcul de la capacité portante peut être calculée au moyen de la formule :

$$R/A' = c' N_c \, b_c \, s_c \, i_c + q' N_q \, b_q \, s_q \, i_q + 0{,}5 \, \gamma' B' N_\gamma \, b_\gamma \, s_\gamma \, i_\gamma \tag{D.2}$$

avec les valeurs de calcul suivantes des facteurs adimensionnels pour :

— la capacité portante :

$$N_q = e^{\pi \tan\phi'} \tan^2(45° + \phi'/2)$$

$$N_c = (N_q - 1) \cot\phi'$$

$$N_\gamma = 2(N_q - 1)\tan\phi', \text{ avec } \delta \geq \phi'/2 \text{ (base rugueuse)}$$

— l'inclinaison de la base de la fondation :

$$b_c = b_q - (1 - b_q) / (N_c \tan\phi')$$

$$b_q = b_\gamma = (1 - \alpha \cdot \tan\phi')^2$$

— la forme de la fondation :

$$s_q = 1 + (B'/L')\sin\phi', \text{ pour une forme rectangulaire}$$

$$s_q = 1 + \sin\phi', \text{ pour une forme carrée ou circulaire}$$

$$s_\gamma = 1 - 0{,}3 \, (B'/L'), \text{ pour une forme rectangulaire}$$

$$s_\gamma = 0{,}7, \text{ pour une forme carrée ou circulaire}$$

$$s_c = (s_q N_q - 1)/(N_q - 1), \text{ pour une forme rectangulaire, carrée ou circulaire}$$

— l'inclinaison de la charge due à la charge horizontale $H$ :

$$i_c = i_q - (1 - i_q) / (N_c \cdot \tan\phi')$$

$$i_q = \left[1 - \frac{H}{V + A'c'\cot\phi'}\right]^m$$

$$i_\gamma = \left[1 - \frac{H}{V + A'c'\cot\phi'}\right]^{m+1}$$

avec :

$$m = m_B = \frac{2 + (B'/L')}{1 + (B'/L')} \text{ lorsque } H \text{ agit dans la direction de } B'$$

$$m = m_L = \frac{2 + (L'/B')}{1 + (L'/B')} \text{ lorsque } H \text{ agit dans la direction de } L'$$

Dans les cas où la composante horizontale de la charge agit selon une direction formant un angle $\theta$ avec la direction de $L'$, on peut calculer $m$ au moyen de la formule :

$$m = m_\theta = m_L \cos^2\theta + m_B \sin^2\theta$$

---

Liens : [[EC7-1_index]] · [[EC7-1_C_capacite-portante]] · [[EC7-1_EF_resistance-pieux]] · [[_Knowledge — Index]] · [[CLAUDE]]
