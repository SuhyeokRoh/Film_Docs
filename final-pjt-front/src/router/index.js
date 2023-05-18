import Vue from 'vue'
import VueRouter from 'vue-router'
import SignupView from '@/views/accounts/Signup'
import LoginView from '@/views/accounts/Login'
import MovieListView from '@/views/movie/MovieListView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movie',
    name: 'movie',
    component: MovieListView
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView,
  },
  {
    path: '/',
    name: 'Login',
    component: LoginView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
