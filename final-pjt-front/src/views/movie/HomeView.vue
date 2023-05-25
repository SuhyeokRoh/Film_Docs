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
        fixed-height="650px">
        <vueper-slide
          v-for="(movie, i) in movieList"
          :key="i"
          :duration=5800
          :video="{'url': movie.trailerUrl, pointerEvents: false}"
          >
          <template #content>
            <div class="vueperslide__content-wrapper">
              <h1 class="mainmovietitle">{{movie.title}}</h1>
              <div class="mainmovieoverview">{{movie.overview}}</div>
            </div>
            <div class="mainmoviedetail ableToClick" @click="gotoDetail(movie)"><p>바로 가기</p></div>
          </template>
        </vueper-slide>
      </vueper-slides>
    </div>

    <div id="image_slider">
      <vueper-slides
      ref="vueperslides2"
      class="no-shadow"
      @slide="$refs.vueperslides1 && $refs.vueperslides1.goToSlide($event.currentSlide.index, { emit: false })"
      :slide-ratio="1 / 10"
      :dragging-distance="70"
      :gap="3"
      :visible-slides="3"
      fixed-height="250px">
        <vueper-slide
          v-for="(movie, i) in movieList"
          :key="i"
          @click="$refs.vueperslides2 && $refs.vueperslides2.goToSlide(i + 1)">
          <template #content>
            <div class="backdropFlexList">
              <img @click="gotoDetail(movie)" class="ableToClick vueperslide__content-wrapper backdrop" :src="movie.backdrop_path_original">
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
  size: 30px;
  color: black;
}

#video_slider {
  margin: 40px 40px 0px 40px;
  position: relative;
  z-index: 1;
}

#image_slider {
  margin: -120px 40px 40px 40px;
  border: none;
  z-index: 2;
}

.backdropFlexList {
  margin-top: 6%
}

.backdrop{
  border-radius: 7px;
  width: 350px;
  height: 200px;
}

.backdrop:hover {
  transition: all 0.3s linear;
  transform: scale(1.2);
}

.mainmovietitle {
  position: absolute;
  color: white;
  font-size: 60px;
  top: 40px;
  left: 70px;
  text-shadow: -1px 0 #000, 0 1px #000, 1px 0 #000, 0 -1px #000;
}

.mainmovieoverview {
  color: lightgray;
  position: absolute;
  width: 30%;
  top: 200px;
  left: 80px;
  line-height: 200%;
  word-break: keep-all;
  text-align: left;
  text-overflow: ellipsis;
  overflow: hidden;
  text-shadow: -1px 0 #000, 0 1px #000, 1px 0 #000, 0 -1px #000;
  display: -webkit-box;
  -webkit-line-clamp: 3 ;
  -webkit-box-orient: vertical;
}

.mainmoviedetail {
  display: flex;
  position: absolute;
  margin: 0 auto;
  height: 60px;
  width: 180px;
  align-items: center;
  color: white;
  font-size: 40px;
  bottom: 150px;
  right: 50px;
  text-shadow: -1px 0 #000, 0 1px #000, 1px 0 #000, 0 -1px #000;
}

</style>