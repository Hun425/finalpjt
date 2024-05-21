<script setup>
  import BoxOfficeList from '@/components/movie/BoxOfficeList.vue';
  import Navbar from '@/components/common/Navbar.vue'
</script>

<template>
  <div>
    <BoxOfficeList class="boxoffice-bg"/>
  </div>
</template>

<style scoped>
  .boxoffice-bg {
    background-color: black;
  }
</style>