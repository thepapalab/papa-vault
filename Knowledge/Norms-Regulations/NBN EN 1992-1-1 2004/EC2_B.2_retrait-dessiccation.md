---
title: "B.2 Équations de base pour la détermination de la déformation relative due au retrait de dessiccation"
source: "EN 1992-1-1:2004 (F)"
norm: EC2
section: "B.2"
chapter: "Annexe B"
part: "Informative"
tags: [EC2, retrait, retrait-dessiccation, déformation, humidité-relative, ciment]
language: fr
jupyter_ref: "EC2/B.2"
---

# B.2 Équations de base pour la détermination de la déformation relative due au retrait de dessiccation

## (1)

La déformation relative de retrait de dessiccation de référence $\varepsilon_{cd,0}$ est calculée par :

$$\varepsilon_{cd,0} = 0.85[(220 + 110\alpha_{ds1}) \exp\left(-\alpha_{ds2} \frac{f_{cm}}{f_{cmo}}\right)] \cdot 10^{-6} \cdot \beta_{RH} \quad (B.11)$$

$$\beta_{RH} = 1.55\left[1-\left(\frac{RH}{RH_0}\right)^3\right] \quad (B.12)$$

### Paramètres

**$f_{cm}$** : résistance moyenne en compression (MPa)

**$f_{cmo}$** : résistance de référence = 10 MPa

**$\alpha_{ds1}$** : coefficient qui dépend du type de ciment (voir 3.1.2 (6)) :
- = 3 pour les ciments de classe S
- = 4 pour les ciments de classe N
- = 6 pour les ciments de classe R

**$\alpha_{ds2}$** : coefficient qui dépend du type de ciment :
- = 0,13 pour les ciments de classe S
- = 0,12 pour les ciments de classe N
- = 0,11 pour les ciments de classe R

**$RH$** : humidité relative de l'environnement ambiant en %

**$RH_0$** : humidité de référence = 100%

### Remarque

$\exp\{\,\}$ a la même signification que $e(\,)$ — notation exponentielle.

---

## Références
- [[EC2_3.1.2_types-ciment.md]] (Section 3.1.2 - Types de ciment)
- [[EC2_3.1.5_retrait.md]] (Section 3.1.5 - Retrait du béton)
