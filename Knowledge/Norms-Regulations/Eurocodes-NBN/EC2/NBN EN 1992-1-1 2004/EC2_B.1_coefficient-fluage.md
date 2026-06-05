---
title: "B.1 Équations de base pour la détermination du coefficient de fluage"
source: "EN 1992-1-1:2004 (F)"
norm: EC2
section: "B.1"
chapter: "Annexe B"
part: "Informative"
tags: [EC2, fluage, coefficient-fluage, déformation-temps, humidité-relative, ciment]
language: fr
jupyter_ref: "EC2/B.1"
---

# B.1 Équations de base pour la détermination du coefficient de fluage

## (1)

Le coefficient de fluage $\varphi(t,t_0)$ peut être calculé à partir de :

$$\varphi(t,t_0) = \varphi_0 \cdot \beta_c(t,t_0) \quad (B.1)$$

où :

**$\varphi_0$** est le coefficient de fluage conventionnel et peut être estimé par :

$$\varphi_0 = \varphi_{RH} \cdot \beta(f_{cm}) \cdot \beta(t_0) \quad (B.2)$$

**$\varphi_{RH}$** est un facteur tenant compte de l'influence de l'humidité relative sur le coefficient de fluage conventionnel :

$$\varphi_{RH} = 1 + \frac{(1-RH/100)}{0.1 \cdot h_0^{0.3}} \quad \text{pour } f_{cm} \leq 35 \text{ MPa} \quad (B.3a)$$

$$\varphi_{RH} = \left(1 + \frac{(1-RH/100)}{0.1 \cdot h_0^{0.3}} \cdot \alpha_1 \cdot \alpha_2\right) \quad \text{pour } f_{cm} > 35 \text{ MPa} \quad (B.3b)$$

où $RH$ est l'humidité relative de l'environnement ambiant en %.

**$\beta(f_{cm})$** est un facteur tenant compte de l'influence de la résistance du béton sur le coefficient de fluage conventionnel :

$$\beta(f_{cm}) = \frac{16.8}{f_{cm}} \quad (B.4)$$

où $f_{cm}$ est la résistance moyenne en compression du béton à 28 jours, en MPa.

**$\beta(t_0)$** est un facteur tenant compte de l'influence de l'âge du béton au moment du chargement sur le coefficient de fluage conventionnel :

$$\beta(t_0) = \frac{1}{0.1 + t_0^{0.20}} \quad (B.5)$$

**$h_0$** est le rayon moyen de l'élément, en mm :

$$h_0 = \frac{2 A_c}{u} \quad (B.6)$$

où $A_c$ est l'aire de la section droite et $u$ est le périmètre de l'élément en contact avec l'atmosphère.

**$\beta_c(t,t_0)$** est un coefficient qui rend compte du développement du fluage avec le temps après chargement, et peut être estimé par l'expression suivante :

$$\beta_c(t,t_0) = \left(\frac{t-t_0}{\beta_H + (t-t_0)}\right)^{0.3} \quad (B.7)$$

où :
- $t$ est l'âge du béton à l'instant considéré, en jours
- $t_0$ est l'âge du béton au moment du chargement, en jours
- $t - t_0$ est la durée non ajustée du chargement, en jours

**$\beta_H$** est un coefficient dépendant de l'humidité relative ($RH$ en %) et du rayon moyen de l'élément ($h_0$ en mm). Il peut être estimé par :

$$\beta_H = 1.5[1 + (0.012 RH)^{18}](h_0 + 250) \leq 1500 \quad \text{pour } f_{cm} \leq 35 \quad (B.8a)$$

$$\beta_H = 1.5[1 + (0.012 RH)^{18}](h_0 + 250)\alpha_3 \leq 1500 \alpha_3 \quad \text{pour } f_{cm} \geq 35 \quad (B.8b)$$

**$\alpha_1, \alpha_2, \alpha_3$** sont des coefficients tenant compte de l'influence de la résistance du béton :

$$\alpha_1 = \left(\frac{f_{cm}}{35}\right)^{0.7}$$

$$\alpha_2 = \left(\frac{f_{cm}}{35}\right)^{0.2}$$

$$\alpha_3 = \left(\frac{f_{cm}}{35}\right)^{0.5} \quad (B.8c)$$

## (2)

L'influence du type de ciment sur le coefficient de fluage du béton peut être prise en compte en modifiant l'âge du chargement $t_0$ dans l'Expression (B.5) conformément à l'expression suivante :

$$t_{0,T} = t_0 \cdot \left[\frac{9}{1 + 1.2 t_{0,T}^{0.5}}\right]^2 \geq 0.5 \quad (B.9)$$

où :
- $t_{0,T}$ est l'âge du béton au moment du chargement, en jours, corrigé en fonction de la température (Expression B.10)
- $\alpha$ est une puissance qui dépend du type de ciment (voir 3.1.2 (6)) :
  - $\alpha = -1$ pour les ciments de la classe S
  - $\alpha = 0$ pour les ciments de la classe N
  - $\alpha = 1$ pour les ciments de la classe R

## (3)

L'influence des températures élevées ou faibles dans l'intervalle de 0 à 80°C sur la maturité du béton peut être prise en compte en ajustant l'âge du béton conformément à l'expression suivante :

$$t_T = \sum_{i=1}^{n} e^{\frac{4000}{273+T(\Delta t_i)} - 13.65} \cdot \Delta t_i \quad (B.10)$$

où :
- $t_T$ est l'âge du béton corrigé en fonction de la température, remplaçant $t$ dans les expressions correspondantes
- $T(\Delta t_i)$ est la température durant la période de temps $\Delta t_i$, en °C
- $\Delta t_i$ est le nombre de jours où règne la température $T$

### Observations générales

Le coefficient de variation moyen des données de fluage prévues ci-dessus et déduites d'une banque de données informatisée de résultats d'essais en laboratoire, est de l'ordre de 20%.

Il convient d'associer les valeurs de $\varphi(t,t_0)$ données ci-dessus au module tangent $E_c$. Lorsqu'une évaluation moins précise est jugée satisfaisante, les valeurs données dans la Figure 3.1 du 3.1.4 peuvent être adoptées pour le fluage du béton à 70 ans.

---

## Références
- [[EC2_3.1.2_types-ciment.md]] (Section 3.1.2 - Types de ciment)
- [[EC2_3.1.4_fluage.md]] (Section 3.1.4 - Fluage du béton)
