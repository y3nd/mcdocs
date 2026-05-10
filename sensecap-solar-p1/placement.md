---
next:
  link: /sensecap-solar-p1/configuration
  text: Configuration
previous:
  link: /sensecap-solar-p1/validation
  text: Validation du répéteur
---

# Placement sur le terrain
Afin de créer un répéteur utile, il est recommandé d'étudier son placement en amont.

## Etude préalable
L'application MeshCore contient 2 outils très utiles pour étudier le placement de votre répéteur :
- La simulation de couverture : elle permet de visualiser la couverture théorique d'un répéteur placé à un endroit donné. Elle prend en compte les obstacles et la topographie du terrain pour estimer la portée du signal.
- Le calcul de ligne de vue : il permet de vérifier si un répéteur placé à un endroit donné peut voir un autre nœud ou des positions spécifiques sur la carte. Cela permet de s'assurer que le répéteur pourra communiquer avec les autres nœuds du réseau, companions ou répéteurs.

## Critères de placement
Le placement doit répondre le plus possible à ces conditions :
- Ne pas se situer en pleine nature sans autorisation et en particulier dans une zone classée Natura 2000 ou Parc National
- Dans le cadre de l'intégration à un réseau maillé existant, le répéteur doit voir au moins 2 noeuds avec un signal correct (>=2db) et couvrir une zone actuellement faiblement couverte.
- Éviter obstacles métalliques et végétaux
- Éviter les zones à fort passage de personnes pour limiter les risques de vol ou de vandalisme
- Privilégier les endroits en hauteur pour maximiser la portée du répéteur
- Ne pas se situer à proximité directe d'autres équipements RF qui pourraient créer des interférences (antennes TNT, relais cellulaires, radars etc..)
- Se fixer sur un mât, tronc ou mur solide et résistant au vent

:::warning
Le placement d'un répéteur en pleine nature sans autorisation est risqué et peut entraîner des sanctions et vols/vandalisme. Il est important de respecter les réglementations locales et de demander les autorisations nécessaires avant d'installer un répéteur dans une zone naturelle.
**Il est recommandé de réaliser une convention écrite avec l'organisme hébergeant l'équipement afin de pérenniser l'installation.**
:::

## Fixation
Le SenseCAP Solar P1 est conçu pour être fixé sur un poteau ou un tronc d'arbre à l'aide de ses fixations intégrées. Il est important de s'assurer que le support choisi est solide et résistant au vent pour éviter que le répéteur ne soit endommagé ou ne tombe.

La bride permettant de fixer sur un support rond est fournie avec le répéteur. Pour les supports rectangulaires, elle peut être omise.

[Voir Préparation matérielle pour plus d'informations](/sensecap-solar-p1/preparation-materielle)

## Orientation
La mât de support doit se situer sous l'antenne, ou alors l'antenne doit être orientée de manière à éviter que le mât ne vienne faire obstacle au signal. Il est recommandé de faire des tests d'orientation pour trouver la position optimale. Cette orientation peut être définie en fonction de la zone à couvrir et des répéteurs à voir.

:::info
Le répéteur Sensecap Solar P1 consomme très peu et dispose d'une très grande autonomie. Il n'est donc pas systématiquement nécessaire de l'orienter plein sud pour maximiser la production d'énergie. Il est recommandé de privilégier une orientation qui maximise la couverture du réseau maillé plutôt que la production d'énergie. Dans le cas d'un placement plein sud et avec une visibilité dégagée, il est possible de retirer certaines cellules Lithium.
:::

:::warning
Bien vérifier l'absence de poussière, puis refermer correctement le port USB-C du boitier pour éviter les infiltrations d'eau et d'humidité qui peuvent endommager le répéteur.
:::