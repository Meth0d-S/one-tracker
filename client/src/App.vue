<script setup lang="ts">
import axios from "axios"

setInterval(async () => {
    const {data} = await axios.get("http://localhost:8000/")
    console.log(data)
}, 1000)
</script>

<template>
</template>

<style scoped>
</style>