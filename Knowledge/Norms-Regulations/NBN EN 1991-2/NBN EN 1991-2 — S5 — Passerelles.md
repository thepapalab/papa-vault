---
title: "NBN EN 1991-2 S5 — Actions sur les passerelles"
type: norm-extract
source: "NBN EN 1991-2:2004 (+ ANB 2011 + AC:2010)"
norm: EC1-2
section: "5"
chapter: "5"
tags: [EC1-2, NBN, passerelles, trottoirs, piétons, charges-piétons, dynamique-piétons, vehicule-service, accidentel]
related: ["[[NBN EN 1991-2 — Index]]", "[[NBN EN 1991-2 — S4 — Trafic-Routier]]", "[[NBN EN 1991-2 — S6 — Trafic-Ferroviaire]]"]
language: fr
jupyter_ref: "EC1-2/5"
created: 2026-06-05
---

# Section 5 — Actions sur les trottoirs, pistes cyclables et passerelles

## 5.1 Domaine d'application

- **q_fk** et **Q_fwk** (charge concentrée) s'appliquent aux trottoirs des ponts routiers **et** aux passerelles.
- Toutes les autres actions (véhicule de service, charges dynamiques, accidentel) : **passerelles uniquement**.
- Pas de modèles de fatigue dans cette section (fatigue negligeable pour piétons).
- Pour passerelles de largeur > 6 m : modèles complémentaires peuvent être nécessaires (comportement spécifique).

## 5.2 Représentation des actions

Les charges de la section 5 incluent la **majoration dynamique** — elles sont traitées comme des charges statiques, **sauf** pour l'analyse dynamique des passerelles (§ 5.7).

**Passages de service** (intérieur des ponts ferroviaires / quais) : modèles séparés, recommandés : 2 kN/m² + 3 kN sur 0,2 m × 0,2 m.

## 5.3 Charges verticales — Valeurs caractéristiques

### 5.3.2.1 Charge uniformément répartie q_fk

**(a) Trottoirs et pistes cyclables sur ponts routiers :**

> [!important] ANB Belgique
> $$q_{fk} = 5{,}0 \text{ kN/m}^2$$

**(b) Passerelles :**

Si LM4 (foule) n'est pas requis, valeur recommandée :

$$q_{fk} = 2{,}0 + \frac{120}{L + 30} \quad \text{[kN/m²]} \qquad (5.1)$$

avec :
$$2{,}5 \text{ kN/m}^2 \leq q_{fk} \leq 5{,}0 \text{ kN/m}^2$$

où L = longueur chargée en [m].

| L [m] | q_fk [kN/m²] |
|-------|--------------|
| 0 | 6,0 → capped → **5,0** |
| 10 | 4,75 |
| 30 | 3,5 |
| 60 | 3,0 |
| 120 | 2,67 |
| 270 | 2,4 → capped → **2,5** |

> [!note]
> Si risque de foule dense : utiliser LM4 = 5 kN/m² (§ 4.3.5).

### 5.3.2.2 Charge concentrée Q_fwk

$$Q_{fwk} = 10 \text{ kN}$$

sur une surface carrée de **0,10 m × 0,10 m**.

- Pour les **effets locaux uniquement** (si effets généraux et locaux distingués).
- **Non pris en compte** si un véhicule de service est spécifié (§ 5.3.2.3).

### 5.3.2.3 Véhicule de service Q_serv

À prendre en compte lorsque des véhicules d'entretien/urgence doivent circuler sur la passerelle.

Valeur par défaut (en l'absence d'obstacle permanent et sauf si ANB précise) :
- Essieu avant : **10 kN** (charge totale) ou conforme aux exigences du projet

> [!note] ANB Belgique
> Le véhicule de service est à définir dans le projet individuel ; en l'absence de précision : charge d'essieu 80 kN / essieu arrière, 40 kN / essieu avant (véhicule type pompiers), ou 3 kN/m² + 3 kN ponctuel pour passerelles d'inspection.

## 5.4 Forces horizontales — Valeurs caractéristiques

Force horizontale caractéristique sur passerelle :

$$Q_{flk} = 10\% \times q_{fk} \text{ (par m de longueur)} \quad \geq 10 \text{ kN}$$

appliquée à 1,0 m au-dessus du tablier, dans la direction la plus défavorable.

> [!note] ANB Belgique
> Valeur caractéristique de la force horizontale : **10% de la charge verticale totale**, minimum 10 kN sur toute la largeur.

## 5.5 Groupes de charges de trafic sur les passerelles

Voir Tableau 4.4a (§ 4.5.1) — lignes gr3 et gr4 s'appliquent aux passerelles.

## 5.6 Actions accidentelles sur les passerelles

### 5.6.2 Forces d'impact des véhicules routiers sous l'ouvrage

**(a) Impact sur piles** : idem ponts routiers §4.7.2 (F_dx, F_dy selon ANB / EN 1991-1-7).

**(b) Impact sur tabliers** (hauteur libre ≤ 5 m) : idem §4.7.2.2.

### 5.6.3 Présence accidentelle de véhicule sur la passerelle

À prendre en compte si aucun obstacle permanent n'empêche l'accès des véhicules.

Valeur recommandée (si ANB ne précise pas) :
- Charge verticale = essieu de **80 kN** (charge totale du véhicule 160 kN / 2 essieux).
- Majoration dynamique : φ_dyn incluse.
- Surface de contact : 0,20 m × 0,20 m par roue.

## 5.7 Modèles dynamiques de charges dues aux piétons

L'analyse dynamique est nécessaire pour les passerelles **souples** (f_v < 5 Hz ou f_h < 2,5 Hz typiquement).

### Modèles de chargement dynamique

**(1) Piéton unique :** force verticale harmonique équivalente (test de marche) :
$$F_v = 0{,}4 \text{ kN} \quad \text{(valeur recommandée pour 1 piéton)}$$

**(2) Foule de piétons :** force équivalente sur toute la surface :
$$q_{dyn} = 0{,}07 \times \sqrt{n} \times F_v \quad \text{ou charge harmonique selon fréquence de marche}$$

> [!note] ANB Belgique
> Les exigences dynamiques pour les passerelles (fréquences propres à éviter, critères d'accélération admissible) sont définies dans le projet individuel et peuvent référencer les recommandations SETRA/AFGC ou CEN/TS.

### Critères de confort

| Type de perception | Accélération verticale a_lim |
|-------------------|------------------------------|
| Maximale (peu de gêne) | 0,50 m/s² |
| Normale | 1,00 m/s² |
| Minimale (gêne acceptée) | 2,50 m/s² |

## 5.8 Actions sur les garde-corps

Identique à §4.8 — voir [[NBN EN 1991-2 — S4 — Trafic-Routier]].

## 5.9 Modèle de charge pour culées et murs adjacents

Identique à §4.9 — charge uniformément répartie q_eq sur remblais.

---

Links: [[NBN EN 1991-2 — Index]] · [[NBN EN 1991-2 — S4 — Trafic-Routier]] · [[NBN EN 1991-2 — S6 — Trafic-Ferroviaire]]
