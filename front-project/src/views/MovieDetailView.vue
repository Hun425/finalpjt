<template>
  <div>
    <MovieDetailMain v-if="movie" :movie="movie"/>
    <div class="movieDetailInfo" v-if="movie">
      <div class="movieNav">
        <div :class="{navItem: true, focus: isFocus === 1, rest: isFocus !== 1 }" @click="setFocus(1)">주요내용</div>
        <div :class="{navItem: true, focus: isFocus === 2, rest: isFocus !== 2 }" @click="setFocus(2)">관람평</div>
        <div :class="{navItem: true, focus: isFocus === 3, rest: isFocus !== 3 }" @click="setFocus(3)">예고편</div>
      </div>
      <MovieDetailInfo v-show="isFocus === 1" :actors="movie.actors" :overview="movie.overview" />
      <MovieDetailReviewList v-show="isFocus === 2" :moviepk="movie.id" :mvtitle="movie.title"/>
      <MovieDetailTrailer v-show="isFocus === 3" :title="movie.title" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
import { useAccountStore } from '@/stores/account';

import MovieDetailMain from '@/components/movie/MovieDetailMain.vue';
import MovieDetailInfo from '@/components/movie/MovieDetailInfo.vue';
import MovieDetailReviewList from '@/components/movie/MovieDetailReviewList.vue';
import MovieDetailTrailer from '@/components/movie/MovieDetailTrailer.vue';

const store = useAccountStore();
store.isDark = false;

const isFocus = ref(1);
const movie = ref(null);

const route = useRoute();

const fetchMovie = async (movieId) => {
  try {
    const response = await axios.get(`/movies/${movieId}/`);
    movie.value = response.data;
    console.log('Movie data:', movie.value);
  } catch (error) {
    console.error('Error fetching movie data:', error);
  }
};

const setFocus = (focus) => {
  isFocus.value = focus;
};

onMounted(() => {
  const defaultTab = route.query.tab ? parseInt(route.query.tab, 10) : 1;
  isFocus.value = defaultTab;
  fetchMovie(route.params.moviepk);
});

// Watch for changes in the route params
watch(() => route.params.moviepk, (newMoviePk) => {
  fetchMovie(newMoviePk);
});
</script>

<style scoped>
.movieDetailInfo {
  width: 1100px;
  margin: 10px auto;
}

.movieNav {
  display: flex;
  height: 40px;
}

.navItem {
  height: 40px;
  padding: 12px 0 0 0;
  border-color: #3b006e;
  border-style: solid;
  font-weight: bold;
  text-align: center;
  cursor: pointer;
  transition: background-color 0.3s ease, color 0.3s ease; /* 애니메이션 효과 */
}

.navItem:hover {
  background-color: #3b006e;
  color: white;
}

.focus {
  width: 370px;
  border-width: 2px 2px 0px 2px;
}

.rest {
  width: 365px;
  border-width: 0 0 2px 0;
}
</style>
