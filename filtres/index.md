---
next:
  link: /filtres/saw-868-f4nlv
  text: Filtre SAW 868 MHz F4NLV
---

# Filtres pour MeshCore
La puce utilisée par la quasi-totalité des modules compatibles avec MeshCore, la Semtech SX1262, possède une bande passante en réception très large, de 150 à 960 MHz. Cette bande très large permet une grande flexibilité, mais elle peut aussi être source de perturbations et de bruits.

Pour améliorer la qualité de réception et réduire les interférences, il est possible d'insérer un filtre dans le circuit d'antenne. Un filtre est un composant électronique qui permet de laisser passer certaines fréquences tout en bloquant d'autres. Dans le cas de MeshCore, l'utilisation d'un filtre adapté peut aider à éliminer les signaux indésirables et à améliorer la performance globale du module.

## Source d'interférences
En France, la principale source d'interférences pour MeshCore est la téléphonie mobile (cellulaire) dans les bandes 700 MHz, 800 MHz et 900 MHz.

Il est possible de consulter la proximité des antennes de téléphonie mobile en France sur le site Cartoradio : [https://www.cartoradio.fr/](https://www.cartoradio.fr/)


## Types de filtres
### Filtre à cavités
Un filtre à cavités est un type de filtre qui utilise des résonateurs en forme de cavité pour sélectionner les fréquences souhaitées. Ces filtres sont très efficaces pour éliminer les signaux indésirables et sont souvent utilisés dans les applications RF où la performance est critique. Le principal avantage des filtres à cavités est leur capacité à offrir une faible perte d'insertion et une puissance maximale élevée. Cependant, ils sont plus coûteux et encombrants que d'autres types de filtres.

### Filtre piezoélectrique ou SAW
Un filtre piezoélectrique, également connu sous le nom de filtre SAW (Surface Acoustic Wave), utilise des ondes acoustiques pour filtrer les signaux. Ces filtres sont très compacts et offrent une bonne sélectivité, ce qui les rend adaptés aux applications où l'espace est limité.

Les filtres SAW sont souvent utilisés dans les télécommunications et les dispositifs mobiles en raison de leur taille réduite et de leur faible coût. Cependant, ils ont une perte d'insertion généralement plus élevée que les filtres à cavités et ont une puissance maximale bien moins élevée.

Les filtres SAW sont particulièrement adaptés pour MeshCore, car alignés avec les coûts et l'encombrement des modules.

<div class="products-grid">

<ProductCard
  title="Filtre SAW 868 MHz F4NLV"
  image="/assets/img/filtre-868-f4nlv-ufl.avif"
  link="/filtres/saw-868-f4nlv"
  tag="MeshCore · Filtre SAW · 868 MHz"
  description="Ce filtre est conçu pour la bande 868 MHz utilisée par MeshCore. Il offre une bonne sélectivité et une faible perte d'insertion, pour améliorer les performances de votre nœud MeshCore à prix et encombrement limités. De plus, il accepte une puissance maximale de 27 dBm, plus élevée que la plupart des autres filtres SAW."
/>

</div>