---
title: PTR CE01 Ch06 — Acier (FR)
type: norm-extract
source: "PTR CE01 Fascicule 1 v1 (Avis 15 I-AM/2022)"
chapters: [6]
tags: [PTR CE01, Infrabel, acier, ponts, fatigue, lambda, soudure, boulons, EC3, FR]
related: ["[[PTR CE01 — Ch06 — Steel]]", "[[PTR CE01 — Index — FR]]", "[[_Knowledge — Index]]"]
created: 2026-06-02
---

# PTR CE01 Ch06 — Constructions en acier (FR)

Les prescriptions de la norme NBN EN 1993 sont d'application sauf dérogations ci-dessous.

---

## 6.2 Conceptions imposées pour la construction de ponts

> En principe, tous les ponts-rails en acier doivent être munis d'un **coffre à ballast**, pour pouvoir poser la voie sur un lit de ballast. Les ponts mobiles font exception à cette règle.

> L'épaisseur d'âme minimale des poutres principales, longerons et entretoises métalliques s'élève à **10 mm** pour les poutres composées.

> Sauf disposition contraire dans le cahier spécial des charges, les sections des éléments porteurs de la construction de classe 1, 2 ou 3 sont des sections conformes au Tableau 5.2 de la NBN EN 1993-1-1. Pour des sections de classe 4, il y a lieu de tenir compte de la résistance réduite par les effets de voilement local.

---

## 6.3 Qualités d'acier à utiliser

### 6.3.1 Qualités pour la construction de ponts

> La limite élastique de l'acier de construction ne peut pas excéder **460 N/mm²**.

> Le choix de la qualité d'acier dépend de la conception du pont, de la méthode d'exécution utilisée, des circonstances de traitement et des conditions d'utilisation de l'ouvrage d'art. La qualité est déterminée selon le tableau 2.1 de la NBN EN 1993-1-10. On emploie :

> 1. les classes **J2, K2, M, N, ML et NL** (+N) pour les éléments principaux soudés de toutes les épaisseurs et pour les éléments principaux comprimés d'une épaisseur ≥ 15 mm. Et donc pour : les poutres principales, entretoises, longerons de construction soudée ; les plaques de tablier pour dalle orthotrope ; toutes les tôles et profils soudés de poutres, de barres de treillis ou d'arcs de caisson ; tous les profils soudés de la structure portante.

> 2. la classe **J0** dans les éléments soudés comprimés d'une épaisseur < 15 mm et les tôles et profils non soudés.

> 3. la classe **JR** pour les tôles et les profils dans les contreventements non soudés et les passerelles reliées à la superstructure.

### 6.3.2 Qualités pour la construction de bâtiments

**Tableau 6.1 — Qualités d'acier pour bâtiments (extrait) :**

| Cas | Acier |
|---|---|
| Garde-corps, tôle armée, élément non chargé | S235JR |
| Construction soudée, charges statiques lourdes ou dynamiques légères | S235J0 |
| Construction soudée, charges dynamiques lourdes, épaisseur ≤ 10 mm | S235J0 |
| Construction soudée, charges dynamiques lourdes, épaisseur > 10 mm | S235J2 / S355K2 |
| Chemin de roulement pont roulant | E295 |

---

## 6.4 Assemblages

### 6.4.1 Conception

> Seuls les assemblages suivants peuvent être mis en œuvre :
> - soudure à l'arc (manuelle, automatique ou semi-automatique) ;
> - assemblages boulonnés chargés en cisaillement suivant cat. A (travaillant à la pression diamétrale) ou cat. C (résistant au glissement à l'état limite ultime) du Tableau 3.2 de la NBN EN 1993-1-8 ;
> - assemblages boulonnés soumis à des charges de traction suivant cat. D (non précontraints) ou cat. E (précontraints). Les boulons de cat. D ne peuvent pas être utilisés dans des assemblages soumis à une charge de traction variable.

> L'usage de boulons non calibrés est exclusivement permis pour des assemblages moins importants (pour des éléments non porteurs) chargés en cisaillement.

### 6.4.2 Assemblages par soudure

> Sauf mention contraire dans le cahier spécial des charges, les types d'assemblage par soudure suivants sont imposés :
> - liaison âme-semelles des longerons, entretoises, poutres principales : **cordon en K à pleine pénétration** ;
> - sections fermées (poutres-caisson) : soudures d'angle avec préparation et reprise à l'envers ; si l'intérieur n'est pas accessible après fermeture : soudure d'angle d'un côté ;
> - cordons de soudure bout à bout : **cordon en X complet avec meulage postérieur** ;
> - assemblages perpendiculaires : soudures d'angle.

> La détermination de la résistance d'une soudure d'angle à forte pénétration ne peut pas tenir compte de la forte augmentation de la gorge (voir §4.5.2 de la NBN EN 1993-1-8).

> L'emplacement des soudures bout à bout est choisi judicieusement de sorte que les variations de contraintes et les contraintes totales y soient les plus petites possibles. Le choix ne doit certainement pas être influencé en premier lieu par les dimensions commerciales des éléments en acier.

### 6.4.3 Joints de montage

> Le nombre de joints de montage est limité au strict minimum. En principe, les assemblages doivent avoir la même résistance que la section des éléments qu'ils lient **(joint d'égale résistance)**.

---

## 6.5 Prescriptions particulières relatives à la fatigue dans la construction de ponts

> L'attention est attirée sur le fait que le dimensionnement en fatigue peut être décisif, et **ne peut donc pas être considéré comme un contrôle ultérieur**. Il convient d'en tenir compte lors des différents stades des calculs.

### 6.5.1 Fatigue des ponts-routes

> Dans le cas des modèles de charge de fatigue 1 et 2, la vérification de l'inégalité FfΔσE,2 ≤ Δσc / γMf peut être ramenée à :
> $$\Delta\sigma_D \leq 0{,}74 \cdot \Delta\sigma_c / \gamma_{Mf}$$

> Le facteur de dommage équivalent λ :
> $$\lambda = \lambda_1 \cdot \lambda_2 \cdot \lambda_3 \cdot \lambda_4 \leq \lambda_{max}$$

> - λ1 : longueur d'influence L (Figure 9.5 NBN EN 1993-2) ;
> - λ2 : composition et fréquence du trafic (Tableau 4.7 NBN EN 1991-2) ;
> - λ3 : durée de vie de 100 ans → **λ3 = 1,0** ;
> - λ4 : nombre de bandes de circulation (NBN EN 1993-2 §9.5.2).

### 6.5.2 Fatigue des ponts-rails

> $$\lambda = \lambda_1 \cdot \lambda_2 \cdot \lambda_3 \cdot \lambda_4 \leq \lambda_{max} = \mathbf{1{,}4}$$

> - λ1 : longueur d'influence, trafic EC-mix (Tableau 9.3 NBN EN 1993-2) ;
> - λ2 : tonnage annuel remorqué (prescrit par le maître de l'ouvrage) ;
> - λ3 : durée de vie de 100 ans → **λ3 = 1,0** ;
> - λ4 : tabliers à double voie — probabilité réduite de chargement simultané le plus défavorable (NBN EN 1993-2 §9.5.3).

---

Liens : [[PTR CE01 — Index — FR]] · [[PTR CE01 — Ch05 — Béton armé et précontraint — FR]] · [[PTR CE01 — Ch07 — Mixte acier-béton — FR]] · [[PTR CE01 — Ch06 — Steel]]
