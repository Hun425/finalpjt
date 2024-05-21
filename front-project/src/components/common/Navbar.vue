<template>
  <div :class="{dark:isDark}">
    <header>
      <div class="userbar" v-if="!store.isLogin">
        <span @click="goToLogin">Login</span>|
        <span @click="goToSignup">Signup</span>
      </div>
      <div v-else>
        <span @click="store.logOut">Logout</span>
      </div>

      <div class="navbar">
        <div class="nav">
          <div  @click="goToMovie">영화</div>
          <div >이벤트</div>
        </div>
        <div class="logotext" @click="goToHome">MOVIE CINEMA</div>
        <div class="nav">
          <div >커뮤니티</div>
          <div @click="goToMypage">마이페이지</div>
        </div>
      </div>
    </header>
  </div>
</template>

<script setup>
  import { RouterLink, RouterView, useRouter, useRoute} from 'vue-router'
  import { useAccountStore } from '@/stores/account';
  import {ref} from 'vue'

  const store = useAccountStore()
  const router = useRouter()
  const route = useRoute()
  const isDark = ref(true)

  // PageList

  // 1) 로그인 페이지 => accounts.js에서 사용
  const goToLogin = function () {
    isDark.value = false
    store.goToLogin()
  }

  // 2) 회원가입 페이지
  const goToSignup = function () {
    isDark.value = false
    router.push({name:'signup'})
  }

  // 3) 로그아웃 => accounts Store에서 처리
  const goTologOut = function () {
    isDark.value = false
    store.logOut()
  }

  /// ----------------------------------- ///

  // 4) home 페이지 (Logo)
  const goToHome = function () {
    isDark.value = true
    router.push({name:'home'})
  }

  // 5) 영화 페이지
  const goToMovie = function () {
    isDark.value = false
    router.push({name:'movies'})
  }

  // 6) 커뮤니티 페이지

  // 7) 마이페이지 (수정필요!)
  const goToMypage = function () {
    if (store.isLogin ) {
      console.log(route.params)
      // router.push({name:'profile',params:{route.}})
    } else {
      router.push({name:'login'})
    }
  }

</script>

<style scoped>
  .dark {
    background-color: black;
    color:white;
  }
  header {
    width: 1440px;
    height:100px;
    margin: 0 auto;
   
  }

  .userbar {
    padding:10px 30px;
    /* text-align: end; */
  }
  .navbar {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    width: 1440px;
    height : 50px;
    margin: 0px auto ;
    font-size: 20px;
    font-weight:bold;
    text-align: center;
  }

  .nav {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    margin-top: auto;
  }

  .logotext {
    font-size: 30px;
  }
</style>
