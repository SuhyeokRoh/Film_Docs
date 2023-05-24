<template>
  <div class="OnePoster ableToClick">
    <div class="card" @click="gotoDetail">
      <div class="front"><img class="posterlist" :src="movie.poster_path_original" ></div>
      <div class="back">{{movie.title}}</div>
    </div>
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
.OnePoster {
  position: relative;
  margin-bottom: 30px;
  width: 230px;
  height: 345px;
}

.posterlist {
  width: 100%;
  height: 100%;
}

.card {
  height: 100%;
  width: 100%;
  position: relative;
  transition: 1s ;
  transform-style: preserve-3d;
}


.front, .back {
  position: absolute;
  width: 100%; 
  height: 100%;
  backface-visibility: hidden;
}

.OnePoster:hover .card {
  transform: rotateY(180deg);
}

.back {
  background-color: black;
  color:white;
  border-radius: 7px;
  line-height: 350px;
  font-size: 20px;
  transform: rotateY(180deg);
}
</style>