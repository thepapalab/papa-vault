---
title: PTR CE01 Ch09 — États limites de service (FR)
type: norm-extract
source: "PTR CE01 Fascicule 1 v1 (Avis 15 I-AM/2022)"
chapters: [9]
tags: [PTR CE01, Infrabel, ELS, flèche, rotation, gauche, L-sur-F, ponts-rails, EC0, FR]
related: ["[[PTR CE01 — Ch09 — SLS]]", "[[PTR CE01 — Index — FR]]", "[[PTR CE01 — Ch03 — Actions — FR]]", "[[_Knowledge — Index]]"]
created: 2026-06-02
---

# PTR CE01 Ch09 — État limite de service (FR)

Les prescriptions de la norme NBN EN 1990 et de son annexe A2 (ponts) sont d'application sauf dérogations ci-dessous.

> Selon la NBN EN 1990 ANB §A2.4.1. et la NBN EN 1991-2 ANB §2.2, les valeurs de calcul non-fréquentes ne sont pas utilisées pour le calcul d'ouvrage d'art. **Seules, les combinaisons fréquentes doivent être considérées.**

---

## 9.1 État limite de service pour les ouvrages d'art

### 9.1.1 Définitions

> Les déformations de pont engendrées par les actions doivent être limitées pour les raisons suivantes : la sécurité ; le confort des voyageurs.

**Déformées verticales :**

> - **yt** : le profil en long théorique du revêtement routier ou des rails (correspond au tracé idéal) ;
> - **yp** : la déformée sous charges permanentes. Les effets différés éventuels dus au retrait et au fluage du béton sont à considérer à l'âge de la mise en service et à terme. Pour les ponts-rails, yp correspond à la position des rails sous l'action des charges permanentes ;
> - **ys** : la déformée des longerons sous charges variables. Pour les ponts-rails, ys correspond à la position des rails sous l'action des charges mobiles et des gradients extrêmes de température ;
> - **y1** : la déformée des poutres maîtresses sous charges variables ;
> - **y2** : la déformée des entretoises sous charges variables.

> **F** : La flèche maximale est la distance verticale maximale entre les déformées ys et toute droite qui joint deux points quelconques de ces déformées.
> **F/L** : La flèche maximale relative est le rapport entre la flèche maximale et la distance horizontale entre les points respectifs.

**Contre-flèches :**

> Les tabliers de pont dont le bord inférieur est théoriquement droit sont posés de façon à ce que leurs flèches en conditions de service ne donnent aucune impression de "fléchissement". C'est pourquoi l'ensemble de la superstructure est posé avec une contre flèche. La valeur imposée de cette contre-flèche doit exister après la finition complète du pont et la mise en œuvre de toutes les charges permanentes.

> En principe, la superstructure des ponts-rails doit présenter une contre-flèche de **L/1000**, sauf pour les très grandes portées. Pour les très grandes portées (à partir de 100 m), la contre-flèche est limitée à **L/2000**.

**Gauche :**

> Si l'on considère quatre roues des deux essieux d'un bogie de train, le gauche t est la distance d'une roue par rapport au plan déterminé par les points de contact sur les rails des trois autres roues.

> Le gauche est également la différence des deux dévers mesurés (base mobile) à une distance de **3 m** et pour un écartement entre rails de **s = 1,435 m**.

> Afin de limiter le gauche, le biais des ouvrages ballastés ou à fixation directe doit être supérieure à **45°**, sauf cas exceptionnel avec l'accord du maître d'ouvrage.

**Rotation angulaire :**

> Les rotations angulaires sont les angles formés aux extrémités des tabliers entre, d'une part, les tangentes aux déformées ys et, d'autre part, le profil en long théorique yt.

---

### 9.1.2 Déformations des ponts-routes

> En combinaison de charges fréquente, la flèche maximale relative F/L est limitée à **1/700**.

---

### 9.1.3 Déformations des passerelles

> En combinaison de charges fréquente, la flèche maximale relative F/L est limitée à **1/300**.

> Si la fréquence vibratoire fondamentale f0 de la passerelle est > à **5 Hz**, aucun problème vibratoire n'est à craindre.
> Si f0 est < à 5 Hz, un contrôle vibratoire sera réalisé selon la méthodologie des guides de conception Setra ou HiVoSS.

---

### 9.1.4 Déformations des ponts-rails

#### 9.1.4.1 Limitation de la flèche verticale

> La flèche verticale est déterminée sous la valeur caractéristique du modèle de charge 71 (et SW/0 et SW/2 aux endroits requis), multipliée par le facteur dynamique Φ et le facteur de classification α.

**Tableau 9.1 — Limites inférieures du rapport L/F :**

| Cas | L/F minimum |
|---|---|
| Voie unique, voie ballastée | 600 (L ≤ 20 m) → 500 (L ≥ 30 m) |
| Voie unique, fixation directe | 900 (L ≤ 20 m) → 800 (L ≥ 30 m) |

*(Interpolation linéaire entre 25 m et 30 m. Tableau complet : PTR §9.1.4.1)*

> La contre-flèche permet de réduire la flèche maximale F. La contre-flèche doit cependant être compatible avec les contre-rotations angulaires admises.

> Si les rails sont fixés directement à la superstructure, sans lit de ballast, la contre-flèche minimale autorisée, en permanence sous l'effet des charges fixes et des températures, s'élève à **40 %** des valeurs admissibles selon le Tableau 9.1.

> En règle générale, la superstructure des ponts-rails doit être posée avec une contre-flèche de **L/1000**. La contre-flèche est calculée à l'état limite de service sous charges permanentes (propre poids, charge fixe, ballast et voie).

> Le déplacement vertical de la face supérieure du tablier par rapport à la construction adjacente (culée ou autre tablier) à la suite de charges variables ne peut pas excéder les valeurs limites suivant le §6.5.4.5.2 de la norme NBN EN 1991-2.

#### 9.1.4.2 Limitation des rotations angulaires

> La rotation angulaire à l'extrémité du tablier de pont est déterminée sous la valeur caractéristique du modèle de charge 71 (et SW/0 et SW/2 aux endroits requis), multipliée par le facteur dynamique Φ et le facteur de classification α, et prend en compte les effets de la température.

**Rotations angulaires maximales admissibles :**

> - pour les tabliers de voie ballastés :
>   - θ⁻ = **0,0065 rad** pour la transition entre le tablier et la pleine voie ;
>   - θ⁺ = **0,0100 rad** pour deux tabliers successifs.
> - pour les tabliers de voie non ballastés :
>   - θ⁻ = **0,0050 rad** pour la transition entre le tablier et la pleine voie ;
>   - θ⁺ = **0,0050 rad** pour deux tabliers successifs.

**Contre-rotation angulaire initiale :**

> Si les rails sont fixés directement à la superstructure, sans lit de ballast, la contre-rotation angulaire maximale θp, en permanence sous l'effet des charges fixes et des températures, s'élève à **40 %** de la rotation angulaire admissible θ⁻.

#### 9.1.4.3 Limitation du gauche dû à la déformation du pont

> Le gauche du tablier de pont est déterminé sous la valeur caractéristique du modèle de charge 71 (et SW/0 et SW/2 aux endroits requis), multipliée par le facteur dynamique Φ et le facteur de classification α.

**Pour des voies en alignement, le gauche admis pour une distance entre essieux de 3 m :**

| Vitesse V (km/h) | Gauche maximal |
|---|---|
| V < 120 | **4,5 mm** |
| 120 ≤ V < 200 | **3 mm** |
| V ≥ 200 | **1,5 mm** |

> Pour deux tabliers biais successifs, il convient de rechercher la position la plus défavorable du bogie situé éventuellement "à cheval" sur les deux tabliers. La torsion totale tT doit être limitée à **7,5 mm/3 m**.

#### 9.1.4.4 Limitation de la déformation horizontale

> Le déplacement horizontal doit être contrôlé pour la combinaison comprenant le modèle de charge 71 (et si requis SW/0), multiplié par le facteur dynamique Φ et le facteur de classification α, et les effets de la température.

> La déformation horizontale du tablier ne peut pas induire :
> - de variation angulaire horizontale supérieure aux valeurs indiquées dans le Tableau A2.8 de la norme NBN EN 1990/A1 ;
> - de rayon de courbure horizontale inférieur aux valeurs indiquées dans le Tableau A2.8 de la norme NBN EN 1990/A1.

---

## 9.2 État limite de service pour les bâtiments

> Dans l'état limite de service, les flèches ne peuvent dépasser **1/300** de la portée ou **1/200** si l'élément est en porte-à-faux. Les flèches de poutres qui supportent des éléments ou revêtements susceptibles d'être détériorés à cause des déformations ne peuvent être supérieures à **1/500** de la portée.

---

Liens : [[PTR CE01 — Index — FR]] · [[PTR CE01 — Ch03 — Actions — FR]] · [[PTR CE01 — Ch05 — Béton armé et précontraint — FR]] · [[PTR CE01 — Ch08-10-12-14 — Dispositions restantes — FR]] · [[PTR CE01 — Ch09 — SLS]]
