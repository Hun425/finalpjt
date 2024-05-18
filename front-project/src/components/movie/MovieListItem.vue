<!-- https://encrypted-tbn0.gstatic.com/images?q=tbn:AN…wwaP9UbKjHzbqMzXEHSPXNyIa6BudJBXpz0WMo&usqp=CAE&s -->

<script setup>
  import {useRouter} from 'vue-router'
  import {onMounted} from 'vue'
  const props = defineProps({
    movie:Object,
  })
  const maxLength = 11
  const router = useRouter()
  const goToDetail = function (movie_pk) {
    router.push({name:'movieDetail', params:{moviepk: movie_pk}})
  }

  // 개봉일에 따른 표시변화
  const getImageSource = function() {
      const currentDate = new Date(); // 현재 날짜와 시간
      const releaseDate = new Date(props.movie.release_date); // movie의 release_date
      const nextMonthDate = new Date(); // 현재 날짜를 복사하여 사용
      nextMonthDate.setMonth(nextMonthDate.getMonth() - 1); // 현재 날짜에 한 달을 더함

      // 현재 날짜와 release_date 비교
      if (releaseDate > currentDate) {
        return 'A'; // 현재 날짜 이후인 경우 'A' 이미지의 경로
      } else if ( nextMonthDate < releaseDate ) {
        return 'B'; // 현재 날짜 이전인 경우 'B' 이미지의 경로
      } else {
        return 0
      }
    }

</script>
<!-- 소수 한자리수 표현 => 평점 : {{movie.vote_average.toFixed(1)}}점 -->
<template>
  <div v-if="movie" class="movieCard">
    <div class="image-container">
      <img @click="goToDetail(movie.pk)" class="poster" :src="'https://image.tmdb.org/t/p/w500/'+ movie.poster_path" :alt="`${movie.title}`">
      
      
      
    </div>
    <div class="movieInfo">
      <div class="title">{{ movie.title.length > maxLength ? movie.title.slice(0, maxLength) + '...' : movie.title }}</div>
      <span v-if="getImageSource() == 'A'" class="day soon">D</span>
      <span v-if="getImageSource() == 'B'" class="day hot">Hot</span>
    </div>
    <div>개봉일 : {{ movie.release_date }}</div>
  </div>

</template>

<style scoped>
  .movieCard {
    display: flex;
    flex-direction: column;
    width: 200px;
    height: 310px;
    border-radius: 10%;
    margin: 30px auto;
  }

  .movieInfo {
    display: flex;
    position: relative;
    padding: 22px 0px 11px 30px ;  /**상 좌 하 우? (시계방향) */
    flex-direction:column;
    align-items:flex-start;
    justify-content:space-around;
  }

  .title {
    font-size: 16px;
    font-weight: 600;
  }

  .poster{
    border-radius: 10px;
    height:270px;
    width:200px;
  }
  
  .image-container {
    height:260px; width:200px;
  }
  .day {
    position: absolute;
    top: 20px;
    left: 0px;
    width:20px;
    height: 20px;
    border-radius: 10%;
    text-align: center;
    font-weight: bold;
    color: white;
  }
  .soon {
    font-size: 15px;
    padding-top: 1px;
    background-color:rgb(35, 148, 0) ;
  }
  .hot {
    padding-top: 3px;
    background-color: rgb(255, 68, 0);
    font-size: 11px;
  }

</style>