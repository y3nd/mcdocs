<script setup>
import MeshCoreRegionBuilder from "../components/mc-region-builder.vue";
</script>

# Configuration des répéteurs
Depuis la console ou l'interface de configuration MeshCore du répéteur, appliquez les lignes de commande suivantes.

```bash
set advert.interval 240
set flood.advert.interval 24
set flood.max.advert 6
set flood.max.unscoped 5
set multi.acks 1
set path.hash.mode 1
set loop.detect minimal
set dutycycle 10
set agc.reset.interval 4
set cad on
set repeat on
region def eu fr
region default fr
region home fr
region save
reboot
clock sync
```

- advert.interval `240` : annonces zero-hop toutes les deux heures pour que la liste des voisins soit à jour.
- flood.advert.interval `24` : garde une découverte de réseau régulière sans surcharger le canal.
- flood.max.advert `6` : Limite le nombre de sauts à 6 pour les annonces d'inondation.
- flood.max.unscoped `5` : limite les messages sans région à un maximum de 5 sauts.
- multi.acks `1` : active les accusés de réception multiples pour plus de fiabilité.
- path.hash.mode `1` : active le mode 2 octets pour les adresses.
- loop.detect `minimal` : indique que l'on bloque les trames qui ont 4 fois le même ID.
- dutycycle `10` : respect de la réglementation européenne sur le duty-cycle.
- agc.reset.interval `4` : réinitialise périodiquement le contrôle de gain automatique - très utile en milieu perturbé.
- set cad `on` : La radio effectue une analyse de l'activité du canal avant la
transmission et la reporte si le canal est occupé.
- repeat `on` : indique que ce nœud est bien un répéteur du réseau.
- guest.password `''` : ne pas mettre de mot de passe « guest » pour donner accès public à la télémétrie.
- region default fr : région par défaut pour la France.
- region save : sauvegarde la configuration des régions.
- reboot
*Attendre que le répéteur redémarre*
- clock sync : synchronisation de l'horloge avec le téléphone. Peut être nécessaire régulièrement.

:::info
- Ne pas mettre de mot de passe "guest" pour donner accès public à la télémétrie. La position n'est pas partagée dans la télémétrie.
- Positionner le répéteur en hauteur (toit, colline, pylône) et le laisser alimenté en continu
- Installer une antenne performante, accordée à la bonne fréquence avec un filtre de qualité si besoin.
:::

## Voir aussi
- [Configuration d'un répéteur Sensecap Solar P1](../sensecap-solar-p1/configuration.md)
- [Nommage des nœuds](../meshcore/nommage-noeuds.md) — Conventions et générateur de noms pour les compagnons et les répéteurs.


<MeshCoreRegionBuilder />