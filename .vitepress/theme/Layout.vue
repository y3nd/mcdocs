
<script setup>
import DefaultTheme from 'vitepress/theme'
import PrintPdfButton from './PrintPdfButton.vue'

const { Layout } = DefaultTheme
</script>

<template>
  <Layout>
    <template #doc-footer-before>
      <div class="pdf-actions">
        <PrintPdfButton />
      </div>
    </template>
  </Layout>
</template>
