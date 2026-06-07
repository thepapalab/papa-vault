---
title: "NBN EN 1992-1-1:2004 — Elu"
type: norm-extract
source: "NBN EN 1992-1-1:2004"
norm: EC2
section: "6"
chapter: "Elu"
tags: [EC2, eurocode-2, elu]
related: ["[[EC2_index]]", "[[EC2_5_analyse-structurale.md]]", "[[EC2_7_els.md]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# 6.1 Flexion simple et flexion composée

**(1)P** La présente section s'applique aux régions sans discontinuité des poutres, dalles et autres éléments analogues dont les sections demeurent approximativement planes avant et après le chargement. Le dimensionnement et le choix des dispositions constructives des régions de discontinuité des poutres et autres éléments, dans lesquelles les sections planes ne restent pas planes, peuvent être effectués conformément à 6.5.

**(2)P** La détermination du moment résistant ultime de sections droites de béton armé ou de béton précontraint s'appuie sur les hypothèses suivantes :
- les sections planes restent planes
- les armatures adhérentes (armatures de béton armé ou armatures de précontrainte), qu'elles soient tendues ou comprimées, subissent les mêmes déformations relatives que le béton adjacent
- la résistance en traction du béton est négligée
- les contraintes dans le béton comprimé se déduisent du diagramme contrainte-déformation de calcul donné en 3.1.7
- les contraintes dans les armatures de béton armé ou dans les armatures de précontrainte se déduisent des diagrammes de calcul donnés en 3.2 (Figure 3.8) et en 3.3 (Figure 3.10)
- l'évaluation des contraintes dans les armatures de précontrainte tient compte de leur déformation relative initiale.

**(3)P** La déformation en compression du béton doit être limitée à $\varepsilon_{cu2}$, ou $\varepsilon_{cu3}$, selon le diagramme contrainte-déformation utilisé — voir 3.1.7 et Tableau 3.1. Les déformations des armatures de béton armé et des armatures de précontrainte doivent être limitées à $\varepsilon_{ud}$ si cette limite existe ; voir 3.2.7 (2) et 3.3.6 (7) respectivement.

**(4)** Dans le cas de sections droites avec un ferraillage symétrique, soumises à un effort de compression, il convient d'adopter une excentricité minimale $e_0 = h/30$, ou 20 mm si cette valeur est supérieure, $h$ étant la hauteur de la section.

**(5)** Dans les parties des sections qui sont soumises à une charge approximativement centrée ($e/h < 0{,}1$), telles que les membrures comprimées des poutres-caissons, il convient de limiter la déformation moyenne en compression dans cette partie de la section à $\varepsilon_{c2}$ (ou $\varepsilon_{c3}$ si l'on utilise la relation bilinéaire de la Figure 3.4).

**(6)** La Figure 6.1 montre les valeurs limites des déformations relatives admissibles.

> **Figure 6.1** — *Diagramme des déformations relatives admissibles à l'état-limite ultime* — *[Figure non extractable — voir document source]*
>
> - A : limite de déformation relative en traction des armatures de béton armé
> - B : limite de déformation relative du béton en compression
> - C : limite de déformation relative du béton en compression pure

**(7)** Pour des éléments précontraints, avec des armatures de précontrainte non-adhérentes de manière permanente, voir 5.10.8.

**(8)** Dans le cas des armatures de précontrainte extérieures, on admet que la déformation de l'armature entre deux points de contact consécutifs (ancrages ou selles de déviation) est constante. La déformation de l'armature est alors égale à la déformation relative initiale, obtenue immédiatement après l'achèvement de la mise en tension, majorée de la déformation résultant des déformations de la structure entre les zones de contact considérées. Voir également 5.10.

# 6.2.1 Effort tranchant — Procédure générale de vérification

**(1)P** Pour la vérification de la résistance à l'effort tranchant, on définit :

- $V_{Rd,c}$ : effort tranchant résistant de calcul de l'élément en l'absence d'armatures d'effort tranchant
- $V_{Rd,s}$ : effort tranchant de calcul pouvant être repris par les armatures d'effort tranchant travaillant à la limite d'élasticité
- $V_{Rd,max}$ : valeur de calcul de l'effort tranchant maximal pouvant être repris par l'élément, avant écrasement des bielles de compression

Dans les éléments de hauteur variable, on définit également (voir Figure 6.2) :
- $V_{ccd}$ : valeur de calcul de la composante d'effort tranchant de la force de compression, dans le cas d'une membrure comprimée inclinée
- $V_{td}$ : valeur de calcul de la composante d'effort tranchant de la force dans l'armature tendue, dans le cas d'une membrure tendue inclinée

> **Figure 6.2** — *Composantes d'effort tranchant dans le cas d'éléments de hauteur variable* — *[Figure non extractable — voir document source]*

**(2)** La résistance à l'effort tranchant d'un élément comportant des armatures d'effort tranchant est égale à :

$$V_{Rd} = V_{Rd,s} + V_{ccd} + V_{td} \tag{6.1}$$

**(3)** Dans les zones de l'élément où $V_{Ed} \leq V_{Rd,c}$, aucune armature d'effort tranchant n'est requise par le calcul. $V_{Ed}$ est l'effort tranchant agissant de calcul dans la section considérée, résultant des charges extérieures appliquées et de la précontrainte (armatures adhérentes ou non).

**(4)** Même lorsque aucune armature d'effort tranchant n'est requise, il convient de prévoir un ferraillage transversal minimal comme indiqué en 9.2.2. Ce ferraillage minimal peut être omis dans les éléments tels que les dalles (pleines, nervurées ou alvéolées) lorsqu'une redistribution transversale des charges est possible. Le ferraillage minimal peut également être omis dans les éléments secondaires (linteaux de portée ≤ 2 m par exemple) qui ne contribuent pas de manière significative à la résistance et à la stabilité d'ensemble de la structure.

**(5)** Dans les régions où $V_{Ed} > V_{Rd,c}$ ($V_{Rd,c}$ étant donné par l'Expression (6.2)), il convient de prévoir des armatures d'effort tranchant en quantité suffisante de telle sorte que $V_{Ed} \leq V_{Rd}$ (voir l'Expression (6.8)).

**(6)** Il convient qu'en tout point de l'élément, la somme de l'effort tranchant agissant de calcul et des contributions des membrures, $V_{Ed} - V_{ccd} - V_{td}$, soit inférieure ou égale à la valeur maximale admise $V_{Rd,max}$ (voir 6.2.3).

**(7)** Il convient que les armatures longitudinales tendues soient capables de résister à l'effort de traction supplémentaire généré par l'effort tranchant (voir 6.2.3 (7)).

**(8)** Dans le cas des éléments soumis principalement à des charges uniformément réparties, il n'y a pas lieu d'effectuer de vérification à l'effort tranchant à une distance au nu de l'appui inférieure à $d$. Il convient de maintenir les armatures d'effort tranchant requises jusqu'au droit de l'appui. Il convient également de vérifier que l'effort tranchant sur appui n'excède pas $V_{Rd,max}$ (voir également 6.2.2 (6) et 6.2.3 (8)).

**(9)** Lorsqu'une charge est appliquée en partie inférieure de l'élément, il convient, en plus des armatures nécessaires pour reprendre l'effort tranchant, de prévoir des armatures verticales suffisantes pour transmettre la charge à la partie supérieure.

# 6.2.2 Éléments pour lesquels aucune armature d'effort tranchant n'est requise

**(1)** L'effort tranchant résistant de calcul $V_{Rd,c}$ est donné par :

$$V_{Rd,c} = \left[C_{Rd,c}\, k\, (100\, \rho_l\, f_{ck})^{1/3} + k_1\, \sigma_{cp}\right] b_w d \tag{6.2a}$$

avec une valeur minimale :

$$V_{Rd,c} = (v_{min} + k_1\, \sigma_{cp})\, b_w\, d \tag{6.2b}$$

où :
- $f_{ck}$ est en MPa
- $k = 1 + \sqrt{200/d} \leq 2{,}0$ avec $d$ en mm
- $\rho_l = A_{sl} / (b_w d) \leq 0{,}02$
- $A_{sl}$ : aire de la section des armatures tendues, prolongées sur une longueur $\geq (l_{bd} + d)$ au-delà de la section considérée (voir Figure 6.3)
- $b_w$ : plus petite largeur de la section droite dans la zone tendue, en mm
- $\sigma_{cp} = N_{Ed}/A_c < 0{,}2\, f_{cd}$ en MPa
- $N_{Ed}$ : effort normal agissant dans la section droite dû aux charges extérieures et/ou à la précontrainte, en N ($N_{Ed} > 0$ en compression)
- $A_c$ : aire de la section droite du béton, en mm²
- $V_{Rd,c}$ en Newtons

> **Note :** Les valeurs de $C_{Rd,c}$, $v_{min}$ et $k_1$ peuvent être fournies par l'Annexe Nationale. Valeurs recommandées : $C_{Rd,c} = 0{,}18/\gamma_c$ ; $k_1 = 0{,}15$.
>
> $$v_{min} = 0{,}035\, k^{3/2} \cdot f_{ck}^{1/2} \tag{6.3N}$$

> **Figure 6.3** — *Définition de $A_{sl}$ dans l'Expression (6.2)* — *[Figure non extractable — voir document source]*

**(2)** Dans les éléments précontraints à une seule travée ne comportant pas d'armatures d'effort tranchant, l'effort tranchant résistant des régions fissurées en flexion peut être calculé à l'aide de l'Expression (6.2a). Dans les régions non fissurées en flexion (où la contrainte de traction en flexion est inférieure à $f_{ctk,0,05}/\gamma_c$), l'effort tranchant résistant est donné par :

$$V_{Rd,c} = \frac{I\, b_w}{S}\, \sqrt{(f_{ctd})^2 + \alpha_l\, \sigma_{cp}\, f_{ctd}} \tag{6.4}$$

où :
- $I$ : moment d'inertie
- $b_w$ : largeur de la section droite au niveau du centre de gravité
- $S$ : moment statique de la surface située au-dessus de l'axe passant par le centre de gravité
- $\alpha_l = l_x / l_{pt2} \leq 1{,}0$ pour les armatures par pré-tension ; $= 1{,}0$ pour les autres types
- $l_x$ : distance de la section considérée à l'origine de la longueur de transmission
- $l_{pt2}$ : limite supérieure de la longueur de transmission selon l'Expression (8.18)
- $\sigma_{cp}$ : contrainte de compression dans le béton au niveau du centre de gravité sous l'effort normal dû aux charges et/ou à la précontrainte

**(3)** Le calcul selon l'Expression (6.4) n'est pas requis pour les sections droites situées entre l'appui et le point correspondant à l'intersection de la ligne moyenne élastique avec la droite partant du nu de l'appui sous un angle de 45°.

**(4)** Pour le cas général d'éléments soumis à une flexion composée, dont on peut montrer qu'ils ne sont pas fissurés à l'ELU, on se reportera à 12.6.3.

**(5)** Pour le calcul des armatures longitudinales, dans la région fissurée en flexion, il convient de décaler la courbe enveloppe des moments de $a_l = d$ dans la direction défavorable (voir 9.2.1.3 (2)).

**(6)** Lorsque des charges sont appliquées sur la face supérieure de l'élément, à une distance $a_v$ du nu de l'appui telle que $0{,}5d \leq a_v < 2d$, la contribution de cette charge à l'effort tranchant agissant $V_{Ed}$ peut être multipliée par $\beta = a_v / (2d)$. Cette réduction peut être appliquée pour la vérification de $V_{Rd,c}$ dans l'Expression (6.2a). Ceci n'est valable que si les armatures longitudinales sont totalement ancrées au droit de l'appui. Pour $a_v \leq 0{,}5d$, il convient de prendre $a_v = 0{,}5d$.

Pour la valeur de $V_{Ed}$ calculée sans appliquer le facteur de réduction $\beta$, il convient de satisfaire :

$$V_{Ed} \leq 0{,}5\, b_w\, d\, \nu\, f_{cd} \tag{6.5}$$

où $\nu$ est le facteur de réduction de la résistance du béton fissuré à l'effort tranchant.

> **Note :** Valeur recommandée :
> $$\nu = 0{,}6\left(1 - \frac{f_{ck}}{250}\right) \quad (f_{ck} \text{ en MPa}) \tag{6.6N}$$

> **Figure 6.4** — *Charges appliquées au voisinage des appuis* — *[Figure non extractable — voir document source]*

# 6.2.3 Éléments pour lesquels des armatures d'effort tranchant sont requises

**(1)** Le calcul des éléments comportant des armatures d'effort tranchant est basé sur un modèle de treillis (Figure 6.5). Notations :

- $\alpha$ : angle entre les armatures d'effort tranchant et la fibre moyenne de l'élément
- $\theta$ : angle entre la bielle de compression et la fibre moyenne de l'élément
- $b_w$ : plus petite largeur de la section comprise entre la membrure tendue et la membrure comprimée
- $z$ : bras de levier des forces internes. Pour les calculs à l'effort tranchant d'une section de béton armé sans effort normal, on peut normalement adopter $z = 0{,}9d$

> **Figure 6.5** — *Modèle de treillis et notations dans le cas d'éléments comportant des armatures d'effort tranchant* — *[Figure non extractable — voir document source]*

**(2)** Il convient de limiter l'angle $\theta$.

> **Note :** Limites recommandées :
> $$1 \leq \cot\theta \leq 2{,}5 \tag{6.7N}$$

**(3)** Dans le cas des éléments comportant des armatures d'effort tranchant **verticales**, la résistance à l'effort tranchant $V_{Rd}$ est la plus petite des valeurs :

$$V_{Rd,s} = \frac{A_{sw}}{s}\, z\, f_{ywd}\, \cot\theta \tag{6.8}$$

> **Note :** Si on utilise l'Expression (6.10), il convient de réduire $f_{ywd}$ à $0{,}8\, f_{ywk}$ dans l'Expression (6.8).

$$V_{Rd,max} = \alpha_{cw}\, b_w\, z\, \nu_1\, f_{cd} / (\cot\theta + \tan\theta) \tag{6.9}$$

où :
- $A_{sw}$ : aire de la section des armatures d'effort tranchant
- $s$ : espacement des cadres ou étriers
- $f_{ywd}$ : limite d'élasticité de calcul des armatures d'effort tranchant
- $\nu_1$ : coefficient de réduction de la résistance du béton fissuré à l'effort tranchant
- $\alpha_{cw}$ : coefficient tenant compte de l'état de contrainte dans la membrure comprimée

> **Note 1 :** Valeur recommandée de $\nu_1$ : voir Expression (6.6N).
>
> **Note 2 :** Pour les éléments en béton armé ou précontraint, si la contrainte de calcul des armatures d'effort tranchant est inférieure à 80 % de $f_{yk}$, on peut adopter :
> - $\nu_1 = 0{,}6$ pour $f_{ck} \leq 60$ MPa $\tag{6.10aN}$
> - $\nu_1 = 0{,}9 - f_{ck}/200 > 0{,}5$ pour $f_{ck} > 60$ MPa $\tag{6.10bN}$
>
> **Note 3 :** Valeurs recommandées de $\alpha_{cw}$ :
> - $= 1$ pour les structures non précontraintes
> - $= (1 + \sigma_{cp}/f_{cd})$ pour $0 < \sigma_{cp} \leq 0{,}25\, f_{cd}$ $\tag{6.11aN}$
> - $= 1{,}25$ pour $0{,}25\, f_{cd} < \sigma_{cp} \leq 0{,}5\, f_{cd}$ $\tag{6.11bN}$
> - $= 2{,}5\, (1 - \sigma_{cp}/f_{cd})$ pour $0{,}5\, f_{cd} < \sigma_{cp} < 1{,}0\, f_{cd}$ $\tag{6.11cN}$
>
> **Note 4 :** Aire effective maximale des armatures d'effort tranchant $A_{sw,max}$, pour $\cot\theta = 1$ :
> $$\frac{A_{sw,max}\, f_{ywd}}{b_w\, s} \leq \frac{\alpha_{cw}\, \nu_1\, f_{cd}}{2} \tag{6.12}$$

**(4)** Dans le cas des éléments comportant des armatures d'effort tranchant **inclinées** :

$$V_{Rd,s} = \frac{A_{sw}}{s}\, z\, f_{ywd}\, (\cot\theta + \cot\alpha)\, \sin\alpha \tag{6.13}$$

$$V_{Rd,max} = \alpha_{cw}\, b_w\, z\, \nu_1\, f_{cd}\, \frac{\cot\theta + \cot\alpha}{1 + \cot^2\theta} \tag{6.14}$$

> **Note :** $A_{sw,max}$ pour $\cot\theta = 1$ :
> $$\frac{A_{sw,max}\, f_{ywd}}{b_w\, s} \leq \frac{\alpha_{cw}\, \nu_1\, f_{cd}}{2\, \sin\alpha} \tag{6.15}$$

**(5)** Dans les régions sans discontinuité de $V_{Ed}$, la détermination des armatures d'effort tranchant sur une longueur élémentaire $l = z\,(\cot\theta + \cot\alpha)$ peut être effectuée en utilisant la plus petite valeur de $V_{Ed}$ sur cette longueur.

**(6)** Lorsque l'âme comporte des gaines injectées d'un diamètre $\phi > b_w/8$, il convient de calculer $V_{Rd,max}$ en adoptant une largeur nominale de l'âme :

$$b_{w,nom} = b_w - 0{,}5\,\Sigma\phi \tag{6.16}$$

Dans le cas des gaines métalliques injectées avec $\phi < b_w/8$ : $b_{w,nom} = b_w$.

Dans le cas des gaines non injectées, des gaines en plastique injectées et des armatures de précontrainte non adhérentes :

$$b_{w,nom} = b_w - 1{,}2\,\Sigma\phi \tag{6.17}$$

**(7)** L'effort de traction supplémentaire $\Delta F_{td}$ dans les armatures longitudinales dû à l'effort tranchant $V_{Ed}$ :

$$\Delta F_{td} = 0{,}5\, V_{Ed}\, (\cot\theta - \cot\alpha) \tag{6.18}$$

Il convient que $(M_{Ed}/z + \Delta F_{td})$ ne soit pas supérieur à $M_{Ed,max}/z$.

**(8)** Lorsque des charges sont appliquées sur la face supérieure à une distance $a_v$ du nu de l'appui telle que $0{,}5d \leq a_v \leq 2{,}0\, d$, la contribution de cette charge à $V_{Ed}$ peut être minorée par $\beta = a_v / (2d)$. Pour $V_{Ed}$ ainsi calculé :

$$V_{Ed} \leq A_{sw} \cdot f_{ywd} \cdot \sin\alpha \tag{6.19}$$

Il convient de ne tenir compte des armatures d'effort tranchant que dans la partie centrale, sur une longueur de $0{,}75\, a_v$. Pour $a_v < 0{,}5d$, prendre $a_v = 0{,}5d$.

En outre, l'Expression (6.5) doit toujours être satisfaite pour la valeur de $V_{Ed}$ sans réduction.

# 6.2.4 Cisaillement entre l'âme et les membrures des sections en T

**(1)** La résistance au cisaillement de la membrure peut être calculée en considérant la membrure comme un système de bielles de compression, associées à des tirants correspondant aux armatures tendues.

**(2)** Il convient de prévoir un ferraillage minimal, comme spécifié en 9.3.1.

**(3)** La contrainte de cisaillement longitudinale $v_{Ed}$, développée à la jonction entre un côté de la membrure et l'âme, est déterminée par la variation d'effort normal (longitudinal) dans la partie de membrure considérée :

$$v_{Ed} = \Delta F_d / (h_f \cdot \Delta x) \tag{6.20}$$

où :
- $h_f$ : épaisseur de la membrure à la jonction
- $\Delta x$ : longueur considérée (voir Figure 6.7)
- $\Delta F_d$ : variation de l'effort normal dans la membrure sur la longueur $\Delta x$

La valeur maximale pour $\Delta x$ est égale à la moitié de la distance entre la section de moment nul et la section de moment maximal. Lorsque des charges ponctuelles sont appliquées, $\Delta x$ est plafonné à la distance entre charges.

> **Figure 6.7** — *Notations pour la jonction entre âme et membrures* — *[Figure non extractable — voir document source]*

**(4)** L'aire de la section des armatures transversales par unité de longueur, $A_{sf}/s_f$, peut être déterminée comme suit :

$$A_{sf}\, f_{yd} / s_f \geq v_{Ed} \cdot h_f / \cot\theta_f \tag{6.21}$$

Afin d'éviter l'écrasement des bielles de compression dans la membrure :

$$v_{Ed} \leq \nu\, f_{cd}\, \sin\theta_f\, \cos\theta_f \tag{6.22}$$

> **Note :** Valeurs recommandées pour $\cot\theta_f$ :
> - $1{,}0 \leq \cot\theta_f \leq 2{,}0$ pour les membrures **comprimées** ($45° \geq \theta_f \geq 26{,}5°$)
> - $1{,}0 \leq \cot\theta_f \leq 1{,}25$ pour les membrures **tendues** ($45° \geq \theta_f \geq 38{,}6°$)

**(5)** Dans le cas où le cisaillement entre membrure et âme est combiné à la flexion transversale, il convient de prendre pour l'aire de la section des armatures la valeur donnée par l'Expression (6.21) ou la moitié de celle-ci plus l'aire requise pour la flexion transversale, si l'aire ainsi obtenue est supérieure.

**(6)** Si $v_{Ed}$ est inférieure à $k \cdot f_{ctd}$, aucune armature supplémentaire n'est nécessaire en plus de celles requises pour la flexion.

> **Note :** Valeur recommandée : $k = 0{,}4$.

**(7)** Il convient d'ancrer les armatures longitudinales tendues dans la membrure au-delà de la bielle nécessaire au report de l'effort dans l'âme dans la section où ces armatures sont requises (voir Coupe A-A de la Figure 6.7).

# 6.2.5 Cisaillement le long des surfaces de reprise

**(1)** À l'interface entre des bétons coulés à des dates différentes, il convient de vérifier :

$$v_{Edi} \leq v_{Rdi} \tag{6.23}$$

La contrainte de cisaillement agissant à l'interface :

$$v_{Edi} = \beta\, V_{Ed} / (z\, b_i) \tag{6.24}$$

où :
- $\beta$ : rapport de l'effort normal (longitudinal) dans le béton de reprise à l'effort longitudinal total dans la zone comprimée ou tendue
- $V_{Ed}$ : effort tranchant transversal
- $z$ : bras de levier des forces internes de la section composite
- $b_i$ : largeur de l'interface (voir Figure 6.8)

La résistance au cisaillement à l'interface :

$$v_{Rdi} = c\, f_{ctd} + \mu\, \sigma_n + \rho\, f_{yd}\, (\mu\, \sin\alpha + \cos\alpha) \leq 0{,}5\, \nu\, f_{cd} \tag{6.25}$$

où :
- $c$ et $\mu$ : coefficients dépendant de la rugosité de l'interface (voir (2))
- $f_{ctd}$ : défini en 3.1.6 (2)P
- $\sigma_n$ : contrainte engendrée par la force normale externe minimale à l'interface, positive en compression ($\sigma_n < 0{,}6\, f_{cd}$). Lorsque $\sigma_n$ est une traction, prendre $c\, f_{ctd} = 0$
- $\rho = A_s / A_i$
- $A_s$ : aire des armatures traversant l'interface, correctement ancrées de part et d'autre
- $A_i$ : aire du joint
- $\alpha$ : $45° \leq \alpha \leq 90°$
- $\nu$ : coefficient de réduction donné par l'Expression (6.6N)

> **Figure 6.8** — *Exemples de surfaces de reprise* — *[Figure non extractable — voir document source]*
> **Figure 6.9** — *Joint de reprise avec indentation* — *[Figure non extractable — voir document source]*

**(2)** Classification des surfaces (valeurs de $c$ et $\mu$) :

| Type de surface | $c$ | $\mu$ |
|---|---|---|
| Très lisse (moules acier, plastique, bois traité) | 0,25 | 0,5 |
| Lisse (coffrages glissants, surface extrudée, non coffrée sans traitement) | 0,35 | 0,6 |
| Rugueuse (aspérités ≥ 3 mm, espacées ≈ 40 mm, par striage ou lavage) | 0,45 | 0,7 |
| Avec indentation (clés selon Figure 6.9) | 0,50 | 0,9 |

**(3)** Les armatures transversales (armatures de coutures) peuvent être réparties par zones de pas constant le long de l'élément. Lorsque la liaison entre deux bétons est assurée par des armatures (poutrelles en treillis), la contribution de l'acier à $v_{Rdi}$ peut être prise égale à la résultante des efforts dans chaque diagonale, sous réserve que $45° \leq \alpha \leq 135°$.

**(4)** La résistance au cisaillement longitudinal de joints coulés en place entre éléments de dalles ou de voiles peut être calculée comme indiqué en 6.2.5 (1). Toutefois, lorsque le joint peut être significativement fissuré, il convient de prendre $c = 0$ pour les joints lisses et rugueux et $c = 0{,}5$ pour les joints avec indentation (voir également 10.9.3 (12)).

**(5)** Sous charges de fatigue ou charges dynamiques, il convient de diviser par deux les valeurs de $c$ données en 6.2.5 (1).

# 6.3 Torsion

## 6.3.1 Généralités

**(1)P** Lorsque l'équilibre statique d'une structure dépend de la résistance en torsion de certains de ses éléments, on doit procéder à une vérification complète à la torsion, couvrant à la fois les états-limites ultimes et les états-limites de service.

**(2)** Lorsque, dans des structures hyperstatiques, les sollicitations de torsion sont issues uniquement de considérations de compatibilité et que la stabilité de la structure n'est pas déterminée par la résistance en torsion, il n'est généralement pas nécessaire de considérer les sollicitations de torsion à l'état-limite ultime. Il convient alors de prévoir un ferraillage minimal (voir 7.3 et 9.2).

**(3)** La résistance en torsion d'une section peut être calculée sur la base d'une section fermée à parois minces, dans laquelle l'équilibre est assuré par un flux fermé de cisaillement. Les sections pleines peuvent être modélisées directement par des sections fermées à parois minces équivalentes. Les sections de forme complexe peuvent être décomposées en sections élémentaires, la résistance en torsion de l'ensemble étant prise égale à la somme des résistances des sections élémentaires.

**(4)** La distribution des moments de torsion dans les sections élémentaires doit être proportionnée à la rigidité en torsion à l'état non-fissuré. Dans le cas de sections creuses, il convient de limiter l'épaisseur des parois fictives à l'épaisseur réelle des parois.

**(5)** Chaque section élémentaire peut être calculée séparément.

---

## 6.3.2 Méthode de calcul

> **Figure 6.11** — *Symboles et définitions utilisés en 6.3* — *[Figure non extractable — voir document source]*

**(1)** Le flux de cisaillement en torsion pure dans la paroi :

$$\tau_{t,i}\, t_{ef,i} = \frac{T_{Ed}}{2\, A_k} \tag{6.26}$$

La sollicitation tangente $V_{Ed,i}$ dans une paroi $i$ :

$$V_{Ed,i} = \tau_{t,i}\, t_{ef,i}\, z_i \tag{6.27}$$

où :
- $T_{Ed}$ : moment de torsion agissant de calcul
- $A_k$ : aire intérieure au feuillet moyen des parois, partie creuse comprise
- $\tau_{t,i}$ : contrainte tangente de torsion dans la paroi $i$
- $t_{ef,i}$ : épaisseur de la paroi fictive, pouvant être prise égale à $A/u$, mais pas inférieure à deux fois la distance entre le parement extérieur et l'axe des armatures longitudinales. Limitée par l'épaisseur réelle pour les sections creuses
- $A$ : aire totale de la section délimitée par le périmètre extérieur, partie creuse comprise
- $u$ : périmètre extérieur de la section
- $z_i$ : longueur de la paroi $i$, définie par la distance entre points d'intersection des parois adjacentes

**(2)** Pour les profils de section creuse comme pour les profils de section pleine, les effets de la torsion peuvent être superposés à ceux de l'effort tranchant, en prenant une même valeur pour l'inclinaison $\theta$ des bielles. Les valeurs limites de $\theta$ données en 6.2.3 (2) s'appliquent.

**(3)** L'aire de la section des armatures longitudinales de torsion $\Sigma A_{sl}$ :

$$\frac{\Sigma A_{sl}\, f_{yd}}{u_k} = \frac{T_{Ed}}{2\, A_k}\, \cot\theta \tag{6.28}$$

où :
- $u_k$ : périmètre de la surface $A_k$
- $f_{yd}$ : limite d'élasticité de calcul des armatures longitudinales $A_{sl}$
- $\theta$ : angle des bielles de compression (voir Figure 6.5)

Dans les membrures comprimées, les armatures longitudinales peuvent être réduites proportionnellement à l'effort de compression disponible. Dans les membrures tendues, il convient d'ajouter les armatures longitudinales de torsion aux autres armatures.

**(4)** La résistance d'un élément soumis aux sollicitations d'effort tranchant et de torsion est limitée par la résistance des bielles de béton. Il convient de satisfaire :

$$T_{Ed} / T_{Rd,max} + V_{Ed} / V_{Rd,max} \leq 1{,}0 \tag{6.29}$$

où :

$$T_{Rd,max} = 2\, \nu\, \alpha_{cw}\, f_{cd}\, A_k\, t_{ef,i}\, \sin\theta\, \cos\theta \tag{6.30}$$

$\nu$ est donné en 6.2.2 (6) et $\alpha_{cw}$ par l'Expression (6.9).

**(5)** Les sections pleines approximativement rectangulaires ne requièrent qu'un ferraillage minimal (voir 9.2.1.1) sous réserve que :

$$T_{Ed} / T_{Rd,c} + V_{Ed} / V_{Rd,c} \leq 1{,}0 \tag{6.31}$$

où $T_{Rd,c}$ est le moment de fissuration en torsion, déterminé en posant $\tau_{t,i} = f_{ctd}$.

---

## 6.3.3 Torsion gênée

**(1)** Dans le cas des sections fermées à parois minces comme dans celui des sections pleines, la torsion gênée peut normalement être négligée.

**(2)** Il peut être nécessaire de la considérer dans le cas des profils minces ouverts. Dans le cas de sections très élancées, il convient d'effectuer le calcul sur la base d'un modèle en réseau de poutres ; dans les autres cas, sur la base d'un modèle de treillis. Dans tous les cas, le calcul doit suivre les règles applicables à la flexion composée et à l'effort tranchant.

# 6.4 Poinçonnement

## 6.4.1 Généralités

**(1)P** Les règles de la présente section complètent celles données en 6.2 et couvrent le poinçonnement des dalles pleines, des dalles à caissons présentant une section pleine au droit des poteaux, et des fondations.

**(2)P** Le poinçonnement peut résulter d'une charge concentrée ou d'une réaction appliquée à une aire relativement petite, dite aire chargée $A_{load}$, d'une dalle ou d'une fondation.

---

## 6.4.2 Répartition des charges et contour de contrôle de référence

**(1)** Le contour de contrôle de référence $u_1$ est situé à une distance $2{,}0\, d$ de l'aire chargée ; il convient de le tracer de manière à minimiser sa longueur (voir Figure 6.13).

La hauteur utile de la dalle peut normalement être prise égale à :

$$d_{eff} = (d_y + d_z) / 2 \tag{6.32}$$

où $d_y$ et $d_z$ sont les hauteurs utiles des armatures dans deux directions orthogonales.

> **Figure 6.13** — *Contours de contrôle de référence types autour d'aires chargées* — *[Figure non extractable — voir document source]*

**(2)** Il convient de considérer des contours de contrôle à une distance inférieure à $2d$ lorsque la force concentrée est équilibrée par une pression élevée ou par les effets d'une charge ou d'une réaction à une distance inférieure ou égale à $2d$ du contour de l'aire chargée.

**(3)** Dans le cas d'aires chargées situées au voisinage de trémies, si la plus faible distance entre le contour de l'aire chargée et le bord de la trémie est inférieure ou égale à $6d$, la partie du contour de contrôle comprise entre deux tangentes à la trémie issues du centre de l'aire chargée est considérée comme non participante.

**(4)** Dans le cas d'une aire chargée au voisinage d'un bord ou d'un angle, il convient de choisir un contour de contrôle similaire à ceux indiqués sur la Figure 6.15, dans la mesure où le périmètre qui en résulte est inférieur à celui obtenu selon (1).

**(5)** À une distance inférieure à $d$ d'un bord ou d'un angle, il convient de prévoir des armatures de rive particulières, voir 9.3.1.4.

**(6)** La section de contrôle est la section dont la trace coïncide avec le contour de contrôle et qui s'étend sur la hauteur utile $d$.

**(7)** Il convient de donner aux autres contours $u_i$, à l'intérieur ou à l'extérieur de la surface de contrôle, la même forme que celle du contour de la surface de contrôle de référence.

**(8)** Dans le cas des dalles avec chapiteaux circulaires, pour lesquels $l_H < 2\, h_H$, une vérification à la section de contrôle n'est exigée que pour une section située à l'extérieur du chapiteau. La distance $r_{cont}$ peut être prise égale à :

$$r_{cont} = 2d + l_H + 0{,}5c \tag{6.33}$$

Dans le cas d'un poteau rectangulaire avec un chapiteau rectangulaire et $l_H < 2{,}0\, d$, de dimensions $l_1$ et $l_2$ ($l_1 \leq l_2$) :

$$r_{cont} = 2d + 0{,}56\, \sqrt{l_1 l_2} \tag{6.34}$$

$$r_{cont} = 2d + 0{,}69\, l_1 \tag{6.35}$$

**(9)** Dans le cas de dalles avec chapiteaux tels que $l_H > 2\, h_H$, il convient de vérifier les sections de contrôle à la fois dans le chapiteau et dans la dalle.

**(10)** Les dispositions de 6.4.2 et 6.4.3 s'appliquent également aux vérifications effectuées dans le chapiteau, avec $d$ pris égal à $d_H$.

**(11)** Dans le cas des poteaux circulaires, les distances $r_{cont}$ peuvent être prises égales à :

$$r_{cont,ext} = l_H + 2d + 0{,}5c \tag{6.36}$$

$$r_{cont,int} = 2(d + h_H) + 0{,}5c \tag{6.37}$$

---

## 6.4.3 Calcul de la résistance au poinçonnement

**(1)P** La méthode de calcul est fondée sur des vérifications effectuées au nu du poteau et sur le contour de contrôle de référence $u_1$. Valeurs de calcul des résistances au poinçonnement [MPa] :
- $v_{Rd,c}$ : résistance au poinçonnement d'une dalle **sans** armatures de poinçonnement
- $v_{Rd,cs}$ : résistance au poinçonnement d'une dalle **avec** armatures de poinçonnement
- $v_{Rd,max}$ : résistance maximale au poinçonnement

**(2)** Vérifications à effectuer :
- **(a)** Au nu du poteau : $v_{Ed} < v_{Rd,max}$
- **(b)** Si $v_{Ed} < v_{Rd,c}$ : aucune armature de poinçonnement n'est nécessaire
- **(c)** Si $v_{Ed} > v_{Rd,c}$ : prévoir des armatures de poinçonnement conformément à 6.4.5

**(3)** Lorsque la réaction d'appui est excentrée par rapport au contour de contrôle, la contrainte maximale de poinçonnement :

$$v_{Ed} = \beta\, V_{Ed} / (u_i\, d) \tag{6.38}$$

$$\beta = 1 + k\, \frac{M_{Ed}}{V_{Ed}}\, \frac{u_1}{W_1} \tag{6.39}$$

où :
- $u_1$ : périmètre du contour de contrôle de référence
- $k$ : coefficient dépendant du rapport $c_1/c_2$ du poteau (voir Tableau 6.1)
- $W_1$ : correspond à une répartition des contraintes de cisaillement, fonction du périmètre $u_1$ :

$$W_1 = \int_0^{u_1} e\, dl \tag{6.40}$$

**Tableau 6.1 — Valeur de $k$ pour les aires chargées rectangulaires**

| $c_1/c_2$ | ≤ 0,5 | 1,0 | 2,0 | ≥ 3,0 |
|---|---|---|---|---|
| $k$ | 0,45 | 0,60 | 0,70 | 0,80 |

Pour un poteau rectangulaire :

$$W_1 = \frac{c_1^2}{2} + c_1 c_2 + 4 c_2 d + 16 d^2 + 2\pi\, d\, c_1 \tag{6.41}$$

Pour les poteaux circulaires intérieurs :

$$\beta = 1 + 0{,}6\pi\, \frac{e}{D + 4d} \tag{6.42}$$

Pour un poteau rectangulaire intérieur avec excentricité dans les deux directions :

$$\beta = 1 + 1{,}8\, \sqrt{\left(\frac{e_y}{b_y}\right)^2 + \left(\frac{e_z}{b_z}\right)^2} \tag{6.43}$$

**(4)** Pour les jonctions de poteaux de rive (excentricité dirigée vers l'intérieur, sans excentricité dans l'autre direction), l'effort de poinçonnement peut être considéré comme uniformément réparti le long du contour $u_1^*$.

Avec excentricités dans les deux directions orthogonales :

$$\beta = \frac{u_1}{u_1^*} + k\, \frac{e_{par}}{W_1}\, u_1 \tag{6.44}$$

$$W_1 = \frac{c_2^2}{2} + c_1 c_2 + 4 c_1 d + 8 d^2 + \pi\, d\, c_2 \tag{6.45}$$

**(5)** Pour les jonctions de poteaux d'angle (excentricité vers l'intérieur) :

$$\beta = u_1 / u_1^* \tag{6.46}$$

**(6)** Pour les structures pour lesquelles la stabilité latérale ne dépend pas du fonctionnement en portique et dont les portées adjacentes ne diffèrent pas de plus de 25%, on peut utiliser des valeurs approchées de $\beta$.

> **Note :** Valeurs recommandées (Figure 6.21N) :
> - Poteau intérieur : $\beta = 1{,}15$
> - Poteau de rive : $\beta = 1{,}4$
> - Poteau d'angle : $\beta = 1{,}5$

**(7)** Lorsqu'une charge concentrée est appliquée au voisinage d'un poteau supportant un plancher-dalle, la réduction prévue en 6.2.2 (6) ou 6.2.3 (8) ne s'applique pas.

**(8)** L'effort de poinçonnement $V_{Ed}$ dans une semelle isolée peut être réduit du fait de l'action favorable de la pression des terres.

**(9)** La composante verticale $V_{pd}$ résultant d'armatures de précontrainte inclinées traversant la section de contrôle peut être prise en compte comme action favorable.

---

## 6.4.4 Résistance au poinçonnement des dalles et des semelles de poteaux sans armatures d'effort tranchant

**(1)** La valeur de calcul de la résistance au poinçonnement [MPa] :

$$v_{Rd,c} = C_{Rd,c}\, k\, (100\, \rho_l\, f_{ck})^{1/3} + k_1\, \sigma_{cp} \geq v_{min} + k_1\, \sigma_{cp} \tag{6.47}$$

où :
- $k = 1 + \sqrt{200/d} \leq 2{,}0$ avec $d$ en mm
- $\rho_l = \sqrt{\rho_{ly} \cdot \rho_{lz}} \leq 0{,}02$
- $\rho_{ly}$, $\rho_{lz}$ : taux d'armatures tendues adhérentes dans les directions $y$ et $z, calculés comme des valeurs moyennes sur une largeur de dalle égale à la largeur du poteau plus $3d$ de part et d'autre
- $\sigma_{cp} = (\sigma_{cy} + \sigma_{cz}) / 2$

> **Note :** Valeur recommandée : $C_{Rd,c} = 0{,}18/\gamma_c$ ; $v_{min}$ selon Expression (6.3N) avec $k_1 = 0{,}1$.

**(2)** Pour les semelles de poteaux, la vérification est effectuée le long de contours de contrôle situés au plus à $2d$ du nu du poteau.

Charge nette agissant :

$$V_{Ed,red} = V_{Ed} - \Delta V_{Ed} \tag{6.48}$$

$$v_{Ed} = V_{Ed,red} / (u\, d) \tag{6.49}$$

$$v_{Rd} = C_{Rd,c}\, k\, (100\, \rho\, f_{ck})^{1/3} \cdot \frac{2d}{a} \geq v_{min} \cdot \frac{2d}{a} \tag{6.50}$$

où $a$ est la distance du nu du poteau au contour de contrôle considéré.

---

## 6.4.5 Résistance au poinçonnement des dalles et des semelles de poteaux avec armatures d'effort tranchant

**(1)** Lorsque des armatures de poinçonnement sont nécessaires :

$$v_{Rd,cs} = 0{,}75\, v_{Rd,c} + 1{,}5\, \frac{d}{s_r}\, A_{sw}\, f_{ywd,ef}\, \frac{1}{u_1\, d}\, \sin\alpha \tag{6.52}$$

où :
- $A_{sw}$ : aire d'un cours d'armatures de poinçonnement sur un périmètre autour du poteau [mm²]
- $s_r$ : espacement radial des cours d'armatures de poinçonnement [mm]
- $f_{ywd,ef}$ : limite d'élasticité de calcul efficace des armatures de poinçonnement : $f_{ywd,ef} = 250 + 0{,}25\, d \leq f_{ywd}$ [MPa]
- $d$ : moyenne des hauteurs utiles dans les directions orthogonales [mm]
- $\alpha$ : angle des armatures de poinçonnement avec le plan de la dalle

Si une seule file de barres pliées vers le bas est prévue, prendre $d/s_r = 0{,}67$.

**(2)** Les exigences en matière de disposition des armatures de poinçonnement sont données en 9.4.3.

**(3)** Au voisinage du poteau, la résistance au poinçonnement est limitée à :

$$v_{Ed} = \beta V_{Ed} / (u_0\, d) \leq v_{Rd,max} \tag{6.53}$$

avec :
- poteau intérieur : $u_0 = \text{périmètre du poteau}$
- poteau de rive : $u_0 = c_2 + 3d \leq c_2 + 2c_1$
- poteau d'angle : $u_0 = 3d \leq c_1 + c_2$

> **Note :** Valeur recommandée : $v_{Rd,max} = 0{,}5\, \nu\, f_{cd}$, avec $\nu$ selon l'Expression (6.6N).

**(4)** Le contour de contrôle $u_{out}$ pour lequel aucune armature de poinçonnement n'est requise :

$$u_{out,ef} = \beta V_{Ed} / (v_{Rd,c}\, d) \tag{6.54}$$

La file périphérique extérieure des armatures de poinçonnement doit être placée à une distance inférieure ou égale à $k\, d$ à l'intérieur de $u_{out}$.

> **Note :** Valeur recommandée : $k = 1{,}5$.

**(5)** Lorsque des produits de marque déposée sont utilisés comme armatures de poinçonnement, il convient de déterminer $v_{Rd,cs}$ par des essais conformes à l'Agrément Technique Européen correspondant.

# 6.5 Dimensionnement à l'aide de modèles bielles-tirants

## 6.5.1 Généralités

**(1)P** Lorsqu'il existe une distribution non-linéaire des déformations relatives (appuis, voisinage de charges concentrées ou contraintes planes), il est possible d'utiliser des modèles bielles-tirants (voir également 5.6.4).

---

## 6.5.2 Bielles

**(1)** La résistance de calcul d'une bielle de béton dans une région où règnent des contraintes de compression transversales ou bien où ne règne aucune contrainte transversale :

$$\sigma_{Rd,max} = f_{cd} \tag{6.55}$$

Il peut être opportun d'adopter une résistance de calcul plus élevée dans des régions soumises à une étreinte.

**(2)** Il convient de réduire la résistance de calcul des bielles de béton dans les zones comprimées avec des fissures longitudinales :

$$\sigma_{Rd,max} = 0{,}6\, \nu'\, f_{cd} \tag{6.56}$$

> **Note :** Valeur recommandée :
> $$\nu' = 1 - f_{ck}/250 \tag{6.57N}$$

**(3)** Dans le cas de bielles permettant une transmission directe des charges, comme dans les corbeaux ou poutres-cloisons de faible longueur, des méthodes de calcul alternatives sont données en 6.2.2 et 6.2.3.

---

## 6.5.3 Tirants

**(1)** Il convient de limiter la résistance de calcul des tirants transversaux et celle des armatures comme indiqué en 3.2 et 3.3.

**(2)** Il convient d'ancrer convenablement les armatures dans les nœuds.

**(3)** L'effort de traction $T$ peut être obtenu au moyen des expressions suivantes :

**a) Régions de discontinuité partielle** ($b \leq H/2$, voir Figure 6.25a) :

$$T = \frac{F}{4}\left(1 - \frac{a}{b}\right) \tag{6.58}$$

**b) Régions de discontinuité totale** ($b > H/2$, voir Figure 6.25b) :

$$T = \frac{F}{4}\left(1 - 0{,}7\, \frac{a}{h}\right) \tag{6.59}$$

---

## 6.5.4 Nœuds

**(1)P** Les règles pour les nœuds s'appliquent également aux régions dans lesquelles des forces concentrées sont transmises à un élément mais qui ne sont pas dimensionnées à l'aide de la méthode des bielles.

**(2)P** Les efforts agissant dans les nœuds doivent s'équilibrer. On doit notamment tenir compte des efforts transversaux de traction perpendiculaires au plan du nœud.

**(3)** Le dimensionnement des nœuds de concentration d'effort et les dispositions constructives correspondantes sont déterminants pour l'établissement de la capacité résistante.

**(4)** Valeurs de calcul des contraintes de compression à l'intérieur des nœuds :

**a)** Nœuds soumis à compression, sans tirant ancré (Figure 6.26) :

$$\sigma_{Rd,max} = k_1\, \nu'\, f_{cd} \tag{6.60}$$

> **Note :** Valeur recommandée : $k_1 = 1{,}0$.

**b)** Nœuds soumis à compression et à traction, avec tirants ancrés dans **une** direction (Figure 6.27) :

$$\sigma_{Rd,max} = k_2\, \nu'\, f_{cd} \tag{6.61}$$

> **Note :** Valeur recommandée : $k_2 = 0{,}85$.

**c)** Nœuds soumis à compression et à traction, avec tirants ancrés dans **plus d'une** direction (Figure 6.28) :

$$\sigma_{Rd,max} = k_3\, \nu'\, f_{cd} \tag{6.62}$$

> **Note :** Valeur recommandée : $k_3 = 0{,}75$.

**(5)** Les valeurs de calcul données en 6.5.4 (4) peuvent être majorées jusqu'à 10%, lorsqu'au moins l'une des conditions ci-après s'applique :
- une compression tri-axiale est assurée
- tous les angles entre bielles et tirants sont ≥ 55°
- les contraintes au droit des appuis ou des charges ponctuelles sont uniformes, et le nœud est confiné par des armatures transversales
- les armatures sont disposées selon plusieurs cours
- le nœud est confiné de manière fiable par une disposition particulière d'appui ou par frottement

**(6)** Les nœuds soumis à une compression tri-axiale peuvent être vérifiés au moyen des Expressions (3.24) et (3.25) avec $\sigma_{Rd,max} \leq k_4\, \nu'\, f_{cd}$.

> **Note :** Valeur recommandée : $k_4 = 3{,}0$.

**(7)** L'ancrage des armatures dans les nœuds soumis à compression et à traction commence à l'entrée du nœud. Il convient que la longueur d'ancrage couvre toute la longueur du nœud.

**(8)** Les nœuds, comprimés à la jonction de trois bielles co-planaires, peuvent être vérifiés conformément à la Figure 6.26. On peut normalement admettre $F_{cd,1}/a_1 = F_{cd,2}/a_2 = F_{cd,3}/a_3$, ce qui entraîne $\sigma_{cd,1} = \sigma_{cd,2} = \sigma_{cd,3} = \sigma_{cd,0}$.

**(9)** Les nœuds correspondant aux parties courbes des armatures peuvent être calculés conformément à la Figure 6.28.

# 6.6 Ancrages et recouvrements

**(1)P** La valeur de calcul de la contrainte d'adhérence est limitée à une valeur qui dépend des caractéristiques de surface des armatures, de la résistance en traction du béton et du confinement du béton entourant ces armatures (enrobage, armatures transversales, pression transversale).

**(2)** La longueur nécessaire au développement de l'effort de traction requis dans l'ancrage ou le recouvrement est calculée en admettant une contrainte d'adhérence constante.

**(3)** Les règles d'application relatives au dimensionnement des ancrages et des recouvrements ainsi qu'aux dispositions constructives correspondantes sont données en 8.4 à 8.8.

---

# 6.7 Pressions localisées

**(1)P** Dans le cas de pressions localisées, on doit considérer l'écrasement local ainsi que les efforts transversaux de traction générés (voir 6.5).

**(2)** Dans le cas d'une charge uniformément répartie sur une surface $A_{c0}$ (voir Figure 6.29), l'effort de compression limite :

$$F_{Rdu} = A_{c0} \cdot f_{cd} \cdot \sqrt{A_{c1} / A_{c0}} \leq 3{,}0 \cdot f_{cd} \cdot A_{c0} \tag{6.63}$$

où :
- $A_{c0}$ : aire chargée
- $A_{c1}$ : aire maximale de diffusion utilisée pour le calcul, $A_{c1}$ et $A_{c0}$ étant homothétiques

**(3)** L'aire de diffusion $A_{c1}$ doit satisfaire les conditions suivantes :
- la hauteur de diffusion de la charge dans la direction de celle-ci est telle qu'indiquée sur la Figure 6.29
- le centre de $A_{c1}$ est situé sur la ligne d'action passant par le centre de $A_{c0}$
- si la section de béton est soumise à plusieurs efforts de compression, il convient de disjoindre les aires de diffusion

Il convient de réduire $F_{Rdu}$ si la charge n'est pas uniformément répartie sur $A_{c0}$ ou s'il existe des efforts tranchants importants.

**(4)** Il convient de prévoir des armatures pour reprendre les efforts de traction transversale dus à l'effet de la charge.

> **Figure 6.29** — *Hypothèses de diffusion pour le calcul dans le cas de pressions localisées* — *[Figure non extractable — voir document source]*

# 6.8 Fatigue

## 6.8.1 Conditions de vérification

**(1)P** La résistance des structures à la fatigue doit, dans certains cas particuliers, faire l'objet d'une vérification. Cette vérification doit être effectuée séparément pour le béton et pour l'acier.

**(2)** Il convient d'effectuer une vérification à la fatigue pour les structures et les éléments de structure soumis à des cycles de chargement réguliers (chemins de roulement de grues, ponts soumis à des charges de trafic élevées).

---

## 6.8.2 Efforts internes et contraintes pour la vérification à la fatigue

**(1)P** Le calcul des contraintes doit être conduit dans l'hypothèse de sections fissurées, en négligeant la résistance en traction du béton mais en assurant la compatibilité des déformations.

**(2)P** L'effet de la différence de comportement vis-à-vis de l'adhérence entre armatures de béton armé et de précontrainte est pris en compte par le coefficient $\eta$ :

$$\eta = \frac{A_s + A_P}{A_s + A_P / (\xi\, \sqrt{\phi_s / \phi_P})} \tag{6.64}$$

où :
- $A_s$ : aire des armatures de béton armé
- $A_P$ : aire des armatures de précontrainte
- $\phi_S$ : plus grand diamètre des armatures de béton armé
- $\phi_P$ : diamètre réel ou équivalent des armatures de précontrainte ($\phi_P = 1{,}6\,\sqrt{A_P}$ pour les paquets ; $1{,}75\,\phi_{wire}$ pour les monotorons 7 fils ; $1{,}20\,\phi_{wire}$ pour les monotorons 3 fils)
- $\xi$ : rapport de la capacité d'adhérence des armatures de précontrainte adhérentes à celle des armatures à haute résistance

**Tableau 6.2 — Rapport $\xi$ de la capacité d'adhérence**

| Type d'armature de précontrainte | Post-tension adhérente | Pré-tension ≤ C50/60 | Pré-tension ≥ C70/85 |
|---|---|---|---|
| Barres ou fils lisses | — | 0,3 | 0,15 |
| Torons | 0,6 | 0,5 | 0,25 |
| Fils crantés | 0,7 | 0,6 | 0,3 |
| Barres à haute adhérence | 0,8 | 0,7 | 0,35 |

**(3)** Pour le calcul des armatures d'effort tranchant, l'inclinaison des bielles de compression pour la fatigue :

$$\tan\theta_{fat} = \sqrt{\tan\theta} \leq 1{,}0 \tag{6.65}$$

---

## 6.8.3 Combinaison d'actions

**(1)P** Pour le calcul des étendues de contrainte, on doit faire la distinction entre actions non cycliques et actions cycliques génératrices de fatigue.

**(2)P** La combinaison de base des charges non cycliques est similaire à la combinaison fréquente utilisée pour l'ELS :

$$E_d = E\left\{G_{k,j};\, P;\, \psi_{1,1}\, Q_{k,1};\, \psi_{2,i}\, Q_{k,i}\right\} \quad j \geq 1;\; i > 1 \tag{6.66}$$

**(3)P** L'action cyclique doit être combinée avec la combinaison de base défavorable :

$$E_d = E\left\{\left\{G_{k,j};\, P;\, \psi_{1,1}\, Q_{k,1};\, \psi_{2,i}\, Q_{k,i}\right\};\, Q_{fat}\right\} \tag{6.68}$$

où $Q_{fat}$ est la charge de fatigue considérée (charge de trafic selon l'EN 1991 ou autre charge cyclique).

---

## 6.8.4 Procédure de vérification pour les armatures

**(1)** L'endommagement pour un cycle d'étendue de contrainte $\Delta\sigma$ peut être déterminé à l'aide des courbes S-N (Figure 6.30). Il convient de multiplier la charge appliquée par $\gamma_{F,fat}$ et de diviser l'étendue de contrainte résistante $\Delta\sigma_{Rsk}$ par $\gamma_{s,fat}$.

> **Note 1 :** Valeur recommandée : $\gamma_{F,fat} = 1{,}0$.

**Tableau 6.3N — Paramètres des courbes S-N pour les armatures de béton armé**

| Type d'armatures | $N^*$ | $k_1$ | $k_2$ | $\Delta\sigma_{Rsk}$ (MPa) pour $N^*$ cycles |
|---|---|---|---|---|
| Barres droites et barres pliées | $10^6$ | 5 | 9 | 162,5 |
| Barres soudées et treillis soudés | $10^7$ | 3 | 5 | 58,5 |
| Dispositifs de couplage | $10^7$ | 3 | 5 | 35 |

> **Note :** Pour les barres pliées, appliquer un coefficient de réduction $\zeta = 0{,}35 + 0{,}026\, D/\phi$ (où $D$ = diamètre du mandrin).

**Tableau 6.4N — Paramètres des courbes S-N pour les armatures de précontrainte**

| Type | $N^*$ | $k_1$ | $k_2$ | $\Delta\sigma_{Rsk}$ (MPa) |
|---|---|---|---|---|
| Pré-tension | $10^6$ | 5 | 9 | 185 |
| Post-tension — monotorons gaine plastique | $10^6$ | 5 | 9 | 185 |
| Post-tension — armatures droites ou courbes gaine plastique | $10^6$ | 5 | 10 | 150 |
| Post-tension — armatures courbes gaine acier | $10^6$ | 5 | 7 | 120 |
| Post-tension — dispositifs de couplage | $10^6$ | 5 | 5 | 80 |

**(2)** Pour des cycles multiples d'étendue variable, l'endommagement peut être cumulé par la règle de Palmgren-Miner :

$$D_{Ed} = \sum_i \frac{n(\Delta\sigma_i)}{N(\Delta\sigma_i)} < 1 \tag{6.70}$$

**(3)P** Les contraintes calculées ne doivent pas excéder la limite d'élasticité de calcul de l'acier.

---

## 6.8.5 Vérification à l'aide de l'étendue de contrainte équivalente

**(1)** Au lieu d'une vérification explicite de l'endommagement, la vérification à la fatigue peut également être effectuée en utilisant des étendues de contrainte équivalentes.

**(3)** La résistance en fatigue est satisfaisante si :

$$\gamma_{F,fat} \cdot \Delta\sigma_{S,equ}(N^*) \leq \Delta\sigma_{Rsk}(N^*) / \gamma_{s,fat} \tag{6.71}$$

---

## 6.8.6 Autres vérifications

**(1)** On peut admettre que la résistance en fatigue des barres d'armature **non soudées** travaillant en traction est satisfaisante si :

$$\Delta\sigma_S \leq k_1 \quad \text{(valeur recommandée : } k_1 = 70 \text{ MPa)}$$

Pour les barres d'armatures **soudées** :

$$\Delta\sigma_S \leq k_2 \quad \text{(valeur recommandée : } k_2 = 35 \text{ MPa)}$$

sous une charge cyclique fréquente associée à la combinaison de base.

**(3)** Lorsque des assemblages soudés ou des dispositifs de couplage sont utilisés dans le béton précontraint, il convient d'éviter toute contrainte de traction dans le béton jusqu'à une distance de 200 mm des armatures, sous la combinaison fréquente avec un coefficient $k_3$ appliqué à la valeur moyenne de la force de précontrainte $P_m$.

> **Note :** Valeur recommandée : $k_3 = 0{,}9$.

---

## 6.8.7 Vérification du béton soumis à un effort de compression ou à un effort tranchant

**(1)** La résistance en fatigue du béton travaillant en compression est satisfaisante si :

$$E_{cd,max,equ} + 0{,}43\,\sqrt{1 - R_{equ}} \leq 1 \tag{6.72}$$

avec :

$$R_{equ} = E_{cd,min,equ} / E_{cd,max,equ} \tag{6.73}$$

$$f_{cd,fat} = k_1\, \beta_{cc}(t_0)\, f_{cd}\left(1 - \frac{f_{ck}}{250}\right) \tag{6.76}$$

> **Note :** Valeur recommandée pour $N = 10^6$ cycles : $k_1 = 0{,}85$.

**(2)** Simplification : la résistance en fatigue du béton en compression est satisfaisante si :

$$\sigma_{c,max} \leq 0{,}5\, f_{cd,fat} + 0{,}45\, \sigma_{c,min} \tag{6.77}$$

$$\leq 0{,}9\, f_{cd,fat} \text{ pour } f_{ck} \leq 50 \text{ MPa}$$
$$\leq 0{,}8\, f_{cd,fat} \text{ pour } f_{ck} > 50 \text{ MPa}$$

**(3)** L'Expression (6.77) s'applique également aux bielles de compression des éléments soumis à des sollicitations d'effort tranchant. Dans ce cas, il convient de réduire $f_{cd,fat}$ par application du coefficient $\nu$ (voir 6.2.2 (6)).

**(4)** Pour les éléments pour lesquels aucune armature d'effort tranchant n'est requise à l'ELU :

Pour $V_{Ed,min} / V_{Ed,max} \geq 0$ :

$$|V_{Ed,max}| / V_{Rd,c} \leq 0{,}5 + 0{,}45\, |V_{Ed,min}| / V_{Rd,c} \tag{6.78}$$

$$\leq 0{,}9 \text{ jusqu'à C50/60 ; } \leq 0{,}8 \text{ au-delà de C55/67}$$

Pour $V_{Ed,min} / V_{Ed,max} < 0$ :

$$|V_{Ed,max}| / V_{Rd,c} \leq 0{,}5 - |V_{Ed,min}| / V_{Rd,c} \tag{6.79}$$

---

Liens : [[EC2_index]] · [[EC2_5_analyse-structurale.md]] · [[EC2_7_els.md]] · [[_Knowledge — Index]] · [[CLAUDE]]
