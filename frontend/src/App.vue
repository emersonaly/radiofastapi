
<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

const currentStation = ref(null)
const audioPlayer = ref(null)
const isPlaying = ref(false)

const playStation = (station) => {
  currentStation.value = station
  if (audioPlayer.value) {
    audioPlayer.value.src = station.stream_url
    audioPlayer.value.play().catch(e => console.error("Play error:", e))
    isPlaying.value = true
  }
}

const togglePlay = () => {
  if (audioPlayer.value) {
    if (isPlaying.value) {
      audioPlayer.value.pause()
    } else {
      audioPlayer.value.play()
    }
    isPlaying.value = !isPlaying.value
  }
}
</script>

<template>
  <header>
    <div class="container navbar">
      <RouterLink to="/" class="nav-brand">RadioFastAPI</RouterLink>
      <nav class="nav-links">
        <RouterLink to="/" class="nav-link">Home</RouterLink>
        <RouterLink to="/admin" class="nav-link">Admin</RouterLink>
        <RouterLink to="/login" class="nav-link">Login</RouterLink>
      </nav>
    </div>
  </header>

  <main class="container">
    <RouterView @play-station="playStation" />
  </main>

  <div v-if="currentStation" class="player-bar">
    <div class="container" style="display: flex; width: 100%; align-items: center; justify-content: space-between;">
      <div class="player-info">
        <div>
          <div style="font-weight: bold;">{{ currentStation.name }}</div>
          <div style="font-size: 0.8rem; color: #9ca3af;">{{ currentStation.genre }}</div>
        </div>
      </div>
      <div class="player-controls">
        <audio ref="audioPlayer" controls autoplay style="width: 100%; max-width: 400px;"></audio>
      </div>
    </div>
  </div>
</template>
