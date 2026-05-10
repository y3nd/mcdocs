<script setup>
import { computed, ref, watch } from "vue";

const props = defineProps({
  lang: {
    type: String,
    default: "en",
  },
});

const pathInput = ref("");
const invertedPath = ref("");
const detectedIdentifierSize = ref(null);
const repeaterCount = ref(0);
const error = ref("");
const copied = ref(false);

const maxRepeatersByIdentifierSize = {
  1: 64,
  2: 32,
  3: 21,
};

const messages = {
  en: {
    title: "MeshCore path inverter",
    label: "Path to invert",
    placeholder: "aa,bb,cc or aaaa,bbbb,cccc",
    invert: "Invert path",
    clear: "Clear",
    copy: "Copy",
    copied: "Copied",
    outputLabel: "Inverted path",
    help: "Enter a comma-separated MeshCore path. Spaces and case differences are normalized. Leading or trailing commas are ignored, but missing entries in the middle are rejected.",
    stats: ({ count, bytes, max }) =>
      `${count} repeater${count > 1 ? "s" : ""}, detected as ${bytes}-byte identifier${bytes > 1 ? "s" : ""} (limit ${max}).`,
    pathRequired: "Please enter a MeshCore path.",
    invalidCharacter: ({ char }) =>
      `Invalid character "${char}". Use hexadecimal digits, commas, and spaces only.`,
    missingData: "The path contains missing data. Remove empty entries between commas, such as in aa,,bb.",
    invalidTokenSize: ({ token }) =>
      `Identifier "${token}" has ${token.length} hex character${token.length > 1 ? "s" : ""}; each identifier must be 2, 4, or 6 hex characters.`,
    inconsistentIdentifierSize: ({ expected, actual, token }) =>
      `Identifier "${token}" has ${actual} hex character${actual > 1 ? "s" : ""}, but this path uses ${expected}-character identifiers. All identifiers must use the same size.`,
    tooManyRepeaters: ({ count, max, bytes }) =>
      `${count} repeaters is too many for ${bytes}-byte paths. The limit is ${max}.`,
    noIdentifiers: "No repeater identifiers were found.",
    clipboardError: "Could not copy the result to the clipboard.",
  },
  fr: {
    title: "Inverseur de chemin MeshCore",
    label: "Chemin à inverser",
    placeholder: "aa,bb,cc ou aaaa,bbbb,cccc",
    invert: "Inverser le chemin",
    clear: "Effacer",
    copy: "Copier",
    copied: "Copié",
    outputLabel: "Chemin inversé",
    help: "Saisissez un chemin MeshCore séparé par des virgules. Les espaces et la casse sont normalisés. Les virgules au début ou à la fin sont ignorées, mais les entrées manquantes au milieu sont refusées.",
    stats: ({ count, bytes, max }) =>
      `${count} répéteur${count > 1 ? "s" : ""}, détecté avec des identifiants de ${bytes} octet${bytes > 1 ? "s" : ""} (limite ${max}).`,
    pathRequired: "Veuillez saisir un chemin MeshCore.",
    invalidCharacter: ({ char }) =>
      `Caractère invalide "${char}". Utilisez uniquement des chiffres hexadécimaux, des virgules et des espaces.`,
    missingData: "Le chemin contient une donnée manquante. Supprimez les entrées vides entre deux virgules, par exemple dans aa,,bb.",
    invalidTokenSize: ({ token }) =>
      `L'identifiant "${token}" contient ${token.length} caractère${token.length > 1 ? "s" : ""} ${token.length > 1 ? "hexadécimaux" : "hexadécimal"} ; chaque identifiant doit contenir 2, 4 ou 6 caractères hexadécimaux.`,
    inconsistentIdentifierSize: ({ expected, actual, token }) =>
      `L'identifiant "${token}" contient ${actual} caractère${actual > 1 ? "s" : ""} ${actual > 1 ? "hexadécimaux" : "hexadécimal"}, mais ce chemin utilise des identifiants de ${expected} caractères. Tous les identifiants doivent avoir la même taille.`,
    tooManyRepeaters: ({ count, max, bytes }) =>
      `${count} répéteurs est trop élevé pour les chemins de ${bytes} octet${bytes > 1 ? "s" : ""}. La limite est ${max}.`,
    noIdentifiers: "Aucun identifiant répéteur n'a été trouvé.",
    clipboardError: "Impossible de copier le résultat dans le presse-papiers.",
  },
};

const t = computed(() => messages[props.lang] ?? messages.en);
const resultStats = computed(() => {
  if (!invertedPath.value || !detectedIdentifierSize.value) {
    return "";
  }

  return t.value.stats({
    count: repeaterCount.value,
    bytes: detectedIdentifierSize.value,
    max: maxRepeatersByIdentifierSize[detectedIdentifierSize.value],
  });
});

watch(pathInput, () => {
  invertedPath.value = "";
  detectedIdentifierSize.value = null;
  repeaterCount.value = 0;
  error.value = "";
  copied.value = false;
});

function removeWhitespace(value) {
  return Array.from(value)
    .filter((char) => char.trim() !== "")
    .join("");
}

function parsePath(rawPath) {
  const withoutSpaces = removeWhitespace(rawPath);

  if (!withoutSpaces) {
    return { error: t.value.pathRequired };
  }

  const invalidCharacter = withoutSpaces.match(/[^0-9a-fA-F,]/);

  if (invalidCharacter) {
    return {
      error: t.value.invalidCharacter({ char: invalidCharacter[0] }),
    };
  }

  const normalized = withoutSpaces.toLowerCase();
  const trimmedCommas = normalized.replace(/^,+|,+$/g, "");

  if (!trimmedCommas) {
    return { error: t.value.noIdentifiers };
  }

  if (trimmedCommas.includes(",,")) {
    return { error: t.value.missingData };
  }

  const identifiers = trimmedCommas.split(",");
  const expectedLength = identifiers[0].length;

  if (![2, 4, 6].includes(expectedLength)) {
    return {
      error: t.value.invalidTokenSize({ token: identifiers[0] }),
    };
  }

  const invalidIdentifier = identifiers.find(
    (identifier) => !/^[0-9a-f]+$/.test(identifier),
  );

  if (invalidIdentifier) {
    return {
      error: t.value.invalidCharacter({ char: invalidIdentifier }),
    };
  }

  const inconsistentIdentifier = identifiers.find(
    (identifier) => identifier.length !== expectedLength,
  );

  if (inconsistentIdentifier) {
    return {
      error: t.value.inconsistentIdentifierSize({
        expected: expectedLength,
        actual: inconsistentIdentifier.length,
        token: inconsistentIdentifier,
      }),
    };
  }

  const bytesPerIdentifier = expectedLength / 2;
  const max = maxRepeatersByIdentifierSize[bytesPerIdentifier];

  if (identifiers.length > max) {
    return {
      error: t.value.tooManyRepeaters({
        count: identifiers.length,
        max,
        bytes: bytesPerIdentifier,
      }),
    };
  }

  return {
    identifiers,
    bytesPerIdentifier,
  };
}

function invertPath() {
  error.value = "";
  invertedPath.value = "";
  detectedIdentifierSize.value = null;
  repeaterCount.value = 0;
  copied.value = false;

  const parsed = parsePath(pathInput.value);

  if (parsed.error) {
    error.value = parsed.error;
    return;
  }

  detectedIdentifierSize.value = parsed.bytesPerIdentifier;
  repeaterCount.value = parsed.identifiers.length;
  invertedPath.value = parsed.identifiers.slice().reverse().join(",");
}

async function copyResult() {
  if (!invertedPath.value) {
    return;
  }

  try {
    await navigator.clipboard.writeText(invertedPath.value);
    copied.value = true;
  } catch {
    error.value = t.value.clipboardError;
  }
}

function clearPath() {
  pathInput.value = "";
  invertedPath.value = "";
  detectedIdentifierSize.value = null;
  repeaterCount.value = 0;
  error.value = "";
  copied.value = false;
}
</script>

<template>
  <div class="meshcore-path-inverter">
    <h3 class="meshcore-path-inverter__title">
      {{ t.title }}
    </h3>

    <div class="meshcore-path-inverter__field">
      <label class="meshcore-path-inverter__label" for="meshcore-path-input">
        {{ t.label }}
      </label>

      <input
        id="meshcore-path-input"
        v-model="pathInput"
        class="meshcore-path-inverter__input"
        type="text"
        :placeholder="t.placeholder"
        autocomplete="off"
        spellcheck="false"
        @keyup.enter="invertPath"
      >
    </div>

    <p class="meshcore-path-inverter__help">
      {{ t.help }}
    </p>

    <div class="meshcore-path-inverter__actions">
      <button
        class="meshcore-path-inverter__button"
        type="button"
        @click="invertPath"
      >
        {{ t.invert }}
      </button>

      <button
        v-if="invertedPath"
        class="meshcore-path-inverter__button meshcore-path-inverter__button--secondary"
        type="button"
        @click="copyResult"
      >
        {{ copied ? t.copied : t.copy }}
      </button>

      <button
        class="meshcore-path-inverter__button meshcore-path-inverter__button--ghost"
        type="button"
        @click="clearPath"
      >
        {{ t.clear }}
      </button>
    </div>

    <div v-if="invertedPath" class="meshcore-path-inverter__result">
      <p class="meshcore-path-inverter__result-label">
        {{ t.outputLabel }}
      </p>

      <code class="meshcore-path-inverter__output">
        {{ invertedPath }}
      </code>

      <p class="meshcore-path-inverter__message meshcore-path-inverter__message--success">
        {{ resultStats }}
      </p>
    </div>

    <p v-if="error" class="meshcore-path-inverter__message meshcore-path-inverter__message--errored">
      {{ error }}
    </p>
  </div>
</template>

<style scoped>
.meshcore-path-inverter {
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 1rem;
  background: var(--vp-c-bg-soft);
}

.meshcore-path-inverter__title {
  margin: 0 0 1rem;
  font-size: 1.05rem;
  line-height: 1.4;
}

.meshcore-path-inverter__field {
  min-width: 0;
}

.meshcore-path-inverter__label {
  display: block;
  margin-bottom: 0.45rem;
  font-weight: 600;
}

.meshcore-path-inverter__input {
  width: 100%;
  min-width: 0;
  padding: 0.7rem 0.85rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-family: var(--vp-font-family-mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace);
}

.meshcore-path-inverter__help {
  margin: 0.75rem 0 0;
  color: var(--vp-c-text-2);
  font-size: 0.92rem;
}

.meshcore-path-inverter__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1rem;
}

.meshcore-path-inverter__button {
  padding: 0.7rem 1rem;
  border: 0;
  border-radius: 10px;
  background: var(--vp-c-brand-1);
  color: white;
  cursor: pointer;
  font-weight: 600;
}

.meshcore-path-inverter__button--secondary {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
}

.meshcore-path-inverter__button--ghost {
  border: 1px solid var(--vp-c-divider);
  background: transparent;
  color: var(--vp-c-text-1);
}

.meshcore-path-inverter__result {
  margin-top: 1rem;
}

.meshcore-path-inverter__result-label {
  margin: 0 0 0.35rem;
  font-weight: 600;
}

.meshcore-path-inverter__output {
  display: block;
  overflow-x: auto;
  padding: 0.75rem 0.85rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  white-space: pre;
}

.meshcore-path-inverter__message {
  margin: 0.85rem 0 0;
}

.meshcore-path-inverter__message--success {
  color: #1e8449;
}

.meshcore-path-inverter__message--errored {
  color: #c0392b;
}

@media (max-width: 640px) {
  .meshcore-path-inverter__actions {
    flex-direction: column;
  }

  .meshcore-path-inverter__button {
    width: 100%;
  }
}
</style>
