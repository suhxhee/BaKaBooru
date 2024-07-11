<template>
  <q-page padding>
    <q-btn @click="showMessage" label="Click me!" />
  </q-page>
</template>

<script>
export default {
  name: 'IndexPage',
  methods: {
    showMessage() {
      this.$q.notify({
        message: 'Hello, Quasar!',
        color: 'positive',
        position: 'top'
      });
    }
  }
}
</script>

<style>
/* 添加一些样式 */
</style>
