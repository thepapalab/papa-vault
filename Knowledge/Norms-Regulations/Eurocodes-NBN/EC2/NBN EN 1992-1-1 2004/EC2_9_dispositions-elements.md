---
title: "9 Dispositions constructives relatives aux éléments et règles particulières"
source: "EN 1992-1-1:2004 (F) — Eurocode 2 : Calcul des structures en béton"
norm: EC2
section: "9"
chapter: "9"
part: "1-1"
tags: [EC2, dispositions-constructives, armatures, poutres, dalles, poteaux, voiles, fondations, chaînages, poinçonnement, ancrage]
language: fr
jupyter_ref: "EC2/9"
---

# 9 Dispositions constructives relatives aux éléments et règles particulières

## 9.1 Généralités

**(1)P** Les exigences vis-à-vis de la sécurité, de l'aptitude au service et de la durabilité sont satisfaites par application des règles données dans cette Section en plus des règles générales données par ailleurs.

**(2)** Il convient que les dispositions constructives des éléments soient conformes aux modèles de calcul adoptés.

**(3)** Des sections minimales d'armatures sont prescrites afin d'empêcher une rupture fragile, de larges fissures et également pour résister à des efforts provenant d'actions gênées.

> Note : Les règles données dans cette Section sont principalement applicables aux bâtiments en béton armé.

## 9.2 Poutres

### 9.2.1 Armatures longitudinales

#### 9.2.1.1 Sections minimale et maximale d'armatures

**(1)** Il convient que la section d'armatures longitudinales tendues ne soit pas inférieure à $A_{s,min}$.

> Note 1 : Voir également 7.3 pour la section d'armatures longitudinale tendues permettant la maîtrise de la fissuration.
>
> Note 2 : La valeur de $A_{s,min}$ à utiliser dans un pays donné peut être fournie par son Annexe Nationale. La valeur recommandée est :

$$A_{s,min} = 0{,}26\, \frac{b_t\, d\, f_{ctm}}{f_{yk}} \geq 0{,}0013\, b_t\, d \tag{9.1N}$$

où $b_t$ = largeur moyenne de la zone tendue. Pour une poutre en T dont la membrure supérieure est comprimée, seule la largeur de l'âme est prise en compte pour $b_t$.

Toutefois, pour les éléments secondaires, $A_{s,min}$ peut être égal à 1,2 fois la section exigée dans la vérification aux ELU.

**(2)** Il convient de considérer les sections contenant une quantité d'armatures inférieure à $A_{s,min}$ comme des sections non armées (voir la Section 12).

**(3)** Il convient que la section des armatures tendues ou comprimées n'excède pas $A_{s,max}$ en dehors des zones de recouvrement.

> Note : Valeur recommandée : $A_{s,max} = 0{,}04\, A_c$.

**(4)** Pour des éléments précontraints avec des armatures non adhérentes de manière permanente ou avec des câbles extérieurs de précontrainte, il convient de vérifier que le moment résistant ultime est supérieur au moment de fissuration en flexion. Un moment résistant de 1,15 fois le moment de fissuration est suffisant.

#### 9.2.1.2 Autres dispositions constructives

**(1)** Pour une poutre formant une construction monolithique avec ses appuis, il convient de dimensionner la section sur appuis pour un moment fléchissant résultant de l'encastrement partiel d'au moins $\beta_1$ fois le moment fléchissant maximal en travée, y compris lorsque des appuis simples ont été adoptés dans le calcul.

> Note : Valeur recommandée : $\beta_1 = 0{,}15$.

**(2)** Aux appuis intermédiaires des poutres continues, il convient de répartir la section totale des armatures tendues $A_s$ d'une section transversale en T sur la largeur participante de la membrure supérieure (voir 5.3.2). Une partie de ces armatures peut être concentrée au droit de l'âme.

**(3)** Il convient de maintenir toute armature longitudinale comprimée (de diamètre $\phi$) prise en compte dans le calcul de résistance au moyen d'armatures transversales espacées au plus de $15\phi$.

#### 9.2.1.3 Épure d'arrêt des armatures longitudinales tendues

**(1)** Il convient, dans toutes les sections, de prévoir un ferraillage suffisant pour résister à l'enveloppe de l'effort de traction agissant, comprenant l'effet des fissures inclinées dans les âmes et les membrures.

**(2)** Pour des éléments avec des armatures d'effort tranchant, il convient de calculer l'effort de traction supplémentaire $\Delta F_{td}$ conformément à 6.2.3 (7). Pour des éléments sans armatures d'effort tranchant, $\Delta F_{td}$ peut être estimé en décalant la courbe enveloppe des moments d'une distance $a_l = d$, conformément à 6.2.2 (5). Cette "règle de décalage" peut également être employée pour des éléments comportant un ferraillage d'effort tranchant :

$$a_l = \frac{z\, (\cot\theta - \cot\alpha)}{2} \tag{9.2}$$

**(3)** La résistance des barres sur leur longueur d'ancrage peut être prise en compte en supposant une variation linéaire de l'effort. Par sécurité, la contribution de cette longueur d'ancrage peut être négligée.

**(4)** Il convient que la longueur d'ancrage d'une barre relevée contribuant à la résistance à l'effort tranchant ne soit pas inférieure à $1{,}3\, l_{bd}$ dans la zone tendue et à $0{,}7\, l_{bd}$ dans la zone comprimée. Cette longueur est mesurée à partir du point d'intersection de l'axe de la barre relevée et de celui des armatures longitudinales.

#### 9.2.1.4 Ancrage des armatures inférieures au niveau des appuis d'extrémité

**(1)** Il convient, au niveau des appuis considérés dans le calcul comme faiblement ou pas encastrés, que l'aire des armatures inférieures soit au moins $\beta_2$ fois l'aire des armatures présente en travée.

> Note : Valeur recommandée : $\beta_2 = 0{,}25$.

**(2)** L'effort de traction à ancrer peut être déterminé conformément à 6.2.3 (7), en incluant l'effet de l'effort normal s'il existe, ou en appliquant la règle de décalage :

$$F_E = \frac{|V_{Ed}|\, a_l}{z} + N_{Ed} \tag{9.3}$$

**(3)** La longueur d'ancrage est $l_{bd}$ conformément à 8.4.4, mesurée à partir de la ligne de contact entre la poutre et l'appui. La pression transversale peut être prise en compte pour un appui direct.

#### 9.2.1.5 Ancrage des armatures inférieures au niveau des appuis intermédiaires

**(1)** L'aire de la section des armatures indiquée en 9.2.1.4 (1) s'applique.

**(2)** Il convient que la longueur d'ancrage ne soit pas inférieure à $10\phi$ dans le cas des barres droites, au diamètre du mandrin dans le cas des crochets et des coudes avec des diamètres de barre au moins égaux à 16 mm, ou à deux fois le diamètre du mandrin dans les autres cas.

**(3)** Il convient de spécifier, dans des documents du contrat, les armatures exigées pour résister à des moments positifs éventuels (tassement de l'appui, explosion, etc.). Il convient que ces armatures soient continues, ce qui peut être réalisé au moyen de recouvrements.

### 9.2.2 Armatures d'effort tranchant

**(1)** Il convient que les armatures d'effort tranchant forment un angle $\alpha$ compris entre 45° et 90° avec l'axe longitudinal de l'élément structural.

**(2)** Les armatures d'effort tranchant peuvent être composées d'une combinaison de cadres, étriers ou épingles entourant les armatures longitudinales tendues et la zone comprimée ; barres relevées ; cadres ouverts, échelles, épingles, etc., correctement ancrés dans les zones comprimées et tendues.

**(3)** Il convient que les cadres, étriers et épingles soient efficacement ancrés. Un recouvrement sur le brin vertical situé près de la surface de l'âme est autorisé sous réserve que le cadre ne participe pas à la résistance à la torsion.

**(4)** Il convient qu'au moins $\beta_3$ des armatures d'effort tranchant nécessaires soient sous forme de cadres, étriers ou épingles.

> Note : Valeur recommandée : $\beta_3 = 0{,}5$.

**(5)** Le taux d'armatures d'effort tranchant :

$$\rho_w = \frac{A_{sw}}{s\, b_w\, \sin\alpha} \geq \rho_{w,min} \tag{9.4}$$

> Note : Valeur recommandée :
> $$\rho_{w,min} = \frac{0{,}08\, \sqrt{f_{ck}}}{f_{yk}} \tag{9.5N}$$

**(6)** Espacement longitudinal maximal :

$$s_{l,max} = 0{,}75\, d\, (1 + \cot\alpha) \tag{9.6N}$$

**(7)** Espacement longitudinal maximal entre barres relevées :

$$s_{b,max} = 0{,}6\, d\, (1 + \cot\alpha) \tag{9.7N}$$

**(8)** Espacement transversal maximal des brins verticaux dans une série de cadres :

$$s_{t,max} = 0{,}75\, d \leq 600 \text{ mm} \tag{9.8N}$$

### 9.2.3 Armatures de torsion

**(1)** Il convient que les cadres de torsion soient fermés et soient ancrés au moyen de recouvrements ou de crochets et qu'ils soient perpendiculaires à l'axe de l'élément structural.

**(2)** Les recommandations de 9.2.2 (5) et (6) sont généralement suffisantes pour la définition de la quantité minimale de cadres de torsion.

**(3)** Il convient que l'espacement longitudinal des cadres de torsion ne soit pas supérieur à $u/8$ (voir 6.3.2), ou à la limite du 9.2.2 (6), ou encore à la plus petite dimension de la section transversale de la poutre.

**(4)** Il convient de disposer les barres longitudinales de sorte qu'il y ait au moins une barre à chaque angle, les autres étant distribuées uniformément le long du périmètre intérieur des cadres, avec un espacement n'excédant pas 350 mm.

### 9.2.4 Armatures de peau

**(1)** Il peut être nécessaire de prévoir des armatures de peau, soit pour maîtriser la fissuration soit pour assurer une résistance adaptée à éclatement de l'enrobage.

> Note : Des règles de dispositions constructives pour les armatures de peau sont données en Annexe Informative J.

### 9.2.5 Appuis indirects

**(1)** Lorsqu'une poutre est portée par une autre poutre, au lieu d'un voile ou d'un poteau, il convient que les armatures soient conçues pour résister aux réactions mutuelles. Cette règle s'applique également à une dalle qui n'est pas appuyée en partie supérieure d'une poutre.

**(2)** Il convient que les armatures de suspente à l'intersection de deux poutres se composent de cadres et d'étriers entourant les armatures principales de l'élément porteur.

## 9.3 Dalles pleines

**(1)** La présente clause s'applique aux dalles pleines uni-directionnelles et bi-directionnelles pour lesquelles $b$ et $l_{eff}$ ne sont pas inférieures à $5h$ (voir 5.3.1).

### 9.3.1 Armatures de flexion

#### 9.3.1.1 Généralités

**(1)** Pour le pourcentage d'acier minimal et le pourcentage d'acier maximal dans la direction principale, 9.2.1.1 (1) et (3) s'appliquent.

**(2)** Il convient de prévoir, dans les dalles uni-directionnelles, des armatures transversales secondaires représentant au moins 20% des armatures principales.

**(3)** Espacement maximal $s_{max,slabs}$ :
- armatures principales : $s_{max,slabs} = 3h \leq 400$ mm
- armatures secondaires : $s_{max,slabs} = 3{,}5h \leq 450$ mm

Dans les zones de moment maximal ou de charges concentrées :
- armatures principales : $2h \leq 250$ mm
- armatures secondaires : $3h \leq 400$ mm

**(4)** Les règles données en 9.2.1.3 (1) à (3), 9.2.1.4 (1) à (3), et 9.2.1.5 (1) à (2) s'appliquent également, mais avec $a_l = d$.

#### 9.3.1.2 Armatures dans les dalles au voisinage des appuis

**(1)** Dans les dalles sur appuis simples, il convient de prolonger jusqu'à l'appui la moitié des armatures calculées en travée, et de les y ancrer conformément à 8.4.4.

**(2)** Lorsqu'un encastrement partiel se produit le long du bord d'une dalle mais n'est pas pris en compte dans l'analyse, il convient que les armatures supérieures soient capables de résister à au moins 25% du moment maximal de la travée adjacente. Ces armatures se prolongent sur une longueur d'au moins 0,2 fois la longueur de la travée adjacente, mesurée à partir du nu de l'appui.

#### 9.3.1.3 Armatures d'angles

**(1)** Lorsque les dispositions constructives sur un appui sont telles que le soulèvement de la dalle dans un angle est empêché, il convient de prévoir des armatures appropriées.

#### 9.3.1.4 Armatures de bords libres

**(1)** Le long du bord libre (non appuyé) d'une dalle, il convient normalement de prévoir des armatures longitudinales et transversales.

**(2)** Les armatures courantes prévues pour une dalle peuvent tenir le rôle d'armatures de rive.

### 9.3.2 Armatures d'effort tranchant

**(1)** Lorsque des armatures d'effort tranchant sont prévues dans une dalle, il convient que son épaisseur soit au moins égale à 200 mm.

**(2)** En ce qui concerne les dispositions constructives des armatures d'effort tranchant, la valeur minimale et la définition du taux d'armatures du 9.2.2 s'appliquent, à moins qu'elles ne soient modifiées par ce qui suit.

**(3)** Dans les dalles, lorsque $|V_{Ed}| \leq (1/3)\, V_{Rd,max}$ (voir 6.2), les armatures d'effort tranchant peuvent consister entièrement en barres relevées ou en cadres, étriers ou épingles.

**(4)** Espacement longitudinal maximal :

$$s_{max} = 0{,}75\, d\, (1 + \cot\alpha) \tag{9.9}$$

Espacement longitudinal maximal des barres relevées :

$$s_{max} = d \tag{9.10}$$

**(5)** Il convient de limiter à $1{,}5d$ l'espacement transversal maximal des armatures d'effort tranchant.

## 9.4 Planchers-dalles

### 9.4.1 Dalle au droit des poteaux intérieurs

**(1)** Il convient que la disposition des armatures dans un plancher-dalle reflète son comportement mécanique en service.

**(2)** Au droit des poteaux intérieurs, il convient de disposer les armatures supérieures d'aire $0{,}5\, A_t$ sur une largeur égale à la somme de $0{,}125$ fois la largeur de panneau de dalle de part et d'autre du poteau. $A_t$ représente l'aire des armatures exigées pour reprendre le moment négatif total sur la somme des deux demi-panneaux adjacents au poteau.

**(3)** Au droit des poteaux intérieurs, il convient de prévoir des armatures inférieures (au moins 2 barres) dans les deux directions principales perpendiculaires qui traversent le poteau.

### 9.4.2 Dalle au droit de poteaux de rive ou d'angle

**(1)** Il convient que les armatures perpendiculaires à un bord libre, exigées pour transmettre les moments fléchissants de la dalle à un poteau de rive ou d'angle, soient disposées sur la largeur participante $b_e$.

### 9.4.3 Armatures de poinçonnement

**(1)** Lorsque des armatures de poinçonnement sont nécessaires (voir 6.4), il convient de les disposer entre l'aire chargée ou le poteau support jusqu'à la distance $kd$ à l'intérieur du contour à partir duquel les armatures d'effort tranchant ne sont plus exigées. Il convient de prévoir au moins deux cours périphériques de cadres ou étriers, espacés au maximum de $0{,}75d$.

Il convient que l'espacement des cadres ou étriers le long d'un contour ne soit pas supérieur à $1{,}5d$, quand celui-ci est à l'intérieur du contour de contrôle de référence. À l'extérieur du premier contour, l'espacement ne doit pas dépasser $2d$.

> Note : La valeur de $k$ est donnée en 6.4.5 (4).

**(2)** Lorsque des armatures de poinçonnement sont exigées, l'aire du brin d'un étrier $A_{sw,min}$ :

$$A_{sw,min}\, \frac{1{,}5\sin\alpha + \cos\alpha}{s_r\, s_t} \geq \frac{0{,}08\, \sqrt{f_{ck}}}{f_{yk}} \tag{9.11}$$

**(3)** Les barres relevées traversant l'aire chargée ou se trouvant à une distance de cette aire inférieure à $0{,}25d$ peuvent être utilisées comme armatures de poinçonnement.

**(4)** Il convient de limiter à $d/2$ la distance entre le nu d'un appui et les armatures de poinçonnement les plus proches. Lorsqu'une seule file de barres relevées est prévue, leur angle de pliage peut être réduit à 30°.

## 9.5 Poteaux

### 9.5.1 Généralités

**(1)** La présente clause traite des poteaux pour lesquels la plus grande dimension $h$ est inférieure ou égale à 4 fois la plus petite dimension $b$.

### 9.5.2 Armatures longitudinales

**(1)** Il convient que le diamètre des barres longitudinales ne soit pas inférieur à $\phi_{min}$.

> Note : Valeur recommandée : $\phi_{min} = 8$ mm.

**(2)** Il convient que la quantité totale d'armatures longitudinales ne soit pas inférieure à $A_{s,min}$ :

$$A_{s,min} = \max\left(0{,}10\, \frac{N_{Ed}}{f_{yd}} ;\; 0{,}002\, A_c\right) \tag{9.12N}$$

**(3)** Il convient de limiter l'aire de la section des armatures longitudinales à $A_{s,max}$ :

> Note : Valeur recommandée : $A_{s,max} = 0{,}04\, A_c$ hors zones de recouvrement. Au droit des recouvrements : $0{,}08\, A_c$.

**(4)** Pour des poteaux de section polygonale, il convient de disposer au moins une barre dans chaque angle. Dans un poteau circulaire, au moins quatre barres longitudinales.

### 9.5.3 Armatures transversales

**(1)** Il convient que le diamètre des armatures transversales (cadres, boucles ou armature en hélice) ne soit pas inférieur à 6 mm ou au quart du diamètre maximal des barres longitudinales. Le diamètre des fils du treillis soudé ne doit pas être inférieur à 5 mm.

**(2)** Il convient d'ancrer convenablement les armatures transversales.

**(3)** Espacement maximal $s_{cl,tmax}$ le long du poteau : plus petite des valeurs :
- 20 fois le diamètre minimal des barres longitudinales
- la plus petite dimension du poteau
- 400 mm

**(4)** Il convient de réduire l'espacement maximal exigé en (3) par un facteur de 0,6 : (i) dans les sections situées à une distance au plus égale à la plus grande dimension de la section transversale du poteau ; (ii) dans les zones de recouvrement d'armatures, si le diamètre maximal des barres longitudinales est supérieur à 14 mm.

**(5)** Lorsque la direction des barres longitudinales change, il convient de calculer l'espacement des armatures transversales en tenant compte des efforts transversaux associés. Ces effets peuvent être ignorés si le changement de direction est inférieur ou égal à 1 pour 12.

**(6)** Il convient que chaque barre longitudinale ou paquet de barres longitudinales placé dans un angle soit maintenu par des armatures transversales. Il convient, dans une zone comprimée, de ne pas disposer de barre non tenue à moins de 150 mm d'une barre tenue.

## 9.6 Voiles

### 9.6.1 Généralités

**(1)** La présente clause se rapporte aux voiles en béton armé dont la longueur est au moins égale à 4 fois l'épaisseur et dont les armatures sont prises en compte dans le calcul de la résistance. Pour les voiles soumis principalement à une flexion due à des charges non-coplanaires, les règles pour les dalles s'appliquent (voir 9.3).

### 9.6.2 Armatures verticales

**(1)** Il convient que l'aire de la section des armatures verticales soit comprise entre $A_{s,vmin}$ et $A_{s,vmax}$.

> Note : Valeurs recommandées : $A_{s,vmin} = 0{,}002\, A_c$ ; $A_{s,vmax} = 0{,}04\, A_c$ hors zones de recouvrement (doublable au droit des recouvrements).

**(2)** Lorsque le calcul conduit à prévoir l'aire minimale d'armatures, il convient de disposer la moitié de cette aire sur chaque face.

**(3)** Il convient de limiter la distance entre deux barres verticales adjacentes à 3 fois l'épaisseur du voile ou à 400 mm si cette valeur est inférieure.

### 9.6.3 Armatures horizontales

**(1)** Il convient de prévoir des armatures horizontales parallèles aux parements du voile sur chaque face, d'aire au moins égale à $A_{s,hmin}$.

> Note : Valeur recommandée : 25% des armatures verticales ou $0{,}001\, A_c$, si cette valeur est supérieure.

**(2)** Il convient de limiter à 400 mm l'espacement entre deux barres horizontales adjacentes.

### 9.6.4 Armatures transversales

**(1)** Dans toute partie d'un voile où l'aire totale des armatures verticales placées sur les deux faces est supérieure à $0{,}02\, A_c$, il convient de prévoir des armatures transversales conformément aux exigences données pour les poteaux (voir 9.5.3). La grande dimension citée en 9.5.3 (4) (i) n'a pas à être prise supérieure à 4 fois l'épaisseur du voile.

**(2)** Lorsque les armatures principales sont celles des lits situés le plus près des parements du voile, il convient de prévoir au moins 4 armatures transversales en forme de cadre ou d'étrier par m² de surface de voile.

> Note : Il n'est pas nécessaire de prévoir des armatures transversales lorsque des treillis soudés et des barres de diamètre $\phi \leq 16$ mm sont employés avec un enrobage de béton supérieur à $2\phi$.

## 9.7 Poutres-cloisons

**(1)** Il convient normalement de ferrailler les poutres-cloisons avec des treillis d'armatures perpendiculaires situés près de chaque face, avec un minimum de $A_{s,dbmin}$.

> Note : Valeur recommandée : 0,1% avec un minimum de 150 mm²/m sur chaque face et dans chaque direction.

**(2)** Il convient de limiter la distance entre deux barres adjacentes de la maille à deux fois l'épaisseur de la poutre-cloison ou à 300 mm si cette valeur est inférieure.

**(3)** Il convient d'ancrer les armatures correspondant aux tirants soit en pliant les barres, soit en employant des retours en U, soit encore au moyen de dispositifs d'ancrage, à moins qu'une longueur suffisante soit disponible permettant une longueur d'ancrage de $l_{bd}$.

## 9.8 Fondations

### 9.8.1 Semelles en tête de pieux

**(1)** Il convient que la distance du bord externe du pieu au bord de la semelle soit telle que les efforts de liaison dans la semelle puissent être correctement ancrés.

**(2)** Il convient de calculer les armatures dans une semelle en tête de pieux en employant la méthode adéquate — méthode des bielles et tirants ou méthode par flexion.

**(3)** Il convient de concentrer les armatures principales de traction résistant aux effets des actions dans les zones tendues situées entre les pieux. Diamètre minimal : $\phi_{min} = 8$ mm (valeur recommandée).

**(4)** Des barres transversales soudées peuvent être employées pour l'ancrage des armatures tendues.

**(5)** On peut considérer que la compression provoquée par la réaction d'appui du pieu se diffuse avec un angle de 45° à partir du bord de celui-ci. Cette compression peut être prise en compte dans le calcul de la longueur d'ancrage.

### 9.8.2 Semelles de fondation de poteaux ou de voiles

#### 9.8.2.1 Généralités

**(1)** Il convient d'ancrer les armatures principales conformément aux stipulations de 8.4 et de 8.5 et de respecter un diamètre minimal d'armatures $\phi_{min} = 8$ mm (valeur recommandée).

**(2)** Les armatures principales des semelles circulaires peuvent être orthogonales et concentrées au milieu de la semelle sur une largeur de 50% ± 10% du diamètre de celle-ci. Les parties non armées sont considérées comme du béton non armé.

**(3)** Lorsque les effets des actions causent une traction sur l'extrados de la semelle, il convient de vérifier les contraintes de traction résultantes et de ferrailler en conséquence.

#### 9.8.2.2 Ancrage des barres

**(1)** Il convient que l'effort de traction $F_s$ trouvé à l'abscisse $x$ soit ancré dans le béton avant cette même distance $x$ prise à partir du bord de la semelle.

**(2)** L'effort de traction à ancrer :

$$F_s = R \cdot \frac{z_e}{z_i} \tag{9.13}$$

où $R$ = résultante de la pression du sol sur la distance $x$ ; $z_e$ = bras de levier des forces externes ; $z_i$ = bras de levier des forces internes.

**(3)** Comme simplification, $z_e$ peut être déterminé en supposant $e = 0{,}15b$ et $z_i = 0{,}9d$.

**(4)** La longueur d'ancrage disponible est $l_b$. Si cette longueur n'est pas suffisante pour ancrer $F_s$, les barres peuvent être soit repliées vers le haut, soit équipées de dispositifs d'ancrage d'extrémité.

**(5)** Pour les barres droites sans dispositif d'ancrage d'extrémité, la valeur minimale de $x$ est déterminante. Simplification : $x_{min} = h/2$.

### 9.8.3 Longrines de redressement

**(1)** Des longrines de redressement peuvent être employées pour équilibrer l'excentricité du chargement des fondations. Diamètre minimal : $\phi_{min} = 8$ mm (valeur recommandée).

**(2)** Il convient également de calculer les longrines de redressement pour une charge minimale descendante $q_1 = 10$ kN/m (valeur recommandée) si les engins de compactage peuvent solliciter les longrines.

### 9.8.4 Semelles de poteaux fondées au rocher

**(1)** Il convient de prévoir des armatures transversales adéquates pour résister aux efforts d'éclatement dans la semelle lorsque la pression du sol aux ELU est supérieure à $q_2 = 5$ MPa (valeur recommandée). Diamètre minimal : $\phi_{min} = 8$ mm.

**(2)** L'effort d'éclatement $F_s$ :

$$F_s = 0{,}25\left(1 - \frac{c}{h}\right) N_{Ed} \tag{9.14}$$

où $h$ est la plus petite des valeurs $b$ et $H$.

### 9.8.5 Pieux forés

**(1)** Les clauses suivantes s'appliquent aux pieux forés armés. Pour les pieux forés non armés, on se reportera à la Section 12.

**(2)** Afin de permettre une bonne mise en place du béton autour des armatures, il est primordial que les armatures, cages d'armatures et tout insert incorporé soient conçus de manière à ne pas compromettre l'écoulement du béton.

**(3)** Il convient d'équiper les pieux forés dont le diamètre est inférieur ou égal à $h_1 = 600$ mm (valeur recommandée) d'une section minimale d'armatures longitudinales $A_{s,bpmin}$.

**Tableau 9.6N — Armatures longitudinales minimales dans les pieux forés coulés en place**

| Section transversale du pieu $A_c$ | Aire minimale $A_{s,bpmin}$ |
|---|---|
| $A_c \leq 0{,}5$ m² | $A_s \geq 0{,}005\, A_c$ |
| $0{,}5 \text{ m}^2 < A_c \leq 1{,}0 \text{ m}^2$ | $A_s \geq 25$ cm² |
| $A_c > 1{,}0$ m² | $A_s \geq 0{,}0025\, A_c$ |

Diamètre minimal des barres longitudinales : 16 mm. Nombre minimal de barres : 6. Distance libre maximale entre barres mesurée sur le pourtour : 200 mm.

**(4)** Pour les dispositions constructives des armatures longitudinales et transversales dans les pieux forés, voir l'EN 1536.

## 9.9 Régions de discontinuités de géométrie ou d'action

**(1)** Il convient de concevoir les régions de discontinuités de géométrie ou d'action à partir de modèles bielles et tirants conformément à la clause 6.5, avec des dispositions constructives conformes aux règles données dans la Section 8.

> Note : Pour plus d'information, on se reportera à l'Annexe J.

**(2)P** Les armatures, correspondant aux tirants, doivent être entièrement ancrées, avec une longueur d'ancrage $l_{bd}$, conformément à 8.4.

## 9.10 Chaînages

### 9.10.1 Généralités

**(1)P** Les structures qui ne sont pas conçues pour résister aux actions accidentelles doivent posséder un système de chaînages approprié, destiné à empêcher l'effondrement progressif en fournissant des cheminements alternatifs pour les charges après apparition de dommages locaux.

**(2)** Il convient de prévoir les chaînages suivants :
- a) chaînages périphériques
- b) chaînages intérieurs
- c) chaînages horizontaux de poteau ou de voile
- d) si nécessaire, chaînages verticaux, en particulier dans des bâtiments construits en panneaux préfabriqués.

**(3)** Lorsqu'un bâtiment est divisé par des joints de dilatation en sections structurellement indépendantes, il convient que chaque section possède un système de chaînages indépendant.

**(4)** Dans le calcul des chaînages, on peut supposer que les armatures travaillent à leur résistance caractéristique et sont capables de supporter les efforts de traction définis dans les paragraphes suivants.

**(5)** Les armatures mises en place, à d'autres fins, dans les poteaux, voiles, poutres et planchers, peuvent être intégrées pour tout ou partie dans ces chaînages.

### 9.10.2 Répartition des chaînages

#### 9.10.2.1 Généralités

**(1)** Les chaînages sont supposés être des armatures minimales et pas des armatures supplémentaires, venant s'ajouter à celles exigées par l'analyse structurale.

#### 9.10.2.2 Chaînages périphériques

**(1)** Il convient de prévoir, à chaque plancher y compris celui en toiture, un chaînage périphérique effectivement continu à moins de 1,2 m de la rive.

**(2)** Il convient que le chaînage périphérique soit capable de résister à un effort de traction :

$$F_{tie,per} = l_i \cdot q_1 \leq Q_2 \tag{9.15}$$

> **Note :** Valeurs recommandées : $q_1 = 10$ kN/m et $Q_2 = 70$ kN.

**(3)** Il convient que les structures comportant des rives internes (atriums, cours, etc.) comportent des chaînages périphériques conçus comme ceux des rives externes, entièrement ancrés.

#### 9.10.2.3 Chaînages intérieurs

**(1)** Il convient de prévoir ces chaînages à chaque plancher y compris celui en toiture dans deux directions approximativement perpendiculaires. Il convient qu'ils soient effectivement continus sur toute leur longueur et qu'ils soient ancrés aux chaînages périphériques à chaque extrémité.

**(2)** Les chaînages intérieurs peuvent être répartis régulièrement dans les dalles ou être groupés au droit des poutres et des voiles. Dans les voiles, il convient qu'ils soient à moins de 0,5 m du dessus ou de la sous-face des dalles de plancher.

**(3)** Dans chaque direction, il convient que les chaînages intérieurs soient capables de résister à une valeur de calcul de l'effort de traction $f_{tie,int}$ (en kN par mètre de largeur).

> **Note :** Valeur recommandée : $f_{tie,int} = 20$ kN/m.

**(4)** Dans les planchers pour lesquels il n'est pas possible de répartir les chaînages dans les travées, les chaînages transversaux peuvent être groupés le long des lignes de poutre. Dans ce cas, l'effort minimal sur une ligne interne de poutre est :

$$F_{tie} = \frac{l_1 + l_2}{2} \cdot q_3 \leq Q_4 \tag{9.16}$$

> **Note :** Valeurs recommandées : $q_3 = 20$ kN/m et $Q_4 = 70$ kN.

**(5)** Il convient de relier les chaînages intérieurs aux chaînages périphériques de façon à ce que le transfert des efforts soit assuré.

#### 9.10.2.4 Chaînages horizontaux des poteaux et/ou des voiles

**(1)** À chaque plancher y compris celui en toiture, il convient de lier horizontalement les poteaux et les voiles de rive à la structure.

**(2)** Il convient que les chaînages soient capables de résister à un effort de traction $f_{tie,fac}$ par mètre de façade. Pour les poteaux, il n'est pas nécessaire que l'effort soit supérieur à $F_{tie,col}$.

> **Note :** Les valeurs de $f_{tie,fac}$ et $F_{tie,col}$ à utiliser dans un pays donné peuvent être fournies par son Annexe Nationale. Les valeurs recommandées sont $f_{tie,fac} = 20$ kN/m et $F_{tie,col} = 150$ kN.

**(3)** Il convient de lier les poteaux d'angle dans les deux directions. Dans ce cas, le chaînage périphérique peut être employé comme chaînage horizontal.

#### 9.10.2.5 Chaînages verticaux

**(1)** Dans les bâtiments en panneaux préfabriqués de 5 étages ou plus, il convient de prévoir des chaînages verticaux dans les poteaux et/ou les voiles afin de limiter les dommages dus à l'effondrement d'un plancher dans le cas de la perte accidentelle d'un poteau ou d'un voile le supportant. Il convient que ces chaînages fassent partie d'un système de pontage permettant un cheminement des efforts contournant la zone endommagée.

**(2)** Normalement, il convient de prévoir des chaînages verticaux continus du niveau le plus bas au niveau le plus élevé, capables de supporter la charge agissant, dans la situation accidentelle de calcul, sur le plancher au-dessus du poteau/voile perdu accidentellement. D'autres solutions, basées par exemple sur l'action de diaphragme des éléments de voile restants et/ou sur l'action de membrane dans les planchers, peuvent être employées si l'équilibre et une capacité de déformation suffisante peuvent être vérifiés.

**(3)** Lorsqu'un poteau ou un voile est soutenu à son niveau le plus bas par un élément autre qu'une fondation (poutre ou plancher-dalle, par exemple), il convient de considérer la perte accidentelle de cet élément dans le calcul et de prévoir un cheminement alternatif convenable pour les charges.

### 9.10.3 Continuité et ancrage des chaînages

**(1)P** Les chaînages dans deux directions horizontales doivent être effectivement continus et ancrés en périphérie de la structure.

**(2)** Des chaînages peuvent être prévus dans le béton de la dalle rapportée coulée en place ou dans celui des joints des éléments préfabriqués. Lorsque les chaînages ne sont pas continus dans un plan, il convient de considérer les effets de flexion résultant des excentricités.

**(3)** Il convient normalement de ne pas faire de recouvrement dans les chaînages placés dans les assemblages étroits entre éléments préfabriqués. Dans ces cas, il convient d'employer des ancrages mécaniques.
