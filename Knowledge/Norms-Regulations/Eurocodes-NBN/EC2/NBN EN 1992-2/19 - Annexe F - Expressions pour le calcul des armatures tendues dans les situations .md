---
parent: "[[00 - Index]]"
norm: "NBN EN 1992-2:2005"
---

## Annexe F — Expressions pour le calcul des armatures tendues dans les situations de contraintes planes

ANNEXE  F
(informative)

Expressions pour le calcul des armatures tendues dans les situations de contraintes
planes

NOTE:  La convention de signes utilisée dans la présente Annexe est identique à celle de l'EN 1992-1-1 et
est différente de celle utilisée en 6.9, à l'Annexe LL et à l'Annexe MM de la présente norme.

Les clauses suivantes de l'EN 1992-1-1 s'appliquent.
| F.1 (1)  |     | F.1 (2)  | F.1 (3)  |     | F.1 (5)  |     |
| -------- | --- | -------- | -------- | --- | -------- | --- |

F.1  Généralités

 ≤ τ2
(104)  Lorsque σ  est une traction ou que σ  ⋅ σ , des armatures sont à prévoir.
|     | Edy |     | Edx Edy | Edxy |     |     |
| --- | --- | --- | ------- | ---- | --- | --- |

Les armatures de béton armé optimales, correspondant à θ = 45°, représentées par l’indice
supérieur ′, et la contrainte dans le béton correspondante, sont déterminées par :

| Pour σ  ≤  |τ | |    |     |     |     |     |     |
| ------------- | ---- | --- | --- | --- | --- | --- |
| Edx           | Edxy |     |     |     |     |     |

| f′ = |τ | |−σ |     |     |     |     | (F.2)  |
| ------- | --- | --- | --- | --- | --- | ------ |
tdx Edxy Edx
| f′ = |τ | |−σ |     |     |     |     | (F.3)  |
| ------- | --- | --- | --- | --- | --- | ------ |
tdy Edxy Edy
| σ  = 2|τ | |   |     |     |     |     | (F.4)  |
| -------- | --- | --- | --- | --- | --- | ------ |
cd Edxy

| Pour σ Edx  >  |τ | Edxy |  |     |     |     |     |     |
| ----------------- | ------- | --- | --- | --- | --- | --- |

| f′ = 0  |     |     |     |     |     |  (F.5)  |
| ------- | --- | --- | --- | --- | --- | ------- |
tdx
τ2
Edxy
| f′ = | −σ     |     |     |     |     |  (F.6)  |
| ---- | ------ | --- | --- | --- | --- | ------- |
tdy Edy
σ
Edx
τ
| σ =σ | (1+ ( Edxy)2)  |     |     |     |     |  (F.7)  |
| ---- | -------------- | --- | --- | --- | --- | ------- |
cd Edx
σ
Edx

Il  convient  de  vérifier  la  contrainte  dans  le  béton, σ ,  avec  une  modélisation  réaliste  des
cd
sections fissurées (voir 6.109 ‘Éléments de plaque’ de l'EN 1992-2).

NOTE:  On obtient la quantité minimale d'armatures si les directions de celles-ci sont parallèles aux
directions des contraintes principales.

A défaut, dans le cas général, les armatures qui sont nécessaires, ainsi que la contrainte dans
le béton, peuvent être déterminées par :

| f  = |τ | |cotθ  - σ  |     |     |     |     |  (F.8)  |
| ------- | ----------- | --- | --- | --- | --- | ------- |
| tdx     | Edxy        | Edx |     |     |     |         |
| f  = |τ | |/cotθ  - σ |     |     |     |     |  (F.9)  |
| tdy     | Edxy        | Ed  |     |     |     |         |

| σ = τ | (cotθ+ | )   |     |     |     |  (F.10)  |
| ----- | ------ | --- | --- | --- | --- | -------- |
cd Edxy
cotθ

où θ  est l’angle de la contrainte principale de compression dans le béton par rapport à l’axe
des x.

NOTE:  Il convient de choisir la valeur de cotθ   de façon à éviter des valeurs de compression pour f .
td

Afin d'éviter des fissures inacceptables aux ELS, et d’assurer la capacité de déformation
requise aux ELU, il convient de limiter les sections des armatures obtenues pour chaque
direction à partir des Expressions (F.8) et (F.9) dans la fourchette de la moitié à deux fois les
sections d’armatures données par les Expressions (F.2) et (F.3) ou (F.5) et (F.6). Ces
limitations sont exprimées par ½f′ ≤f ≤2f′ et ½f′ ≤f ≤2f′ .
tdx tdx tdx tdy tdy tdy
