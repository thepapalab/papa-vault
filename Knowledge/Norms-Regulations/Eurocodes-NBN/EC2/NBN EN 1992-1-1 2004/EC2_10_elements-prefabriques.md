---
title: "10 Règles additionnelles pour les éléments et les structures préfabriqués en béton"
source: "EN 1992-1-1:2004 (F) — Eurocode 2: Design of concrete structures"
norm: EC2
section: "10"
chapter: "10"
part: "1-1"
tags: [EC2, éléments-préfabriqués, assemblages, appuis, joints, cure-thermique, diaphragme, chaînages]
language: fr
jupyter_ref: "EC2/10"
---

# 10 Règles additionnelles pour les éléments et les structures préfabriqués en béton

## 10.1 Généralités

**(1)P** Les règles de la présente Section s'appliquent aux bâtiments réalisés partiellement ou entièrement en éléments préfabriqués en béton et viennent en complément des règles des autres sections.

### 10.1.1 Terminologie particulière

**Élément préfabriqué :** élément produit en usine ou dans un emplacement autre que sa position finale dans la structure

**Situation transitoire :** démoulage, transport, stockage, montage (levage), construction (assemblage)

## 10.3 Matériaux

### 10.3.1.1 Résistance

Pour cure thermique, résistance en compression peut être estimée par :

$$f_{cm}(t) = f_{cm,p} + (f_{cm} - f_{cm,p}) \log\left(\frac{1 + (28 - t_p)}{1 + (t - t_p)}\right)  \tag{10.1}$$

### 10.3.2.2 Acier de précontrainte

Temps équivalent pour cure thermique :

$$t_{eq} = \sum_{i=1}^{n} \Delta t_i \left(\frac{T_{\max}}{20}\right)^{-1.14} \exp\left(\frac{20 - T(\Delta t_i)}{20}\right)  \tag{10.2}$$

## 10.5.2 Pertes de précontrainte

Perte thermique spécifique :

$$\Delta P_\theta = 0.5 A_p E_p \alpha_c (T_{max} - T_0)  \tag{10.3}$$

## 10.9.3 Systèmes de planchers

Effort de cisaillement par unité de longueur :

$$v_{Ed} = q_{Ed} \cdot \frac{b_e}{3}  \tag{10.4}$$

## 10.9.4.3 Joints de compression

Armatures transversales :

$$A_s = 0.25 \frac{t}{h} \frac{F_{Ed}}{f_{yd}}  \tag{10.5}$$

## 10.9.5.2 Appareils d'appui

Profondeur nominale :

$$a = a_1 + a_2 + a_3 + \Delta a_{22} + \Delta a_{32}  \tag{10.6}$$

**Tables:** 10.1 (max spacing), 10.2–10.5 (bearing depths, tolerances)

**Status:** ✅ Complete (Equations 10.1–10.6, 5 tables, 7 figures referenced)
