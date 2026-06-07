---
title: "NBN EN 1992-1-1:2004 — Beton non arme"
type: norm-extract
source: "NBN EN 1992-1-1:2004"
norm: EC2
section: "12"
chapter: "Beton non arme"
tags: [EC2, eurocode-2, beton-non-arme]
related: ["[[EC2_index]]", "[[EC2_11_beton-granulats-legers.md]]", "[[EC2_A_coefficients-partiels.md]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# 12.1 Généralités

(1)P La présente Section fournit des règles complémentaires pour les structures en béton non armé ou lorsque le ferraillage mis en place est inférieur au minimum requis pour le béton armé.

Note : Les titres sont numérotés 12 suivi du numéro de la Section principale correspondante. Les titres d'un niveau inférieur sont numérotés dans l'ordre, sans lien avec les titres des sections précédentes.

(2) Cette section s'applique aux éléments pour lesquels l'effet des actions dynamiques peut être ignoré. Elle ne s'applique pas quand les effets sont ceux engendrés par des machines tournantes et les charges de trafic. A titre d'exemple on citera :
- les éléments principalement soumis à la compression autre que celle provoquée par la précontrainte, voiles, poteaux, arcs, voûtes et tunnels par exemple ;
- les semelles de fondations isolées et filantes ;
- les murs de soutènement ;
- les pieux dont le diamètre est ≥ 600 mm et pour lesquels N_Ed/A_c ≤ 0,3 f_ck.

(3) Pour les éléments de béton de granulats légers à structure fermée suivant la Section 11 ou pour les éléments et les structures préfabriqués en béton couverts par le présent Eurocode, il convient de modifier les règles de conception et de calcul en conséquence.

(4) Dans les éléments en béton non armé, il n'est pas exclu de disposer des armatures qui seraient nécessaires pour satisfaire les exigences d'aptitude au service et/ou de durabilité ou qui seraient nécessaires dans certaines parties de ces éléments. Ce ferraillage peut être pris en compte pour la vérification locale des états limites ultimes aussi bien que pour la vérification des états-limites de service.

# 12.3.1 Béton : hypothèses de calcul complémentaires

(1) Du fait de la plus faible ductilité du béton non armé, il convient de prendre des valeurs de α_cc,pl et α_ct,pl inférieures à α_cc et α_ct du béton armé.

Note : Les valeurs de α_cc,pl et α_ct,pl à utiliser dans un pays donné peuvent être fournies par son Annexe Nationale. Les valeurs recommandées sont α_cc,pl = 0,8 et α_ct,pl = 0,8.

(2) Lorsque des contraintes de traction sont prises en compte dans la résistance de calcul d'éléments de béton non armé, le diagramme contrainte-déformation (voir 3.1.7) peut être prolongé jusqu'à la résistance de calcul en traction par application de l'Expression (3.16) ou d'une relation linéaire.

f_ctd = α_ct · f_ctk,0,05 / γ_c (12.1)

(3) Les méthodes basées sur la mécanique de la rupture peuvent être utilisées sous réserve qu'on puisse montrer qu'elles conduisent au niveau de sécurité requis.

# 12.3 Matériaux

See subsection 12.3.1 for concrete calculation assumptions.

# 12.5 Analyse structurale : états-limites ultimes

(1) Du fait de la ductilité limitée du béton non armé, il convient de n'utiliser une analyse linéaire avec redistribution ou une analyse plastique - méthodes sans vérification explicite de la capacité de déformation, par exemple - que si leur application peut être justifiée.

(2) L'analyse structurale peut être basée sur la théorie de l'élasticité linéaire ou de l'élasticité non-linéaire. Dans le cas d'une analyse non-linéaire (selon la mécanique de la rupture, par exemple), il convient d'effectuer une vérification de la capacité de déformation.

# 12.6.1 Résistance de calcul aux forces axiales et aux moments

(1) Dans le cas des voiles, sous réserve de prévoir des dispositions constructives adéquates ainsi qu'une cure appropriée, les déformations imposées dues à la température ou au retrait peuvent être ignorées.

(2) Il convient de prendre les relations contrainte-déformation du béton non armé en 3.1.7.

(3) L'effort normal résistant, N_Rd, d'une section rectangulaire avec une excentricité uniaxiale e dans la direction de h_w, peut être prise égale à :

N_Rd = η f_cd × b × h_w × (1-2e/h_w) (12.2)

où:
- η f_cd est la résistance de calcul effective en compression (voir 3.1.7 (3))
- b est la largeur totale de la section droite
- h_w est la hauteur totale de la section droite
- e est l'excentricité de N_Ed dans la direction h_w.

Note : Lorsque d'autres méthodes simplifiées sont utilisées, il convient qu'elles ne soient pas moins conservatrices qu'une méthode plus rigoureuse utilisant une relation contrainte-déformation donnée en 3.1.7.

# 12.6.2 Rupture locale

(1)P Sauf si des mesures permettant d'éviter une rupture locale de la section par traction ont été prises, l'excentricité maximale de la force axiale N_Ed dans la section doit être limitée afin d'éviter l'apparition de fissures ouvertes.

# 12.6.3 Effort tranchant

(1) Il est possible de tenir compte de la résistance en traction du béton dans les éléments en béton non armé à l'état-limite ultime d'effort tranchant, sous réserve que, soit par calcul soit par expérience, la rupture fragile puisse être exclue et qu'une résistance adéquate puisse être assurée.

(2) Pour une section soumise à un effort tranchant V_Ed et un effort normal N_Ed agissant sur une aire comprimée A_cc, il convient de prendre les valeurs suivantes pour la valeur absolue des composantes des contraintes de calcul :

σ_cp = N_Ed / A_cc (12.3)

τ_cp = k V_Ed / A_cc (12.4)

Note: la valeur de k à utiliser dans un pays donné peut être fournie par son Annexe Nationale. La valeur recommandée est k = 1,5.

Et il y a lieu de vérifier que:

τ_cp ≤ f_cvd

où
si σ_cp ≤ σ_c,lim : f_cvd = √(f_ctd² + σ_cp · f_ctd) (12.5)

ou bien
si σ_cp > σ_c,lim : f_cvd = √(f_ctd² + σ_cp · f_ctd) - (σ_cp - σ_c,lim) · σ_cp / (f_ctd + f_cd) (12.6)

σ_c,lim = f_cd - 2 (12.7)

avec :
- f_cvd   résistance de calcul en cisaillement et compression du béton
- f_cd résistance de calcul en compression du béton
- f_ctd   résistance de calcul en traction du béton

(3) Un élément en béton peut être considéré comme non fissuré à l'état-limite ultime s'il reste complètement comprimé ou bien si la valeur absolue de la contrainte principale de traction dans le béton σ_ct1 ne dépasse pas f_ctd.

# 12.6.4 Torsion

(1) Il convient normalement de ne pas dimensionner les éléments fissurés pour résister à des moments de torsion, sauf s'il est possible de le justifier par ailleurs.

# 12.6.5.1 Élancement des poteaux et des voiles

(1) L'élancement d'un poteau ou d'un voile est donné par :

λ = l_0 / i (12.8)

où :
- i est le rayon de giration minimal
- l_0 est la longueur efficace de l'élément, qui peut être supposée égale à :

l_0 = β · l_w (12.9)

avec :
- l_w hauteur libre de l'élément
- β coefficient qui dépend des conditions d'appui :
  - pour les poteaux, il convient en général de retenir β = 1
  - pour les poteaux et les voiles libres à une extrémité β = 2
  - pour les autres voiles, les valeurs de β sont données dans le Tableau 12.1

(2) Il convient de majorer de façon appropriée les valeurs de β si la capacité portante transversale est affectée par des saignées ou des évidements.

(3) Un voile transversal peut être considéré comme un voile de contreventement si :
- son épaisseur totale n'est pas inférieure à 0,5 h_w, où h_w est l'épaisseur totale du voile qu'il contrevente
- il a la même hauteur l_w que le voile qu'il contrevente
- sa longueur l_ht est au moins égale à l_w / 5, où l_w est la hauteur libre du voile contreventé
- il ne comporte pas d'ouvertures sur la longueur l_ht

(4) Dans le cas d'un voile lié de manière rigide en flexion le long de ses bords haut et bas, par du béton coulé en place et un ferraillage approprié, de sorte que les moments sur ses bords peuvent être complètement équilibrés, les valeurs de β données au Tableau 12.1 peuvent être multipliées par 0,85.

(5) Il convient que l'élancement des voiles en béton non armé coulés en place n'excède pas λ = 86 (c'est-à-dire l_0/h_w = 25).

# 12.6.5.2 Méthode de calcul simplifiée pour les voiles et les poteaux

(1) En l'absence d'une approche plus rigoureuse, l'effort normal résistant de calcul pour un voile ou un poteau élancé en béton non armé peut être calculé comme suit :

N_Rd = b × h_w × f_cd × Φ (12.10)

où
- N_Rd est l'effort normal résistant
- b est la largeur totale de la section
- h_w est la profondeur totale de la section
- Φ est un facteur prenant en compte l'excentricité et incluant les effets du second ordre ainsi que les effets normaux de fluage; voir ci-dessous

Pour les éléments contreventés, le facteur Φ peut être pris égal à :

Φ = (1,14 × (1-2e_tot/h_w) - 0,02 × l_o/h_w) ≤ (1-2 e_tot/h_w) (12.11)

où :
e_tot = e_o + e_i (12.12)

- e_o est l'excentricité du premier ordre incluant, le cas échéant, les effets des planchers (éventuels moments transmis par la dalle au voile, par exemple) et les actions horizontales
- e_i est l'excentricité additionnelle couvrant les effets des imperfections géométriques, voir 5.2

(2) D'autres méthodes simplifiées peuvent être utilisées sous réserve qu'elles conduisent à une sécurité au moins égale à celle obtenue par une méthode rigoureuse conformément à 5.8.

# 12.6.5 États-limites ultimes provoqués par une déformation structurale (flambement)

See subsections 12.6.5.1 and 12.6.5.2 for slenderness criteria and calculation methods.

# 12.6 États-limites ultimes (ELU)

See subsections 12.6.1 through 12.6.5 for verification methods.

# 12.7 États-limites de service (ELS)

(1) Il convient de vérifier les contraintes là où des gênes structurales sont susceptibles de se produire.

(2) Il convient d'adopter les mesures suivantes pour assurer une aptitude au service adéquate:

a) en ce qui concerne la formation de fissures:
- limitation des contraintes de traction dans le béton à des valeurs admissibles
- mise en place d'un ferraillage auxiliaire (armatures de peau, chaînages si nécessaire)
- mise en place de joints de construction
- choix de technologie du béton (par exemple, composition appropriée du béton, cure)
- choix de méthodes de construction appropriées

b) en ce qui concerne la limitation des déformations:
- dimensions minimales de la section (voir 12.9 ci-après)
- limitation de l'élancement dans le cas d'éléments comprimés

(3) Pour toute armature mise en place dans le béton non armé, même si elle n'est pas prise en compte dans les vérifications de résistance, il convient de satisfaire à 4.4.1.

# 12.9.1 Éléments structuraux

(1) Il convient que l'épaisseur totale h_w des voiles en béton coulé en place ne soit pas inférieure à 120 mm.

(2) Il convient de procéder aux vérifications de résistance et de stabilité nécessaires de tout élément comprenant des saignées ou des évidements.

# 12.9.2 Joints de construction

(1) Si des contraintes de traction sont attendues dans le béton des joints de construction, il convient de prévoir des armatures afin de limiter la fissuration.

# 12.9.3 Semelles isolées et semelles filantes superficielles

(1) En l'absence de données plus précises, les semelles isolées et les semelles filantes superficielles soumises à des charges axiales peuvent être calculées et les dispositions constructives retenues en considérant que le béton est non armé, sous réserve que :

0,85 · h_F · f_ctd / a ≥ 9 σ_gd (12.13)

où :
- h_F est la hauteur de la fondation
- a est le débord de la fondation par rapport au poteau
- σ_gd est la valeur de calcul de la pression du sol
- f_ctd est la valeur de calcul de la résistance en traction du béton (dans la même unité que σ_gd)

La relation simplifiée h_F / a ≥ 2 peut être utilisée.

# 12.9 Dispositions constructives relatives aux éléments et règles particulières

See subsections 12.9.1 through 12.9.3 for structural elements, construction joints, and foundation design.

---

Liens : [[EC2_index]] · [[EC2_11_beton-granulats-legers.md]] · [[EC2_A_coefficients-partiels.md]] · [[_Knowledge — Index]] · [[CLAUDE]]
