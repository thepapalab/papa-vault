---
title: "NBN EN 1997-2:2007 — Annexe G Essai de pénétration dynamique (DP)"
type: norm-extract
source: "NBN EN 1997-2:2007 + ANB:2013 + AC:2010 — Eurocode 7 — Calcul géotechnique — Partie 2 : Reconnaissance des terrains et essais, Bureau de Normalisation, 2e éd. août 2007, version française"
norm: EC7-2
section: "Annexe G"
chapter: "Essai de pénétration dynamique (DP) — corrélations et exemples"
tags: [EC7-2, eurocode-7, DP, DPL, DPH, DPSH, indice-densite, angle-frottement, module-oedometrique, correlation-DPH-qc]
related: ["[[EC7-2_index]]", "[[EC7-2_4_essais-en-place]]", "[[EC7-2_F_SPT]]", "[[EC7-2_D_CPT-CPTU]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# NBN EN 1997-2:2007 — Annexe G Essai de pénétration dynamique (DP)

## Annexe G (informative) — Essai de pénétration dynamique (DP)

### G.1 Corrélations $N_{10} \to I_D$ pour différents pénétromètres

(1) Corrélations pour $I_D$ à partir d'essais DP (domaine de validité : $3 \leq N_{10} \leq 50$) :

**Sable mal gradué ($C_U \leq 3$) — au-dessus de la nappe :**

$$I_D = 0{,}15 + 0{,}260 \log N_{10L} \quad \text{(DPL)}$$

$$I_D = 0{,}10 + 0{,}435 \log N_{10H} \quad \text{(DPH)}$$

**Sable mal gradué ($C_U \leq 3$) — sous la nappe :**

$$I_D = 0{,}21 + 0{,}230 \log N_{10L} \quad \text{(DPL)}$$

$$I_D = 0{,}23 + 0{,}380 \log N_{10H} \quad \text{(DPH)}$$

**Gravier sableux bien gradué ($C_U \geq 6$) — au-dessus de la nappe :**

$$I_D = -0{,}14 + 0{,}550 \log N_{10H} \quad \text{(DPH)}$$

> [!note] NOTE
> Source : Stenzel et al. (1978), DIN 4094-3:2002. Voir X.3.4.

### G.2 Corrélation $I_D \to \varphi'$ pour sols grenus pulvérulents

**Tableau G.1 — Angle de frottement interne $\varphi'$ en fonction de $I_D$ et $C_U$**

| Type de sol | Plage de $I_D$ [%] | Description | $\varphi'$ [°] |
|---|---|---|---|
| Sable peu de fines, mal gradué ($C_U < 6$) | 15 – 35 | lâche | 30 |
| | 35 – 65 | moyennement dense | 32,5 |
| | > 65 | dense | 35 |
| Sable, gravier sableux, bien gradué ($6 \leq C_U \leq 15$) | 15 – 35 | lâche | 30 |
| | 35 – 65 | moyennement dense | 34 |
| | > 65 | dense | 38 |

> [!note] NOTE
> Source : DIN 1054-100:1996. Voir X.3.4.

### G.3 Détermination de $E_{oed}$ à partir des résultats DP

(1) Module œdométrique en fonction de la contrainte verticale :

$$E_{oed} = w_1 \cdot p_a \left( \frac{\sigma'_v + 0{,}5 \Delta\sigma'_v}{p_a} \right)^{w_2}$$

avec $w_2 = 0{,}5$ (sables $C_U \leq 3$) ou $w_2 = 0{,}6$ (argiles peu plastiques, $I_p \leq 10$, $w_L \leq 35$).

Valeurs du coefficient de raideur $w_1$ à partir des résultats DP :

**Sables mal gradués ($C_U \leq 3$) — au-dessus de la nappe :**

$$w_1 = 214 \log N_{10L} + 71 \quad \text{(DPL ; } 4 \leq N_{10L} \leq 50\text{)}$$

$$w_1 = 249 \log N_{10H} + 161 \quad \text{(DPH ; } 3 \leq N_{10H} \leq 10\text{)}$$

**Argiles peu plastiques, fermes ($0{,}75 \leq I_c \leq 1{,}30$) — au-dessus de la nappe :**

$$w_1 = 4 N_{10L} + 30 \quad \text{(DPL ; } 6 \leq N_{10L} \leq 19\text{)}$$

$$w_1 = 6 N_{10H} + 50 \quad \text{(DPH ; } 3 \leq N_{10H} \leq 13\text{)}$$

> [!note] NOTE
> Source : Stenzel et al. (1978), Biedermann (1984), DIN 4094-3:2002. Voir X.3.4.

### G.4 Corrélation $N_{10H}$ (DPH) $\to q_c$ (CPT) — pour calcul de portance des pieux

(1) La Figure G.1 donne des exemples de corrélations entre $N_{10H}$ (DPH) et $q_c$ (CPT) dans les sables (objectif : appliquer les méthodes D.6 / D.7 à partir de données DP). Quatre courbes selon le type de sol et la position par rapport à la nappe :

1. Sable mal gradué — au-dessus de la nappe
2. Sable mal gradué — sous la nappe
3. Sable et gravier bien gradués — au-dessus de la nappe
4. Sable et gravier bien gradués — sous la nappe

> [!note] NOTE
> Source : Stenzel et al. (1978), DIN 4094-3:2002. Voir X.3.4. Référence croisée : Section 4.3.4.2(1)P et Annexe D.6.

### G.5 Corrélations entre différents pénétromètres dynamiques

(1) Corrélations pour les sables mal gradués ($C_U < 3$) — au-dessus de la nappe :

**À partir des résultats DPH :**

$$N_{10L} = 3 N_{10H} \quad \text{(domaine de validité : } 3 \leq N_{10H} \leq 20\text{)}$$

**À partir des résultats DPL :**

$$N_{10H} = 0{,}34 N_{10L} \quad \text{(domaine de validité : } 3 \leq N_{10L} \leq 50\text{)}$$

> [!note] NOTE
> Source : Stenzel (1978), Biedermann (1984), DIN 4094-3. Pour les argiles, voir Butcher, McElmeel, Powell (1995). Voir X.3.4.

---

Liens : [[EC7-2_index]] · [[EC7-2_F_SPT]] · [[EC7-2_HIJ_WST-FVT-DMT-PLT]] · [[_Knowledge — Index]] · [[CLAUDE]]
