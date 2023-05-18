<template>
  <div>
    <h2>{{ movie.title }}</h2>
    <img :src=getPoster >
    <p>{{ movie.vote_average }}</p>
    <p>{{ movie.release_date }}</p>
    <p>{{ movie.overview }}</p>
  </div>
</template>

<script>
export default {
  name: 'MovieItemView',
  props: {
    movie: Object,
  },
  computed: {
    getPoster() {
      console.log(`https://image.tmdb.org/t/p/original/${this.movie.poster_path}`)
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
    }
  }
}
</script>

<style>

</style>