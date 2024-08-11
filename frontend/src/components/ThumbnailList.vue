<template>
  <div class="row q-gutter-xs q-pa-sm">
    <ThumbnailCard
      v-for="set in sets"
      :key="set.id"
      :set_id="set.id"
      :thumbnail_width=thumbnail_width
      :thumbnail_height=thumbnail_height
    />
  </div>
</template>

<script setup>
import ThumbnailCard from "components/ThumbnailCard.vue";

const props = defineProps({
  sets: {
    type: Array,
    required: true,
  },
  thumbnail_width: {
    type: Number,
    required: true,
  },
  thumbnail_height: {
    type: Number,
    required: true,
  }
})
</script>

<style scoped>
</style>
