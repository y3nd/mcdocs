<script setup>
import MeshCoreNameGenerator from '../components/name-gen.vue'
</script>

# Nommage des noeuds
Pour un compagnon, nous recommandons:
- 2 chiffres pour le département
- 4 premières lettres pour la ville
- Ensuite, ce que vous voulez
Exemple, le nœud compagnon de Paul habitant Le Pradet: `83LPRA-Paul-Mobile`.
Pour un répéteur, nous recommandons :
- 2 chiffres pour le département
- 4 premières lettres pour la ville
- Nom du lieu espacé par un -
Exemple pour un nœud à Toulon sur le mont Faron : `83TOUL-Mont-Faron`

Vous pouvez aussi utiliser le générateur de nom de nœud MeshCore pour générer un nom de nœud conforme.

<MeshCoreNameGenerator lang="fr" />