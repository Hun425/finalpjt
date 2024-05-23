<template>
  <div class="movie-container" id="item">
    <div class="movieList">
      <MovieListItem v-for="movie in movieList" :key="movie.title" :movie="movie" />
    </div>
    <div class="pagination">
      <div class="clickbar">
        <button @click="changePage(currentPage - 5)" :disabled="currentPage <= 5"> < </button>
        <button v-for="page in pagesToShow" :key="page" @click="changePage(page)" :disabled="page === currentPage">{{ page }}</button>
        <button @click="changePage(currentPage + 5)" :disabled="currentPage > totalPages - 5"> > </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import MovieListItem from './MovieListItem.vue'
import { useAccountStore } from '@/stores/account';
// import { useUserStore } from '@/stores/userStore';

const movieList = ref([])
const currentPage = ref(1)
const totalPages = ref(1)
const store = useAccountStore()

const fetchMovies = (page = 1) => {
  if (store.isLogin) {
    axios.get('/movies/', {headers:{Authorization:`Token ${store.token}`}, params: { page } })
    .then(res => {
      movieList.value = res.data.results
      totalPages.value = Math.ceil(res.data.count / 20)
      currentPage.value = page
    })
    .catch(err => console.log(err))
  } else {
    axios.get('/movies/', { params: { page } })
    .then(res => {
      movieList.value = res.data.results
      totalPages.value = Math.ceil(res.data.count / 20)
      currentPage.value = page
    })
    .catch(err => console.log(err))
  }
}

const pagesToShow = computed(() => {
  const startPage = Math.floor((currentPage.value - 1) / 5) * 5 + 1
  return Array.from({ length: 5 }, (v, k) => k + startPage).filter(page => page <= totalPages.value)
})

const changePage = (page) => {
  if (page > 0 && page <= totalPages.value) {
    fetchMovies(page)
    window.scrollTo({ top: 0, behavior: 'smooth' })  // 부드럽게 스크롤 이동
  }
}

// 초기 데이터 로드
fetchMovies()
</script>

<style>
.movie-container {
  display: flex;
  margin-bottom: 50px;
  flex-direction: column;
  justify-content: center; /* 중앙 정렬 */
  align-items: center; /* 수직 중앙 정렬 */
}
.movieList {
  width: 1100px;
  margin: 30px auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}

.pagination {
  margin:20px auto;
  display: flex;
  justify-content: center; /* 중앙 정렬 */
  align-items: center; /* 수직 중앙 정렬 */
}

.clickbar {
  display: inline-block;
  width:300px;
}

.pagination button {
  all: unset;
  margin: 0 5px;
  padding: 10px;
  background-color: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.pagination button:hover {
  background-color: #ddd;
}

.pagination button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}
</style>
