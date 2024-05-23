<template>
  <div v-if="props.movies.length === 0" class="no-movie">
    <p>선택한 영화가 없습니다. 관심있는 영화를 선택해주세요!</p>
    <button @click="goToMovies" class="move-btn">Select Movie</button>
  </div>
  <div v-else class="carousel-container">
    <button @click="prevSlide" class="carousel-button left-button">&lt;</button>
    <div class="carousel-wrapper">
      <div class="carousel" :style="carouselStyle">
        <div class="carousel-item" v-for="(movie, index) in props.movies" :key="index">
          <div class="movie-card" @click="goToMovieDetail(movie.id)">
            <img :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" :alt="movie.title" class="movie-poster">
          </div>
        </div>
      </div>
    </div>
    <button @click="nextSlide" class="carousel-button right-button">&gt;</button>
  </div>
</template>

<script setup>
import router from '@/router';
import { ref, computed } from 'vue';

const props = defineProps({
  movies: {
    type: Array,
    required: true,
  },
});

const currentSlide = ref(0);

const totalSlides = computed(() => {
  return Math.ceil(props.movies.length / 6);
});

const carouselStyle = computed(() => {
  return {
    transform: `translateX(-${currentSlide.value * 100}%)`,
  };
});

const prevSlide = () => {
  if (currentSlide.value > 0) {
    currentSlide.value -= 1;
  }
};

const nextSlide = () => {
  if (currentSlide.value < totalSlides.value - 1) {
    currentSlide.value += 1;
  }
};

const goToMovies = () => {
  router.push({ name: 'movies' });
};

const goToMovieDetail = (moviepk) => {
  router.push({ name: 'movieDetail', params: { moviepk: moviepk } });
};
</script>

<style scoped>
.no-movie {
  height: 150px;
  display: flex;
  flex-direction: column;
  justify-content:space-around;
  align-items: center;
  font-size: 24px;  
}
.move-btn {
  all: unset;
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: 0.5s;
}
.move-btn:hover {
  background-color: blueviolet;
  color: white;
}
.carousel-container {
  display: flex;
  align-items: center;
  position: relative;
  width: 1200px;
  height: 286px;
  margin: 0 auto;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.carousel-wrapper {
  overflow: hidden;
  width: calc(100% - 60px);
}

.carousel {
  display: flex;
  transition: transform 0.5s ease;
}

.carousel-item {
  min-width: calc(100% / 6);
  box-sizing: border-box;
  padding: 10px;
}

.movie-card {
  display: flex;
  align-items: center;
  justify-content: center;
}

.movie-poster {
  max-width: 200px;
  max-height: 260px;
  border-radius: 10px;
  object-fit: cover;
}

.carousel-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  border: none;
  border-radius: 10px;
  padding: 10px;
  cursor: pointer;
  z-index: 10;
  transition: 0.5s;
}

.carousel-button:hover {
  background-color: rgba(180, 52, 255, 0.7);
}

.left-button {
  left: 0;
}

.right-button {
  right: 0;
}


</style>
