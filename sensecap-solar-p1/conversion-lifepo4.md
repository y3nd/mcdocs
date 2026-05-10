# Conversion Li-ion vers LiFePO4

:::warning
Ce guide est purement théorique et n'a pas été testé par l'auteur. Il est basé sur des recherches et des connaissances générales sur les batteries Li-ion et LiFePO4, ainsi que sur les composants électroniques nécessaires pour la conversion. Il est fortement recommandé de faire des recherches supplémentaires et de consulter des experts en électronique avant de tenter cette conversion.
:::

:::warning
Cette conversion implique des risques et nécessite une expertise technique en électronique et en soudure de précision. Procédez avec prudence et assurez-vous de suivre les instructions avec soin.
:::

Les Sensecap Solar P1 sont équipés de batteries Li-ion. Cependant, il est possible de les convertir pour utiliser des batteries LiFePO4, qui offrent une meilleure sécurité et une durée de vie plus longue. Voici un guide **théorique** pour effectuer cette conversion.

## Idée générale
La conversion consiste à remplacer les cellules Li-ion par des cellules LiFePO4, ainsi que les circuits de charge et de protection associés.

<img src="https://files.seeedstudio.com/wiki/SenseCAP/Meshtastic/solar_node_diagram.png" alt="isolated" width="400"/>

## Matériel nécessaire
- 1 à 4 cellules LiFePO4 (en fonction de la capacité souhaitée)
- Une puce de charge solaire LiFePO4: CN3059
- Une puce de BMS LiFePO4: R5478N184CJ

## Outils et compétences requises
- Compétences en soudure de précision
- Multimètre pour tester les connexions
- Poste de soudure avec une pointe fine
- Flux de soudure
- Acétone pour retirer le verni de tropicalisation

## Étapes de conversion
1. Ouvrir le boitier du Sensecap Solar P1 et retirer les cellules Li-ion existantes.
2. Déconnecter et démonter la carte électronique
3. Identifier les composants suivants:
    - Le circuit de charge solaire Li-ion CN3065 en boitier DFN8
    - Le circuit de protection Li-ion R5478N218CD-TR-FF
4. Dessouder les composants CN3065 et R5478N218CD-TR-FF de la carte électronique.
5. Souder les composants CN3059 et R5478N184CJ à la place des composants précédents
6. Re-appliquer le verni de tropicalisation
7. Remonter la carte électronique dans le boitier
8. Connecter les cellules LiFePO4. Attention, il faudra certainement ajuster les connexions car les emplacements sont prévus pour des cellules button-top et non flat-top. Il est possible de remplacer par un pack LiFePO4 pré-assemblé.

## Ressources
- [Wiki Seeedstudio SenseCAP Solar P1](https://wiki.seeedstudio.com/meshtastic_solar_node/)
- [Diagramme block issu du wiki Seeedstudio](https://files.seeedstudio.com/wiki/SenseCAP/Meshtastic/solar_node_diagram.png)
- [Datasheet CN3065](https://content.instructables.com/FGJ/QXX8/MH9I7U1D/FGJQXX8MH9I7U1D.pdf)
- [Datasheet R5478](https://www.mouser.com/datasheet/2/294/r5478_ea-3159015.pdf)
- [Datasheet CN3059](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/196/CN3059.pdf)