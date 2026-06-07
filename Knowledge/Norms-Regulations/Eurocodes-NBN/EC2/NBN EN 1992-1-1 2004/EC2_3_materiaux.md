---
title: "NBN EN 1992-1-1:2004 — Materiaux"
type: norm-extract
source: "NBN EN 1992-1-1:2004"
norm: EC2
section: "3"
chapter: "Materiaux"
tags: [EC2, eurocode-2, materiaux]
related: ["[[EC2_index]]", "[[EC2_2_bases-calcul.md]]", "[[EC2_4_durabilite-enrobage.md]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# 3.1 Béton

## 3.1.1 Généralités

(1)P Les articles qui suivent donnent les principes et les règles applicables au béton de résistance normale et au béton à haute résistance.

(2) Les règles relatives au béton de granulats légers sont données à la Section 11.

## 3.1.2 Résistance

(1)P La résistance en compression du béton est désignée par des classes de résistance liées à la résistance caractéristique (fractile 5%) mesurée sur cylindre fck ou sur cube fck,cube, conformément à l'EN 206-1.

(2)P Les classes de résistance du présent code sont basées sur la résistance caractéristique mesurée sur cylindre, fck, déterminée à 28 jours, compatible avec une valeur maximale Cmax.

> **Note** : La valeur de Cmax à utiliser dans un pays donné peut être fournie par son Annexe Nationale. La valeur recommandée est C90/105.

(3) Les résistances caractéristiques fck et les caractéristiques mécaniques correspondantes, nécessaires pour le calcul, sont données dans le Tableau 3.1.

(4) Dans certains cas (précontrainte, par exemple), il peut être indiqué d'établir la résistance en compression du béton avant ou après 28 jours, à partir d'éprouvettes conservées dans des conditions différentes de celles prescrites dans l'EN 12390.

Si la résistance en compression du béton est déterminée à un âge t > 28 jours, il convient de réduire les valeurs des coefficients αcc et αct définis en 3.1.6 (1)P et 3.1.6 (2)P par un facteur kt.

> **Note** : La valeur de kt à utiliser dans un pays donné peut être fournie par son Annexe Nationale. La valeur recommandée est kt = 0,85.

(5) Il peut être nécessaire de spécifier la résistance en compression du béton, fck(t), à l'instant t, pour un certain nombre de phases (décoffrage, transfert de précontrainte par exemple), où :

- fck(t) = fcm(t) - 8 (MPa) pour 3 < t < 28 jours
- fck(t) = fck pour t ≥ 28 jours

Il convient de fonder des valeurs plus précises sur des essais, notamment pour t ≤ 3 jours.

(6) La résistance en compression du béton à l'âge t dépend du type de ciment, de la température et des conditions de cure. Pour une température moyenne de 20°C et une cure conforme à l'EN 12390, la résistance en compression du béton à différents âges t, fcm(t), peut être estimée à l'aide des Expressions (3.1) et (3.2).

$$f_{cm}(t) = \beta_{cc}(t) \, f_{cm} \quad (3.1)$$

avec :

$$\beta_{cc}(t) = \exp \left\{ s \left(1 - \left(\frac{28}{t}\right)^{1/2}\right) \right\} \quad (3.2)$$

où :

- fcm(t) est la résistance moyenne en compression du béton à l'âge de t jours
- fcm est la résistance moyenne en compression du béton à 28 jours, conformément au Tableau 3.1
- βcc(t) est un coefficient qui dépend de l'âge t du béton
- t est l'âge du béton, en jours
- s est un coefficient qui dépend du type de ciment :
  - s = 0,20 pour les ciments de classe de résistance CEM 42,5 R, CEM 52,5 N et CEM 52,5 R (Classe R)
  - s = 0,25 pour les ciments de classe de résistance CEM 32,5 R, CEM 42,5 N (Classe N)
  - s = 0,38 pour les ciments de classe de résistance CEM 32,5 N (Classe S)

> **Note** : exp{ } a la même signification que e( ).

Lorsque le béton ne satisfait pas la prescription de résistance en compression à 28 jours, l'utilisation des Expressions (3.1) et (3.2) est inappropriée.

Il convient de ne pas utiliser le présent alinéa afin de justifier a posteriori une résistance non conforme à celle de référence, par un accroissement ultérieur de sa valeur.

Dans le cas où une cure thermique est appliquée à l'élément, on se reportera à 10.3.1.1 (3).

(7)P La résistance en traction se rapporte à la contrainte maximale atteinte sous chargement en traction uni-axiale centrée. Pour la résistance à la traction en flexion, il convient de se reporter à 3.1.8 (1).

(8) Lorsque la résistance en traction est déterminée comme la résistance en traction par fendage fct,sp, il est possible de prendre, pour la résistance en traction directe fct, une valeur approchée égale à :

$$f_{ct} = 0,9 \, f_{ct,sp} \quad (3.3)$$

(9) L'évolution de la résistance en traction avec le temps dépend fortement des conditions de cure et de séchage ainsi que des dimensions des éléments structuraux considérés. En première approximation, on peut admettre que la résistance en traction fctm(t) vaut :

$$f_{ctm}(t) = (\beta_{cc}(t))^\alpha \cdot f_{ctm} \quad (3.4)$$

où βcc(t) est donné par l'expression (3.2) et :
- α = 1 pour t < 28
- α = 2/3 pour t ≥ 28

Les valeurs de fctm sont données dans le Tableau 3.1.

> **Note** : Dans le cas où l'évolution de la résistance en traction avec le temps a de l'importance, on recommande de procéder à des essais en tenant compte des conditions d'exposition et des dimensions de l'élément.

### Tableau 3.1 : Caractéristiques de résistance et de déformation du béton

| Classes de résistance du béton | fck (MPa) | fck,cube (MPa) | fcm (MPa) | fctm (MPa) | fctk,0,05 (MPa) | fctk,0,95 (MPa) | Ecm (GPa) | εc1 (‰) | εcu1 (‰) | εc2 (‰) | εcu2 (‰) | n | εc3 (‰) | εcu3 (‰) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C12 | 12 | 15 | 20 | 1.6 | 1.1 | 2.0 | 27 | 1.8 | — | — | — | — | — | — |
| C16 | 16 | 20 | 24 | 1.9 | 1.3 | 2.5 | 29 | 1.9 | — | — | — | — | — | — |
| C20 | 20 | 25 | 28 | 2.2 | 1.5 | 2.9 | 30 | 2.0 | 3.5 | 2.0 | 3.5 | 2.0 | 1.75 | 3.5 |
| C25 | 25 | 30 | 33 | 2.6 | 1.8 | 3.3 | 31 | 2.1 | — | — | — | — | — | — |
| C30 | 30 | 37 | 38 | 2.9 | 2.0 | 3.8 | 33 | 2.2 | — | — | — | — | — | — |
| C35 | 35 | 45 | 43 | 3.2 | 2.2 | 4.2 | 34 | 2.25 | — | — | — | — | — | — |
| C40 | 40 | 50 | 48 | 3.5 | 2.5 | 4.6 | 35 | 2.3 | — | — | — | — | — | — |
| C45 | 45 | 55 | 53 | 3.8 | 2.7 | 4.9 | 36 | 2.4 | — | — | — | — | — | — |
| C50 | 50 | 60 | 58 | 4.1 | 2.9 | 5.3 | 37 | 2.45 | — | — | — | — | — | — |
| C55 | 55 | 67 | 63 | 4.2 | 3.0 | 5.5 | 38 | 2.5 | 3.2 | 2.2 | 3.1 | 1.75 | 1.8 | 3.1 |
| C60 | 60 | 75 | 68 | 4.4 | 3.1 | 5.7 | 39 | 2.6 | 3.0 | 2.3 | 2.9 | 1.6 | 1.9 | 2.9 |
| C70 | 70 | 85 | 78 | 4.6 | 3.2 | 6.0 | 41 | 2.7 | 2.8 | 2.4 | 2.7 | 1.45 | 2.0 | 2.7 |
| C80 | 80 | 95 | 88 | 4.8 | 3.4 | 6.3 | 42 | 2.8 | 2.8 | 2.5 | 2.6 | 1.4 | 2.2 | 2.6 |
| C90 | 90 | 105 | 98 | 5.0 | 3.5 | 6.6 | 44 | 2.8 | 2.8 | 2.6 | 2.6 | 1.4 | 2.3 | 2.6 |

**Expressions analytiques :**

- fcm = fck + 8 (MPa)
- fctm = 0,30 × fck^(2/3) pour ≤ C50/60
- fctm = 2,12·ln(1+(fcm/10)) pour > C50/60
- fctk,0,05 = 0,7 × fctm
- fctk,0,95 = 1,3 × fctm
- Ecm = 22[(fcm)/10]^0,3 (fcm en MPa)
- εc1 (‰) = 0,7 fcm^0,31 < 2.8 pour fck ≥ 50 MPa
- εcu1 (‰) = 2,8 + 27[(98-fcm)/100]^4 pour fck ≥ 50 MPa
- εc2 (‰) = 2,0 + 0,085(fck-50)^0,53 pour fck ≥ 50 MPa
- εcu2 (‰) = 2,6 + 35[(90-fck)/100]^4 pour fck ≥ 50 MPa
- n = 1,4 + 23,4[(90-fck)/100]^4 pour fck ≥ 50 MPa
- εc3 (‰) = 1,75 + 0,55[(fck-50)/40] pour fck ≥ 50 MPa
- εcu3 (‰) = 2,6 + 35[(90-fck)/100]^4 pour fck ≥ 50 MPa

## 3.1.3 Déformation élastique

(1) Les déformations élastiques du béton dépendent largement de la composition de celui-ci (notamment des granulats). Il convient de considérer les valeurs données dans la présente Norme comme des valeurs indicatives, valables pour des applications générales. Il convient cependant de les déterminer de manière explicite si la structure est considérée comme sensible aux écarts éventuels par rapport à ces valeurs générales.

(2) Le module d'élasticité du béton dépend du module d'élasticité de ses constituants. Des valeurs approchées de Ecm, module sécant entre σc = 0 et 0,4fcm, sont données dans le Tableau 3.1 pour des bétons contenant des granulats de quartzite. Pour des granulats calcaires et des granulats issus de grès, il convient de réduire la valeur de 10% et 30% respectivement tandis qu'il convient de l'augmenter de 20% pour des granulats issus de basalte.

> **Note** : L'Annexe Nationale du pays peut faire état d'informations complémentaires non contradictoires.

(3) L'évolution du module d'élasticité avec le temps peut être estimée par :

$$E_{cm}(t) = \left(\frac{f_{cm}(t)}{f_{cm}}\right)^{0.3} E_{cm} \quad (3.5)$$

expression dans laquelle Ecm(t) et fcm(t) sont les valeurs à l'âge t (jours) et Ecm et fcm les valeurs déterminées à 28 jours. La relation entre fcm(t) et fcm est donnée par l'Expression (3.1).

(4) Le coefficient de Poisson peut être pris égal à 0,2 pour le béton non fissuré et à 0 pour le béton fissuré.

(5) À défaut d'informations plus précises, le coefficient linéaire de dilatation thermique peut être pris égal à 10·10^-6 K^-1.

## 3.1.4 Fluage et retrait

(1)P Le fluage et le retrait du béton dépendent de l'humidité ambiante, des dimensions de l'élément et de la composition du béton. Le fluage dépend également de la maturité du béton lors du premier chargement ainsi que de la durée et de l'intensité de la charge.

(2) Le coefficient de fluage φ(t, t0) est fonction de Ec, le module tangent, qui peut être pris égal à 1,05 Ecm. Dans les cas où une grande précision n'est pas requise, la valeur obtenue à l'aide de la Figure 3.1 peut être considérée comme le coefficient de fluage, sous réserve que le béton ne soit pas soumis à une contrainte de compression supérieure à 0,45 fck(t0) à un âge t0, âge du béton au moment du chargement.

> **Note** : Pour plus d'informations, y compris sur l'évolution du fluage avec le temps, on pourra se reporter à l'Annexe B.

(3) La déformation de fluage du béton à l'instant t = ∞, εcc(∞,t0) sous une contrainte de compression constante σc appliquée à l'âge du béton t0, est donnée par :

$$\varepsilon_{cc}(\infty, t_0) = \varphi(\infty, t_0) \cdot \frac{\sigma_c}{E_c} \quad (3.6)$$

(4) Lorsque la contrainte de compression dans le béton à l'âge t0 dépasse la valeur 0,45 fck(t0), il convient de tenir compte de la non-linéarité du fluage. Une contrainte aussi élevée peut résulter de la précontrainte par pré-tension ; ce peut être le cas au niveau de l'armature de précontrainte dans les éléments préfabriqués en béton, par exemple. Il convient alors de déterminer le coefficient de fluage théorique non-linéaire de la manière suivante :

$$\varphi_k(\infty, t_0) = \varphi(\infty, t_0) \exp(1,5(k_\sigma - 0,45)) \quad (3.7)$$

où :
- φk(∞, t0) est le coefficient de fluage théorique non-linéaire, qui remplace φ(∞, t0)
- kσ est le rapport σc/fcm(t0), dans lequel σc est la contrainte de compression et fcm(t0) la résistance moyenne en compression du béton à la date du chargement.

(5) Les valeurs de la Figure 3.1 sont valables pour des températures ambiantes comprises entre -40°C et +40°C et une humidité relative comprise entre RH = 40% et RH = 100%. Les symboles utilisés sont les suivants :
- φ(∞,t0) : valeur finale du coefficient de fluage
- t0 : âge du béton au moment du chargement, en jours
- h0 : rayon moyen = 2Ac/u, où Ac est l'aire de la section transversale du béton et u le périmètre de la partie exposée à la dessiccation
- S : désigne les ciments de Classe S
- N : désigne les ciments de Classe N
- R : désigne les ciments de Classe R

(6) La déformation totale de retrait se compose de la déformation due au retrait de dessiccation et de la déformation due au retrait endogène. La déformation due au retrait de dessiccation évolue lentement, car elle est fonction de la migration de l'eau au travers du béton durci. La déformation due au retrait endogène se développe au cours du durcissement du béton : elle se produit par conséquent en majeure partie au cours des premiers jours suivant le coulage. Le retrait endogène est une fonction linéaire de la résistance du béton. Il convient d'en tenir compte de manière spécifique lorsque du béton frais est coulé au contact de béton durci.

Par conséquent, la déformation totale de retrait εcs est égale à :

$$\varepsilon_{cs} = \varepsilon_{cd} + \varepsilon_{ca} \quad (3.8)$$

où :
- εcs est la déformation totale de retrait
- εcd est la déformation due au retrait de dessiccation
- εca est la déformation due au retrait endogène

La valeur finale du retrait de dessiccation, εcd,∞, est égale à kh·εcd,0. εcd,0 peut être lu dans le Tableau 3.2 (valeurs moyennes probables, avec un coefficient de variation de l'ordre de 30%).

> **Note** : La formule de εcd,0 est donnée dans l'Annexe B.

### Tableau 3.2 : Valeurs nominales du retrait de dessiccation non gêné εcd,0 (en ‰) pour le béton avec des ciments CEM de classe N

| fck/fck,cube (MPa) | Humidité Relative (%) |||||
|---|---|---|---|---|---|
| | 20 | 40 | 60 | 80 | 90 | 100 |
| 20/25 | 0.62 | 0.58 | 0.49 | 0.30 | 0.17 | 0.00 |
| 40/50 | 0.48 | 0.46 | 0.38 | 0.24 | 0.13 | 0.00 |
| 60/75 | 0.38 | 0.36 | 0.30 | 0.19 | 0.10 | 0.00 |
| 80/95 | 0.30 | 0.28 | 0.24 | 0.15 | 0.08 | 0.00 |
| 90/105 | 0.27 | 0.25 | 0.21 | 0.13 | 0.07 | 0.00 |

L'évolution du retrait de dessiccation avec le temps est donnée par :

$$\varepsilon_{cd}(t) = \beta_{ds}(t, t_s) \cdot k_h \cdot \varepsilon_{cd,0} \quad (3.9)$$

où kh est un coefficient dépendant du rayon moyen h0, conformément au Tableau 3.3.

### Tableau 3.3 : Valeurs de kh dans l'expression (3.9)

| h0 | kh |
|---|---|
| 100 | 1.0 |
| 200 | 0.85 |
| 300 | 0.75 |
| ≥ 500 | 0.70 |

$$\beta_{ds}(t, t_s) = \frac{(t - t_s)}{0.04\sqrt{h_0} + (t - t_s)} \quad (3.10)$$

où :
- t est l'âge du béton à l'instant considéré, en jours
- ts est l'âge du béton (jours) au début du retrait de dessiccation (ou gonflement). Normalement, ceci correspond à la fin de la cure.
- h0 est le rayon moyen (mm) de la section transversale = 2Ac/u, avec Ac aire de la section du béton et u périmètre de la partie de la section exposée à la dessiccation.

La déformation due au retrait endogène est donnée par :

$$\varepsilon_{ca}(t) = \beta_{as}(t) \varepsilon_{ca}(\infty) \quad (3.11)$$

expression dans laquelle :

$$\varepsilon_{ca}(\infty) = 2,5(f_{ck} - 10) \times 10^{-6} \quad (3.12)$$

et

$$\beta_{as}(t) = 1 - \exp(-0.2 t^{0.5}) \quad (3.13)$$

t étant exprimé en jours.

## 3.1.5 Relation contrainte-déformation pour l'analyse structurale non-linéaire

(1) La relation entre σc et εc pour le chargement uni-axial de courte durée (contrainte de compression et raccourcissement exprimés en valeurs absolues) est donnée par l'Expression (3.14) :

$$\sigma_c = f_{cm} \frac{k\eta - \eta^2}{1 + (k-2)\eta} \quad (3.14)$$

dans laquelle :
- η = εc / εc1
- εc1 est la déformation au pic de contrainte, telle qu'indiquée dans le Tableau 3.1
- k = 1,05 Ecm × |εc1| / fcm (fcm selon Tableau 3.1)

L'Expression (3.14) vaut pour 0 < |εc| < |εcu1| où εcu1 est la valeur nominale de la déformation ultime.

(2) D'autres relations contrainte-déformation simplifiées peuvent être appliquées, sous réserve qu'elles représentent correctement le comportement du béton considéré.

## 3.1.6 Résistance de calcul en compression et résistance de calcul en traction

(1)P La résistance de calcul en compression est définie comme :

$$f_{cd} = \alpha_{cc} \frac{f_{ck}}{\gamma_C} \quad (3.15)$$

où :
- γC est le coefficient partiel relatif au béton, voir 2.4.2.4
- αcc est un coefficient tenant compte des effets à long terme sur la résistance en compression et des effets défavorables résultant de la manière dont la charge est appliquée.

> **Note** : La valeur de αcc à utiliser dans un pays donné, qu'il convient de prendre entre 0,8 et 1,0, peut être fournie par son Annexe Nationale. La valeur recommandée est αcc = 1.

(2)P La résistance de calcul en traction fctd est définie comme :

$$f_{ctd} = \alpha_{ct} \frac{f_{ctk,0.05}}{\gamma_C} \quad (3.16)$$

où :
- γC est le coefficient partiel relatif au béton, voir 2.4.2.4
- αct est un coefficient tenant compte des effets à long terme sur la résistance en traction et des effets défavorables résultant de la manière dont la charge est appliquée.

> **Note** : La valeur de αct à utiliser dans un pays donné peut être fournie par son Annexe Nationale. La valeur recommandée est αct = 1,0.

## 3.1.7 Relations contrainte-déformation pour le calcul des sections

(1) Le calcul des sections peut être effectué en utilisant la relation contrainte-déformation suivante (déformations en compression représentées positives) :

$$\sigma_c = f_{cd} \left[1 - \left(1 - \frac{\varepsilon_c}{\varepsilon_{c2}}\right)^n\right] \quad \text{pour } 0 \leq \varepsilon_c \leq \varepsilon_{c2} \quad (3.17)$$

$$\sigma_c = f_{cd} \quad \text{pour } \varepsilon_{c2} \leq \varepsilon_c \leq \varepsilon_{cu2} \quad (3.18)$$

où :
- n est l'exposant, tel qu'indiqué dans le Tableau 3.1
- εc2 est la déformation atteinte pour la contrainte maximale, telle qu'indiquée dans le Tableau 3.1
- εcu2 est la déformation ultime, telle qu'indiquée dans le Tableau 3.1

(2) D'autres relations contrainte-déformation simplifiées sont admises, à condition qu'elles soient équivalentes, voire plus conservatrices, que celle définie en (1) – diagramme bilinéaire, par exemple (contrainte de compression et raccourcissement représentés en valeur absolue), avec les valeurs de εc3 et εcu3 telles qu'indiquées dans le Tableau 3.1.

(3) On peut admettre un diagramme rectangulaire de compression dans le béton. Le coefficient λ, définissant la hauteur utile de la zone comprimée, et le coefficient η, définissant la résistance effective, valent :

$$\lambda = 0,8 \quad \text{pour } f_{ck} \leq 50 \text{ MPa} \quad (3.19)$$

$$\lambda = 0,8 - \frac{f_{ck} - 50}{400} \quad \text{pour } 50 < f_{ck} \leq 90 \text{ MPa} \quad (3.20)$$

et

$$\eta = 1,0 \quad \text{pour } f_{ck} \leq 50 \text{ MPa} \quad (3.21)$$

$$\eta = 1,0 - \frac{f_{ck} - 50}{200} \quad \text{pour } 50 < f_{ck} \leq 90 \text{ MPa} \quad (3.22)$$

> **Note** : Si la largeur de la zone comprimée diminue dans la direction de la fibre extrême la plus comprimée, il convient de réduire η fcd de 10%.

## 3.1.8 Résistance à la traction en flexion

(1) La résistance moyenne à la traction en flexion des éléments en béton armé dépend de leur résistance moyenne en traction directe et de la hauteur de leur section droite. On peut appliquer la formule suivante :

$$f_{ctm,fl} = \max\left\{\left(1,6 - \frac{h}{1000}\right)f_{ctm}; f_{ctm}\right\} \quad (3.23)$$

où :
- h est la hauteur totale de l'élément, en mm
- fctm est la résistance moyenne en traction directe, telle qu'indiquée dans le Tableau 3.1.

La relation donnée par l'Expression (3.23) s'applique également aux valeurs caractéristiques de la résistance en traction.

## 3.1.9 Béton confiné

(1) Le confinement du béton entraîne une modification de la relation contrainte-déformation : la résistance et la déformation ultime sont toutes deux supérieures. Les autres caractéristiques de base du matériau peuvent être considérées comme inchangées pour le calcul.

(2) En l'absence de données plus précises, il est possible d'utiliser une relation contrainte-déformation modifiée (les déformations en compression apparaissent comme positives), avec une résistance caractéristique et des déformations accrues, conformément à :

$$f_{ck,c} = f_{ck}(1.000 + 5.0 \frac{\sigma_2}{f_{ck}}) \quad \text{pour } \sigma_2 \leq 0.05f_{ck} \quad (3.24)$$

$$f_{ck,c} = f_{ck}(1.125 + 2.50 \frac{\sigma_2}{f_{ck}}) \quad \text{pour } \sigma_2 > 0.05f_{ck} \quad (3.25)$$

$$\varepsilon_{c2,c} = \varepsilon_{c2}\left(\frac{f_{ck,c}}{f_{ck}}\right)^2 \quad (3.26)$$

$$\varepsilon_{cu2,c} = \varepsilon_{cu2} + 0.2\frac{\sigma_2}{f_{ck}} \quad (3.27)$$

où σ2 (= σ3) est la contrainte effective de compression latérale à l'ELU due au confinement, εc2 et εcu2 étant donnés par le Tableau 3.1. Le confinement peut être obtenu au moyen de cadres correctement fermés ou d'armatures transversales, qui atteignent l'état plastique du fait de la dilatation latérale du béton.

# 3.2 Acier de béton armé

## 3.2.1 Généralités

(1)P Les paragraphes qui suivent donnent les principes et les règles applicables aux armatures de béton armé sous forme de barres, de fils redressés, de treillis soudés et de poutres en treillis pré-assemblées. Ils ne s'appliquent pas aux barres comportant un revêtement spécial.

(2)P Les exigences relatives aux propriétés des aciers de béton armé visent le matériau en place dans le béton durci. Si certaines opérations effectuées sur le chantier peuvent affecter les propriétés des aciers, celles-ci doivent être vérifiées à l'issue de ces opérations.

(3)P Lorsque d'autres armatures, non conformes à l'EN 10080, sont utilisées, on doit vérifier que leurs propriétés sont conformes selon 3.2.2 à 3.2.6 et à l'Annexe C.

(4)P Les propriétés requises pour les aciers de béton armé doivent être vérifiées par application des procédures d'essai indiquées dans l'EN 10080.

> **Note** : L'EN 10080 fait référence à une limite d'élasticité Re qui se rapporte à la valeur caractéristique, à la limite supérieure et à la limite inférieure, sur la base du niveau de qualité à long terme de la production. À l'inverse, la limite caractéristique d'élasticité fyk est basée uniquement sur les armatures utilisées dans la structure considérée. Il n'y a pas de relation directe entre fyk et la valeur de Re. Néanmoins, les méthodes d'évaluation et de vérification de la limite d'élasticité données dans l'EN 10080 constituent un moyen suffisant d'évaluation de fyk.

(5) Les règles d'application relatives aux poutres en treillis pré-assemblées s'appliquent uniquement à celles constituées d'armatures à haute adhérence. Des poutres en treillis pré-assemblées réalisées avec d'autres types d'armatures peuvent être définies dans un Agrément Technique Européen correspondant.

## 3.2.2 Propriétés

(1)P Le comportement des armatures de béton armé est défini par les propriétés ci-après :

- limite d'élasticité (fyk ou f0,2k)
- limite supérieure réelle d'élasticité (fy,max)
- résistance en traction (ft)
- ductilité (εuk et ft/fyk)
- aptitude au pliage
- caractéristiques d'adhérence (fR : voir Annexe C)
- dimensions de la section et tolérances
- résistance de fatigue
- soudabilité
- résistance au cisaillement et résistance des soudures dans le cas des treillis soudés et des poutres en treillis pré-assemblées.

(2)P Le présent Eurocode s'applique aux armatures à haute adhérence et soudables, y compris les treillis soudés. Les procédés de soudage admis sont donnés dans le Tableau 3.4.

> **Note 1** : Les propriétés des armatures de béton armé requises pour l'emploi avec le présent Eurocode sont données à l'Annexe C.
>
> **Note 2** : Les propriétés et les règles relatives aux fils à empreintes utilisés dans les produits préfabriqués en béton peuvent être indiquées dans la norme de produit correspondante.

(3)P Les règles d'application relatives au dimensionnement et aux dispositions constructives figurant dans le présent Eurocode sont valables pour une gamme de la limite d'élasticité spécifiée, telle que fyk = 400 à 600 MPa.

> **Note** : La valeur maximale de fyk de cette gamme à utiliser dans un pays donné peut être fournie par son Annexe Nationale.

(4)P Les caractéristiques de surface des armatures à haute adhérence doivent être telles qu'elles assurent une adhérence correcte avec le béton.

(5) Une adhérence correcte peut être admise moyennant le respect de la spécification de la surface projetée des verrous, fR.

> **Note** : Des valeurs minimales de la surface projetée des verrous fR sont données dans l'Annexe C.

(6)P Les armatures doivent posséder une aptitude au pliage telle qu'elle permette l'emploi des diamètres minimaux de mandrin indiqués dans le Tableau 8.1, et qu'elle autorise le re-pliage.

> **Note** : Pour les exigences de pliage-dépliage, voir l'Annexe C.

## 3.2.3 Résistance

(1)P La limite d'élasticité fyk (ou la limite d'élasticité conventionnelle à 0,2%, f0,2k) et la résistance en traction ftk sont définies respectivement comme la valeur caractéristique de la charge à la limite d'élasticité et la valeur caractéristique de la charge maximale, en traction directe, divisées par l'aire nominale de la section.

## 3.2.4 Caractéristiques de ductilité

(1)P L'acier de béton armé doit présenter une ductilité adéquate, définie par le rapport de la résistance en traction à la limite d'élasticité (ft/fy)k, et par l'allongement sous charge maximale εuk.

(2) La Figure 3.7 présente des courbes contrainte-déformation pour des aciers laminés à chaud types et des aciers profilés à froid types.

> **Note** : Des valeurs de (ft/fy)k et εuk sont données dans l'Annexe C pour les classes A, B et C.

## 3.2.5 Soudage

(1)P Les procédés de soudage des armatures de béton armé doivent être tels qu'indiqués dans le Tableau 3.4 et la soudabilité telle qu'indiquée dans l'EN 10080.

(2)P Le soudage d'armatures de béton armé doit dans tous les cas être réalisé conformément à l'EN ISO 17760.

(3)P La résistance des soudures situées sur la longueur d'ancrage des treillis doit être suffisante pour reprendre les efforts calculés.

(4) La résistance des assemblages soudés des treillis peut être considérée comme adéquate si chaque soudure est capable de reprendre un effort de cisaillement supérieur ou égal à 25% de la force équivalente au produit de l'aire nominale de la section par la limite caractéristique d'élasticité spécifiée. Il convient de retenir l'aire de la section du plus gros des deux fils si les sections sont différentes.

### Tableau 3.4 : Procédés de soudage admis et exemples d'application

| Cas de charge | Procédé de soudage | Barres tendues | Barres comprimées |
|---|---|---|---|
| Principalement statique (voir 6.8.1(2)) | Soudage par étincelage | Assemblage bout à bout | Assemblage bout à bout |
| | Soudage à l'arc avec électrode enrobée et soudage à l'arc avec fil fourré | Assemblage bout à bout avec φ ≥ 20 mm, assemblage à couvre-joint, assemblage par recouvrement, assemblage en croix, assemblage avec d'autres éléments en acier | Assemblage à couvre-joint, assemblage par recouvrement, assemblage en croix et assemblage avec d'autres éléments en acier |
| | Soudage MAG | Assemblage bout à bout avec φ ≥ 20 mm | — |
| | Soudage par friction | Assemblage bout à bout, assemblage avec d'autres éléments en acier | — |
| | Soudage par points par résistance | Assemblage par recouvrement, assemblage en croix | — |
| Non principalement statique (voir 6.8.1(2)) | Soudage par étincelage | Assemblage bout à bout | Assemblage bout à bout |
| | Soudage à l'arc avec électrode enrobée | Assemblage bout à bout avec φ ≥ 14mm | — |
| | Soudage MAG | Assemblage bout à bout avec φ ≥ 14mm | — |
| | Soudage par points par résistance | Assemblage par recouvrement, assemblage en croix | — |

**Notes**:
1. Seules des barres ayant approximativement le même diamètre nominal peuvent être assemblées par soudage.
2. Rapport admis des diamètres des barres ≥ 0,57
3. Dans le cas d'assemblages porteurs φ ≤ 16 mm
4. Dans le cas d'assemblages porteurs φ ≤ 28 mm

## 3.2.6 Fatigue

(1)P Lorsqu'une résistance à la fatigue est requise, elle doit être vérifiée comme indiqué dans l'EN 10080.

> **Note** : Des informations sont données dans l'Annexe C.

## 3.2.7 Hypothèses de calcul

(1) Il convient d'établir les calculs sur la base de l'aire nominale de la section des armatures, et de déduire les valeurs de calcul des valeurs caractéristiques données en 3.2.2.

(2) Pour un calcul courant, l'une ou l'autre des hypothèses suivantes peut être faite :

a) branche supérieure inclinée, avec une limite de déformation égale à εud et une contrainte maximale k fyk/γs pour εuk, avec k = (ft/fy)k

b) branche supérieure horizontale, sans nécessité de vérifier la limite de déformation.

> **Note 1** : La valeur de εud à utiliser dans un pays donné peut être fournie par son Annexe Nationale. La valeur recommandée est εud = 0,9εuk.
>
> **Note 2** : La valeur de (ft/fy)k est donnée dans l'Annexe C.

(3) La valeur moyenne de la masse volumique peut être supposée égale à 7850 kg/m³.

(4) La valeur de calcul du module d'élasticité Es peut être supposée égale à 200 GPa.

# 3.3 Acier de précontrainte

## 3.3.1 Généralités

(1)P Le présent article s'applique aux fils, barres et torons utilisés comme armatures de précontrainte dans les structures en béton.

(2)P Les armatures de précontrainte doivent posséder un niveau suffisamment faible de susceptibilité à la corrosion sous tension.

(3) Le niveau de susceptibilité à la corrosion sous tension peut être supposé suffisamment faible si les armatures de précontrainte satisfont aux critères spécifiés dans l'EN 10138 ou donnés dans un Agrément Technique Européen correspondant.

(4) Les exigences relatives aux propriétés des armatures de précontrainte visent les matériaux en place dans la structure. Lorsque les méthodes de production, d'essai et d'attestation de la conformité des armatures sont conformes à l'EN 10138 ou figurent dans un Agrément Technique Européen, on peut admettre que les exigences du présent Eurocode sont satisfaites.

(5)P Pour les aciers conformes au présent Eurocode, la résistance en traction, la limite d'élasticité conventionnelle à 0,1% et l'allongement sous charge maximale sont spécifiés en termes de valeurs caractéristiques ; ces valeurs sont désignées respectivement par fpk, fp0,1k et εuk.

> **Note** : L'EN 10138 fait référence à la valeur caractéristique, à la valeur minimale et à la valeur maximale, sur la base du niveau de qualité à long terme de la production. À l'inverse, fp0,1k et fpk, valeur caractéristique de la limite d'élasticité conventionnelle et résistance caractéristique en traction, sont basées uniquement sur les armatures de précontrainte nécessaires à la structure considérée. Il n'y a pas de relation directe entre ces deux ensembles de valeurs. Néanmoins, les méthodes d'évaluation et de vérification données dans l'EN 10138 et la valeur caractéristique de la charge correspondant à 0,1% d'allongement rémanent, Fp0,1k, divisée par la section Sn, donnée dans cette même norme, constituent un moyen suffisant d'évaluation de fp0,1k.

(6) Lorsque d'autres armatures, non conformes à l'EN 10138, sont utilisées, les propriétés peuvent figurer dans un Agrément Technique Européen approprié.

(7)P Chaque produit doit être clairement identifiable au regard du système de classification donné en 3.3.2 (2)P.

(8)P Les armatures de précontrainte doivent être classées vis-à-vis de la relaxation comme indiqué en 3.3.2 (4)P ou comme indiqué dans un Agrément Technique Européen approprié.

(9)P Chaque livraison doit être accompagnée d'un certificat contenant toutes les informations nécessaires à son identification au regard des caractéristiques (i) à (iv) du 3.3.2 (2)P et, au besoin, des informations complémentaires.

(10)P Les fils et barres ne doivent comporter aucune soudure. Les fils constitutifs des torons peuvent comporter des soudures décalées, à condition uniquement qu'elles aient été réalisées avant tréfilage à froid.

(11)P Dans le cas d'armatures de précontrainte en couronnes, la flèche maximale après déroulement d'une longueur de fil ou de toron doit être conforme à l'EN 10138 ou à la valeur figurant dans un Agrément Technique Européen approprié.

## 3.3.2 Propriétés

(1)P Les propriétés des aciers de précontrainte sont données dans l'EN 10138 Parties 2 à 4 ou dans un Agrément Technique Européen.

(2)P Les armatures de précontrainte (fils, torons et barres) doivent être classées en fonction des caractéristiques suivantes :

(i) leur résistance, décrite par la valeur de la limite d'élasticité conventionnelle à 0,1% (fp0,1k), par le rapport de la résistance en traction à la limite d'élasticité conventionnelle (fpk / fp0,1k) et par l'allongement sous charge maximale (εuk)

(ii) leur classe, indiquant leur comportement vis-à-vis de la relaxation

(iii) leur section

(iv) leurs caractéristiques de surface.

(3)P La masse réelle des armatures de précontrainte ne doit pas différer de la masse nominale au-delà des limites spécifiées dans l'EN 10138 ou données dans un Agrément Technique Européen.

(4)P Le présent Eurocode définit trois classes de relaxation :

- Classe 1 : fil ou toron – relaxation normale
- Classe 2 : fil ou toron – basse relaxation
- Classe 3 : barres laminées à chaud, ayant subi un traitement complémentaire

> **Note** : La classe 1 n'est pas couverte par l'EN 10138.

(5) Il convient d'établir les calculs des pertes dues à la relaxation des aciers de précontrainte sur la base de la valeur de ρ1000, la perte par relaxation (en %) 1000 heures après la mise en tension, pour une température moyenne de 20°C (voir l'EN 10138 pour la définition de l'essai de relaxation isotherme).

> **Note** : La valeur de ρ1000 est exprimée sous forme d'un pourcentage de la contrainte initiale ; elle est obtenue pour une contrainte initiale de 0,7fp, où fp est la résistance en traction réelle de l'acier de précontrainte, mesurée sur éprouvettes. Pour les calculs de dimensionnement, on utilise la résistance caractéristique en traction (fpk). Ceci a été pris en compte dans les expressions ci-après.

(6) ρ1000 peut soit être pris égal à 8% pour la Classe 1, à 2,5% pour la Classe 2 et à 4% pour la Classe 3, soit être donné par le certificat.

(7) La perte par relaxation peut être obtenue à partir des certificats d'essai du fabricant, ou définie comme le rapport, en %, de la variation de la contrainte sur la contrainte initiale, en appliquant l'une des expressions ci-dessous. Les Expressions (3.28) et (3.29) s'appliquent respectivement aux fils ou aux torons des armatures de précontrainte de relaxation normale et aux armatures de précontrainte basse relaxation, tandis que l'Expression (3.30) s'applique aux barres laminées à chaud ayant subi un traitement complémentaire.

**Classe 1** (relaxation normale) :

$$\Delta\sigma_{pr} = 10^{-5} \rho_{1000} \mu (1 - \mu)^{5.39} \left(\frac{\sigma_{pi}}{f_{pk}}\right) \exp\left(-\frac{0.75(1-\mu)}{6.7}\right) \times 1000^{t} \quad (3.28)$$

**Classe 2** (basse relaxation) :

$$\Delta\sigma_{pr} = 10^{-5} \rho_{1000} \mu (1 - \mu)^{0.66} \left(\frac{\sigma_{pi}}{f_{pk}}\right) \exp\left(-\frac{0.75(1-\mu)}{9.1}\right) \times 1000^{t} \quad (3.29)$$

**Classe 3** (barres traitées) :

$$\Delta\sigma_{pr} = 10^{-5} \rho_{1000} \mu (1 - \mu)^{1.98} \left(\frac{\sigma_{pi}}{f_{pk}}\right) \exp\left(-\frac{0.75(1-\mu)}{8}\right) \times 1000^{t} \quad (3.30)$$

où :

- Δσpr est la valeur absolue des pertes de précontrainte par relaxation
- σpi : Dans le cas de la précontrainte par post-tension, σpi est la valeur absolue de la contrainte initiale σpi = σpm0 (voir également 5.10.3 (2)); Dans le cas de la précontrainte par pré-tension, σpi est la contrainte à l'origine moins les pertes instantanées se produisant au cours du processus de mise en tension, voir 5.10.4 (1) (i)
- t : est le temps après la mise en tension (en heures)
- μ = σpi / fpk, avec fpk valeur caractéristique de la résistance en traction de l'acier de précontrainte
- ρ1000 : est la valeur de la perte par relaxation (en %), 1000 heures après la mise en tension, à une température moyenne de 20°C.

> **Note** : Il convient de se reporter à l'Annexe D dans le cas où les pertes par relaxation sont calculées pour différents intervalles de temps (différentes phases) et où une plus grande précision est requise.

(8) Les valeurs à long terme (finales) des pertes par relaxation peuvent être estimées à un temps t égal à 500 000 heures (soit 57 ans environ).

(9) Les pertes par relaxation sont très sensibles à la température de l'acier. Lorsqu'un traitement thermique est appliqué au béton (cure vapeur, par exemple), 10.3.2.2 s'applique. Dans les autres cas, lorsque la température de l'acier est supérieure à 50°C, il convient de procéder à une vérification des pertes par relaxation.

## 3.3.3 Résistance

(1)P La limite d'élasticité conventionnelle à 0,1% (fp0,1k) et la valeur spécifiée pour la résistance en traction (fpk) sont définies respectivement comme la valeur caractéristique de la charge correspondant à 0,1% d'allongement rémanent et comme la valeur caractéristique de la charge maximale en traction directe, divisées par l'aire nominale de la section.

## 3.3.4 Caractéristiques de ductilité

(1)P Les armatures de précontrainte doivent présenter une ductilité adéquate, telle que spécifiée dans l'EN 10138.

(2) Une ductilité adéquate à l'allongement peut être admise pour les armatures de précontrainte dont l'allongement sous charge maximale correspond à la valeur spécifiée par l'EN 10138.

(3) Une ductilité adéquate en flexion peut être admise si les armatures de précontrainte satisfont les exigences d'aptitude au pliage de l'EN ISO 15630.

(4) Des diagrammes contrainte-déformation, basés sur des données de production, doivent être établis pour les armatures de précontrainte et mis à disposition par le fabricant en annexe au certificat accompagnant la livraison (voir 3.3.1 (9)P).

(5) Une ductilité adéquate en traction peut être admise pour les armatures de précontrainte si fpk / fp0,1k ≥ k.

> **Note** : La valeur de k à utiliser dans un pays donné peut être fournie par son Annexe Nationale. La valeur recommandée est k = 1,1.

## 3.3.5 Fatigue

(1)P Les armatures de précontrainte doivent présenter une résistance de fatigue suffisante.

(2)P L'étendue de contrainte pour la fatigue, dans le cas des armatures de précontrainte, doit être conforme à l'EN 10138 ou donnée dans un Agrément Technique Européen approprié.

## 3.3.6 Hypothèses de calcul

(1)P L'analyse structurale est réalisée sur la base de l'aire nominale de la section des armatures de précontrainte et des valeurs caractéristiques fp0,1k, fpk et εuk.

(2) La valeur de calcul du module d'élasticité Ep peut être prise égale à 205 GPa pour les fils et les barres. La valeur réelle peut varier entre 195 et 210 GPa, selon le procédé de fabrication. Il convient de faire figurer la valeur correcte sur les certificats accompagnant la livraison.

(3) La valeur de calcul du module d'élasticité Ep peut être supposée égale à 195 GPa pour les torons. La valeur réelle peut varier entre 185 et 205 GPa, selon le procédé de fabrication. Il convient de faire figurer la valeur correcte sur les certificats accompagnant la livraison.

(4) La masse volumique moyenne des armatures de précontrainte peut normalement, pour le calcul, être supposée égale à 7 850 kg/m³.

(5) On peut admettre que les valeurs données ci-dessus sont valables pour des températures comprises entre –40°C et +100°C pour l'armature de précontrainte en place dans la structure.

(6) La valeur de calcul de la contrainte de l'acier, fpd, est prise égale à fp0,1k/γS.

(7) Pour le dimensionnement des sections, l'une ou l'autre des hypothèses suivantes peut être faite :

- branche inclinée, avec une limite de déformation εud. Le calcul peut également être basé sur la relation contrainte-déformation réelle, si celle-ci est connue, la contrainte au-delà de la limite d'élasticité étant réduite de manière analogue, ou

- branche supérieure horizontale, sans limite pour la déformation.

> **Note** : La valeur de εud à utiliser dans un pays donné peut être fournie par son Annexe Nationale. La valeur recommandée est εud = 0,9εuk. À défaut de valeurs plus précises, les valeurs recommandées sont εud = 0,02 et fp0,1k / fpk = 0,9.

## 3.3.7 Armatures de précontrainte logées dans des gaines

(1)P Les armatures de précontrainte logées dans une gaine (adhérentes ou non) doivent être protégées de manière adéquate et permanente contre la corrosion (voir 4.3).

(2)P Les armatures de précontrainte logées dans une gaine doivent être convenablement protégées contre les effets du feu (voir l'EN 1992-1-2).

# 3.4 Dispositifs de précontrainte

## 3.4.1 Ancrages et coupleurs

### 3.4.1.1 Généralités

(1)P Le paragraphe 3.4.1 s'applique aux dispositifs d'ancrage (ancrages) et aux dispositifs d'assemblage (coupleurs) utilisés dans les constructions précontraintes par post-tension, lorsque :

(i) les ancrages sont utilisés pour transmettre les efforts des armatures au béton dans la zone d'ancrage

(ii) les coupleurs sont utilisés pour assurer l'assemblage d'armatures individuelles de manière à obtenir des armatures continues.

(2)P Les ancrages et coupleurs destinés au système de précontrainte considéré doivent être conformes à l'Agrément Technique Européen concerné.

(3)P Les détails constructifs des zones d'ancrage doivent être conformes à 5.10, 8.10.3 et 8.10.4.

### 3.4.1.2 Propriétés mécaniques

#### 3.4.1.2.1 Armatures de précontrainte ancrées

(1)P Les assemblages armature-ancrage et armature-coupleur doivent présenter des caractéristiques de résistance, d'allongement et de fatigue suffisantes pour satisfaire aux exigences du projet.

(2) On peut admettre que ceci est vérifié sous réserve que :

(i) Les caractéristiques géométriques et mécaniques des composants de l'ancrage et du coupleur sont conformes à l'Agrément Technique Européen concerné et leur rupture prématurée n'est pas à craindre.

(ii) La rupture de l'armature n'est pas provoquée par la liaison avec l'ancrage ou le coupleur.

(iii) L'allongement à la rupture des assemblages est ≥ 2%.

(iv) Les assemblages armature-ancrage ne sont pas situés dans des zones fortement sollicitées par ailleurs.

(v) Les caractéristiques de fatigue des assemblages sont au moins équivalentes à celles de l'armature libre.

3.4.1.2.2  Organes d'ancrage et zones d'ancrage 
 
(1)P  La résistance des organes d'ancrage et des zones d'ancrage doit être suffisante pour 
permettre le transfert de la force de précontrainte au béton et l'apparition de fissures dans les 
zones d'ancrage ne doit pas altérer le fonctionnement des ancrages. 
 
3.4.2 Armatures de précontrainte extérieures (non adhérentes) 
 
3.4.2.1  Généralités 
 
(1)P  Une armature extérieure (non adhérente) est une armature située à l'extérieur de la 
section de béton associée, et reliée à la structure par des ancrages et des déviateurs 
uniquement. 
 
(2)P  Le système de précontrainte à utiliser avec des armatures extérieures doit être conforme 
à l'Agrément Technique Européen concerné.   
 
(3)  Il convient de suivre les règles données en 8.10 pour les dispositions constructives. 
 
3.4.2.2  Ancrages 
 
(1)  Dans le cas d'armatures non adhérentes, il convient d'indiquer, dans l'Agrément Technique 
Européen concerné, le rayon de courbure minimal de l'armature dans la zone d'ancrage.

---

Liens : [[EC2_index]] · [[EC2_2_bases-calcul.md]] · [[EC2_4_durabilite-enrobage.md]] · [[_Knowledge — Index]] · [[CLAUDE]]
