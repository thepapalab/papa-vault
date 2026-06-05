---
title: PTR CE01 Ch07 — Mixte acier-béton (FR)
type: norm-extract
source: "PTR CE01 Fascicule 1 v1 (Avis 15 I-AM/2022)"
chapters: [7]
tags: [PTR CE01, Infrabel, mixte, acier-béton, préflex, connexion-cisaillement, EC4, FR]
related: ["[[PTR CE01 — Ch07 — Composite Steel-Concrete]]", "[[PTR CE01 — Index — FR]]", "[[_Knowledge — Index]]"]
created: 2026-06-02
---

# PTR CE01 Ch07 — Constructions mixtes acier-béton (FR)

Les prescriptions de la norme NBN EN 1994 sont d'application sauf dérogations ci-dessous. Les chapitres 5 et 6 sont pleinement d'application à ces constructions.

---

## 7.1 Domaine d'application

> Les prescriptions du présent chapitre sont d'application pour les constructions où tant le béton que l'acier contribuent à la résistance de l'élément structurel. Les deux matériaux agissent ensemble si bien qu'il doit y avoir une forte adhérence entre les deux.

---

## 7.3 Concepts-types pour la construction de ponts

### 7.3.1 Tabliers à poutres enrobées

> Dans le cas de profilés enrobés de béton, on se trouve dans les conditions requises pour pouvoir compter sur une contribution suffisante de l'adhérence naturelle entre le profilé en acier et le béton. Les profilés ne sont, en général, pas pourvus de connecteurs. Ceci n'est cependant permis qu'à condition qu'un certain nombre de règles technologiques (voir §6.3 de la NBN EN 1994-2) soient respectées, et que la fissuration soit limitée.

> Les profilés en acier sont pourvus d'orifices forés, d'une part, pour permettre le passage des armatures transversales du tablier de pont et, d'autre part, pour y fixer les tiges filetées. En guise de critère, les tensions à l'état limite de service sont limitées à **fyk/3**.

> Les tiges filetées sont placées en alternance. La distance entre les tiges filetées équivaut à environ **1/4 de la travée**, avec un minimum de **3 m**.

> L'armature transversale minimale est de **3 barres d'armature par mètre de Ø 16 mm**, sur toute la surface de ce tablier de pont.
> Une armature transversale minimale dans la partie supérieure doit atteindre au moins la moitié du pourcentage d'armature transversale présente dans la partie inférieure, avec un minimum de **5 barres Ø 10 mm par mètre**.

### 7.3.2 Tabliers de ponts avec poutres préfléchies et précontraintes

> Les prescriptions ci-après concernent les poutres en acier enrobées de béton dont au moins la semelle inférieure des poutres en acier est enrobée de béton en usine (première phase du béton). Pendant ce bétonnage, la partie inférieure de la poutre métallique est soumise à de la traction.

> Après durcissement du béton d'enrobage (de classe minimale **C35/45**), la flexion est relâchée, et la précontrainte est transmise au béton.

> Les forces de préflexion s'exercent sur une poutre qui repose simplement sur ses points d'appui théoriques. Ces forces sont dirigées vers le bas et s'appliquent à une distance de l'appui le plus proche, égale au **quart de la portée**. Les forces de préflexion ne contribuent pas à l'état limite ultime.

**Nuance de l'acier :**

> L'acier des poutres métalliques est au moins de type **S355J2**, puisqu'une grande ductilité est requise.

**Phases d'exécution (voir Tableau 7.1 du PTR) :**

> 1. Élastification de la poutre en acier — Les poutres sont chargées de telle manière que, sur toute la portée, les contraintes dans l'acier soient au moins égales à celles à l'état limite de service. L'élastification est poursuivie jusqu'à ce que la différence de flèche entre deux charges successives soit inférieure à **3 %**.
>
> 2. Préflexion de la poutre en acier avec deux forces de préflexion.
>
> 3. Bétonnage de la semelle inférieure (béton de première phase, classe ≥ C35/45).
>
> 4. Enlèvement des forces de préflexion et découpe de l'armature de précontrainte.
>
> 5. Bétonnage de la phase précontrainte par post-tension (si prévue) — la poutre est soutenue intégralement sur sa longueur de telle sorte que le béton coulé durant cette phase **n'exerce aucune charge sur la poutre**.
>
> 6. Mise en tension des câbles de précontrainte par post-tension — durant cette précontrainte, la poutre se soulève de son coffrage et ne repose que sur ses points d'appui.
>
> 7. Bétonnage de la dernière phase (dalle de compression) — le béton de 2ème phase situé juste au-dessus du béton de 1ère phase se trouve généralement dans la zone tendue. Des armatures passives complémentaires sont nécessaires.

**Précautions hivernales pour l'injection des gaines (1er novembre – 15 mars) :**

> a) sans mortier d'injection : évacuer toutes les eaux de la gaine au moyen d'air sous pression. Les gaines sont ensuite remplies d'un liquide non corrosif avec un antigel. Le liquide ne peut geler à une température supérieure à **-20 °C**.
>
> b) avec mortier d'injection : soit la construction en béton est maintenue à une température d'au moins **5 °C** durant toute la période d'injection jusqu'à la fin de la prise du mortier ; soit par adjonction d'un antigel approprié au mortier d'injection.

**Application type :**

> L'exemple-type de tabliers de ponts-rails avec des poutres en acier préfléchies et précontraintes est celui des **"ponts en auge"** ou **"ponts bacs"** — tablier de pont entièrement préfabriqué, largeur de la dalle ≈ 4 m.
> Lors de la conception, il faut veiller à ce que le béton de la dalle du tablier (béton de première phase) reste toujours comprimé en service.

---

## 7.4 Élaboration du projet

### 7.4.2 État limite de service

> Pour les états limites de service, il convient d'utiliser une méthode de calcul élastique, avec des corrections adéquates pour les effets non linéaires (comme la fissuration dans le béton) et moyennant l'utilisation de sections homogénéisées.

> À défaut de disposition précise, on fait l'hypothèse d'un coefficient d'équivalence fictif :
> $$n_L = n_0 (1 + \psi \cdot \varphi)$$
> où n0 = Ea/Ecm ; φ = coefficient de fluage du béton ; ψ = coefficient de réduction dépendant de As/Ac.

**Valeurs forfaitaires de ψ (t → ∞, à ciel ouvert) :**

| As/Ac | ψ |
|---|---|
| 0,03 | 1,25 |
| 0,05 | 1,00 |
| ≥ 0,10 | 0,65 |

*(Interpolation linéaire pour les valeurs intermédiaires)*

**Limites de contraintes lors de la préflexion :**

> - Dans la poutre en acier : σ ≤ **0,75 fyk**
> - Dans le béton au moment du déblocage : σc ≤ **0,8 fck** (résistance à la compression du béton en vigueur à ce moment-là), afin de limiter les fissures.

---

## 7.5 Liaison entre l'acier et le béton

### 7.5.1 Connecteurs

> Une connexion et une armature transversale doivent être appliquées afin de transmettre le cisaillement longitudinal entre le béton et l'élément en acier de construction, **en négligeant l'adhérence naturelle** entre les deux (NBN EN 1994-2, §6.6).

**Goujons à tête :**

> Les goujons à tête avec un diamètre de tige d de maximum **22 mm** et une hauteur ≥ **4d** sont presque toujours des connecteurs ductiles, pour autant qu'un degré de liaison minimum soit respecté.

**Connecteurs rigides :**

> Ces connecteurs sont de nature très rigide. Leur fonctionnement s'effectue par écrasement du béton contre la face arrière du connecteur. Les connecteurs rigides doivent être considérés comme cassants.
>
> La contrainte de cisaillement limite d'un goujon rigide s'élève à :
> $$V_{Rd} = \eta \cdot A_{f1} \cdot f_{ck} / \gamma_c$$
> où η = Af2/Af1 avec un maximum de **2,5** pour le béton à base de gravier, et de **2,0** pour le béton léger.
>
> Les soudures doivent être calculées pour résister à **1,2 VRd**.

### 7.5.2 Liaison entièrement et parfaitement résistante au cisaillement

> Une liaison est entièrement résistante au cisaillement si une augmentation du nombre d'organes de liaison n'entraîne pas d'augmentation de la valeur de calcul du moment résistant de l'élément.

> Le degré de liaison est défini par : **η = N/Nf**, où Nf correspond au nombre de connecteurs nécessaires pour atteindre le moment résistant de l'élément mixte MRd.

> Les limites d'utilisation de liaison partiellement résistante au cisaillement sont reprises à la Figure 7.6 (assurer la ductilité des goujons et assurer un degré de liaison minimal).
> Dans tous les cas, le contrôle de la résistance de la liaison doit être réalisé à l'état limite ultime.

---

Liens : [[PTR CE01 — Index — FR]] · [[PTR CE01 — Ch05 — Béton armé et précontraint — FR]] · [[PTR CE01 — Ch06 — Acier — FR]] · [[PTR CE01 — Ch09 — ELS — FR]] · [[PTR CE01 — Ch07 — Composite Steel-Concrete]]
