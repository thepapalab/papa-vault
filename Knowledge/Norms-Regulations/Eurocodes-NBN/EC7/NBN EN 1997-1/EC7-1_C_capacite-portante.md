---
title: "NBN EN 1997-1:2004 — Annexe C (informative) — Capacité portante fondations superficielles"
type: norm-extract
source: "NBN EN 1997-1:2004 (EN 1997-1:2004+AC:2009) — Eurocode 7: Calcul géotechnique, Partie 1: Règles générales, édition française"
norm: EC7-1
section: "C"
chapter: "Annexe C (informative, révisée AC:2009) — Exemples de procédures de détermination de la pression des terres"
tags: [EC7-1, eurocode-7, geotechnique, pression-terres, capacite-portante, fondations-superficielles]
related: ["[[EC7-1_index]]", "[[EC7-1_B_facteurs-partiels-notes]]", "[[EC7-1_D_tassement-oedometre]]", "[[_Knowledge — Index]]"]]", "[[EC7-1_B_facteurs-partiels-notes]]", "[[EC7-1_D_tassement-oedometre]]", "[[EC7-1_6_fondations-superficielles]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# NBN EN 1997-1:2004 — Annexe C (informative) — Capacité portante fondations superficielles

> *Annexe informative*

> [!note] Version AC:2009
> Cette annexe remplace intégralement l'annexe C originale conformément au corrigendum EN 1997-1:2004/AC:2009.

## Annexe C (informative) — Exemple de procédures de détermination de la pression des terres

### C.1 Valeurs limites de la pression des terres

(1) Il convient de calculer suivant les équations suivantes les valeurs limites de la pression des terres sur un écran vertical dans le cas d'un sol de masse volumique ($\gamma$), d'angle de frottement ($\phi$) et de cohésion ($c$) ainsi que dans le cas d'une surcharge verticale uniforme sur la surface à l'arrière de l'écran ($q$) :

— état limite de poussée :

$$\sigma_a(z) = K_a \left[ \int \gamma \, dz + q - u \right] + u - c \, K_{ac} \tag{C.1}$$

où l'intégration est réalisée depuis la surface du terrain jusqu'à la profondeur $z$

$$K_{ac} = 2\sqrt{K_a(1+a/c)}, \text{ limité à } 2{,}56\sqrt{K_a}$$

— état limite de butée :

$$\sigma_p(z) = K_p \left[ \int \gamma \, dz + q - u \right] + u + c \, K_{pc} \tag{C.2}$$

où l'intégration est réalisée depuis la surface du terrain jusqu'à la profondeur $z$

$$K_{pc} = 2\sqrt{K_p(1+a/c)}, \text{ limité à } 2{,}56\sqrt{K_p}$$

où :

- $a$ est l'inclinaison des contraintes (entre le terrain et le mur)
- $c$ est la cohésion
- $K_a$ est le coefficient de poussée horizontale des terres
- $K_p$ est le coefficient de butée horizontale des terres
- $q$ est la charge verticale appliquée en surface
- $z$ est la distance verticale le long de la surface de l'écran
- $\beta$ est l'angle de la pente du terrain derrière le mur (positif vers le haut)
- $\delta$ est l'angle de frottement entre le terrain et le mur
- $\gamma$ est le poids volumique du terrain soutenu
- $\sigma_a(z)$ est la contrainte totale normale à l'écran (état limite de poussée)
- $\sigma_p(z)$ est la contrainte totale normale à l'écran (état limite de butée)

(2) Pour un sol en condition drainée, $K_a$ et $K_p$ sont des fonctions de l'angle de frottement $\phi'$ et de la cohésion effective $c = c'$. Pour un sol en condition non drainée, $K_a = K_p = 1$ et la cohésion non drainée vaut $c = c_u$.

(3) Il convient d'extraire les valeurs des coefficients de pression des terres des Figures C.1.1 à C.1.4 pour $K_a$ et C.2.1 à C.2.4 pour $K_p$.

(4) De manière alternative, il convient d'utiliser la procédure analytique décrite en C.2.

(5) Dans les sols stratifiés, il est normalement considéré que les coefficients $K$ sont déterminés en fonction des paramètres de cisaillement à la profondeur $z$ seulement, indépendamment des valeurs aux autres profondeurs.

*Figure C.1.1 — Coefficients de poussée effective $K_a$ (composante horizontale) dans le cas d'un remblai à surface horizontale derrière l'écran ($\beta = 0$)*

*Figure C.1.2 — Coefficients de poussée effective $K_a$ (composante horizontale) dans le cas d'un remblai à surface inclinée de $\beta$ derrière l'écran ($\delta/\phi' = 0$ et $\delta = 0$)*

*Figure C.1.3 — Coefficients de poussée effective $K_a$ (composante horizontale) dans le cas d'un remblai à surface inclinée de $\beta$ derrière l'écran ($\delta/\phi' = 0{,}66$)*

*Figure C.1.4 — Coefficients de poussée effective $K_a$ (composante horizontale) dans le cas d'un remblai à surface inclinée de $\beta$ derrière l'écran ($\delta/\phi' = 1$)*

*Figure C.2.1 — Coefficients de butée effective $K_p$ (composante horizontale) dans le cas d'un remblai à surface horizontale derrière l'écran ($\beta = 0$)*

*Figure C.2.2 — Coefficients de butée effective $K_p$ (composante horizontale) dans le cas d'un remblai à surface inclinée de $\beta$ derrière l'écran ($\delta/\phi' = 0$ et $\delta = 0$)*

*Figure C.2.3 — Coefficients de butée effective $K_p$ (composante horizontale) dans le cas d'un remblai à surface inclinée de $\beta$ derrière l'écran ($\delta/\phi' = 0{,}66$)*

*Figure C.2.4 — Coefficients de butée effective $K_p$ (composante horizontale) dans le cas d'un remblai à surface inclinée de $\beta$ derrière l'écran ($\delta/\phi' = 1$)*

### C.2 Procédure analytique pour déterminer les états limites de poussée et de butée

(1) La procédure suivante qui inclut certaines approximations peut être utilisée dans tous les cas.

(2) La procédure est formulée pour les pressions de butée avec des paramètres de résistance (notés dans ce qui suit $\phi$, $c$, $\delta$, $a$) à valeurs positives, voir Figure C.3.

(3) Pour les pressions de poussée, le même procédure est utilisée avec les changements suivants :

- les paramètres de résistance $\phi$, $c$, $\delta$ et $a$ sont à valeurs négatives ;
- la valeur de l'angle d'incidence de la charge surfacique équivalente $\beta$ est $\beta$, principalement du fait des approximations faites pour l'estimation de $K_\gamma$.

(4) Les symboles suivants sont utilisés (en plus de ceux de l'article 1.6) :

- $a$ est l'adhésion (homogène à une contrainte) entre l'écran et le terrain
- $c$ est la cohésion
- $K_c$ est le coefficient pour la cohésion
- $K_n$ est le coefficient pour le chargement perpendiculaire à la surface du terrain
- $K_q$ est le coefficient vertical pour le chargement vertical
- $K_\gamma$ est le coefficient pour le poids du sol
- $m_t$ est l'angle entre la ligne de glissement du volume de sol retenu par l'écran et la surface du terrain en arrière de l'écran, il est compté positivement suivant les conventions de la figure C.3
- $m_w$ est l'angle entre la normale du parement en arrière de l'écran et la ligne de glissement du volume de sol retenu par l'écran, il est compté positivement suivant les conventions de la figure C.3
- $\beta$ est l'angle de la pente de la surface inclinée en arrière de l'écran, il est compté positivement suivant les conventions de la figure C.3
- $\delta$ est l'obliquité de la contrainte de poussée ou de butée par rapport à la normale à l'écran, elle est comptée positivement pour un état de butée selon les conventions de la figure C.3
- $\phi$ est l'angle de frottement interne
- $\theta$ est l'angle entre la verticale et le parement en arrière de l'écran, il est compté positivement quand le sol surplombe le mur
- $\nu$ est la rotation tangente le long d'une ligne de glissement extérieur, elle est positive quand la masse de sol située au-dessus de cette ligne présente une forme convexe
- $q$ est la surcharge uniforme par unité de surface sur la surface en arrière de l'écran
- $p$ est la surcharge uniforme par unité de surface projetée sur un plan horizontal

*Figure C.3 — Définitions concernant l'inclination d'un ouvrage de soutènement et du remblai, les surcharges et la géométrie des lignes de glissement*

(5) Les paramètres d'interface $\delta$ et $a$ doivent être choisis tels que :

$$\frac{a}{c} = \frac{\tan\delta}{\tan\phi}$$

(6) La condition limite à la surface du sol nécessite la détermination de $\beta$, qui est l'angle d'incidence d'une charge surfacique équivalente. Selon ce concept, l'angle est défini comme la somme vectorielle de deux termes :

- la charge surfacique actuelle $q$, uniforme mais pas nécessairement verticale, et ;
- $c \cot\phi$ agissant comme une charge normale.

L'angle $\beta$ est positif quand la composante tangentielle de $q$ est dirigée vers le mur tandis que la composante normale est dirigée vers le sol. Si $c = 0$ et si la charge surfacique est verticale ou nulle, pour des pressions de poussée en général, $\beta = \beta$.

(7) L'angle $m_t$ est déterminé par la condition limite à la surface du sol :

$$\cos(2m_t + \phi + \beta_0) = -\frac{\sin\beta_0}{\sin\phi} \tag{C.3}$$

(8) La condition limite au niveau de l'écran détermine $m_w$ :

$$\cos(2m_w + \phi + \delta) = \frac{\sin\delta}{\sin\phi} \tag{C.4}$$

L'angle $m_w$ est négatif pour des pressions de butée ($\phi > 0$) si le rapport $\sin\delta / \sin\phi$ est suffisamment grand.

(9) La rotation tangente totale le long de la ligne de glissement de la masse de sol en mouvement est déterminée par l'angle $\nu$ calculé selon l'expression suivante :

$$\nu = m_t + \beta - m_w - \theta \tag{C.5}$$

(10) Le coefficient $K_n$ pour une charge normale à la surface du terrain (i.e. la pression de terres normale à l'écran déduite d'une pression normale à la surface du terrain) est alors déterminé par l'expression suivante dans laquelle $\nu$ est en radians :

$$K_n = \frac{1 + \sin\phi\sin(2m_w + \phi)}{1 - \sin\phi\sin(2m_t + \phi)} \exp(2\nu\tan\phi) \tag{C.6}$$

(11) Le coefficient pour une charge verticale sur la surface (projeté dans un plan horizontal) est :

$$K_q = K_n \cos\beta \tag{C.7}$$

et le coefficient pour le terme de cohésion est :

$$K_c = (K_n - 1)\cot\phi \tag{C.8}$$

(12) Pour un sol pesant, une expression approchée est :

$$K_\gamma = K_n \cos\beta \cos(\beta - \theta) \tag{C.9}$$

Cette expression est conservative. Tandis que l'erreur est négligeable pour des états de poussée, elle peut être importante pour des états de butée où les valeurs de $\beta$ sont positives.

Pour $\phi = 0$, les valeurs limites suivantes sont :

$$\cos 2m_t = -\frac{\sin\beta_0}{\cos\beta_0}; \quad \cos 2m_w = \frac{a}{c}; \quad K_q = \cos\beta;$$

$$K_c = 2\nu + \sin 2m_t + \sin 2m_w$$

(avec $\nu$ en radians), et pour $K_\gamma$ ($\phi = 0$), une meilleure approximation est :

$$K_\gamma = \cos\theta + \frac{\sin\beta \cos m_w}{\sin m_t} \tag{C.10}$$

(13) À la fois pour des pressions correspondant à des états de butée et de poussée, la procédure suppose que l'angle de convexité est positif ($\nu \geq 0$).

(14) Si la condition n'est pas remplie (même approximativement), par exemple, pour un mur lisse et une pente de terrain suffisante quand $\beta$ et $\phi$ ont des signes opposés, il doit être considéré d'autres méthodes. Cette situation est rencontrée quand la surface du terrain à l'arrière du mur est irrégulière.

### C.3 Mouvements nécessaires pour mobiliser les pressions des terres

(1) Il est d'usage de tenir compte de la relation entre la pression des terres et le mouvement de l'écran pour les états de poussée. L'importance de ce mouvement dépend du type de mouvement de l'écran, de l'état initial des pressions des terres et de la densité du sol. Supposant un état initial des contraintes avec $K_o < 1$, le tableau C.1 fournit des estimations du rapport $v_a/h$ pour des pressions effectives de poussée des terres entièrement mobilisées dans le cas d'un écran vertical avec un sol drainé non cohésif et une surface du terrain horizontale.

(2) Il est d'usage de tenir compte de la relation entre la pression des terres et le mouvement de l'écran pour les états de butée. L'importance de ce mouvement dépend du type de mouvement de l'écran, de l'état initial des pressions des terres et de la densité du sol. Supposant un état initial des contraintes avec $K_o < 1$, le tableau C.2 fournit des estimations du rapport $v_p/h$ pour des pressions effectives de butée des terres entièrement mobilisées dans le cas d'un écran vertical avec un sol drainé non cohésif et une surface du terrain horizontale. Les valeurs des rapports $v/h$ entre parenthèses correspondent aux valeurs limites des pressions effectives de butée des terres diminuées de moitié.

(3) Des valeurs intermédiaires de la pression effective des terres entre l'état limite et l'état de pression des terres au repos peuvent être obtenues par une interpolation linéaire.

(4) Pour les états limites de butée, les valeurs peuvent être interpolées à partir de celles fournies dans le tableau C.2 en utilisant une courbe dont l'allure générale est précisée sur la figure C.4.

**Table C.1 — Rapports $v_a/h$ pour des sols non cohésifs**

| **Type de mouvement de l'écran** | **$v_a/h$ sol lâche (%)** | **$v_a/h$ sol dense (%)** |
|---|---:|---:|
| a) | 0,4 à 0,5 | 0,1 à 0,2 |
| b) | 0,2 | 0,05 à 0,1 |
| c) | 0,8 à 1,0 | 0,2 à 0,5 |
| d) | 0,4 à 0,5 | 0,1 à 0,2 |

où :
- $v_a$ est le mouvement de l'écran pour mobiliser l'état de poussée
- $h$ est la hauteur de l'écran

**Table C.2 — Rapports $v_p/h$ et $v/h$ pour $0{,}5\sigma_p$ dans le cas de sols non cohésifs**

| **Type de mouvement de l'écran** | **$v_p/h$ ($v/h$ pour $0{,}5\sigma_p$) sol lâche (%)** | **$v_p/h$ ($v/h$ pour $0{,}5\sigma_p$) sol dense (%)** |
|---|---|---|
| a) | 7 (1,5) à 25 (4,0) | 5 (1,1) à 10 (2,0) |
| b) | 5 (0,9) à 10 (1,5) | 3 (0,5) à 6 (1,0) |
| c) | 6 (1,0) à 15 (1,5) | 5 (0,5) à 6 (1,3) |

où :
- $v$ est le déplacement de l'écran
- $v_p$ est le déplacement de l'écran pour mobiliser la pression de butée des terres
- $h$ est la hauteur de l'écran
- $\sigma_p$ est la pression maximale de pression de butée des terres

*Figure C.4 — Mobilisation de la pression effective de butée des terres pour un sol non cohésif en fonction du déplacement normalisé $v/v_p$ de l'écran*
*($v$ : déplacement ; $v_p$ : déplacement pour la mobilisation complète de la pression de butée des terres)*

---

Liens : [[EC7-1_index]] · [[EC7-1_B_facteurs-partiels-notes]] · [[EC7-1_D_tassement-oedometre]] · [[_Knowledge — Index]] · [[CLAUDE]]
