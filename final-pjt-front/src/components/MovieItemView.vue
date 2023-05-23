<template>
  <div class="ableToClick" @click="gotoDetail">
    <img :src="movie.poster_path" >
    <h2>{{ movie.title }}</h2>
  </div>
</template>

<script>

export default {
  name: 'MovieItemView',
  props: {
    movie: Object,
  },
  methods: {
    setToken: function() {
      const token = this.$store.state.access_token
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