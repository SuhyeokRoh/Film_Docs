<template>
  <div class="ableToClick rcmlist" @click="gotoDetail">
    <div class="cardrcm"  @click="gotoDetail(movie)">
      <div class="frontrcm"><img :src="movie.poster_path_500" class="rcmPoster"></div>
      <div class="backrcm">{{movie.title}}</div>
    </div>
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