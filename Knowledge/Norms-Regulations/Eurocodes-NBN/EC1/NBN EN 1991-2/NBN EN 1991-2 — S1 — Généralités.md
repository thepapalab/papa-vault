---
title: "NBN EN 1991-2 S1 — Généralités"
type: norm-extract
source: "NBN EN 1991-2:2004 (+ ANB 2011 + AC:2010)"
norm: EC1-2
section: "1"
chapter: "1"
tags: [EC1-2, NBN, généralités, domaine-application, définitions, symboles, ponts]
related: ["[[NBN EN 1991-2 — Index]]", "[[NBN EN 1991-2 — S4 — Trafic-Routier]]", "[[NBN EN 1991-2 — S6 — Trafic-Ferroviaire]]"]
language: fr
jupyter_ref: "EC1-2/1"
created: 2026-06-05
---

# Section 1 — Généralités

## 1.1 Domaine d'application

**(1)** L'EN 1991-2 spécifie les charges d'exploitation (modèles et valeurs représentatives) associées au trafic routier, à la circulation des piétons et au trafic ferroviaire, y compris les effets dynamiques, forces centrifuges, forces de freinage/accélération et actions accidentelles.

**(2)** Destinée au calcul des **ponts neufs**, piles, culées, murs garde-grève, murs en aile et en retour.

**(3)** Les modèles s'appliquent également aux murs de soutènement bordant routes et voies ferrées.

**(4)** L'EN 1991-2 est utilisée en association avec **EN 1990 (notamment A2)** et EN 1991 à EN 1999.

> [!note] Limites de domaine
> - Ponts routiers : longueur chargée ≤ **200 m** (calibrage LM1)
> - Ferroviaire : grandes lignes, voie standard ou grande, à l'exclusion des voies étroites, tramways, crémaillères, funiculaires

## 1.2 Références normatives

| Norme | Titre |
|-------|-------|
| EN 1317-1, -2, -6 | Dispositifs de retenue routiers |
| EN 1990 | Bases de calcul des structures |
| EN 1991-1-1 | Poids volumiques, poids propres, charges bâtiments |
| EN 1991-1-3 | Charges de neige |
| EN 1991-1-4 | Actions dues au vent |
| EN 1991-1-5 | Actions thermiques |
| EN 1991-1-6 | Actions en cours d'exécution |
| EN 1991-1-7 | Actions accidentelles |
| EN 1992 à EN 1999 | Eurocodes matériaux |

## 1.3 Principes et Règles d'Application

- **Principes (P)** : prescriptions sans alternative, identifiés par le numéro suivi de la lettre P.
- **Règles d'Application** : règles généralement reconnues, conformes aux Principes.
- Une règle alternative est admissible si la conformité aux Principes est démontrée avec un niveau de sécurité équivalent.

## 1.4 Termes et définitions

### 1.4.1 Termes communs

| Terme | Définition |
|-------|-----------|
| **tablier** | Parties du pont supportant la charge de trafic au-dessus des piles/culées (hors pylônes) |
| **dispositif de retenue** | Terme général pour dispositifs de retenue véhicules + piétons |
| **barrière de sécurité** | Dispositif en accotement ou terre-plein central |
| **barrière pour ouvrage d'art** | Barrière de sécurité en bordure de pont |
| **garde-corps** | Dispositif pour piétons, non destiné à la retenue des véhicules |
| **passerelle** | Pont principalement pour piétons/deux-roues ; trafic routier/ferroviaire interdit |
| **écran anti-bruit** | Écran de réduction du bruit |
| **passerelle fixe de visite** | Accès permanent pour inspection (non public) |
| **plate-forme mobile de visite** | Élément de véhicule, non solidaire du pont, pour inspection |

### 1.4.2 Termes propres aux ponts routiers

| Terme | Définition |
|-------|-----------|
| **chaussée** | Surface de route supportée par une structure unique, toutes voies réelles incluses |
| **bande d'arrêt** | Bande revêtue côté extérieur, utilisable en cas de difficultés |
| **bande dérasée** | Bande revêtue ≤ 2 m, entre voie et barrière |
| **terre-plein central** | Séparation entre chaussées d'une route à deux chaussées |
| **voie conventionnelle** | Bande parallèle au bord, largeur 3 m, pour modèles de charge |
| **aire résiduelle** | Chaussée − somme des voies conventionnelles |
| **tandem** | Assemblage de deux essieux consécutifs chargés simultanément |
| **charge exceptionnelle** | Charge ne pouvant circuler sans autorisation |

### 1.4.3 Termes propres aux ponts ferroviaires

| Terme | Définition |
|-------|-----------|
| **voies** | Rails + traverses, sur ballast ou fixées directement au tablier |
| **passage de service** | Bande entre voies et parapets |
| **vitesse de résonance** | Vitesse à laquelle la fréquence de chargement coïncide avec fréquence propre |
| **vitesse d'exploitation fréquente** | Vitesse la plus probable (utilisée pour fatigue) |
| **vitesse maximale de ligne** | Vitesse maximale autorisée au point considéré |

## 1.5 Symboles principaux

### 1.5.2 Symboles pour les sections 4 et 5 (ponts routiers)

| Symbole | Signification |
|---------|--------------|
| α_Qi, α_qi | Coefficients d'ajustement pour tandem et UDL sur voie i |
| α_qr | Coefficient d'ajustement pour UDL sur aire résiduelle |
| β_Q | Coefficient d'ajustement LM2 |
| Q_ik | Valeur caractéristique charge d'essieu tandem, voie i [kN] |
| q_ik | Valeur caractéristique UDL, voie i [kN/m²] |
| q_rk | UDL sur aire résiduelle [kN/m²] |
| Q_lk | Force longitudinale (freinage/accélération) |
| Q_tk | Force transversale (centrifuge) |
| q_fk | Charge UDL trottoirs/passerelles |
| n_l | Nombre de voies conventionnelles |
| w_l | Largeur d'une voie conventionnelle (= 3 m) |
| w | Largeur totale de chaussée |
| Δφ_fat | Coefficient dynamique supplémentaire pour fatigue aux joints |

### 1.5.3 Symboles pour la section 6 (ponts ferroviaires)

| Symbole | Signification |
|---------|--------------|
| α | Coefficient de classification (LM71, SW) |
| Φ₂ | Coefficient dynamique — voie soigneusement entretenue |
| Φ₃ | Coefficient dynamique — voie normalement entretenue |
| L_Φ | Longueur déterminante pour le coefficient dynamique [m] |
| Q_tk, q_tk | Force centrifuge caractéristique [kN, kN/m] |
| Q_sk | Effort de lacet caractéristique [kN] |
| Q_lbk | Force de freinage caractéristique [kN] |
| Q_lak | Force d'accélération caractéristique [kN] |
| F_Tk | Force longitudinale due à la température (interaction voie-ouvrage) |
| F_Qk | Force longitudinale due à la déformation (interaction voie-ouvrage) |
| K₂, K₅, K₂₀ | Raideur longitudinale d'appui [kN/m/m de voie] |
| ΔT_R, ΔT_D | Variation température rail / tablier |
| v, V | Vitesse maximale [m/s, km/h] |
| r | Rayon de courbure [m] |

---

Links: [[NBN EN 1991-2 — Index]] · [[NBN EN 1991-2 — S2-3 — Classification-Situations]] · [[NBN EN 1991-2 — S4 — Trafic-Routier]]
