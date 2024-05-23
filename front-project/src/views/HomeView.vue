<template>
  <div class="main-container main-movie">
    <div :style="backgroundStyle" class="background-image bg"></div>
    <div class="bg-pattern"></div>
    <div class="overlay">
      <BoxOfficeList />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import BoxOfficeList from '@/components/movie/BoxOfficeList.vue';
import { usePosterStore } from '@/stores/poster';

const posterStore = usePosterStore();
const topMoviePoster = ref('');

const backgroundStyle = computed(() => ({
  backgroundImage: `url(${topMoviePoster.value})`,
  backgroundSize: 'cover',
  backgroundPosition: 'center',
  backgroundRepeat: 'no-repeat',
  backgroundAttachment: 'scroll',
  height: '100%',
  width: '100%',
  position: 'absolute',
  top: 0,
  left: 0,
}));

const fetchTopMovieBackdrop = async () => {
  try {
    const dailyDate = new Date(Date.now() - 86400000).toISOString().slice(0, 10).replace(/-/g, '');
    const response = await axios.get('https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json', {
      params: {
        key: import.meta.env.VITE_BOXOFFICE_API_KEY,
        targetDt: dailyDate,
        itemPerPage: 1,
      },
    });
    if (response.data.boxOfficeResult.dailyBoxOfficeList.length > 0) {
      const topMovie = response.data.boxOfficeResult.dailyBoxOfficeList[0];

      const movieResponse = await axios.get('/movies/gpt/search/', {
        params: { movie_name: topMovie.movieNm },
      });
      if (movieResponse.data.similar_movies && movieResponse.data.similar_movies.length > 0) {
        const topMovieData = movieResponse.data.similar_movies[0];
        topMoviePoster.value = `https://image.tmdb.org/t/p/w1280${topMovieData.backdrop_path}`;
       
      }
    }
  } catch (error) {
    console.error('Error fetching top movie backdrop:', error);
  }
};

onMounted(() => {
  fetchTopMovieBackdrop();
});
</script>

<style scoped>
.main-container {
  display: block;
  position: relative;
  min-height: 880px;
  padding: 0 0 0px 0;
}

.background-image {
  overflow: hidden;
  position: absolute;
  z-index: 1;
  width: 100%;
  min-width: 1100px;
  height: 100%;
  margin: 0 auto;
  background-attachment: scroll;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;

}

.background-image:before {
  content: '';
  display: block;
  position: absolute;
  left: 0;
  top: 0;
  z-index: 2;
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, rgba(85, 63, 5, 1) 0%, rgba(23, 17, 1, 0) 50%, rgba(85, 63, 5, 1) 100%);
}

.background-image:after {
  content: '';
  display: block;
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  z-index: 2;
  background-color: rgba(3, 1, 21, 0.7);
}

.bg-pattern {
  position: absolute;
  left: 0;
  top: 0;
  z-index: 3;
  width: 100%;
  height: 100%;
  background: url('https://www.megabox.co.kr/static/pc/images/movie/bg-movie-detail-pattern.png') repeat 0 0;
}

.overlay {
  position: relative;
  z-index: 4; /* z-index를 높여서 BoxOfficeList가 보이게 함 */
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6); /* 어두운 오버레이 */
  display: flex;
  align-items: center;
  justify-content: center;
}

.overlay::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    rgba(0, 0, 0, 0) 0%, 
    rgba(0, 0, 0, 0.2) 50%, 
    rgba(0, 0, 0, 0) 100%
  );
  z-index: -1;
}

/* BoxOfficeList의 스타일 및 호버 효과 */
.box-office-item {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.box-office-item:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}
</style>
