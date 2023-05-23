<template>
  <div id="home" v-if="movieList">

    <div id="video_slider">
      <vueper-slides
        ref="vueperslides1"
        @slide="$refs.vueperslides2 && $refs.vueperslides2.goToSlide($event.currentSlide.index, { emit: false })"
        :touchable="false"
        :arrows="false"
        autoplay
        fade
        :bullets="false"
        fixed-height="500px"
        :slide-content-outside="contentPosition">
        <vueper-slide
          v-for="(movie, i) in movieList"
          :key="i"
          :video="movie.trailerUrl">
          <template #content>
            <div class="vueperslide__content-wrapper"><h1>{{movie.title}}</h1></div>
          </template>
        </vueper-slide>
      </vueper-slides>
    </div>

    <div id="image_slider">
      <vueper-slides
      ref="vueperslides2"
      @slide="$refs.vueperslides1 && $refs.vueperslides1.goToSlide($event.currentSlide.index, { emit: false })"
      :slide-ratio="1 / 10"
      :dragging-distance="70"
      :gap="3"
      :visible-slides="3"
      fixed-height="169px">
        <vueper-slide
          v-for="(movie, i) in movieList"
          :key="i"
          @click="$refs.vueperslides2 && $refs.vueperslides2.goToSlide(i + 1)">
          <template #content>
            <div>
              <img @click="gotoDetail(movie)" class="vueperslide__content-wrapper" :src="movie.backdrop_path">
            </div>
          </template>
        </vueper-slide>
      </vueper-slides>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

const URL = "http://127.0.0.1:8000"
export default {
  name: 'HomeView',
  data() {
    return {
      contentPosition: 'top',
      movieList: [],
    }
  },
  components: { 
    VueperSlides, VueperSlide 
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
#home {
  width: 80%;
  margin: auto;
}

.vueperslides__arrow {
  color: yellow
}

#video_slider {
  margin: 40px;
}

#image_slider {
  padding-top: 50px;
  margin: 40px;
}
</style>