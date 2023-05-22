<template>
  <div>
    <h1>영화 추천입니다.</h1>
    <div>
      <p>무작위</p>
      <div @click="gotoDetail(r_movie)" v-for="r_movie in random_movies" :key="r_movie.id">
        <img :src="getMoviePoster(r_movie)" >
        <h2>{{ r_movie.title }}</h2>
      </div>
    </div>

    <div>
      <p>평점순</p>
      <div>
        <RecommendVoterateView v-for="v_movie in vote_rate_movies" :key="v_movie.id" 
      :movie="v_movie" />
      </div>
    </div>

    <div>
      <p>인기순</p>
      <div>
        <RecommendPopularityView v-for="p_movie in popularity_movies" :key="p_movie.id" 
      :movie="p_movie" />
      </div>
    </div>

    <div>
      <p>좋아요순</p>
      <div>
        <RecommendLikeView v-for="l_movie in like_movies" :key="l_movie.id" 
      :movie="l_movie" />
      </div>
    </div>

    <div>
      <p>싫어요순</p>
      <div>
        <RecommendDislikeView v-for="d_movie in dislike_movies" :key="d_movie.id" 
      :movie="d_movie" />
      </div>
    </div>

  </div>
</template>

<script>
import RecommendVoterateView from '@/components/RecommendVoterateView'
import RecommendPopularityView from '@/components/RecommendPopularityView'
import RecommendLikeView from '@/components/RecommendLikeView'
import RecommendDislikeView from '@/components/RecommendDislikeView'

import _ from 'lodash'
import axios from 'axios'
const URL = "http://127.0.0.1:8000"


export default {
  name: 'MovieRecommendView',
  data: function() {
    return {
      vote_rate_movies : null,
      popularity_movies : null,
      like_movies: null,
      dislike_movies: null,
      random_movies: [],
    }
  },
  components: {
    RecommendVoterateView,
    RecommendPopularityView,
    RecommendLikeView,
    RecommendDislikeView,
  },
  methods: {
    setToken: function() {
      const token = this.$store.state.access_token
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },
    
    getRecommendMovie() {
      axios({
        method: 'get',
        url: `${URL}/movies/recommend/`,
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        // this.vote_rate_movies = res.data[0]
        this.vote_rate_movies = res.data.high_vote_rate_movies
        this.popularity_movies = res.data.high_popularity_movies
        this.like_movies = res.data.high_like_movies
        this.dislike_movies = res.data.high_dislike_movies
        this.random_movies = res.data.random_movies
        this.pickMovie()

      })
      .catch((err) => console.log(err))
    },
    pickMovie() {
      const rdMovies = this.random_movies
      const randomMovies = _.sampleSize(rdMovies, 5)
      console.log(randomMovies)
      this.random_movies = randomMovies
    },
    getMoviePoster(movie) {
      return `https://image.tmdb.org/t/p/w500/${movie.poster_path}`
    },
    gotoDetail(r_movie) {
        const movie = r_movie
        this.$router.push({name: 'moviedetail', query : {data: JSON.stringify({movie: movie, })}})
    },
  },
  created() {
    this.getRecommendMovie()
  },
  
}
</script>

<style>

</style>