<template>
  <q-menu touch-position context-menu>
    <q-list dense style="min-width: 100px">
     <!-- 查看 -->
      <q-item clickable @click="viewItem" v-close-popup>
        <q-item-section avatar>
          <q-icon name="visibility" />
        </q-item-section>
        <q-item-section class="text-center">
          <q-item-label> 查看 </q-item-label>
        </q-item-section>
      </q-item>
      <!-- 下载 -->
      <q-item clickable @click="downloadItem" v-close-popup>
        <q-item-section avatar>
          <q-icon name="download" />
        </q-item-section>
        <q-item-section class="text-center">
          <q-item-label> 下载 </q-item-label>
        </q-item-section>
      </q-item>
      <!-- 复制链接 -->
      <q-item clickable @click="copyLink" v-close-popup>
        <q-item-section avatar>
          <q-icon name="link" />
        </q-item-section>
        <q-item-section class="text-center">
          <q-item-label> 复制链接 </q-item-label>
        </q-item-section>
      </q-item>
      <!-- 删除图集 -->
      <q-item clickable @click="deleteItem(set_id)" v-close-popup>
        <q-item-section avatar>
          <q-icon name="delete" />
        </q-item-section>
        <q-item-section class="text-center">
          <q-item-label> 删除图集 </q-item-label>
        </q-item-section>
      </q-item>
      <!-- Test -->
      <q-separator />

      <q-item clickable>
        <q-item-section>Test</q-item-section>
        <q-item-section side>
          <q-icon name="keyboard_arrow_right" />
        </q-item-section>

        <q-menu anchor="top end" self="top start">
          <q-list>
            <q-item
              v-for="n in 3"
              :key="n"
              dense
              clickable
            >
              <q-item-section>Submenu Label</q-item-section>
              <q-item-section side>
                <q-icon name="keyboard_arrow_right" />
              </q-item-section>
              <q-menu auto-close anchor="top end" self="top start">
                <q-list>
                  <q-item
                    v-for="n in 3"
                    :key="n"
                    dense
                    clickable
                  >
                    <q-item-section>3rd level Label</q-item-section>
                  </q-item>
                </q-list>
              </q-menu>
            </q-item>
          </q-list>
        </q-menu>
      </q-item>

      <q-separator />

      <q-item clickable v-close-popup>
        <q-item-section>Test</q-item-section>
      </q-item>
    </q-list>
  </q-menu>
</template>

<script setup>
import axios from "axios";

const props = defineProps({
  set_id: {
    type: String,
    required: true,
  },
})



function viewItem() {

}

function downloadItem() {

}

function copyLink() {

}

function deleteItem(set_id) {
  axios.delete(`http://localhost:5000/api/set/${set_id}/delete`)
}


</script>

<style scoped>

</style>
