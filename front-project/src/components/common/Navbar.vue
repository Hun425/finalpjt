<template>
  <div
    :class="{ 'has-background-black has-text-white': isDark, 'has-background-white has-text-black': !isDark }"
  >
    <nav class="navbar is-dark custom-navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item logotext" @click="goToHome">MOVIE CINEMA</a>
        <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" @click="toggleBurger">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div :class="{'navbar-menu': true, 'is-active': burgerActive}" style="padding:15px">
        <div class="navbar-start">
          <a class="navbar-item" @click="goToMovie">영화</a>
          <a class="navbar-item">추천</a>
          <a class="navbar-item">커뮤니티</a>
        </div>
        <div class="navbar-end">
          <a class="navbar-item" @click="toggleSearchBar" id="search-bar">
            영화 검색
          </a>
          <a v-if="!store.isLogin" class="navbar-item" @click="goToLogin">로그인/회원가입</a>
          <a v-else class="navbar-item" @click="goToLogout">로그아웃</a>
          <a class="navbar-item" @click="goToMypage">마이페이지</a>
        </div>
      </div>
    </nav>

    <div id="search-bar" v-show="isSearchBarVisible" class="search-bar">
      <input
        type="text"
        v-model="searchQuery"
        @compositionupdate="handleInput"
        @compositionend="onCompositionEnd"
        @input="handleInput"
        placeholder="영화 제목을 입력하세요."
        class="input"
     
      />
      <div id="search-results" class="search-results">
        <div v-for="movie in searchResults" :key="movie.pk" @click="goToMovieDetail(movie.pk)" class="search-result-item">
          {{ movie.title }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';
import { useRouter } from 'vue-router';
import { useAccountStore } from '@/stores/account';
import * as Hangul from 'es-hangul';

const store = useAccountStore();
const router = useRouter();
const isDark = computed(() => store.isDark);

const burgerActive = ref(false);
const toggleBurger = () => {
  burgerActive.value = !burgerActive.value;
};

// 검색 기능을 위한 상태 변수와 함수들
const searchQuery = ref('');
const searchResults = ref([]);
const isSearchBarVisible = ref(false);
const isComposing = ref(false);

const toggleSearchBar = () => {
  isSearchBarVisible.value = !isSearchBarVisible.value;
  console.log('Search bar toggled, isSearchBarVisible:', isSearchBarVisible.value); // 디버그 메시지
  if (!isSearchBarVisible.value) {
    searchQuery.value = '';
    searchResults.value = [];
  }
};

const closeSearchBar = () => {
  isSearchBarVisible.value = false;
  searchQuery.value = '';
  searchResults.value = [];
};

const searchMovies = async (query) => {
  try {
    const encodedQuery = encodeURIComponent(query);
    const response = await fetch(`http://127.0.0.1:8000/movies/gpt/search/?movie_name=${encodedQuery}`, {
      headers: {
        'Accept': 'application/json'
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log('Received search results:', data);
    searchResults.value = data.similar_movies || [];
  } catch (error) {
    console.error('Error fetching search results:', error);
    searchResults.value = [];
  }
};

// 검색어 입력 처리 함수
const handleInput = (event) => {
  const inputValue = event.target.value;
  
};

const onCompositionEnd = () => {
  isComposing.value = false;
  searchMovies(searchQuery.value);
};

const goToMovieDetail = (moviepk) => {
  console.log('Navigating to movie detail with id:', moviepk);
    // 검색창 닫기
  goToMovie();
  closeSearchBar();
  router.push({ name: 'movieDetail', params: { moviepk } });
  
};

// 페이지 이동 함수들 
const goToLogin = () => {
  store.isDark = false;
  closeSearchBar();
  store.goToLogin();
  
};

const goToSignup = () => {
  store.isDark = false;
  closeSearchBar();
  router.push({ name: 'account' });
};

const goToLogout = () => {
  store.isDark = false;
  closeSearchBar();
  store.logOut();
};

const goToHome = () => {
  store.isDark = true;
  closeSearchBar();
  router.push({ name: 'home' });
};

const goToMovie = () => {
  store.isDark = false;
  closeSearchBar();
  router.push({ name: 'movies' });
};

const goToMypage = () => {
  closeSearchBar();
  if (store.isLogin) {
    store.isDark = false;
    router.push({ name: 'profile', params: { userpk: store.userData.pk } });
  } else {
    router.push({ name: 'account' });
  }
};

// 클릭 이벤트 리스너 추가 및 제거
const handleClickOutside = (event) => {
  if (!event.target.closest('#search-bar')) {
    closeSearchBar();
  }
};


</script>

<style scoped>
.navbar-item {
  font-size: 1.2rem;
}
.logotext {
  font-size: 2.5rem;
  font-weight: bold;
}
.custom-navbar {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.custom-navbar .navbar-item {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}
.navbar-item:hover {
  background-color: #444; /* 배경 색 변경 */
  color: #fff; /* 글자 색 변경 */
  transition: background-color 0.3s ease, color 0.3s ease; /* 부드러운 전환 효과 */
}
.navbar {
  background-color: #222;
}

.navbar-burger {
  display: none;
}

@media (max-width: 1024px) {
  .navbar-burger {
    display: block;
  }

  .navbar-menu.is-active {
    display: block;
  }
}

.navbar-end .navbar-item {
  display: flex;
  align-items: center;
}

.section.is-fullwidth {
  width: 100%;
  padding-left: 0;
  padding-right: 0;
}

.container.is-fluid {
  width: 100%;
  max-width: 100%;
  padding-left: 0;
  padding-right: 0;
}

.search-bar {
  position: absolute;
  top: 60px;
  right: 20px;
  background-color: white;
  border: 1px solid #ccc;
  padding: 10px;
  width: 300px;
  z-index: 1000;
}

.search-bar .input {
  width: 100%;
  padding: 5px;
  margin-bottom: 10px;
  z-index: 10;
}

.search-results {
  max-height: 200px;
  overflow-y: auto;
  color: black;
  z-index: 10;
}

.search-result-item {
  padding: 5px;
  cursor: pointer;
}

.search-result-item:hover {
  background-color: #f0f0f0;
}
</style>
