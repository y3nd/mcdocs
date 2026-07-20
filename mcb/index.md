# MCB: MeshCore Beacon
<img src="./mcb.avif" alt="MCB" target="_blank" width="500"/>

MCB (MeshCore Beacon) est le nom du protocole et projet pour l'utilisation de balises sur MeshCore. Il est conçu pour permettre aux utilisateurs de partager leur position et d'autres informations via le réseau maillé MeshCore, offrant ainsi une alternative aux systèmes de suivi traditionnels tels que APRS ou LoRa APRS.

## Companion
Le firmware MeshCore MCB modifié permet affiche un nouvel écran sur les companions MeshCore, permettant de configurer et activer le mode balise. Il est également possible de faire la configuration via la ligne série en USB ou Bluetooth. Pour l'instant le seul matériel supporté est le Seeedstudio Wio Tracker L1-Pro.

### Fonctionnalités
- Activation/désactivation
- Envoi uniquement si le GPS a fix
- Expiration automatique
- Intervalle configurable en temps ou en distance
- Intervalle minimum d'émission configurable
- Possibilité de configurer un message à envoyer avec la position
- Heartbeat: envoi forcé d'un message à intervalle régulier même si la position n'a pas changé
- Configuration du canal d'émission (par défaut `#beacon`)
- Configuration de la région de diffusion

### Téléchargement
- Firmware pour Wio Tracker L1-Pro
  - UF2: <a href="/mcb-firmware/meshcore-mcb_1.16.0-wio-tracker-l1-ble.uf2" download>Télécharger</a>
  - ZIP: <a href="/mcb-firmware/meshcore-mcb_1.16.0-wio-tracker-l1-ble.zip" download>Télécharger</a>

## Service MCB
Le service MCB est un serveur qui reçoit les informations des balises MeshCore grâce aux observers MeshCore sur MQTT. Il fait l'historisation et rend accessible les messages MCB. Une interface web est disponible pour visualiser les balises et leurs positions sur une carte.

Le service est actuellement disponible ici: [mcb.f4nlv.fr](https://mcb.f4nlv.fr).

## Standard
Le canal par défaut est `#beacon`.

Les messages sont en CSV avec le format suivant:
```csv
latitude,longitude,altitude,speed,course,message

exemple:
43.123456,6.123456,125.4,42.7,183.2,Vehicle12
```