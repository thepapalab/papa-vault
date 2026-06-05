---
title: "B — Annexe B — Procédure 1 de détermination du coefficient structural cscd (informative)"
source: "NBN EN 1991-1-4:2005 (F) — Eurocode 1: Actions du vent (+ AC:2010)"
norm: EC1-1-4
section: "B"
chapter: "B"
tags: [EC1-1-4, cscd, procedure-1, calcul-dynamique, coefficient-structural]
language: fr
jupyter_ref: "EC1-1-4/B"
created: 2026-06-05
---

# Annexe B — Procédure 1 de détermination du coefficient structural c_s·c_d (informative)

> Annexe informative. Procédure recommandée pour `c_s·c_d` selon §6.3.1. Alternative : Annexe C (écart < 5%).

## B.1 Facteur de pointe k_p

Le facteur de pointe `k_p` est défini comme le rapport de la valeur maximale de la partie variable de la réponse à son écart type :

$$k_p = \max\left(\sqrt{2 \cdot \ln(\nu \cdot T)},\ 3\right) \tag{B.1}$$

avec approximation :

$$k_p \approx \sqrt{2 \cdot \ln(\nu \cdot T)} + \frac{0{,}6}{\sqrt{2 \cdot \ln(\nu \cdot T)}}$$

où :
- T = 600 s (durée d'observation = 10 min)
- ν = fréquence de franchissement du niveau moyen (Hz)

$$\nu = n_{1,x} \cdot \sqrt{\frac{R^2}{B^2 + R^2}} \tag{B.2}$$

Pour `ν·T < 0,5` : `k_p = 3`.

## B.2 Coefficient de réponse quasi-statique B²

$$B^2 = \frac{1}{1 + \frac{0{,}9 \cdot (b+h)^{0{,}63}}{L(z_s)^{0{,}63}}} \tag{B.3}$$

où `L(z_s)` est l'échelle de turbulence :

$$L(z_s) = L_t \cdot \left(\frac{z_s}{z_t}\right)^\alpha \quad \text{pour } z_s \geq z_{min} \tag{B.1 — L}$$

avec `z_t = 200 m`, `L_t = 300 m`, α = 0,67 + 0,05·ln(z_0) (NDP).

## B.3 Coefficient de réponse résonante R²

$$R^2 = \frac{\pi^2}{2 \cdot \delta_s} \cdot S_L(z_s, n_{1,x}) \cdot R_h(η_h) \cdot R_b(η_b) \tag{B.6}$$

Fonction adimensionnelle de densité spectrale de puissance `S_L` :

$$S_L(z, n) = \frac{6{,}8 \cdot f_L(z,n)}{(1 + 10{,}2 \cdot f_L(z,n))^{5/3}} \tag{B.2}$$

$$f_L(z, n) = \frac{n \cdot L(z)}{v_m(z)} \tag{B.3}$$

Fonctions d'admittance aérodynamique :

$$R_h(\eta_h) = \frac{1}{\eta_h} - \frac{1}{2\eta_h^2}(1 - e^{-2\eta_h}) \quad \text{avec } \eta_h = \frac{4{,}6 \cdot h}{L(z_s)} \cdot f_L \tag{B.7}$$

$$R_b(\eta_b) = \frac{1}{\eta_b} - \frac{1}{2\eta_b^2}(1 - e^{-2\eta_b}) \quad \text{avec } \eta_b = \frac{4{,}6 \cdot b}{L(z_s)} \cdot f_L \tag{B.8}$$

## B.4 Décrément logarithmique total d'amortissement δ

$$\delta = \delta_s + \delta_a + \delta_d \tag{B.9}$$

| Composante | Définition |
|-----------|-----------|
| `δ_s` | Amortissement structural |
| `δ_a` | Amortissement aérodynamique |
| `δ_d` | Amortissement par dispositifs spéciaux |

$$\delta_a = \frac{c_f \cdot \rho \cdot b \cdot v_m(z_s)}{2 \cdot n_{1,x} \cdot m_e} \tag{B.10}$$

Valeurs recommandées de δ_s :

| Type de structure | δ_s |
|------------------|-----|
| Acier soudé | 0,05 |
| Acier boulonné | 0,05 |
| Béton armé | 0,10 |
| Mixte | 0,08 |
| Bois | 0,06–0,12 |
| Mâts ou pylônes | 0,04 |
| Cheminées en acier sans revêtement | 0,03 |
| Cheminées en acier avec revêtement | 0,04–0,12 |

## B.5 Déplacement et accélération (aptitude au service)

Le déplacement maximal dans la direction du vent et l'écart type de l'accélération `σ_{a,x}` sont calculés par les expressions (B.13) et (B.14).

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_6_coefficient-cscd]] · [[EC1-1-4_C_procedure2-cscd]]
