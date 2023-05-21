import Vue from 'vue'
import VueRouter from 'vue-router'
import SignupView from '@/views/accounts/Signup'
import LoginView from '@/views/accounts/Login'
import MovieListView from '@/views/movie/MovieListView'
import ProfileView from '@/views/accounts/ProfileView'
import MovieDetailView from '@/components/MovieDetailView'
import ReviewDetailView from '@/components/ReviewDetailView'
import MovieRecommendView from '@/views/movie/MovieRecommendView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movie',
    component: MovieListView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
  },
  {
    path: '/movie/detail',
    name: 'moviedetail',
    component: MovieDetailView,
  },
  {
    path: '/movie/review/detail',
    name: 'reviewdetail',
    component: ReviewDetailView,
  },
  {
    path: '/movie/recommend/',
    name: 'recommend',
    component: MovieRecommendView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
