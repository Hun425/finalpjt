<template>
    <div class="mainText">전체 영화</div>
    <div>
        <MovieList />
    </div>
  </template>
  
  <script setup>
    import MovieList from '@/components/movie/MovieList.vue'
    
  </script>
  
  <style scoped>
    .mainText {
      margin: 30px 0;
      font-weight: bold;
      font-size: 24px;
      text-align: center;
    }
  </style>
  