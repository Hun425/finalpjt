<!-- https://encrypted-tbn0.gstatic.com/images?q=tbn:AN…wwaP9UbKjHzbqMzXEHSPXNyIa6BudJBXpz0WMo&usqp=CAE&s -->


<script setup>
  import {useRoute} from 'vue-router'
  import {ref} from 'vue'
  import axios from 'axios'
  const props = defineProps({
    movie:Object,
  })
  // console.log(props)
  console.log(props.movie)



  // 영화 세부정보 가져오기 -> TMDB
  const movieDetail = ref({})
  // 영화를 가져오기 위해서는 movieId가 필요하다!! => 영화진흥원과 TMDB의 영화 ID가 다르다!!
  // const url = `https://api.themoviedb.org/3/movie/${props.movie.movieCd}`
  // axios
  // .request(
  //   {
  //     method: 'GET',
  //     url: url,
  //     params: {
  //       language: 'ko-KR',
  //       // include_adult:false,
  //       // include_video:true,
  //       // sort_by:'tol_rated.desc',
  //     },
  //     headers: {
  //       accept: 'application/json',
  //       Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZTE2Mzg5OTFhMTgwMjJmMzZhM2FlNDMyM2JlZDk4NSIsInN1YiI6IjY2M2IyZjYzNjlkYWYzM2Q5NjhkYTM2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Gsg5VKMoFDJo4eUrc_ICTuipDFShTQj0-x2QGpEMQvI'
  //     }
  //   }
  // )
  // .then(function (response) {
  //   console.log(response.data)
  //   movieDetail.value = response.data
  //   console.log('DetailAPI completed')
  //   })
  // .catch(error => {
  //   console.log('error')
  // })
    
</script>

<template>
  <div class="movieCard">
    <div class="image-container">
      <img class="poster" src='@/assets/common.jpg' alt="">
      <span class="rank">{{ movie.rank }}</span>
      <span class="change" v-if="movie.rankInten != 0">{{ movie.rankInten }} | UP</span>
      <div class="overlay">
        <div>
            <a :href="`https://m.search.naver.com/search.naver?query=영화+${movie.movieNm}+예매`"><button class="info-btn" type="submit">예매하기</button></a>
        </div>
      </div>
    </div>
  </div>

</template>

<!-- 개봉일자까지 고려해서 D-N까지 표현해도 좋을 듯! -->
<style scoped>
  .movieCard {
    display: flex;
    flex-direction: row;
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

 .change {
  position:absolute;
  top:190px;
  right: 10px;
  color:white;
  font-size: 30px;
  font-weight: 500;
  padding: 0;
 }

  .image-container {
    position: relative;
    height:260px; width:200px;
    overflow: hidden;
  }

  .image-container img {
    width: 100%;
    height: 100%;
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
    color: #333;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease, color 0.3s ease;
  }

  .info-btn:hover {
    background-color: #333;
    color: #fff;
  }
</style>




