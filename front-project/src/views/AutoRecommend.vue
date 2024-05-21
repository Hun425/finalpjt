<template>
    <div>
      <h1>영화 검색</h1>
      <input v-model="movieName" placeholder="영화 이름을 입력하세요" />
      <button @click="searchMovies">영화 검색</button>
      <h2>유사한 영화</h2>
      <ul>
        <li v-for="movie in similarMovies" :key="movie.pk" >
          <div>
            <a :href="'/movies/' + movie.pk">{{ movie.title }}</a> - 유사도: {{ movie.similarity.toFixed(2) }}<br>
            평점: {{ movie.vote_average }}<br>
            <img :src="'https://image.tmdb.org/t/p/w500/'+ movie.poster_path" alt="포스터" style="width: 100px;"><br>
            출시 날짜: {{ movie.release_date }}
          </div >
        </li>
      </ul>
    </div>
  </template>
  
<script setup>
</script>


<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        movieName: '',
        similarMovies: []
      };
    },
    methods: {
      async searchMovies() {
        try {
          const response = await axios.get(import.meta.env.VITE_API_URL, {
            params: {
              movie_name: this.movieName,
            },
          });
          console.log('유사한 영화 검색 결과:', response.data);
          this.similarMovies = response.data.similar_movies;
        } catch (error) {
          console.error('영화 검색 오류:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* 스타일을 여기에 추가하세요 */
  </style>
  