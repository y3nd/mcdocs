# Canaux et régions
L'association "canaux-regions" sur votre nœud compagnon permettra de filtrer les répéteurs qui relayeront ou non votre message. Cela permet d'éviter que votre message soit relayé par des répéteurs qui ne sont pas dans votre zone géographique. Cela permet également de limiter la propagation des messages à une zone géographique spécifique.
:::info
- Dans le département du Var, votre canal `#var` doit être restreint à la région `fr-83`.
- Lorsqu'un message est émis sur ce canal, il est retransmis de répéteur en répéteur, à condition que la région `fr-83` soit listée dans leur configuration.
- Le premier répéteur du département voisin qui aura par exemple comme régions `eu` + `fr` + `fr-pac` + `fr-13` recevra le message, mais comme fr-83 n'est pas dans sa liste, il ne relaiera pas votre message.
- Si jamais le message rencontre un répéteur qui n'a pas de régions explicitement définies (c'est-à-dire qu'il a juste `*` de défini), alors le message ne sera pas répété.
:::

## Ajouter les régions
Ouvrez un canal, rendez-vous sur les 3 points en haut à droite et cliquez sur *Définir le périmètre de la région*, puis à nouveau sur les 3 points en haut à droite *Découvrir les régions*. Ajoutez les régions qui s'affichent.

## Liste des canaux et des régions
### Canaux Généraux

| Canal      | Région associée |
| ---------- | --------------- |
| Public     | eu              |
| #fr        | fr              |
| #emergency | fr-pac          |
| #info      | fr-pac          |
| #meteo     | fr-pac          |
| #test      | fr-pac          |

### Canal Région PACA

| Canal | Région associée |
| ----- | ------ |
| #paca | fr-pac |

### Canal Départemental du Var

| Canal | Région associée |
| ----- | ------ |
| #var  | fr-83         |

### Canal de la ville de Toulon
| Canal | Région associée |
| ----- | ------ |
| #toulon | fr-83 |
