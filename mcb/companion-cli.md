# MCB : interface en ligne de commande du compagnon MeshCore Beacon

La fonctionnalité de balise MCB peut être configurée depuis l'écran OLED du Wio
Tracker L1 Pro ou depuis la console texte USB physique du firmware compagnon.
Les paramètres et les régions personnalisées sont conservés et partagés entre
les deux interfaces.

## Ouverture de la console

Vous pouvez utiliser l'outil [WebTerm](https://webterm.y3n.co/)

### Firmware compagnon BLE

La console texte USB physique reste disponible en permanence tandis que le
protocole compagnon avec trames continue de fonctionner via BLE :

1. Connectez le Wio Tracker L1 Pro en USB.
2. Ouvrez son port série USB à 115 200 bauds.
3. Exécutez `beacon help` pour afficher le résumé des commandes.

Toutes les commandes de la console texte restent disponibles, y compris les
commandes du système de fichiers et de récupération telles que `erase`,
`rebuild`, `ls`, `cat`, `rm` et `reboot`.

### Firmware compagnon USB

Le port série USB transporte normalement le protocole compagnon MeshCore avec
trames. La console texte reste donc un mode de secours exclusif :

1. Redémarrez le Wio Tracker L1 Pro.
2. Pendant les huit premières secondes suivant le démarrage, maintenez enfoncé
   le bouton Entrée du joystick.
3. Ouvrez la console série de l'appareil à 115 200 bauds.
4. Exécutez `beacon help` pour afficher le résumé des commandes.

## Commandes de session

Affichez la configuration actuelle de la balise et l'état de la session :

```text
get beacon
```

La commande abrégée `beacon` affiche les mêmes informations.

Démarrez ou arrêtez une session de balise :

```text
beacon start
beacon stop
```

L'état affiché comprend :

- l'activation ou non de la session ;
- l'état actuel de la session ;
- le temps restant avant expiration, en minutes ;
- le mode d'intervalle et les intervalles configurés ;
- le canal et la région sélectionnés ;
- les paramètres d'expiration, du buzzer et du message personnalisé.

## Paramètres de la balise

### Mode d'intervalle

Sélectionnez un fonctionnement basé sur le temps ou sur la distance :

```text
set beacon mode time
set beacon mode distance
```

### Intervalle de temps

Définissez l'intervalle de transmission basé sur le temps, en secondes. Les
valeurs valides vont de 10 à 86 400 secondes.

```text
set beacon interval 300
```

### Intervalle de distance

Définissez l'intervalle de transmission basé sur la distance, en mètres. Les
valeurs valides vont de 10 à 10 000 mètres.

```text
set beacon distance 100
```

### Intervalle minimal

Définissez le délai minimal autorisé entre deux transmissions de la balise. La
valeur est exprimée en secondes et vaut 60 secondes par défaut. Les valeurs
valides vont de 10 à 86 400 secondes.

```text
set beacon min_interval 60
```

La première balise d'une session est envoyée immédiatement après l'obtention
d'une position GPS valide. Les transmissions suivantes déclenchées par le
temps, la distance ou le signal de présence attendent que l'intervalle minimal
se soit écoulé. Cela évite des transmissions rapprochées lorsque le seuil de
distance est franchi plusieurs fois.

### Intervalle du signal de présence

Définissez l'intervalle du signal de présence à l'arrêt, en secondes. Ce
paramètre est utilisé uniquement en mode distance. Les valeurs valides vont de
60 à 86 400 secondes.

```text
set beacon heartbeat 1800
```

### Expiration

Définissez la durée de vie de la session, en secondes. Les valeurs valides vont
de 300 à 86 400 secondes.

```text
set beacon expiration 3600
```

### Canal

Sélectionnez un canal configuré par son nom ou son index numérique :

```text
set beacon channel #beacon
set beacon channel 1
```

Le firmware crée automatiquement le canal de hashtag `#beacon` s'il n'existe
pas encore.

### Région

Sélectionnez une région enregistrée par son nom ou son index numérique :

```text
set beacon region france
set beacon region 0
```

Deux choix intégrés sont toujours disponibles :

```text
set beacon region default
set beacon region unscoped
```

`default` utilise la portée de diffusion par défaut configurée sur l'appareil
compagnon. `unscoped` effectue l'envoi sans portée de transport régionale.

### Message personnalisé

Définissez le texte personnalisé ajouté à chaque balise :

```text
set beacon message Vehicle 12
```

Effacez le message personnalisé :

```text
set beacon message
```

Le message personnalisé peut contenir jusqu'à 31 caractères.

### Bip de transmission

Activez ou désactivez le signal sonore indiquant la réussite des transmissions
de la balise :

```text
set beacon beep on
set beacon beep off
```

Le paramètre global de mise en sourdine du buzzer de l'appareil reste
prioritaire.

## Gestion des régions

Vous pouvez enregistrer jusqu'à huit régions personnalisées. Elles sont
conservées et apparaissent dans le sélecteur de région de l'écran OLED.

Affichez toutes les régions :

```text
beacon regions
```

La région sélectionnée est signalée par `*`. La liste affiche également la clé
de transport associée à chaque région personnalisée.

### Ajout Région

Ajoutez une région :

```text
beacon region add fr-83
```

### Suppression d'une région

Supprimez une région par son nom ou son index numérique :

```text
beacon region remove fr-83
beacon region remove 0
```

Si la région sélectionnée est supprimée, le paramètre de la balise revient à la
région par défaut de l'appareil.

## Exemple complet

Les commandes suivantes configurent une balise de véhicule basée sur la
distance :

```text
beacon region add fr-83
set beacon mode distance
set beacon distance 100
set beacon min_interval 60
set beacon heartbeat 1800
set beacon expiration 3600
set beacon channel #beacon
set beacon region fr-83
set beacon message Vehicle 12
set beacon beep on
beacon start
get beacon
```

## Format des messages de balise

Les messages de balise utilisent le préfixe habituel du nom d'affichage des
messages texte de groupe, suivi d'un enregistrement CSV comportant exactement
six colonnes :

```text
display-name: latitude,longitude,altitude,speed,course,message
```

Exemple :

```text
Rover 1: 43.123456,6.123456,125.4,42.7,183.2,Vehicle12
```

Les colonnes sont les suivantes :

1. Latitude en degrés décimaux avec six décimales.
2. Longitude en degrés décimaux avec six décimales.
3. Altitude en mètres avec une décimale.
4. Vitesse en kilomètres par heure avec une décimale.
5. Cap en degrés avec une décimale.
6. Message personnalisé configuré.

Après le préfixe habituel `display-name: ` des messages texte de groupe, les
cinq premières colonnes CSV ne contiennent ni nom de champ, ni unité, ni espace.
Les espaces de la colonne du message personnalisé sont conservés. Le firmware
remplace les virgules du message personnalisé par des tirets bas afin qu'il
reste dans une seule colonne CSV. Lorsqu'aucun message personnalisé n'est
configuré, la sixième colonne est vide et l'enregistrement se termine par une
virgule.
