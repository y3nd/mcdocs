<script setup>
import MeshCoreNameGenerator from '../components/name-gen.vue'
</script>

# Nommage des noeuds
## Compagnon
Pour un compagnon, nous recommandons:
- Code ISO 2 lettres pour le pays. FR en France
- 2 chiffres pour le département
- Tiret
- Prénom de l'utilisateur pour un compagnon
Exemple, le nœud compagnon de Paul habitant Le Pradet: `FR83-Paul-Mobile`.

## Répéteur
Pour un répéteur, nous recommandons :
- Code ISO 2 lettres pour le pays. FR en France
- 2 chiffres pour le département
- Nom de la commune ou du lieu
Exemple pour un nœud à Toulon sur le mont Faron : `FR83-Mont-Faron`

Vous pouvez aussi utiliser le générateur de nom de nœud MeshCore pour générer un nom de nœud conforme pour un répéteur.

<MeshCoreNameGenerator lang="fr" />