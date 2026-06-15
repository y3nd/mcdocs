---
next:
  link: /sensecap-solar-p1/placement
  text: Placement sur le terrain
previous:
  link: /sensecap-solar-p1/flash-meshcore
  text: Flash MeshCore
---

<script setup>
import MeshCoreNameGenerator from '../components/name-gen.vue'
import MeshCoreRegionBuilder from "../components/mc-region-builder.vue";
</script>

# Configuration
Après avoir flashé le bootloader et le firmware MeshCore, il est temps de configurer votre répéteur pour qu'il puisse rejoindre votre réseau maillé.

Voici un guide simplifié issu du [Guide Gaulix](https://gaulix.fr/docs-parametrage/regles-de-nommage-meshcore/)

La configuration de base du répéteur peut être effectuée à l'aide du [Configurateur de répéteur MeshCore](https://config.meshcore.io/) en USB. Ce configurateur permet de configurer les paramètres essentiels tels que le nom du nœud et les paramètres radios et de réseau.

Elle peut également se faire via la console d'administration en se connectant au répéteur via un companion lorsqu'un mot de passe administrateurest défini.

## Nom du répéteur
Utilisez cet outil pour générer un nom de répéteur conforme.

<MeshCoreNameGenerator lang="fr" />

## Mot de passe administrateur du répéteur
Générez un mot de passe avec un générateur de mot de passe aléatoire et complexe.

## Position
Sélectionner la position de votre répéteur sur la carte. Celle-ci peut être différente de la position exacte du répéteur, mais il est recommandé de la placer au plus proche de sa position réelle.

## Contact
Indiquer dans les informations de contact un moyen de contacter le propriétaire du répéteur en cas de problème ou de besoin d'assistance. Cela peut être un identifiant MeshCore, une adresse e-mail, un numéro de téléphone ou un lien vers un site web.

## Paramètres radios et de réseau
Le plus simple est d'utiliser la console pour insérer les paramètres suivants :
```bash
set advert.interval 120
set flood.advert.interval 24
set agc.reset.interval 4
set multi.acks 1
set dutycycle 10
set path.hash.mode 1
set loop.detect minimal
set repeat on
set guest.password ''
```
*Paramètres issus de [meshcore.fr](https://www.meshcore.fr/)*

## Régions
Les régions permettent de limiter la propagation des messages à une zone géographique spécifique. Les régions sont ensuite définies dans chaque canal pour limiter la portée des messages à cette zone. Les régions sont définies par des codes spécifiques qui correspondent **uniquement** à des zones géographiques, pas des thèmes ou sujets.

Les paramètres de régions sont spécifiques à l'endroit où va être placé le répéteur. Les régions à mettre en **France** sont
```bash
europe
fr
```

Ensuite les régions sont spécifiques au département et sa région administrative. Exemple ici pour le **Var**

**Régions pour le département du Var (83)**
```bash
fr-83
fr-pac
```

:::info
Un cas spécial est à noter pour les répéteurs de frontière entre 2 départements. Ces répéteurs peuvent être utiles pour les 2 départements à la fois et donc peuvent intégrer les régions des 2 départements. À noter que cela doit être fait **__uniquement__** si le répéteur est utile au routage au sein de chacun ces 2 départements. L'objectif ici n'est pas de faire le pont entre 2 départements.
:::

<MeshCoreRegionBuilder />

## Sauvegarde de la configuration
Il est vivement recommandé de sauvegarder la configuration du répéteur contenant sa clé privée afin de pouvoir restaurer la configuration en cas de réinitialisation du répéteur ou de remplacement du matériel. La sauvegarde peut être effectuée à l'aide du configurateur USB.