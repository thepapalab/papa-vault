---
title: "NBN EN 1991-2 S6 — Actions du trafic ferroviaire"
type: norm-extract
source: "NBN EN 1991-2:2004 (+ ANB 2011 + AC:2010)"
norm: EC1-2
section: "6"
chapter: "6"
tags: [EC1-2, NBN, trafic-ferroviaire, LM71, SW0, SW2, HSLM, coefficient-dynamique, centrifuge, lacet, freinage, interaction-voie-ouvrage, aerodynamique, deraillement, fatigue-ferroviaire]
related: ["[[NBN EN 1991-2 — Index]]", "[[PTR CE01 — Ch03 — Actions]]", "[[NBN EN 1991-2 — Ann-A-D — Vehicules-Speciaux-Fatigue]]", "[[NBN EN 1991-2 — Ann-E-H — Dynamique-Avancee]]"]
language: fr
jupyter_ref: "EC1-2/6"
created: 2026-06-05
---

# Section 6 — Actions du trafic ferroviaire et autres actions spécifiques sur les ponts ferroviaires

## 6.1 Domaine d'application

- Grandes lignes du réseau européen, **voie standard** (1 435 mm) ou **grande** (> 1 435 mm).
- **Exclu** : voie étroite, tramways, crémaillère, funiculaires — charges à spécifier séparément.
- La section ne s'applique pas directement aux tabliers auxiliaires (exigences spécifiques dans l'ANB ou le projet).
- Limites de déformation : voir **EN 1990, Annexe A2**.

## 6.2 Modèles de charge disponibles

| Type | Modèle | Référence |
|------|--------|-----------|
| Charge verticale | LM71, SW/0, SW/2, train à vide, HSLM | 6.3, 6.4.6 |
| Charge embankment | LM71 (diffusion) | 6.3.6.4 |
| Effets dynamiques | Coefficient Φ, analyse dynamique | 6.4 |
| Forces centrifuges | Qtk, qtk | 6.5.1 |
| Effort de lacet | Qsk | 6.5.2 |
| Freinage/accélération | Qlbk, Qlak | 6.5.3 |
| Interaction voie-ouvrage | FTk, FQk | 6.5.4 |
| Aérodynamique | — | 6.6 |
| Déraillement (accidentel) | QA1d, qA1d | 6.7 |
| Fatigue | Trains-types D1–D12 | 6.9 + Annexe D |

## 6.3 Charges verticales — Valeurs caractéristiques

### 6.3.2 Modèle de charge 71 (LM71)

Trafic ferroviaire standard sur grandes lignes.

$$\text{Disposition : 4 forces ponctuelles de 250 kN + UDL de 80 kN/m (illimitée de part et d'autre)}$$

$$\text{Charges classifiées} = \alpha \times \text{LM71}$$

**Valeurs de α :**

$$\alpha \in \{0{,}75 ;\ 0{,}83 ;\ 0{,}91 ;\ \mathbf{1{,}00} ;\ 1{,}10 ;\ 1{,}21 ;\ 1{,}33 ;\ 1{,}46\}$$

> [!important] ANB Belgique
> Pour les lignes internationales : **α ≥ 1,00** recommandé.  
> PTR CE01 §3.1.6.3 impose **α = 1,20** pour LM71 et SW/0 (ULS, calcul élastique, flèches).

Le coefficient α s'applique également à : forces centrifuges, lacet (si α ≥ 1), freinage/accélération, interaction voie-ouvrage, déraillement, SW/0.

### 6.3.3 Modèles de charge SW/0 et SW/2

**Tableau 6.1 — Valeurs caractéristiques SW/0 et SW/2**

| Modèle | q_vk [kN/m] | a [m] | c [m] |
|--------|------------|-------|-------|
| **SW/0** | **133** | **15,0** | **5,3** |
| **SW/2** | **150** | **25,0** | **7,0** |

- a = longueur de la zone uniformément chargée
- c = intervalle entre les deux zones chargées
- SW/0 : ponts continus uniquement (combiné avec LM71)
- SW/2 : trafic lourd — lignes à spécifier dans l'ANB/projet individuel

$$\text{SW/0 multiplié par α (comme LM71)}$$

### 6.3.4 Modèle de charge "train à vide"

$$q_{vide} = 10{,}0 \text{ kN/m (uniforme)}$$

Usage : vérification de la **stabilité latérale** des ponts à voie unique.

### 6.3.5 Excentricité des charges verticales

Rapport des charges de roues d'un même essieu ≤ **1,25 : 1,00** sur n'importe quelle voie.

Négligeable pour la **fatigue**.

### 6.3.6 Diffusion des charges par rails, traverses et ballast

**(a) Diffusion longitudinale par le rail** (Fig. 6.4) : charge d'essieu répartie sur 3 traverses.

**(b) Diffusion par traverse et ballast** (Fig. 6.5) :
- Longitudinal : B = a + 2h_b (h_b = hauteur de ballast sous traverse)
- Transversal : voir table 6.x

**(c) Diffusion sur remblai** (§6.3.6.4) : charges équivalentes pour calcul des pressions au sol et poussées.

## 6.4 Effets dynamiques (incluant la résonance)

### 6.4.4 Nécessité d'une analyse statique ou dynamique

Pour V ≤ 200 km/h et dans les limites de fréquence de la Figure 6.10 : **analyse statique avec Φ**.

Pour V > 200 km/h ou hors limites : **analyse dynamique requise**.

> [!note] Limites de fréquence (Fig. 6.10)
> Pour une portée L :
> - Fréquence propre verticale f_v doit se situer dans la bande définie par deux courbes (fonctions de L).
> - Si f_v hors bande → analyse dynamique nécessaire.

### 6.4.5 Coefficient dynamique Φ (Φ₂, Φ₃)

Le coefficient dynamique tient compte de l'amplification des contraintes et vibrations, **pas** des effets de résonance.

**(a) Voie soigneusement entretenue :**

$$\Phi_2 = \frac{1{,}44}{\sqrt{L_\Phi} - 0{,}2} + 0{,}82 \qquad \text{avec : } 1{,}00 \leq \Phi_2 \leq 1{,}67 \tag{6.4}$$

**(b) Voie normalement entretenue :**

$$\Phi_3 = \frac{2{,}16}{\sqrt{L_\Phi} - 0{,}2} + 0{,}73 \qquad \text{avec : } 1{,}00 \leq \Phi_3 \leq 2{,}00 \tag{6.5}$$

où $L_\Phi$ = longueur déterminante [m] (Tableau 6.2).

> [!important] ANB Belgique — PTR CE01
> **Par défaut : Φ₃** (voie normalement entretenue) — sauf si spécification contraire dans l'ANB ou le projet.  
> PTR CE01 retient la formule Φ₂ (voie soigneusement entretenue) pour les ponts de l'Infrabel.

**Valeurs indicatives Φ₂ en fonction de L_Φ :**

| L_Φ [m] | Φ₂ | Φ₃ |
|---------|-----|-----|
| 2 | 1,67 | 2,00 |
| 4 | 1,58 | 1,91 |
| 6 | 1,46 | 1,73 |
| 8 | 1,38 | 1,61 |
| 10 | 1,32 | 1,51 |
| 15 | 1,22 | 1,36 |
| 20 | 1,17 | 1,26 |
| 30 | 1,12 | 1,16 |
| 50 | 1,08 | 1,10 |
| 100 | 1,04 | 1,05 |

**Réduction pour ponts voûtés et béton avec couverture h > 1,00 m :**

$$\Phi_{2,3\,\text{red}} = \Phi_{2,3} - \frac{h - 1{,}00}{10} \geq 1{,}0 \tag{6.8}$$

où h = épaisseur couverture (ballast inclus) du niveau supérieur tablier au niveau supérieur traverse [m].

> [!important] PTR CE01 §3.1.6.4
> Formule identique utilisée par Infrabel : $\Phi_{2,\text{red}} = \Phi_2 - (h - 1{,}00)/10 \geq 1{,}0$

**Φ NE s'applique PAS à :** trains réels, trains-types fatigue (Annexe D), HSLM, train à vide.

**Φ ne se réduit PAS** pour les ouvrages à plusieurs voies.

### 6.4.5.3 Longueur déterminante L_Φ (Tableau 6.2, extraits)

| Cas | Élément structural | L_Φ |
|-----|--------------------|-----|
| 1.1 | Poutre principale sur appuis simples | Portée L |
| 1.2 | Poutre principale continue n travées | k × L_m (k selon n ; k=1,2 pour n=2 …) |
| 2 | Dalles de tablier (portée transversale) | 3 fois la portée transversale (≤ L portée principale) |
| 3 | Entretoises | 3 fois l'espacement des entretoises |
| 5 | Voûtes, arcs | demi-portée |
| 6 | Appuis, appareils | Longueur déterminante de l'élément supporté |

Pour poutre continue à n travées : $L_\Phi = k \times L_m$ avec $L_m = (L_1 + L_2 + \ldots + L_n)/n$

| n | 2 | 3 | 4 | ≥5 |
|---|---|---|---|----|
| k | 1,2 | 1,3 | 1,4 | 1,5 |

### 6.4.5.4 Effets dynamiques réduits

Pour poteaux d'élancement < 30, culées, fondations, murs de soutènement : **effets dynamiques négligeables**.

### 6.4.6 Analyse dynamique — Modèle HSLM

Nécessaire pour V > 200 km/h ou si critères d'analyse statique non satisfaits.

**Tableau 6.3 — HSLM-A**

| Train | N voitures | D [m] | d [m] | P [kN] |
|-------|-----------|-------|-------|-------|
| A1 | 18 | 18 | 2,0 | 170 |
| A2 | 17 | 19 | 3,5 | 200 |
| A3 | 16 | 20 | 2,0 | 180 |
| A4 | 15 | 21 | 3,0 | 190 |
| A5 | 14 | 22 | 2,0 | 170 |
| A6 | 13 | 23 | 2,0 | 180 |
| A7 | 13 | 24 | 2,0 | 190 |
| A8 | 12 | 25 | 2,5 | 190 |
| A9 | 11 | 26 | 2,0 | 210 |
| A10 | 11 | 27 | 2,0 | 210 |

**HSLM-B** : N forces ponctuelles de 170 kN à espacement d [m], définis par graphique (fonctions de L).

**Tableau 6.4 — Choix HSLM-A ou HSLM-B**

| Configuration | L < 7 m | L ≥ 7 m |
|--------------|---------|---------|
| Travée simple | HSLM-B | HSLM-A (train critique de A1-A10) |
| Ouvrage continu | HSLM-A (A1-A10) | HSLM-A (A1-A10) |
| Ouvrage complexe | HSLM-A + HSLM-B | HSLM-A + HSLM-B |

**Vérification finale (6.4.6.5) :** retenir la valeur la plus défavorable parmi :

$$\left(1 + \varphi'_{dyn} + \frac{\varphi''}{2}\right) \times \begin{cases} \text{HSLM} \\ \text{RT (trains réels)} \end{cases} \quad \text{ou} \quad \Phi \times (\text{LM71 "+"SW/0}) \tag{6.15, 6.16}$$

## 6.5 Forces horizontales — Valeurs caractéristiques

### 6.5.1 Forces centrifuges

$$Q_{tk} = \frac{v^2}{g \cdot r}\,(f \cdot Q_{vk}) = \frac{V^2}{127\,r}\,(f \cdot Q_{vk}) \tag{6.17}$$

$$q_{tk} = \frac{v^2}{g \cdot r}\,(f \cdot q_{vk}) = \frac{V^2}{127\,r}\,(f \cdot q_{vk}) \tag{6.18}$$

où :
- V = vitesse maximale de ligne [km/h]
- r = rayon de courbure [m]
- f = coefficient de réduction (voir 6.5.1(4))
- Q_vk, q_vk = charges verticales LM71/SW/0/SW/2 (sans Φ)

> [!note]
> - Appliquée **horizontalement** vers l'extérieur, à **h_t = 1,80 m** au-dessus du plan de roulement.
> - **Non multipliée** par Φ ni par f (centrifuge).
> - Toujours combinée avec la charge verticale.

**Coefficient de réduction f :** varie selon V et r (voir graphique §6.5.1(4)).

### 6.5.2 Effort de lacet

$$Q_{sk} = 100 \text{ kN} \quad \text{(force horizontale unique, dans le sens latéral, au niveau des rails)}$$

- Applicable à LM71, SW/0, SW/2 uniquement.
- **Non multipliée** par Φ.
- À combiner avec les charges verticales.

> [!note] ANB Belgique
> Valeur caractéristique de l'effort de lacet : **Q_sk = 100 kN** (valeur recommandée EN = conforme PTR CE01 §3.1.7).

### 6.5.3 Forces de freinage et d'accélération

**Freinage (Q_lbk)** et **accélération (Q_lak)** caractéristiques pour LM71 (± SW/0) :

$$Q_{lbk} = 20\,\alpha \cdot L_{adj} \leq 6\,000\,\alpha \text{ kN} \quad \text{(freinage)}$$

$$Q_{lak} = 33\,\alpha \cdot L_{adj} \leq 1\,000\,\alpha \text{ kN} \quad \text{(accélération)}$$

où L_adj = longueur d'influence [m].

> [!note]
> Pour SW/2 : Q_lbk = 35 × longueur chargée ≤ 3 500 kN.  
> Ces forces s'appliquent à la surface de contact rail/traverse.

### 6.5.4 Réponse combinée du système voie–ouvrage

Pour les ponts avec **rail soudé continu (CWR)** s'étendant au-delà du pont :

**Déformations du tablier → forces dans les rails**

Critères de dimensionnement (6.5.4.5) :

| Critère | Valeur limite |
|---------|--------------|
| Contrainte additionnelle max. dans le rail — traction | **72 MPa** |
| Contrainte additionnelle max. dans le rail — compression | **92 MPa** |
| Déplacement relatif rail/tablier (à l'extrémité) | ≤ **5 mm** (trafic, non chargé) |

Méthodes de calcul simplifiées (6.5.4.6) :

- Méthode simplifiée (1 tablier, portée unique) : force F_Tk due à température selon formule avec K = raideur voie (K₂, K₅ ou K₂₀ selon conditions).
- Méthode générale : voir **Annexe G**.
- Référence complémentaire : **UIC 774-3**.

### Raideurs longitudinales de la voie

| Condition | K [kN/m de voie par m] |
|-----------|------------------------|
| K₂ | 2 × 10³ (non chargé) |
| K₅ | 5 × 10³ (non chargé, voie rigide) |
| K₂₀ | 20 × 10³ (chargé) |

## 6.6 Actions aérodynamiques dues au passage des trains

### 6.6.1 Généralités

Les trains en mouvement génèrent des pressions de surface (charges d'impulsion) sur les structures adjacentes.

### 6.6.2 Surfaces verticales simples parallèles à la voie (ex. écrans anti-bruit)

Charge de surface max. (positive puis négative) :

$$q_{pmax} = \frac{0{,}4 \cdot c_{pmax}}{k} \cdot \left(\frac{v_{tr}}{c_0}\right)^2 \quad \text{[kN/m}^2\text{]}$$

### 6.6.3–6.6.6 Autres configurations

- **Surfaces horizontales** au-dessus des voies (auvent caténaire) : pressions vers le bas puis vers le haut.
- **Structures mixtes** verticales + horizontales (abris quai) : combinaison des effets.
- **Structures enveloppant la voie sur ≤ 20 m** (échafaudage, construction provisoire) : majoration.

> [!note]
> Les formules détaillées dépendent de la distance à l'axe de la voie, de la hauteur de la structure et de la vitesse des trains. Voir tableaux §6.6.2 à 6.6.6.

## 6.7 Déraillement et autres actions sur les ponts ferroviaires

### 6.7.1 Déraillement sur un pont ferroviaire — Class B

Charges équivalentes pour le déraillement (situations accidentelles) :

**Cas I — Déraillement sur le tablier :**

$$Q_{A1d} = \alpha \times 250 \text{ kN (charge concentrée)} ; \quad q_{A1d} = \alpha \times 80 \text{ kN/m}$$

Disposition : charges parallèles à la voie, dans une bande de largeur 1,5 × voie, sur un côté.  
Pour tabliers ballastés : répartition sur 0,45 × 0,45 m sur le tablier.  
Vérification : **stabilité globale uniquement** (pas consoles ni trottoirs indépendants).

**Cas II — Déraillement hors voie :** charges réduites, selon l'AN/projet individuel.

> [!important] ANB Belgique — PTR CE01 §3.1.11
> Classe B structures : ponts rail, ponts route/piétons, PX, bâtiments non habités.  
> Forces peuvent être réduites de 50% si vitesse max ≤ 50 km/h.  
> Hauteur d'application de la force : **1,8 m** au-dessus du niveau de la voie.

### 6.7.2 Déraillement sous ou à proximité de l'ouvrage

Zone d < 3 m de l'axe de voie (Zone 1) : éviter les éléments structuraux ; si inévitable → charge exceptionnelle UIC 777-2 Annexe D.

### 6.7.3 Autres actions

- **Rupture de caténaire** : voir PTR CE01.
- **Effets thermiques différentiels** : EN 1991-1-5.
- **Poids des équipements** : caténaire, signalisation, câbles (poids propre, hors tension de câble).

## 6.8 Application des charges de trafic sur les ponts ferroviaires

### 6.8.1 Généralités

- Appliquer les modèles de charge sur chaque voie **séparément** ou de manière la plus défavorable.
- **Excentricité** : voir 6.3.5.
- **Position de la voie** : tenir compte de la tolérance de positionnement (±50 mm pour voies à voie large).

### 6.8.2 Groupes de charges — Valeurs caractéristiques (Tableau 6.10)

| Groupe | LM71/SW | Centrifuge | Lacet | Freinage | Train à vide |
|--------|---------|------------|-------|----------|-------------|
| **gr11** | Dominant | Caract. | Caract. | Caract. | — |
| **gr12** | — | Caract. | Dominant | — | — |
| **gr13** | Caract. | — | — | Dominant | — |
| **gr14** | — | — | — | — | Dominant |
| **gr15** | Caract. | Dominant | — | — | — |
| **gr16** | Caract. | Caract. | Caract. | Dominant (SW/2) | — |
| **gr17** | Dominant (SW/2) | — | — | — | — |

### 6.8.3 Autres valeurs représentatives

- Valeurs fréquentes : LM71 seul (ou SW/0) avec ψ₁ selon EN 1990 A2.
- Valeurs quasi-permanentes : généralement = 0 pour trafic ferroviaire.

## 6.9 Charges de trafic pour la fatigue

- Trains-types définis à l'**Annexe D** (D.3) : 12 trains-types (de D1 à D12 selon 3 trafics : dense, mixte, léger).
- Application : Φ **non** applicable aux trains-types ; utiliser les charges nominales.
- Voir [[NBN EN 1991-2 — Ann-A-D — Vehicules-Speciaux-Fatigue]] pour les détails.

---

Links: [[NBN EN 1991-2 — Index]] · [[PTR CE01 — Ch03 — Actions]] · [[NBN EN 1991-2 — Ann-A-D — Vehicules-Speciaux-Fatigue]] · [[NBN EN 1991-2 — Ann-E-H — Dynamique-Avancee]]
