
<template>
  <div  class="minheight" :class="[, {Dark:isDark}]">
    <header >
      <div>
        <span @click="goToLogin" :class="{Dark:isDark}">LOGIN</span><span @click="goToSignup" :class="{Dark:isDark}">SIGNUP</span>
      </div>
      <div>
      </div>
      <nav class="navbar">
        <div>
          <span @click="goToMovies" :class="{Dark:isDark}">영화</span>|
          <span :class="{Dark:isDark}">이벤트</span>
        </div>
        <div class="logo">
          <p class="logotext">Logo</p>
        </div>
        <div>
          <span :class="{Dark:isDark}">커뮤니티</span>|
          <span :class="{Dark:isDark}">마이페이지</span>
        </div>
      </nav>
    </header>
    <div>
      <RouterView />
    </div>
  </div>
</template>

<script setup>
 import {RouterLink, RouterView, useRouter} from 'vue-router'
 import {ref} from 'vue'

 const router = useRouter()
 const isDark = ref(true)

// 라우터별 이동함수
 const goToMovies = function () {
  isDark.value = false
  router.push({name:'movies'})
 }

 const goToLogin = function () {
  isDark.value = false
  router.push({name:'login'})
 }

 const goToSignup = function () {
  isDark.value = false
  router.push({name:'signup'})
 }

</script>


<style scoped>
  .minheight {
    min-height: 1440px;
  }
  .Dark {
    background-color: black;
    color:white;
  }
  .navbar {
    display: flex;
    justify-content: space-between;
    width: 1440px;
    margin: 0px auto ;
    color:white;
    font-size: 20px;
  }
  .logo {
    width:700px
  }
  .logotext {
    text-align: center;
  }
</style>
