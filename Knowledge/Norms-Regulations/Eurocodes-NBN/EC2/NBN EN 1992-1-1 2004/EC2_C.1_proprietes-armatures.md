---
title: "C.1 Généralités — Propriétés des armatures"
source: "EN 1992-1-1:2004 (F)"
norm: EC2
section: "C.1"
chapter: "Annexe C"
part: "Normative"
tags: [EC2, armatures, propriétés, température, pliage-soudage]
language: fr
jupyter_ref: "EC2/C.1"
---

# C.1 Généralités

## (1) Domaine de validité et conditions de température

Le Tableau C.1 donne les propriétés des armatures compatibles avec l'utilisation du présent Eurocode. Les propriétés sont valables pour des températures des armatures dans la structure terminée comprises entre **–40°C et 100°C**.

En outre, il convient de restreindre tout pliage et tout soudage des armatures effectués sur le chantier aux champs de température tels qu'autorisés dans l'**EN 13670**.

---

## Tableau C.1 : Propriétés des armatures

### Structure du tableau

| Propriété | Classe A | Classe B | Classe C | Fractile (%) |
|-----------|----------|----------|----------|---|
| **Limite caractéristique d'élasticité** $f_{yk}$ ou $f_{0,2k}$ (MPa) | 400 à 600 | 400 à 600 | 400 à 600 | 5,0 |
| **Valeur minimale de** $k = (f_t / f_y)_k$ | ≥1,05 | ≥1,08 | ≥1,15 <1,35 | 10,0 |
| **Déformation relative sous charge max** $\varepsilon_{uk}$ (%) | ≥2,5 | ≥5,0 | ≥7,5 | 10,0 |
| **Aptitude au pliage** | Essai pliage/dépliage | Essai pliage/dépliage | Essai pliage/dépliage | — |
| **Résistance au cisaillement** | $0.3 A f_{yk}$ | $0.3 A f_{yk}$ | $0.3 A f_{yk}$ | Minimum |
| **Tolérance masse nominale** ($\phi \leq 8$ mm) | ±6,0% | ±6,0% | ±6,0% | 5,0 |
| **Tolérance masse nominale** ($\phi > 8$ mm) | ±4,5% | ±4,5% | ±4,5% | 5,0 |

où $A$ est l'aire du fil.

---

## Notes et recommandations

**Note :** Les valeurs d'étendue de contrainte en fatigue avec leur limite supérieure de $\beta f_{yk}$, et la surface projetée des verrous, à utiliser dans un pays donné peuvent être fournies par son Annexe Nationale. Les valeurs recommandées sont données dans le [[EC2_C.2_tableau-fatigue.md|Tableau C.2N]]. 

La valeur de $\beta$ à utiliser dans un pays donné peut être fournie par son Annexe Nationale. **La valeur recommandée est** $\beta = 0,6$.

---

## Tableau C.2N : Propriétés additionnelles des armatures

### Fatigue et adhérence

| Propriété | Classe A | Classe B | Classe C | Fractile (%) |
|-----------|----------|----------|----------|---|
| **Étendue de contrainte en fatigue** (MPa) *pour N ≥ 2 × 10⁶ cycles* avec limite $\beta f_{yk}$ | ≥150 | ≥100 | — | 10,0 |

### Adhérence : surface projetée des nervures/verrous

| $\phi$ nominale (mm) | $f_{R,\text{min}}$ |
|---|---|
| 5–6 | 0,035 |
| 6,5–12 | 0,040 |
| >12 | 0,056 |
| Fractile | 5,0% |

---

## Dispositions particulières

### Fatigue

Des exceptions aux règles pour la fatigue, à utiliser dans un pays donné, peuvent être fournies par son Annexe Nationale. Les exceptions recommandées concernent :
- Les armatures définies pour un chargement **principalement statique**, ou
- S'il est prouvé par des essais que des valeurs supérieures de l'étendue de contrainte en fatigue et/ou du nombre de cycles peuvent être appliquées

Dans ce dernier cas, les valeurs du [[EC2_6.3_fatigue.md|Tableau 6.3]] peuvent être modifiées en conséquence. La conformité de tels essais doit être assurée avec **l'EN 10080**.

### Adhérence

Lorsqu'il peut être prouvé qu'une capacité d'adhérence suffisante peut être atteinte avec des valeurs de $f_R$ inférieures à celles spécifiées ci-dessus, ces limites peuvent être assouplies.

Afin de garantir qu'une capacité d'adhérence suffisante est atteinte, les contraintes d'adhérence doivent respecter les expressions recommandées **(C.1N)** et **(C.2N)** lorsqu'elles ont été évaluées par l'essai **CEB/RILEM** :

$$\tau_m \geq 0.098(80 - 1.2\varphi) \quad (C.1N)$$

$$\tau_r \geq 0.098(130 - 1.9\varphi) \quad (C.2N)$$

où :
- $\varphi$ : dimension nominale de la barre (mm)
- $\tau_m$ : valeur moyenne de la contrainte d'adhérence (MPa) pour glissements de 0,01 mm, 0,1 mm et 1 mm
- $\tau_r$ : contrainte d'adhérence à rupture par glissement

---

## Voir aussi

- [[EC2_C.2_resistance.md|C.2]] — Résistance (limite d'élasticité maximale)
- [[EC2_C.3_pliage.md|C.3]] — Aptitude au pliage
- [[EC2_8.1_armatures.md|8.1]] — Généralités sur les armatures
