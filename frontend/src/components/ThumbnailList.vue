<template>
  <div class="row q-gutter-xs q-pa-sm">
    <q-card v-for="set in sets" :key="set.id">
      <q-img
        :src="getThumbnailUrl(set.id)"
        @mouseover="set.isHovered = true"
        @mouseleave="set.isHovered = false"
        :style="{
          'width':thumbnail_width+'px',
          'height':thumbnail_height+'px',
          filter: set.isHovered ?isHoverStyle: notHoverStyle
        }"
      />
    </q-card>
  </div>
</template>

<script setup>
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

const isHoverStyle =  'brightness(90%)';
const notHoverStyle =  'brightness(100%)';
const getThumbnailUrl = (set_id) => {
  return `http://localhost:5000/api/set/${set_id}/thumbnail`;
};

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
