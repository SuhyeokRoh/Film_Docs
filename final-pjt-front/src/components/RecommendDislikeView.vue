<template>
  <div @click="gotoDetail">
    <img :src="movie.poster_path_500" >
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