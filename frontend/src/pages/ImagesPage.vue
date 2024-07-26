<template>
  <div class="q-gutter-xs">
    <div class="row q-gutter-sm q-pa-sm" >
      <q-card v-for="image in images" :key="image.id">
        <q-img
          :src="getImageUrl(image.id)"
          @mouseover="image.isHovered = true"
          @mouseleave="image.isHovered = false"
          :style="{ filter: image.isHovered ? 'brightness(90%)' : 'brightness(100%)' }"
          class="img"
        />
      </q-card>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const images = ref([]);

const fetchImages = async () => {
  try {
    const response = await axios.get('http://localhost:5000/api/gallery');
    images.value = response.data;
  } catch (error) {
    console.error('Failed to fetch images:', error);
  }
};

const getImageUrl = (imageId) => {
  return `http://localhost:5000/api/set/${imageId}`;
};

onMounted(fetchImages);
</script>


<style scoped>

.img{
   width: 150px;
   height: 210px;
}

</style>
