<template>
  <div v-if="movieList">
    <h1>HomePage</h1>
    <div @click="gotoDetail(movie)" v-for="movie in movieList" :key="movie.id">
      <h3>{{movie.title}}</h3>
      <img :src=getPoster(movie)>
      <!-- <img :src=getBackDropPath(movie)> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'

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
        url: `${URL}/movies/main/`,
      })
      .then((res) => {
        this.movieList = res.data
      })
      .catch(err => console.log(err))
    },

    getPoster(movie) {
      return `https://image.tmdb.org/t/p/w500/${movie.poster_path}`
    },

    gotoDetail(select_movie) {
      const movie = select_movie

      this.$router.push({name: 'moviedetail', query : {data: JSON.stringify({movie: movie,})}})
    }
  },
  created() {
    this.getMovie()
  }
}
</script>

<style>

</style>