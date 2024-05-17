<template>
    <div class="movieList">
        <!-- 데이터 받은 후에 v-for로 전달하기 -->
            <MovieListItem v-for="movie in movieList" :key="movie.title" :movie="movie"/>
    </div>
  </template>
  
  <script setup>
    import {ref} from 'vue'
    import axios from 'axios'
    import MovieListItem from './MovieListItem.vue';
    
    const JangoURL = 'http://127.0.0.1:8000'
  
    // 영화 목록 가져오기
    const movieList = ref([])
  
    axios({
      method:'get',
      url:JangoURL + '/movies/',
      // params:{
      // }
    })
    .then(res => {
      console.log(res.data)
      movieList.value = res.data
      return 0
    })
    .catch(err => console.log(err))
  
  
  
  </script>
  
  <style>
    .movieList {
      width:1100px;
      margin:0 auto;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
  
    }
  </style>