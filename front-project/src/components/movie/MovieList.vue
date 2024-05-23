<template>
  <div>
    <div class="movieList">
    <MovieListItem v-for="movie in movieList" :key="movie.title" :movie="movie" />
    </div>
    <div class="pagination">
      <div>
        <button @click="changePage(currentPage - 5)" :disabled="currentPage <= 5"> < </button>
        <button button v-for="page in pagesToShow" :key="page" @click="changePage(page)" :disabled="page === currentPage">{{ page }}</button>
        <button @click="changePage(currentPage + 5)" :disabled="currentPage > totalPages - 5"> > </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import MovieListItem from './MovieListItem.vue'

const movieList = ref([])
const currentPage = ref(1)
const totalPages = ref(1)

const fetchMovies = (page = 1) => {
  axios.get('/movies/', { params: { page } })
    .then(res => {
      movieList.value = res.data.results
      totalPages.value = Math.ceil(res.data.count / 20)
      currentPage.value = page
    })
    .catch(err => console.log(err))
}

const pagesToShow = computed(() => {
  const startPage = Math.floor((currentPage.value - 1) / 5) * 5 + 1
  return Array.from({ length: 5 }, (v, k) => k + startPage).filter(page => page <= totalPages.value)
})

const changePage = (page) => {
  if (page > 0 && page <= totalPages.value) {
    fetchMovies(page)
    window.scrollTo({ top: 0 })  // 이 부분에서 부드럽게 이동하고싶다면 hehavior:'smooth'
  }
}

// 초기 데이터 로드
fetchMovies()
</script>

<style>
.movieList {
  width: 1100px;
  margin: 30px auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}

  .pagination {
    position:inline;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    justify-content:space-between;
    align-items:flex-end;
  }

  .pagination button {
    all:unset;
    margin: 0 5px;
    padding: 10px;
  }
</style>