---
next:
  link: /sensecap-solar-p1/flash-meshcore
  text: Flash MeshCore
previous:
  link: /sensecap-solar-p1/preparation-materielle
  text: Préparation matérielle
---

# Flash bootloader
Le bootloader est un petit programme qui s'exécute au démarrage de l'appareil et qui permet de charger le firmware principal (MeshCore dans notre cas). Le bootloader de base ne permet pas de réaliser des mises à jour du firmware via Bluetooth (OTA: Over The Air) de manière fiable. Il est donc nécessaire de le remplacer par un bootloader amélioré et conçu pour les mises à jour OTA.

Avantages du bootloader OTAFIX par rapport au bootloader de base :
* Basculement automatique vers le mode OTA DFU si une mise à jour échoue
* Vitesses de mise à jour OTA considérablement plus rapides
* Possibilité d'entrer en mode OTA DFU en maintenant un bouton enfoncé pendant la réinitialisation.

## [Lien du bootloader OTAFIX (anglais)](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
## [Guide d'installation (anglais)](https://blog.meshcore.io/2026/04/06/otafix-bootloader)

## Étapes d'installation (simplifiées et traduites de l'anglais)

### 1. Entrer en mode UF2 DFU

Commencez par mettre votre appareil en mode UF2 DFU.

* Branchez l'appareil à votre ordinateur
* Appuyez rapidement deux fois sur le bouton reset (deux fois en moins de 0,5 seconde)
* Un lecteur USB UF2 devrait apparaître ; le nom du lecteur varie selon l'appareil

---

### 2. Télécharger le bootloader OTAFIX

Vous pouvez maintenant télécharger directement le bootloader OTAFIX depuis le site de flashage MeshCore :

[flasher.meshcore.io](https://flasher.meshcore.io?utm_source=chatgpt.com)

* Sélectionnez votre appareil
* Choisissez **Repeater**
* Un lien de téléchargement pour le bootloader OTAFIX apparaîtra dans une bannière mise en évidence ; le fichier sera nommé `update-xxxx.uf2`

Le bootloader OTAFIX est également disponible sur le site officiel :

[OTAFIX Releases GitHub](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX/releases?utm_source=chatgpt.com)

* Téléchargez le fichier UF2 correspondant à votre appareil depuis la section **Assets**
* Les fichiers sont nommés sous la forme : `update-xxxx.uf2`
* Vous devrez peut-être cliquer sur **“Show more”** pour afficher tous les fichiers disponibles


**Pour la variante Seeed Sensecap Solar P1, vous devrez télécharger :

`update-sensecap_solar_p1_bootloader-0.9.2-OTAFIX2.2-BP1.3_nosd.uf2`

[Lien direct vers le bootloader OTAFIX pour Sensecap Solar P1](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX/releases/download/0.9.2-OTAFIX2.2-BP1.3/update-sensecap_solar_p1_bootloader-0.9.2-OTAFIX2.2-BP1.3_nosd.uf2)

:::warning
Il est recommandé de vérifier la page de téléchargement pour voir si une version plus récente du bootloader est disponible, car des améliorations et corrections de bugs sont régulièrement publiées.
:::

---

### 3. Installer le bootloader

* Glissez-déposez le fichier `update-xxxx.uf2` sur le lecteur UF2
* L'appareil va automatiquement :

  * mettre à jour le bootloader
  * redémarrer une fois l'opération terminée

---

### 4. Vérifier la mise à jour

* Entrez de nouveau en mode UF2 DFU
* Ouvrez encore une fois le fichier `INFO_UF2.TXT`
* La ligne de version devrait maintenant inclure `OTAFIX`

---

## Notes

* Par défaut le bootloader OTAFIX est configuré pour basculer automatiquement en mode OTA DFU si une mise à jour échoue, si le firmware ne démarre pas ou en l'absence de firmware.
* Afin de passer en mode USB DFU, il suffit de d'appuyer deux fois rapidement (moins de 0,5 seconde) sur le bouton reset.