<template>
  <div>
    <div class="boxoffice">
      <div class="contents">
        <div class="titleTag">
          <p class="contentNm">일별 박스오피스</p>
          <p class="line"></p>
        </div>
        <div class="container">
          <BoxOfficeListItem v-for="movie in dailyMovieList" :key="movie.rank" :movie="movie"/>
        </div>
      </div>
      <div calss="contents">
        <div class="titleTag">
          <p class="contentNm">주간 박스오피스</p>
          <p class="line"></p>
        </div>
        <div class="container">
          <BoxOfficeListItem v-for="movie in WeeklyMovieList" :key='movie.rank' :movie="movie"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import {ref} from 'vue'
  import BoxOfficeListItem from './BoxOfficeListItem.vue';
  import axios from 'axios'
  
  // daily는 하루전 / weekDate는 이틀 전
  const dailyDate = new Date(Date.now() - 86400000).toISOString().slice(0, 10).replace(/-/g, ''); // 하루 전 날짜
  const weekDate = new Date(Date.now() - 86400000 * 2).toISOString().slice(0, 10).replace(/-/g, ''); // 이틀 전 날짜



  // 이전 코드

  // 1) 일별 박스오피스 API
  /* "http://www.kobis.or.kr//kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json" */
  const dailyMovieList = ref({})
  axios({
    method:'get',
    url:'http://www.kobis.or.kr//kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json',
    params:{
      key:import.meta.env.VITE_BOXOFFICE_API_KEY,
      targetDt:dailyDate,
      itemPerPage:5,
      multiMovieYn:'N'
    }
  })
  .then(res => {
    dailyMovieList.value = res.data.boxOfficeResult.dailyBoxOfficeList
    console.log(dailyMovieList.value)
    return 0
  })
  .catch(err => console.log(err))


  // 2) 주간 박스오피스 API
  const WeeklyMovieList = ref({})
  axios({
    method:'get',
    url:'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json',
    params:{
      key:import.meta.env.VITE_BOXOFFICE_API_KEY,
      targetDt:weekDate,
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
  .boxoffice {
    width:1440px;
    height: 100vh;
    margin:0px auto;
    padding-top:50px;
    text-align: center;
    color:white;
  }
  .contents {
    margin-bottom:80px;
  }

  .container {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
  }

  .titleTag {
    margin: 30px 0 70px 0;
  }
  .titleTag p {
    margin: 0 auto;
  }
  .contentNm {
    width: 250px;
    font-weight:bold;
    font-size: 24px;
    padding-bottom: 20px;
  }
  .line {
    width: 120px;
    border-bottom: 1px solid white;

  }


  
</style>

<!-- https://m.search.naver.com/search.naver?query=%EC%98%81%ED%99%94+%EB%B2%94%EC%A3%84%EB%8F%84%EC%8B%9C4+%EC%98%88%EB%A7%A4 -->
