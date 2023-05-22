<template>
  <div @click="gotoDetail">
    <img :src=getPoster >
    <h2>{{ movie.title }}</h2>
  </div>
</template>

<script>

export default {
  name: 'RecommendDislikeView',
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
  
  methods: {
    setToken: function() {
      const token = localStorage.getItem("jwt")
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },
    gotoDetail() {
        const movie = this.movie
        this.$router.push({name: 'moviedetail', query : {data: JSON.stringify({movie: movie, })}})  
    }
  }
}
</script>

<style>

</style>