<template>
    <div class="movie-container">
      <div class="movieList">
        <MovieListItem v-for="movie in movieList" :key="movie.title" :movie="movie" />
      </div>
      <div class="pagination">
        <div>
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

  const store = useAccountStore()
  const movieList = ref([])
  const currentPage = ref(1)
  const totalPages = ref(1)
  const showingNow = "1" // showing_now 상태를 저장하는 변수
  
  const fetchMovies = (page = 1) => {
    if (store.isLogin) {
    axios.get('/movies/', { headers:{Authorization:`Token ${store.token}`}, params: { page, showing_now: "1"} })
      .then(res => {
        movieList.value = res.data.results
        totalPages.value = Math.ceil(res.data.count / 20)
        currentPage.value = page
      })
      .catch(err => console.log(err))
  } else {
    axios.get('/movies/', { params: { page, showing_now: "1"} })
      .then(res => {
        movieList.value = res.data.results
        totalPages.value = Math.ceil(res.data.count / 20)
        currentPage.value = page
      })
      .catch(err => console.log(err))
  }}


//   const fetchMovies = (page = 1) => {
//   if (store.isLogin) {
//     axios.get('/movies/', {headers:{Authorization:`Token ${store.token}`}, params: { page } })
//     .then(res => {
//       movieList.value = res.data.results
//       totalPages.value = Math.ceil(res.data.count / 20)
//       currentPage.value = page
//     })
//     .catch(err => console.log(err))
//   } else {
//     axios.get('/movies/', { params: { page } })
//     .then(res => {
//       movieList.value = res.data.results
//       totalPages.value = Math.ceil(res.data.count / 20)
//       currentPage.value = page
//     })
//     .catch(err => console.log(err))
//   }
// }
  
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
  
  // showing_now 상태를 변경하는 함수
  const toggleShowingNow = () => {
    showingNow.value = !showingNow.value
    fetchMovies()  // 상태 변경 후 영화 목록 다시 로드
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
  margin: 20px auto;
  display: flex;
  justify-content: center; /* 중앙 정렬 */
  align-items: center; /* 수직 중앙 정렬 */
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
  