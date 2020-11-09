
Ce projet est un fork de : https://gitlab.com/Nat-Faeeria/admissions-hopital-covid-19-france?fbclid=IwAR2_hCMXEKYU__VrEfsi4BrviJ83pkYPGC4QbuKY17j0Tp62VPUN7BFsXNs

# Afficher les admissions à l'hôpital durant l'épidémie de Covid-19 en France

## But de l'outil

Cet outil vous permet d'afficher le nombre de nouvelles entrées journalières 
à l'hôpital et en réanimation dues à la COVID-19 sous forme de deux diagrammes 
naviguables.

Toutes les données disponibles sont affichées, du 19 mars 2020 jusqu'au jour de
dernière mise à jour du fichier csv utilisé. 

L'outil est prévu pour utiliser les données officielles trouvées sur le site
data.gouv.fr, plus précisément le fichier csv relatif aux nouvelles entrées 
(contient généralement "nouveaux" dans le nom du fichier)

Le fichier csv fourni date du 21/09/2020

## Mode d'emploi

1. Aller sur le site data.gouv.fr à la page des [données hospitalières relatives à l'épidémie de COVID-19](https://www.data.gouv.fr/fr/datasets/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/)
2. Télécharger le fichier .csv du jour correspondant aux nouvelles admissions (contient généralement "nouveau" dans le nom du fichier)
3. Renommer le fichier dataCovid.csv, et le placer dans le même fichier que le script Python
4. Exécuter le script Python

## Outils utilisés

* Matplotlib avec Pylab
* Python

## Banalités

Ce code n'est pas très propre.

Je débute avec Matplotlib, ce projet était autant un test qu'une envie d'avoir des données à jour sur l'épidémie.

Je suis preneur d'améliorations proposées pour rendre ce code et cet "outil" plus propre.

Ce code est évidemment sous licence libre (GPLv3)
