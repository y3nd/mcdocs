---
next:
  link: /liens-utiles
  text: Liens utiles
previous:
  link: /sensecap-solar-p1/validation
  text: Validation du répéteur
---

# Maintenance
## Tests réguliers du signal
L'outil trace path permet de régulièrement tester les valeurs en émission et réception du signal du répéteur. Il est recommandé de faire ces tests à différents moments de la journée et dans différentes conditions météorologiques pour avoir une idée précise de la performance du répéteur.

Voir la section [Validation](./validation.md) pour plus d'informations sur les tests à réaliser.

## Date et heure
L'heure et la date du répéteur sont importantes pour le bon fonctionnement du réseau maillé. Il est recommandé de vérifier régulièrement que l'heure et la date sont correctes, surtout après une mise à jour du firmware ou un redémarrage du répéteur. L'heure peut également se décaler dans le temps, surtout si le GPS est désactivé.

Pour cela, il suffit de se connecter au répéteur via le companion et de vérifier l'heure et la date dans la console d'administration, onglet **Status**.

## Mise à jour du firmware
*Informations provenant de [GitHub oltaco/Adafruit_nRF52_Bootloader_OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)*

Il est recommandé de vérifier régulièrement les [mises à jour du firmware MeshCore](https://github.com/meshcore-dev/MeshCore/releases) et de les appliquer pour bénéficier des dernières améliorations et corrections de bugs.
Si vous avez installé le bootloader OTAFIX, les mises à jour du firmware peuvent être appliquées directement via Bluetooth (OTA) sans avoir besoin de connecter l'appareil à un ordinateur.

Afin de passer un répéteur en mode OTA DFU, il suffit de taper la commande suivante dans la console du répéteur :
```
start ota
```

Utiliser ensuite l'application **nRF Device Firmware Update** (**nRF DFU**) disponible sur ([Android](https://play.google.com/store/apps/details?id=no.nordicsemi.android.dfu&hl=en&gl=US) ou [iOS](https://apps.apple.com/sa/app/device-firmware-update/id1624454660)) pour appliquer la mise à jour OTA.