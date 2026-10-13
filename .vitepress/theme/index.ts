import DefaultTheme from 'vitepress/theme'
import ProductCard from './components/ProductCard.vue'
import Layout from './Layout.vue'
import type { Theme } from 'vitepress'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout,
  enhanceApp({ app }) {
    app.component('ProductCard', ProductCard)
  }
} satisfies Theme
