<template>
  <q-layout view="hhh Lpr lfr">

    <q-header reveal elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="drawer = !drawer" />
        <q-toolbar-title>
          BaKaBooru
        </q-toolbar-title>
        <q-btn @click="toggleDarkMode" :icon="darkModeIcon" >
        </q-btn>
      </q-toolbar>
    </q-header>

    <q-drawer
        v-model="drawer"
        show-if-above
        :mini="miniState"
        @mouseover="miniState = false"
        @mouseout="miniState = true"
        :width="180"
        :breakpoint="500"
        bordered
      >
      <q-list class="text-h6 q-gutter-sm q-py-sm">
        <!-- 菜单项: 图片库 -->
        <q-item clickable v-ripple @click="goToPage('GalleryPage')">
          <q-item-section avatar> <q-icon name="image" /> </q-item-section>
          <q-item-section> <q-item-label>图库</q-item-label> </q-item-section>
        </q-item>
        <!-- 菜单项: 上传 -->
        <q-item clickable v-ripple @click="goToPage('UpdatePage')">
          <q-item-section avatar> <q-icon name="update" /> </q-item-section>
          <q-item-section> <q-item-label>上传</q-item-label> </q-item-section>
        </q-item>
         <!-- 菜单项: 设置 -->
        <q-item clickable v-ripple @click="goToPage('settings')">
          <q-item-section avatar>
            <q-icon name="settings" />
          </q-item-section>
          <q-item-section>
            <q-item-label>设置</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer>

    </q-footer>

  </q-layout>
</template>

<script setup>
import {computed, ref} from 'vue';
import { useRouter } from 'vue-router';
import { Dark } from 'quasar'

const isDark = ref(Dark.isActive)

const toggleDarkMode = () => {
  isDark.value = !isDark.value
  Dark.set(isDark.value)
}

const darkModeIcon = computed(() => isDark.value ? 'light_mode' : 'dark_mode')
const drawer = ref(false);
const miniState = ref(true);
const router = useRouter();

const goToPage = (page) => {
  router.push({ name: page });
};
</script>
