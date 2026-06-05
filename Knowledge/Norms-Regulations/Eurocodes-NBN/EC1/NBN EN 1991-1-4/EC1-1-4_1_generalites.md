---
title: "1 Généralités"
source: "NBN EN 1991-1-4:2005 (F) — Eurocode 1: Actions du vent (+ AC:2010)"
norm: EC1-1-4
section: "1"
chapter: "1"
tags: [EC1-1-4, domaine-application, references, definitions, symboles, vent]
language: fr
jupyter_ref: "EC1-1-4/1"
created: 2026-06-05
---

# 1 Généralités

## 1.1 Domaine d'application

(1) L'EN 1991-1-4 indique comment déterminer les actions du vent naturel pour le calcul structurel des bâtiments et des ouvrages de génie civil, pour chacune des zones affectées par ces actions. Ceci inclut l'ensemble de la structure, certains de ses éléments constitutifs, voire des éléments qui y sont fixés, par exemple des composants, des éléments de façade et leurs fixations, des glissières de sécurité et des écrans antibruit.

(2) La présente partie s'applique aux :
- bâtiments et ouvrages de génie civil dont la hauteur peut atteindre **200 m** ;
- ponts dont aucune travée n'est supérieure à **200 m**, à condition qu'ils satisfassent aux critères relatifs à la réponse dynamique (voir §8.2).

(3) La présente partie est destinée à prévoir les actions caractéristiques du vent sur les structures terrestres, leurs composants et accessoires.

(4) Certains aspects nécessaires pour déterminer les actions du vent dépendent du lieu, de la disponibilité et de la qualité des données météorologiques, du type de terrain, etc. Ils doivent être fournis dans l'Annexe Nationale.

(11) La présente partie ne fournit **pas** de recommandations concernant :
- les actions du vent sur les pylônes en treillis à membrures non parallèles ;
- les actions du vent sur les mâts haubanés et les cheminées haubanées ;
- les vibrations de torsion (bâtiments élevés avec noyau central) ;
- les vibrations des tabliers de ponts dues à la turbulence transversale ;
- les ponts à câbles ;
- les vibrations lorsque d'autres modes que le mode fondamental doivent être pris en considération.

NOTE 2 Pour les actions du vent sur les mâts haubanés, les cheminées haubanées et les pylônes en treillis à membrures non parallèles, voir EN 1993-3-1, Annexe A.

## 1.2 Références normatives

- EN 1990 — Eurocode : Bases de calcul des structures
- EN 1991-1-3 — Charges de neige
- EN 1991-1-6 — Actions pendant l'exécution
- EN 1991-2 — Charges dues au trafic sur les ponts
- EN 1993-3-1 — Mâts et tours

## 1.3 Hypothèses

(1)P Les hypothèses générales données dans l'EN 1990, §1.3 s'appliquent.

## 1.4 Distinction entre les principes et les règles d'application

(1)P Les règles énoncées dans l'EN 1990, §1.4 s'appliquent.

## 1.5 Calcul au moyen d'essais et de mesures

(1) Il est possible, en complément des calculs, de recourir à des essais en soufflerie et/ou à des méthodes numériques dûment validées afin d'obtenir des informations concernant les charges et la réponse.

NOTE NDP — L'Annexe Nationale peut donner des indications sur l'utilisation des essais et des mesures.

## 1.6 Termes et définitions

**1.6.1 valeur de base de la vitesse de référence du vent** — vitesse moyenne sur 10 min, probabilité de dépassement annuelle = 0,02, toutes directions confondues, à 10 m de hauteur en terrain « rase campagne ».

**1.6.2 vitesse de référence du vent** — valeur de base modifiée pour tenir compte de la direction du vent et de la saison.

**1.6.3 vitesse moyenne du vent** — vitesse de référence modifiée pour tenir compte de la rugosité du terrain et de l'orographie.

**1.6.4 coefficient de pression** — coefficients de pression extérieure (effet du vent sur surfaces extérieures) et intérieure. Coefficients locaux (A ≤ 1 m²) et globaux (A > 10 m²).

**1.6.5 coefficient de force** — effet global du vent sur une structure ou composant, y compris le frottement.

**1.6.6 coefficient de réponse quasi-statique** — tient compte de l'absence de corrélation parfaite de la pression sur la surface.

**1.6.7 coefficient de réponse résonante** — tient compte de l'effet de la turbulence en résonance avec le mode de vibration.

## 1.7 Symboles (sélection)

| Symbole | Définition |
|---------|-----------|
| `v_b,0` | Valeur de base de la vitesse de référence du vent (NDP) |
| `v_b` | Vitesse de référence du vent |
| `v_m` | Vitesse moyenne du vent |
| `q_b` | Pression dynamique moyenne de référence |
| `q_p` | Pression dynamique de pointe |
| `c_dir` | Coefficient de direction (NDP, rec. = 1,0) |
| `c_season` | Coefficient de saison (NDP, rec. = 1,0) |
| `c_alt` | Coefficient d'altitude |
| `c_r(z)` | Coefficient de rugosité |
| `c_o(z)` | Coefficient d'orographie |
| `c_e(z)` | Coefficient d'exposition |
| `c_s·c_d` | Coefficient structural |
| `c_f` | Coefficient de force |
| `c_p` | Coefficient de pression |
| `c_fr` | Coefficient de frottement |
| `I_v` | Intensité de turbulence |
| `z_0` | Longueur de rugosité |
| `z_min` | Hauteur minimale |
| `ρ` | Masse volumique de l'air (NDP, rec. = 1,25 kg/m³) |
| `δ_s` | Décrément logarithmique d'amortissement structural |
| `δ_a` | Décrément logarithmique d'amortissement aérodynamique |
| `St` | Nombre de Strouhal |
| `Sc` | Nombre de Scruton |
| `Re` | Nombre de Reynolds |
| `n_{1,x}` | Fréquence fondamentale de vibration dans la direction du vent |
| `n_{1,y}` | Fréquence fondamentale de vibration perpendiculaire au vent |
| `B²` | Partie quasi-statique de la réponse |
| `R²` | Partie résonante de la réponse |

---

Liens : [[EC1-1-4_index]] · [[EC1-1-4_2_situations-projet]]
