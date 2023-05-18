<template>
  <div>
    <h2>{{ movie.title }}</h2>
    <img :src=getPoster >
    <p>{{ movie.vote_average }}</p>
    <p>{{ movie.release_date }}</p>
    <p>{{ movie.overview }}</p>
    <ReviewListView />
  </div>
</template>

<script>
import axios from 'axios'
import ReviewListView from './ReviewListView.vue'

const URL = "http://127.0.0.1:8000"
export default {
  name: 'MovieItemView',
  components: {
    ReviewListView,
  },
  props: {
    movie: Object,
  },
  computed: {
    getPoster() {
      // console.log(`https://image.tmdb.org/t/p/original/${this.movie.poster_path}`)
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
    }
  },
  created() {
    this.getReview()
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem("jwt")
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },
    getReview(movie_pk) {
      axios({
        method: 'get',
        url: `${URL}/reviews/${movie_pk}/`,
        headers: this.setToken()
      })
      .then(res => {
        console.log(res.data)
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>

</style>