<template>
  <div :class="{ 'has-background-black has-text-white': isDark, 'has-background-white has-text-black': !isDark }">
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
          <a v-if="!store.isLogin" class="navbar-item" @click="goToLogin">로그인/회원가입</a>
          <a v-else class="navbar-item" @click="goToLogout">로그아웃</a>
          <a class="navbar-item" @click="goToMypage">마이페이지</a>
        </div>
      </div>
    </nav>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useAccountStore } from '@/stores/account';

const store = useAccountStore();
const router = useRouter();
const route = useRoute();
const isDark = computed(() => store.isDark);

const burgerActive = ref(false);
const toggleBurger = () => {
  burgerActive.value = !burgerActive.value;
};

// 페이지 이동 함수들 
const goToLogin = () => {
  store.isDark = false;
  store.goToLogin();
};

const goToSignup = () => {
  store.isDark = false;
  router.push({ name: 'account' });
};

const goToLogout = () => {
  store.isDark = false;
  store.logOut();
};

const goToHome = () => {
  store.isDark = true;
  router.push({ name: 'home' });
};

const goToMovie = () => {
  store.isDark = false;
  router.push({ name: 'movies' });
};

const goToMypage = () => {
  if (store.isLogin) {
    store.isDark = false;
    router.push({ name: 'profile', params: { userpk: store.userData.pk } });
  } else {
    router.push({ name: 'account' });
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
</style>
