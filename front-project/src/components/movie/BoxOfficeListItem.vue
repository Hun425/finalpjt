<!-- https://encrypted-tbn0.gstatic.com/images?q=tbn:AN…wwaP9UbKjHzbqMzXEHSPXNyIa6BudJBXpz0WMo&usqp=CAE&s -->

<script setup>
  import { usePosterStore } from '@/stores/poster';
  const store = usePosterStore()
  const props = defineProps({
    movie:Object,
  })
  props.movie
  
</script>

<template>
  <div class="movieCard">
    <div class="image-container">
      <img class="poster" :src="store.poster[`${movie.movieNm}`]" alt="movie_poster">
      <!-- <span class="rank">{{ movie.rank }}</span> -->
      <div class="overlay">
        <a class="link" :href="`https://m.search.naver.com/search.naver?query=영화+${movie.movieNm}+예매`">
          <button class="info-btn" type="submit">예매하기</button>
        </a>
      </div>
    </div>
  </div>
</template>

<!-- 개봉일자까지 고려해서 D-N까지 표현해도 좋을 듯! -->
<style scoped>
  .movieCard {
    margin:0 auto;
    width: 200px;
    height: 260px;
    border-radius: 10px;
  }
  .movieCard:hover {
    scale:1.1;
  }

  .poster{
    border-radius: 10px;
    height:260px;
    width:200px;
  }
  .rank {
  position:absolute;
  top:200px;
  left: 10px;
  color:white;
  font-size: 64px;
  font-style: italic;
  /* font-weight:bold; */
  padding: 0;
 }

 /* .change {
  position:absolute;
  top:190px;
  right: 10px;
  color:white;
  font-size: 30px;
  font-weight: 500;
  padding: 0;
 } */

  .image-container {
    position: relative;
    height:260px; width:200px;
    overflow: hidden;
  }

  .image-container img {
    width: 100%;
    height: 100%;
    box-shadow: inset 0px 0px 15px 15px #62b0cb;
    transition: filter 0.3s ease;
  }

  .image-container .overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.5);
    opacity: 0;
    transition: opacity 0.3s ease;
    display: flex;
    padding: 10px;
    /* justify-content: center;
    align-items: center; */
  }
  .overlay {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .image-container:hover img {
    filter: brightness(70%);
  }

  .image-container:hover .overlay {
    opacity: 1;
  }

  .description {
    color:white;
  }
  .info-btn {
    padding: 10px 20px;
    background-color: #fff;
    color: #000000;
    border: none;
    border-radius: 5px;
    cursor: pointer;

    transition: background-color 0.3s ease, color 0.3s ease;
  }

  .info-btn:hover {
    background-color: #2a0072;
    color: #fff;
  }


</style>