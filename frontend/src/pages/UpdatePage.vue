<template>
  <q-page padding>
    <div class="row justify-center">
      <q-uploader
        url="http://localhost:5000/api/upload"
        label="上传图像"
        @uploaded="handleUpload"
        accept="image/*"
        multiple
        auto-upload
      />
    </div>
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
