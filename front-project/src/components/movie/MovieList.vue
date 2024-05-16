<!-- https://m.search.naver.com/search.naver?query=%EC%98%81%ED%99%94+%EB%B2%94%EC%A3%84%EB%8F%84%EC%8B%9C4+%EC%98%88%EB%A7%A4 -->


<template>
  <div class="main">
    <p class="textcenter">MovieListVue</p>
    <div class="boxofficetitle">
      <p class="textcenter">일별 박스오피스</p>
      <!-- <div class="line"></div> -->
    </div >
    <div class="container">
      <MovieListItem v-for="movie in dailyMovieList" :key="movie.rank" :movie="movie"/>
    </div>
    <div class="boxofficetitle">
      <p class="textcenter">주간 박스오피스</p>
      <!-- <div class="line"></div> -->
    </div>
    <div v-if="WeeklyMovieList" class="container">
      <MovieListItem v-for="movie in WeeklyMovieList" :key='movie.rank' :movie="movie"/>
    </div>
  </div>

</template>
<script setup>
  import {ref} from 'vue'
  import MovieListItem from './MovieListItem.vue';
  import axios from 'axios'
  
  /* 진흥원 API KEY 2ff10453a726bf1ff793c4f8179b2afd */

  // 1) 일별 박스오피스 API
  /* "http://www.kobis.or.kr//kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json" */
  const dailyMovieList = ref({})
  axios({
    method:'get',
    url:'http://www.kobis.or.kr//kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json',
    params:{
      key:'2ff10453a726bf1ff793c4f8179b2afd',
      targetDt:'20240512',
      itemPerPage:5,
      multiMovieYn:'N'
    }
  })
  .then(res => {
    dailyMovieList.value = res.data.boxOfficeResult.dailyBoxOfficeList
    return 0
  })
  .catch(err => console.log(err))


  // 2) 주간 박스오피스 API
  const WeeklyMovieList = ref({})
  axios({
    method:'get',
    url:'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json',
    params:{
      key:'2ff10453a726bf1ff793c4f8179b2afd',
      targetDt:'20240512',
      itemPerPage:5,
      weekGb:0,
    }
  })
  .then(res => {
    WeeklyMovieList.value = res.data.boxOfficeResult.weeklyBoxOfficeList
    console.log(WeeklyMovieList.value)

    return 0
  })
  .catch(err => console.log(err))
</script>

<style scoped>
  * {
    margin: 10px 0; /* 상하 | 좌우 */
  }
  .main {
    display: flex;
    flex-direction: column;

    width:1100px;
    margin:0px auto;
  }
  .container {
    display: flex;
    justify-content: space-between;
    width: 1100px;
  }
  .boxofficetitle{
    display: flex;
    /* flex-direction: column; */
    justify-content: center;
    position: relative;
  }
  .textcenter {
    font-weight:bold;
  }
  .line{
    border: 1px solid rgb(36, 31, 31);
    height:1px;
    width: 110px;
    top:140px;
    left:497px;
    
  }
  
</style>  