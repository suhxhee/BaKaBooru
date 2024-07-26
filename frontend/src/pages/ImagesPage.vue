<template>
  <q-page>
    <div>
      <header class="q-ma-lg row">
        <div class="row">
         <p class="text-h5">默认图库</p>
         <span class="text-h5">({{gallery.length}})</span>
        </div>
        <div class="q-ml-auto">
          <q-btn @click="clearGallery">
            <q-icon name="delete"/>清空图库
          </q-btn>
        </div>
      </header>
      <main class="row q-gutter-xs q-pa-sm">
        <q-card v-for="set in gallery" :key="set.id">
          <q-img
            :src="getThumbnailUrl(set.id)"
            @mouseover="set.isHovered = true"
            @mouseleave="set.isHovered = false"
            :style="{ filter: set.isHovered ? 'brightness(90%)' : 'brightness(100%)' }"
            class="img"
          />
        </q-card>
      </main>
    </div>
  </q-page>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const gallery = ref([]);

const fetchImages = async () => {
  const response = await axios.get('http://localhost:5000/api/gallery');
  gallery.value = response.data;
};

const getThumbnailUrl = (set_id) => {
  return `http://localhost:5000/api/set/${set_id}/thumbnail`;
};

const clearGallery = () => {
  axios.delete('http://localhost:5000/api/gallery/clear')
  gallery.value=[]
};


onMounted(fetchImages);
</script>


<style scoped>

.img{
   width: 150px;
   height: 210px;
}


</style>
