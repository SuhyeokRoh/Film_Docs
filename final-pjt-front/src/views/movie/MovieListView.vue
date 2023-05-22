<template>
  <div>
    <ul>
      <MovieItemView v-for="movie in movies" :key="movie.id" 
      :movie="movie" />
    </ul>
  </div>
</template>


<script>
import axios from 'axios'
import MovieItemView from '@/components/MovieItemView'

const URL = "http://127.0.0.1:8000"
export default {
  name: 'MovieListView',
  components: {
    MovieItemView,
  },
  data: function() {
    return {
      movies: null,
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      axios({
        method: 'get',
        url: `${URL}/movies/`,
      })
      .then(res => {
        this.movies = res.data
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>
