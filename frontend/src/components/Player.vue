<template>
  <div>
    <h2>Reproduciendo: {{ station.name }}</h2>
    <audio controls autoplay :src="station.stream_url"></audio>
  </div>
</template>

<script>
export default {
  props: ["station"]
}
</script>
