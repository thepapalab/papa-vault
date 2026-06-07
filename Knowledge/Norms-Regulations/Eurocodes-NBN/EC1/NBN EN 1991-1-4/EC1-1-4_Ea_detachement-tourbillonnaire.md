---
title: "NBN EN 1991-1-4:2005 — Détachement tourbillonnaire"
type: norm-extract
source: "NBN EN 1991-1-4:2005"
norm: EC1-1-4
section: "E.1"
chapter: "Détachement tourbillonnaire"
tags: [EC1-1-4, eurocode-1, vent]
related: ["[[EC1-1-4_index]]", "[[EC1-1-4_D_valeurs-cscd]]", "[[EC1-1-4_Eb_galop-divergence-flottement]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

Annexe E
(informative)
Détachement tourbillonnaire et instabilités aéroélastiques
E.1 Détachement tourbillonnaire
E.1.1 Généralités
(1) Le détachement tourbillonnaire survient lorsque des tourbillons se détachent alternativement à partir des côtés
opposés de la construction. Ceci produit une force fluctuante perpendiculaire à la direction du vent. La mise en
vibration de la construction peut se produire si la fréquence du détachement tourbillonnaire est identique à une
fréquence propre de la construction. Cette condition se produit lorsque la vitesse du vent est égale à la vitesse
critique du vent définie en E.1.3.1. Généralement, la vitesse critique est une vitesse fréquemment observée du
vent de sorte que, du fait du nombre de cycles de chargement, la fatigue peut devenir préoccupante.
(2) La réponse (de la construction) au détachement tourbillonnaire se compose d'une réponse à large bande qui
se produit que la construction se déplace ou non, et d'une réponse à bande étroite ayant pour origine une force
aérodynamique induite par le mouvement.
NOTE 1 La réponse à large bande est généralement plus importante pour les constructions en béton armé et les
constructions lourdes en acier.
NOTE 2 La réponse à bande étroite est généralement plus importante pour les constructions légères en acier.
E.1.2 Critères relatifs au détachement tourbillonnaire
(1) Il convient d'examiner l'effet de détachement tourbillonnaire lorsque le rapport entre la plus grande et la plus
petite dimension transversale de la construction, toutes deux prises dans le plan perpendiculaire au vent, est
supérieur à 6.
(2) Il n'est pas nécessaire d'examiner l'effet du détachement tourbillonnaire lorsque :
v > 1,25 . v (E.1)
crit,i m
où
v est la vitesse critique du vent pour le mode i, tel que définie en E.1.3.1
crit,i
v est la vitesse moyenne sur 10 min caractéristique du vent, spécifiée en 4.3.1 (1) au niveau de la
m
section transversale où se produit le détachement tourbillonnaire (voir Figure E.3)
117


EN 1991-1-4:2005 (F)
E.1.3 Paramètres fondamentaux du détachement tourbillonnaire
E.1.3.1 Vitesse critique du vent v
crit,i
(1) La vitesse critique du vent pour le mode de vibration de flexion i est définie comme la vitesse du vent à
laquelle la fréquence du détachement tourbillonnaire est égale à une fréquence propre de la construction ou d'un
élément structural ; elle est donnée par l'expression (E.2).
b⋅n
v = i,y (E.2)
crit,i St
où
b est la largeur de référence de la section transversale sur laquelle se produit le détachement
tourbillonnaire en résonance et sur laquelle la déformée modale est maximale, pour la construction ou
l'élément structural considérés ; dans le cas des cylindres à base circulaire, la largeur de référence est
le diamètre extérieur
n est la fréquence propre du mode considéré i, de vibration en flexion perpendiculairement au vent. Des
i,y
valeurs approchées de n sont données en F.2
1,y
St est le nombre de Strouhal tel que défini en E.1.3.2
(2) La vitesse critique du vent pour le mode i de vibration par ovalisation des coques cylindriques est définie
comme la vitesse du vent à laquelle le double de la fréquence du détachement tourbillonnaire est égal à la
fréquence propre du mode d'ovalisation i de la coque cylindrique ; elle est donnée par l'expression (E.3).
b⋅n
v = i,0 (E.3)
crit,i 2⋅St
où
b est le diamètre extérieur de la coque
St est le nombre de Strouhal tel que défini en E.1.3.2
n est la fréquence propre du mode d'ovalisation i de la coque
i,0
NOTE 1 n est donné en F.2 (3) pour les coques dépourvues d'anneaux de rigidité.
0
NOTE 2 L'annexe E ne traite pas des méthodes de calcul des vibrations d'ovalisation.
E.1.3.2 Nombre de Strouhal St
Le nombre de Strouhal St applicable à différentes sections transversales peut être lu dans le Tableau E.1.
118


EN 1991-1-4:2005 (F)
Tableau E.1 — Nombres de Strouhal St pour différentes sections transversales
Section transversale  St
|     |     | 0,18  |
| --- | --- | ----- |

| pour tous les nombres de Reynolds (Re)  |     |     |
| --------------------------------------- | --- | --- |
donné à la

Figure E.1

| 0,5 ≤ d/b ≤ 10  |          |       |
| --------------- | -------- | ----- |
|                 | d/b = 1  | 0,11  |
d/b = 1,5
0,10
|     | d/b = 2  | 0,14  |
| --- | -------- | ----- |

| interpolation linéaire  |          |       |
| ----------------------- | -------- | ----- |
|                         | d/b = 1  | 0,13  |
|                         | d/b = 2  | 0,08  |

| interpolation linéaire  |          |       |
| ----------------------- | -------- | ----- |
|                         | d/b = 1  | 0,16  |
|                         | d/b = 2  | 0,12  |

| interpolation linéaire  |            |       |
| ----------------------- | ---------- | ----- |
|                         | d/b = 1,3  | 0,11  |
|                         | d/b = 2,0  | 0,07  |

| interpolation linéaire  |     |     |
| ----------------------- | --- | --- |
NOTE  Les extrapolations du nombre de Strouhal en fonction de d/b ne
sont pas admises.
119

EN 1991-1-4:2005 (F)
Figure E.1 — Nombre de Strouhal (St ) pour les sections transversales
rectangulaires à angles vifs
E.1.3.3 Nombre de Scruton Sc
(1) La sensibilité aux vibrations dépend de l'amortissement structural et du rapport de la masse de la construction
à la masse du fluide. Ceci est exprimé par le nombre de Scruton Sc, donné par l'expression (E.4) suivante :
2⋅δ ⋅m
Sc= s i,e (E.4)
ρ⋅b2
où
δ est l'amortissement structural exprimé par le décrément logarithmique
s
ρ est la masse volumique de l'air dans les conditions de détachement tourbillonnaire
m est la masse équivalente m par unité de longueur pour le mode i telle que définie en F.4 (1)
i,e e
b est la largeur de référence de la section transversale à laquelle se produit le détachement
tourbillonnaire en résonance
NOTE La valeur de la masse volumique ρ peut être donnée dans l'Annexe Nationale. La valeur recommandée est
1,25 kg/m3.
E.1.3.4 Nombre de Reynolds Re
(1) L'action du détachement tourbillonnaire sur un cylindre à base circulaire dépend du nombre de Reynolds Re à
la vitesse critique du vent v . Le nombre de Reynolds est donné par l'expression (E.5).
crit,i
b⋅v
Re(v )= crit,i (E.5)
crit,i ν
où
b est le diamètre extérieur du cylindre à base circulaire
ν est la viscosité cinématique de l'air (ν ≈ 15.10-6 m2/s)
v est la vitesse critique du vent, voir E.1.3.1
crit,i
120


EN 1991-1-4:2005 (F)
E.1.4 Action du détachement tourbillonnaire
(1) Il convient de calculer l'effet des vibrations dues au détachement tourbillonnaire à partir de l'effet de la force
d'inertie par unité de longueur F (s), qui agit perpendiculairement à la direction du vent à l'emplacement s sur la
w
construction et qui est donnée par l'expression (E.6).
F (s)=m(s)⋅(2⋅π⋅n )2⋅Φ (s)⋅y (E.6)
w i,y i,y F,max
où
m(s) est la masse en vibration de la construction par unité de longueur [kg/m]
n est la fréquence propre de la construction
i,y
Φ (s) est la déformée modale de la construction normalisée à 1 au point de déplacement maximal i,y
y est le déplacement maximal dans le temps au point où Φ (s) est égal à 1, voir E.1.5 F,max i,y
E.1.5 Calcul de l'amplitude perpendiculairement au vent
E.1.5.1 Généralités
(1) Deux méthodes différentes de calcul des amplitudes des vibrations perpendiculaires au vent, excitées par le
détachement tourbillonnaire sont définies en E.1.5.2 et E.1.5.3.
NOTE 1 Le choix de la méthode de calcul ou de méthodes de calcul alternatives peut être spécifié dans l'Annexe
Nationale.
NOTE 2 Il n'est pas possible d'effectuer une comparaison directe des méthodes proposées en E.1.5.2 et E.1.5.3 du
fait que certains paramètres d'entrée sont choisis pour des conditions environnementales différentes. L'Annexe
Nationale peut définir la plage d'application de chacune des méthodes proposées.
NOTE 3 Il n'est pas admis de mélanger les méthodes définies en E.1.5.2 et E.1.5.3, sauf stipulation spécifique dans
le texte.
(2) La méthode définie en E.1.5.2 peut être utilisée pour différents types de constructions et déformées modales.
Elle inclut les effets de la turbulence et de la rugosité, et peut être utilisée pour des conditions climatiques normales.
(3) La méthode définie en E.1.5.3 peut être utilisée pour calculer la réponse pour des vibrations selon le premier
mode de constructions en console dont les dimensions, perpendiculairement au vent, sont réparties régulièrement
le long de l’axe principal de la construction. Les constructions types couvertes sont les cheminées ou les mâts.
Cette méthode ne peut pas s'appliquer aux constructions disposées en groupe ou en ligne, et aux cylindres
assemblés (couplés). Cette méthode permet de prendre en considération différentes intensités de turbulence,
pouvant différer du fait des conditions météorologiques. Dans les régions susceptibles d'être soumises à des
conditions climatiques pouvant se révéler très froides et où des conditions d'écoulement stratifié peuvent se
produire (par exemple dans les zones côtières de l'Europe septentrionale), la méthode E.1.5.3 peut être utilisée.
NOTE L'Annexe Nationale peut mentionner les régions dans lesquelles des conditions de froid extrême et d'écoulement
stratifié peuvent se produire. Pour ce type de régions, la méthode 2 définie en E.1.5.3 convient davantage, et
l'Annexe Nationale peut définir les paramètres d'entrée appropriés (tels que K ou l'intensité de turbulence) qu'il convient
a
d'utiliser avec cette méthode.
121


EN 1991-1-4:2005 (F)
E.1.5.2  Méthode 1 pour le calcul des amplitudes perpendiculairement au vent
| E.1.5.2.1  | Calcul des déplacements  |     |     |     |
| ---------- | ------------------------ | --- | --- | --- |
Le plus grand déplacement y  peut être calculé à l'aide de l'expression (E.7).
F,max
y
| F,max | 1 1      |       |     |        |
| ----- | -------- | ----- | --- | ------ |
|       | = ⋅ ⋅K⋅K | ⋅C    |     | (E.7)  |
|       | b St2 Sc | w lat |     |        |
où
| St  | est le nombre de Strouhal donné dans le Tableau E.1  |     |     |     |
| --- | ---------------------------------------------------- | --- | --- | --- |
| Sc  | est le nombre de Scruton donné en E.1.3.3            |     |     |     |
K w   est le facteur de longueur de corrélation effective donné en E.1.5.2.4
| K   | est le facteur de déformée modale donné en E.1.5.2.5              |     |     |     |
| --- | ----------------------------------------------------------------- | --- | --- | --- |
| c   |   est le coefficient de force latérale donné dans le Tableau E.2  |     |     |     |
lat
NOTE  Les forces aéroélastiques sont prises en compte par le facteur de longueur de corrélation effective K .
w
| E.1.5.2.2  | Coefficient de force latérale c |     |     |     |
| ---------- | ------------------------------- | --- | --- | --- |
lat
(1)  La valeur de base c  du coefficient de force latérale est donnée dans le Tableau E.2.
lat,0
122

EN 1991-1-4:2005 (F)
Tableau E.2 — Valeur de base du coefficient de force latérale c  pour différentes
lat,0
sections transversales
Section transversale  c
lat,0
donné à la

Figure E.2

| pour tous les nombres de Reynolds (Re)  |     |      |
| --------------------------------------- | --- | ---- |
|                                         |     | 1,1  |

| 0,5 ≤ d/b ≤ 10  |     |     |
| --------------- | --- | --- |
d/b = 1
0,8
|     | d/b = 1,5  | 1,2  |
| --- | ---------- | ---- |
|     | d/b = 2  | 0,3  |
| --- | -------- | ---- |

| interpolation linéaire  |          |      |
| ----------------------- | -------- | ---- |
|                         | d/b = 1  | 1,6  |
|                         | d/b = 2  | 2,3  |

| interpolation linéaire  |          |      |
| ----------------------- | -------- | ---- |
|                         | d/b = 1  | 1,4  |
d/b = 2
1,1

| interpolation linéaire  |            |      |
| ----------------------- | ---------- | ---- |
|                         | d/b = 1,3  | 0,8  |
|                         | d/b = 2,0  | 1,0  |

| interpolation linéaire  |     |     |
| ----------------------- | --- | --- |
NOTE  Les extrapolations du coefficient de force latérale en fonction de d/b ne
sont pas admises.
123

EN 1991-1-4:2005 (F)
Figure E.2 — Valeur de base du coefficient de force latérale c en fonction du nombre de
lat,0
Reynolds Re(v ) pour les cylindres à base circulaire,
crit,i
voir E.1.3.4
(2) Le coefficient de force latérale c est donné dans le Tableau E.3.
lat
Tableau E.3 — Coefficient de force latérale c en fonction du rapport lat
de vitesse critique v / v
crit,i i m,Lj
Rapport de vitesse critique c lat
v
crit,i ≤0,83 c = c
lat lat,0
v
m,Lj
v  v 
0,83≤ crit,i ≤1,25 c =3−2,4⋅ crit,i ⋅c
v m,Lj lat   v m,Lj   lat,0
v
1,25≤ crit,i c = 0 lat
v
m,Lj
où
c est la valeur de base de c telle que donnée dans le Tableau E.2 et, pour les cylindres
lat,0 lat
à base circulaire, à la Figure E.2
v vitesse critique du vent (voir expression (E.1))
crit,i
v vitesse moyenne du vent (voir 4.2) au centre de la longueur de corrélation effective telle
m,Lj
que définie à la Figure E.3
E.1.5.2.3 Longueur de corrélation L
(1) Il convient de positionner la longueur de corrélation L, dans les zones de ventres du mode. Des exemples
j
sont donnés à la Figure E.3. Des recommandations spéciales se révèlent nécessaires pour les mâts haubanés et
les ponts à travées multiples continues.
124


EN 1991-1-4:2005 (F)

NOTE  Lorsque deux longueurs de corrélation au moins sont indiquées, elles peuvent être utilisées en toute sécurité de
manière simultanée, et il convient d'employer la valeur la plus élevée de c .
lat
Figure E.3 — Exemples d'application de la longueur de corrélation L ( j  = 1, 2, 3)
j
Tableau E.4 — Longueur de corrélation effective L
j
| en fonction de l'amplitude de vibration y |     | (s)  |
| ----------------------------------------- | --- | ---- |
F j
| y (s) / b  | L / b  |      |
| ---------- | ------ | ---- |
| F j        | j      |      |
| < 0,1      | 6      |      |
|            | y      | (S ) |
F j
| 0,1 à 0,6  | 4,8+12⋅ |     |
| ---------- | ------- | --- |
b
| > 0,6  | 12  |     |
| ------ | --- | --- |
125

EN 1991-1-4:2005 (F)
E.1.5.2.4 Facteur de longueur de corrélation effective K
w
(1) Le facteur de longueur de corrélation effective, K , est donné dans l'expression (E.8) suivante :
w
n
∑∫
Φ (s) ds
i,y
k =
j=1Lj
≤0,6 (E.8)
w n
∑∫
Φ (s) ds
i,y
j=1
j
où
Φ est la déformée modale i (voir F.3)
i,y
L est la longueur de corrélation
j
 est la longueur de la construction entre deux nœuds (voir Figure E.3) ; pour les constructions en
j
console, elle est égale à la hauteur de la construction
n est le nombre de régions où se produit l'excitation par détachement tourbillonnaire simultanément (voir
Figure E.3)
m est le nombre de ventres de la construction en vibration, dans la déformée modale considérée Φ i,y
s est la coordonnée définie dans le Tableau E.5
(2) Pour certaines constructions simples vibrant selon le mode fondamental perpendiculaire au vent et avec la
force d'excitation indiquée dans le Tableau E.5, le facteur de longueur de corrélation effective K peut être calculé w
de manière approchée par les expressions données dans le Tableau E.5.
126


EN 1991-1-4:2005 (F)
Tableau E.5 — Facteur de longueur de corrélation K  et facteur de déformée modale K
w
pour certaines constructions simples
déformée modale
| Construction  |         |     |     | K   |     |     | K   |
| ------------- | ------- | --- | --- | --- | --- | --- | --- |
|               | Φ  (s)  |     |     |     | w   |     |     |
i,y
|     | voir F.3       |     |     |      |      | 2    |       |
| --- | -------------- | --- | ---- | ---- | ---- | ----- | ----- |
|     |                | L   | /b   | L /b | L   | /b   |       |
|     |                |     | j   | j    | 1    | j    |       |
|     | avec ζ = 2,0   | 3⋅  | ⋅ 1− | +    | ⋅  |     | 0,13  |
|     |                |     | λ   | λ    | 3    | λ    |       |
|     |                |     |      |      |     |      |       |
|     | n = 1 ; m = 1  |     |     |      |      |      |       |

|     |                   |      |     | L /b |     |     |       |
| --- | ----------------- | ---- | ----- | ------ | --- | --- | ----- |
|     | voir Tableau F.1  |      | π     | j      |     |     |       |
|     |                   | cos | ⋅ 1− |       |    |     | 0,10  |
|     |                   |      |      |       |     |     |       |
|     | n = 1 ; m = 1     |      | 2  | λ   |     |     |       |
|     |     | Lj b | 1   |   | Lj  | b |     |
| --- | --- | ---- | --- | --- | --- | --- | --- |
voir Tableau F.1
|     |                |     | +π ⋅s i-n | ⋅1 |     |   | 0,11  |
| --- | -------------- | --- | ---------- | --- | --- | --- | ----- |
|     | n = 1 ; m = 1  | λ   | π          |   | λ   |  |       |


n
|     |                 |     | ∑ ∫ ϕ | (s) | ds  |     |     |
| --- | --------------- | --- | ----- | --- | --- | --- | --- |
|     | analyse modale  |     | i,y   |     |     |     |     |
i=1 Lj
|     | n = 3  |     |     |     |     |     | 0,10  |
| --- | ------ | --- | --- | --- | --- | --- | ----- |
n
|     | m = 3  |     | ∑ ∫ ϕ | (s) | ds  |     |     |
| --- | ------ | --- | ----- | --- | --- | --- | --- |
i,y
j=1 
j

NOTE 1  La déformée modale, Φ (s), est celle indiquée en F.3. Les paramètres n et m sont définis dans
i,y
l'expression (E.7) et à la Figure E.3.
NOTE 2  λ =  / b.
127

EN 1991-1-4:2005 (F)
E.1.5.2.5  Facteur de déformée modale
(1)  Le facteur de déformée modale K est donné dans l'expression (E.9).
m
| ∑   | ∫Φ  |     |     |     |
| --- | --- | --- | --- | --- |
(s) ds
i,y
| j=1 |    |       |     |        |
| --- | --- | ----- | --- | ------ |
| K = | j   | ≤0,6  |     | (E.9)  |
m
| 4⋅π⋅ | ∑ ∫Φ2 (s)ds |     |     |     |
| ---- | ----------- | --- | --- | --- |
i,y
j=1 
j
où
| m   | est défini en E.1.5.2.4 (1)  |     |     |     |
| --- | ---------------------------- | --- | --- | --- |
| Φ (s)  | est la déformée du mode i perpendiculaire au vent (voir F.3)  |     |     |     |
| ------ | ------------------------------------------------------------- | --- | --- | --- |
i,y
  est la longueur de la construction entre deux nœuds (voir Figure E.3)
j
(2)  Pour certaines constructions simples vibrant selon le mode fondamental perpendiculaire au vent, le facteur de
déformée modale est donné dans le Tableau E.5.
E.1.5.2.6  Nombre de cycles de chargement
(1)  Le nombre de cycles de chargement N dû à une oscillation excitée par détachement tourbillonnaire est donné
par l'expression (E.10) suivante :
|          |       | 2      | 2      |         |
| -------- | ----- | ------- | ------- | ------- |
|          | v    |  v    |        |         |
|          | crit  | ⋅exp− | crit   |         |
| N =2⋅T⋅n | ⋅ε ⋅ |        |        | (E.10)  |
|          | v 0 v |        | v      |         |
|          |  0   |      | 0     |         |
où
n   est la fréquence propre du mode perpendiculaire au vent [Hz]. Des valeurs approchées de n  sont
| y   |     |     |     | y   |
| --- | --- | --- | --- | --- |
données à l'Annexe F
| v   | est la vitesse critique du vent [m/s] donnée en E.1.3.1  |     |     |     |
| --- | -------------------------------------------------------- | --- | --- | --- |
crit
v   est égale à  2 fois la valeur modale de la distribution statistique (loi de Weibull) de la vitesse du
0
vent [m/s] ; voir Note 2
T  est la durée de vie en secondes, égale à 3,2 107 multiplié par la durée de vie prévue en années
ε  est le coefficient de largeur de bande qui décrit la bande des vitesses de vent dans laquelle
0
apparaissent les vibrations dues au détachement tourbillonnaire ; voir Note 3
L'Annexe Nationale peut spécifier la valeur minimale de N. La valeur recommandée est N ≥ 104.
NOTE 1
NOTE 2  La valeur v  peut être considérée comme étant égale à 20 % de la vitesse moyenne caractéristique du vent
0
telle que spécifiée en 4.3.1 (1) à la hauteur de la section transversale où se produit le détachement tourbillonnaire.
NOTE 3  Le coefficient de largeur de bande ε se situe dans l'intervalle  0,1 - 0,3. Il peut être considéré comme étant
0
égal à ε = 0,3.
0
128

EN 1991-1-4:2005 (F)
E.1.5.2.7  Résonance tourbillonnaire de cylindres verticaux disposés en ligne ou en groupe
(1)  Des vibrations dues à une excitation par le détachement tourbillonnaire peuvent se produire dans le cas des
cylindres à base circulaire disposés en ligne ou en groupe, avec ou sans couplage (voir Figure E.4).

Figure E.4 — Disposition de cylindres en ligne et en groupe
(2)  Les amplitudes maximales d'oscillation peuvent être exprimées au moyen de l'expression (E.7) et de la
procédure de calcul indiquée en E.1.5.2 avec les modifications données par les expressions (E.11) et (E.12).
-  Dans le cas des cylindres à base circulaire, en ligne, indépendants les uns des autres :
| c  = 1,5 . c |             | pour 1≤ | ≤10  |     |     |
| ------------ | ----------- | ------- | ---- | --- | --- |
| lat          | lat(single) |         |      |     |     |
b
a
| c lat  = c lat(single) |     | pour  | ≤15  |     |     |
| ---------------------- | --- | ----- | ---- | --- | --- |
b
a
| Interpolation linéaire  |     | pour 10≤ | ≤15  |     | (E.11)  |
| ----------------------- | --- | -------- | ---- | --- | ------- |
b
|                    | a |         | a   |     |     |
| ------------------ | --- | ------- | --- | --- | --- |
| St =0,1+0,085⋅log |    | pour 1≤ | ≤9  |     |     |
|                    | b |         | b   |     |     |
a
| St = 0,18  |     | pour  | >9  |     |     |
| ---------- | --- | ----- | --- | --- | --- |
b
où
| c  = c  tel qu'indiqué dans le Tableau E.3.  |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- |
lat(single) lat
-  Pour les cylindres assemblés (reliés entre eux) :
| c  = K  . c |       pour   1,0 ≤ a/b ≤ 3,0  |     |     |     | (E.12)  |
| ----------- | ----------------------------- | --- | --- | --- | ------- |
| lat iv      | lat(single)                   |     |     |     |         |
où
K   est le facteur d'interférence applicable au détachement tourbillonnaire (Tableau E.8)
iv
St  est le nombre de Strouhal donné dans le Tableau E.8
Sc  est le nombre de Scruton donné dans le Tableau E.8
Pour les cylindres assemblés avec a/d > 3,0, il est recommandé de consulter un spécialiste.
NOTE  Le coefficient 1,5 ⋅ c  pour les cylindres à base circulaire indépendants les uns des autres, est une valeur
lat
approximative. Il est supposé traduire une certaine prudence.
129

EN 1991-1-4:2005 (F)
E.1.5.3  Méthode 2 pour le calcul des amplitudes perpendiculairement au vent
(1)  Le  déplacement  maximal  caractéristique,  au  point  de  plus  grand  déplacement,  est  donné  par
l'expression (E.13).
 = σ . k
| y     |     |     |     |     | (E.13)  |
| ----- | --- | --- | --- | --- | ------- |
| max y | p   |     |     |     |         |
où
σ  est l'écart type du déplacement ; voir (2)
y
k   est le facteur de pointe ; voir (6)
p
(2)  L'écart type σ du déplacement rapporté à la largeur b, au point de plus grand déplacement (Φ = 1) peut être
y
| σ   |     |     | ρ⋅b2 |     |         |
| --- | --- | --- | ---- | --- | ------- |
| y 1 |     | C   |      | b   |         |
| =   | ⋅   | c   | ⋅    | ⋅   | (E.14)  |
St2
| b   |     |          | 2 m | h   |     |
| --- | --- | --------- | ---- | --- | --- |
|     | Sc  |  σ       |  e  |     |     |
|     | −K  | ⋅1− y   |     |     |     |
|     |     | a         |     |     |     |
|     | 4⋅π |  b⋅a L |     |     |     |
|     |     |          |     |     |     |
où
C   est la constante aérodynamique dépendant de la forme de section transversale, ainsi que, pour un
c
cylindre à base circulaire, du nombre de Reynolds Re défini en E.1.3.4 (1) ; elle est donnée dans le
Tableau E.6
K a   est le paramètre d'amortissement aérodynamique donné en E.1.5.3 (4)
a   est l'amplitude de limitation normalisée donnant le déplacement des constructions très faiblement
L
amorties; elle est donnée dans le Tableau E.6
| St  | est le nombre de Strouhal donné en E.1.6.2  |     |     |     |     |
| --- | ------------------------------------------- | --- | --- | --- | --- |
ρ  est la masse volumique de l'air dans les conditions de détachement tourbillonnaire ; voir Note 1
m   est la masse effective par unité de longueur ; elle est donnée en F.4 (1)
e
h,b  sont respectivement la hauteur et la largeur de la construction. Dans le cas des constructions à
largeur  variable,  la  largeur  à  utiliser  est  celle  au  point  présentant  les  déplacements  les  plus
importants
La valeur de la masse volumique ρ  peut être donnée dans l'Annexe Nationale. La valeur recommandée
NOTE 1
est 1,25 kg/m3.
NOTE 2  La constante aérodynamique C  dépend de la force de portance qui agit sur une construction ne se
c
déplaçant pas.
NOTE 3  Les charges du vent dues au mouvement sont prises en compte par K  et a .
a L
130

EN 1991-1-4:2005 (F)
(3)  La solution de l'équation (E.14) est donnée dans l'expression (E.15).
2
σ 
| y   |        | c2   |     |     |     |     |     |     |     |         |
| --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | ------- |
|    |  =c + | +c   |     |     |     |     |     |     |     | (E.15)  |
|  b |  1    | 1 2  |     |     |     |     |     |     |     |         |
 
| où les constantes c |      |  et c  sont données par :  |     |      |       |     |     |     |     |         |
| ------------------- | ---- | -------------------------- | --- | ---- | ----- | --- | --- | --- | --- | ------- |
|                     |      | 1 2                        |     |      |       |     |     |     |     |         |
|                     | a2  |                           |     | ρ⋅b2 | a2 C2 |     |     |     |     |         |
|                     | L    | Sc                         |     |      |       | b   |     |     |     |         |
| c =                 | ⋅1− |    ;   c                  |     | = ⋅  | L ⋅ c | ⋅   |     |     |     | (E.16)  |
| 1                   | 2    | 4⋅π⋅K                      | 2   | m    | K St4 | h   |     |     |     |         |
|                     |     | a                         |     | e    | a     |     |     |     |     |         |
(4)  La constante d'amortissement aérodynamique K  diminue avec l'augmentation de l'intensité de turbulence.
a
Pour une intensité de turbulence de 0 %, la constante d'amortissement peut être considérée égale à K a  = K a,max ,
qui est donnée dans le Tableau E.6.
NOTE  L’utilisation de K a,max pour des intensités de turbulence supérieures à 0 % conduit à des estimations prudentes
des déplacements. Des informations plus détaillées concernant l'influence de l'intensité de turbulence sur K a  peuvent
être spécifiées dans l'Annexe Nationale.
(5)  Les constantes C , K et a  applicables à un cylindre à base circulaire et à une section transversale carrée
|     |     | c a,max  |     | L   |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
sont données dans le Tableau E.6.
Tableau E.6 — Constantes pour la détermination de l'effet du détachement tourbillonnaire
|     |     | Cylindre à base  |     |     | Cylindre à base  |     | Cylindre à base  |     | Section  |     |
| --- | --- | ---------------- | --- | --- | ---------------- | --- | ---------------- | --- | -------- | --- |
Constante  circulaire Re ≤ 105  circulaire Re = 5.105  circulaire Re ≥ 106  transversale
carrée
|     | C   |     | 0,02  |     |     | 0,005  |     | 0,01  | 0,04  |     |
| --- | --- | --- | ----- | --- | --- | ------ | --- | ----- | ----- | --- |
c
|     | K   |     | 2   |     |     | 0,5  |     | 1   | 6   |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
a,max
|     | a   |     | 0,4  |     |     | 0,4  |     | 0,4  | 0,4  |     |
| --- | --- | --- | ---- | --- | --- | ---- | --- | ---- | ---- | --- |
L
NOTE  Dans le cas des cylindres à base circulaire, les constantes C  et K a,max sont supposées
c
varier de manière linéaire avec le logarithme du nombre de Reynolds pour 105 < Re <5.105 et pour
5.105 < Re < 106, respectivement.
| (6)  Il convient de déterminer le facteur de pointe k |     |     |     |     |     | .   |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
p
NOTE  L'Annexe Nationale peut spécifier le facteur de pointe. L'expression (E.17) donne la valeur recommandée.
|     |    |     |     |    |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |    |     |     |    |     |     |     |     |     |     |
1,2
| =   | 2⋅  1+ |     |     |    |     |     |     |     |     |         |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- |
| k   |        |     |     |    |     |     |     |     |     | (E.17)  |
| p   |         |    | Sc  |    |     |     |     |     |     |         |
|     |        |     |     |   |     |     |     |     |     |         |
tan0,75⋅
|     |    |     | (4⋅π⋅K |      |     |     |     |     |     |     |
| --- | --- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- |
|     |    |    |        | a   |     |     |     |     |     |     |
(7)  Le nombre de cycles de chargement peut être obtenu à partir de E.1.5.2.6 en utilisant un coefficient de largeur
de bande ε = 0,15.
0
131

EN 1991-1-4:2005 (F)
E.1.6 Mesures susceptibles de réduire les vibrations dues au détachement tourbillonnaire
(1) Les amplitudes dues au détachement tourbillonnaire peuvent être réduites au moyen de dispositifs
aérodynamiques (uniquement dans certaines conditions, par exemple nombres de Scruton supérieurs à 8) ou de
dispositifs d'amortissement mis en place sur la construction. Pour une construction de section transversale
circulaire et équipée de dispositifs aérodynamiques, le coefficient de traînée c fondé sur le diamètre initial b, peut
f
augmenter jusqu'à une valeur de 1,4. Ces applications nécessitent le recours à des spécialistes.
(2) Pour de plus amples informations, se reporter aux codes applicables aux constructions spéciales.

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_D_valeurs-cscd]] · [[EC1-1-4_Eb_galop-divergence-flottement]] · [[_Knowledge — Index]] · [[CLAUDE]]
