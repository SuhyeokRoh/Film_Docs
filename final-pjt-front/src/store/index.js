import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    username : null,
  },
  getters: {
  },
  mutations: {
    LOGIN_USER(state, username) {
      state.username = username
    },
    LOGOUT_USER(state) {
      state.username = null
    },
    // GET_REVIEWS(state, reviews) {
    //   state.reviews = reviews
    // },
  },
  actions: {
    Login_create_username(context, username) {
      context.commit('LOGIN_USER', username)
    },
    Logout_delete_username(context) {
      context.commit('LOGOUT_USER')
    },
    getReviews(movie_id) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${movie_id}/reviews/`,
      })
        .then((res) => {
          // context.commit('GET_REVIEWS', res.data)
          console.log(res.data)
          return res.data
        })
        .catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
