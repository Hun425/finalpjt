<template>
  <div>
    <div class="list-container">
      <div class="mainText">전체 영화</div>
      <MovieList />
    </div>
  </div>
  </template>
  
<script setup>
  import MovieList from '@/components/movie/MovieList.vue'
  import { useAccountStore } from '@/stores/account';
  const store = useAccountStore()
  store.isDark = false
  
</script>

<style scoped>
.list-container {
  width:1440px;
  margin:0 auto;
}
  .mainText {
    margin: 30px 0;
    font-weight: bold;
    font-size: 24px;
    text-align: center;
  }
</style>
