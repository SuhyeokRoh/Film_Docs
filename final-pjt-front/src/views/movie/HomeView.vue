<template>
  <div v-if="movieList">
    <h1>HomePage</h1>
    <div v-for="movie in movieList" :key="movie.id">
      <h3>{{movie.title}}</h3>
      <img :src=getPoster(movie)>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

const URL = "http://127.0.0.1:8000"
export default {
  name: 'HomeView',
  data() {
    return {
      movieList: [],
    }
  },
  methods: {
    getMovie(){
      axios({
        method: 'get',
        url: `${URL}/movies/`,
      })
      .then((res) => {
        const movie = res.data
        this.movieList = _.sampleSize(movie, 10)
      })
      .catch(err => console.log(err))
    },
    getPoster(movie) {
      return `https://image.tmdb.org/t/p/w500/${movie.poster_path}`
    }
  },
  created() {
    this.getMovie()
  }
}
</script>

<style>

</style>