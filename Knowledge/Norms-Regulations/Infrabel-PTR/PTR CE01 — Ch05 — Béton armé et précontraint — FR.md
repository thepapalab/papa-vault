---
title: PTR CE01 Ch05 — Béton armé et précontraint (FR)
type: norm-extract
source: "PTR CE01 Fascicule 1 v1 (Avis 15 I-AM/2022)"
chapters: [5]
tags: [PTR CE01, Infrabel, béton-armé, précontraint, fyk, coefficients-partiels, enrobage, ancrage, fatigue, EC2, FR]
related: ["[[PTR CE01 — Ch05 — RC and Prestressed Concrete]]", "[[PTR CE01 — Index — FR]]", "[[_Knowledge — Index]]"]
created: 2026-06-02
---

# PTR CE01 Ch05 — Béton armé et précontraint (FR)

Les prescriptions de la norme NBN EN 1992 sont d'application sauf dérogations ci-dessous.

---

## 5.1 Calculs et vérifications

> En plus de l'état limite ultime, les états limites de service suivants doivent être contrôlés :
> - limite de contrainte ;
> - maîtrise de la fissuration ;
> - contrôle de la flèche (conditions d'utilisation et de confort compte tenu de la formation de fissures, du retrait et du fluage, ...) ;
> - résistance à la fatigue de l'acier d'armature passive et active.

---

## 5.2 Données pour les calculs

### 5.2.1 Géométrie des sections

> Pour la vérification des états limites de service, des sections homogénéisées peuvent être utilisées à condition d'avoir des armatures adhérentes ou pouvant être considérées comme telles. La section homogénéisée est obtenue par multiplication des sections d'armatures adhérentes par le facteur d'équivalence αe.
>
> Pour des charges de courte durée : αe = Es / Ec
> Pour des charges de longue durée : αe = Es / [Ec · (1 + φ(t,t₀))]

> À défaut de calcul précis, on peut faire l'hypothèse :
> - que pour le béton armé : **αe = 15** pour toutes les charges ;
> - que pour le béton précontraint : **αe = 15** pour des charges de longue durée ; **αe = 6** pour des charges de courte durée.

### 5.2.2 Coefficients partiels de sécurité

> Coefficients partiels relatifs aux matériaux, γc et γs (Tableau 2.1N de la NBN EN 1992-1-1) :

| Situations de projet | γc (béton) | γs (acier BA) | γs (acier BP) |
|---|---|---|---|
| Durable et transitoire | **1,50** | **1,15** | **1,15** |
| Accidentelle | 1,20 | 1,00 | 1,00 |

> Des valeurs supérieures ou inférieures pour le facteur partiel γc peuvent être utilisées à condition d'être justifiées par des procédures de contrôle adéquates :

| Niveau de réception | γc |
|---|---|
| Réception suivie en usine | 1,40 |
| Réception propre | 1,50 |
| Réception restreinte | 1,60 |

### 5.2.3 Détermination de l'effet de la précontrainte

> Les prescriptions suivantes ne concernent que les armatures précontraintes complètement enrobées de béton. L'emploi d'autres armatures de précontrainte (précontrainte sans adhérence, etc.) n'est pas autorisé, sauf mention contraire au cahier spécial des charges.

### 5.2.4 Effets structurels de déformations différées

> En général, l'effet du retrait et du fluage ne doit être considéré que dans l'état limite de service, sauf lorsque des effets de deuxième ordre sont importants.
> Pour déterminer les pertes de précontrainte, il faut tenir compte des effets du retrait et du fluage et de l'effet de la relaxation de l'armature précontrainte.

---

## 5.3 Béton

> Dans les cas courants, on peut prendre **24 kN/m³** comme poids volumique pour du béton non armé et **25 kN/m³** pour du béton armé et précontraint à pourcentage normal d'armature.

### 5.3.1 Résistance

> Pour les ouvrages d'art, la classe de résistance minimum est **C30/37** et la classe de résistance maximum est **C90/105**.

### 5.3.2 Fluage

> La déformation de fluage du béton à l'instant t :
> εcc(t,t₀) = φ(t,t₀) · (σc / Ec)
> où Ec est le module tangent du béton à 28 jours, pris égal à **1,05 Ecm**.

---

## 5.4 Acier d'armature passive

### 5.4.1 Domaine d'application

> Seuls les aciers d'armature de qualité **B500B** suivant l'annexe C de la norme NBN EN 1992-1-1 peuvent être utilisés dans les ouvrages d'art. Selon la nomenclature belge, les nuances d'acier répondant à la qualité B500B sont celles reprises dans la PTV 302 de l'OCAB, sous la mention **BE 500…**
>
> L'utilisation d'aciers d'armature de qualité B500A, c'est-à-dire de nuance DE 500 BS selon la nomenclature belge reprise dans la PTV 303 de l'OCAB, est donc **interdite** dans les ouvrages d'art.

> Toutefois, pour les armatures de nuance BE 500, il faut considérer qu'elles possèdent les caractéristiques mécaniques de la nuance BE 400 : **fyk vaut donc 400 N/mm²** pour les calculs de résistance.

### 5.4.2 Hypothèses de calcul

> La masse volumique des armatures peut être supposée égale à **7 850 kg/m³**.
> La valeur de calcul du module d'élasticité Es peut être supposée égale à **200 000 N/mm²**.

### 5.4.3 Géométrie

> On utilise de préférence les barres de diamètres nominaux suivants : **Ø = 6 – 8 – 10 – 12 – 14 – 16 – 20 – 25 et 32 mm**.
> On essaiera autant que possible de ne pas utiliser des barres de grand diamètre et ce, pour limiter la fissuration, à savoir des barres dont le diamètre est supérieur à 32 mm.

---

## 5.5 Acier de précontrainte

> La valeur de calcul du module d'élasticité Ep peut être prise égale à **205 000 N/mm²** pour les fils et les barres et à **195 000 N/mm²** pour les torons.

**Relaxations :**

> Les pertes de précontrainte avec le temps peuvent être assimilées à une valeur forfaitaire de **15** ou **20 %** de la force de précontrainte initiale (respectivement pour des conditions climatiques extérieures et intérieures).

---

## 5.6 Durabilité et enrobage des armatures

**Tableau 5.6.1 — Prescription du béton et enrobage dans les cas les plus courants :**

| Description | Spécification | cnom / cmin |
|---|---|---|
| Béton de propreté (env. non agressif) | C16/20 – BNA – E0 | — |
| Éléments BA, gel, pas de pluie | C25/30 – BA – EE2 – WAI(0,50) | 40 mm / 30 mm |
| Éléments BA, gel + pluie | C30/37 – BA – EE3 – WAI(0,50) | 45 mm / 35 mm |
| Éléments BA, gel + agents de déverglaçage | C35/45 – BA – EE4 – WAI(0,45) | 60 mm / 50 mm |
| **Ouvrages d'art — éléments structurels** | **C35/45 – BA – EE4 – WAI(0,45)** | **60 mm / 50 mm** |
| Béton précontraint, bâtiments | C50/60 – BP – EE3 – WAI(0,50) | 35 mm / 25 mm |
| **Béton précontraint, ouvrages d'art** | **C50/60 – BP – EE4 – WAI(0,45) – Cl 0,10** | **50 mm / 40 mm** |
| Fondations sur pieux (pas de pluie) | C30/37 – BA – EE2, EA1 – ciment ≥ 375 kg/m³ | **75 mm** |

> S'il y a une différence dans la spécification des performances du béton, la spécification la plus exigeante s'applique.

**Fissuration — structures en contact avec l'eau souterraine :**

> Pour les ouvrages en contact permanent avec l'eau souterraine (comme les cadres), la largeur des fissures doit être limitée à **0,2 mm** afin d'assurer l'étanchéité et la durabilité.

---

## 5.7 Dispositions constructives des armatures

### 5.7.1 Ancrages

> La valeur de calcul de la longueur d'ancrage lbd est égale à :
> **lbd = α1 α2 α3 α4 α5 · lb,rqd ≥ lb,min**

> Les longueurs d'ancrage sont calculées avec la résistance du BE500.

> Toutes les longueurs d'ancrage sont déterminées sur base des hypothèses suivantes :
> - contrainte maximale dans les barres (σsd = fyk/1,15) ;
> - conditions d'adhérence "médiocres" ;
> - coefficients α1, α2, α3, α4 et α5 sont fixés à 1.

**Tableau 5.1 — Longueur d'ancrage lbd en mm pour BE500 (extrait) :**

| Ø (mm) | fck 25 | fck 30 | fck 35 | fck 40 | fck 50 |
|---|---|---|---|---|---|
| 10 | 580 | 510 | 460 | 420 | 360 |
| 12 | 690 | 610 | 550 | 510 | 440 |
| 16 | 920 | 820 | 740 | 670 | 580 |
| 20 | 1150 | 1020 | 920 | 840 | 730 |
| 25 | 1440 | 1280 | 1150 | 1050 | 910 |
| 32 | 1840 | 1630 | 1470 | 1350 | 1160 |

*(Tableau complet pour fck 20–70 : PTR §5.7.2.1, Tableau 5.1)*

> Attention, ce Tableau 5.1 ne peut pas être utilisé dans le cadre de l'ancrage des barres d'armature "collées" dans des trous percés. Dans ce cas, il faut utiliser la méthode du Technical Report 23 de l'EOTA.

### 5.7.2 Recouvrements

> La valeur de calcul de la longueur de recouvrement l0 est égale à :
> **l0 = α1 α2 α3 α4 α5 α6 · lb,rqd ≥ l0,min**
> avec l0,min > max{0,3 · α6 · lb,rqd ; 15Ø ; 200 mm}

> Dans la zone de recouvrement, des armatures transversales sont requises afin de pouvoir compenser les efforts transversaux de traction, conformément au §8.7.4 de la norme NBN EN 1992-1-1.

**Tableau 5.2 — Longueur de recouvrement l0 en mm, BE500 (extrait fck 30 et fck 40) :**

| Ø (mm) | fck 30, <25% | fck 30, 50% | fck 40, <25% | fck 40, 50% |
|---|---|---|---|---|
| 12 | 610 | 860 | 510 | 710 |
| 16 | 820 | 1140 | 670 | 940 |
| 20 | 1020 | 1430 | 840 | 1180 |
| 25 | 1280 | 1790 | 1050 | 1480 |
| 32 | 1630 | 2290 | 1350 | 1890 |

*(Tableaux complets pour fck 20–60 : PTR §5.7.2.2, Tableau 5.2)*

### 5.7.3 Soudage

> La réalisation de soudures sur le chantier est interdite (conditions pas idéales). Sauf prescriptions contraires, les cordons structurels sont absolument interdits. **Souder des armatures est interdit.**

Exceptions (vérification à la fatigue non requise) : fondations ; piles et poteaux non rigidement reliés au tablier ; culées des ponts non rigidement reliés au tablier (sauf dalles de culées creuses) ; passerelles (sauf éléments sensibles au vent).

### 5.7.4 Dispositions d'armatures dans les angles

> Dans tous les angles formés par des poutres, des colonnes, des dalles, des parois, etc. de structures en béton, les coudes des armatures ne peuvent pas suivre le côté intérieur des angles, pour éviter le phénomène de **poussée au vide**. Cette exigence reste également d'application lorsque l'intérieur de l'angle est renforcé par un chanfrein, et pour les éléments préfabriqués en béton.

---

## 5.8 Calcul des sections

### 5.8.1 Flexion à l'ELU

> Pour définir le moment de résistance à l'état limite ultime, il ne faut pas tenir compte de la résistance à la traction du béton.

### 5.8.2 Calcul des éléments en béton précontraint

> Sous toutes les combinaisons de charge en phase finale, **toutes les fibres du béton doivent être comprimées**.

> Dans le cas d'un concept élastique d'éléments en béton précontraint, les tensions normales sont limitées suivant :

| Combinaison de charge | σc,adm | σct,adm |
|---|---|---|
| g + P | 0,5 fck(t) | fct0,05 |
| Combinaisons permanentes uniquement | 0,45 fck | 0 |
| Combinaisons fréquentes | 0,5 fck | 0 |

> Selon la NBN EN 1990 ANB §A2.4.1. et la NBN EN 1991-2 ANB §2.2, les valeurs de calcul non-fréquentes ne sont pas utilisées pour le calcul d'ouvrage d'art. **Seules, les combinaisons fréquentes doivent être considérées.**

---

## 5.9 Résistance à la fatigue des tabliers en béton

### 5.9.1 Généralités

> Une vérification à la fatigue n'est généralement pas nécessaire pour :
> a. passerelles, à l'exception des éléments de structure très sensibles à l'action du vent ;
> b. structures enterrées en voûte ou en cadre avec une couverture minimale de terre de **1,00 m** et **1,50 m** respectivement pour les ponts routiers et ferroviaires ;
> c. fondations ;
> d. piles et poteaux non rigidement reliés au tablier ;
> e. murs de soutènement de chaussées et de voies ferrées ;
> f. culées des ponts non rigidement reliés au tablier (sauf dalles de culées creuses) ;
> g. armatures de précontrainte et armatures de béton armé, dans les zones où, sous combinaison fréquente d'actions avec Pk, les fibres extrêmes du béton restent comprimées.

> Le calcul des contraintes doit être réalisé en faisant l'hypothèse de sections fissurées, en négligeant la résistance en traction du béton mais en assurant la compatibilité des déformations.

### 5.9.3 Vérification de l'état limite de fatigue

> Pour des cycles multiples d'étendue variable, l'endommagement peut être cumulé en appliquant la **règle de Palmgren-Miner**.

**Assemblages par organes mécaniques (manchons) :**

> Outre l'effort de traction de la liaison barre-manchon-barre, la résistance à la fatigue de l'assemblage doit également être connue pour au moins **2 millions de cycles**. L'aptitude de ces organes mécaniques doit être démontrée par un certificat d'agrément. Les essais s'effectuent sur un minimum de **3 échantillons** par type de manchon et par diamètre de barre utilisé.

### 5.9.4 Méthode simplifiée (annexe NN de la NBN EN 1992-2)

**Ponts-rails :**

> $$\Delta\sigma_{s,equ} = \lambda_s \cdot \Phi \cdot \Delta\sigma_{s,71}$$
> où Δσs,71 est l'étendue de contrainte de l'acier due au modèle de charge 71 appliqué au maximum sur deux voies, **sans tenir compte du coefficient de classification α**, et Φ le coefficient dynamique.

**Ponts-routes (modèle de charge de fatigue 3 modifié) :**

> Les charges d'essieu doivent être multipliées par :
> - **1,75** pour une vérification au droit des appuis intermédiaires des ponts continus ;
> - **1,40** pour une vérification dans d'autres zones.
>
> $$\Delta\sigma_{s,equ} = \Delta\sigma_{s,EC} \cdot \lambda_s$$
> avec λs = φfat · λs,1 · λs,2 · λs,3 · λs,4
> φfat = **1,2** pour les surfaces de bonne rugosité ; φfat = **1,4** pour les surfaces de rugosité moyenne.

---

Liens : [[PTR CE01 — Index — FR]] · [[PTR CE01 — Ch04 — Fondations — FR]] · [[PTR CE01 — Ch06 — Acier — FR]] · [[PTR CE01 — Ch09 — ELS — FR]] · [[PTR CE01 — Ch05 — RC and Prestressed Concrete]]
