
<script setup>
import { ref, onMounted } from 'vue'

const stations = ref([])
const loading = ref(true)

const emit = defineEmits(['play-station'])

const fetchStations = async () => {
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL}/stations/`)
    if (res.ok) {
        stations.value = await res.json()
    }
  } catch (error) {
    console.error('Error fetching stations:', error)
  } finally {
    loading.value = false
  }
}

const play = (station) => {
  emit('play-station', station)
}

onMounted(() => {
  fetchStations()
})
</script>

<template>
  <div>
    <h1 style="margin-bottom: 2rem;">Radio Stations</h1>
    
    <div v-if="loading" style="text-align: center; color: var(--text-muted);">Loading stations...</div>
    
    <div v-else class="radio-grid">
      <div v-for="station in stations" :key="station.id" class="radio-card">
        <div style="display: flex; justify-content: space-between; align-items: start;">
            <div>
                <div class="radio-name">{{ station.name }}</div>
                <div class="radio-genre">{{ station.genre || 'Unknown' }}</div>
            </div>
            <button @click="play(station)" class="play-btn">
              ▶
            </button>
        </div>
      </div>
    </div>
  </div>
</template>
