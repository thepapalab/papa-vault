---
title: EN 1990 ANB — 03 — Annexe A2 Ponts : ELU et ELS (valeurs normatives belges)
type: norm-extract
source: "NBN EN 1990 ANB:2021 — Eurocode 0 : Bases de calcul des structures — Annexe nationale belge, NBN, 23-03-2021"
norm: EN1990-ANB
tags: [EN1990, ANB, ELU, ELS, coefficients-partiels, gamma, ponts-ferroviaires, déformation, gauche, flèche, accélération, confort, approche-1]
related: ["[[EN 1990 ANB — Index]]", "[[EN 1990 ANB — 02 — A2 Ponts — Combinaisons et ψ]]", "[[EN 1990 ANB — 04 — Annexes B C D — Fiabilité et Classes]]", "[[EN 1990 A1 — 02 — A2.3 — États-Limites Ultimes]]", "[[EN 1990 A1 — 03 — A2.4 — États-Limites de Service]]", "[[PTR CE01 — Ch09 — ELS — FR]]"]
created: 2026-06-05
---

# EN 1990 ANB — 03 — Annexe A2 Ponts : ELU et ELS (valeurs normatives belges)

## A2.3 États-limites ultimes

### A2.3.1 Valeurs de calcul des actions dans les situations de projet durables et transitoires

(1) NOTE : Les valeurs des coefficients partiels pour les divers niveaux de fiabilité comme recommandés aux tableaux A2.4(A), A2.4(B) et A2.4(C) sont **normatives**, à moins d'une mention contraire.

(5) NOTE : **L'Approche 1 est applicable en Belgique** (voir EN 1997).

(7) NOTE : Les actions dues à la pression des glaces et à l'impact des bateaux sont considérées comme des **charges accidentelles** et sont définies dans l'ANB de l'EN 1991-1-7. Si nécessaire, ces actions peuvent être définies par le projet individuel.

(8) NOTE : Les valeurs appropriées de γ_P sont définies dans les Eurocodes relatifs aux matériaux et leurs ANB ou, le cas échéant, par le projet individuel.

> La NOTE 2 du Tableau A2.4(A) n'est **pas d'application** en Belgique.

---

#### NOTE 1 du Tableau A2.4(B) — Choix d'équation

Autant l'application de l'équation 6.10 que l'application des équations 6.10a et 6.10b sont **autorisées** en Belgique.

#### NOTE 2 du Tableau A2.4(B) — STR/GEO Ensemble B (valeurs normatives, CC2)

| Coefficient | Valeur normative | Domaine d'application |
|-------------|-----------------|----------------------|
| γ_{G,sup} | **1,35** | |
| γ_{G,inf} | **1,00** | |
| γ_Q (trafic routier et piétons, non favorable) | **1,35** (0 si favorable) | |
| γ_Q (trafic ferroviaire général, non favorable) | **1,45** (0 si favorable) | gr11–31 (sauf 16, 17, 26 assoc. SW/2, 27 assoc. SW/2), LM71, SW/0, HSLM, Trains réels |
| γ_Q (trafic ferroviaire lourd, non favorable) | **1,20** (0 si favorable) | Groupes 16, 17, 26 assoc. SW/2, 27 assoc. SW/2 |
| γ_Q (autres charges de trafic et actions variables) | **1,50** (0 si favorable) | |
| ξ | **0,85** → ξγ_{G,sup} ≅ **1,15** | |

> **Exception géotechnique** : ξ = **1,00** est toujours utilisé pour les applications géotechniques.

#### NOTE 3 du Tableau A2.4(B) — γ_{Sd}

Applicable uniquement si l'approche probabiliste détaillée (Annexe C) est autorisée. Valeurs suggérées :
- γ_{Sd} = **1,05** — constructions isostatiques à faible incertitude de modèle
- γ_{Sd} = **1,10** — constructions intermédiaires
- γ_{Sd} = **1,15** — constructions à haut degré d'hyperstaticité

---

### A2.3.2 Valeurs de calcul des actions dans les situations de projet accidentelles et sismiques

#### Tableau A2.5 ANB — Valeurs de calcul pour les combinaisons accidentelles et sismiques

| Situation | Actions permanentes | Prec. | Action acc./sismique | Action variable principale | Autres |
|-----------|--------------------|----|---------------------|---------------------------|--------|
| Accidentelle (*) (Éq. 6.11a/b) | G_{k,j,sup}, G_{k,j,inf} | P | A_d | ψ_{1,1} Q_{k,1} | ψ_{2,i} Q_{k,i} |
| Sismique (***) (Éq. 6.12a/b) | G_{k,j,sup}, G_{k,j,inf} | P | A_{Ed} = γ_I A_{Ek} | — | ψ_{2,i} Q_{k,i} |

> (*) L'action variable principale est prise avec sa **valeur fréquente** ψ_{1,1} Q_{k,1}.
> (**) Les actions variables sont celles des Tableaux A2.1 ANB à A2.3 ANB.
> (***) Des situations de projet sismiques particulières peuvent être spécifiées pour le projet individuel. Pour les ponts ferroviaires, **une seule voie** est supposée chargée et le modèle de charge SW/2 peut être ignoré.

> NOTE : Le tableau A2.5 ANB implique la valeur **normative γ = 1,0** pour toutes les actions non sismiques, y compris pour la précontrainte.

---

## A2.4 États-limites de service et autres états-limites particuliers

### A2.4.1 Généralités

(1) NOTE 1 : Les coefficients γ pour les actions de trafic et les autres actions pour les ELS sont pris égal à la valeur recommandée **γ = 1,0** pour toutes les combinaisons, y compris pour la précontrainte.

NOTE 2 : Il n'est **en principe pas prévu** de référence aux combinaisons d'actions non-fréquentes pour les critères d'aptitude au service applicables en Belgique.

(2) NOTE : Les critères d'aptitude au service applicables en Belgique sont définis par les clauses A2.4.2 à A2.4.4, par les Eurocodes spécifiques au calcul des ponts, et le cas échéant par le projet individuel. Les critères couvrant les conséquences des déformations sur le profil final et la position des appuis sont à définir pour chaque projet individuel.

### A2.4.2 Critères d'aptitude au service — Ponts routiers

(3) NOTE 2 (belge spécifique) : Il convient de contrôler le **critère de confort défini pour les passerelles en A2.4.3** pour tous les ponts-routes où la circulation des piétons est autorisée.

### A2.4.3 Vérifications de la vibration des passerelles

#### A2.4.3.2 Critères de confort pour les piétons

(1) NOTE : Les valeurs maximales des accélérations recommandées dans l'EN sont **normatives** en Belgique :

| Direction | Accélération maximale normative |
|-----------|--------------------------------|
| Vibrations verticales | **0,7 m/s²** |
| Vibrations horizontales (usage normal) | **0,2 m/s²** |
| Conditions exceptionnelles de foule | **0,4 m/s²** |

---

## A2.4.4 Vérifications relatives aux déformations et aux vibrations pour ponts ferroviaires

### A2.4.4.1 Généralités

(1) NOTE 3 : Les limites de déformation et de vibration pour le dimensionnement des **tabliers auxiliaires** (ouvrages temporaires) sont déterminées par l'organisme responsable de l'infrastructure ferroviaire (Infrabel — voir [www.infrabel.be](//www.infrabel.be)).

(1) NOTE 4 (complément non contradictoire) : Les prescriptions relatives aux ponts mobiles et aux ponts soumis à la fois aux actions ferroviaires et routières sont à fixer par chaque projet individuel.

### A2.4.4.2 Critères pour la sécurité du trafic

#### A2.4.4.2.1 Accélération verticale du tablier

(4)P NOTE : Les valeurs maximales pour les valeurs de crête de l'accélération du tablier sont **normatives** (valeurs recommandées de l'EN) :

| Type de voie | Limite normative |
|-------------|-----------------|
| Voie **ballastée** | γ_bt = **3,5 m/s²** |
| Voie posée **directement** | γ_df = **5,0 m/s²** |

#### A2.4.4.2.2 Gauche du tablier

(2) NOTE : Les valeurs maximales du gauche t [mm/3m] recommandées dans l'EN sont **normatives** pour des tabliers en alignement droit :

| Domaine de vitesse | Valeur normative |
|-------------------|-----------------|
| V ≤ 120 km/h | t₁ = **4,5 mm/3m** |
| 120 < V ≤ 200 km/h | t₂ = **3,0 mm/3m** |
| V > 200 km/h | t₃ = **1,5 mm/3m** |

**Spécificités belges :**
- En cas de **tabliers biais successifs**, la position des charges ferroviaires la plus défavorable doit être recherchée, y compris la répartition à califourchon sur deux tabliers.
- Pour les ouvrages au voisinage de raccordements en courbe, joints de dilatation, aiguillages et croisements : les valeurs maximales sont à fixer pour le **projet individuel**.

(3) NOTE : Le gauche total (tel que défini dans l'EN) est limité à la valeur **normative** :
> t_T = **7,5 mm/3m**

#### A2.4.4.2.3 Déformation verticale du tablier

(1) NOTE : Les valeurs minimales du rapport L/δ sont données par le **Tableau A2.10 ANB** pour les ponts-rails dont :
- la vitesse maximale de ligne V ≤ 220 km/h au point considéré, ET
- la première fréquence propre est dans les limites de la figure 6.10 de la NBN EN 1991-2 avec son ANB.

Les valeurs minimales dans les cas non couverts par le Tableau A2.10 ANB sont fixées par l'organisme responsable de l'infrastructure ferroviaire (Infrabel).

##### Tableau A2.10 ANB — Valeurs minimales du rapport L/δ

| Vitesse V | 1 ou 2 tabliers successifs (L ≤ 25 m) | 1 ou 2 tabliers successifs (L ≥ 30 m) | 3 à 5 tabliers successifs (L ≤ 25 m) | 3 à 5 tabliers successifs (L ≥ 30 m) |
|-----------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
| V ≤ 120 km/h | **600** | **600** | **600** | **900** |
| 120 < V ≤ 200 km/h | **600** | **800** | **1000** | **2200** |
| V > 200 km/h | **800** | **1000** | **1200** | **2200** |

> La flèche verticale totale maximale δ est calculée sur base des actions ferroviaires de l'EN 1991-2 avec son ANB, y compris le coefficient de voie α et le coefficient dynamique Φ.

> L'organisme responsable de l'infrastructure ferroviaire peut fixer d'autres prescriptions sur les flèches/déformations verticales aux ELS, ainsi que sur les contre-flèches à exécuter lors de la construction.

(2) NOTE : Les **limites des rotations** aux extrémités des tabliers sont fixées par les prescriptions de l'organisme responsable de l'infrastructure ferroviaire (Infrabel). Les rotations sont calculées avec les actions mobiles de l'EN 1991-2 avec son ANB, y compris α et Φ.

(3) NOTE : Des limites pour les rotations angulaires des extrémités de tabliers au voisinage des joints de dilatation, aiguillages et croisements sont fixées par les prescriptions d'Infrabel et complétées si nécessaire pour chaque projet individuel.

#### A2.4.4.2.4 Déformation transversale et vibration du tablier

(2) NOTE : Les déformations transversales différentielles maximales à l'extrémité d'un tablier (entre tablier et voie adjacente, ou entre tabliers adjacents) sont fixées par les prescriptions d'Infrabel.

**Tableau A2.8 NOTE 3** : Les valeurs des α_i et r_i recommandées dans l'EN sont **normatives** :

| | α₁ | α₂ | α₃ |
|--|----|----|-----|
| Rotation horizontale max. | **0,0035 rad** | **0,0020 rad** | **0,0015 rad** |

| | r₁ | r₂ | r₃ | r₄ | r₅ | r₆ |
|--|----|----|----|----|----|----|
| Rayon courbure min. (m) | **1700** | **6000** | **14000** | **3500** | **9500** | **17500** |

(3) NOTE : La valeur minimale de la première fréquence propre de vibration latérale d'une travée recommandée dans l'EN est **normative** :
> f_{h0} = **1,2 Hz**

#### A2.4.4.2.5 Déplacement longitudinal du tablier

(1) NOTE (information non contradictoire) : Les valeurs à ne pas dépasser pour les déplacements longitudinaux aux extrémités des tabliers sont données dans **l'EN 1991-2, 6.5.4.5.2 avec son ANB**.

### A2.4.4.3 Valeurs limites de la flèche verticale maximale pour le confort des passagers

#### A2.4.4.3.2 Critères de flèche

(2) NOTE (complément non contradictoire) : La nécessité d'une analyse dynamique de l'interaction véhicule/pont est fixée par l'EN 1991-2, 6.4.4 avec ANB.

(6) NOTE : Les exigences de confort des passagers pour les **tabliers auxiliaires** (ouvrages temporaires) sont fixées par les prescriptions d'Infrabel.

---

Liens : [[EN 1990 ANB — Index]] · [[EN 1990 ANB — 02 — A2 Ponts — Combinaisons et ψ]] · [[EN 1990 ANB — 04 — Annexes B C D — Fiabilité et Classes]] · [[EN 1990 A1 — 02 — A2.3 — États-Limites Ultimes]] · [[EN 1990 A1 — 03 — A2.4 — États-Limites de Service]] · [[PTR CE01 — Ch09 — ELS — FR]] · [[_Knowledge — Index]] · [[CLAUDE]]
