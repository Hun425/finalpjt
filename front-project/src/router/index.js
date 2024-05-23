import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import MovieListView from "../views/MovieListView.vue";
// import LoginView from "../views/LoginView.vue";
// import SignupView from "../views/SignupView.vue";
import AccountView from "../views/AccountView.vue"
import MovieDetailView from "../views/MovieDetailView.vue";
import ProfileView from "@/views/ProfileView.vue";
import MovieRecommendation from '../views/AutoRecommend.vue';
// import View from '../views/View.vue'
import {  useAccountStore  } from '@/stores/account'
import CommmunityView from "@/views/CommmunityView.vue";
import BasicRecommendView from '@/views/BasicRecommendView.vue'
import axios from "axios";
import Swal from "sweetalert2";

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
      path: '/account',
      name: 'account',
      component: AccountView
    },
    // {
    //   path: "/login",
    //   name: "login",
    //   component: LoginView,
    // },
    // {
    //   path: "/signup",
    //   name: "signup",
    //   component: SignupView,
    // }, 
    {
      path: "/movies/:moviepk",
      name: "movieDetail",
      component: MovieDetailView,
      beforeEnter: async (to, from, next) => {
        const store = useAccountStore();
        try {
          // 사용자 정보를 가져옵니다
   
          const user = store.userData
          
          if (user.age=="" || !user) {
            Swal.fire({
              title: '접근 불가',
              text: '로그인이 필요합니다.',
              icon: 'warning',
              confirmButtonText: '확인',
              scrollbarPadding: false ,
            });
            return ({name:'account'})
          }
  
          const userAge = user.age;
          const movieId = to.params.moviepk;
  
          // 영화 정보를 API로 가져옵니다
          const response = await axios.get(`/movies/${movieId}`);
          const movieAgeRating = response.data.certification;
          console.log(movieAgeRating)
          if (!isAgeAppropriate(userAge, movieAgeRating)) {
            Swal.fire({
              title: '접근 불가',
              text: '이 영화는 나이 등급 제한으로 인해 볼 수 없습니다.',
              icon: 'warning',
              confirmButtonText: '확인',
              scrollbarPadding: false ,
            });
            return next(false); // 접근을 막습니다
          } else {
            return next(); // 접근을 허용합니다
          }
        } catch (error) {
          console.error('Error fetching movie data:', error);
          return next(false); // 오류가 발생하면 접근을 막습니다
        }
      }
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
    {
      path: '/community',
      name: 'community',
      component: CommmunityView
    },
    {
      path: '/BasicRecommend',
      name: 'basicRecommend',
      component: BasicRecommendView
    },
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


function isAgeAppropriate(userAge, movieAgeRating) {
  const ageRatings = {
    'ALL': 0,
    '12': 12,
    '15': 15,
    '18': 18,
  };
  
  // 영화 나이 등급이 ageRatings에 존재하지 않으면 무조건 true 반환
  if (!(movieAgeRating in ageRatings)) {
    return true;
  }
  
  return userAge >= ageRatings[movieAgeRating];
}
export default router;
