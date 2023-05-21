<template>
  <div>
    <h1>영화 추천입니다.</h1>
    <div>
      <p>무작위</p>
    </div>
    <div>
      <p>평점순</p>
      <div>
        <RecommendVoterateView v-for="movie in vote_rate_movies" :key="movie.id" 
      :movie="movie" />
      </div>
    </div>
    <div>
      <p>인기순</p>
    </div>
    <div>
      <p>좋아요순</p>
    </div>
    <div>
      <p>싫어요순</p>
    </div>
  </div>
</template>

<script>
import RecommendVoterateView from '@/components/RecommendVoterateView'

import axios from 'axios'
const URL = "http://127.0.0.1:8000"


export default {
  name: 'MovieRecommendView',
  data: function() {
    return {
      vote_rate_movies : null
    }
  },
  components: {
    RecommendVoterateView,
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem("jwt")
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
        this.vote_rate_movies = res.data
      })
      .catch((err) => console.log(err))
    },
  },
  created() {
    this.getRecommendMovie()
  }
  
}
</script>

<style>

</style>