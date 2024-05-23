<script setup>
import { useRouter } from 'vue-router'
import { computed } from 'vue'

const props = defineProps({
  movie: Object,
})

const maxLength = 11
const router = useRouter()

const goToDetail = (movie_pk) => {
  router.push({ name: 'movieDetail', params: { moviepk: movie_pk } })
}

const getImageSource = () => {
  const currentDate = new Date() // 현재 날짜와 시간
  const releaseDate = new Date(props.movie.release_date) // movie의 release_date
  const nextMonthDate = new Date() // 현재 날짜를 복사하여 사용
  nextMonthDate.setMonth(nextMonthDate.getMonth() - 3) // 현재 날짜에 한 달을 더함

  // 현재 날짜와 release_date 비교
  if (releaseDate > currentDate) {
    return 'A' // 현재 날짜 이후인 경우 'A' 이미지의 경로
  } else if (nextMonthDate < releaseDate) {
    return 'B' // 현재 날짜 이전인 경우 'B' 이미지의 경로
  } else {
    return 0
  }
}

const truncatedOverview = computed(() => {
  const overview = props.movie.overview
  const maxLength = 70
  return overview.length > maxLength ? overview.slice(0, maxLength) + '...' : overview
})
</script>

<template>
  <div v-if="movie" class="movieCard">
    <div class="image-container">
      <img @click="goToDetail(movie.pk)" class="poster" :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" :alt="`${movie.title}`" />
      <div class="overlay">
        <div class="overview">{{ truncatedOverview }}</div>
        <div class="rating">평점: {{ movie.vote_average.toFixed(1) }}</div>
      </div>
    </div>
    <div class="movieInfo">
      <div class="title">{{ movie.title.length > maxLength ? movie.title.slice(0, maxLength) + '...' : movie.title }}</div>
      <span v-if="getImageSource() == 'A'" class="day soon">New</span>
      <span v-else-if="getImageSource() == 'B'" class="day hot">Hot</span>
      <span v-else class="day old">R</span>
      <div>개봉일 : {{ movie.release_date }}</div>
    </div>
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
  transition: transform 0.3s ease;
}

.movieCard:hover {
  transform: scale(1.1);
 
}

.image-container {
  position: relative;
  height: 260px;
  width: 200px;

}

.poster {
  border-radius: 10px;
  height: 100%;
  width: 100%;
  transition: filter 0.3s ease;
  cursor: pointer; /* Ensure the cursor indicates the image is clickable */
  border-radius: 10px;
}

.image-container:hover img {
  filter: brightness(70%);
  border-radius: 10px;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none; /* Ensure the overlay does not block mouse events */
  border-radius: 10px;
}

.image-container:hover .overlay {
  opacity: 1;
  border-radius: 10px;
}

.rating {
  font-size: 1.5em;
  font-weight: bold;
}

.overview {
  font-size: 0.9em;
  padding: 10px;
  text-align: center;
}

.movieInfo {
  display: flex;
  position: relative;
  padding: 22px 0px 11px 30px;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-around;
}

.title {
  font-size: 16px;
  font-weight: 600;
}

.day {
  position: absolute;
  top: 20px;
  left: 0px;
  width: 20px;
  height: 20px;
  border-radius: 10%;
  text-align: center;
  font-weight: bold;
  color: white;
}

.soon {
  font-size: 15px;
  padding-top: 1px;
  background-color: rgb(35, 148, 0);
}

.hot {
  padding-top: 3px;
  background-color: rgb(255, 68, 0);
  font-size: 11px;
}

.old {
  padding-top: 3px;
  background-color: rgb(40, 40, 40);
  font-size: 11px;
}
</style>
