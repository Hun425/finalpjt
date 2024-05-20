<script setup>
  import BoxOfficeList from '@/components/movie/BoxOfficeList.vue';
  import Navbar from '@/components/common/Navbar.vue'
</script>

<template>
  <div>
    <Navbar class="dark" />
    <BoxOfficeList class="boxoffice-bg"/>
  </div>
</template>

<style scoped>
  .dark {
    background-color: black;
    color: white;
  }
  .boxoffice-bg {
    background-color: black;
  }
</style>