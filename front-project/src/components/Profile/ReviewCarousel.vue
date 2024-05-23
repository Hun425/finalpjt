<template>
  <div v-if="props.reviews.length === 0" class="no-review">
    <p>작성한 리뷰가 없습니다. 리뷰를 작성해주세요!</p>
  </div>
  <div v-else class="carousel-container">
    <button @click="prevSlide" class="carousel-button left-button">&lt;</button>
    <div class="carousel-wrapper">
      <div class="carousel" :style="carouselStyle">
        <div class="carousel-item" v-for="(review, index) in props.reviews" :key="index">
          <div @click="goToMovieDetail(review.movie.pk)" class="review-card">
            <img :src="'https://image.tmdb.org/t/p/w500/' + review.movie.poster_path" :alt="review.movie.title" class="movie-poster">
            <p class="movie-title">{{ review.title }}</p>
          </div>
        </div>
      </div>
    </div>
    <button @click="nextSlide" class="carousel-button right-button">&gt;</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const props = defineProps({
  reviews: {
    type: Array,
    required: true,
  },
});

const currentSlide = ref(0);

const totalSlides = computed(() => {
  return Math.ceil(props.reviews.length / 6);
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

const goToMovieDetail = (moviepk) => {
  router.push({ name: 'movieDetail', params: { moviepk: moviepk } });
};
</script>

<style scoped>
.no-review {
  height: 150px;
  display: flex;
  flex-direction: column;
  justify-content:space-around;
  align-items: center;
  font-size: 24px;  
}

.carousel-container {
  display: flex;
  align-items: center;
  position: relative;
  width: 1200px; /* 고정된 너비 설정 */
  height: 300px; /* 260px (포스터 높이) + 16px (제목 높이) + 10px */
  margin: 0 auto; /* 좌우 마진 자동으로 가운데 정렬 */
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.carousel-wrapper {
  overflow: hidden;
  width: calc(100% - 60px); /* To account for the buttons */
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

.review-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.movie-poster {
  max-width: 200px;
  max-height: 260px;
  border-radius: 10px;
  object-fit: cover;
}

.movie-title {
  margin-top: 10px;
  font-size: 16px;
  text-align: center;
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
