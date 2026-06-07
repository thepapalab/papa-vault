---
parent: "[[00 - Index]]"
norm: "NBN EN 1992-2:2005"
---

## Annexe KK — Effets structurels induits par le comportement différé du béton

ANNEXE KK
(informative)
Effets structurels induits par le comportement différé du béton
KK.1 Introduction
La présente Annexe décrit les différentes méthodes d'évaluation des effets structurels induits
par le comportement différé du béton.
KK.2 Considérations générales
(101) Il convient, en règle générale, de prendre en compte les effets structurels induits par le
comportement différé du béton, tels que l'évolution des déformations et/ou la redistribution des
efforts, dans les conditions d'aptitude au service.
NOTE: Dans des cas particuliers (par exemple structures ou éléments de structure sensibles aux effets de
second ordre ou structures pour lesquelles les sollicitations ne peuvent pas se redistribuer), les effets différés
peuvent également avoir une influence aux ELU.
(102) Lorsque les contraintes de compression dans le béton sont inférieures à 0,45f (t) sous
ck
combinaison quasi-permanente, une analyse structurelle linéaire et un modèle viscoélastique
linéaire de vieillissement sont appropriés. Il convient de décrire le comportement différé du
béton par le coefficient ϕ(t,t ) ou la fonction de fluage J(t,t ) ou, alternativement, par la fonction
0 0
de relaxation R(t,t ).
Pour des contraintes de compression plus élevées, il convient de tenir compte des effets de la
non-linéarité du fluage.
(103) L'analyse permettant d'évaluer, en fonction du temps, la déformation et les sollicitations
des structures en béton armé ou précontraint en présence de liaisons rigides peut être
effectuée en supposant que ces structures sont homogènes, et la variabilité limitée des
propriétés du béton dans différentes zones de la structure peut être ignorée. Il convient de tenir
compte dans l'évaluation de toute variation des rigidité des liaisons au cours des phases de
construction ou pendant la durée d'utilisation de projet de la structure.
(104) Différents types d'analyse et leurs applications types sont présentés dans le
Tableau KK.101.

Tableau KK.101 : Type d'analyse
Type d'analyse Commentaire et application type
Méthode générale et méthode Il s'agit de méthodes générales applicables à toutes les
incrémentale structures. Ces méthodes sont particulièrement utiles pour
une vérification des phases intermédiaires de construction
des structures dont les propriétés varient avec la longueur
(construction par encorbellements, par exemple).
Méthodes basées sur les Méthodes applicables aux structures homogènes en
théorèmes de la viscoélasticité présence de liaisons rigides.
linéaire
Méthode du coefficient de Cette méthode est utile lorsqu'on ne doit vérifier que la
vieillissement répartition à long terme des efforts et des contraintes.
Méthode applicable aux ponts à section composite (poutres
préfabriquées et dalles de béton coulées en place).
Méthode du coefficient de Méthode applicable aux structures soumises à des
vieillissement simplifiée changements de conditions d'appui (construction travée par
travée ou par encorbellements, par exemple).
Toutes les méthodes décrites ci-dessus sont fondées sur les hypothèses suivantes :
- Le fluage et le retrait sont pris en compte indépendamment l'un de l'autre,
- Pour chaque type de béton dans une section donnée, les propriétés moyennes du
fluage et du retrait sont adoptées en ignorant les différences peu importantes entre
différents emplacements,
- Le principe de superposition est valable pour l'évaluation de la déformation totale due
aux actions appliquées à différents âges.
Les clauses suivantes décrivent succinctement les principaux détails de certaines de ces
méthodes.
KK.3 Méthode générale
(101) La présente méthode repose sur les hypothèses suivantes :
a) L'équation fondamentale relative à la déformation différée du béton est la suivante :
σ σ n  1 ϕ(t,t ) 
ε (t)= 0 +ϕ(t,t ) 0 +∑ + i ∆σ ( t ) +ε ( t,t ) (KK.101)
c E (t ) 0 E (28)  E ( t ) E (28)  i cs s c 0 c i=1 c i c 
Dans cette équation, le premier terme représente les déformations instantanées dues
à une contrainte appliquée à t . Le deuxième terme représente le fluage dû à cette
contrainte. Le troisième terme représente la somme des déformations instantanées et
de fluage dues à la variation des contraintes qui se produit à l'instant t. Le quatrième
i
terme représente la déformation due au retrait.
b) On suppose que les armatures de béton armé ont un comportement élastique sous
l'application de charges instantanées. Lorsque la contrainte à laquelle sont soumises
les armatures de précontrainte est supérieure à 0,5f il convient de prendre en
pmax,
compte la relaxation et un état de déformation variable correspondant à une historique
des déformations.
c) Il existe une adhérence parfaite entre le béton et les armatures adhérentes.

d)   Dans le cas d'éléments linéiques, les sections droites sont supposées rester planes
après la déformation.

e)  L'équilibre et la compatibilité sont assurés.

(102)  Le fluage du béton au droit de chaque section dépend de l'historique des contraintes.
Une méthode pas à pas tient compte de cet historique. L'analyse structurelle est effectuée à
des intervalles de temps successifs en maintenant des conditions d'équilibre et de compatibilité,
et en utilisant des propriétés des matériaux, effectives à l'instant considéré. La déformation est
calculée à des intervalles de temps successifs en utilisant la variation de la contrainte dans le
béton définie dans l'intervalle de temps précédent.

KK.4  Méthode incrémentale

(101)  À l'instant t où la contrainte appliquée est σ, et où la déformation de fluage est ε (t), la
cc
déformation potentielle de fluage ε ∞cc (t) (c'est-à-dire la déformation de  fluage qui serait obtenue
au temps t = ∞, si la contrainte appliquée à l'instant t était maintenue constante) et la vitesse de
fluage sont calculés théoriquement à partir de l'historique complet du chargement.

(102)  La déformation potentielle de fluage à l'instant t peut être évaluée grâce au principe de
superposition (pour les notations voir l’Expression (KK.101) et l'Annexe B de l'EN 1992-1-1) :

| dε (t) | dσϕ(∞,t) |     |     |     |     |     |     |     |           |
| ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --------- |
| ∞cc    | =        |     |     |     |     |     |     |     | (KK.102)  |
| dt     | dt E     |     |     |     |     |     |     |     |           |
c

(103)  À l'instant t, il est possible de définir un temps équivalent t  de manière à obtenir, sous
e
l'application d'une contrainte constante à partir de l'instant t , la même déformation de fluage et
e
la même déformation potentielle de fluage ; t  satisfait l'équation :
e

| ε ( t ) | ⋅β ( t,t ) =ε | ( t )   |     |     |     |     |     |     | (KK.103)  |
| ------- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --------- |
| ∞cc     | c e           | cc      |     |     |     |     |     |     |           |
La  vitesse  de  fluage  à  l'instant  t  peut  ainsi  être  calculée  en  utilisant  la  courbe  de  fluage
correspondant au temps équivalent :
| dε (t) | ∂β  | ( t,t | )   |     |     |     |     |     |     |
| ------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
( )
| cc  | =ε t | c e |     |     |     |     |     |     | (KK.104)  |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --------- |
∞cc
| dt  |     | ∂t  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

(104)  Lorsque |ε (t)|>| ε (t)| , c'est notamment le cas du retour de fluage, t  est défini par
|     | cc  | ∞cc |     |     |     |     |     | e   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rapport  à  la  phase  considérée  et  tient  compte  du  changement  de  signe  de  la  contrainte

appliquée. L'équation obtenue est la suivante :

|         |           | (     |       | )      | ( )      |       |     |     |           |
| ------- | --------- | ----- | ----- | ------ | -------- | ----- | --- | --- | --------- |
| ε (t)−ε | (t)=      | ε     | (t)−ε | (t) ⋅β | t,t      |       |     |     | (KK.105)  |
| ccMax   | cc        | ccMax | ∞cc   | c      | e        |       |     |     |           |
| d ( ε   | (t)−ε (t) | )     |       |        | ∂β ( t,t | )     |     |     |           |
|         |           | (     |       | )      |          |       |     |     |           |
| ccMax   | cc        | = ε   | (t)−ε | (t)    | ⋅ c      | e     |     |     | (KK.106)  |
|         |           | ccMax |       | ∞cc    |          |       |     |     |           |
|         | dt        |       |       |        | ∂t       |       |     |     |           |

où ε (t) est le dernier extremum de la déformation de fluage obtenue avant l'instant t.
ccMax

KK.5  Application des théorèmes de la viscoélasticité linéaire

(101)    Dans  les  structures  comportant  des  liaisons  rigides,  il  est  possible  d'évaluer  les
contraintes et les déformations initiales au moyen d'une analyse élastique de la structure dans
laquelle le module d'élasticité est supposé constant.

(102)  Les propriétés rhéologiques du béton sont totalement décrites par la fonction de fluage
| J(t,t ) et la fonction de relaxation R(t,t |     |     | ), où :  |     |     |     |     |
| ------------------------------------------ | --- | --- | -------- | --- | --- | --- | --- |
| 0                                          |     |     | 0        |     |     |     |     |
J(t,t )  représente la déformation totale dépendant des contraintes par unité de contrainte,
c'est-à-dire la réponse, en terme de déformation, à l'instant "t" résultant d'une
contrainte unité imposée maintenue constante appliquée à l'instant "t "
R(t,t )  représente la réponse, en terme de contrainte, à l'instant "t" résultant d'une
déformation unité imposée maintenue constante appliquée à l'instant "t "

(103)  Les contraintes élastiques ne sont pas modifiées par le fluage sous l'application d'actions
directes (charges d'exploitation). Les déformations D(t) peuvent être évaluées à l'instant "t" par
intégration  des  incréments  de  déformation  élastique  multipliés  par  le  coefficient  de  fluage
J(t,τ)⋅E  :
c
( )
| S(t)=S | t     |     |     |     |     |     | (KK.107)  |
| ------ | ----- | --- | --- | --- | --- | --- | --------- |
el 0
t
|        | ( )      | ( ) |     |     |     |     |           |
| ------ | -------- | --- | --- | --- | --- | --- | --------- |
| D(t)=E | ∫J t,τdD | τ   |     |     |     |     | (KK.108)  |
|        | C        | el  |     |     |     |     |           |

(104)    Les  déformations  élastiques  ne  sont  pas  modifiées  par  le  fluage  sous  l'application
d'actions indirectes (déformations imposées). Les contraintes peuvent être évaluées à l'instant
"t"  par  l'intégration  des  incréments  de  contrainte  élastique  multipliés  par  le  coefficient  de
| relaxation R(t,τ)/E |  :  |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
c

( )
| D(t)=D | t     |     |     |     |     |     | (KK.109)  |
| ------ | ----- | --- | --- | --- | --- | --- | --------- |
el 0
1 t
|       | ( )    | ( )    |     |     |     |     |           |
| ----- | ------ | ------ | --- | --- | --- | --- | --------- |
| S(t)= | ∫R t,τ | dS τ   |     |     |     |     | (KK.110)  |
el
E
C 0
(105) Dans une structure soumise à des charges d'exploitation constantes, dont la configuration
statique initiale (101) est modifiée en une configuration finale (102) par l'introduction de liaisons
supplémentaires  à  l'instant  t ≥t   (t   représentant  l'âge  de  la  structure  au  moment  du
|     |     | 1    | 0 0 |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- |
chargement),  la  répartition  des  contraintes  évolue  pour  t>t   et  s'approche  de  celle
    1
correspondant à l'application des charges dans la configuration statique finale :

| ( ) | (        | )        |     |     |     |     |           |
| --- | -------- | -------- | --- | --- | --- | --- | --------- |
| S t | =S +ξt,t | ,t ∆S    |     |     |     |     | (KK.111)  |
| 2   | el,1     | 0 1 el,1 |     |     |     |     |           |

  où :
S ( t )      est  la  répartition  des  contraintes  pour  t>t   dans  la  structure  avec  liaisons
    1
modifiées

S       est la répartition des contraintes élastiques dans la configuration statique initiale
el,1
∆S      est la correction à appliquer à la solution élastique S  afin de satisfaire à la
| el,1 |     |     |     |     | el,1 |     |     |
| ---- | --- | --- | --- | --- | ---- | --- | --- |
solution élastique relative à l'application des charges dans la configuration statique
finale
( )
ξt,t,t   est la fonction de redistribution
0 1
t
|     | ( )       | ∫R ( ) ( | )   |     |     |     |           |
| --- | --------- | -------- | --- | --- | --- | --- | --------- |
|     | ξt,t ,t = | t,τdJτ,t |     |     |     |     | (KK.112)  |
|     | 0 1       |          | 0   |     |     |     |           |
t
| avec   |   0 ≤ξt,t | ( ,t ) ≤1  |     |     |     |     |     |
| ------ | --------- | ---------- | --- | --- | --- | --- | --- |
0 1
( )
|     | (        | )   | R t,t   |     |     |     |           |
| --- | -------- | --- | ------- | --- | --- | --- | --------- |
|     |          | ,t+ | 0       |     |     |     |           |
| et  |     ξt,t | =1− |         |     |     |     | (KK.113)  |
|     |          | 0 0 | E ( t ) |     |     |     |           |
c 0

(106) Lorsque l'évolution entre la configuration statique initiale et la configuration finale
s'effectue au moyen de plusieurs modifications de liaison à des instants t ≥t différents, la
i 0
variation des contraintes dues au fluage, par l'effet de l'application d'un groupe ∆n de liaisons
j
additionnelles à l'instant t, est indépendante de l'historique des liaisons additionnelles
j
précédemment introduites aux instants t <t , et dépend uniquement de l'instant t d'application
i j j
des liaisons ∆n :
j
j
S = S +∑ξ ( t,t ,t ) ∆S (KK.114)
j+1 el,1 0 i el,i
i=1
KK.6 Méthode du coefficient de vieillissement
(101) La méthode du coefficient de vieillissement permet de calculer au temps infini les
variations des contraintes, déformations, sollicitations et flèches, dues au comportement différé
du béton et de l'acier de précontrainte, sans recourir à une analyse temporelle. Au niveau d'une
section, notamment, les variations de déformation longitudinale et de courbure dues au fluage,
au retrait et à la relaxation, peuvent être déterminés à l'aide d'une procédure relativement
simple.
(102) La déformation produite par les variations de contraintes avec le temps dans le béton
peut être considérée comme étant celle qui serait obtenue du fait d'une augmentation de la
contrainte appliquée et maintenue constante à partir d'un âge intermédiaire.
t
∫(1+ϕ (t,τ ))dσ ( τ ) = (1+χ (t,t ) ϕ (t,t )) ∆σ (KK.118)
0 0 t →t
τ=t
où χ est le coefficient de vieillissement. La valeur de χ peut être déterminée à tout
instant, au moyen d'un calcul pas à pas, ou peut être prise égale à 0,80 pour t = ∞.
La relaxation correspondant à une historique des déformations peut être évaluée, de manière
simplifiée au temps infini, comme étant la relaxation correspondant à une longueur constante,
multipliée par un coefficient de réduction de 0,80.
KK.7 Formules simplifiées
(101) Les sollicitations au temps t peuvent être calculées pour les structures soumises à des
∞
modifications des conditions d'appui (construction travée par travée, construction par
encorbellements, dénivellations d'appuis, etc.) en utilisant une méthode simplifiée. Dans ces
cas et en première approximation, la répartition des sollicitations au temps t peut être prise ∞
égale à :
ϕ(∞,t )−ϕ(t ,t )
S =S + ( S −S ) 0 c 0 (KK.119)
∞ 0 c 0 1+χϕ ( ∞,t )
c
où :
S représente les sollicitations en fin de construction
S représente les sollicitations obtenues si la structure était construite sur cintre c
t est l'âge du béton au moment de l'application de la charge 0
t est l'âge du béton au moment du changement des conditions d'appui
c
