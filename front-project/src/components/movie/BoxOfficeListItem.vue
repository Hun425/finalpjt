<template>
  <div class="movieCard">
    <div class="image-container">
      <img v-if="posterUrl" class="poster" :src="posterUrl" alt="movie_poster">
      <div v-else class="no-poster">포스터 없음</div>
      <div class="overlay">
        <a class="link" :href="`https://m.search.naver.com/search.naver?query=영화+${movie.movieNm}+예매`">
          <button class="info-btn" type="submit">예매하기</button>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { usePosterStore } from '@/stores/poster';

const props = defineProps({
  movie: Object,
});

const store = usePosterStore();
const posterUrl = ref('');

const fetchPosterUrl = async () => {
  if (store.poster[props.movie.movieNm]) {
    posterUrl.value = store.poster[props.movie.movieNm];
  } else {
    await store.fetchPoster(props.movie.movieNm);
    posterUrl.value = store.poster[props.movie.movieNm];
  }
};

onMounted(() => {
  fetchPosterUrl();
});
</script>

<style scoped>
.movieCard {
  margin: 0 auto;
  width: 200px;
  height: 260px;
  border-radius: 10px;
}
.movieCard:hover {
  transform: scale(1.1);
}
a
.poster {
  border-radius: 10px;
  height: 260px;
  width: 200px;
}

.no-poster {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 260px;
  width: 200px;
  background-color: #ccc;
  border-radius: 10px;
  color: #000;
}

.image-container {
  position: relative;
  height: 260px;
  width: 200px;
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
  justify-content: center;
  align-items: center;
}

.image-container:hover img {
  filter: brightness(70%);
}

.image-container:hover .overlay {
  opacity: 1;
}

.info-btn {
  padding: 10px 20px;
  background-color: #fff;
  color: #000;
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
