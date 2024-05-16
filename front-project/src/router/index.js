import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieListView from '../views/MovieListView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'

// import View from '../views/View.vue'




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/movies',
      name: 'movies',
      component: MovieListView
    },
        {
      path: '/login',
      name: 'login',
      component: LoginView
    },
        {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/:movieId',
      name: 'movieDetail',
      component: MovieDetailView
    },
    //     {
    //   path: '/',
    //   name: '',
    //   component: () => import('../views/AboutView.vue')
    // },
  ]
})

export default router
