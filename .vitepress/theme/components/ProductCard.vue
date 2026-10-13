
<script setup lang="ts">
withDefaults(defineProps<{
  title: string
  image: string
  link: string
  description: string
  tag?: string
  linkText?: string
  datasheet?: string
  imageHeight?: number
}>(), {
  tag: 'MeshCore'
})
</script>

<template>
  <article class="product-card">
    <a :href="link" :style="{ height: imageHeight ? imageHeight + 'px' : 'auto' }" class="product-image">
      <img :src="image" :alt="title" loading="lazy" />
    </a>

    <div class="product-content">
      <span class="product-tag">{{ tag }}</span>

      <h3 class="product-title">
        <a :href="link">{{ title }}</a>
      </h3>

      <p class="product-description">
        {{ description }}
      </p>

      <div class="product-actions">
        <a :href="link" class="product-button">
          {{ linkText || 'Voir le produit' }} <span aria-hidden="true">→</span>
        </a>
        <a
          v-if="datasheet"
          :href="datasheet"
          class="product-button"
          target="_blank"
        >
          Fiche technique
        </a>
      </div>
    </div>
  </article>
</template>

<style scoped>
.product-card {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
  transition: transform .2s, border-color .2s;
}

.product-card:hover {
  transform: translateY(-3px);
  border-color: var(--vp-c-brand-1);
}

.product-image {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 300px;
  padding: 10px;
  background: var(--vp-c-bg);
}

.product-image img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.product-content {
  display: flex;
  flex: 1;
  flex-direction: column;
  padding: 20px;
}

.product-tag {
  color: var(--vp-c-brand-1);
  font-size: 12px;
  font-weight: 600;
}

.product-title {
  margin: 10px 0;
  padding: 0;
  border: none;
  font-size: 18px;
  line-height: 1.4;
}

.product-title a {
  color: var(--vp-c-text-1);
  text-decoration: none;
}

.product-description {
  flex: 1;
  margin: 0 0 20px;
  color: var(--vp-c-text-2);
  font-size: 14px;
  line-height: 1.6;
}

.product-actions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
}

.product-button {
  align-self: center;
  padding: 9px 40px;
  border-radius: 8px;
  background: var(--vp-c-brand-1);
  color: var(--vp-c-white);
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
}

.product-button:hover {
  background: var(--vp-c-brand-2);
  color: var(--vp-c-white);
}
</style>
