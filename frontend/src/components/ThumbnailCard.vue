<template>
  <q-card>
    <ThumbnailCardMenu :set_id=set_id />
    <q-img
      :src="getThumbnailUrl(set_id)"
      @mouseover="isHovered = true"
      @mouseleave="isHovered = false"
      @click="showImage(set_id)"
      :style="{
        'width':thumbnail_width+'px',
        'height':thumbnail_height+'px',
        filter: isHovered ? isHoverStyle : notHoverStyle
      }"
    />
  </q-card>
</template>

<script setup>
import {ref} from "vue";
import ThumbnailCardMenu from "components/ThumbnailCardMenu.vue";

const props = defineProps({
  set_id: {
    type: String,
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

const isHovered = ref(false);
const isHoverStyle =  'brightness(90%)';
const notHoverStyle =  'brightness(100%)';
const getThumbnailUrl = (set_id) => {
  return `http://localhost:5000/api/set/${set_id}/thumbnail`;
}
const showImage = (set_id)=>{
  window.open(`http://localhost:5000/api/set/${set_id}/image/${0}`, '_blank');
}

</script>

<style scoped>

</style>
