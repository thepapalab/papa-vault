---
parent: "[[00 - Index]]"
norm: "NBN EN 1992-2:2005"
---

## Annexe MM — Effort tranchant et flexion transversale

ANNEXE  MM
(informative)

Effort tranchant et flexion transversale

(101)  L'interaction, au sein des âmes des caissons, entre l'effort tranchant longitudinal et la
flexion transversale peut être déterminée à l'aide du modèle de type sandwich (voir Annexe LL).
Les simplifications suivantes peuvent être introduites par rapport au modèle général pour les
besoins de la présente application (Figure MM.1) :
•  Il convient de considérer que l'effort tranchant longitudinal par unité de longueur a une
| valeur constante le long de ∆x : v |     |  = V  / ∆y.  |     |     |     |
| ---------------------------------- | --- | ------------ | --- | --- | --- |
|                                    |     | Ed Ed        |     |     |     |
•  Il convient de considérer que le moment fléchissant transversal par unité de longueur a
| une valeur constante le long de ∆y : m |     |  = M |  / ∆x.  |     |     |
| -------------------------------------- | --- | ---- | ------- | --- | --- |
|                                        |     | Ed   | Ed      |     |     |
•  Il est supposé que la force longitudinale a une valeur constante sur la longueur ∆y :
p Ed  = P Ed  / ∆y.
Il convient de négliger, sur la longueur ∆y, l'effort tranchant transversal dans l'âme, dû à
•
la variation du moment fléchissant correspondant.

y
b
w
m
Ed
p
v
|     |     | Ed  | Ed  |     |     |
| --- | --- | --- | --- | --- | --- |
∆y
v
Ed
z
v
Ed
|     | p   | v   |     |     |     |
| --- | --- | --- | --- | --- | --- |
Ed
Ed
∆x
m
Ed
x

Figure MM.1 : Sollicitations dans une âme

(102)    Sur  la  base  des  hypothèses  ci-dessus,  le  modèle  de  type  sandwich  comprend
uniquement deux couches sur lesquelles agissent les contraintes suivantes (Figure MM.2) :

b −z
| τ =v     | w 2   |      |     |     |   (MM.101)  |
| -------- | ----- | ---- | --- | --- | ----------- |
| Ed1 Ed ( |       | )    |     |     |             |
| 2b       | −z −z | z    |     |     |             |
|          | w 1 2 | 1    |     |     |             |

b −z
| τ =v        | w 1   |      |     |     |   (MM.102)  |
| ----------- | ----- | ---- | --- | --- | ----------- |
| Ed2 Ed ( 2b | −z −z | ) z  |     |     |             |
|             | w 1 2 | 2    |     |     |             |

m
Edx
| σ =    |          |         |     |     |   (MM.103)  |
| ------ | -------- | ------- | --- | --- | ----------- |
| Edy1 ( | b ( z +z | ) 2 ) z |     |     |             |
−
|     | w 1 | 2 1 |     |     |     |
| --- | --- | --- | --- | --- | --- |

m
| σ =  | Edx          |         |     |     |   (MM.104)  |
| ---- | ------------ | ------- | --- | --- | ----------- |
| Edy2 | ( b − ( z +z | ) 2 ) z |     |     |             |
|      | w 1          | 2 2     |     |     |             |

b −z
| σ = p | w       | 2      |     |     |   (MM.105)  |
| ----- | ------- | ------ | --- | --- | ----------- |
|       | (       | )      |     |     |             |
| Edx1  | d 2b −z | −z z   |     |     |             |
|       | w 1     | 2 1    |     |     |             |

b −z
| σ = p | w     | 1     |     |     |   (MM.106)  |
| ----- | ----- | ----- | --- | --- | ----------- |
| Edx2  | d (   | )     |     |     |             |
|       | 2b −z | −z z  |     |     |             |
|       | w     | 1 2 2 |     |     |             |

b
w
|     |     |     | z   | z   |     |
| --- | --- | --- | --- | --- | --- |
|     |     |     | 2   | 1   |     |
σ
Edy1 σ
Edy2
τ
Ed2
τ
Ed1
|     |     | τ τ |     |     |     |
| --- | --- | --- | --- | --- | --- |
Ed2
Ed1
σ
Edx2  σ
Edx1

Figure MM.2 : Modèle de type sandwich modifié

(103)    Il  convient  de  fonder  le  calcul  des  deux  couches  sur  une  méthode  itérative,  afin
d'optimiser les épaisseurs z  et z  , en utilisant le mode opératoire donné en 6.109 et dans
|     | 1   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- |
l'Annexe F ; différentes valeurs de l'angle θ   et de l'angle θ peuvent être supposées pour les
el
deux couches, bien qu'une valeur constante doive s'appliquer à chaque couche. Si le ferraillage

résultant  présente  une  excentricité  entre  les  deux  couches,  il  convient  d'appliquer  les
Expressions (LL.149) et (LL.150) de l'Annexe LL.

(104)  Lorsque l'effort longitudinal calculé est un effort de traction, il peut être procédé à la
répartition des armatures le long de l'âme ou, alternativement, il peut être considéré que l'effort
est transmis aux membrures tendue et comprimée ; une moitié de l'effort étant transmise à la
membrure tendue et l'autre moitié étant transmise à la membrure comprimée.

(105)    En  l'absence  d'effort  longitudinal,  les  règles  définies  au  6.24  peuvent  être  utilisées
comme simplification, mais il convient cependant d'ajouter les armatures de cisaillement aux
armatures de flexion.
