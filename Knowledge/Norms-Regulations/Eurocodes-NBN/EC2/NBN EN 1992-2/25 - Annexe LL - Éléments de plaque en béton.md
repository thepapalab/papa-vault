---
parent: "[[00 - Index]]"
norm: "NBN EN 1992-2:2005"
---

## Annexe LL — Éléments de plaque en béton

ANNEXE  LL
(informative)

Éléments de plaque en béton

(101) La présente section s'applique aux éléments de plaque, comportant généralement huit
composantes différentes de sollicitations. Ces huit composantes sont énumérées ci-dessous et
présentées à la Figure LL.1 pour un élément de dimensions unitaires :
| • 3 composantes d'effort de plaque  n       |     |  , n n     | = n        |     |
| ------------------------------------------- | --- | ---------- | ---------- | --- |
|                                             |     | Edx Edy ,  | Edxy  Edyx |     |
| • 3 composantes de flexion de plaque  m     |     |  , m       | m = m      |     |
|                                             |     | Edx Edy ,  | Edxy  Edyx |     |
| • 2 efforts de cisaillement transversaux  v |     |  , v       |            |     |
Edx Edy
h
y  x
|      | v   dx  |     | v     |     |
| ---- | ------- | --- | ----- | --- |
|      | E       | z   | Edy   |     |
| n    |         |     | n     |     |
| Edx  | n       |     | n Edy |     |
|      | Edyx    |     | Edxy  | m   |
E dy
m
| E dx  |     |     |     | m   |
| ----- | --- | --- | --- | --- |
m Edxy
Edxy

Figure LL.1: Éléments de plaque
(102)  La première phase de la procédure de vérification consiste à déterminer si l'élément de
plaque présente ou non des fissures.

h
|     | 1   |     | 1   |     |
| --- | --- | --- | --- | --- |

ts
tc
t z
i
|     |     | y   | x   |     |
| --- | --- | --- | --- | --- |

Figure LL.2: Modèle de type sandwich

(103) Dans le cas des éléments non fissurés, la seule vérification requise consiste à s'assurer
que la contrainte principale minimale est inférieure à la résistance de calcul en compression f .
cd
Il peut être approprié de prendre en compte l'état de compression multi-axiale dans la définition
de f .
cd

(104)  Dans le cas des éléments fissurés, il convient d'utiliser un modèle de type sandwich pour
le calcul ou la vérification de l'élément de plaque.

(105) Le modèle de type sandwich identifie trois couches (Figure LL.2) : les deux couches
extérieures résistent aux actions de la membrane dues à n  , n n , m  , m m ; et
|     |     |     |     |     |     |     |     |     | Edx | Edy ,  Edxy  | Edx | Edy ,  | Edxy   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | ------ |
la couche intermédiaire résiste aux efforts tranchants v  , v . Il convient de déterminer
|     |     |     |     |     |     |     |     |     | Edx | Edy |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
l'épaisseur des différentes couches par une méthode itérative (voir clauses (113) à (115)).

(106)  Il convient de calculer la couche intermédiaire conformément au 6.2, en tenant compte
de l'effort tranchant principal, de sa direction principale et des armatures longitudinale dans
cette direction (voir clauses (113) à (115)).

(107)  Il convient, afin de déterminer la fissuration effective des éléments de plaque, de vérifier
les contraintes principales à différents niveaux d'épaisseur de l'élément. Il convient, dans la
pratique, de vérifier l'inégalité suivante :

J
|     |     |     | J    |     | I   |          |     |     |     |     |     |     |           |
| --- | --- | --- | ---- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --------- |
|     | Φ=α |     | 2 +λ | 2   | +β  | 1 −1≤0   |     |     |     |     |     |     | (LL.101)  |
|     |     |     | f 2  | f   | f   |          |     |     |     |     |     |     |           |
|     |     |     | cm   | cm  | cm  |          |     |     |     |     |     |     |           |

où :
|     |     | 1[  |      |     |      |     |      | ]   |     |     |     |     |           |
| --- | --- | --- | ---- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --------- |
|     |     |     | (    | )2  | (    | )2  | (    | )2  |     |     |     |     |           |
|     | J   | =   | σ −σ | +   | σ −σ | +   | σ −σ |     |     |     |     |     | (LL.102)  |
|     |     | 2   | 1    | 2   | 2    | 3   | 3    | 1   |     |     |     |     |           |
|     |     | (   |       | )(   | )(  |     | )   |     |     |     |     |     |           |
| --- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
|     | J   | = σ | −σ    | σ −σ | σ   | −σ  |     |     |     |     |     |     | (LL.103)  |
|     |     | 3   | 1 m   | 2    | m   | 3 m |     |     |     |     |     |     |           |
|     | I   | =σ  | +σ +σ |      |     |     |     |     |     |     |     |     | (LL.104)  |
|     | 1   | 1   | 2     | 3    |     |     |     |     |     |     |     |     |           |
|     |     | (   |       | )    |     |     |     |     |     |     |     |     |           |
|     | σ   | = σ | +σ    | +σ   | 3   |     |     |     |     |     |     |     | (LL.105)  |
|     |     | m   | 1     | 2 3  |     |     |     |     |     |     |     |     |           |
|     | α=  |     |     |     |     |     |     |     |     |     |     |     | (LL.106)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
9k1,4
|     |     |        | 1  |         |         |    |     |      |       |     |     |     |     |
| --- | --- | ------ | --- | ------- | ------- | --- | --- | ---- | ----- | --- | --- | --- | --- |
|     | λ   | =c cos |     | arcos ( | c cos3θ | )   |     | pour | cos3θ | ≥0  |     |     |     |
|     |     |        |    |         |         |    |     |      |       |     |     |     |     |
|     |     | 1      | 3  |         | 2       |     |     |      |       |     |     |     |     |

|                                                                  |     |     |     |         |     |       |     |      |       |     |     |     | (LL.107)  |
| ---------------------------------------------------------------- | --- | --- | --- | ------- | --- | ----- | --- | ---- | ----- | --- | --- | --- | --------- |
|                                                                  |     |     | π  | 1       |     |       |    |      |       |     |     |     |           |
|                                                                  |     |     |     |         | (   |       | )   |      |       |     |     |     |           |
|                                                                  | λ   | =c  | cos | − arcos | −c  | cos3θ |     | pour | cos3θ | <0  |     |     |           |
|  |     | 1   |    |         |     | 2     |    |      |       |     |     |     |           |
|                                                                  |     |     | 3  | 3       |     |       |    |      |       |     |     |     |           |
|     | β=  |     |     |     |     |     |     |     |     |     |     |     | (LL.108)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
3,7k1,1
|     |       |     | 3 3 | J   |     |     |     |     |     |     |     |     |           |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
|     | cos3θ |     | =   | 3   |     |     |     |     |     |     |     |     | (LL.109)  |
|     |       |     | 2   | 3   |     |     |     |     |     |     |     |     |           |
J 2
|     | c   | =   |     |     |     |     |     |     |     |     |     |     | (LL.110)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
0,7k0,9
|     |     |        | (   |       | )2  |     |     |     |     |     |     |     |           |
| --- | --- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
|     | c   | =1−6,8 | k   | −0,07 |     |     |     |     |     |     |     |     | (LL.111)  |
f
|     | k   | = ctm |     |     |     |     |     |     |     |     |     |     | (LL.112)  |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
f
cm

Si l'inégalité (LL.101) est satisfaite, l'élément est considéré comme non fissuré ; dans le cas
contraire, il convient de considérer qu'il est fissuré.

(108)  Lorsque l'élément de plaque est considéré comme étant fissuré, il est recommandé de
déterminer les efforts appliqués aux couches extérieures du modèle de type sandwich selon les
équations suivantes (Figures LL.3a et LL.3b).

|          | z −y | m          |     |     |     |     |     |     |     |           |
| -------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --------- |
| n = n    | x    | xs + Edx   |     |     |     |     |     |     |     | (LL.113)  |
| Edxs Edx |      |            |     |     |     |     |     |     |     |           |
|          | z    | z          |     |     |     |     |     |     |     |           |
|          | x    | x          |     |     |     |     |     |     |     |           |

|          | z −y | m      |     |     |     |     |     |     |     |           |
| -------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --------- |
|          | x    | xi Edx |     |     |     |     |     |     |     |           |
| n =n     |      | −      |     |     |     |     |     |     |     | (LL.114)  |
| Edxi Edx | z    | z      |     |     |     |     |     |     |     |           |
|          | x    | x      |     |     |     |     |     |     |     |           |

|          | z −y | m      |     |     |     |     |     |     |     |           |
| -------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --------- |
|          | y    | ys Edy |     |     |     |     |     |     |     |           |
| n = n    |      | +      |     |     |     |     |     |     |     | (LL.115)  |
| Edys Edy |      |        |     |     |     |     |     |     |     |           |
|          | z    | z      |     |     |     |     |     |     |     |           |
|          | y    | y      |     |     |     |     |     |     |     |           |

|          | z −y | m      |     |     |     |     |     |     |     |           |
| -------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --------- |
|          | y    | yi Edy |     |     |     |     |     |     |     |           |
| n =n     |      | −      |     |     |     |     |     |     |     | (LL.116)  |
| Edyi Edy |      |        |     |     |     |     |     |     |     |           |
|          | z    | z      |     |     |     |     |     |     |     |           |
|          | y    | y      |     |     |     |     |     |     |     |           |

|       | z      | −y m       |     |     |     |     |     |     |     |           |
| ----- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --------- |
| n = n | yx     | yxs − Edyx |     |     |     |     |     |     |     | (LL.117)  |
| Edyxs | Edyx z | z          |     |     |     |     |     |     |     |           |
|       |        | yx yx      |     |     |     |     |     |     |     |           |

|            | z −y | m            |     |     |     |     |     |     |     |           |
| ---------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --------- |
| n =n       | yx   | yxi + Edyx   |     |     |     |     |     |     |     | (LL.118)  |
| Edyxi Edyx | z    | z            |     |     |     |     |     |     |     |           |
|            |      | yx yx        |     |     |     |     |     |     |     |           |

|       | z      | −y m     |     |     |     |     |     |     |     |           |
| ----- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --------- |
|       | xy     | xys Edxy |     |     |     |     |     |     |     |           |
| n = n |        | −        |     |     |     |     |     |     |     | (LL.119)  |
| Edxys | Edxy z | z        |     |     |     |     |     |     |     |           |
|       |        | xy xy    |     |     |     |     |     |     |     |           |

|            | z −y | m        |     |     |     |     |     |     |     |           |
| ---------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --------- |
|            | xy   | xyi Edxy |     |     |     |     |     |     |     |           |
| n =n       |      | +        |     |     |     |     |     |     |     | (LL.120)  |
| Edxyi Edxy |      |          |     |     |     |     |     |     |     |           |
|            | z    | z        |     |     |     |     |     |     |     |           |
|            |      | xy xy    |     |     |     |     |     |     |     |           |

où :
(cid:131)  z  et z  représentent les bras de levier pour les moments fléchissants et les efforts
| x   | y   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
normaux de la plaque ;

(cid:131)  y  , y  , y  , y  , représentent les distances comprises entre le centre de gravité
| xs  | xi ys | yi  |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
des armatures de béton armé et le plan central de l'élément dans les directions x et
y, par rapport aux efforts normaux et de flexion de la plaque ; par conséquent
| z x  = y | xs  +y   xi   et  z | y  =y   ys  +y   | yi   ;  |     |     |     |     |     |     |     |
| -------- | ------------------- | ---------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
(cid:131)  y  , y  , y  , y  , représentent les distances comprises entre le centre de gravité
| yxs | yxi xys | xyi |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
des armatures de béton armé et le plan central de l'élément, par rapport au couple
de torsion et aux efforts tranchants de la plaque; par conséquent z =y +y   et
|            |               |     |     |     |     |     |     |     | yx    | yxs    yxi |
| ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- |
| z xy  =y   | xys  +y   xyi |  ;  |     |     |     |     |     |     |       |            |

h
|     |     |     | 1   |     |     |     | 1   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| y   | x   s |     |     |     |     |     |     |     | y y   s    |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | ---------- |
zx    z
| y   |      |     |        |     |     |     |     |       | y   y |
| --- | ---- | --- | ------ | --- | --- | --- | --- | ----- | ----- |
|     | x i  |     |        |     |     |     |     |       |       |
|     |      |     |        |     |     | z   |     |       | y i   |
|     |      |     | n      |     |     |     | n   |       |       |
|     |      |     | E dxs  |     |     |     |     | E dys |       |
m
|     |     | m      |     |     |     |     |     |     | E dy    |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | ------- |
E dx
n
Edx
|     |     |     | n    |     | y   | x   | n    |     |     |
| --- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- |
|     |     |     | Edxi |     |     |     | Edyi | n   |     |
Edy

Figure LL.3a : Efforts normaux et moments fléchissants dans la couche extérieure

h
|         |     |     | 1   |     |     |     | 1   |     |       |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
| y       |     |     |     |     |     |     |     |     | y     |
| z   yxs |     |     |     |     |     |     |     |     | xys z |
yx xy
| y    |      |       |     |       |     |       |       |      | y   |
| ---- | ---- | ----- | --- | ----- | --- | ----- | ----- | ---- | --- |
| yxi  |      |       |     |       | z   |       |       |      | xyi |
|      |      | n     |     |       |     |       | n     |      |     |
|      |      | Edyxs |     |       |     |       | Edxys |      |     |
|      | n    |       | n   |       |     | n     |       |      |     |
|      |      |       |     | Edyxi |     | Edxyi |       | n    |     |
|      | Edyx |       |     |       |     |       |       | Edxy |     |
| m    |      |       |     | y     |     | x     |       |      | m   |
| Edyx |      |       |     |       |     |       |       |      |     |
Edxy

Figure LL.3b : Actions de cisaillement de la plaque et moments de torsion dans la
couche extérieure

Les efforts tranchants hors plan v  et v   sont appliqués à la couche intermédiaire avec le
|     |     |     | Edx | Edy |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bras  de  levier,  z ,  déterminé  par  rapport  au  centre  de  gravité  des  couches  appropriées

d'armatures.

(109)  Pour le calcul de la couche intermédiaire, il convient d'évaluer l'effort tranchant principal
v  et sa direction ϕ de la manière suivante :
Edo o

|     |     | 2   | 2   |     |     |     |     |     |               |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
| v   | = v | +v  |     |     |     |     |     |     |     (LL.121)  |
| Edo | Edx | Edy |     |     |     |     |     |     |               |
v
Edy
| tanϕ | =   |     |     |     |     |     |     |     |     (LL.122)  |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
|      | o v |     |     |     |     |     |     |     |               |
Edx

(110)  Dans la direction de l'effort tranchant principal, l'élément de plaque se comporte comme
une poutre et il convient par conséquent d'appliquer les règles de calcul appropriées. Il est

recommandé d'appliquer notamment le 6.2.2 pour les éléments ne nécessitant pas d'armatures
d'effort  tranchant  et  le  6.2.3  pour  les  éléments  nécessitant  de  telles  armatures.  Dans
l'Expression (6.2.a), il convient de déterminer ρ comme suit :  l

|      | cos2ϕ | sin2ϕ |     |     |     |     |     |     |     |           |
| ---- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --------- |
| ρ =ρ | +ρ    |       |     |     |     |     |     |     |     | (LL.123)  |
| l    | x o   | y     | o   |     |     |     |     |     |     |           |

(111)  Lorsque des armatures d'effort tranchant sont nécessaires, l'effort longitudinal résultant
du modèle en treillis V cotθ entraîne les efforts de plaque suivants dans les directions x et y :
Edo

v 2
| n = | Edy cotθ  |     |     |     |     |     |     |     |     | (LL.124)  |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
Edyc
v
Edo
v v
| n     | = Edx Edy cotθ  |     |     |     |     |     |     |     |     | (LL.125)  |
| ----- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
| Edxyc | v               |     |     |     |     |     |     |     |     |           |
Edo
v 2
Edx
| n =  | cotθ  |     |     |     |     |     |     |     |     | (LL.126)  |
| ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
| Edxc | v     |     |     |     |     |     |     |     |     |           |
Edo
|       | v     | v       |       |     |     |     |     |     |     |           |
| ----- | ----- | ------- | ----- | --- | --- | --- | --- | --- | --- | --------- |
|       |       | Edx Edy |       |     |     |     |     |     |     |           |
| n     | =n =  |         | cotθ  |     |     |     |     |     |     | (LL.127)  |
| Edyxc | Edxyc |         |       |     |     |     |     |     |     |           |
v
Edo

(112)  Il convient de dimensionner les couches extérieures comme des éléments de plaque, en
utilisant les règles de calcul de la clause 6.109 et de l'Annexe F.

(113)    La  méthode  simplifiée  suivante  peut  généralement  être  choisie  eu  égard  aux
Figures LL.3a et LL.3b :

| y = y | = y     |       |     |     |     |     |     |     |     | (LL.128)  |
| ----- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --------- |
| ns    | xs ys   |       |     |     |     |     |     |     |     |           |
| y = y | = y     |       |     |     |     |     |     |     |     | (LL.129)  |
| ni    | xi yi   |       |     |     |     |     |     |     |     |           |
| y = y | = y     |       |     |     |     |     |     |     |     | (LL.130)  |
| ts    | xys yxs |       |     |     |     |     |     |     |     |           |
| y = y | = y     |       |     |     |     |     |     |     |     | (LL.131)  |
| ti    | xyi yxi |       |     |     |     |     |     |     |     |           |
| z = z | = z = y | +y    |     |     |     |     |     |     |     | (LL.132)  |
| x     | y n ns  | ni    |     |     |     |     |     |     |     |           |
| z = z | = z = y | +y    |     |     |     |     |     |     |     | (LL.133)  |
| xy    | yx t    | ts ti |     |     |     |     |     |     |     |           |

La différence entre z  et z peut généralement être négligée, en supposant que l'épaisseur des
n t
couches extérieures représente le double de l'enrobage du béton, par conséquent :

| y = y | = y    |     |     |     |     |     |     |     |     | (LL.134)  |
| ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
| ns    | ts s   |     |     |     |     |     |     |     |     |           |
| y = y | = y    |     |     |     |     |     |     |     |     | (LL.135)  |
| ni    | ti i   |     |     |     |     |     |     |     |     |           |
| z = z | = z    |     |     |     |     |     |     |     |     | (LL.136)  |
| n     | t      |     |     |     |     |     |     |     |     |           |

(114)  Sur la base des hypothèses ci-dessus, les efforts appliquées sur les couches extérieures
peuvent être évalués comme suit :

a)  lorsque aucune armature d'effort tranchant n'est requise pour reprendre v  et v
|     |     |     |     |     |     |     |     |     | Edx | Edy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

z−y m
| n = n    | s + | Edx   |     |     |     |     |     |     |     | (LL.137)  |
| -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --------- |
| Edxs Edx |     |       |     |     |     |     |     |     |     |           |
|          | z   | z     |     |     |     |     |     |     |     |           |

|      | z−y |     | m   |     |     |     |     |     |     |     |           |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
|      |     | i   | Edx |     |     |     |     |     |     |     |           |
| n =  | n   | −   |     |     |     |     |     |     |     |     | (LL.138)  |
| Edxi | Edx | z   | z   |     |     |     |     |     |     |     |           |
m
z−y
| n =  | n   | s + | Edy   |     |     |     |     |     |     |     | (LL.139)  |
| ---- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --------- |
| Edys | Edy | z   | z     |     |     |     |     |     |     |     |           |
|      | z−y |     | m     |     |     |     |     |     |     |     |           |
Edy
| n =   | n    | i − |        |     |     |     |     |     |     |     | (LL.140)  |
| ----- | ---- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --------- |
| Edyi  | Edy  |     |        |     |     |     |     |     |     |     |           |
|       |      | z   | z      |     |     |     |     |     |     |     |           |
|       |      | z−y | m      |     |     |     |     |     |     |     |           |
| n     | = n  | s   | − Edxy |     |     |     |     |     |     |     | (LL.141)  |
| Edxys | Edxy | z   | z      |     |     |     |     |     |     |     |           |
|       |      | z−y | m      |     |     |     |     |     |     |     |           |
| n =   | n    | i + | Edxy   |     |     |     |     |     |     |     | (LL.142)  |
| Edxyi | Edxy |     |        |     |     |     |     |     |     |     |           |
|       |      | z   | z      |     |     |     |     |     |     |     |           |

b)  lorsque des armatures d'effort tranchant sont nécessaires pour reprendre v  et v
|     |     |     |     |     |     |     |     |     |     |     | Edx Edy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- |

|      |     | z−y | m     | 1v  |       |     |     |     |     |     |           |
| ---- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --------- |
| n =  | n   | s + | Edx + | Edx | cotθ  |     |     |     |     |     | (LL.143)  |
| Edxs | Edx | z   | z     | 2 v |       |     |     |     |     |     |           |
Edo
|      | z−y |     | m     | 1v  | 2     |     |     |     |     |     |           |
| ---- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --------- |
| n =  | n   | i − | Edx + | Edx | cotθ  |     |     |     |     |     | (LL.144)  |
| Edxi | Edx |     |       |     |       |     |     |     |     |     |           |
|      |     | z   | z     | 2 v |       |     |     |     |     |     |           |
Edo
|      |     | z−y | m     | 1v  |       |     |     |     |     |     |           |
| ---- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --------- |
| n =  | n   | s + | Edy + | Edy | cotθ  |     |     |     |     |     | (LL.145)  |
| Edys | Edy | z   | z     | 2 v |       |     |     |     |     |     |           |
Edo
|     |     |     | m   | 1v  | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
z−y
| n =  | n   | i − | Edy + | Edy | cotθ  |     |     |     |     |     | (LL.146)  |
| ---- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --------- |
| Edyi | Edy | z   | z     | 2 v |       |     |     |     |     |     |           |
Edo
|       |      | z−y | m      | 1v  | v             |     |     |     |     |     |           |
| ----- | ---- | --- | ------ | --- | ------------- | --- | --- | --- | --- | --- | --------- |
| n     | = n  | s   | − Edxy | +   | Edx Edy cotθ  |     |     |     |     |     | (LL.147)  |
| Edxys | Edxy | z   | z      | 2   | v             |     |     |     |     |     |           |
Edo
|       |      | z−y | m    | 1v  | v     |     |     |     |     |     |           |
| ----- | ---- | --- | ---- | --- | ----- | --- | --- | --- | --- | --- | --------- |
|       |      |     | Edxy | Edx | Edy   |     |     |     |     |     |           |
| v =   | n    | i + |      | +   | cotθ  |     |     |     |     |     | (LL.148)  |
| Edxyi | Edxy |     |      |     |       |     |     |     |     |     |           |
|       |      | z   | z    | 2   | v     |     |     |     |     |     |           |
Edo

(115)  Si la vérification décrite en (112) ci-dessus n'est pas satisfaite, il convient d'appliquer l'un
des modes opératoires suivants :

a)  augmenter l'enrobage et par conséquent réduire le bras de levier interne ;
b)  utiliser différentes valeurs pour z  et z avec z  > z ; il convient alors d'additionner
|     |     |     |     |     | n t |     | n   | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vectoriellement les contraintes dans le béton ;
c)  augmenter l'épaisseur de couche afin de satisfaire la vérification du béton et ne pas

modifier la position de l'armature. Ceci entraîne un excentrement des armatures
dans  la  couche,  et  par  conséquent  deux  moments  fléchissants  internes,  qu’il
convient  d’équilibrer  dans  l'élément  de  plaque.  Dans  ce  type  de  situations,  les
sollicitations appliquées sur les armatures s'expriment comme suit :

| *   |    |  t  |        |    | t      |  (  |     | )   |     |     |            |
| --- | --- | ---- | ------ | --- | -------- | ---- | --- | --- | --- | --- | ---------- |
| n   | = n |  h− | s −b' | +n  |  i −b' | h−b' | −b' |     |     |     |  (LL.149)  |
|     |    | Eds  | i      | Edi | i        |     | i   | s   |     |     |            |
| Eds |     |     | 2      |    | 2     |      |     |     |     |     |            |

| *     |     |       | *   |     |     |     |     |     |     |     |  (LL.150)  |
| ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |
| n Edi | = n | +n −n |     |     |     |     |     |     |     |     |            |
|       | Eds | Edi   | Eds |     |     |     |     |     |     |     |            |

où :
t  et t  représentent l'épaisseur des couches, respectivement supérieure et
s i
inférieure

b' est la distance entre la surface extérieure de la couche et l'axe des
i , s
armatures dans la couche.
Il convient de vérifier la couche intermédiaire afin de déterminer un effort tranchant hors plan
supplémentaire correspondant à l'effort transmis entre les couches d'armatures.
