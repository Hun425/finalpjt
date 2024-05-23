<template>
  <div class="recommend-container">
    <div class="intro">
      <p>매일매일 새로운 영화!</p>
      <p>{{ store.userData.username }} 님, 총 <span>{{ movies.length }}</span> 개의 영화를 추천해드려요.</p>
    </div>
    <div class="carousel-container">
      <button @click="prevSlide" class="carousel-button left-button">&lt;</button>
      <div class="carousel-wrapper">
        <div class="carousel" :style="carouselStyle">
          <div class="carousel-item" v-for="(movie, index) in movies" :key="index">
            <div class="movieCard" @click="goToMovie(movie.id)">
              <div class="image-container">
                <img :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" :alt="movie.title" class="poster">
                <div class="overlay">
                  <div class="overview">{{ truncatedOverview(movie.overview) }}</div>
                  <div class="rating">평점: {{ movie.vote_average.toFixed(1) }}</div>
                </div>
              </div>
              <div class="movieInfo">
                <div class="title">{{ movie.title.length > maxLength ? movie.title.slice(0, maxLength) + '...' : movie.title }}</div>
                <span v-if="getImageSource(movie.release_date) == 'A'" class="day soon">New</span>
                <span v-else-if="getImageSource(movie.release_date) == 'B'" class="day hot">Hot</span>
                <span v-else class="day old">R</span>
                <p class="release-date">개봉일 : {{ movie.release_date }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button @click="nextSlide" class="carousel-button right-button">&gt;</button>
    </div>
    <div class="rest">
      <p>더 많은 리뷰를 보고싶다면?</p>
      <button @click="goToMain">CLICK</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/account'

const store = useAccountStore()
const movies = ref([])
const selectedCard = ref(0)
const slidesToShow = 6 // 한 번에 보여줄 슬라이드 수
const slideWidth = 250 // 각 슬라이드의 너비
const maxLength = 11

const getMovieData = () => {
  axios({
    method: "get",
    url: "http://127.0.0.1:8000/movies/recommended/",
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
  .then(res => {
    movies.value = res.data.results
    console.log(movies.value)
  })
  .catch(err => console.log(err))
}

getMovieData()


const nextSlide = () => {
  if (selectedCard.value + slidesToShow < movies.value.length) {
    selectedCard.value += slidesToShow;
  } else {
    selectedCard.value = 0; // 마지막 슬라이드가 넘칠 경우 처음으로 돌아갑니다.
  }
}

const prevSlide = () => {
  if (selectedCard.value - slidesToShow >= 0) {
    selectedCard.value -= slidesToShow;
  } else {
    selectedCard.value = Math.floor((movies.value.length - 1) / slidesToShow) * slidesToShow; // 마지막 슬라이드가 넘칠 경우 끝으로 돌아갑니다.
  }
}
const carouselStyle = computed(() => {
  const offset = selectedCard.value * -slideWidth;
  console.log('Carousel Style:', offset); // 디버깅 로그
  return {
    transform: `translateX(${offset}px)`,
  };
});

const router = useRouter()
const goToMovie = (movie_pk) => {
  router.push({ name: 'movieDetail', params: { moviepk: movie_pk } })
}
const goToMain = () => {
  router.push({name:'movies'})
}

const getImageSource = (release_date) => {
  const currentDate = new Date()
  const releaseDate = new Date(release_date)
  const nextMonthDate = new Date()
  nextMonthDate.setMonth(nextMonthDate.getMonth() - 3)

  if (releaseDate > currentDate) {
    return 'A'
  } else if (nextMonthDate < releaseDate) {
    return 'B'
  } else {
    return 0
  }
}

const truncatedOverview = (overview) => {
  const maxLength = 100
  return overview.length > maxLength ? overview.slice(0,maxLength) + '...' : overview
}
</script>


<style scoped>
.recommend-container {
  position: relative;
}
.intro {
  margin: 80px 0 60px 0;
  text-align: center;
  font-size: 32px;
  font-weight: bold;
}

.intro span {
  color: blueviolet;
}

.carousel-container {
  display: flex;
  align-items: center;
  position: relative;
  width: 1600px;
  height: 600px;
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

.movieCard {
  display: flex;
  flex-direction: column;
  width: 250px;
  height: 380px;
  border-radius: 10%;
  margin: 0 auto;
  transition: transform 0.3s ease;
}

.image-container {
  position: relative;
  height: 300px;
  width: 250px;
}

.poster {
  border-radius: 10px;
  height: 100%;
  width: 100%;
  transition: filter 0.3s ease;
  cursor: pointer;
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
  pointer-events: none;
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
}

.title {
  margin: 0px;
  font-size: 16px;
  font-weight: 600;
}

.release-date {
  position: absolute;
  top: 50px;
  left: 0px;
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

.rest {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
  text-align: center;
  font-size: 32px;
}

.rest p {
  margin: 50px 0;
  font-size: 36px;
  font-weight: bold;
}

.rest button {
  padding: 20px 50px;
  background-color: rgb(255, 255, 255);
  color: blueviolet;
  border: 2px solid blueviolet;
  border-radius: 30px;
  cursor: pointer;
  transition: 0.5s;
}
.rest button:hover {
  background-color: blueviolet;
  color: rgb(255, 255, 255);
}
</style>
