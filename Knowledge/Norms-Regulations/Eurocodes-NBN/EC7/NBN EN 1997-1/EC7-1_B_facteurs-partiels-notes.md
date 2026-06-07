
title: "NBN EN 1997-1:2004 — Annexe B (informative) — Commentaires sur les facteurs partiels"
type: norm-extract
source: "NBN EN 1997-1:2004 (EN 1997-1:2004+AC:2009) — Eurocode 7: Calcul géotechnique, Partie 1: Règles générales, édition française"
norm: EC7-1
section: "B"
chapter: "Annexe B (informative) — Commentaires sur les facteurs partiels"
tags: [EC7-1, eurocode-7, geotechnique, facteurs-partiels, approches-calcul, DA1, DA2, DA3]
related: ["[[EC7-1_index]]", "[[EC7-1_A_facteurs-partiels]]", "[[EC7-1_C_capacite-portante]]", "[[_Knowledge — Index]]"]]", "[[EC7-1_A_facteurs-partiels]]", "[[EC7-1_C_capacite-portante]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# NBN EN 1997-1:2004 — Annexe B (informative) — Commentaires sur les facteurs partiels

> *Annexe informative*

## Annexe B (informative) — Commentaires sur les facteurs partiels des approches de calcul 1, 2 et 3

### B.1 Généralités

(1) Pour les états limites de type STR et GEO, dans les situations permanentes et transitoires, trois approches de calcul ont été décrites dans 2.4.7.3.4. Elles diffèrent par la façon dont elles distribuent les facteurs partiels entre les actions, les effets des actions, les propriétés des matériaux et les résistances. Ceci est dû pour partie à des approches différentes de la prise en compte des incertitudes dans la modélisation des effets des actions et des résistances.

(2) Dans l'approche de calcul 1, pour tous les calculs, les vérifications sont en principe exigées pour deux ensembles de facteurs, appliqués dans deux calculs séparés. Lorsqu'il est évident que l'un de ces ensembles gouverne le calcul, il n'est pas nécessaire d'exécuter les calculs de l'autre ensemble. En général, les facteurs sont appliqués aux actions, plutôt qu'aux effets des actions, à une exception notable (alinéa 2.4.7.3.4.2(2)). Dans beaucoup de cas, les facteurs sont appliqués aux paramètres du terrain mais, pour le calcul des pieux et des ancrages, ils sont appliqués aux résistances.

(3) Dans les approches de calcul 2 et 3, un calcul unique est exigé pour chaque partie du projet, et la façon dont les facteurs sont appliqués varie suivant le calcul considéré.

(4) Dans l'approche de calcul 2, les facteurs sont appliqués d'une part aux actions ou aux effets des actions et, d'autre part, aux résistances.

(5) Dans l'approche de calcul 3, les facteurs sont appliqués d'une part aux actions ou aux effets des actions provenant de la structure et, d'autre part, aux paramètres de résistance du terrain (paramètres des matériaux).

### B.2 Facteurs pour les actions et les effets des actions

(1) La norme EN 1990:2002 indique que $\gamma_f$ est un facteur partiel pour une action et qu'il tient compte de la possibilité de déviations défavorables par rapport à sa valeur caractéristique. De la même façon, $\gamma_{S;d}$ est un facteur partiel qui tient compte des incertitudes de la modélisation des actions et de la modélisation des effets des actions.

(2) La norme EN 1990:2002 permet de combiner en un seul facteur $\gamma_F$ les facteurs partiels $\gamma_{S;d}$ et $\gamma_f$ :

$$\gamma_F = \gamma_{S;d} \cdot \gamma_f \tag{B.1}$$

(3) Les différentes approches de la norme EN 1997-1 exigent que les facteurs soient appliqués soit aux actions soit aux effets des actions. Comme l'utilisation de facteurs de modèle $\gamma_{S;d}$ pour les actions venant du sol va rester exceptionnelle et est pour cette raison laissée à l'appréciation nationale, $\gamma_F$ est utilisé partout, par simplicité, pour les actions et $\gamma_E$ pour les effets des actions dans le calcul géotechnique (voir annexe A, Tableaux A.1 et A.3). Ceci permet aux autorités nationales de sélectionner des valeurs alternatives de la combinaison $\gamma_{S;d} \cdot \gamma_f$.

(4) Les équations (2.6a) et (2.6b) incluent $X_k / \gamma_M$ dans le calcul des actions parce que les propriétés du matériau "terrain" peuvent affecter les valeurs des actions géotechniques dans certains cas.

(5) Dans l'approche de calcul 1, des vérifications sont exigées pour deux combinaisons d'ensembles de facteurs, appliqués dans deux calculs séparés.

Dans la combinaison 1, les facteurs différents de 1 sont généralement appliqués aux actions, avec des facteurs égaux à 1 pour les effets des actions. De ce fait, $\gamma_F \neq 1$ et $\gamma_E = 1$ sont appliqués dans l'équation (2.6).

Une exception à cette règle a été notée dans l'alinéa 2.4.7.3.2(2), dans les cas où il serait physiquement déraisonnable d'appliquer $\gamma_F \neq 1$ (par exemple, pour un réservoir à niveau de fluide fixe). On utilise alors $\gamma_F = 1$ et $\gamma_E \neq 1$.

Dans la combinaison 2, on utilise toujours $\gamma_E = 1$, et $\gamma_F \neq 1$ seulement pour les actions variables.

De ce fait, à part dans le cas noté en 2.4.7.3.2(2), les équations (2.6a) et (2.6b) s'appliquent sous la forme :

$$E_d = E\{\gamma_F \cdot F_{rep} ; X_k / \gamma_M ; a_d\} \tag{B.2}$$

(6) Dans l'approche de calcul 2, un calcul unique est demandé pour chaque partie du dimensionnement et la façon dont les facteurs sont appliqués soit aux actions, soit aux effets des actions, varie suivant le calcul considéré et est sujette à détermination nationale.

On applique les équations suivantes soit $\gamma_F \neq 1$ et $\gamma_E = 1$, soit $\gamma_F = 1$ et $\gamma_E \neq 1$. Comme $\gamma_M = 1$ est utilisé, les équations (2.6a) et (2.6b) se réduisent à :

$$E_d = \gamma_E \cdot E\{F_{rep} ; X_k ; a_d\} \tag{B.3.1}$$

ou :

$$E_d = E\{\gamma_F \cdot F_{rep} ; X_k ; a_d\} \tag{B.3.2}$$

(7) Dans l'approche de calcul 3, un calcul unique est exigé. Toutefois, dans cette approche de calcul, une différence est faite entre les actions $F_{rep}$ venant de la structure et les actions qui viennent du terrain ou sont transmises par lui et qui sont calculées à partir des valeurs de $X_k$.

On applique soit $\gamma_F \neq 1$ et $\gamma_E = 1$, soit $\gamma_F = 1$ et $\gamma_E \neq 1$. De ce fait, les équations (2.6a) et (2.6b) restent :

$$E_d = E\{\gamma_F \cdot F_{rep} ; X_k / \gamma_M ; a_d\} \tag{B.4.1}$$

ou :

$$E_d = \gamma_E \cdot E\{F_{rep} ; X_k / \gamma_M ; a_d\} \tag{B.4.2}$$

### B.3 Facteurs pour les résistances du matériau et de l'ouvrage

(1) L'équation (6.6) de la norme EN 1990:2002 et l'équation (2.7c) de la norme EN 1997-1 sont équivalentes :

$$R_d = \frac{1}{\gamma_{R;d}} R\{X_{i;d} ; a_d\} = \frac{1}{\gamma_{R;d}} R\left\{\frac{\eta_i X_{i;k}}{\gamma_{m;i}} ; a_d\right\} \quad \text{(EN 1990:2002, équation 6.6)} \tag{B.5.1}$$

$$R_d = \frac{1}{\gamma_R} R\left\{\gamma_F \cdot F_{rep} ; \frac{X_k}{\gamma_M} ; a_d\right\} \quad \text{(EN 1997-1, équation 2.7c)} \tag{B.5.2}$$

(2) Il faut noter que la norme EN 1997-1, équations (2.7a), (2.7b) et (2.7c), incluent $\gamma_F \cdot F_{rep}$ dans le calcul des résistances de calcul parce que l'amplitude des actions peut, dans certains cas, affecter les valeurs des résistances, par exemple pour la portance d'une fondation superficielle.

(3) La valeur du facteur de conversion $\eta$ est fixée à 1,0 dans la norme EN 1997-1 parce que les valeurs caractéristiques des propriétés de résistance du matériau sont définies comme correspondant à la situation sur le terrain et qu'à ce titre $\eta$ est inclus dans la valeur caractéristique.

(4) Les différentes approches de cette norme exigent que les facteurs soient appliqués soit aux propriétés de résistance des matériaux ($X$), soit aux résistances globales du terrain ou de la structure ($R$). Ces facteurs combinent les rôles des facteurs appliqués aux matériaux ($\gamma_m$) et des facteurs de modèle de résistance ($\gamma_{R;d}$) de différentes façons. Par simplicité, les facteurs appliqués aux propriétés de résistance des matériaux ($X$) sont notés $\gamma_M$ et les facteurs appliqués aux résistances globales $R$ sont notés $\gamma_R$.

(5) Dans l'approche de calcul 1, les vérifications sont exigées pour des combinaisons d'ensembles de facteurs dans deux calculs séparés.

Dans la combinaison 1, des facteurs égaux à 1 sont appliqués aux propriétés de résistance des matériaux et aux résistances globales. De ce fait : $\gamma_M = \gamma_R = 1$ dans l'équation (2.7c).

Dans la combinaison 2, sauf pour les pieux et les ancrages, $\gamma_M > 1$, $\gamma_R = 1$.

Pour cette raison, dans la plupart des cas l'approche de calcul 1 adopte l'équation (2.7a) :

$$R_d = R\{\gamma_F \cdot F_{rep} ; X_k / \gamma_M ; a_d\} \tag{B.6.1.1}$$

Mais, dans la combinaison 2 pour les pieux et les ancrages, $\gamma_M = 1$ et $\gamma_R > 1$ sont utilisés dans l'équation (2.7b), d'où :

$$R_d = \frac{1}{\gamma_R} R\{\gamma_F \cdot F_{rep} ; X_k ; a_d\} \tag{B.6.1.2}$$

(6) Dans l'approche de calcul 2, des facteurs égaux à 1 sont généralement appliqués aux propriétés de résistance des matériaux, et des facteurs plus grands que 1 sont appliqués aux résistances. Par conséquent, $\gamma_M = 1$; $\gamma_R > 1$ sont utilisés dans l'équation (2.7b) :

$$R_d = \frac{1}{\gamma_R} R\{\gamma_F \cdot F_{rep} ; X_k ; a_d\} \tag{B.6.2.1}$$

Lorsque l'on utilise aussi $\gamma_F = 1$, l'équation (2.7b) est utilisée sous la forme :

$$R_d = \frac{1}{\gamma_R} R\{F_{rep} ; X_k ; a_d\} \tag{B.6.2.2}$$

(7) Dans l'approche de calcul 3, $\gamma_M > 1$ et $\gamma_R = 1$ sont généralement appliqués. L'équation (2.7a) est donc utilisée :

$$R_d = R\{\gamma_F \cdot F_{rep} ; X_k / \gamma_M ; a_d\} \tag{B.6.3.1}$$

Mais il faut noter qu'il est parfois aussi nécessaire d'avoir $\gamma_R > 1$ (pour les pieux en tension, par exemple), de telle sorte que l'équation (2.7a) est utilisée :

$$R_d = \frac{1}{\gamma_R} R\{\gamma_F \cdot F_{rep} ; X_k / \gamma_M ; a_d\} \tag{B.6.3.2}$$

---

Liens : [[EC7-1_index]] · [[EC7-1_A_facteurs-partiels]] · [[EC7-1_C_capacite-portante]] · [[_Knowledge — Index]] · [[CLAUDE]]
