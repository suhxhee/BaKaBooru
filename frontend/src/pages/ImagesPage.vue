<template>
  <q-page >
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
            :style="{ filter: set.isHovered ?isHoverStyle: notHoverStyle}"
            class="thumbnail_large"
          />
        </q-card>
      </main>
  </q-page>
</template>


<script setup>
import {ref, onMounted, watch} from 'vue';
import {Dark, useQuasar} from 'quasar'
import axios from 'axios';
const $q = useQuasar()
const isDark = ref($q.dark.isActive)

const isHoverStyle =  ref(isDark.value?'brightness(70%)':'brightness(90%)');
const notHoverStyle =  ref(isDark.value?'brightness(80%)':'brightness(100%)')
// 监听深色模式的变化
watch(() => $q.dark.isActive, (newVar) => {
  if(newVar) {
    isHoverStyle.value = 'brightness(70%)';
    notHoverStyle.value =  'brightness(80%)'
  }
  else {
    isHoverStyle.value = 'brightness(90%)';
    notHoverStyle.value =  'brightness(100%)'
  }



})

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

.thumbnail_large{
   width: 200px;
   height: 280px;
}
.thumbnail_normal{
   width: 150px;
   height: 210px;
}
.thumbnail_small{
   width: 100px;
   height: 140px;
}


</style>
