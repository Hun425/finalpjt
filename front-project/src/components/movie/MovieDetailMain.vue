<template>
  <div v-show="movie" class="background">
    <div class="contents">
      <img v-if="movie && movie.backdrop_path" class="backdrop" :src="'https://image.tmdb.org/t/p/w500/'+ movie.backdrop_path" alt="backdrop">
      <img v-else class="backdrop" src="@/assets/backdrop.webp" alt="backdrop">
      <img v-if="movie && movie.poster_path" class="poster" :src="'https://image.tmdb.org/t/p/w500/'+ movie.poster_path" alt="@/assets/backdrop.webp">
      <p v-if="movie && movie.title" class="title">{{ movie.title }}</p>
      <p  class="releaseDate" >개봉일 : {{ movie.release_date }} $ {{ movie.id }}
      <br>
      {{ movie.like_users }}
    </p>
    </div>
  </div>
  <button class="likeBtn" @click="likeMovie">Like</button>
</template>

<script setup>
  import axios from 'axios';
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/account';
  const store = useAccountStore()
  const movie = ref({})
  const props = defineProps({
    movie:Object,
  })
  movie.value = props.movie

  const likeMovie = function () {
    axios({
      method:'post',
      url:`/movies/${movie.value.id}/likemovie/`,
      headers:{
        Authorization: `Token ${store.token}`
      }
    })
    .then(res => {
      movie.value = res.data
      console.log('clear!!')
    })
    .catch(err => {
      console.log(err)
    })
  }

</script>

<style scoped>
  .background {
    height: 524px;
    background-color: black;
  }
  .contents {
    position: relative;
    width: 842px;
    margin:0 auto;
    color: white;
  }
  .backdrop {
    height: 524px;
    width: 842px;
    filter: brightness(0.7) contrast(1); /* 밝기와 대비 조절 */
  }
  .title {
    position:absolute;
    top: 100px;
    left:100px;
    font-size: 24px;
    font-weight: bold;
  }
  .releaseDate {
    position:absolute;
    top:130px;
    left:100px;
    font-size: 16px;
    font-weight: bold;
  }
  .poster {
    position:absolute;
    top:100px;
    right:100px;
    width:200px;
    height:312px;
    border-radius: 10px;
  }
  .likeBtn {
    position:absolute;
    top:100px;
    left:300px;
    width: 50px;
    height: 30px;
    font-size: 16px;
    color:black;
    /* border-radius: 10px; */
  }


</style>