---
title: "Particularités du modèle 3D et des plans 2D (en complément de l’article 36.3 du fascicule 61 v4)"
source: "103310_04_01.103_nlfr.md"
language: fr
---

# Terminologie

Dans ce paragraphe, les termes suivants sont définis successivement :

* Fichier 3D-DWG ;

* Fichier 3D-RVT ;
* Le modèle 3D ;
* Plan 2D et informations techniques spécifiques ;
* Le modèle 3D consolidé.

* Fichier 3D-DWG

Un fichier 3D-DWG est un fichier DWG dans lequel la conception est dessinée en trois dimensions dans l’espace modèle (Modelspace). Le fichier 3D-DWG constitue une partie composante du modèle 3D. Un fichier 3D-DWG est en soi également un modèle 3D.

* Fichier 3D-RVT

Un fichier 3D-RVT est un fichier RVT dans lequel la conception est réalisée en trois dimensions. Le fichier RVT contient à la fois un modèle 3D et les plans 2D correspondants. Le fichier 3D-RVT constitue une partie composante du modèle 3D. Un fichier 3D-RVT est en soi également un modèle 3D.

* Le modèle 3D

Le modèle 3D est l’ensemble de tous les fichiers 3D-DWG ou 3D-RVT inclus dans les documents du marché. Le modèle 3D constitue donc une collection de fichiers 3D-DWG et 3D-RVT distincts qui n’ont pas encore été intégrés en un modèle consolidé unique. Dans le texte ci-dessous, le terme « modèle 3D » est utilisé pour désigner les fichiers 3D-DWG ou 3D-RVT.

* Plan 2D

Un plan 2D est la représentation du résultat d’une conception réalisée en deux ou trois dimensions, présentée dans une mise en page prédéfinie.

Un plan 2D est soit un fichier DWG, un fichier DWF, un fichier PDF ou une feuille (sheet) dans un fichier RVT.

Si le plan 2D est un fichier DWG, la conception a été réalisée dans l’espace modèle (Modelspace) en deux ou trois dimensions. Seule la mise en page en espace papier (Paperspace layout) de ces fichiers DWG est applicable pour l’exécution des travaux et est contractuellement contraignante. Les représentations d’objets 3D sur ces plans sont uniquement fournies à titre visuel et de référence, et ne sont pas contractuellement contraignantes, tout comme la structure des calques de ces fichiers. Pour les objets 3D représentés sur les plans 2D, le modèle 3D original représentant ces objets prévaut en toutes circonstances. Le contenu du Modelspace ainsi que la structure des calques ne peuvent être invoqués par l’adjudicataire pour signaler des erreurs dans les documents contractuels.

Si le plan 2D concerne un fichier RVT, la conception a été réalisée dans une vue en deux ou trois dimensions. Seule la présentation en feuille (sheet layout) de ces fichiers RVT, portant la mention FINAL dans le cartouche, est applicable pour l’exécution des travaux et est contractuellement contraignante. Le fichier RVT peut contenir d’autres vues ainsi que d’autres feuilles utilisées pour l’élaboration du modèle 3D. Ces vues et feuilles supplémentaires ne sont pas contractuellement contraignantes.

Les plans 2D peuvent également être des plans de principe servant de complément au modèle 3D et étant indispensables à la transformation du modèle 3D en documents d’exécution, parmi lesquels (liste non limitative) : * Détails d’exécution ;

* Phasage des travaux ;
* Armatures ;
* Plan d’ensemble de la situation projetée ;
* Installation de chantier et accès chantier ;
* Étude de sol ;
* Etc.

* Informations techniques spécifiques

Pour certaines disciplines, des données de base spécifiques sont transmises dans un autre format (XML, XLSX, etc.). Ces données constituent un complément à la conception contenue dans les fichiers 3D-DWG, les fichiers 3D-RVT et les plans 2D.

* Le modèle 3D consolidé

Le modèle 3D consolidé est le modèle obtenu après la fusion de tous les fichiers 3D-DWG et 3D-RVT individuels en un seul modèle, complété par les informations pertinentes issues des plans 2D et des données techniques spécifiques. L’objectif du modèle 3D consolidé est de fournir une représentation visuelle de l’ensemble du projet et des différentes techniques, afin de permettre la maîtrise du phasage et des éventuelles difficultés d’exécution.

Dans le cadre du présent marché, l’établissement du modèle 3D consolidé sur la base du modèle 3D, des plans 2D et des informations techniques spécifiques constitue une charge contractuelle et doit être réalisé par l’adjudicataire sur la base des données fournies par l’adjudicateur dans les documents du marché. L’adjudicataire choisit lui-même le logiciel de consolidation qu’il souhaite utiliser.

# Général

Au début des travaux, l’adjudicataire reçoit un dossier de conception complet composé du modèle 3D, des plans 2D et des informations techniques spécifiques. Sur base de ces données, l’adjudicataire doit établir le modèle 3D consolidé afin d’obtenir une vue d’ensemble des travaux à réaliser. L’adjudicateur considère que ce dossier de conception contient toutes les informations utiles à la réalisation de l’étude d’exécution et des travaux. En conséquence, pendant l’exécution des travaux, l’adjudicateur ne fournira aucun fichier 3D-DWG, fichier 3D-RVT, plan 2D ou donnée complémentaire – à l’exception d’éventuels éléments manquants mentionnés au § 7 du présent article technique – ni aucune étude.

# Le modèle 3D

## Général

Le modèle 3D est mis à disposition de manière numérique dans le cadre du présent marché. Ce modèle 3D doit permettre à l’adjudicataire d'extraire toutes les données géométriques nécessaires relatives à l'état à réaliser ainsi qu'aux ouvrages d’art eux-mêmes (épaisseurs, longueurs, largeurs, composition, etc.), ainsi que les caractéristiques importantes des matériaux inclus dans la structure en couches du modèle 3D (dans le cas de fichiers 3D-DWG) ou les paramètres attribués aux objets 3D (dans le cas de fichiers 3D-RVT). Si les caractéristiques des matériaux d’un élément donné ne sont pas reprises dans la structure en couches du modèle 3D ou dans les paramètres attribués aux objets 3D dans les fichiers 3D-RVT, l’adjudicataire devra consulter les plans 2D, l’article technique correspondant ou les informations techniques spécifiques. Si l’adjudicataire estime que certaines données essentielles font défaut pour exécuter correctement le marché, il doit en faire la demande par écrit à l’adjudicateur. Ce dernier jugera de manière autonome si les données demandées sont ou non nécessaires à l’exécution du marché. Le fait que ces données soient ou non fournies ne pourra en aucun cas donner lieu à une quelconque indemnité ou prolongation de délai au bénéfice de l’adjudicataire.

Le modèle 3D est développé en trois dimensions selon les systèmes de coordonnées suivants : * Planimétrie : Lambert 72 (EPSG 31370 : Belge 1972 / Belgian Lambert 72) * Altimétrie (hauteur) : Deuxième Nivellement Général de la Belgique (TAW) (EPSG 5710 : Ostend Height)

L’adjudicataire doit être conscient que la situation as-built devra être remise à Infrabel sous forme de modèle 3D. Par conséquent, toutes les modifications relatives à la situation as-built, qui ne sont pas reprises dans les fichiers 3D-DWG ou les fichiers 3D-RVT obtenus au début des travaux, devront être ajoutées par l’adjudicataire dans ces fichiers 3D-DWG ou 3D-RVT initiaux et communiquées au pouvoir adjudicateur au plus tard 30 jours calendriers avant la réception provisoire du projet.

## Fichiers 3D-DWG

## Structure des layers

Le modèle 3D est construit sur base d'une structure de couches définie et établie contractuellement. Les couches (appelées « layers ») sont nommées selon la convention suivante : XX\_YYYY\_ZZ\_AAA\_texte Avec : * XX : acronyme de la discipline responsable de l’adjudicateur * ST : Structures * LT : Lines & Track * TR : Track * LV : Low Voltage * HV : High Voltage Si l’adjudicataire souhaite ajouter une couche au modèle 3D, il doit utiliser l’acronyme EB.

* YYYY (facultatif) : indication de l’ouvrage d’art concerné * ZZ (facultatif) : indication informative d’une partie des travaux * AAA (facultatif) : indication informative des différents éléments appartenant à une partie des travaux. Cette indication correspond souvent à une chronologie des travaux, mais ce n’est pas systématiquement le cas. L’adjudicataire ne peut donc se prévaloir d’éventuelles erreurs dans la chronologie des travaux à exécuter.
* Texte : description de la couche, avec éventuellement une référence à la partie 4 des documents du marché ou aux plans 2D. Les couches dont le nom commence par XX\_0\_CONSTRUCTIONLINE contiennent des éléments qui ont servi de base pour la conception, mais qui sont ajoutés à titre purement informatif et ne sont pas contractuellement contraignants. L’adjudicataire ne peut donc en aucun cas se fonder sur ces éléments pour invoquer d’éventuelles erreurs dans le modèle 3D ou pour signaler des éléments inconnus ou ambigus. L’adjudicataire est tenu de respecter cette convention de dénomination des couches lorsqu’il travaille avec le modèle 3D. Pour garantir la lisibilité du modèle 3D, certaines couches peuvent être « gelées ». Néanmoins, ces couches doivent également être prises en compte, et l’adjudicataire ne peut invoquer leur statut pour contester des éléments inconnus ou peu clairs.

## Configuration du système

Le modèle 3D est établi au format « AutoCAD 2018 Drawing ». TUC RAIL utilise actuellement la version 2025 du logiciel AutoCAD (AutoCAD, AutoCAD Map et AutoCAD Civil3D). Pendant l’exécution des travaux, le format « AutoCAD 2018 Drawing » doit impérativement être utilisé. L’utilisation d’un format de version ultérieure n’est autorisée que moyennant l’accord préalable et exprès des deux parties, à savoir l’adjudicateur et l’adjudicataire.

Les exigences minimales pour l’utilisation du modèle 3D et du logiciel AutoCAD Civil 3D versions 2023 à 2025 sont disponibles à l’adresse suivante : https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/System-requirements-for-Autodesk-Civil-3D-2025.html

## Modifications par l’adjudicateur ou l’adjudicataire

Toute modification ou complétion du dossier de conception repris dans le cahier des charges fait partie du dossier d’exécution à établir par l’adjudicataire et doit être traitée conformément à la procédure suivante : L’adjudicataire introduit numériquement le modèle 3D modifié ou complété, dans lequel la modification ou la complétion est indiquée de la manière suivante : Le modèle 3D (càd le(s) fichier(s) 3D-DWG modifié(s)) doit porter la dénomination suivante : AA-I-STATUS, où * AA : nom du fichier 3D-DWG original ayant fait l’objet d’une modification * I : nouvel index du fichier 3D-DWG * STATUS : indication du statut du fichier 3D-DWG : * DRAFT : cette version n’a pas encore été approuvée par l’adjudicateur * FINAL : tous les contrôles sur le fichier 3D-DWG ont été effectués par l’adjudicateur et le fichier peut être validé pour usage. Ce statut est attribué par l’adjudicateur.

* AS BUILT : le fichier est conforme aux travaux exécutés et ne peut plus être modifié

Toute modification est désignée et traitée comme suit : * Modification d’éléments déjà présents dans le fichier 3D-DWG ou ajout de nouveaux éléments par l’adjudicateur : L’adjudicataire identifie les couches dans la structure de couches dans lesquelles une modification a été effectuée, en attribuant un index. Cela peut concerner une modification du nom de la couche ou un ajustement dans le fichier 3D-DWG lui-même. Le nom de la couche devient donc : XX\_YYYY\_ZZ\_AAA\_(I)\_texte Avec (I) = index du fichier 3D-DWG – lettre alphabétique (A, B, C, …) Si plusieurs révisions se succèdent, le nom de la couche évoluera comme suit : XX\_YYYY\_ZZ\_AAA\_(II)\_(I)\_texte L’index le plus récent est placé en premier. Si une couche n’est plus applicable (par exemple, parce que l’élément n’est pas réalisé ou a été intégré dans une autre couche), tous les éléments de la couche doivent être supprimés, et un seul point doit être ajouté dans cette couche. Cela évite que la couche soit supprimée lors d’un « purge » du fichier. Dans ce cas, le nom de la couche devient : XX\_YYYY\_ZZ\_AAA\_(I)\_(CANCELLED)\_texte * Ajout de nouveaux éléments par l’adjudicataire : L’adjudicataire crée une nouvelle couche commençant par l’acronyme EB et respectant la nomenclature de la structure de couches décrite ci-dessus, dans laquelle les nouveaux éléments sont représentés. Dans ce cas, le nom de la couche est : EB\_YYYY\_ZZ\_AAA\_(I)\_texte Par ailleurs, pour chaque modification apportée à un fichier 3D-DWG, une description des modifications doit être conservée dans le fichier lui-même, en l’insérant dans une zone de texte liée à la couche intitulée XX\_Textes. Il convient de détailler précisément quelles modifications sont effectuées pour chaque index. Le modèle 3D modifié ou complété (c’est-à-dire le(s) fichier(s) 3D-DWG modifié(s)) est transmis à l’adjudicateur accompagné d’une note explicitant la modification ou la complétion (justification et impact sur les travaux à réaliser). Après examen par l’adjudicateur, cette modification ou complétion est soit rejetée, soit acceptée. Dans ce dernier cas, le modèle 3D révisé (c’est-à-dire le(s) fichier(s) 3D-DWG modifié(s)) est mis à disposition, avec les modifications ou complétions intégrées dans la structure de couches appropriée.

La dénomination du ou des fichiers 3D-DWG correspondants sera, après approbation par l’adjudicateur, modifiée en AA-I-FINAL et devra être mise à disposition de toutes les parties via la plateforme d’échange (voir paragraphe 6).

Ce n’est qu’après la mise à disposition du modèle 3D (c’est-à-dire du ou des fichiers 3D-DWG modifiés) que celui-ci pourra être traité par l’adjudicateur. Pour cette vérification, l’adjudicateur dispose du délai de 30 jour calendaire fixé dans le cahier des charges. Ce délai de 30 jours s’applique également pour la vérification des éventuelles révisions résultant de remarques précédemment émises.

Remarque importante :

Si l’adjudicataire modifie une couche, supprime une couche ou ajoute une couche supplémentaire au modèle 3D (c’est-à-dire un ou plusieurs fichiers 3D-DWG) sans respecter les principes mentionnés ci-dessus, cette modification ne sera pas examinée par le pouvoir adjudicateur et sera considérée comme inexistante par celui-ci. L’examen par l’adjudicateur des modifications apportées au modèle 3D peut entraîner la facturation de prestations supplémentaires à l’adjudicataire (voir également la partie 2 des documents du marché, paragraphe 36.4). Si l’adjudicataire souhaite, pour des raisons clairement définies, apporter des modifications à la procédure susmentionnée, cela doit être discuté lors de la première réunion de conception. À défaut, l’adjudicataire accepte la procédure telle que décrite ci-dessus.

## Fichiers 3D-RVT

## Paramètres

Le modèle 3D est composé d’objets/familles qui possèdent par défaut un certain nombre de paramètres contenant les informations de base relatives à cet élément. Ces informations de base décrivent les caractéristiques propres à l’élément ainsi que les informations concernant le responsable de cet élément.

## Phasage

Le modèle 3D est construit en différentes phases. Le phasage peut être attribuée à chaque objet/famille, ainsi qu’être représentée dans différentes vues sur une feuille sous forme de plan 2D avec une indication dans le cartouche comme « Final ». Il appartient à l’adjudicataire d’élaborer un phasage détaillé.

## Configuration du système

Le modèle 3D est réalisé dans un fichier RVT version 2025. TUC RAIL utilise actuellement Revit version 2025. Pendant l’exécution des travaux, il faut utiliser Revit version 2025. Revit 2025 n’est pas compatible avec les versions antérieures de Revit. L’utilisation d’une version supérieure n’est pas autorisée afin de garantir l’échange avec TUC RAIL. L’utilisation de fichiers IFC n’est pas autorisée.

Les exigences minimales pour l’utilisation du modèle 3D modélisé dans Revit 2025 sont disponibles sur : https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/System-requirements-for-Revit-2025-products.html

## Modifications par l’adjudicateur ou l’adjudicataire

Toute modification ou complétion du dossier de conception repris dans le cahier des charges fait partie du dossier d’exécution à établir par l’adjudicataire et doit être traitée conformément à la procédure suivante : L’adjudicataire introduit numériquement le modèle 3D modifié ou complété, dans lequel la modification ou la complétion est indiquée de la manière suivante : Le modèle 3D (càd le(s) fichier(s) 3D-RVT modifié(s)) doit porter la dénomination suivante : AA-I-STATUS, où * AA : nom du fichier 3D-RVT original ayant fait l’objet d’une modification * I : nouvel index du fichier 3D-RVT * STATUS : indication du statut du fichier 3D-RVT : * DRAFT : cette version n’a pas encore été approuvée par l’adjudicateur ;

* FINAL : tous les contrôles sur le fichier 3D-RVT ont été effectués par l’adjudicateur et le fichier peut être validé pour usage. Ce statut est attribué par l’adjudicateur.
* AS BUILT : le fichier est conforme aux travaux exécutés et ne peut plus être modifié

Chaque modification est indiquée et traitée comme suit : * Modification d’objets/familles déjà intégrés dans le fichier 3D-RVT par l’adjudicateur ou l’adjudicataire : En cas de modification, les paramètres suivants sont ajustés : * ACC\_File Name : un index est ajouté au nom actuel du fichier. Le nom du fichier devient donc : XXXX\_XX\_103\_XXX\_XXXX\_XXXXX\_XXX\_XXX-(I) * Avec (I) = index du fichier 3D-RVT – lettre alphabétique (A, B, C, ...) * ACC\_Engineer : si un objet/famille est modifié, l’ingénieur responsable de l’adjudicataire ou de l’adjudicateur (celui qui effectue la modification) assumera la responsabilité de cet objet.

* ACC\_CAD Designer : si un objet/famille est modifié, le modeleur CAD responsable de l’adjudicataire ou de l’adjudicateur (celui qui effectue la modification) assumera la responsabilité de cet objet. Si un objet/famille donné n’est plus applicable (par exemple parce qu’il ne sera pas réalisé ou qu’il a été intégré dans un autre objet/famille), les éléments concernés doivent être rendus invisibles (masqués) dans les vues 3D ainsi que dans les vues 2D. Le paramètre suivant est ajouté : * ACC\_Responsible Designer : il s’agit du nom du modeleur CAD de l’adjudicataire ou de l’adjudicateur (celui qui a effectué la modification).
* Ajout de nouveaux objets/familles par l’adjudicateur ou l’adjudicataire : Les paramètres suivants sont ajoutés à un nouvel élément : * ACC\_File Name : un index est ajouté au nom actuel du fichier. Le nom du fichier devient donc : XXXX\_XX\_103\_XXX\_XXXX\_XXXXX\_XXX\_XXX-(I) Avec (I) = index du fichier 3D-RVT – lettre alphabétique (A, B, C, ...) * ACC\_Engineer : si un objet/famille est nouvellement ajouté, l’ingénieur responsable de l’adjudicateur ou de l’adjudicataire (celui qui ajoute le nouvel objet) assumera la responsabilité de cet objet.
* ACC\_CAD Designer : si un objet/famille est nouvellement ajouté, le modeleur CAD responsable de l’adjudicateur ou de l’adjudicataire (celui qui ajoute le nouvel objet) assumera la responsabilité de l’objet dessiné.
* Paramètres représentant les caractéristiques propres de l’objet/famille * ACC\_Responsible Designer : il s’agit du nom de l’adjudicataire ayant modifié l’objet/la famille.

En outre, chaque modification apportée dans un fichier 3D-RVT doit être documentée dans la section “project issues” du fichier 3D-RVT, accessible via la vue 00\_About => Drafting views => 00.Start page. Chaque issue doit être liée à l’objet concerné à l’aide de l’étiquette disponible pour la création des project issues. Il convient de discuter en détail les modifications apportées pour chaque issue.

Le modèle 3D modifié/completé (c’est-à-dire le(s) fichier(s) 3D-RVT modifié(s)) est accompagné, lors de sa transmission à l’adjudicateur, d’une note contextualisant la modification/complément (justification et impact sur les travaux à exécuter). Après analyse par l’adjudicateur, cette modification/complément peut soit être refusée, soit acceptée. Dans ce dernier cas, l’acceptation se traduit par la mise à disposition du modèle 3D révisé (c’est-à-dire le(s) fichier(s) 3D-RVT modifié(s)) dans lequel/lesquels les modifications/compléments sont intégrés dans les objets/familles appropriés.

La dénomination du ou des fichiers 3D-DWG correspondants sera, après approbation par l’adjudicateur, modifiée en AA-I-FINAL et devra être mise à disposition de toutes les parties via la plateforme d’échange (voir paragraphe 6).

Ce n’est qu’après la mise à disposition du modèle 3D (c’est-à-dire du ou des fichiers 3D-RVT modifiés) que celui-ci pourra être traité par l’adjudicateur. Pour cette vérification, l’adjudicateur dispose du délai de 30 jour calendaire fixé dans le cahier des charges. Ce délai de 30 jours s’applique également pour la vérification des éventuelles révisions résultant de remarques précédemment émises.

Remarque importante :

Si l’adjudicataire modifie un objet/famille, cache (supprime temporairement) un objet/famille ou ajoute un nouvel objet/famille au modèle 3D (c’est-à-dire un ou plusieurs fichiers 3D-RVT) sans respecter les principes mentionnés ci-dessus, cette modification ne sera pas examinée par l’adjudicateur et sera considérée comme inexistante. L’examen par l’adjudicateur de toute modification du modèle 3D peut entraîner la facturation de prestations supplémentaires à l’adjudicataire (voir également la partie 2 des documents de marché, paragraphe 36.4). Si l’adjudicataire souhaite, pour des raisons clairement définies, apporter des modifications à la procédure susmentionnée, cela doit être discuté lors de la première réunion de conception. À défaut, l’adjudicataire accepte la procédure telle que décrite ci-dessus.

# plans 2D

## Modifications par l’adjudicateur ou l’adjudicataire

Les modifications des plans 2D par l’adjudicateur ou l’adjudicataire doivent toujours être effectuées selon les accords suivants : * Un plan modifié porte systématiquement un indice suivant celui du plan 2D concerné. Dans le cas d’un plan 2D intégré dans un fichier 3D-RVT, l’ensemble du fichier 3D-RVT ainsi que les plans 2D associés seront révisés.

* Les modifications sont brièvement décrites en haut de la page de titre pour chaque révision, par ordre alphabétique.
* Sur le plan 2D lui-même, toutes les adaptations doivent être indiquées par un nuage de révision mentionnant l’indice du plan, avec une représentation claire des éléments modifiés.
* Toute modification sur un plan 2D doit également être intégrée dans le modèle 3D (c’est-à-dire le(s) fichier(s) 3D-DWG ou 3D-RVT correspondant(s)) afin de permettre une visualisation consolidée du modèle et d’assurer une représentation des données as-built.

# informations techniques spécifiques

Ces données complètent la conception contenue dans les fichiers 3D-DWG et 3D-RVT ainsi que dans les plans 2D, et constituent des données de base fournies par l’adjudicateur. Ces données ne peuvent pas être modifiées par l’adjudicataire.

# liste des plans

L’adjudicataire met chaque semaine à disposition une liste des plans reprenant les dernières révisions des documents contractuels ainsi que les documents soumis pour approbation avec leur statut. Cela afin d’éviter toute discussion concernant les différents documents en circulation et de permettre à toutes les parties de se baser de manière univoque sur les mêmes documents.

# plateforme d’échange

## Général - objectif

Pour pouvoir suivre la gestion des documents créés durant les travaux, l’adjudicateur souhaite utiliser pour ce projet une plateforme sécurisée de stockage en ligne afin de sauvegarder, synchroniser et partager les documents élaborés. Tous les documents élaborés seront archivés sur cette plateforme. La plateforme doit être mise en place dès le début du projet et rester disponible jusqu’à la signature du décompte final. L’espace de stockage ainsi mis à disposition permettra la gestion de fichiers volumineux tout en garantissant leur disponibilité.

Cette plateforme a pour objectifs de : * centraliser la dernière version du modèle 3D (càd l’ensemble des différents fichiers 3D-DWG/3D-RVT) ;

* centraliser la dernière version des plans 2D ;
* centraliser la dernière version des informations techniques spécifiques ;
* centraliser la dernière version des documents d’exécution élaborés par l’adjudicataire et soumis pour approbation au maître d’ouvrage ;
* servir de base à la constitution du dossier as-built (voir l’article technique 01.101 « Dossier As-Built » de la partie 4 du cahier des charges) : la constitution du dossier as-built doit donc commencer dès le premier jour des travaux ;
* transmettre des documents au maître d’ouvrage en vue de la préparation de la réunion de conception ;
* centraliser les mesures et contrôles réalisés sur l’état d’exécution. Cette plateforme **n’**a **pas** pour objectif de : * valider ou officialiser les documents entre l’adjudicateur et l’adjudicataire : pour cela, la plateforme d’approbation (HERMES) est utilisée. Voir à ce sujet l’article 36 de la partie 2 du cahier des charges.

## La plateforme d’échange

**L’adjudicataire met à disposition une plateforme numérique pendant toute la durée des travaux, sur laquelle sont accessibles à tout moment le modèle 3D** (c’est-à-dire les fichiers 3D-DWG et 3D-RVT séparés), les plans 2D (au format DWG/RVT et/ou PDF) ainsi que les informations techniques spécifiques, de même que les documents d’exécution élaborés par l’adjudicataire et soumis pour approbation à l’adjudicateur. Avec ces documents est également mise à disposition une version récente de la liste des documents, incluant les différentes révisions des documents ainsi que leur statut.

Pour l’utilisation de la plateforme numérique, les droits de lecture et d’écriture nécessaires doivent être accordés tant à l’adjudicateur qu’à l’adjudicataire.

Les exigences système pour l’utilisation de la plateforme numérique sont un environnement Windows et une bande passante suffisante pour télécharger des fichiers volumineux.

Le contenu de la plateforme numérique doit être régulièrement mis à jour et géré par l’adjudicataire pendant toute la durée des travaux.

Le contenu de la plateforme doit être clairement structuré. Au début des travaux, l’adjudicataire soumet une structure de cette plateforme pour approbation à l’adjudicataire. Un exemple d’organisation de la plateforme est donné par :

* 01 Documents du marché – contractuel + 01 Fichiers 3D-DWG + 02 Fichiers 2D-DWG + 03 Fichiers 3D-RVT (y compris les plans 2D intégrés) + 04 Informations techniques spécifiques * 02 Dossier d’exécution + 01 Fichiers 3D-DWG – POUR APPROBATION + 02 Fichiers 2D-DWG – POUR APPROBATION + 03 Fichiers 3D-RVT – POUR APPROBATION + 04 Fiches techniques + 05 Procédures d’exécution * 03 Réunion de conception + 01 Préparation + 02 Rapports

La sous-structure des dossiers pour les fichiers 3D-DWG / 2D-DWG / 3D-RVT est définie comme suit :

* 01 Voies * 02 Ouvrages d’art + KW01 + KW02 + … * 03 Plateforme * 04 Hydraulique * 05 Voirie * 06 Caténaire * 07 Signalisation * 08 Telecom

Tant l’adjudicateur que l’adjudicataire valident cette structure et ne peuvent plus en dévier après validation. Toute modification ultérieure de la structure doit être préalablement approuvée par les deux parties avant d’entrer en vigueur. Le contenu de cette plateforme servira également de base pour la constitution du dossier as-built (voir à ce sujet l’article technique 01.101 « Dossier As-Built » de la partie 4 des documents du marché). La constitution du dossier as-built doit donc commencer dès le premier jour des travaux et nécessite des ajustements continus des fichiers déposés par l’adjudicataire sur cette plateforme. Après les travaux, l’intégralité du contenu de cette plateforme — complétée par les exigences supplémentaires du dossier as-built — deviendra la propriété de l’adjudicateur. Dans le métrage récapitulatif, aucune ligne spécifique n’est prévue pour l’utilisation de cette plateforme numérique. Le soumissionnaire doit en tenir compte dans son offre.

La plateforme d’échange doit être présentée lors de la première réunion de conception, où les éventuelles remarques de l’adjudicateur devront être prises en compte dans son développement. Ces remarques ne pourront en aucun cas donner lieu à une quelconque indemnisation ou compensation et doivent être considérées comme une charge contractuelle.

Les exigences auxquelles la plateforme doit répondre sont les suivantes : * Environnement convivial et intuitif, afin que l’outil puisse être utilisé facilement et rapidement par tous les collaborateurs du chantier ;

* Application web, compatible avec Microsoft Edge et Google Chrome, pour éviter l’installation d’un programme pour des opérations simples (comme la consultation d’un document) ;
* Notification lorsqu’un document est ajouté, mis à jour, lorsqu’un avis est donné ou une validation requise, avec la possibilité de choisir qui doit être informé, quand et pour quels événements, afin d’éviter un flux continu d’e-mails ;
* Nomenclature logique des documents, facile à comprendre et à retenir, à soumettre préalablement pour approbation à l’adjudicateur ;
* Archivage simple et structuré.

## Remarque importante

Il est rappelé que certains fichiers doivent être déposés par l’adjudicataire à la fois sur la plateforme d’approbation HERMES et sur la plateforme d’échange.

# remarques spécifiques pour ce projet