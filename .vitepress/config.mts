import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "meshcore.f4nlv.fr",
  description: "Documentation",
  //head: [['link', { rel: 'icon', href: '/logo.svg' }]],
  lastUpdated: true,
  lang: 'fr-FR',
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      //{ text: 'Main website', link: '' },
    ],
    docFooter: {
      prev: 'Page précédente',
      next: 'Page suivante',
    },
    outline: {
      label: 'Sur cette page',
    },
    darkModeSwitchLabel: 'Apparence',
    lightModeSwitchTitle: 'Passer au thème clair',
    darkModeSwitchTitle: 'Passer au thème sombre',
    sidebarMenuLabel: 'Menu',
    returnToTopLabel: 'Retour en haut',
    langMenuLabel: 'Changer de langue',
    skipToContentLabel: 'Aller au contenu',
    lastUpdated: {
      text: 'Dernière mise à jour',
    },
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: 'Rechercher',
            buttonAriaLabel: 'Rechercher',
          },
          modal: {
            displayDetails: 'Afficher la liste détaillée',
            resetButtonTitle: 'Réinitialiser la recherche',
            backButtonTitle: 'Fermer la recherche',
            noResultsText: 'Aucun résultat pour',
            footer: {
              selectText: 'pour sélectionner',
              selectKeyAriaLabel: 'entrée',
              navigateText: 'pour naviguer',
              navigateUpKeyAriaLabel: 'flèche vers le haut',
              navigateDownKeyAriaLabel: 'flèche vers le bas',
              closeText: 'pour fermer',
              closeKeyAriaLabel: 'échap',
            },
          },
        },
      },
    },
    //logo: '/logo.svg',
    sidebar: [
      {
        text: 'MESHCORE',
        items: [
          { text: 'Paramètres radio', link: '/meshcore/parametres-radio' },
          { text: 'Nommage des noeuds', link: '/meshcore/nommage-noeuds' },
          { text: 'Configuration des Compagnons', link: '/meshcore/configuration-companion' },
          { text: 'Configuration des répéteurs', link: '/meshcore/configuration-repeteur' },
          { text: 'Association Canaux-Régions', link: '/meshcore/canaux-et-regions' },
        ]
      },
      {
        text: 'Sensecap Solar P1',
        link: '/sensecap-solar-p1',
        items: [
          { text: 'Liens d\'achat', link: '/sensecap-solar-p1/achats' },
          { text: 'Préparation matérielle', link: '/sensecap-solar-p1/preparation-materielle' },
          { text: 'Flash bootloader', link: '/sensecap-solar-p1/flash-bootloader' },
          { text: 'Flash MeshCore', link: '/sensecap-solar-p1/flash-meshcore' },
          { text: 'Configuration', link: '/sensecap-solar-p1/configuration' },
          { text: 'Placement', link: '/sensecap-solar-p1/placement' },
          { text: 'Validation', link: '/sensecap-solar-p1/validation' },
          { text: 'GPS', link: '/sensecap-solar-p1/gps' },
          { text: 'Maintenance', link: '/sensecap-solar-p1/maintenance' },
        ]
      },
      {
        text: 'Liens utiles',
        link: '/liens-utiles',
      },
      {
        text: 'Outils',
        // link: '/outils',
        items: [
          { text: 'Inverseur de chemin', link: '/outils/inverseur-de-chemin' },
        ]
      },
    ],
    socialLinks: [
    ],
    footer: {
    },
  },
  locales: {
    root: {
      label: 'Français',
      lang: 'fr-FR',
    },
  },
})
