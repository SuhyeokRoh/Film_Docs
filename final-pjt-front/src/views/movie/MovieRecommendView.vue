<template>
  <div>
    <h1>영화 추천입니다.</h1>
    <div>
      <p>무작위</p>
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
    </div>

    <div>
      <p>싫어요순</p>
    </div>

  </div>
</template>

<script>
import RecommendVoterateView from '@/components/RecommendVoterateView'
import RecommendPopularityView from '@/components/RecommendPopularityView'

import axios from 'axios'
const URL = "http://127.0.0.1:8000"


export default {
  name: 'MovieRecommendView',
  data: function() {
    return {
      vote_rate_movies : null,
      popularity_movies : null,
    }
  },
  components: {
    RecommendVoterateView,
    RecommendPopularityView
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