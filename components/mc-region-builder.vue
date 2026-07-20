<script setup>
import { computed, ref } from "vue";

const props = defineProps({
  lang: {
    type: String,
    default: "fr",
  },
});

const selectedCode = ref("");
const searchQuery = ref("");
const copied = ref(false);

const regionMap = {
  "fr-01": ["fr-ara"],
  "fr-02": ["fr-hdf"],
  "fr-03": ["fr-ara"],
  "fr-04": ["fr-pac"],
  "fr-05": ["fr-pac"],
  "fr-06": ["fr-pac"],
  "fr-07": ["fr-ara"],
  "fr-08": ["fr-ges"],
  "fr-09": ["fr-occ"],
  "fr-10": ["fr-ges"],
  "fr-11": ["fr-occ"],
  "fr-12": ["fr-occ"],
  "fr-13": ["fr-pac"],
  "fr-14": ["fr-nor"],
  "fr-15": ["fr-ara"],
  "fr-16": ["fr-naq"],
  "fr-17": ["fr-naq"],
  "fr-18": ["fr-cvl"],
  "fr-19": ["fr-naq"],
  "fr-2a": ["fr-cor"],
  "fr-2b": ["fr-cor"],
  "fr-21": ["fr-bfc"],
  "fr-22": ["fr-bre"],
  "fr-23": ["fr-naq"],
  "fr-24": ["fr-naq"],
  "fr-25": ["fr-bfc"],
  "fr-26": ["fr-ara"],
  "fr-27": ["fr-nor"],
  "fr-28": ["fr-cvl"],
  "fr-29": ["fr-bre"],
  "fr-30": ["fr-occ"],
  "fr-31": ["fr-occ"],
  "fr-32": ["fr-occ"],
  "fr-33": ["fr-naq"],
  "fr-34": ["fr-occ"],
  "fr-35": ["fr-bre"],
  "fr-36": ["fr-cvl"],
  "fr-37": ["fr-cvl"],
  "fr-38": ["fr-ara"],
  "fr-39": ["fr-bfc"],
  "fr-40": ["fr-naq"],
  "fr-41": ["fr-cvl"],
  "fr-42": ["fr-ara"],
  "fr-43": ["fr-ara"],
  "fr-44": ["fr-pdl"],
  "fr-45": ["fr-cvl"],
  "fr-46": ["fr-occ"],
  "fr-47": ["fr-naq"],
  "fr-48": ["fr-occ"],
  "fr-49": ["fr-pdl"],
  "fr-50": ["fr-nor"],
  "fr-51": ["fr-ges"],
  "fr-52": ["fr-ges"],
  "fr-53": ["fr-pdl"],
  "fr-54": ["fr-ges"],
  "fr-55": ["fr-ges"],
  "fr-56": ["fr-bre"],
  "fr-57": ["fr-ges"],
  "fr-58": ["fr-bfc"],
  "fr-59": ["fr-hdf"],
  "fr-60": ["fr-hdf"],
  "fr-61": ["fr-nor"],
  "fr-62": ["fr-hdf"],
  "fr-63": ["fr-ara"],
  "fr-64": ["fr-naq"],
  "fr-65": ["fr-occ"],
  "fr-66": ["fr-occ"],
  "fr-67": ["fr-ges"],
  "fr-68": ["fr-ges"],
  "fr-69": ["fr-ara"],
  "fr-70": ["fr-bfc"],
  "fr-71": ["fr-bfc"],
  "fr-72": ["fr-pdl"],
  "fr-73": ["fr-ara"],
  "fr-74": ["fr-ara"],
  "fr-75": ["fr-idf"],
  "fr-76": ["fr-nor"],
  "fr-77": ["fr-idf"],
  "fr-78": ["fr-idf"],
  "fr-79": ["fr-naq"],
  "fr-80": ["fr-hdf"],
  "fr-81": ["fr-occ"],
  "fr-82": ["fr-occ"],
  "fr-83": ["fr-pac"],
  "fr-84": ["fr-pac"],
  "fr-85": ["fr-pdl"],
  "fr-86": ["fr-naq"],
  "fr-87": ["fr-naq"],
  "fr-88": ["fr-ges"],
  "fr-89": ["fr-bfc"],
  "fr-90": ["fr-bfc"],
  "fr-91": ["fr-idf"],
  "fr-92": ["fr-idf"],
  "fr-93": ["fr-idf"],
  "fr-94": ["fr-idf"],
  "fr-95": ["fr-idf"],

  // Overseas departments: left without a mainland quadrant.
  "fr-971": ["fr-gua"],
  "fr-972": ["fr-mtq"],
  "fr-973": ["fr-guf"],
  "fr-974": ["fr-reu"],
  "fr-976": ["fr-may"],
};

const labels = {
  "fr-01": "01 - Ain",
  "fr-02": "02 - Aisne",
  "fr-03": "03 - Allier",
  "fr-04": "04 - Alpes-de-Haute-Provence",
  "fr-05": "05 - Hautes-Alpes",
  "fr-06": "06 - Alpes-Maritimes",
  "fr-07": "07 - Ardèche",
  "fr-08": "08 - Ardennes",
  "fr-09": "09 - Ariège",
  "fr-10": "10 - Aube",
  "fr-11": "11 - Aude",
  "fr-12": "12 - Aveyron",
  "fr-13": "13 - Bouches-du-Rhône",
  "fr-14": "14 - Calvados",
  "fr-15": "15 - Cantal",
  "fr-16": "16 - Charente",
  "fr-17": "17 - Charente-Maritime",
  "fr-18": "18 - Cher",
  "fr-19": "19 - Corrèze",
  "fr-2a": "2A - Corse-du-Sud",
  "fr-2b": "2B - Haute-Corse",
  "fr-21": "21 - Côte-d'Or",
  "fr-22": "22 - Côtes-d'Armor",
  "fr-23": "23 - Creuse",
  "fr-24": "24 - Dordogne",
  "fr-25": "25 - Doubs",
  "fr-26": "26 - Drôme",
  "fr-27": "27 - Eure",
  "fr-28": "28 - Eure-et-Loir",
  "fr-29": "29 - Finistère",
  "fr-30": "30 - Gard",
  "fr-31": "31 - Haute-Garonne",
  "fr-32": "32 - Gers",
  "fr-33": "33 - Gironde",
  "fr-34": "34 - Hérault",
  "fr-35": "35 - Ille-et-Vilaine",
  "fr-36": "36 - Indre",
  "fr-37": "37 - Indre-et-Loire",
  "fr-38": "38 - Isère",
  "fr-39": "39 - Jura",
  "fr-40": "40 - Landes",
  "fr-41": "41 - Loir-et-Cher",
  "fr-42": "42 - Loire",
  "fr-43": "43 - Haute-Loire",
  "fr-44": "44 - Loire-Atlantique",
  "fr-45": "45 - Loiret",
  "fr-46": "46 - Lot",
  "fr-47": "47 - Lot-et-Garonne",
  "fr-48": "48 - Lozère",
  "fr-49": "49 - Maine-et-Loire",
  "fr-50": "50 - Manche",
  "fr-51": "51 - Marne",
  "fr-52": "52 - Haute-Marne",
  "fr-53": "53 - Mayenne",
  "fr-54": "54 - Meurthe-et-Moselle",
  "fr-55": "55 - Meuse",
  "fr-56": "56 - Morbihan",
  "fr-57": "57 - Moselle",
  "fr-58": "58 - Nièvre",
  "fr-59": "59 - Nord",
  "fr-60": "60 - Oise",
  "fr-61": "61 - Orne",
  "fr-62": "62 - Pas-de-Calais",
  "fr-63": "63 - Puy-de-Dôme",
  "fr-64": "64 - Pyrénées-Atlantiques",
  "fr-65": "65 - Hautes-Pyrénées",
  "fr-66": "66 - Pyrénées-Orientales",
  "fr-67": "67 - Bas-Rhin",
  "fr-68": "68 - Haut-Rhin",
  "fr-69": "69 - Rhône",
  "fr-70": "70 - Haute-Saône",
  "fr-71": "71 - Saône-et-Loire",
  "fr-72": "72 - Sarthe",
  "fr-73": "73 - Savoie",
  "fr-74": "74 - Haute-Savoie",
  "fr-75": "75 - Paris",
  "fr-76": "76 - Seine-Maritime",
  "fr-77": "77 - Seine-et-Marne",
  "fr-78": "78 - Yvelines",
  "fr-79": "79 - Deux-Sèvres",
  "fr-80": "80 - Somme",
  "fr-81": "81 - Tarn",
  "fr-82": "82 - Tarn-et-Garonne",
  "fr-83": "83 - Var",
  "fr-84": "84 - Vaucluse",
  "fr-85": "85 - Vendée",
  "fr-86": "86 - Vienne",
  "fr-87": "87 - Haute-Vienne",
  "fr-88": "88 - Vosges",
  "fr-89": "89 - Yonne",
  "fr-90": "90 - Territoire de Belfort",
  "fr-91": "91 - Essonne",
  "fr-92": "92 - Hauts-de-Seine",
  "fr-93": "93 - Seine-Saint-Denis",
  "fr-94": "94 - Val-de-Marne",
  "fr-95": "95 - Val-d'Oise",
  "fr-971": "971 - Guadeloupe",
  "fr-972": "972 - Martinique",
  "fr-973": "973 - Guyane",
  "fr-974": "974 - La Réunion",
  "fr-976": "976 - Mayotte",
};

const overseasDepartmentCodes = ["fr-971", "fr-972", "fr-973", "fr-974", "fr-976"];

const messages = {
  fr: {
    title: "Générateur de région MeshCore France",
    searchPlaceholder: "Rechercher un département...",
    resultTitle: "Résultat",
    cliTitle: "CLI",
    copy: "Copier",
    copied: "Copié",
    noSelection: "Sélectionnez un département pour générer les commandes.",
    emptySearch: "Aucun département trouvé.",
  },
  en: {
    title: "MeshCore France region generator",
    searchPlaceholder: "Search for a department...",
    resultTitle: "Result",
    cliTitle: "CLI",
    copy: "Copy",
    copied: "Copied",
    noSelection: "Select a department to generate the commands.",
    emptySearch: "No department found.",
  },
};

const t = computed(() => messages[props.lang] ?? messages.fr);

const departments = computed(() =>
  Object.entries(labels).map(([code, label]) => ({
    code,
    label,
  })),
);

const normalizedSearchQuery = computed(() => normalizeText(searchQuery.value));

const filteredDepartments = computed(() => {
  if (!normalizedSearchQuery.value) {
    return departments.value;
  }

  return departments.value.filter((department) => {
    const searchable = normalizeText(`${department.label} ${department.code}`);
    return searchable.includes(normalizedSearchQuery.value);
  });
});

const selectedValues = computed(() => {
  if (!selectedCode.value) {
    return [];
  }

  const isOverseasDepartment = overseasDepartmentCodes.includes(selectedCode.value);
  const regions = regionMap[selectedCode.value];

  const parts = ["eu", "fr"];

  if (!isOverseasDepartment && regions && regions.length > 0) {
    parts.push(...regions);
  }

  return [...parts, selectedCode.value];
});

const cliCommands = computed(() => {
  if (!selectedValues.value.length) {
    return "";
  }

  return [
    `region def ${[...selectedValues.value].join(" ")}`,
    `region default fr`,
    "region save",
  ].join("\n");
});

function normalizeText(value) {
  return value
    .toLowerCase()
    .normalize("NFD")
    .replace(/\p{Diacritic}/gu, "");
}

function selectDepartment(code) {
  selectedCode.value = code;
  copied.value = false;
}

async function copyCliCommands() {
  if (!cliCommands.value) {
    return;
  }

  copied.value = false;

  try {
    await navigator.clipboard.writeText(cliCommands.value);
    copied.value = true;
  } catch {
    fallbackCopy(cliCommands.value);
    copied.value = true;
  }

  window.setTimeout(() => {
    copied.value = false;
  }, 1600);
}

function fallbackCopy(text) {
  const textarea = document.createElement("textarea");
  textarea.value = text;
  textarea.setAttribute("readonly", "");
  textarea.style.position = "absolute";
  textarea.style.left = "-9999px";

  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  document.body.removeChild(textarea);
}
</script>

<template>
  <div class="meshcore-builder">
    <div class="meshcore-builder__header">
      {{ t.title }}
    </div>

    <div class="meshcore-builder__body">
      <section class="meshcore-builder__panel">
        <input
          v-model="searchQuery"
          class="meshcore-builder__input"
          type="search"
          :placeholder="t.searchPlaceholder"
        >

        <div class="meshcore-builder__list" role="list">
          <button
            v-for="department in filteredDepartments"
            :key="department.code"
            class="meshcore-builder__item"
            :class="{ 'meshcore-builder__item--active': department.code === selectedCode }"
            type="button"
            role="listitem"
            :aria-pressed="department.code === selectedCode"
            @click="selectDepartment(department.code)"
          >
            <span>{{ department.label }}</span>
            <span>{{ department.code }}</span>
          </button>

          <p
            v-if="filteredDepartments.length === 0"
            class="meshcore-builder__empty"
          >
            {{ t.emptySearch }}
          </p>
        </div>
      </section>

      <section class="meshcore-builder__panel">
        <div class="meshcore-builder__box">
          <strong>{{ t.resultTitle }}</strong>

          <ul v-if="selectedValues.length" class="meshcore-builder__result">
            <li v-for="value in selectedValues" :key="value">
              {{ value }}
            </li>
          </ul>

          <p v-else class="meshcore-builder__muted">
            {{ t.noSelection }}
          </p>
        </div>

        <div class="meshcore-builder__box">
          <div class="meshcore-builder__box-header">
            <strong>{{ t.cliTitle }}</strong>

            <button
              class="meshcore-builder__copy"
              type="button"
              :disabled="!cliCommands"
              @click="copyCliCommands"
            >
              {{ copied ? t.copied : t.copy }}
            </button>
          </div>

          <pre class="meshcore-builder__cli">{{ cliCommands }}</pre>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.meshcore-builder {
  --mc-bg: var(--vp-c-bg);
  --mc-bg-dark: var(--vp-c-bg-soft);
  --mc-bg-darker: var(--vp-c-bg-alt);

  --mc-panel-border: var(--vp-c-border);
  --mc-border: var(--vp-c-divider);
  --mc-border-soft: var(--vp-c-divider);

  --mc-text: var(--vp-c-text-1);
  --mc-text-muted: var(--vp-c-text-2);

  --mc-accent: var(--vp-c-brand-1);
  --mc-accent-dark: var(--vp-c-brand-2);
  --mc-accent-hover: var(--vp-c-brand-2);
  --mc-active-bg: var(--vp-c-brand-soft);

  --mc-input-bg: var(--vp-c-bg-alt);
  --mc-cli-text: var(--vp-c-brand-1);
  --mc-white: var(--vp-c-white);

  max-width: 900px;
  overflow: hidden;
  border: 1px solid var(--mc-border);
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
  color: var(--mc-text);
}

.meshcore-builder__header {
  padding: 14px 16px;
  border-bottom: 1px solid var(--mc-panel-border);
  color: var(--mc-accent);
  font-weight: 600;
}

.meshcore-builder__body {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.meshcore-builder__panel {
  padding: 14px;
  border-right: 1px solid var(--mc-border-soft);
}

.meshcore-builder__panel:last-child {
  border-right: 0;
}

.meshcore-builder__input {
  width: 100%;
  box-sizing: border-box;
  margin-bottom: 10px;
  padding: 8px;
  border: 1px solid var(--mc-border);
  border-radius: 8px;
  background: var(--mc-input-bg);
  color: var(--mc-text);
  font: inherit;
}

.meshcore-builder__input::placeholder {
  color: var(--mc-text-muted);
}

.meshcore-builder__list {
  max-height: 260px;
  overflow: auto;
  border: 1px solid var(--mc-panel-border);
  border-radius: 8px;
  background: var(--mc-bg-darker);
}

.meshcore-builder__item {
  display: flex;
  width: 100%;
  justify-content: space-between;
  gap: 12px;
  padding: 8px;
  border: 0;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font: inherit;
  font-size: 13px;
  text-align: left;
  transition: background 0.15s, color 0.15s;
}

.meshcore-builder__item:hover {
  background: var(--mc-bg-dark);
}

.meshcore-builder__item--active {
  background: var(--mc-active-bg);
  color: var(--mc-accent);
}

.meshcore-builder__box {
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid var(--mc-panel-border);
  border-radius: 10px;
  background: var(--mc-bg-darker);
}

.meshcore-builder__box-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 8px;
}

.meshcore-builder__result {
  margin: 8px 0 0;
  padding-left: 1.25rem;
}

.meshcore-builder__muted,
.meshcore-builder__empty {
  margin: 8px 0 0;
  color: var(--mc-text-muted);
  font-size: 13px;
}

.meshcore-builder__empty {
  padding: 8px;
}

.meshcore-builder__cli {
  min-height: 110px;
  margin: 0;
  color: var(--mc-cli-text);
  font-size: 12px;
  white-space: pre-wrap;
}

.meshcore-builder__copy {
  padding: 6px 10px;
  border: 0;
  border-radius: 6px;
  background: var(--mc-accent-dark);
  color: var(--mc-white);
  cursor: pointer;
  font: inherit;
  transition: background 0.2s, opacity 0.2s;
}

.meshcore-builder__copy:hover:not(:disabled) {
  background: var(--mc-accent-hover);
}

.meshcore-builder__copy:disabled {
  opacity: 0.45;
  cursor: not-allowed;
}

.meshcore-builder__list::-webkit-scrollbar {
  width: 6px;
}

.meshcore-builder__list::-webkit-scrollbar-thumb {
  border-radius: 6px;
  background: var(--mc-border);
}

@media (max-width: 720px) {
  .meshcore-builder__body {
    grid-template-columns: 1fr;
  }

  .meshcore-builder__panel {
    border-right: 0;
    border-bottom: 1px solid var(--mc-border-soft);
  }

  .meshcore-builder__panel:last-child {
    border-bottom: 0;
  }
}
</style>