<template>
  <q-page padding>
    <q-uploader
      url="http://localhost:5000/api/upload"
      label="上传图片"
      @uploaded="handleUpload"
      accept="image/*"
      multiple
      auto-upload
    />
    <q-list v-if="uploadedImages.length">
      <q-item v-for="image in uploadedImages" :key="image.file_id">
        <q-item-section>{{ image.filename }}</q-item-section>
      </q-item>
    </q-list>
  </q-page>
</template>

<script setup>
import { ref } from 'vue';

const uploadedImages = ref([]);

const handleUpload = (response) => {
  const uploadedFile = response.xhr.response ? JSON.parse(response.xhr.response) : response;
  uploadedImages.value.push(uploadedFile);
};
</script>

<style>
</style>
