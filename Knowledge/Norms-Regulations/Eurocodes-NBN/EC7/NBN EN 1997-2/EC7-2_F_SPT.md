---
title: "NBN EN 1997-2:2007 — Annexe F Essai SPT"
type: norm-extract
source: "NBN EN 1997-2:2007 + ANB:2013 + AC:2010 — Eurocode 7 — Calcul géotechnique — Partie 2 : Reconnaissance des terrains et essais, Bureau de Normalisation, 2e éd. août 2007, version française"
norm: EC7-2
section: "Annexe F"
chapter: "Essai de pénétration au carottier (SPT) — corrélations et exemples"
tags: [EC7-2, eurocode-7, SPT, N60, indice-densite, angle-frottement, tassement, sable, Burland-Burbridge]
related: ["[[EC7-2_index]]", "[[EC7-2_4_essais-en-place]]", "[[EC7-2_D_CPT-CPTU]]", "[[EC7-2_G_DP]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# NBN EN 1997-2:2007 — Annexe F Essai SPT

## Annexe F (informative) — Essai de pénétration au carottier (SPT)

### F.1 Exemples de corrélations $N_{60} \to I_D$ — sables

(1) La relation entre le nombre de coups normalisé $(N_1)_{60}$, l'indice de densité $I_D = (e_{max} - e)/(e_{max} - e_{min})$ et la contrainte verticale effective $\sigma'_{v0}$ (en kPa × 10⁻²) dans un sable est :

$$\frac{(N_1)_{60}}{I_D^2} = a + b \sigma'_{v0}$$

Pour les sables normalement consolidés, $a$ et $b$ sont quasi-constants pour $0{,}35 < I_D < 0{,}85$ et $0{,}5 < \sigma'_{v0} < 2{,}5$ (kPa × 10⁻²) (Skempton 1986, Tableau 8).

**Tableau F.1 — Corrélation $(N_1)_{60} \to I_D$ pour sables naturels normalement consolidés**

| Classe | $(N_1)_{60}$ | $I_D$ [%] |
|---|---|---|
| Très lâche | 0 – 3 | 0 – 15 |
| Lâche | 3 – 8 | 15 – 35 |
| Moyennement dense | 8 – 25 | 35 – 65 |
| Dense | 25 – 42 | 65 – 85 |
| Très dense | 42 – 58 | 85 – 100 |

Pour $I_D > 0{,}35$ : $(N_1)_{60} / I_D^2 \approx 60$.

> [!note] NOTE
> Pour les sables fins, réduire $N$ dans le rapport 55/60. Pour les sables grossiers, augmenter dans le rapport 65/60.

**Tableau F.2 — Effet du vieillissement dans des sables fins normalement consolidés**

| Âge | $(N_1)_{60} / I_D^2$ |
|---|---|
| Essais de laboratoire | 35 |
| Remblais récents (~ 10 ans) | 40 |
| Dépôts naturels (> 100 ans) | 55 |

La surconsolidation accroît le coefficient $b$ d'un facteur $(1 + 2K_0) / (1 + 2K_{0;NC})$.

> [!note] NOTE
> Source : Skempton (1986). Voir X.3.3.

### F.2 Exemples de corrélations $I_D \to \varphi'$ — sables siliceux

**Tableau F.3 — $I_D \to \varphi'$ pour sables siliceux (US Army Corps of Engineers 1993)**

| $I_D$ [%] | Sable fin uniforme | Sable fin bien gradué | Sable moyen uniforme | Sable moyen bien gradué | Sable grossier uniforme | Sable grossier bien gradué |
|---|---|---|---|---|---|---|
| 40 | 34° | 36° | 36° | 38° | 38° | 41° |
| 60 | 36° | 38° | 38° | 41° | 41° | 43° |
| 80 | 39° | 41° | 41° | 43° | 43° | 44° |
| 100 | 42° | 43° | 43° | 44° | 44° | 46° |

> [!note] NOTE
> Voir X.3.3.

### F.3 Exemple de méthode de calcul du tassement des fondations superficielles (méthode Burland & Burbridge)

(1) Pour les sables surconsolidés ($q' \geq \sigma'_p$), le tassement immédiat $s_i$ [mm] d'une semelle carrée de largeur $B$ [m] :

$$s_i = \sigma'_p \cdot B^{0{,}7} \cdot \frac{I_{cc}}{3} + (q' - \sigma'_p) \cdot B^{0{,}7} \cdot I_{cc}$$

Pour $q' \leq \sigma'_p$ :

$$s_i = \sigma'_p \cdot B^{0{,}7} \cdot \frac{I_{cc}}{3}$$

Pour les sables normalement consolidés :

$$s_i = (q' - \sigma'_p) \cdot B^{0{,}7} \cdot I_{cc}$$

(2) Compressibilité de la couche de fondation par analyse de régression :

$$I_{cc}^{1{,}4} = \frac{1{,}71}{N}$$

où $N$ est la moyenne du nombre de coups SPT sur la profondeur d'influence $z_I = B^{0{,}75}$ (75 % du tassement).

> [!note] NOTE
> Ne pas corriger $N$ pour la pression verticale dans cette méthode. Pour $N > 15$, corriger $N' = 15 + 0{,}5 (N - 15)$ pour les sables fins ou limoneux immergés. Pour graviers, multiplier $N$ par ~1,25.

(3) Correction pour élancement L/B :

$$f_s = \frac{1{,}25 L/B}{(L/B) + 0{,}25}$$

$f_s \to 1{,}56$ pour $L/B \to \infty$. Aucune correction de profondeur nécessaire pour $D/B < 3$.

(4) Correction pour effets différés (fondations sur sables et graviers) :

$$f_t = 1 + R_3 + R_t \log(t/3)$$

- Charges statiques : $R_3 = 0{,}3$, $R_t = 0{,}2$ → à $t = 30$ ans : $f_t = 1{,}5$
- Charges fluctuantes (cheminées, ponts, silos) : $R_3 = 0{,}7$, $R_t = 0{,}8$ → à $t = 30$ ans : $f_t = 2{,}5$

> [!note] NOTE
> Source : Burland and Burbridge (1985). Voir X.3.3.

---

Liens : [[EC7-2_index]] · [[EC7-2_E_PMT]] · [[EC7-2_G_DP]] · [[_Knowledge — Index]] · [[CLAUDE]]
