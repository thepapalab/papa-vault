---
title: "NBN EN 1992-1-1:2004 — Dispositions armatures"
type: norm-extract
source: "NBN EN 1992-1-1:2004"
norm: EC2
section: "8"
chapter: "Dispositions armatures"
tags: [EC2, eurocode-2, dispositions-armatures]
related: ["[[EC2_index]]", "[[EC2_7_els.md]]", "[[EC2_9_dispositions-elements.md]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# 8.1 Généralités

**(1)P** Les règles données dans la présente Section s'appliquent aux armatures à haute adhérence, aux treillis et aux armatures de précontrainte soumis principalement à un chargement statique. Elles s'appliquent aux bâtiments et ponts courants et peuvent ne pas être suffisantes pour les éléments soumis à un chargement dynamique d'origine sismique ou provoqué par les vibrations des machines, ou encore soumis à des charges d'impact.

**(2)P** Les exigences relatives à l'enrobage minimal doivent être satisfaites (voir 4.4.1.2).

**(4)** Les règles relatives aux structures soumises à un chargement de fatigue sont données en 6.8.

---

# 8.2 Espacement des armatures de béton armé

**(1)P** L'espacement des armatures de béton armé (barres) doit permettre une mise en place et un compactage satisfaisants du béton, et ainsi garantir le développement d'une bonne adhérence.

**(2)** Il convient d'adopter une distance libre (horizontalement et verticalement) entre barres parallèles ou entre lits horizontaux de barres parallèles supérieure ou égale à la plus grande des valeurs suivantes : $k_1$ fois le diamètre de la barre, $(d_g + k_2)$ mm ou 20 mm (où $d_g$ est la dimension du plus gros granulat).

> **Note :** Valeurs recommandées : $k_1 = 1$ ; $k_2 = 5$ mm.

**(3)** Lorsque les barres sont placées en lits horizontaux distincts, il convient de superposer les barres de chaque lit en files verticales en ménageant entre ces files un espace suffisant pour permettre le passage des aiguilles vibrantes.

**(4)** Dans le cas d'un recouvrement de barres, on peut admettre que celles-ci sont en contact sur la longueur de recouvrement. On se reportera à 8.7 pour plus de détails.

---

# 8.3 Diamètres admissibles des mandrins de cintrage pour les barres pliées

**(1)P** Le diamètre de courbure minimal des barres doit être tel qu'il évite toute fissure de flexion dans l'armature ainsi que toute rupture du béton situé dans la partie courbe de celle-ci.

**(2)** Afin d'éviter d'endommager les armatures, il convient de plier la barre avec un mandrin de diamètre supérieur ou égal à $\phi_{m,min}$.

**Tableau 8.1N — Diamètre minimal du mandrin $\phi_{m,min}$**

| Type | Diamètre de la barre | Diamètre minimal du mandrin |
|---|---|---|
| Barres et fils — coudes, crochets, boucles | $\phi \leq 16$ mm | $4\phi$ |
| Barres et fils — coudes, crochets, boucles | $\phi > 16$ mm | $7\phi$ |
| Assemblages soudés pliés après soudage | $d \geq 3\phi$ | $5\phi$ |
| Assemblages soudés pliés après soudage | $d < 3\phi$ ou soudure dans la partie courbe | $20\phi$ |

> **Note :** Dans le cas de soudures situées dans la partie courbe, le diamètre du mandrin peut être réduit à $5\phi$ lorsque le soudage est effectué conformément à l'EN ISO 17660 Annexe B.

**(3)** Il n'est pas nécessaire de justifier le diamètre du mandrin vis-à-vis de la rupture du béton si :
- l'ancrage nécessaire de la barre ne dépasse pas $5\phi$ au-delà de l'extrémité de la partie courbe
- la barre n'est pas disposée près de la surface et il existe une barre transversale de diamètre ≥ $\phi$ à l'intérieur de la partie courbe
- le diamètre du mandrin est supérieur ou égal aux valeurs recommandées du Tableau 8.1N

Dans le cas contraire :

$$\phi_m \geq F_{bt}\, \left[\frac{1}{a_b} + \frac{1}{2\phi}\right] / f_{cd} \tag{8.1}$$

où :
- $F_{bt}$ : effort de traction dû aux charges ultimes dans une barre ou un groupe de barres en contact à l'origine de la partie courbe
- $a_b$ : pour une barre donnée, moitié de l'entraxe entre les barres perpendiculairement au plan de la courbure. Pour une barre proche du parement, $a_b = $ enrobage $+ \phi/2$

Il convient de limiter $f_{cd}$ à la valeur correspondant à la classe de béton C55/67.

# 8.4 Ancrage des armatures longitudinales

## 8.4.1 Généralités

**(1)P** Les barres, fils ou treillis soudés doivent être ancrés de manière à assurer une bonne transmission des forces d'adhérence au béton, en évitant toute fissuration longitudinale ainsi que tout éclatement du béton.

**(3)** Les coudes et les crochets ne contribuent pas aux ancrages des barres comprimées.

> **Figure 8.1** — *Méthodes d'ancrage autres que le scellement droit* — *[Figure non extractable — voir document source]*

---

## 8.4.2 Contrainte ultime d'adhérence

**(2)** Pour les armatures à haute adhérence, la valeur de calcul de la contrainte ultime d'adhérence $f_{bd}$ :

$$f_{bd} = 2{,}25\, \eta_1\, \eta_2\, f_{ctd} \tag{8.2}$$

où :
- $f_{ctd}$ : résistance de calcul en traction du béton (voir 3.1.6 (2)P). $f_{ctk,0,05}$ est limitée à la valeur correspondant à la classe C60/75
- $\eta_1$ : coefficient lié aux conditions d'adhérence et à la position de la barre au cours du bétonnage (voir Figure 8.2) :
  - $\eta_1 = 1{,}0$ lorsque les conditions d'adhérence sont **bonnes**
  - $\eta_1 = 0{,}7$ dans tous les autres cas et pour les barres dans les éléments réalisés au moyen de coffrages glissants
- $\eta_2$ : lié au diamètre de la barre :
  - $\eta_2 = 1{,}0$ pour $\phi \leq 32$ mm
  - $\eta_2 = (132 - \phi)/100$ pour $\phi > 32$ mm

**Conditions d'adhérence (Figure 8.2) :**
- Barres à $45° \leq \alpha \leq 90°$ : bonnes pour toutes les barres
- Éléments de hauteur $h \leq 250$ mm : bonnes pour toutes les barres
- Éléments de hauteur $h > 250$ mm : bonnes dans la zone non hachurée ; médiocres dans la zone hachurée (supérieure à 300 mm du fond ou supérieure à 250 mm du sommet)
- Éléments de hauteur $h > 600$ mm : médiocres pour les barres situées dans la zone supérieure

---

## 8.4.3 Longueur d'ancrage de référence

**(2)** En admettant une contrainte d'adhérence constante égale à $f_{bd}$, la longueur d'ancrage de référence $l_{b,rqd}$ nécessaire pour ancrer l'effort $A_s\, \sigma_{sd}$ dans une barre droite :

$$l_{b,rqd} = (\phi / 4)\, (\sigma_{sd} / f_{bd}) \tag{8.3}$$

où $\sigma_{sd}$ est la contrainte de calcul de la barre dans la section à partir de laquelle on mesure l'ancrage.

**(4)** Lorsque les treillis soudés sont constitués de fils ou barres doubles, remplacer le diamètre $\phi$ de l'Expression (8.3) par le diamètre équivalent $\phi_n = \phi\sqrt{2}$.

---

## 8.4.4 Longueur d'ancrage de calcul

**(1)** La longueur d'ancrage de calcul $l_{bd}$ :

$$l_{bd} = \alpha_1\, \alpha_2\, \alpha_3\, \alpha_4\, \alpha_5\, l_{b,rqd} \geq l_{b,min} \tag{8.4}$$

Le produit vérifie :

$$(\alpha_2 \cdot \alpha_3 \cdot \alpha_5) \geq 0{,}7 \tag{8.5}$$

$l_{b,min}$ est la longueur d'ancrage minimale :
- Ancrages de barres **tendues** : $l_{b,min} > \max\{0{,}3\, l_{b,rqd} ;\; 10\phi ;\; 100 \text{ mm}\}$ $\tag{8.6}$
- Ancrages de barres **comprimées** : $l_{b,min} > \max\{0{,}6\, l_{b,rqd} ;\; 10\phi ;\; 100 \text{ mm}\}$ $\tag{8.7}$

**Tableau 8.2 — Valeurs des coefficients $\alpha_1$, $\alpha_2$, $\alpha_3$, $\alpha_4$ et $\alpha_5$**

| Facteur d'influence | Type d'ancrage | Tendue | Comprimée |
|---|---|---|---|
| Forme des barres | Droit | $\alpha_1 = 1{,}0$ | $\alpha_1 = 1{,}0$ |
| Forme des barres | Autre (Fig. 8.1 b, c, d) | $\alpha_1 = 0{,}7$ si $c_d > 3\phi$ ; sinon $1{,}0$ | $\alpha_1 = 1{,}0$ |
| Enrobage | Droit | $\alpha_2 = 1 - 0{,}15\,(c_d - \phi)/\phi$ ; $[0{,}7 ; 1{,}0]$ | $\alpha_2 = 1{,}0$ |
| Enrobage | Autre (Fig. 8.1 b, c, d) | $\alpha_2 = 1 - 0{,}15\,(c_d - 3\phi)/\phi$ ; $[0{,}7 ; 1{,}0]$ | $\alpha_2 = 1{,}0$ |
| Confinement par armatures transversales non soudées | Tous types | $\alpha_3 = 1 - K\lambda$ ; $[0{,}7 ; 1{,}0]$ | $\alpha_3 = 1{,}0$ |
| Confinement par armatures transversales soudées | Tous types (Fig. 8.1e) | $\alpha_4 = 0{,}7$ | $\alpha_4 = 0{,}7$ |
| Confinement par compression transversale | Tous types | $\alpha_5 = 1 - 0{,}04p$ ; $[0{,}7 ; 1{,}0]$ | — |

où :
- $\lambda = (\Sigma A_{st} - \Sigma A_{st,min}) / A_s$
- $\Sigma A_{st}$ : aire des armatures transversales le long de $l_{bd}$
- $\Sigma A_{st,min} = 0{,}25\, A_s$ pour les poutres ; $0$ pour les dalles
- $A_s$ : aire de la section d'une barre ancrée individuelle de diamètre maximal
- $K$ : valeur selon la Figure 8.4 ($K = 0{,}1$ pour barre en position de coin ; $K = 0{,}05$ pour barre en position centrale ; $K = 0$ pour dalle)
- $p$ : pression transversale à l'ELU le long de $l_{bd}$ en MPa

**(2)** Simplification : l'ancrage de barres tendues selon les formes de la Figure 8.1 peut être assuré moyennant une longueur d'ancrage équivalente $l_{b,eq}$ :
- $\alpha_1\, l_{b,rqd}$ pour les formes des Figures 8.1b) à 8.1d)
- $\alpha_4\, l_{b,rqd}$ pour la forme de la Figure 8.1e)

# 8.5 Ancrage des armatures d'effort tranchant et autres armatures transversales

**(1)** Il convient normalement de réaliser l'ancrage des armatures d'effort tranchant et autres armatures transversales au moyen de coudes et de crochets, ou à l'aide d'armatures transversales soudées, en prévoyant une barre à l'intérieur du crochet ou du coude.

**(2)** Il convient que l'ancrage soit conforme à la Figure 8.5. Le soudage doit être effectué conformément à l'EN ISO 17660 avec une résistance conforme à 8.6 (2).

> **Figure 8.5** — *Ancrage des armatures transversales* — *[Figure non extractable — voir document source]*
>
> Note : Pour les solutions c) et d), l'enrobage ne doit pas être inférieur à $3\phi$ ni à 50 mm.

---

# 8.6 Ancrage au moyen de barres soudées

**(1)** On peut réaliser un ancrage au moyen de barres transversales soudées (voir Figure 8.6) s'appuyant sur le béton, sous réserve de démontrer que la qualité des assemblages soudés est correcte.

**(2)** La résistance à l'entraînement d'une barre transversale (diamètre compris entre 14 mm et 32 mm) soudée du côté intérieur de la barre principale vaut $F_{btd}$. Dans l'Expression (8.3), $\sigma_{sd}$ peut être réduit par le facteur $F_{btd}/A_s$.

> **Note :** Valeur recommandée :
>
> $$F_{btd} = l_{td}\, \phi_t\, \sigma_{td} \leq F_{wd} \tag{8.8N}$$
>
> où :
> - $F_{wd}$ : valeur de calcul de la résistance au cisaillement de la soudure (exemple : $0{,}5\, A_s\, f_{yd}$)
> - $l_{td} = 1{,}16\, \phi_t\, (f_{yd}/\sigma_{td})^{0{,}5} \leq l_t$
> - $l_t$ : longueur de la barre transversale, limitée à l'espacement des barres à ancrer
> - $\phi_t$ : diamètre de la barre transversale
> - $\sigma_{td} = (f_{ctd} + \sigma_{cm}) / y \leq 3\, f_{cd}$
> - $\sigma_{cm}$ : contrainte de compression dans le béton perpendiculairement aux deux barres (positive en compression)
> - $y = 0{,}015 + 0{,}14\, e^{-0{,}18x}$ ; $x = 2\,(c/\phi_t) + 1$
> - $c$ : enrobage perpendiculairement aux deux barres

**(3)** Si deux barres de même diamètre sont soudées chacune sur un côté de la barre à ancrer, la résistance à l'entraînement donnée en 8.6 (2) peut être doublée sous réserve que l'enrobage de la barre extérieure soit conforme aux exigences de la Section 4.

**(4)** Si deux barres sont soudées du même côté, avec un espacement minimal de $3\phi$, la résistance à l'entraînement est multipliée par un facteur 1,41.

**(5)** Pour les barres de diamètre nominal inférieur ou égal à 12 mm :

$$F_{btd} = F_{wd} \leq 16\, A_s\, f_{cd}\, \phi_t / \phi_l \tag{8.9}$$

où :
- $F_{wd}$ : valeur de calcul de la résistance au cisaillement de la soudure
- $\phi_t$ : diamètre nominal de la barre transversale ($\phi_t \leq 12$ mm)
- $\phi_l$ : diamètre nominal de la barre à ancrer ($\phi_l \leq 12$ mm)

Si deux barres transversales soudées espacées au minimum de $\phi_t$ sont utilisées, multiplier la résistance à l'entraînement par 1,41.

# 8.7 Recouvrements et coupleurs

## 8.7.1 Généralités

**(1)P** La transmission des efforts d'une barre à l'autre s'effectue par :
- recouvrement des barres, avec ou sans coudes ou crochets
- soudage
- organes mécaniques assurant la transmission à la fois des efforts de traction et de compression ou des efforts de compression uniquement.

---

## 8.7.2 Recouvrements

**(1)P** Les recouvrements des barres doivent être tels que :
- la transmission des efforts d'une barre à l'autre soit assurée
- il ne se produise pas d'éclatement du béton au voisinage des jonctions
- il n'apparaisse pas de fissures ouvertes qui affecteraient le comportement de la structure.

**(2)** Il convient normalement de décaler les recouvrements et de ne pas les disposer dans des zones fortement sollicitées (rotules plastiques par exemple), et de les disposer de manière symétrique.

**(3)** Dispositions des barres (Figure 8.7) :
- distance libre entre barres en recouvrement : $\leq 4\phi$ ou 50 mm. Si cette condition n'est pas satisfaite, augmenter la longueur de recouvrement d'une valeur égale à la distance libre
- espacement longitudinal entre recouvrements voisins : $\geq 0{,}3\, l_0$
- distance libre minimale entre barres adjacentes en recouvrement voisin : $\geq 2\phi$ ou 20 mm

**(4)** Lorsque les dispositions sont conformes à (3) ci-dessus, la proportion de barres tendues en recouvrement peut être de 100% si les barres sont dans un même lit. Pour plusieurs lits, la proportion est réduite à 50%.

Toutes les barres comprimées et les armatures secondaires peuvent comporter un recouvrement dans une même section.

---

## 8.7.3 Longueur de recouvrement

**(1)** La longueur de recouvrement de calcul :

$$l_0 = \alpha_1\, \alpha_2\, \alpha_3\, \alpha_4\, \alpha_5\, \alpha_6\, l_{b,rqd} \geq l_{0,min} \tag{8.10}$$

$$l_{0,min} > \max\{0{,}3\, \alpha_6\, l_{b,rqd} ;\; 15\phi ;\; 200 \text{ mm}\} \tag{8.11}$$

Les valeurs de $\alpha_1$ à $\alpha_5$ peuvent être prises dans le Tableau 8.2 ; pour le calcul de $\alpha_3$, prendre $\Sigma A_{st,min} = 1{,}0\, A_s\, (\sigma_{sd}/f_{yd})$.

$$\alpha_6 = (\rho_1/25)^{0{,}5}, \text{ limité à } [1 ; 1{,}5] \tag{}$$

avec $\rho_1$ = proportion de barres avec recouvrement dont l'axe se situe à moins de $0{,}65\, l_0$ de l'axe du recouvrement considéré.

**Tableau 8.3 — Valeurs du coefficient $\alpha_6$**

| $\rho_1$ | < 25% | 33% | 50% | > 50% |
|---|---|---|---|---|
| $\alpha_6$ | 1 | 1,15 | 1,4 | 1,5 |

---

## 8.7.4 Armatures transversales dans une zone de recouvrement

### 8.7.4.1 Armatures transversales dans le cas de barres tendues

**(2)** Lorsque le diamètre $\phi$ des barres ancrées par recouvrement est inférieur à 20 mm, ou lorsque la proportion des barres avec recouvrement est inférieure à 25%, les armatures transversales nécessaires par ailleurs suffisent.

**(3)** Lorsque $\phi \geq 20$ mm, il convient que la section totale $A_{st}$ des armatures transversales soit supérieure ou égale à la section $A_s$ d'une des barres du recouvrement ($\Sigma A_{st} \geq 1{,}0\, A_s$). Il convient de disposer les barres transversales perpendiculairement à la direction du recouvrement, entre celui-ci et le parement de béton.

Si plus de 50% des armatures sont ancrées par recouvrement dans une section donnée et si la distance $a$ entre recouvrements adjacents est $\leq 10\phi$, il convient d'utiliser comme armatures transversales des cadres, étriers ou épingles ancrés dans la section.

**(4)** Il convient de disposer les armatures transversales aux extrémités du recouvrement (voir Figure 8.9a).

### 8.7.4.2 Armatures transversales dans le cas de barres toujours comprimées

**(1)** En complément aux règles applicables aux barres tendues, il convient de disposer une barre transversale de part et d'autre du recouvrement, à une distance inférieure à $4\phi$ des extrémités (Figure 8.9b).

---

## 8.7.5 Recouvrements des treillis soudés constitués de fils à haute adhérence

### 8.7.5.1 Recouvrements des armatures principales

**(3)** Dans le cas de recouvrement des panneaux dans un même plan, il convient de respecter les dispositions de 8.7.2 et d'ignorer tout effet favorable des barres transversales ($\alpha_3 = 1{,}0$).

**(4)** Dans le cas du recouvrement des panneaux dans des plans distincts, il convient de disposer les recouvrements des armatures principales dans des zones où la contrainte dans l'acier à l'ELU est inférieure ou égale à 80% de la résistance de calcul.

**(6)** Proportion admissible d'armatures principales à ancrer par recouvrement :
- recouvrement en même plan : valeurs du Tableau 8.3
- recouvrement en plans distincts :
  - 100% si $(A_s/s)_{prov} \leq 1200$ mm²/m
  - 60% si $(A_s/s)_{prov} > 1200$ mm²/m

**(7)** Aucune armature transversale supplémentaire n'est nécessaire dans la zone de recouvrement.

### 8.7.5.2 Recouvrements des armatures de répartition

**(1)** Toutes les armatures de répartition peuvent être ancrées par recouvrement dans une même section.

**Tableau 8.4 — Longueurs de recouvrement requises pour les fils de répartition des treillis**

| Diamètre des fils de répartition (mm) | Longueur minimale de recouvrement |
|---|---|
| $\phi \leq 6$ | ≥ 150 mm ; au moins 1 maille (2 soudures) dans $l_0$ |
| $6 < \phi \leq 8{,}5$ | ≥ 250 mm ; au moins 2 mailles (3 soudures) |
| $8{,}5 < \phi \leq 12$ | ≥ 350 mm ; au moins 2 mailles (3 soudures) |

# 8.8 Règles supplémentaires pour les barres de gros diamètre

**(1)** Les règles ci-après remplacent celles énoncées en 8.4 et 8.7 dans le cas des barres d'un diamètre supérieur à $\phi_{large}$.

> **Note :** Valeur recommandée : $\phi_{large} = 32$ mm.

**(2)** Lorsqu'on utilise des barres de gros diamètre, la maîtrise de la fissuration peut être obtenue soit par l'utilisation d'armatures de peau (voir 9.2.4) soit par le calcul (voir 7.3.4).

**(3)** Lorsqu'on utilise des barres de gros diamètre, les efforts de fendage ainsi que l'effet de goujon sont supérieurs. Il convient d'ancrer ce type de barres au moyen d'organes mécaniques spécifiques. L'ancrage peut également être droit, mais il convient alors de confiner les armatures au moyen de cadres ou d'étriers.

**(4)** De manière générale, il convient de ne pas réaliser de jonctions par recouvrement avec des barres de gros diamètre, sauf dans les sections dont les dimensions sont au minimum égales à 1,0 m ou lorsque la contrainte dans les barres ne dépasse pas 80% de la résistance ultime de calcul.

**(5)** Il convient de prévoir des armatures transversales, en plus des armatures d'effort tranchant, dans les zones d'ancrage lorsqu'il n'existe pas de compression transversale.

**(6)** Dans le cas de scellements droits, les sections minimales des armatures supplémentaires sont :

En direction parallèle à la face tendue :

$$A_{sh} = 0{,}25\, A_s\, n_1 \tag{8.12}$$

En direction orthogonale à la face tendue :

$$A_{sv} = 0{,}25\, A_s\, n_2 \tag{8.13}$$

où :
- $A_s$ : aire de la section de l'armature ancrée
- $n_1$ : nombre de lits comportant des barres ancrées dans la même section
- $n_2$ : nombre de barres ancrées dans chaque lit

**(7)** Il convient de répartir les armatures transversales supplémentaires de manière uniforme dans la zone d'ancrage, sans dépasser un espacement de $5$ fois le diamètre des armatures longitudinales.

**(8)** Dans le cas des armatures de peau, 9.2.4 s'applique, mais retenir une aire minimale égale à :
- $0{,}01\, A_{ct,ext}$ dans la direction perpendiculaire aux barres de gros diamètre
- $0{,}02\, A_{ct,ext}$ dans la direction parallèle à ces barres

---

# 8.9 Paquets de barres

## 8.9.1 Généralités

**(1)** Sauf indication contraire, les règles pour les barres individuelles s'appliquent également aux paquets de barres. Il convient que toutes les barres d'un paquet aient les mêmes caractéristiques. Des barres de diamètres différents peuvent être groupées en paquet sous réserve que le rapport des diamètres n'excède pas 1,7.

**(2)** Pour le calcul, le paquet est remplacé par une barre fictive équivalente :

$$\phi_n = \phi\,\sqrt{n_b} \leq 55 \text{ mm} \tag{8.14}$$

où $n_b$ est le nombre de barres du paquet :
- $n_b \leq 4$ dans le cas des barres verticales comprimées et des barres à l'intérieur d'une jonction par recouvrement
- $n_b \leq 3$ dans tous les autres cas

**(3)** Les règles de 8.2 relatives à l'espacement des barres s'appliquent en utilisant le diamètre équivalent $\phi_n$, la distance libre entre paquets étant mesurée à partir du contour extérieur effectif du paquet. L'enrobage est mesuré à partir du contour extérieur effectif du paquet et doit être supérieur ou égal à $\phi_n$. Il convient de ne pas effectuer de recouvrement pour des paquets de plus de trois barres.

**(4)** Lorsque deux barres en contact sont disposées l'une au-dessus de l'autre et que les conditions d'adhérence sont bonnes, il n'est pas nécessaire de les traiter comme un paquet.

---

## 8.9.2 Ancrage des paquets de barres

**(1)** Les paquets dont le diamètre équivalent est $< 32$ mm peuvent être arrêtés au voisinage de l'appui sans qu'il soit nécessaire de décaler les arrêts de barre. Dans le cas des paquets dont le diamètre équivalent est $\geq 32$ mm, il convient de décaler les arrêts de barre longitudinalement (voir Figure 8.12).

**(2)** Lorsque les barres individuelles sont ancrées avec un décalage supérieur à $1{,}3\, l_{b,rqd}$, il est possible d'utiliser le diamètre de la barre pour évaluer $l_{bd}$. Sinon, utiliser le diamètre équivalent $\phi_n$.

**(3)** Il n'est pas nécessaire de décaler les arrêts de barre dans le cas de paquets de barres comprimées. Dans le cas de paquets de diamètre équivalent $\geq 32$ mm, il convient de prévoir au moins quatre cours d'armatures transversales d'un diamètre $\geq 12$ mm aux extrémités du paquet ainsi qu'un cours supplémentaire juste après l'arrêt de la barre.

---

## 8.9.3 Recouvrement des paquets de barres

**(1)** La longueur de recouvrement est calculée conformément à 8.7.3 en utilisant $\phi_n$.

**(2)** Dans le cas de paquets constitués de deux barres avec $\phi_n < 32$ mm, le recouvrement peut être effectué sans décalage des arrêts de barre.

**(3)** Dans le cas de paquets de deux barres avec $\phi_n \geq 32$ mm ou de trois barres, il convient de décaler les arrêts de barre d'au moins $1{,}3\, l_0$ dans la direction longitudinale. Une $4^e$ barre peut être utilisée comme barre de recouvrement.

# 8.10 Armatures de précontrainte

## 8.10.1 Disposition des armatures de précontrainte et des gaines

### 8.10.1.1 Généralités

**(1)P** L'espacement des gaines ou des armatures de précontrainte par pré-tension doit permettre d'assurer une mise en place et un compactage corrects du béton ainsi que l'obtention d'une adhérence suffisante entre le béton et les armatures.

### 8.10.1.2 Armatures de précontrainte par pré-tension

**(1)** Les distances libres minimales entre armatures individuelles de précontrainte par pré-tension doivent être conformes à la Figure 8.14 :

> **Figure 8.14** — *Distances libres minimales entre armatures de précontrainte par pré-tension* — *[Figure non extractable — voir document source]*
>
> $\geq d_g$ ; $\geq 2\phi$ ; $\geq 20$ mm (horizontal) ; $\geq d_g + 5$ ; $\geq 2\phi$ (vertical)

**(2)** Il convient de ne pas disposer de paquets d'armatures de précontrainte dans les zones d'ancrage.

### 8.10.1.3 Gaines de précontrainte (post-tension)

**(1)P** Il convient de réaliser et de disposer les gaines de précontrainte de telle sorte que le béton puisse être coulé dans de bonnes conditions, que le béton puisse résister aux efforts exercés par les gaines dans les parties courbes pendant et après la mise en tension, et qu'aucun coulis ne pénètre dans d'autres gaines pendant l'injection.

**(2)** Normalement, il n'y a pas lieu de regrouper les gaines en paquets, sauf lorsqu'il s'agit de deux gaines placées à la verticale l'une de l'autre.

**(3)** Distances libres minimales entre gaines (Figure 8.15) :

> **Figure 8.15** — *[Figure non extractable — voir document source]*
>
> $\geq d_g$ ; $\geq \phi$ ; $\geq 40$ mm (horizontal) ; $\geq \phi$ ; $\geq 40$ mm (vertical) ; $\geq d_g + 5$ ; $\geq \phi$ ; $\geq 50$ mm

---

## 8.10.2 Ancrage des armatures de précontrainte par pré-tension

### 8.10.2.1 Généralités

**(1)** Les longueurs à considérer dans les zones d'ancrage (voir Figure 8.16) :
- **$l_{pt}$** : longueur de transmission le long de laquelle la force de précontrainte $P_0$ est entièrement transmise au béton
- **$l_{disp}$** : longueur de régularisation le long de laquelle les contraintes dans le béton se diffusent progressivement jusqu'à une distribution linéaire
- **$l_{bpd}$** : longueur d'ancrage le long de laquelle l'effort de précontrainte $F_{pd}$ à l'ELU est entièrement ancré dans le béton

### 8.10.2.2 Transfert de la force de précontrainte

**(1)** Au relâchement de l'armature, la précontrainte est transmise au béton par une contrainte d'adhérence constante $f_{bpt}$ :

$$f_{bpt} = \eta_{p1}\, \eta_1\, f_{ctd}(t) \tag{8.15}$$

où :
- $\eta_{p1} = 2{,}7$ pour les fils crantés ; $= 3{,}2$ pour les torons à 3 ou 7 fils
- $\eta_1 = 1{,}0$ pour bonnes conditions d'adhérence ; $= 0{,}7$ dans les autres cas
- $f_{ctd}(t) = \alpha_{ct} \cdot 0{,}7 \cdot f_{ctm}(t) / \gamma_c$

**(2)** La valeur de référence de la longueur de transmission $l_{pt}$ :

$$l_{pt} = \alpha_1\, \alpha_2\, \phi\, \sigma_{pm0} / f_{bpt} \tag{8.16}$$

où :
- $\alpha_1 = 1{,}0$ pour un relâchement progressif ; $= 1{,}25$ pour un relâchement brutal
- $\alpha_2 = 0{,}25$ pour les armatures de section circulaire ; $= 0{,}19$ pour les torons à 3 ou 7 fils
- $\sigma_{pm0}$ : contrainte dans l'armature juste après le relâchement

**(3)** Valeurs de calcul de la longueur de transmission :

$$l_{pt1} = 0{,}8\, l_{pt} \tag{8.17}$$
$$l_{pt2} = 1{,}2\, l_{pt} \tag{8.18}$$

> **Note :** $l_{pt1}$ est normalement utilisée pour les vérifications des contraintes locales au relâchement ; $l_{pt2}$ pour les ELU.

**(4)** Les contraintes dans le béton sont réparties linéairement au-delà de la longueur de régularisation :

$$l_{disp} = \sqrt{l_{pt}^2 + d^2} \tag{8.19}$$

### 8.10.2.3 Ancrage de l'effort de traction à l'ELU

**(1)** Il convient de vérifier l'ancrage des armatures de précontrainte dans des zones où la contrainte de traction dans le béton excède $f_{ctk,0,05}$.

**(2)** La capacité d'adhérence de l'ancrage à l'ELU :

$$f_{bpd} = \eta_{p2}\, \eta_1\, f_{ctd} \tag{8.20}$$

où :
- $\eta_{p2} = 1{,}4$ pour les fils à empreintes
- $\eta_{p2} = 1{,}2$ pour les torons à 3 ou 7 fils

**(3)** Il convient de limiter $f_{ctk,0,05}$ à la valeur correspondant à la classe C60/75.

**(4)** La longueur d'ancrage totale nécessaire pour ancrer une armature avec une contrainte $\sigma_{pd}$ :

$$l_{bpd} = l_{pt2} + \alpha_2\, \phi\, (\sigma_{pd} - \sigma_{pm\infty}) / f_{bpd} \tag{8.21}$$

où :
- $l_{pt2}$ : valeur supérieure de calcul de la longueur de transmission
- $\alpha_2$ : tel que défini en 8.10.2.2 (2)
- $\sigma_{pd}$ : contrainte dans l'armature à l'ELU
- $\sigma_{pm\infty}$ : précontrainte, toutes pertes déduites

---

## 8.10.3 Zones d'ancrage des éléments précontraints par post-tension

**(1)** Il convient de calculer les zones d'ancrage conformément aux règles d'application données dans le présent paragraphe ainsi qu'en 6.5.3.

**(4)** Il convient d'évaluer les efforts de traction dus à des forces concentrées au moyen d'un modèle bielles-tirants ou d'autres modes de représentation appropriés (voir 6.5). Il convient de disposer les armatures passives en admettant qu'elles travaillent à leur résistance de calcul. Si la contrainte dans les armatures passives est limitée à 300 MPa, aucune vérification de l'ouverture des fissures n'est nécessaire.

**(5)** Pour simplifier, on peut admettre que l'angle de diffusion de la force de précontrainte, qui prend effet à l'extrémité de l'organe d'ancrage, est égal à $2\beta$ avec $\beta = \arctan(2/3) = 33{,}7°$.

---

## 8.10.4 Ancrages et coupleurs pour armatures de précontrainte

**(1)P** Les organes d'ancrage utilisés pour les armatures de précontrainte par post-tension doivent être conformes à ceux spécifiés pour le système utilisé.

**(2)P** Lorsque des coupleurs sont utilisés, ils doivent être conformes à ceux spécifiés pour le système utilisé et disposés de manière à ne pas affecter la capacité portante de l'élément.

**(5)** Il convient d'éviter l'utilisation de coupleurs sur 50% ou plus des armatures d'une même section.

---

## 8.10.5 Déviateurs

**(1)P** Un déviateur doit résister à la fois aux efforts longitudinaux et transversaux appliqués par l'armature et transmettre ces efforts à la structure, et assurer que le rayon de courbure de l'armature de précontrainte n'entraîne pas de surtension dans l'armature ou de dommages.

**(4)** Des déviations jusqu'à 0,01 radian peuvent être admises au niveau du projet sans qu'il soit nécessaire de prévoir des déviateurs.

---

Liens : [[EC2_index]] · [[EC2_7_els.md]] · [[EC2_9_dispositions-elements.md]] · [[_Knowledge — Index]] · [[CLAUDE]]
