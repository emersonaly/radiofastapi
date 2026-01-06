<template>
  <div>
    <h2>Agregar Estación</h2>
    <form @submit.prevent="addStation">
      <input v-model="name" placeholder="Nombre de la estación" required />
      <input v-model="url" placeholder="URL del stream" required />
      <button type="submit">Agregar</button>
    </form>
  </div>
</template>

<script>
import { ref } from "vue"

export default {
  emits: ["station-added"],
  setup(_, { emit }) {
    const name = ref("")
    const url = ref("")

    const addStation = async () => {
      await fetch("http://192.168.0.200:4440/stations/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name.value, stream_url: url.value })
      })
      name.value = ""
      url.value = ""
      emit("station-added")
    }

    return { name, url, addStation }
  }
}
</script>
