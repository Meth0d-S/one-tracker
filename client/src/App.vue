<script setup lang="ts">
import axios from "axios"

setInterval(async () => {
    const {data} = await axios.get("http://95.214.63.182")
    console.log(data)
}, 1000)
</script>

<template>
</template>

<style scoped>
</style>