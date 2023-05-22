import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
// import axios from 'axios'

Vue.use(Vuex)

// const API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    username : null,
    access_token : null,
  },
  getters: {
    
  },
  mutations: {
    LOGIN_USER(state, payload) {
      state.username = payload.username
      state.access_token = payload.access_token
    },
    LOGOUT_USER(state) {
      state.username = null
      state.access_token = null
    },
    
  },
  actions: {
    Login_create(context, payload) {
      context.commit('LOGIN_USER', payload)
    },
    Logout_delete(context) {
      context.commit('LOGOUT_USER')
    },
  },
  modules: {
  }
})