---
parent: "[[00 - Index]]"
norm: "NBN EN 1992-2:2005"
---

## Annexe B — Déformations dues au fluage et au retrait

ANNEXE B
(informative)
Déformations dues au fluage et au retrait
Les clauses suivantes de l'EN 1992-1-1 s'appliquent pour un béton courant, à l’exception des
sections particulièrement épaisses (voir ci-dessous).
B.1 (1) B.1 (2) B.1 (3) B.2 (1)
La clause B.103 s’applique spécifiquement au béton à haute performance, composé de ciment
de classe R, de classe de résistance supérieure à C50/60, avec ou sans fumées de silice. En
général, les méthodes données en B.103 sont préférables à celles de l’EN 1992-1-1 pour les
bétons cités ci-dessus et pour les éléments épais, pour lesquels la cinétique du fluage propre et
du fluage de dessication sont complètement différents. Il convient de noter que les
recommandations de la présente Annexe ont été vérifiées par des essais et des mesures in
situ.
NOTE: Pour une documentation de référence, on peut se reporter à:
• LE ROY R., DE LARRARD F., PONS G. (1996) The AFREM code type model for creep and
shrinkage of high performance concrete.
• TOUTLEMONDE F., DE LARRARD F., BRAZILLIER D. (2002) Structural application of
HPC: a survey of recent research in France.
• LE ROY R., CUSSAC J.M., MARTIN O. (1999) Structures sensitive to creep :from laboratory
experimentation to structural design - The case of the Avignon high-speed rail viaduct.
B.100 Généralités
(101) La présente Annexe peut être utilisée pour calculer le fluage et le retrait, y compris leur
évolution en fonction du temps. Les valeurs expérimentales types peuvent toutefois présenter
une dispersion de ± 30 % par rapport aux valeurs de fluage et de retrait estimées
conformément à la présente Annexe. Lorsque la sensibilité de la structure au fluage et/ou retrait
requiert une plus grande précision, il convient d'effectuer une évaluation expérimentale de ces
effets et de l'évolution des déformations différées en fonction du temps. La clause B.104
comprend les recommandations relatives à la détermination expérimentale des coefficients de
fluage et de retrait.
(102) La clause B.103 définit une méthode alternative pour l'évaluation du fluage et du retrait
dans le cas du béton à haute résistance (f > 50 MPa) (BHP). Cette méthode alternative tient
ck
compte de l'effet de l'adjonction de fumée de silice et améliore de manière significative la
précision de la prévision.
(103) Par ailleurs, les expressions relatives au fluage définies dans les clauses B.1 et B.103
sont valables lorsque la valeur moyenne de la résistance du béton, mesurée sur cylindre, au
moment du chargement f (t ) est supérieure à 0,6 f (f (t ) > 0,6 f ).
cm 0 cm cm 0 cm
Lorsque le chargement du béton doit être effectué plus tôt, avec un développement significatif
de la résistance au début de la phase de chargement, il convient de déterminer spécifiquement
le coefficient de fluage. Cette détermination est à fonder sur une approche expérimentale, et
l'expression mathématique propre au fluage est à déterminer sur la base des recommandations
indiquées en B.104.

(104) Les formules et les déterminations expérimentales du fluage et du retrait sont fondées
sur des données collectées sur des périodes limitées. L'extrapolation de tels résultats pour des
évaluations à très long terme (par exemple un siècle) conduit à l'introduction d'erreurs
supplémentaires associées aux expressions mathématiques utilisées pour l'extrapolation.
Lorsque la surestimation des déformations différées entraîne une augmentation de la sécurité,
et lorsque le projet le justifie, il convient de multiplier le fluage et le retrait prévus sur la base des
formules ou des déterminations expérimentales par un coefficient partiel, tel qu'indiqué en
B.105.
B.103 Béton à haute résistance
(101) Dans le cas du béton à haute résistance (BHP), à savoir pour les classes de résistance
du béton supérieures ou égales à C55/67, il convient d'utiliser le modèle décrit dans la présente
clause afin d'obtenir des données expérimentales d'une plus grande cohérence, lorsque les
informations nécessaires à l'utilisation du modèle sont disponibles. Dans le cas du BHP sans
fumée de silice, le fluage est généralement plus important que ce que prévoient les expressions
moyennes de B.1. Lorsque la proportion de granulats est inférieure à 67 %, ce qui est fréquent
pour le béton auto-compactant, il convient de ne pas utiliser les expressions proposées dans
cette clause sans verification.
(102) Le modèle différencie les déformations observées sur le béton protégé de la dessiccation
des déformations supplémentaires dues au séchage. La présente clause donne deux
expressions pour le retrait et deux expressions pour le fluage. Les composantes des
déformations différées sont les suivantes :
- retrait endogène,
- retrait de dessiccation,
- fluage propre,
- fluage de dessiccation.
Cette classification différencie les phénomènes régis par des mécanismes physiques différents.
Le retrait endogène est associé au processus d'hydratation tandis que le retrait de dessiccation,
provoqué par des échanges hydriques, est associé à l'environnement de la structure.
(103) Des formules spécifiques sont données pour le béton avec fumée de silice (BHPFS).
Pour les besoins de la présente clause, le BHPFS est considéré comme du béton contenant
une quantité de fumée de silice équivalente à au moins 5 % de la masse de ciment.
B.103.1 Retrait endogène
(101) Le degré d'hydratation régit la cinétique du retrait endogène. Par conséquent, le degré de
( ) développement de la résistance régule l'évolution du phénomène. Le rapport f t /f ,
cm ck
représentant la maturité du béton au jeune âge, est choisi comme variable principale avant
28 jours. Le retrait semble négligeable pour une maturité inférieure à 0,1. Pour des bétons de
plus de 28 jours, le temps est la variable qui régit l'évolution du retrait endogène.
Le modèle d'évaluation du retrait endogène est le suivant :
- pour t < 28 jours,
( ) f t
• si cm <0,1 ε (t)=0 (B.113)
f ca
ck

|     |     |       | f   | ( t ) |     |     |     |         |      | f (t)         |    |            |     |
| --- | --- | ----- | --- | ----- | --- | --- | --- | ------- | ----- | ------------- | --- | ---------- | --- |
|     |     |       |     |       |     |     | (   | ) (     | )2,2 |               |     |            |     |
|     |     | • si  | cm  | ≥0,1  |     |     | ε t | = f −20 |       | cm −0,210−6  |     |   (B.114)  |     |
|     |     |       |     |       |     |     | ca  | ck      |      |               |    |            |     |
|     |     |       | f   |       |     |     |     |         |       | f             |     |            |     |
|     |     |       |     | ck    |     |     |     |         |      | ck            |    |            |     |

où ε  est le retrait endogène se produisant entre la prise et l'instant t. Lorsque cette résistance
ca
f (t) n'est pas connue, elle peut être évaluée conformément au 3.1.2 (6) de l'EN 1992-1-1.
cm

- pour t ≥ 28 jours,
|     |          |     |      | [                 |     |     |     | ] 10−6  |     |     |     |     |          |
| --- | -------- | --- | ---- | ----------------- | --- | --- | --- | ------- | --- | --- | --- | --- | -------- |
|     | ε (t)=(f |     | −20) | 2,8−1,1exp(−t/96) |     |     |     |         |     |     |     |     | (B.115)  |
|     | ca       |     | ck   |                   |     |     |     |         |     |     |     |     |          |

Par conséquent, conformément à ce modèle, 97 % du retrait endogène total se sont produits au
bout de 3 mois.

B.103.2  Retrait de dessiccation

Les formules du B.103.2 s’appliquent pour des valeurs de RH inférieures ou égales à 80%.

(101)  L'expression relative au retrait de dessiccation est la suivante :

|     |        | K(f | ) [ | 72exp(−0,046f |     |        | )+75−RH | ](  | t −t ) 10−6 |     |     |     |          |
| --- | ------ | --- | --- | ------------- | --- | ------ | ------- | --- | ----------- | --- | --- | --- | -------- |
|     | ε (t)= |     | ck  |               |     | ck     |         |     | s           |     |     |     | (B.116)  |
|     | cd     |     |     |               | (t  | −t )+β | h       | 2   |             |     |     |     |          |
|     |        |     |     |               |     | s      | cd      | 0   |             |     |     |     |          |

| où :    |     | K(f | )=18       |     |     |     | si f | ≤55 MPa   |     |     |     |     |     |
| ------- | --- | --- | ---------- | --- | --- | --- | ---- | --------- | --- | --- | --- | --- | --- |
|         |     |     | ck         |     |     |     |      | ck        |     |     |     |     |     |
|         |     | K(f | )=30−0,21f |     |     |     | si f | >55 MPa.  |     |     |     |     |     |
|         |     |     | ck         |     | ck  |     |      | ck        |     |     |     |     |     |

|     |     |     | 0,007 |     |     | pour le béton avec fumée de silice  |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | β   | =     |     |     |                                     |     |     |     |     |     |     |     |
cd  0,021
pour le béton sans fumée de silice

B.103.3  Fluage

Les formules du B.103.3 s’appliquent pour des valeurs de RH inférieures ou égales à 80%.

|     |     |     |     |     |     |     |     | ( ) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(101)  La déformation différée de fluage, ε t,t , c'est-à-dire la somme du fluage propre et du
|     |     |     |     |     |     |     |     | cc 0 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
fluage de dessiccation, est dépendante de la contrainte et peut être calculée par l'expression
suivante :

( )
σt
 ε ( t,t ) = 0 [ ϕ ( t,t ) +ϕ ( t,t )]   (B.117)
|     | cc  | 0   | E   | b   | 0   | d   | 0   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
c

B.103.4  Fluage propre

(101)  Le coefficient de fluage propre, au temps infini, du béton avec fumée de silice s'avère
|     |     |     |     |     |     |     |     | ( ) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dépendre de la résistance au chargement f t . En outre, plus le béton est jeune au moment
cm 0
du chargement, plus la déformation se produit rapidement. Cette tendance n'est toutefois pas
observée pour le béton sans fumée de silice. Pour ce matériau, on fait l'hypothèse que le
coefficient de fluage demeure constant à une valeur moyenne de 1,4. Le terme cinétique est
( )
par conséquent fonction de la maturité, exprimée par la grandeur f t /f . L'équation est la
cm ck
suivante :

|           |     | t −t |     |          |
| --------- | --- | ---- | --- | -------- |
| ϕ ( t,t ) | =ϕ  | 0 ]  |     | (B.118)  |
[
| b 0 | b0 t −t | +β  |     |     |
| --- | ------- | --- | --- | --- |
0 bc
où :

|    | 3,6       |                                     |       |             |
| --- | --------- | ----------------------------------- | ----- | ----------- |
|    |           | pour le béton avec fumée de silice  |       |             |
| f  | ( t )0,37 |                                     |       |             |
|     |           |                                     |       |     (B.119) |
| ϕ = | cm 0      |                                     |       |             |
b0 

pour le béton sans fumée de silice
|    | 1,4 |     |     |     |
| --- | --- | --- | --- | --- |

et

|             |     | ( )                                    |       |            |
| ------------ | --- | --------------------------------------- | ----- | ---------- |
|              |    | f t pour le béton avec fumée de silice  |       |            |
| 0,37exp2,8 |     | cm 0                                   |       |            |
|              |    |                                        |       |            |
|             |     | f                                       |       |            |
|              |    |                                        |       |    (B.120) |
ck
| β =  |     |                                     |     |     |
| ----- | --- | ----------------------------------- | --- | --- |
| bc   |     | pour le béton sans fumée de silice  |     |     |
|       |    | f ( t )                            |     |     |

|     | 0,4exp3,1 | cm 0  |     |     |
| --- | ---------- | ------ | --- | --- |
|    |           |       |     |     |
f
|    |    | ck  |     |     |
| --- | --- | ---- | --- | --- |

B.103.5  Fluage de dessiccation

Les formules du B.103.5 s’appliquent pour des valeurs de RH inférieures ou égales à 80%.

(101)  Le fluage de dessiccation, qui est très faible pour le béton avec fumée de silice, est
évalué par référence au retrait de séchage se produisant au cours de la même période. Le
coefficient de fluage de dessiccation peut être exprimé par l'équation suivante :

|           | [       | ]      |     |          |
| --------- | ------- | ------ | --- | -------- |
| ϕ(t,t )=ϕ | ε (t)−ε | (t )   |     | (B.121)  |
| d 0       | d0 cd   | cd 0   |     |          |

où :

| 1000 |     | pour le béton avec fumée de silice  |     |     |
| ----- | --- | ----------------------------------- | --- | --- |
| ϕ =  |     |                                     |     |     |
d0 
3200
pour le béton sans fumée de silice

B.104  Procédure d'identification expérimentale

(101)  Afin d'évaluer les déformations différées avec une plus grande précision, il peut être

nécessaire d'identifier les paramètres inclus dans les modèles décrivant le fluage et le retrait
sur la base de mesures expérimentales. La procédure suivante, fondée sur la détermination
expérimentale des coefficients modifiant les formules de B.103, peut être utilisée.

(102) Les données expérimentales peuvent être obtenues à partir d'essais de fluage et de
retrait  appropriés,  tous  deux  effectués  dans  des  conditions  endogènes  et  de  séchage.  Il
convient de réaliser les mesures dans des conditions contrôlées et de les consigner pendant
une durée minimale de 6 mois.

B.104.1  Retrait endogène

(101)  Le modèle de retrait endogène doit être scindé en deux parties :

-  pour t < 28 jours,

( )
|     |       | f   | t     |     |     |      |        |      | f (t)          |    |     |          |
| --- | ----- | --- | ----- | --- | --- | ---- | ------ | ----- | -------------- | --- | --- | -------- |
|     |       | cm  |       |     |     | ( )  | (      | )2,2 | cm −0,210−6   |     |     |          |
|     | • si  |     | ≥0,1  |     | ε   | t =β | f      | −20   |                |     |     | (B.122)  |
|     |       | f   |       |     | ca  |      | ca1 ck |      | f              |    |     |          |
|     |       |     |       |     |     |      |        |      |                |    |     |          |
|     |       |     | ck    |     |     |      |        |       | ck             |     |     |          |

Le  paramètre β  doit  être  choisi  afin  de  réduire  au  minimum  la  somme  des  carrés  des
ca1
différences entre l'estimation du modèle et les résultats expérimentaux obtenus entre le début
des mesures et à 28 jours.

-  pour t ≥ 28 jours,
|     |     |       |         | [   |     |        |     | ]       |     |     |     |          |
| --- | --- | ----- | ------- | --- | --- | ------ | --- | ------- | --- | --- | --- | -------- |
|     | ε   | (t)=β | (f −20) | β   | −β  | exp(−t | /β  | ) 10−6  |     |     |     | (B.123)  |
|     | ca  |       | ca1 ck  | ca2 | ca3 |        | ca4 |         |     |     |     |          |

Les autres paramètres β ,β ,β  sont alors choisis en utilisant la même méthode.
|     |     |     |     | ca2 ca3 | ca4 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |

B.104.2  Retrait de dessiccation

Les formules du B.104.2 s’appliquent pour des valeurs de RH inférieures ou égales à 80%.

(101)  L’expression pour le retrait de dessication est la suivante :

|     |     |       | [     |               |       |         |     | ](   | )    |     |     |          |
| --- | --- | ----- | ----- | ------------- | ----- | ------- | --- | ---- | ---- | --- | --- | -------- |
|     |     |       | K(f ) | 72exp(−0,046f |       | )+75−RH |     | t −t | 10−6 |     |     |          |
|     |     |       | ck    |               |       | ck      |     | s    |      |     |     |          |
|     | ε   | (t)=β |       |               |       |         |     |      |      |     |     | (B.124)  |
|     | cd  |       | cd1   |               |       |         |     |      |      |     |     |          |
|     |     |       |       |               | (t −t | )+β     | h 2 |      |      |     |     |          |
|     |     |       |       |               |       | s cd2   | 0   |      |      |     |     |          |
Les paramètres β , β  doivent être choisis afin de réduire au minimum la somme des carrés
|     |     |     | cd1 cd2 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
des différences entre l'estimation du modèle et les résultats expérimentaux.

B.104.3  Fluage propre

(101)    Deux  paramètres  doivent  être  identifiés,  à  savoir  un  paramètre  global β  qui  est
cd1
appliqué à l'ensemble de l'expression relative au fluage propre :
t −t
|     | ϕ   | ( t,t ) | =β ϕ |     | 0 ]  |     |     |     |     |     |     | (B.125)  |
| --- | --- | ------- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | -------- |
[
|     | b   | 0   | cd1 b0 |         |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |        | t −t +β |     |     |     |     |     |     |     |     |
0 bc

| et le paramètre β |     |     |  inclus dans β |     |  :  |     |     |     |     |     |     |     |
| ----------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                   |     |     | bc2            |     | bc  |     |     |     |     |     |     |     |

|     |     |    |    | f ( t | )  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
 β pour le béton avec fumée de silice
|     |     |     | exp2,8 | cm 0 |    |     |     |     |     |     |     |            |
| --- | --- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | ---------- |
|     |     |     | bc2    |      |    |     |     |     |     |     |     |            |
|     |     |    |        | f    |    |     |     |     |     |     |     |    (B.126) |
ck

|     | β   | =   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bc 
( ) pour le béton sans fumée de silice
|     |     |     |        | f t  |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |    | exp3,1 | cm 0 |    |     |     |     |     |     |     |     |
β
|     |     |    | bc2  | f   |    |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |    |      |     |    |     |     |     |     |     |     |     |
ck

Ces deux paramètres doivent être déterminés en réduisant au minimum la somme des carrés
des différences entre l'estimation du modèle et les résultats expérimentaux.

B.104.4  Fluage de dessiccation

Les formules du B.104.4 s’appliquent pour des valeurs de RH inférieures ou égales à 80%.

(101)  Seul le paramètre global ϕ  doit être identifié :
d0

| ϕ(t,t )=ϕ | [ ε (t)−ε | (t ) ]   |     |     |     | (B.127)  |
| --------- | --------- | -------- | --- | --- | --- | -------- |
| d 0       | d0 cd     | cd 0     |     |     |     |          |

Ce paramètre doit être déterminé en rendant minimale la somme des carrés des différences
entre l'estimation du modèle et les résultats expérimentaux.

B.105  Estimation des déformations différées à long terme

(101)  Les formules et les déterminations expérimentales du fluage et du retrait sont fondées
sur des données collectées sur des périodes limitées. L'extrapolation de tels résultats pour des
évaluations  à  très  long  terme  (par  exemple  un  siècle)  conduit  à  l'introduction  d'erreurs
supplémentaires associées aux expressions mathématiques utilisées pour l'extrapolation.

(102)  Les formules indiquées en B.1, B.2 et B.103 de la présente Annexe fournissent une
estimation  moyenne  satisfaisante  des  déformations  différées  extrapolées  à  long  terme.
Toutefois, lorsque la surestimation des déformations différées entraîne une augmentation de la
sécurité, et lorsque le projet le justifie, il convient de multiplier le fluage et le retrait prévus sur la
base des formules ou des déterminations expérimentales par un coefficient partiel.

(103) Il est possible d'inclure le facteur partiel γ  suivant, afin de tenir compte de l'incertitude
 lt
concernant les déformations différées réelles du béton à long terme (c'est-à-dire l'incertitude
liée à la validité de l'extrapolation des formules mathématiques issues des mesures du fluage et
du  retrait  sur  une  période  relativement  courte).  Les  valeurs  de γ  lt   sont  données  dans  le
Tableau B.101 :

Tableau B.101 : Coefficient partiel pour l'extrapolation à long terme des déformations
différées, le cas échéant

t (âge du béton pour l'estimation
γ
|     | des déformations différées)  |              |  lt   |     |     |     |
| --- | ---------------------------- | ------------ | ----- | --- | --- | --- |
|     |                              | t < 1 an     | 1     |     |     |     |
|     |                              | t = 5 ans    | 1,07  |     |     |     |
|     |                              | t = 10 ans   | 1;1   |     |     |     |
|     |                              | t = 50 ans   | 1,17  |     |     |     |
|     |                              | t = 100 ans  | 1,20  |     |     |     |
|     |                              | t = 300 ans  | 1,25  |     |     |     |

 ce qui correspond à l'expression mathématique suivante :

| t ≤ 1 | an  |     | γ = 1 |     |     |     |
| ------ | --- | --- | ----- | --- | --- | --- |
lt

|     |     |     |  t  |     |     | (B.128)  |
| --- | --- | --- | ----- | --- | --- | -------- |

| t ≥ 1 | an  | γ = 1 + 0,1log |   où | t = 1an |     |     |
| ----- | --- | -------------- | ------ | ------- | --- | --- |
|      |     | lt             |      | ref     |     |     |
|      |     |                |  t   |         |     |     |
ref

Pour le béton âgé de moins de un an, les Expressions (B.1), (B.2) et (B.103) peuvent être
utilisées directement, dans la mesure où elles correspondent à la durée des essais servant à
l'étalonnage des formules.
Pour le béton âgé de un an ou plus, et donc particulièrement pour les évaluations à long terme
des déformations, les valeurs données par les Expressions (B.1) et (B.11) de l’EN 1992-1-1 et
les Expressions (B.116) et (B.118) du présent document (amplitude des déformations différées
| au temps t) doivent être multipliées par γ |     |     | .   |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- |
 lt
