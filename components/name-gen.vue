<script setup>
import { computed, ref } from "vue";

const departement = ref("");
const placeName = ref("");

const props = defineProps({
  lang: {
    type: String,
    default: "en",
  },
});

const messages = {
  en: {
    title: "Generate MeshCore repeater name",
    departementLabel: "Département number",
    departementPlaceholder: "Example: 75",
    placeLabel: "Place name",
    placePlaceholder: "Example: Montmartre",
    resultLabel: "Generated name",
    copy: "Copy",
    copied: "Copied!",
    departementRequired: "Please enter a département number.",
    placeRequired: "Please enter a place name.",
  },
  fr: {
    title: "Générer un nom de répéteur MeshCore",
    departementLabel: "Numéro de département",
    departementPlaceholder: "Exemple : 75",
    placeLabel: "Nom du lieu",
    placePlaceholder: "Exemple : Montmartre",
    resultLabel: "Nom généré",
    copy: "Copier",
    copied: "Copié !",
    departementRequired: "Veuillez saisir un numéro de département.",
    placeRequired: "Veuillez saisir un nom de lieu.",
  },
};

const t = computed(() => messages[props.lang] ?? messages.en);

const copied = ref(false);

const normalizedDepartement = computed(() =>
  departement.value
    .trim()
    .toUpperCase()
    .replace(/[^0-9AB]/gi, "")
    .padStart(2, "0")
    .slice(0, 3),
);

// Trim normalized place to 10 characters to avoid generating names that are too long
const normalizedPlace = computed(() => placeName.value.trim().substring(0, 10));

const error = computed(() => {
  if (!departement.value.trim()) {
    return t.value.departementRequired;
  }

  if (!placeName.value.trim()) {
    return t.value.placeRequired;
  }

  return "";
});

const generatedName = computed(() => {
  if (error.value) {
    return "";
  }

  return `FR${normalizedDepartement.value}-${normalizedPlace.value}`;
});

async function copyGeneratedName() {
  if (!generatedName.value) {
    return;
  }

  await navigator.clipboard.writeText(generatedName.value);
  copied.value = true;

  window.setTimeout(() => {
    copied.value = false;
  }, 1500);
}
</script>

<template>
  <div class="meshcore-name-generator">
    <p class="meshcore-name-generator__title">
      {{ t.title }}
    </p>

    <div class="meshcore-name-generator__fields">
      <label class="meshcore-name-generator__field" for="departement-input">
        <span class="meshcore-name-generator__label">
          {{ t.departementLabel }}
        </span>

        <input
          id="departement-input"
          v-model="departement"
          class="meshcore-name-generator__input"
          type="text"
          inputmode="text"
          :placeholder="t.departementPlaceholder"
        >
      </label>

      <label class="meshcore-name-generator__field" for="place-input">
        <span class="meshcore-name-generator__label">
          {{ t.placeLabel }}
        </span>

        <input
          id="place-input"
          v-model="placeName"
          class="meshcore-name-generator__input"
          type="text"
          :placeholder="t.placePlaceholder"
        >
      </label>
    </div>

    <p
      v-if="error"
      class="meshcore-name-generator__message meshcore-name-generator__message--errored"
    >
      {{ error }}
    </p>

    <div
      v-else
      class="meshcore-name-generator__result"
    >
      <span class="meshcore-name-generator__result-label">
        {{ t.resultLabel }}
      </span>

      <code class="meshcore-name-generator__code">
        {{ generatedName }}
      </code>

      <button
        class="meshcore-name-generator__button"
        type="button"
        @click="copyGeneratedName"
      >
        {{ copied ? t.copied : t.copy }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.meshcore-name-generator {
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 1rem;
  background: var(--vp-c-bg-soft);
}

.meshcore-name-generator__title {
  margin: 0 0 1rem;
  font-weight: 600;
}

.meshcore-name-generator__fields {
  display: grid;
  gap: 0.85rem;
}

.meshcore-name-generator__field {
  display: block;
}

.meshcore-name-generator__label {
  display: block;
  margin-bottom: 0.35rem;
  font-weight: 600;
}

.meshcore-name-generator__input {
  width: 100%;
  box-sizing: border-box;
  padding: 0.7rem 0.85rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-family: inherit;
}

.meshcore-name-generator__result {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.meshcore-name-generator__result-label {
  font-weight: 600;
}

.meshcore-name-generator__code {
  padding: 0.35rem 0.55rem;
  border-radius: 8px;
  background: var(--vp-code-bg);
  color: var(--vp-code-color);
  font-size: 1rem;
}

.meshcore-name-generator__button {
  padding: 0.55rem 0.85rem;
  border: 0;
  border-radius: 10px;
  background: var(--vp-c-brand-1);
  color: white;
  cursor: pointer;
  font-weight: 600;
}

.meshcore-name-generator__message {
  margin: 0.85rem 0 0;
}

.meshcore-name-generator__message--errored {
  color: #6b7280;
}

@media (max-width: 640px) {
  .meshcore-name-generator__result {
    align-items: stretch;
    flex-direction: column;
  }

  .meshcore-name-generator__button {
    width: 100%;
  }
}
</style>