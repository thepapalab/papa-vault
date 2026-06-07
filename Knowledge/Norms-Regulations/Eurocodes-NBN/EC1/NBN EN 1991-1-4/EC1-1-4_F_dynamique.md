---
title: "NBN EN 1991-1-4:2005 — Caractéristiques dynamiques des structures"
type: norm-extract
source: "NBN EN 1991-1-4:2005"
norm: EC1-1-4
section: "F"
chapter: "Caractéristiques dynamiques des structures"
tags: [EC1-1-4, eurocode-1, vent]
related: ["[[EC1-1-4_index]]", "[[EC1-1-4_Eb_galop-divergence-flottement]]", "[[EC1-1-4_Bibliographie]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

Annexe F
(informative)
Caractéristiques dynamiques des structures
F.1 Généralités
(1) Les méthodes de calcul recommandées dans la présente section présupposent que les structures présentent
un comportement élastique linéaire ainsi que des modes de vibration normaux classiques. Les propriétés
dynamiques structurales se caractérisent par conséquent par :
 les fréquences propres ;
 les déformées modales ;
 les masses équivalentes ;
 les décréments logarithmiques d'amortissement.
(2) Il convient d'évaluer, de manière théorique ou expérimentalement, les fréquences propres, déformées
modales, masses équivalentes et décréments logarithmiques d'amortissement, en appliquant les méthodes de la
dynamique des structures.
(3) Les propriétés dynamiques fondamentales peuvent être évaluées de manière approximative, au moyen
d'équations simplifiées analytiques, semi empiriques ou empiriques, pourvu qu’elles soient convenablement
justifiées : certaines de ces équations sont données de F.2 à F.5.
F.2 Fréquence fondamentale
(1) Dans le cas des structures en console comportant une masse à l'extrémité, une expression simplifiée
permettant de calculer la fréquence fondamentale de flexion n est donnée par l'expression (F.1). 1
1 g
n = ⋅ (F.1)
1 2⋅π x
1
où
g est l'accélération due à la pesanteur = 9,81 m/s2
x est le déplacement maximal dû au poids propre appliqué dans la direction de vibration, en [m]
1
(2) La fréquence fondamentale de flexion n de bâtiments à plusieurs niveaux ayant une hauteur de plus de 50 m,
1
peut être estimée à l'aide de l'expression (F.2).
46
n = ⋅[Hz] (F.2)
1 h
où
h est la hauteur de la construction, en [m]
La même expression peut donner des indications utiles pour les bâtiments à un seul niveau et les tours.
140


EN 1991-1-4:2005 (F)
(3)  La fréquence fondamentale de flexion n 1  des cheminées, peut être estimée à l'aide de l'expression (F.3).
| ε ⋅b | W          |     |        |
| ---- | ---------- | --- | ------ |
| 1    | s          |     |        |
| n =  | ⋅    [Hz]  |     | (F.3)  |
| 1 h2 | W          |     |        |
t
eff
avec
h
2
| h =h + |     |     | (F.4)  |
| ------ | --- | --- | ------ |
| eff 1  | 3   |     |        |
où
b  est le diamètre en tête de la cheminée [m]
eff 1 2
W s   est le poids des éléments structuraux contribuant à la rigidité de la cheminée
W  est le poids total de la cheminée
t
ε  est égal à 1 000 pour les cheminées en acier, et à 700 pour les cheminées en béton ou en maçonnerie
1

| NOTE  h |  = h /3, voir F.4 (2).  |     |     |
| ------- | ----------------------- | --- | --- |
3 1
Figure F.1 — Paramètres géométriques des cheminées
(4)  La fréquence fondamentale d'ovalisation n  d'une longue coque cylindrique sans anneaux de rigidité peut
1,0
être calculée à l'aide de l'expression (F.5).
t3⋅E
| n =0,492⋅ |              |     | (F.5)  |
| --------- | ------------ | --- | ------ |
| 1,0       | µ ⋅(1−ν2)⋅b4 |     |        |
s
où
est le module de Young en [N/m2]
E
t  est l'épaisseur de la coque en [m]
ν  est le coefficient de Poisson
µ   est la masse de la coque par unité d’aire en [kg/m2]
s
141

EN 1991-1-4:2005 (F)
b  est le diamètre de la coque en [m]
L'expression (F.5) donne la fréquence propre la plus basse de la coque. Les anneaux de rigidité augmentent n .
0
La fréquence fondamentale de flexion verticale n
(5)  1,B  d'un pont à poutres à âme pleine ou à poutres-caissons
peut être calculée de manière approchée à partir de l'expression (F.6).
K2
EL
| n = | ⋅ b   |     | (F.6)  |
| --- | ----- | --- | ------ |
1,B 2⋅π⋅L2
m
où
L  est la longueur de la travée principale en [m]
I   est le moment d'inertie d’aires de la section transversale, pour la flexion verticale, à mi-travée en [m4]
b
m  est la masse par unité de longueur de la section transversale complète à mi-travée (poids propre et
poids propres ajoutés) en [kg/m]
K  est un coefficient adimensionnel dépendant de la disposition des travées définie ci-dessous
a)  Pour les ponts à une seule travée :
| K = π   | si la travée repose sur deux appuis simples ; ou  |     |     |
| ------- | ------------------------------------------------- | --- | --- |
K = 3,9  si elle est encastrée sur un appui et libre sur le second ; ou
| K = 4,7  | si elle est encastrée aux deux appuis ;  |     |     |
| -------- | ---------------------------------------- | --- | --- |
b)  pour les ponts à deux travées continues :
K  est obtenu à partir de la Figure F.2, en utilisant la courbe applicable aux ponts à deux travées ;
|     | où  |     |     |
| --- | --- | --- | --- |

| L   | est la longueur de la travée latérale et L > L | ;   |     |
| --- | ---------------------------------------------- | --- | --- |
| 1   |                                                | 1   |     |
c)  pour les ponts à trois travées continues :
K  est obtenu à partir de la Figure F.2, en utilisant la courbe appropriée applicable aux ponts à
| trois   | travées ; où                                         |     |     |
| ------- | ---------------------------------------------------- | --- | --- |
| L       | est la longueur de la plus longue travée latérale ;  |     |     |
1
| L   | est la longueur de l'autre travée latérale et L > L |  > L  ;  |     |
| --- | --------------------------------------------------- | -------- | --- |
| 2   |                                                     | 1 2      |     |
Cela s'applique également aux ponts à trois travées avec une travée principale en poutre cantilever.
Si L  > L, alors K peut être obtenu à partir de la courbe applicable aux ponts à deux travées, en ne tenant pas
1
compte de la travée latérale la plus courte et en considérant la travée latérale la plus grande comme la travée
principale d'un pont à deux travées équivalent.
d)  pour les ponts à quatre travées continues symétriques (à savoir les ponts symétriques par rapport au support
central) :
142

EN 1991-1-4:2005 (F)
K peut être obtenu à partir de la courbe applicable aux ponts à deux travées décrite à la Figure F.2, en
considérant chaque moitié du pont comme un pont à deux travées équivalent.
e) pour les ponts à quatre travées continues non symétriques et les ponts comprenant plus de quatre travées
continues :
K peut être obtenu à partir de la Figure F.2 en utilisant la courbe appropriée applicable aux ponts à
trois travées, en considérant la travée principale comme la plus grande travée intérieure.
EI
NOTE 1 Si la valeur de b au niveau des appuis est supérieure à deux fois la valeur à mi-travée, ou est
m
inférieure à 80 % de la valeur à mi-travée, il convient alors de ne pas utiliser l'expression (F.6) sauf lorsque des valeurs
très approchées sont suffisantes.
NOTE 2 Il convient d'utiliser un ensemble cohérent de variables (sur le plan dimensionnel) pour obtenir n en
1,B
cycles par seconde.
(6) La fréquence fondamentale de torsion des ponts à poutres à âme pleine est égale à la fréquence
fondamentale de flexion calculée à partir de l'expression (F.6), à condition que la rigidité en flexion moyenne
longitudinale par unité de largeur ne soit pas inférieure à 100 fois la rigidité en flexion moyenne transversale par
unité de longueur.
(7) La fréquence fondamentale de torsion d'un pont à poutres caissons peut être calculée de manière approchée
à partir de l'expression (F.7).
n =n ⋅ P ⋅(P +P ) (F.7)
1,T 1,B 1 2 3
avec
m⋅b2
P = (F.8)
1 I
p
∑ r2⋅I
j j P = (F.9)
2 b2⋅I
p
L2⋅∑
J
j
P = (F.10)
3 2⋅K ⋅b2⋅I ⋅(1+ν)
2 p
où
n est la fréquence fondamentale de flexion en Hz
1,B
b est la largeur totale du pont
m est la masse par unité de longueur définie en F.2 (5)
ν est le coefficient de Poisson du matériau des poutres
r est la distance entre l'axe du caisson élémentaire j et l'axe du pont
j
I est le moment d’inertie de masse par unité de longueur du caisson élémentaire j pour une flexion
j
verticale à mi-travée, y compris une largeur effective associée du tablier
143


EN 1991-1-4:2005 (F)
I est le moment d’inertie de masse par unité de longueur de la section transversale à mi-travée. Il est
p
décrit par l'expression (F.11)
I = m d ⋅b2 +∑ (I +m ⋅r2) (F.11)
p pj j j
12
où
m est la masse par unité de longueur du seul tablier, à mi-travée
d
I est le moment d'inertie de masse du caisson élémentaire j à mi-travée
pj
m est la masse par unité de longueur du seul caisson élémentaire j à mi-travée, sans partie de tablier
j
associée
J est la constante de torsion du caisson élémentaire j à mi-travée. Elle est décrite par l'expression (F.12)
j
4⋅A2
J = j (F.12)
j ds
∫
t
où
A est l’aire de la surface fermée délimitée par le caisson à mi-travée
j
ds
∫ est l'intégrale sur le périmètre du caisson du rapport longueur/épaisseur pour chaque partie de paroi
t
de caisson à mi-travée
NOTE Une perte sensible de précision peut se produire si l'expression proposée (F.12) est appliquée aux ponts à
caissons multiples dont le rapport de forme en plan (= portée / largeur) est supérieur à 6.
144


EN 1991-1-4:2005 (F)
Figure F.2 — Coefficient K utilisé pour le calcul de la fréquence fondamentale de flexion
145


EN 1991-1-4:2005 (F)
F.3 Déformée du mode fondamental
(1) Le mode fondamental de flexion Φ(z) des bâtiments, tours et cheminées en console à partir du sol peut être
1
estimé à l'aide de l'expression (F.13), voir Figure F.3.
ς
z
Φ 1 (z)= h   (F.13)
où
ζ = 0,6 pour les constructions à ossature élancée et murs non porteurs ou bardage
ζ = 1,0 pour les bâtiments à noyau central et poteaux périphériques ou poteaux plus importants et
contreventements
ζ = 1,5 pour les bâtiments élancés en encorbellement et les bâtiments supportés par noyau central en
béton armé
ζ = 2,0 pour les tours et les cheminées
ζ = 2,5 pour les tours métalliques à treillis
Figure F.3 — Déformée du mode fondamental de flexion pour les bâtiments, tours et
cheminées en console à partir du sol
(2) La déformée du mode fondamental vertical de flexion Φ(s) des ponts peut être estimée comme indiqué dans
1
le Tableau F.1.
146


EN 1991-1-4:2005 (F)
Tableau F.1 — Déformée du mode fondamental vertical de flexion pour les structures et
les éléments structuraux sur appuis simples ou encastrés
Plan Déformée modale Φ(s)
1
 s
sinπ⋅ 
 
1   s
⋅1−cos2⋅π⋅ 
2   
F.4 Masse équivalente
(1) La masse équivalente par unité de longueur m du mode fondamental est donnée par l'expression (F.14).
e

∫m(s)⋅Φ2(s)ds
1
m = 0 (F.14) e 
∫Φ2(s)ds
1
0
où
m est la masse par unité de longueur
 est la hauteur ou la portée de la construction ou de l'élément structural
i = 1 est le numéro du mode
(2) Pour les structures en console avec une répartition de masse variable, m peut être calculé de manière
e
approchée par la valeur moyenne de m sur le tiers supérieur de la construction h (voir figure F.1).
3
(3) Pour les structures appuyées aux deux extrémités de la portée  avec une répartition variable de la masse par
unité de longueur, m peut être calculé de manière approchée par la valeur moyenne de m sur une longueur de /3
e
centrée sur le point de la structure où la valeur Φ(s) est maximale (voir Tableau F.1).
147


EN 1991-1-4:2005 (F)
F.5 Décrément logarithmique d'amortissement
(1) Le décrément logarithmique d'amortissement δ pour le mode fondamental de flexion peut être estimé par
l'expression (F.15) suivante :
δ = δ + δ + δ (F.15)
s a d
où
δ est le décrément logarithmique d'amortissement structural
s
δ est le décrément logarithmique d'amortissement aérodynamique pour le mode fondamental
a
δ est le décrément logarithmique d'amortissement dû à des dispositifs spéciaux (amortisseurs dynamiques
d
accordés, amortisseurs à mouvement de liquide, etc.)
(2) Des valeurs approchées du décrément logarithmique d'amortissement structural δ sont données dans le s
Tableau F.2.
(3) Le décrément logarithmique d'amortissement aérodynamique δ pour le mode fondamental de flexion dans le
a
sens du vent peut être estimé par l'expression (F.16).
c ⋅ρ⋅v (z )
δ = f m s (F.16)
a 2⋅n ⋅µ
1 e
où
c est le coefficient de force applicable à l'action du vent dans la direction de ce dernier, indiquée en
f
Section 7
µ est la masse équivalente par unité d’aire de la construction pour les surfaces rectangulaires, donnée par
e
l'expression (F.17)
h b
∫∫µ(y,z)⋅Φ2(y,z)dydz
1
µ = 00 (F.17)
e h b
∫∫Φ2(y,z)dydz
1
00
où
µ(y,z) est la masse par unité d’aire de la construction
Φ(y,z) est la déformée modale
1
La masse par unité d’aire de la construction au point où l'amplitude de la déformée modale est la plus grande, est
généralement une valeur approchée correcte de µ.
e
148


EN 1991-1-4:2005 (F)
Dans la plupart des cas, les déformations modales Φ(y,z) sont constantes pour chaque hauteur z (c’est-à-dire
(4)
que Φ(y,z) est indépendant de y) et le décrément logarithmique d'amortissement aérodynamique δ pour les
a
vibrations dans le sens du vent, peut être estimé par l'expression (F.18) en lieu et place de l'expression (F.16).
| c ⋅ρ⋅b⋅v | (z )  |     |     |         |
| -------- | ----- | --- | --- | ------- |
| δ = f    | m s   |     |     | (F.18)  |
a
| 2⋅n | ⋅m  |     |     |     |
| --- | --- | --- | --- | --- |
1 e
(5)  Lorsque des dispositifs dissipatifs spéciaux sont ajoutés à la construction, il convient de calculer δ au moyen
d
de méthodes théoriques ou expérimentales appropriées.
Tableau F.2 — Valeurs approchées du décrément logarithmique d'amortissement structural
du mode fondamental, δ
s
amortissement
Type de construction
structural δ
| bâtiments en béton armé           |     |     |     | 0,10  |
| --------------------------------- | --- | --- | --- | ----- |
| bâtiments en acier                |     |     |     | 0,05  |
| structures mixtes béton + acier   |     |     |     | 0,08  |
| tours et cheminées en béton armé  |     |     |     | 0,03  |
cheminées en acier soudé non revêtues sans isolation thermique externe  0,012
cheminées en acier soudé non revêtues avec isolation thermique externe  0,020
h/b < 18
0,020
cheminée en acier avec un conduit et isolation thermique
20 ≤ h/b < 24  0,040
externe a
h/b ≥ 26
0,014
h/b < 18  0,020
| cheminée  | en  acier  avec  | plusieurs  conduits  | et  isolation  |     |
| --------- | ---------------- | -------------------- | -------------- | --- |
20 ≤ h/b < 24
| thermique externe a  |     |     |     | 0,040  |
| -------------------- | --- | --- | --- | ------ |
h/b ≥ 26  0,025
| cheminée en acier avec conduit en brique intérieur  |     |         |     | 0,070  |
| --------------------------------------------------- | --- | ------- | --- | ------ |
| cheminée en acier avec gunite à l’intérieur         |     |         |     | 0,030  |
| cheminées couplées sans conduit                     |     |         |     | 0,015  |
| cheminée en acier haubanée sans conduit             |     |         |     | 0,04   |
| ponts en acier                                      |     | soudés  |     | 0,02   |
+ tours à treillis en acier  assemblés par boulons à haute résistance  0,03
|               |     | assemblés par boulons ordinaires  |     | 0,05  |
| ------------- | --- | --------------------------------- | --- | ----- |
| ponts mixtes  |     |                                   |     | 0,04  |
|               |     | précontraint sans fissures        |     | 0,04  |
ponts en béton
|     |     | avec fissures  |     | 0,10  |
| --- | --- | -------------- | --- | ----- |
« à suivre »
149

EN 1991-1-4:2005 (F)
Tableau F.2 (fin)
amortissement
Type de construction structural δ
s
ponts en bois 0,06 - 0,12
ponts en alliages d'aluminium 0,02
ponts en résine renforcée de fibres ou verre 0,04 - 0,08
fils parallèles 0,006
câbles
fils en torons 0,020
NOTE 1 Les valeurs relatives aux composites de bois et de plastique sont des valeurs données
uniquement à titre indicatif. Dans les cas où il est montré que les effets aérodynamiques sont significatifs
dans le calcul, des valeurs d'une plus grande précision sont nécessaires et peuvent être obtenues en
consultant un spécialiste (avec l’accord, le cas échéant, de l'autorité compétente).
NOTE 2 Dans le cas de ponts à câbles, les valeurs données dans le Tableau F.2 doivent être multipliées
par le coefficient 0,75.
a L'interpolation linéaire peut être utilisée pour les valeurs intermédiaires de h/b.
150


EN 1991-1-4:2005 (F)

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_Eb_galop-divergence-flottement]] · [[EC1-1-4_Bibliographie]] · [[_Knowledge — Index]] · [[CLAUDE]]
