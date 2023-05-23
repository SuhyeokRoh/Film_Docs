<template>
  <div v-if="movieList">
    <h1>HomePage</h1>
    <!-- <div @click="gotoDetail(movie)" v-for="movie in movieList" :key="movie.id">
      <h3>{{movie.title}}</h3>
      <img :src=getPoster(movie)>
    </div> -->
    <vueper-slides autoplay fade :touchable="false">
      <vueper-slide v-for="movie in movieList"
      :key="movie.id" 
      :title="movie.title"
      :image="getPoster(movie)" 
      />
      <template #pause>
        <i class="icon pause_circle_outline"></i>
      </template>
    </vueper-slides>
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
        const movies = res.data
        console.log(movies)
        for (let i=0; i<movies.length; i++) {
          const content = {
            title : movies[i].title,
            image: movies[i].backdrop_path,
            video : {
              url : movies[i].trailerUrl,
            }
          }
          this.movieList.push(content)
        }
      })
      .catch(err => console.log(err))
    },

    getPoster(movie) {
      return `https://image.tmdb.org/t/p/original/${movie.backdrop_path}`
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
.vueperslides__arrow {
  color: yellow
}
</style>