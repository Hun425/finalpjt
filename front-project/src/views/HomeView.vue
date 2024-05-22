<script setup>
  import BoxOfficeList from '@/components/movie/BoxOfficeList.vue';
  import Navbar from '@/components/common/Navbar.vue'

  import { useAccountStore } from '@/stores/account';
  const store = useAccountStore()
  store.isDark = true
</script>

<template>
  <div class="main-container">
    <div :style="backgroundStyle" class="background-image"></div>
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
  filter: 'blur(8px)',
  height: '100%',
  width: '100%',
  position: 'absolute',
  top: 0,
  left: 0,
  zIndex: -1,
  opacity: 0.5
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
    console.log('Daily Response:', response.data);
    if (response.data.boxOfficeResult.dailyBoxOfficeList.length > 0) {
      const topMovie = response.data.boxOfficeResult.dailyBoxOfficeList[0];

      const movieResponse = await axios.get('/movies/gpt/search/', {
        params: { movie_name: topMovie.movieNm },
      });
      console.log('Movie Response:', movieResponse.data);
      if (movieResponse.data.similar_movies && movieResponse.data.similar_movies.length > 0) {
        const topMovieData = movieResponse.data.similar_movies[0];
        console.log('Backdrop Path:', topMovieData.backdrop_path);
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
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  filter: blur(12px);
  opacity: 0.5;
}

.overlay {
  position: relative;
  z-index: 1;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7); /* 어두운 오버레이 */
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
    rgba(0, 0, 0, 0.5) 50%, 
    rgba(0, 0, 0, 0) 100%
  );
  z-index: -1;
}
</style>
