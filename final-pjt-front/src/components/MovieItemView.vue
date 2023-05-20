<template>
  <div @click="gotoDetail">
    <img :src=getPoster >
    <h2>{{ movie.title }}</h2>
  </div>
</template>

<script>
import axios from 'axios'

const URL = "http://127.0.0.1:8000"
export default {
  name: 'MovieItemView',
  props: {
    movie: Object,
  },
  data() {
    return {
      reviews: null,
    }
  },
  computed: {
    getPoster() {
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
    getReview() {
      axios({
        method: 'get',
        url: `${URL}/movies/${this.movie.id}/reviews/`,
        // headers: this.setToken()
      })  
      .then(res => {
        this.reviews = res.data
      })
      .catch(err => console.log(err))
    },
    gotoDetail() {
      const movie = this.movie
      const reviews = this.reviews

      this.$router.push({name: 'moviedetail', query : {data: JSON.stringify({movie: movie, reviews: reviews })}})
    }
  }
}
</script>

<style>

</style>