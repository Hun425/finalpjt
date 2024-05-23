<template>
  <div>
    <div class="list-container">
      <div class="mainText">영화 목록</div>
      <div class="button-group">
        <button @click="showAllMovies" class="styled-button">최신 영화 보기</button>
        <button @click="showNowMovies" class="styled-button">전체 영화 보기</button>
      </div>
      <div>
        <NowMovieList v-if="showAllMoviesList" />
        <MovieList v-else />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import MovieList from '@/components/movie/MovieList.vue';
import NowMovieList from '@/components/movie/NowMovieList.vue';
import { useAccountStore } from '@/stores/account';

const store = useAccountStore();
store.isDark = false;

const showAllMoviesList = ref(true);

const showAllMovies = () => {
  showAllMoviesList.value = true;
};

const showNowMovies = () => {
  showAllMoviesList.value = false;
};
</script>

<style scoped>
.list-container {
  width: 1440px;
  margin: 0 auto;
}

.mainText {
  margin: 30px 0;
  font-weight: bold;
  font-size: 24px;
  text-align: center;
  color: #333;
}

.button-group {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

button.styled-button {
  margin: 0 10px;
  padding: 12px 24px;
  font-size: 16px;
  cursor: pointer;
  background: linear-gradient(135deg, #667eea, #764ba2);
  border: none;
  border-radius: 30px;
  color: white;
  font-weight: bold;
  transition: all 0.4s ease;
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
}

button.styled-button:hover {
  background: linear-gradient(135deg, #764ba2, #667eea);
  transform: translateY(-5px);
  box-shadow: 0 15px 20px rgba(0, 0, 0, 0.15);
}

button.styled-button:active {
  transform: translateY(-2px);
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.1);
}
</style>
