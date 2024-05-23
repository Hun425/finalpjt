<script setup>
import { useRouter } from 'vue-router'
import { ref, computed } from 'vue'

const props = defineProps({
  movie: Object,
})

const maxLength = 11
const router = useRouter()

const goToDetail = (movie_pk) => {
  router.push({ name: 'movieDetail', params: { moviepk: movie_pk } })
}
const age = ref(0)
const getSource = () => {
  const certification = props.movie.certification; // movie의 certification
    if (certification == null) {
      age.value = "N" 
    } else if  (certification.includes('12')) {
      age.value = '12'
    } else if (certification.includes('15')) {
      age.value = '15'
    } else if (certification.includes('18') || certification.includes('청소년')) {
      age.value = '18'
    } else if (certification.includes('A') || certification.includes('전체')) {
      age.value = 'All'
    } else {
      age.value = 'N'
    }}
getSource()

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
      <span class="day" :class="{ 'soon': age < 12, 'two': age == 12, 'eight': age == 18, 'all': age == 'all', 'five': age !== '12' && age !== '18' && age !== 'all' }">{{ age }}</span>

      <p class="release-date">개봉일 : {{ movie.release_date }}</p>
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
  /* align-items: flex-start; */
  /* justify-content: space-around; */
}

.title {
  margin: 0px;
  font-size: 16px;
  font-weight: 600;
}
.release-date {
  position: absolute;
  top:50px;
  left:0px;
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

.five {
  font-size: 15px;
  padding-top: 1px;
  background-color: rgb(250, 137, 0);
}

.eight {
  padding-top: 3px;
  background-color: rgb(255, 68, 0);
  font-size: 11px;
}

.two {
  padding-top: 3px;
  background-color: rgb(253, 218, 75);
  font-size: 11px;
}
.all{
  padding-top: 3px;
  background-color: rgb(68, 123, 0);
  font-size: 11px;
}
</style>
