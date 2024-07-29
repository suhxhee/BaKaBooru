<template>
  <q-page class="q-ma-lg">
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
       <ThumbnailList :sets="gallery" :thumbnail_width=200 :thumbnail_height=280 />
  </q-page>
</template>

<script setup>
import {ref, onMounted} from 'vue';
import axios from 'axios';
import ThumbnailList from "components/ThumbnailList.vue";

const gallery = ref([]);

const fetchImages = async () => {
  const response = await axios.get('http://localhost:5000/api/gallery');
  gallery.value = response.data;
};

const clearGallery = () => {
  axios.delete('http://localhost:5000/api/gallery/clear')
  gallery.value=[]
};

onMounted(fetchImages);
</script>


<style scoped>




</style>
