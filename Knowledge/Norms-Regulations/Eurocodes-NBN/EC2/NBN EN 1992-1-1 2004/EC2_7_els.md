---
title: "NBN EN 1992-1-1:2004 — Els"
type: norm-extract
source: "NBN EN 1992-1-1:2004"
norm: EC2
section: "7"
chapter: "Els"
tags: [EC2, eurocode-2, els]
related: ["[[EC2_index]]", "[[EC2_6_elu.md]]", "[[EC2_8_dispositions-armatures.md]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# 7.1 Généralités

**(1)P** La présente section concerne les états-limites de service courants :
- limitation des contraintes (voir 7.2)
- maîtrise de la fissuration (voir 7.3)
- limitation des flèches (voir 7.4)

**(2)** Dans le calcul des contraintes et des flèches, il convient d'admettre que les sections sont non fissurées dès lors que la contrainte de traction en flexion n'excède pas $f_{ct,eff}$. La valeur de $f_{ct,eff}$ peut être prise égale à $f_{ctm}$ ou à $f_{ctm,fl}$ sous réserve d'utiliser la même valeur pour le calcul du ferraillage minimal de traction. Pour le calcul des ouvertures de fissures et de la participation du béton tendu, il convient d'utiliser $f_{ctm}$.

---

# 7.2 Limitation des contraintes

**(1)P** La contrainte de compression dans le béton doit être limitée afin d'éviter les fissures longitudinales, les micro-fissures ou encore des niveaux élevés de fluage, lorsque ceux-ci pourraient avoir des effets inacceptables pour le fonctionnement de la structure.

**(2)** Des fissures longitudinales peuvent apparaître si le niveau de contrainte sous la combinaison caractéristique de charges excède une valeur critique. En l'absence d'autres dispositions, il peut être pertinent de limiter les contraintes de compression à $k_1\, f_{ck}$ dans les parties exposées aux environnements XD, XF et XS.

> **Note :** Valeur recommandée : $k_1 = 0{,}6$.

**(3)** Si, sous charges quasi-permanentes, la contrainte dans le béton est inférieure à $k_2\, f_{ck}$, on peut admettre que le fluage est linéaire. Si la contrainte dans le béton excède $k_2\, f_{ck}$, il convient de considérer un fluage non-linéaire (voir 3.1.4).

> **Note :** Valeur recommandée : $k_2 = 0{,}45$.

**(4)P** Les contraintes de traction dans les armatures doivent être limitées afin d'éviter les déformations inélastiques ainsi qu'un niveau de fissuration ou de déformation inacceptable.

**(5)** On peut considérer qu'un niveau de fissuration ou de déformation inacceptable est évité si, sous la combinaison caractéristique de charges, la contrainte de traction dans les armatures n'excède pas $k_3\, f_{yk}$. Lorsque la contrainte est provoquée par une déformation imposée, la contrainte de traction est limitée à $k_4\, f_{yk}$. Il convient de limiter la valeur probable de la contrainte des armatures de précontrainte à $k_5\, f_{pk}$.

> **Note :** Valeurs recommandées : $k_3 = 0{,}8$ ; $k_4 = 1$ ; $k_5 = 0{,}75$.

# 7.3 Maîtrise de la fissuration

## 7.3.1 Considérations générales

**(1)P** La fissuration doit être limitée de telle sorte qu'elle ne porte pas préjudice au bon fonctionnement ou à la durabilité de la structure ou encore qu'elle ne rende pas son aspect inacceptable.

**(2)** La fissuration est normale dans les structures en béton armé soumises à des sollicitations de flexion, d'effort tranchant, de torsion ou de traction résultant soit d'un chargement direct soit de déformations gênées ou imposées.

**(5)** Il convient de définir une valeur limite de l'ouverture calculée des fissures ($w_{max}$) en tenant compte de la nature et du fonctionnement envisagés de la structure ainsi que du coût de la limitation de la fissuration.

**Tableau 7.1N — Valeurs recommandées de $w_{max}$ (mm)**

| Classe d'exposition | Béton armé et BP non adhérentes — quasi-permanente | BP adhérentes — fréquente |
|---|---|---|
| X0, XC1 | 0,4 ¹ | 0,2 |
| XC2, XC3, XC4 | 0,3 | 0,2 |
| XD1, XD2, XS1, XS2, XS3 | 0,3 | Décompression |

> **Note 1 :** Pour les classes X0 et XC1, l'ouverture des fissures n'a pas d'incidence sur la durabilité.

---

## 7.3.2 Sections minimales d'armatures

**(1)P** Si la maîtrise de la fissuration est requise, une quantité minimale d'armatures adhérentes est nécessaire pour maîtriser la fissuration dans les zones où l'on prévoit l'existence de contraintes de traction.

**(2)** Les sections minimales d'armatures peuvent être calculées comme suit :

$$A_{s,min}\, \sigma_s = k_c\, k\, f_{ct,eff}\, A_{ct} \tag{7.1}$$

où :
- $A_{s,min}$ : section minimale d'armatures dans la zone tendue
- $A_{ct}$ : aire de la section droite de béton tendu (juste avant la première fissure)
- $\sigma_s$ : valeur absolue de la contrainte maximale admise dans l'armature immédiatement après la formation de la fissure (peut être prise égale à $f_{yk}$)
- $f_{ct,eff} = f_{ctm}$ (ou $f_{ctm}(t)$ si fissuration avant 28 jours)
- $k$ : coefficient d'effet des contraintes non-uniformes auto-équilibrées :
  - $= 1{,}0$ pour les âmes $h \leq 300$ mm ou les membrures de largeur $< 300$ mm
  - $= 0{,}65$ pour les âmes $h \geq 800$ mm ou les membrures de largeur $> 800$ mm
  - Interpolation linéaire pour les valeurs intermédiaires
- $k_c$ : coefficient tenant compte de la répartition des contraintes dans la section :

**En traction pure :** $k_c = 1{,}0$

**En flexion simple ou flexion composée — sections rectangulaires et âmes :**

$$k_c = 0{,}4\left[1 - \frac{\sigma_c}{k_1\, (h/h^*)\, f_{ct,eff}}\right] \leq 1{,}0 \tag{7.2}$$

**En flexion simple ou flexion composée — membrures des caissons et sections en T :**

$$k_c = \frac{F_{cr}}{A_{ct}\, f_{ct,eff}} \geq 0{,}5 \tag{7.3}$$

avec :

$$\sigma_c = N_{Ed} / (b\, h) \tag{7.4}$$

- $k_1 = 1{,}5$ si $N_{Ed}$ est un effort de compression ; $k_1 = (2/3)\, h/h^*$ si $N_{Ed}$ est un effort de traction
- $h^* = h$ pour $h < 1{,}0$ m ; $h^* = 1{,}0$ m pour $h \geq 1{,}0$ m
- $F_{cr}$ : valeur absolue de l'effort de traction dans la membrure juste avant la fissuration

**(3)** On peut admettre que les armatures de précontrainte adhérentes situées dans la zone tendue contribuent à la maîtrise de la fissuration sur une distance ≤ 150 mm du centre de l'armature. Ceci peut être pris en compte en ajoutant le terme $\xi_1\, A_P'\, \Delta\sigma_p$ au membre gauche de l'Expression (7.1).

$$\xi_1 = \sqrt{\xi\, \phi_s / \phi_p} \tag{7.5}$$

**(4)** Dans les éléments précontraints, aucun ferraillage minimal n'est requis dans les sections où, sous la combinaison caractéristique de charges et pour la valeur caractéristique de la précontrainte, le béton est comprimé ou la valeur absolue de la contrainte de traction dans le béton est inférieure à $\sigma_{ct,p}$ (valeur recommandée : $f_{ct,eff}$).

---

## 7.3.3 Maîtrise de la fissuration sans calcul direct

**(2)** Les règles données en 7.3.4 peuvent être présentées sous forme de tableaux limitant le diamètre ou l'espacement des armatures.

**Tableau 7.2N — Diamètre maximal $\phi_s^*$ des barres (mm)**

| Contrainte acier (MPa) | $w_k = 0{,}4$ mm | $w_k = 0{,}3$ mm | $w_k = 0{,}2$ mm |
|---|---|---|---|
| 160 | 40 | 32 | 25 |
| 200 | 32 | 25 | 16 |
| 240 | 20 | 16 | 12 |
| 280 | 16 | 12 | 8 |
| 320 | 12 | 10 | 6 |
| 360 | 10 | 8 | 5 |
| 400 | 8 | 6 | 4 |
| 450 | 6 | 5 | — |

> Hypothèses : $c = 25$ mm ; $f_{ct,eff} = 2{,}9$ MPa ; $h_{cr} = 0{,}5$ ; $(h-d) = 0{,}1h$ ; $k_1 = 0{,}8$ ; $k_2 = 0{,}5$ ; $k_c = 0{,}4$ ; $k = 1{,}0$ ; $k_t = 0{,}4$ ; $k' = 1{,}0$.

**Tableau 7.3N — Espacement maximal des barres (mm)**

| Contrainte acier (MPa) | $w_k = 0{,}4$ mm | $w_k = 0{,}3$ mm | $w_k = 0{,}2$ mm |
|---|---|---|---|
| 160 | 300 | 300 | 200 |
| 200 | 300 | 250 | 150 |
| 240 | 250 | 200 | 100 |
| 280 | 200 | 150 | 50 |
| 320 | 150 | 100 | — |
| 360 | 100 | 50 | — |

**Correction du diamètre maximal :**

En flexion :

$$\phi_s = \phi_s^*\, (f_{ct,eff}/2{,}9)\, \frac{8\,(h-d)}{k_c\, h_{cr}} \tag{7.6N}$$

En traction axiale :

$$\phi_s = \phi_s^*\, (f_{ct,eff}/2{,}9)\, \frac{8\,(h-d)}{h_{cr}} \tag{7.7N}$$

**(3)** Dans le cas des poutres d'une hauteur totale supérieure ou égale à 1000 mm, dans lesquelles les armatures principales sont concentrées sur une petite portion de la hauteur seulement, il convient de prévoir des armatures de peau supplémentaires afin de maîtriser la fissuration sur les joues de la poutre. Ces armatures doivent être réparties régulièrement entre le niveau des armatures de traction et l'axe neutre, à l'intérieur de cadres. La section ne doit pas être inférieure à la valeur obtenue selon 7.3.2 (2) avec $k = 0{,}5$ et $\sigma_s = f_{yk}$.

---

## 7.3.4 Calcul de l'ouverture des fissures

**(1)** L'ouverture des fissures $w_k$ :

$$w_k = s_{r,max}\, (\varepsilon_{sm} - \varepsilon_{cm}) \tag{7.8}$$

où :
- $s_{r,max}$ : espacement maximal des fissures
- $\varepsilon_{sm}$ : déformation moyenne de l'armature sous la combinaison de charges considérée (incluant l'effet des déformations imposées et la participation du béton tendu)
- $\varepsilon_{cm}$ : déformation moyenne du béton entre les fissures

**(2)** $\varepsilon_{sm} - \varepsilon_{cm}$ peut être calculé au moyen de l'expression :

$$\varepsilon_{sm} - \varepsilon_{cm} = \frac{\sigma_s - k_t\, \frac{f_{ct,eff}}{\rho_{p,eff}}\, (1 + \alpha_e\, \rho_{p,eff})}{E_s} \geq 0{,}6\, \frac{\sigma_s}{E_s} \tag{7.9}$$

où :
- $\sigma_s$ : contrainte dans les armatures de béton armé tendues, en supposant la section fissurée
- $\alpha_e = E_s / E_{cm}$
- $\rho_{p,eff} = (A_s + \xi_1^2\, A_P') / A_{c,eff}$ $\tag{7.10}$
- $A_{c,eff}$ : aire de la section effective de béton autour des armatures tendues, de hauteur $h_{c,ef} = \min\{2{,}5(h-d) ;\, (h-x)/3 ;\, h/2\}$
- $k_t = 0{,}6$ pour un chargement de courte durée ; $k_t = 0{,}4$ pour un chargement de longue durée

**(3)** Lorsque les armatures adhérentes sont disposées dans la zone tendue avec un entraxe suffisamment faible (espacement $\leq 5\,(c + \phi/2)$), l'espacement final maximal des fissures :

$$s_{r,max} = k_3\, c + k_1\, k_2\, k_4\, \phi / \rho_{p,eff} \tag{7.11}$$

avec le diamètre équivalent pour $n_1$ barres de diamètre $\phi_1$ et $n_2$ barres de diamètre $\phi_2$ :

$$\phi_{eq} = \frac{n_1\, \phi_1^2 + n_2\, \phi_2^2}{n_1\, \phi_1 + n_2\, \phi_2} \tag{7.12}$$

où :
- $c$ : enrobage des armatures longitudinales
- $k_1 = 0{,}8$ pour les barres à haute adhérence ; $= 1{,}6$ pour les armatures à surface lisse
- $k_2 = 0{,}5$ en flexion ; $= 1{,}0$ en traction pure
- En cas de traction excentrée : $k_2 = (\varepsilon_1 + \varepsilon_2) / (2\, \varepsilon_1)$ $\tag{7.13}$

> **Note :** Valeurs recommandées : $k_3 = 3{,}4$ ; $k_4 = 0{,}425$.

Lorsque l'espacement des armatures adhérentes excède $5\,(c + \phi/2)$ ou lorsqu'il n'y a pas d'armatures adhérentes dans le béton tendu :

$$s_{r,max} = 1{,}3\, (h - x) \tag{7.14}$$

**(4)** Lorsque l'angle entre les directions des contraintes principales et les directions des armatures est significatif ($> 15°$) :

$$\frac{1}{s_{r,max}} = \frac{\cos\theta}{s_{r,max,y}} + \frac{\sin\theta}{s_{r,max,z}} \tag{7.15}$$

**(5)** Dans le cas des voiles soumis à un retrait thermique précoce pour lesquels la section d'armatures horizontales $A_s$ ne satisfait pas les exigences de 7.3.2 et dont le pied est encastré dans une semelle coulée au préalable, $s_{r,max}$ peut être pris égal à $1{,}3$ fois la hauteur du voile.

# 7.4 Limitation des flèches

## 7.4.1 Considérations générales

**(1)P** La déformation d'un élément ou d'une structure ne doit pas être préjudiciable à leur bon fonctionnement ou à leur aspect.

**(4)** L'aspect et la fonctionnalité générale de la structure sont susceptibles d'être altérés lorsque la flèche calculée d'une poutre, d'une dalle ou d'une console soumises à des charges quasi-permanentes est supérieure à $l/250$ où $l$ représente la portée. Une contre-flèche peut être prévue pour compenser en partie ou en totalité la déformation, toutefois la contre-flèche ne doit pas dépasser $l/250$.

**(5)** Pour la déformation après construction, $l/500$ représente normalement une limite adéquate pour les charges quasi-permanentes.

**(6)** L'état-limite de déformation peut être vérifié :
- en limitant le rapport portée/hauteur, comme indiqué en 7.4.2
- ou bien en comparant une déformation calculée, conformément à 7.4.3, à une valeur limite.

---

## 7.4.2 Cas de dispense du calcul

**(2)** La valeur limite du rapport portée/hauteur peut être obtenue à l'aide des Expressions suivantes :

Pour $\rho \leq \rho_0$ :

$$\frac{l}{d} = K\left[11 + 1{,}5\,\sqrt{f_{ck}}\, \frac{\rho_0}{\rho} + 3{,}2\,\sqrt{f_{ck}}\, \left(\frac{\rho_0}{\rho} - 1\right)^{3/2}\right] \tag{7.16a}$$

Pour $\rho > \rho_0$ :

$$\frac{l}{d} = K\left[11 + 1{,}5\,\sqrt{f_{ck}}\, \frac{\rho_0}{\rho - \rho'} + \frac{1}{12}\,\sqrt{f_{ck}}\, \sqrt{\frac{\rho'}{\rho_0}}\right] \tag{7.16b}$$

où :
- $l/d$ : valeur limite du rapport portée/hauteur
- $K$ : coefficient tenant compte des différents systèmes structuraux (voir Tableau 7.4N)
- $\rho_0 = \sqrt{f_{ck}} \cdot 10^{-3}$ : pourcentage d'armatures de référence
- $\rho$ : pourcentage d'armatures de traction nécessaire à mi-portée (ou sur appui dans le cas des consoles)
- $\rho'$ : pourcentage d'armatures de compression nécessaire à mi-portée
- $f_{ck}$ en MPa

Les Expressions (7.16a) et (7.16b) ont été établies en admettant que la contrainte de l'acier est égale à 310 MPa (ce qui correspond approximativement à $f_{yk} = 500$ MPa) sous les charges de calcul aux ELS. Pour d'autres niveaux de contrainte :

$$310 / \sigma_s = 500 / (f_{yk} \cdot A_{s,req} / A_{s,prov}) \tag{7.17}$$

**Tableau 7.4N — Valeurs de base du rapport portée/hauteur utile**

| Système structural | $K$ | $\rho = 1{,}5\%$ | $\rho = 0{,}5\%$ |
|---|---|---|---|
| Poutre / dalle sur appuis simples | 1,0 | 14 | 20 |
| Travée de rive d'une poutre continue / dalle continue | 1,3 | 18 | 26 |
| Travée intermédiaire d'une poutre ou d'une dalle | 1,5 | 20 | 30 |
| Dalle sans nervures sur poteaux (plancher-dalle) | 1,2 | 17 | 24 |
| Console | 0,4 | 6 | 8 |

Corrections :
- Pour les sections en Té dont le rapport largeur membrure / largeur âme est supérieur à 3 : multiplier par 0,8.
- Pour les poutres et dalles de portée > 7 m supportant des cloisons susceptibles d'être endommagées : multiplier par $7/l_{eff}$ ($l_{eff}$ en mètres).
- Pour les planchers-dalles dont la plus grande portée est > 8,5 m supportant des cloisons : multiplier par $8{,}5/l_{eff}$.

---

## 7.4.3 Vérification des flèches par le calcul

**(3)** Pour les éléments fissurés, il convient de les considérer comme se comportant d'une manière intermédiaire entre l'état non fissuré et l'état entièrement fissuré. Pour les éléments travaillant principalement en flexion :

$$\alpha = \zeta\, \alpha_{II} + (1 - \zeta)\, \alpha_{I} \tag{7.18}$$

où :
- $\alpha$ : paramètre de déformation (déformation unitaire, courbure, rotation, ou flèche)
- $\alpha_I$, $\alpha_{II}$ : valeurs du paramètre dans l'état non fissuré et dans l'état entièrement fissuré
- $\zeta$ : coefficient de distribution (tient compte de la participation du béton tendu) :

$$\zeta = 1 - \beta\, \left(\frac{\sigma_{sr}}{\sigma_s}\right)^2 \tag{7.19}$$

$\zeta = 0$ pour les sections non fissurées.

- $\beta = 1{,}0$ pour un chargement unique de courte durée
- $\beta = 0{,}5$ pour un chargement prolongé ou un grand nombre de cycles de chargement
- $\sigma_s$ : contrainte dans les armatures tendues, calculée en supposant la section fissurée
- $\sigma_{sr}$ : contrainte dans les armatures tendues, calculée sous les conditions de chargement provoquant la première fissure

> **Note :** $\sigma_{sr}/\sigma_s$ peut être remplacé par $M_{cr}/M$ en flexion ou par $N_{cr}/N$ en traction pure.

**(5)** Dans le cas de charges d'une durée telle que le béton subit un fluage, la déformation totale peut être calculée en utilisant le module d'élasticité effectif du béton :

$$E_{c,eff} = \frac{E_{cm}}{1 + \varphi(\infty, t_0)} \tag{7.20}$$

**(6)** Les courbures dues au retrait peuvent être évaluées au moyen de :

$$\frac{1}{r_{cs}} = \varepsilon_{cs}\, \alpha_e\, \frac{S}{I} \tag{7.21}$$

où :
- $1/r_{cs}$ : courbure due au retrait
- $\varepsilon_{cs}$ : déformation libre de retrait (voir 3.1.4)
- $S$ : moment statique de la section d'armatures par rapport à l'axe passant par le centre de gravité de la section
- $I$ : moment d'inertie de la section
- $\alpha_e = E_s / E_{c,eff}$

$S$ et $I$ doivent être calculés pour l'état non-fissuré et pour l'état entièrement fissuré, l'estimation de la courbure finale étant effectuée au moyen de l'Expression (7.18).

**(7)** La méthode la plus rigoureuse pour déterminer la flèche consiste à calculer la courbure dans un grand nombre de sections le long de l'élément, puis à calculer la flèche par intégration numérique. Dans la plupart des cas, on peut se contenter de deux calculs (état non fissuré, état entièrement fissuré), puis interpoler en utilisant l'Expression (7.18) pour obtenir la flèche.

---

Liens : [[EC2_index]] · [[EC2_6_elu.md]] · [[EC2_8_dispositions-armatures.md]] · [[_Knowledge — Index]] · [[CLAUDE]]
