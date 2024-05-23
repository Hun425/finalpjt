<template>
  <div class="boxoffice">
    <div class="contents">
      <div class="titleTag">
        <p class="contentNm">일별 박스오피스</p>
        <p class="line"></p>
      </div>
      <div class="container">
        <BoxOfficeListItem 
          v-for="(movie, index) in dailyMovieList" 
          :key="movie.rank" 
          :movie="movie" 
          @click="emitTopMoviePoster(index)"
        />
      </div>
    </div>
    <div class="contents">
      <div class="titleTag">
        <p class="contentNm">주간 박스오피스</p>
        <p class="line"></p>
      </div>
      <div class="container">
        <BoxOfficeListItem 
          v-for="(movie, index) in weeklyMovieList" 
          :key="movie.rank" 
          :movie="movie" 
          @click="emitTopMoviePoster(index)"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
  import {ref, onMounted} from 'vue'
  import BoxOfficeListItem from './BoxOfficeListItem.vue';
  import axios from 'axios'
  
  // // daily는 하루전 / weekDate는 이틀 전
  // const dailyDate = new Date(Date.now() - 86400000).toISOString().slice(0, 10).replace(/-/g, ''); // 하루 전 날짜
  // const weekDate = new Date(Date.now() - 86400000 * 3).toISOString().slice(0, 10).replace(/-/g, ''); // 이틀 전 날짜

const dailyMovieList = ref([]);
const weeklyMovieList = ref([]);

const fetchBoxOfficeData = async () => {
  const dailyDate = new Date(Date.now() - 86400000).toISOString().slice(0, 10).replace(/-/g, '');
  const weekDate = new Date(Date.now() - 86400000 * 7).toISOString().slice(0, 10).replace(/-/g, '');

  try {
    const dailyResponse = await axios.get('https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json', {
      params: {
        key: import.meta.env.VITE_BOXOFFICE_API_KEY,
        targetDt: dailyDate,
        itemPerPage: 5,
        multiMovieYn: 'N',
      }
    });
    console.log('Daily Response:', dailyResponse.data);
    if (dailyResponse.data?.boxOfficeResult?.dailyBoxOfficeList) {
      dailyMovieList.value = dailyResponse.data.boxOfficeResult.dailyBoxOfficeList;
    } else {
      console.error('Daily box office list not found in response:', dailyResponse.data);
    }

    const weeklyResponse = await axios.get('https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json', {
      params: {
        key: import.meta.env.VITE_BOXOFFICE_API_KEY,
        targetDt: weekDate,
        itemPerPage: 5,
        weekGb: 0,
      }
    });
    console.log('Weekly Response:', weeklyResponse.data);
    if (weeklyResponse.data?.boxOfficeResult?.weeklyBoxOfficeList) {
      weeklyMovieList.value = weeklyResponse.data.boxOfficeResult.weeklyBoxOfficeList;
    } else {
      console.error('Weekly box office list not found in response:', weeklyResponse.data);
    }
  } catch (error) {
    console.error('Error fetching box office data:', error);
  }
};

const emitTopMoviePoster = (index) => {
  if (dailyMovieList.value[index]) {
    // 포스터 이벤트 방출
    this.$emit('top-movie-poster', dailyMovieList.value[index].movieNm);
  }
};

onMounted(() => {
  fetchBoxOfficeData();
});
</script>

<style scoped>
.boxoffice {
  width: 1440px;
  height: 100vh;
  margin: 0 auto;
  padding-top: 50px;
  text-align: center;
  color: white;
}
.contents {
  margin-bottom: 80px;
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
  font-weight: bold;
  font-size: 24px;
  padding-bottom: 20px;
}
.line {
  width: 120px;
  border-bottom: 1px solid white;
}
</style>
