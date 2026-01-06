<template>
  <div>
    <h2>Lista de Estaciones</h2>
    <ul>
      <li v-for="station in stations" :key="station.id">
        {{ station.name }}
        <button @click="$emit('play', station)">▶ Reproducir</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ["stations"]
}
</script>
