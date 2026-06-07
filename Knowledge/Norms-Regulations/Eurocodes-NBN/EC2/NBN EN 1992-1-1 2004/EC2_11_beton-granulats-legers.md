---
title: "NBN EN 1992-1-1:2004 — Beton granulats legers"
type: norm-extract
source: "NBN EN 1992-1-1:2004"
norm: EC2
section: "11"
chapter: "Beton granulats legers"
tags: [EC2, eurocode-2, beton-granulats-legers]
related: ["[[EC2_index]]", "[[EC2_10_elements-prefabriques.md]]", "[[EC2_12_beton-non-arme.md]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# 11.1.1 Domaine d'application

## (1)P - Applicabilité générale

**Toutes les règles** des sections 1 à 10 et 12 sont **généralement applicables**, à moins d'être **remplacées par des règles spéciales** de la présente Section 11.

### Adaptation des formules

En règle générale, lorsque les expressions utilisent des **valeurs de résistance** issues du Tableau 3.1, celles-ci doivent être **remplacées par les valeurs correspondantes** pour le béton léger, données dans la présente Section dans le **Tableau 11.3.1**.

## (2)P - Champ d'application spécifique

La **Section 11** s'applique à **tous les bétons** à structure fermée constitués de:
- **Granulats légers minéraux**
- **Granulats naturels ou artificiels**

À moins que l'**expérience indique de manière fiable** que des dispositions **différentes** de celles données ici peuvent être adoptées en toute sécurité.

## (3) - Exclusions

La présente Section **ne s'applique ni à**:
- **Béton cellulaire** durci en autoclave ou non
- **Béton de granulats légers** à structure ouverte

Ces produits nécessitent des régles ou des reconnaissances techniques spécifiques.

## (4)P - Définition précise

Le **béton de granulats légers** est un béton à **structure fermée** dont la **masse volumique** est:
- **Inférieure ou égale à 2200 kg/m³**

Et qui est **constitué ou qui contient** une certaine proportion de **granulats légers**:
- **Naturels ou artificiels**
- **Masse volumique < 2000 kg/m³**

# 11.1.2 Symboles spécifiques

## (1)P - Symboles pour béton léger

Les symboles ci-après sont utilisés **spécifiquement** pour le béton léger:

### Classes de résistance

**LC** = Les classes de résistance des bétons de granulats légers sont **précédées du symbole LC**

Exemple: LC 20/22, LC 30/33, etc.

### Coefficients de conversion

| Symbole | Désignation | Utilisation |
|---------|---|---|
| **η_E** | Coefficient de conversion pour le module d'élasticité | Calcul de E_lcm = E_cm × η_E |
| **η₁** | Coefficient pour la résistance en traction | f_lct = f_ct × η₁ |
| **η₂** | Coefficient pour le coefficient de fluage | Multiplication du coefficient de fluage |
| **η₃** | Coefficient pour le retrait de dessiccation | Multiplication du retrait final |

### Masse volumique

**ρ** = Masse volumique du béton de granulats légers **séché en étuve** (kg/m³)

Utilisée comme base de référence pour tous les calculs.

### Propriétés mécaniques

Pour les propriétés mécaniques des bétons légers, on ajoute l'**indice** $l$ **(léger)**.

#### Exemples

- E_lcm = module d'élasticité sécant du béton léger
- f_lck = résistance caractéristique en compression du béton léger
- f_lctm = résistance moyenne en traction du béton léger
- ε_lc2 = déformation au pic du béton léger

# 11.1 Généralités

## Portée générale

Cette section fournit les principes généraux d'application et les symboles spécifiques pour le béton de granulats légers.

### Sections connexes

- **11.1.1** : Domaine d'application
- **11.1.2** : Symboles spécifiques

# 11.2 Bases de calcul

## (1)P - Application de la Section 2

La **Section 2** (Bases de calcul) **s'applique au béton léger** **sans aucune modification**.

### Implications

Cela signifie que:

1. **Principes de calcul** : Les mêmes états-limites et combinaisons d'actions s'appliquent
2. **Coefficients partiels** : Les valeurs de γ_c, γ_s, etc. restent inchangées
3. **Combinaisons d'actions** : ELU et ELS suivent les mêmes règles
4. **Imperfections géométriques** : Mêmes prescriptions que pour béton normal

### Différences spécifiques

Les différences résident dans:
- Les **propriétés des matériaux** (Section 11.3)
- Les **formules de calcul** spécifiques au béton léger (Sections 11.6-11.9)
- L'**enrobage** (Section 11.4.2)

### Référence

Voir:
- **Section 2** : Bases de calcul des structures

# 11.3.1 Béton

## (1)P - Classification et masse volumique

Dans l'**EN 206-1**, les granulats légers sont classés en fonction de leur **masse volumique**, comme indiqué dans le **Tableau 11.1**.

Ce tableau indique également les **masses volumiques correspondantes** pour:
- **Béton non armé**
- **Béton comportant un pourcentage normal d'armatures**

Ces valeurs peuvent être utilisées pour les **calculs du poids propre** ou des **charges d'exploitation permanentes**.

### Alternative

Une autre possibilité consiste à **spécifier une masse volumique** en termes de **valeur cible**.

## (2) - Calcul alternatif de la contribution des armatures

Une autre solution consiste à **calculer la contribution des armatures** à la **masse volumique du béton**.

### Procédure

Plutôt que d'utiliser les valeurs du tableau, on peut:
1. Déterminer la masse volumique du béton seul (sans armatures)
2. Ajouter la contribution des armatures
3. Obtenir la masse volumique totale plus précise

## Tableau 11.1 - Classes de masse volumique

| Classe | 1.0 | 1.2 | 1.4 | 1.6 | 1.8 | 2.0 |
|---|---|---|---|---|---|---|
| **Masse volumique (kg/m³)** | 801-1000 | 1001-1200 | 1201-1400 | 1401-1600 | 1601-1800 | 1801-2000 |
| **Béton non armé** | 1050 | 1250 | 1450 | 1650 | 1850 | 2050 |
| **Béton armé** | 1150 | 1350 | 1550 | 1750 | 1950 | 2150 |

## (3) - Résistance en traction

La **résistance en traction** d'un béton de granulats légers peut être obtenue en **multipliant les valeurs** de $f_{ct}$ du **Tableau 3.1** par un **coefficient**:

$$\eta_1 = 0,40 + 0,60 \frac{\rho}{2200}$$

Où:
- $\rho$ = limite supérieure de la masse volumique pour la classe considérée (voir Tableau 11.1)

### Interprétation

Plus la **masse volumique est faible**, plus le coefficient **η₁ est faible**, ce qui reflète la **traction réduite** des bétons légers.

Exemples:
- ρ = 1050 kg/m³ (classe 1.0): η₁ ≈ 0,63
- ρ = 1650 kg/m³ (classe 1.6): η₁ ≈ 0,85
- ρ = 2200 kg/m³ (béton normal): η₁ = 1,00

# 11.3.2 Déformation élastique

## (1) - Module d'élasticité sécant

Une **estimation des valeurs moyennes** du **module sécant** $E_{lcm}$ des bétons de granulats légers peut être obtenue en **multipliant les valeurs** du **Tableau 3.1** (pour bétons de masse volumique normale) par le **coefficient**:

$$\eta_E = \left(\frac{\rho}{2200}\right)^2$$

Où:
- $\rho$ = masse volumique après séchage en étuve (voir EN 206-1 Section 4 et Tableau 11.1)

### Formule complète

$$E_{lcm} = E_{cm} \times \eta_E = E_{cm} \times \left(\frac{\rho}{2200}\right)^2$$

### Cas où des données précises sont requises

Lorsqu'il est **nécessaire de disposer de données précises** (notamment lorsque les flèches ont une grande importance), il convient de **réaliser des essais** afin de **déterminer les valeurs de** $E_{lcm}$ **conformément à l'ISO 6784**.

### Note

L'**Annexe Nationale** du pays concerné peut faire référence à des informations complémentaires non contradictoires.

## (2) - Coefficient de dilatation thermique

Le **coefficient de dilatation thermique** du béton de granulats légers **dépend essentiellement du type de granulats** utilisés.

### Plage de variation

Le coefficient varie **très largement** entre:
- **Minimum**: 4 × 10⁻⁶ /K
- **Maximum**: 14 × 10⁻⁶ /K

Depending on the type and porosity of lightweight aggregate.

### Valeur simplifiée pour projets courants

Pour les **projets pour lesquels la dilatation thermique a une importance mineure**, le **coefficient de dilatation thermique** peut être **pris égal à**:

$$\alpha = 8 \times 10^{-6} \text{ /K}$$

### Différence avec l'acier

Il **n'y a pas lieu**, pour le calcul, de **tenir compte des différences** entre les coefficients de dilatation thermique de l'acier et du béton de granulats légers.

En d'autres termes, pour le calcul de la dilatation du béton armé léger, on peut considérer que le coefficient moyen s'applique à l'ensemble.

# 11.3.3 Fluage et retrait

## (1) - Coefficient de fluage

Dans le cas du **béton de granulats légers**, on peut admettre que le **coefficient de fluage** $\varphi$ est égal à la **valeur pour béton de masse volumique normale**, **multipliée par un coefficient**:

$$\varphi_{léger} = \varphi_{normal} \times \left(\frac{\rho}{2200}\right)^2$$

### Amplification des déformations de fluage

Il convient de **multiplier les déformations de fluage** ainsi obtenues par le **facteur** $\eta_2$:

$$\eta_2 = \begin{cases} 
1,3 & \text{pour } f_{lck} \leq LC16/18 \\
1,0 & \text{pour } f_{lck} \geq LC20/22
\end{cases}$$

### Interpolation

Pour les classes intermédiaires (LC17, LC18, LC19), une **interpolation linéaire** peut être utilisée.

## (2) - Retrait de dessiccation

Les **valeurs finales du retrait** de dessiccation dans le cas du béton léger peuvent être obtenues en **multipliant les valeurs** pour béton de masse volumique normale du **Tableau 3.2** par un **facteur**:

$$\eta_3 = \begin{cases} 
1,5 & \text{pour } f_{lck} \leq LC16/18 \\
1,2 & \text{pour } f_{lck} \geq LC20/22
\end{cases}$$

### Signification

- Les bétons légers de faible résistance ont un **retrait amplifié** (η₃ = 1,5)
- Les bétons légers de résistance plus élevée ont un retrait moins amplifié (η₃ = 1,2)

## (3) - Retrait endogène et granulats saturés

Les **Expressions (3.11), (3.12) et (3.13)** (fournissant des informations sur le **retrait endogène**) donnent les **valeurs maximales** pour les bétons de granulats légers **lorsque les granulats ne peuvent fournir aucune eau** à la microstructure au cours de la dessiccation.

### Si granulats saturés ou partiellement saturés

Si l'on utilise des **granulats légers saturés** en eau, **voire partiellement saturés seulement**, les **valeurs des déformations** dues au retrait endogène **seront considérablement réduites**.

### Implications pratiques

- **Granulats secs** : Utiliser les formules standard avec les majoration η₃
- **Granulats saturés** : Réduction possible du retrait endogène
- **Granulats partiellement saturés** : Cas intermédiaire

# 11.3.4 Relations contrainte-déformation pour l'analyse structurale non-linéaire

## (1) - Remplacement des déformations

Dans le cas des **bétons de granulats légers**, il convient de **remplacer les valeurs** $\varepsilon_{c1}$ et $\varepsilon_{cu1}$ de la **Figure 3.2** par les valeurs:

- **$\varepsilon_{lc1}$** = déformation au pic du béton léger (au lieu de ε_c1)
- **$\varepsilon_{lcu1}$** = déformation ultime du béton léger (au lieu de ε_cu1)

Ces valeurs sont données dans le **Tableau 11.3.1**.

## (2) - Utilisation dans l'analyse

### Contexte d'application

Cette disposition s'applique à l'**analyse non-linéaire** des structures, par exemple:
- Analyse par éléments finis non-linéaire
- Analyse par méthode des bielles et tirants
- Analyse plastique de portiques

### Courbe complète

La **forme générale** de la courbe contrainte-déformation (Figure 3.2) reste la même, seules les **valeurs numériques** des déformations changent.

### Tableau 11.3.1

Le Tableau 11.3.1 fournit **les valeurs complètes** de:
- ε_lc1 (déformation au pic)
- ε_lcu1 (déformation ultime)
- Pour chaque classe de résistance LC

En fonction de la **classe de résistance** (LC12 à LC80) et de la **masse volumique** via le coefficient η₁.

## (3) - Implication pour la ductilité

Les bétons légers montrent généralement:
- **Déformations au pic réduites** (ε_lc1 < ε_c1)
- **Déformations ultimes réduites** (ε_lcu1 < ε_cu1)

Cela signifie que le béton léger a une **ductilité inférieure** à celle du béton normal, ce qui doit être pris en compte lors de la conception.

# 11.3.5 Résistance de calcul en compression – Résistance de calcul en traction

## (1)P - Résistance de calcul en compression

La **résistance de calcul en compression** est définie par:

$$f_{lcd} = \alpha_{lcc} \frac{f_{lck}}{\gamma_c}$$

Où:
- $\gamma_c$ = coefficient partiel relatif au béton (voir 2.4.1.4)
- $\alpha_{lcc}$ = coefficient défini en 3.1.6 (1)P

### Note sur α_lcc

La **valeur de** $\alpha_{lcc}$ à utiliser dans un pays donné peut être fournie par son **Annexe Nationale**.

**Valeur recommandée**: $\alpha_{lcc} = 0,85$

### Interprétation

Le coefficient 0,85 est une réduction par rapport à la résistance caractéristique, tenant compte des:
- Imprécisions géométriques
- Imprécisions matériaux
- Effets de taille et conditions de chargement

## (2)P - Résistance de calcul en traction

La **résistance de calcul en traction** est définie par:

$$f_{lctd} = \alpha_{lct} \frac{f_{lctk}}{\gamma_c}$$

Où:
- $\gamma_c$ = coefficient partiel relatif au béton (voir 2.4.1.4)
- $\alpha_{lct}$ = coefficient défini en 3.1.6 (2)P

### Note sur α_lct

La **valeur de** $\alpha_{lct}$ à utiliser dans un pays donné peut être fournie par son **Annexe Nationale**.

**Valeur recommandée**: $\alpha_{lct} = 0,85$

### Relation avec la compression

Le **même coefficient** (0,85) est recommandé pour la traction, ce qui est cohérent avec l'approche de sécurité globale.

## Tableau 11.3.1

Le Tableau 11.3.1 fournit les **résistances caractéristiques**:
- $f_{lctm}$ = résistance moyenne en traction
- $f_{lctk,0,05}$ = fractile 5% (côté inférieur)
- $f_{lctk,0,95}$ = fractile 95% (côté supérieur)

Pour **toutes les classes** de béton léger (LC12 à LC80).

# 11.3.6 Relations contrainte-déformation pour le calcul des sections

## (1) - Remplacement pour Figure 3.3

Dans le cas du **béton de granulats légers**, il convient de **remplacer les valeurs**:
- $\varepsilon_{c2}$ et $\varepsilon_{cu2}$ de la **Figure 3.3**

Par les valeurs correspondantes:
- **$\varepsilon_{lc2}$** et **$\varepsilon_{lcu2}$** du **Tableau 11.3.1**

### Contexte

La **Figure 3.3** donne la relation contrainte-déformation **pour le calcul des sections** (diagramme parabole-rectangle).

Cette figure est utilisée pour:
- Le calcul des moments résistants
- Le calcul des armatures nécessaires
- La vérification des sections

## (2) - Remplacement pour Figure 3.4

Dans le cas du **béton de granulats légers**, il convient de **remplacer les valeurs**:
- $\varepsilon_{c3}$ et $\varepsilon_{cu3}$ de la **Figure 3.4**

Par les valeurs correspondantes:
- **$\varepsilon_{lc3}$** et **$\varepsilon_{lcu3}$** du **Tableau 11.3.1**

### Contexte

La **Figure 3.4** donne la relation contrainte-déformation **parabole-rectangle** avec des valeurs différentes de la Figure 3.3.

Cette figure est utilisée pour:
- Certains types de calcul
- Les analyses spécifiques exigeant cette approximation

## Tableau 11.3.1

Le Tableau 11.3.1 fournit les **valeurs complètes** de:
- ε_lc2 et ε_lcu2 (pour Figure 3.3)
- ε_lc3 et ε_lcu3 (pour Figure 3.4)

Pour **toutes les classes** de béton léger.

# 11.3.7 Béton confiné

## (1) - Relation contrainte-déformation du béton confiné

À défaut de **données précises**, il est possible d'utiliser la **relation contrainte-déformation** de la **Figure 3.6**, avec une **résistance et des déformations caractéristiques majorées**, conformément aux expressions suivantes:

### Résistance augmentée par confinement

$$f_{lck,c} = f_{lck} \left(1,0 + k\frac{\sigma_2}{f_{lck}}\right)$$

Où:
- $\sigma_2$ = contrainte transversale de confinement
- $k$ = coefficient dépendant du type de granulats

**Note:** La **valeur de** $k$ à utiliser dans un pays donné peut être fournie par son **Annexe Nationale**.

**Valeurs recommandées:**
- $k = 1,1$ pour bétons légers comportant du sable comme granulats fins
- $k = 1,0$ pour bétons comportant **uniquement** des granulats légers

### Déformation au pic augmentée

$$\varepsilon_{lc2,c} = \varepsilon_{lc2} \left(\frac{f_{lck,c}}{f_{lck}}\right)^2$$

### Déformation ultime augmentée

$$\varepsilon_{lcu2,c} = \varepsilon_{lcu2} + 0,2\frac{\sigma_2}{f_{lck}}$$

Où $\varepsilon_{lc2}$ et $\varepsilon_{lcu2}$ sont donnés par le **Tableau 11.3.1**.

## (2) - Utilité du confinement

Le confinement du béton améliore:
- La **résistance à la compression**
- La **ductilité**
- La **capacité de déformation**

## Applications pratiques

Le confinement peut être obtenu par:
- **Armatures transversales** (cerces, spirales)
- **Béton externe** (chemisage)
- **Éléments externes** (profilés d'acier, FRP)

# 11.3 Matériaux

## Portée générale

Cette section fournit les propriétés et les relations spécifiques au béton de granulats légers pour:

- Les caractéristiques des bétons légers (masse volumique, résistance)
- Le comportement élastique (module d'élasticité, coefficient de Poisson)
- Les déformations différées (fluage, retrait)
- Les relations contrainte-déformation pour les analyses et calculs de sections

## Sections de la Section 11.3

- **11.3.1** : Béton (résistance, masse volumique, traction)
- **11.3.2** : Déformation élastique (module d'élasticité)
- **11.3.3** : Fluage et retrait
- **11.3.4** : Relations contrainte-déformation pour analyse non-linéaire
- **11.3.5** : Résistance de calcul en compression et traction
- **11.3.6** : Relations contrainte-déformation pour calcul des sections
- **11.3.7** : Béton confiné

## Principe fondamental

Toutes les propriétés sont obtenues en:
1. Prenant les **valeurs pour béton normal** (Tableau 3.1, Figures 3.2-3.6)
2. Appliquant des **coefficients correcteurs** spécifiques au béton léger
3. Utilisant la **masse volumique réelle** comme base de normalisation

Voir Tableau 11.3.1 pour synthèse des propriétés.

# 11.4.1 Conditions d'environnement

## (1) - Classes d'exposition pour béton léger

Les **classes d'exposition indicatives** du **Tableau 4.1** peuvent être utilisées pour les **bétons de granulats légers** **comme pour les bétons de masse volumique normale**.

### Implication

Cela signifie que:
- La **classification** en classes X0, XC, XD, XS, XF, etc. reste la même
- Les **critères de sélection** des classes sont identiques
- La différence réside dans les **propriétés** requises du béton léger

# 11.4.2 Enrobage et propriétés du béton

## (1)P - Augmentation de l'enrobage minimal

Dans le cas des **bétons de granulats légers**, les **valeurs de l'enrobage minimal** données dans le **Tableau 4.2** **doivent être majorées de 5 mm**.

### Justification

Cette majoration de 5 mm compense:
- La **porosité plus élevée** des bétons légers
- La **perméabilité plus importante**
- Le **risque de pénétration d'agents agressifs**

### Formule

$$c_{min,light} = c_{min,normal} + 5 \text{ mm}$$

Où:
- $c_{min,light}$ = enrobage minimal pour béton léger
- $c_{min,normal}$ = enrobage minimal du Tableau 4.2

### Impact pratique

Pour une classe d'exposition donnée:
- Béton normal XC2: c_min ≈ 30 mm
- Béton léger XC2: c_min ≈ 35 mm

## Autres propriétés du béton léger

Voir:
- **Section 11.3** : Propriétés mécaniques du béton léger
- **Tableau 11.3.1** : Caractéristiques complètes

# 11.4 Durabilité et enrobage des armatures

## Portée générale

Cette section traite des aspects de durabilité spécifiques au béton de granulats légers.

### Sections connexes

- **11.4.1** : Conditions d'environnement
- **11.4.2** : Enrobage et propriétés du béton

## Principes fondamentaux

Le béton léger ayant une **porosité naturellement plus élevée** que le béton normal, des dispositions spécifiques sont nécessaires pour assurer la durabilité.

# 11.5.1 Capacité de rotation

## Note - Ajustement de la rotation plastique

Dans le cas des **bétons légers**, il convient de **multiplier les valeurs** de $\theta_{plast}$ de la **Figure 5.6N** (capacité de rotation plastique) par un **facteur**:

$$\text{Coefficient} = \frac{\varepsilon_{lcu2}}{\varepsilon_{cu2}}$$

### Justification

Cette correction tient compte du fait que le **béton léger a une ductilité différente** du béton normal.

- Si $\varepsilon_{lcu2} < \varepsilon_{cu2}$ : le béton léger est moins ductile → la rotation admissible diminue
- Si $\varepsilon_{lcu2} > \varepsilon_{cu2}$ : le béton léger est plus ductile → la rotation admissible augmente

### Tableau 11.3.1

Les valeurs de $\varepsilon_{lcu2}$ et $\varepsilon_{cu2}$ sont données dans le Tableau 11.3.1 pour toutes les classes.

### Figure 5.6N

La Figure 5.6N (voir section 5.6.3) donne les valeurs de base de la rotation plastique admissible pour béton normal. Cette correction les ajuste pour béton léger.

# 11.5 Analyse structurale

## Portée générale

Cette section traite des aspects d'analyse structurale spécifiques au béton de granulats légers.

### Section connexe

- **11.5.1** : Capacité de rotation

# 11.6.1 Éléments pour lesquels aucune armature d'effort tranchant n'est requise

## (1) - Effort tranchant résistant

La **valeur de calcul de l'effort tranchant résistant** $V_{lRd,c}$ d'un élément en béton de granulats légers **ne comportant pas d'armatures d'effort tranchant** est donnée par:

$$V_{lRd,c} = \left[C_{lRd,c} \eta_1 k (100\rho_l f_{lck})^{1/3} + k_1 \sigma_{cp}\right] b_w d \geq (v_{l,min} + k_1 \sigma_{cp}) b_w d$$

Où:
- $\eta_1$ = coefficient défini par l'Expression (11.1): $\eta_1 = 0,40 + 0,60\frac{\rho}{2200}$
- $f_{lck}$ = résistance caractéristique du béton léger (Tableau 11.3.1)
- $\sigma_{cp}$ = contrainte de compression moyenne (efforts axiales + précontrainte)
- $b_w$ = largeur utile de l'âme
- $d$ = hauteur utile

**Note:** Les **valeurs de** $C_{lRd,c}$, $v_{l,min}$ et $k_1$ à utiliser dans un pays donné peuvent être fournies par son **Annexe Nationale**.

**Valeurs recommandées:**
- $C_{lRd,c} = 0,15/\gamma_c$
- $v_{l,min} = 0,30 k 3^{1/2} f_{lck}^{1/2}$
- $k_1 = 0,15$

## (2) - Vérification de la rupture par écrasement

Pour l'**effort tranchant**, calculé **sans le coefficient de réduction** β (voir 6.2.2(6)), il convient de **toujours satisfaire**:

$$V_{Ed} \leq 0,5 \eta_1 b_w d \nu_l f_{lcd}$$

Où:
- $\nu_l$ = coefficient de réduction (voir 11.6.2)
- $f_{lcd}$ = résistance de calcul en compression

# 11.6.2 Éléments nécessitant des armatures transversales

## (1) - Coefficient de réduction pour les bielles

Le **coefficient de réduction** pour la **résistance à l'écrasement des bielles** en béton est $\nu_l$.

**Note:** La **valeur de** $\nu_l$ à utiliser dans un pays donné peut être fournie par son **Annexe Nationale**.

**Valeur recommandée:**
$$\nu_l = 0,5 \eta_1 \left(1 - \frac{f_{lck}}{250}\right)$$

Où:
- $\eta_1 = 0,40 + 0,60\frac{\rho}{2200}$ (résistance en traction)
- $f_{lck}$ = résistance caractéristique en compression (MPa)

### Interprétation

- À **faible résistance**: $\nu_l$ est plus faible
- À **forte résistance**: $\nu_l$ est encore plus faible (sauf à très haute résistance, où le béton se raidit)
- Ce coefficient reflète la **réduction de ductilité** du béton léger sous effort tranchant

## Application

Ce coefficient est utilisé dans:
- Les formules de résistance au cisaillement
- La vérification de l'écrasement des bielles
- Le calcul de l'effort tranchant résistant

# 11.6.3.1 Méthode de calcul

## (1) - Remplacement du coefficient ν

Pour le **béton léger**, dans l'**Expression (6.30)** (formule de torsion de la section 6.3), le coefficient **ν** est **remplacé par** $\nu_l$ **défini en 11.6.2 (1)**.

### Expression modifiée

L'expression devient:

$$T_{Rd} = ... \times \nu_l \times ...$$

Au lieu de:

$$T_{Rd} = ... \times \nu \times ...$$

Où $\nu_l$ est le coefficient de réduction pour béton léger.

### Justification

La torsion, comme l'effort tranchant, dépend de la **capacité de l'âme à transmettre les contraintes de cisaillement**. Le béton léger ayant une **ductilité réduite**, le coefficient $\nu_l$ s'applique également à la torsion.

### Référence

Voir:
- **Section 6.3** : Torsion (béton normal)
- **11.6.2** : Définition et calcul de ν_l

# 11.6.3 Torsion

## Portée générale

Cette section traite du calcul de la torsion pour le béton de granulats légers.

### Section connexe

- **11.6.3.1** : Méthode de calcul

# 11.6.4.1 Résistance au poinçonnement des dalles ou des semelles de poteaux sans armatures d'effort tranchant

## (1) - Résistance au poinçonnement des dalles

La **résistance au poinçonnement** par unité de surface d'une **dalle en béton léger** est donnée par:

$$v_{lRd,c} = C_{lRd,c} k \eta_1 (100\rho_l f_{lck})^{1/3} + k_2 \sigma_{cp} \geq (\eta_1 v_{l,min} + k_2 \sigma_{cp})$$

Où:
- $\eta_1$ = coefficient de traction (Expression 11.1)
- $C_{lRd,c}$ = voir 11.6.1(1)
- $v_{l,min}$ = voir 11.6.1(1)
- $k$ = coefficient dépendant du type de granulats
- $\sigma_{cp}$ = contrainte moyenne de compression

**Note:** La **valeur de** $k_2$ à utiliser peut être fournie par son **Annexe Nationale**.

**Valeur recommandée:** $k_2 = 0,08$

## (2) - Résistance au poinçonnement des semelles de poteaux

La **résistance au poinçonnement** $V_{lRd}$ des **semelles de poteaux** en béton léger est donnée par:

$$v_{lRd} = C_{lRd,c} \eta_1 k (100\rho_l f_{lck})^{1/3} \frac{2d}{a} \geq \eta_1 v_{l,min} \frac{2d}{a}$$

Où:
- $\rho_1 \geq 0,005$ (ratio d'armature)
- $d$ = hauteur utile
- $a$ = dimension critique

Les autres paramètres sont définis comme en (1).

# 11.6.4.2 Résistance au poinçonnement des dalles ou semelles de poteaux avec armatures d'effort tranchant

## (1) - Formule générale avec armatures

Lorsque des **armatures de poinçonnement** sont nécessaires, la **résistance au poinçonnement** est donnée par:

$$v_{lRd,cs} = v_{lRd,c} + \frac{0,75 k A_{sw} f_{ywd,eff} \sin \alpha}{u_r d}$$

Où:
- $v_{lRd,c}$ = résistance sans armature (Expression 11.6.47 ou 11.6.50)
- $A_{sw}$ = aire de l'armature transversale
- $f_{ywd,eff}$ = contrainte effective dans l'armature
- $\alpha$ = angle de l'armature avec le plan
- $u_r$ = périmètre critique
- $d$ = hauteur utile

## (2) - Limitation de la résistance

Au **voisinage du poteau**, la **résistance au poinçonnement** est **limitée à**:

$$v_{lRd,max} = 0,5 \nu_l f_{lcd}$$

Où:
- $\nu_l$ = coefficient de réduction défini en 11.6.2(1)
- $f_{lcd}$ = résistance de calcul en compression du béton léger

### Condition de vérification

$$V_{Ed} \leq v_{lRd,max} \times u_d \times d$$

Où $u_d$ est le périmètre au voisinage du poteau.

# 11.6.4 Poinçonnement

## Portée générale

Cette section traite du calcul de la résistance au poinçonnement pour le béton de granulats légers.

### Sections connexes

- **11.6.4.1** : Sans armatures d'effort tranchant
- **11.6.4.2** : Avec armatures d'effort tranchant

## Contexte

Le **poinçonnement** est le **cisaillement concentré** près d'un appui ou d'une charge concentrée. Le béton léger ayant une **ductilité réduite**, des **corrections spécifiques** s'appliquent.

# 11.6.5 Pressions localisées

## (1) - Charge uniformément répartie

Dans le cas d'une **charge uniformément répartie** sur une surface $A_{c0}$, l'**effort de compression limite** peut être déterminé comme suit:

$$F_{Rdu} = A_{c0} f_{lcd} \left[\frac{\rho}{2200} + 3,0 \left(\frac{A_{c1}}{A_{c0}}\right)\right] \leq A_{c1} f_{lcd}$$

Où:
- $f_{lcd}$ = résistance de calcul en compression du béton léger
- $\rho$ = masse volumique du béton léger
- $A_{c0}$ = surface de charge
- $A_{c1}$ = surface d'influence (voir Figure 6.29)

### Simplification

La formule tient compte du fait que le **béton léger a une résistance aux pressions localisées réduite** par rapport au béton normal, compte tenu de sa porosité.

## Références

Voir:
- **Section 6.5** : Pressions localisées (béton normal)
- **Figure 6.29** : Définition des surfaces

# 11.6.6 Fatigue

## (1) - Prise en compte particulière requise

Pour la **vérification de la fatigue** des **éléments en béton de granulats légers**, une **prise en compte particulière est nécessaire**.

Il convient de **se référer à un Agrément Technique Européen**.

### Justification

Le **comportement en fatigue** du béton léger peut **différer sensiblement** du béton normal, notamment du fait de:
- La **structure interne** du béton léger
- La **porosité** et **l'absorption d'eau**
- Les **propriétés d'adhérence** des granulats

### Ressources

Les Agréments Techniques Européens (ETA) spécifiques aux bétons légers fournissent:
- Des **courbes S-N** adaptées
- Des **coefficients de sécurité** spécifiques
- Des **limites de contrainte** pour la fatigue

Consulter le fabricant et les dispositions constructives spécifiques pour ce type de béton.

# 11.6 États-limites ultimes (ELU)

## Portée générale

Cette section traite de la vérification des états-limites ultimes pour le béton de granulats légers.

### Domaines couverts

- **11.6.1** : Effort tranchant (sans armatures)
- **11.6.2** : Effort tranchant (avec armatures)
- **11.6.3** : Torsion
- **11.6.4** : Poinçonnement
- **11.6.5** : Pressions localisées
- **11.6.6** : Fatigue

## Principes fondamentaux

Pour le béton léger:
1. Les formules de base restent similaires à celles du béton normal
2. Des **coefficients correcteurs** sont introduits (notamment η₁)
3. Des **coefficients de réduction** spécifiques s'appliquent (notamment ν_l)

# 11.7 États-limites de service (ELS)

## (1)P - Réduction du rapport portée/hauteur

Dans le cas des **bétons de granulats légers**, il convient de **réduire les valeurs de base** du **rapport portée/hauteur utile** données en **7.4.2** pour les **éléments de béton armé** (en l'absence d'effort normal de compression), en **appliquant un coefficient**:

$$\text{Coefficient} = \eta_E^{0,15}$$

Où:
- $\eta_E = \left(\frac{\rho}{2200}\right)^2$ (coefficient du module d'élasticité)

### Justification

Le béton léger ayant un **module d'élasticité réduit**, les **flèches sont plus importantes** pour un même rapport portée/hauteur. Cette réduction compense cela.

### Calcul pratique

Pour une classe donnée:
- Béton léger LC20/22: $\eta_E \approx 0,35$ → coefficient ≈ 0,75
- Béton léger LC35/38: $\eta_E \approx 0,53$ → coefficient ≈ 0,83
- Béton léger LC55/60: $\eta_E \approx 0,84$ → coefficient ≈ 0,95

### Implications

La **portée admissible** pour une flèche donnée est **réduite** pour le béton léger, ce qui signifie que les **flèches doivent être vérifiées plus attentivement**.

## Référence

Voir **Section 7.4** : Limitation des flèches (béton normal)

# 11.8.1 Diamètres admissibles des mandrins de cintrage

## (1) - Majoration pour béton léger

Dans le cas des **bétons de granulats légers**, il convient de **majorer de 50%** les **valeurs des diamètres de mandrin** données en **8.4.4** (pour bétons de masse volumique normale).

### Objectif

Cela permet d'**éviter l'éclatement du béton** à l'arrière des:
- **Coudes**
- **Crochets**
- **Boucles**

### Justification

Le **béton léger** ayant une **ductilité réduite** et une **résistance en traction inférieure**, il est plus susceptible de s'**éclater sous les contraintes** induites par le cintrage.

### Formule

$$\phi_{mandrin, léger} = 1,5 \times \phi_{mandrin, normal}$$

Où:
- $\phi_{mandrin, normal}$ = diamètre du mandrin pour béton normal (section 8.4.4)
- $\phi_{mandrin, léger}$ = diamètre du mandrin majore pour béton léger

### Exemples

- Béton normal, acier HA 500: φ_mandrin ≈ 20 × φ_barre
- Béton léger, acier HA 500: φ_mandrin ≈ 30 × φ_barre

## Référence

Voir **Section 8.4.4** : Diamètres de mandrin (béton normal)

# 11.8.2 Contrainte ultime d'adhérence

## (1) - Calcul pour béton léger

La **valeur de calcul de la contrainte ultime d'adhérence** peut être obtenue, dans le cas de **barres dans un béton léger**, à l'aide de l'**Expression (8.2)** (section 8) dans laquelle on **remplace** $f_{ctd}$ **par** $f_{lctd}$.

### Formule

$$f_{lctd} = \frac{f_{lctk,0,05}}{\gamma_c}$$

Où:
- $f_{lctk,0,05}$ = résistance en traction fractile 5% du béton léger
- $\gamma_c$ = coefficient partiel pour le béton

### Valeurs

Les **valeurs de** $f_{lctk,0,05}$ **sont données dans le Tableau 11.3.1** pour toutes les classes de béton léger.

### Expression (8.2)

La **formule générale** (Expression 8.2) de l'adhérence reste inchangée:

$$f_{bd} = 2,25 \eta_1 \eta_2 f_{ctd}$$

où:
- $\eta_1$ = facteur tenant compte de la qualité d'adhérence
- $\eta_2$ = facteur tenant compte du diamètre de la barre
- $f_{ctd}$ = remplacé par $f_{lctd}$ pour béton léger

## Implication pratique

L'adhérence est **généralement réduite** pour le béton léger, ce qui peut **augmenter les longueurs d'ancrage** requises.

## Référence

Voir **Section 8** : Dispositions constructives (ancrage, recouvrement, etc.)

# 11.8 Disposition des armatures - Généralités

## Portée générale

Cette section traite des dispositions constructives spécifiques au béton de granulats légers.

### Sections connexes

- **11.8.1** : Diamètres admissibles des mandrins de cintrage
- **11.8.2** : Contrainte ultime d'adhérence

# 11.9 Dispositions constructives et règles particulières

## (1) - Diamètre maximal des barres

Il convient **normalement de limiter** à **32 mm** le **diamètre des barres** noyées dans les **bétons de granulats légers**.

### Justification

Le béton léger ayant une **adhérence réduite** et une **ductilité inférieure**, les barres de diamètre important peuvent poser des problèmes de:
- **Ancrage insuffisant**
- **Fissuration excessive**
- **Risque d'éclatement** local

## (2) - Paquets de barres

### Limitations

Il convient:
- **Ne pas utiliser de paquets constitués de plus de deux barres**
- **Limiter le diamètre équivalent à 45 mm**

### Diamètre équivalent

Le **diamètre équivalent** d'un paquet est défini comme le diamètre d'une barre unique ayant la même section qu'le paquet.

### Justification

Plus de deux barres ou des paquets trop volumineux entraînent des risques de:
- **Ségregation** du béton lors de la mise en place
- **Vides** autour des barres
- **Ancrage insuffisant** des barres internes

## Références

Voir:
- **Section 8** : Dispositions constructives (béton normal)
- **11.8** : Disposition des armatures spécifique au béton léger

# 11.10 Règles additionnelles pour les éléments et les structures préfabriqués en béton

## (1) - Applicabilité de la Section 10

La **Section 10** (Règles additionnelles pour éléments et structures préfabriqués) **peut s'appliquer aux bétons de granulats légers** **sans aucune modification**.

### Implication

Cela signifie que:
- Les **règles de transport** et de manutention restent applicables
- Les **règles de stockage** peuvent être suivies
- Les **liaisons** entre éléments sont dimensionnées suivant la Section 10
- Le seul changement est l'**utilisation des propriétés du béton léger** au lieu du béton normal

## Références

Voir **Section 10** : Règles additionnelles pour les éléments et les structures préfabriqués en béton

# 11.12 Structures en béton non armé ou faiblement armé

## (1) - Applicabilité de la Section 12

La **Section 12** (Structures en béton non armé ou faiblement armé) **peut s'appliquer aux bétons de granulats légers** **sans aucune modification**.

### Implication

Cela signifie que:
- Les **principes** de vérification du béton non armé restent applicables
- Les **vérifications** à l'ELU et ELS suivent les mêmes approches
- Le seul changement est l'**utilisation des propriétés du béton léger**

### Note importante

Bien que la Section 12 s'applique sans modification, il faut noter que:
- Le **béton léger non armé** a une **ductilité inférieure**
- Les **flèches** peuvent être plus importantes
- La **résistance en traction** est réduite

## Références

Voir **Section 12** : Structures en béton non armé ou faiblement armé

# 11 Structures en béton de granulats légers

## Portée générale

Cette Section fournit des **exigences supplémentaires** pour les bétons de granulats légers.

### Principes d'application

1. **Règles générales** : Toutes les sections 1-10 et 12 s'appliquent
2. **Exigences spéciales** : Remplacées ou complétées par les règles de la présente Section 11
3. **Remplacement des propriétés** : Les valeurs du Tableau 3.1 sont remplacées par celles du Tableau 11.3.1

### Note sur la numérotation

Les titres sont numérotés **11** suivi du numéro de la section principale correspondante. Les numéros d'origine sont conservés, précédés de 11 également.

## Sections de la Section 11

- **11.1** : Généralités (domaine d'application, symboles)
- **11.2** : Bases de calcul
- **11.3** : Matériaux (béton, déformation, fluage, retrait)
- **11.4** : Durabilité et enrobage
- **11.5** : Analyse structurale
- **11.6** : États-limites ultimes
- **11.7** : États-limites de service
- **11.8** : Disposition des armatures
- **11.9** : Dispositions constructives
- **11.10** : Règles additionnelles pour éléments préfabriqués
- **11.12** : Structures en béton non armé ou faiblement armé

## Définition du béton léger

Béton à structure **fermée** dont:
- **Masse volumique** ≤ 2200 kg/m³
- **Composé de** granulats légers minéraux naturels ou artificiels
- **Masse volumique des granulats** < 2000 kg/m³

## Exclusions

Cette Section **ne s'applique pas** à:
- Béton cellulaire (durci en autoclave ou non)
- Béton de granulats légers à structure ouverte

---

Liens : [[EC2_index]] · [[EC2_10_elements-prefabriques.md]] · [[EC2_12_beton-non-arme.md]] · [[_Knowledge — Index]] · [[CLAUDE]]
