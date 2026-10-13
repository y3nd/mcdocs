
<template>
  <button class="pdf-button" @click="window.print()">
    Print
  </button>
</template>

<script setup>
const window = globalThis.window
</script>
