import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import MovieListView from "../views/MovieListView.vue";
import LoginView from "../views/LoginView.vue";
import SignupView from "../views/SignupView.vue";
import MovieDetailView from "../views/MovieDetailView.vue";
import ProfileView from "@/views/ProfileView.vue";
import MovieRecommendation from '../views/AutoRecommend.vue';
// import View from '../views/View.vue'
import {  useAccountStore  } from '@/stores/account'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/movies",
      name: "movies",
      component: MovieListView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignupView,
    }, 
    {
      path: "/:moviepk",
      name: "movieDetail",
      component: MovieDetailView,
    },
    {
      path: '/profile/:userpk',
      name: 'profile',
      component: ProfileView
    },
    { // 영화 검색 기능 페이지 
      path: '/gpt/recommend',
      name: 'MovieRecommendation',
      component: MovieRecommendation,
    },
    // {
    //   path: '/',
    //   name: '',
    //   component: 
    // },
  ],
});



// 페이지별로 접근을 제한하고 싶은 페이지 설정하기!!
// router.beforeEach((to, from) => {
//   const store = useAccountStore()
//   if (to.name === 'ReviewView' && store.isLogin) {
//     window.alert('로그인이 필요합니다.')
//     return {name: 'LoginView'}
//   }
//   if (to.name === 'SignupView' && store.isLogin) {
//     window.alert('이미 로그인이 되어있습니다.')
//     return {name: 'movies'}
//   }
// })

export default router;
