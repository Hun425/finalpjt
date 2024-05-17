<template>
  <div :class="{Dark:isDark}">
    <header class="content">
      <div><span :class="{Dark:isDark}" @click="goToLogin">Login</span>|<span :class="{Dark:isDark}" @click="goToSignup">Signup</span></div>
      <nav class="navbar">
          <span class="nav" :class="{Dark:isDark}" @click="goToMovie">영화</span>
          <span class="nav">이벤트</span>
        <div class="logotext">MOVIE CINEMA</div>
          <span class="nav" :class="{Dark:isDark}">커뮤니티</span>|
          <span class="nav" :class="{Dark:isDark}">마이페이지</span>
      </nav>
    </header>
    <hr>
    <div class="content">
      <RouterView/>
    </div>
  </div>
</template>

<script setup>
  import {RouterLink, RouterView, useRouter} from 'vue-router'
  import {ref} from 'vue'

  const router = useRouter()
  const isDark = ref(true)


  // 1) 페이지 렌더링 목록
    // 영화 페이지
  const goToMovie = function () {
    isDark.value = false
    router.push({name:'movies'})
  }
    // 로그인 페이지
  const goToLogin = function () {
    isDark.value = false
    router.push({name:'login'})
  }
    // 회원가입 페이지
  const goToSignup = function () {
    isDark.value = false
    router.push({name:'signup'})
  }


</script>

<style scoped>
  .content {
    width: 1440px;
    margin: 0 auto;
  }

  .Dark {
    /* background-color: black;
    color: white; */
  }

  .navbar {
    display: flex;
    justify-content: space-between;
    width: 1440px;
    margin: 0px auto ;
    font-size: 20px;
  }

  .nav {
    width: 100px;
    text-align:center;
  }
  .logo {
    width:700px
  }
  .logotext {
    width: 1100px;
    text-align: center;
    font-weight: bold;
    font-size: 30px;
  }
</style>
