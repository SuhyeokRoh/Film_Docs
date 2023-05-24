<template>
  <div class="inner">
    <div class="col">
      <h1>무작위</h1>
      <div class="row wrapper">
        <div class="ableToClick rcmlist" v-for="r_movie in random_movies" :key="r_movie.id">
          <div class="cardrcm"  @click="gotoDetail(r_movie)">
            <div class="frontrcm"><img :src="r_movie.poster_path_500" class="rcmPoster"></div>
            <div class="backrcm">{{r_movie.title}}</div>
          </div>
        </div>
      </div>
    </div>

    <div class="col">
      <h1>평점순</h1>
      <div class="row wrapper">
        <RecommendVoterateView v-for="v_movie in vote_rate_movies" :key="v_movie.id" 
      :movie="v_movie" />
      </div>
    </div>

    <div class="col">
      <h1>인기순</h1>
      <div class="row wrapper">
        <RecommendPopularityView v-for="p_movie in popularity_movies" :key="p_movie.id" 
      :movie="p_movie" />
      </div>
    </div>

    <div class="col">
      <h1>좋아요순</h1>
      <div class="row wrapper">
        <RecommendLikeView v-for="l_movie in like_movies" :key="l_movie.id" 
      :movie="l_movie" />
      </div>
    </div>

    <div class="col">
      <h1>싫어요순</h1>
      <div class="row wrapper">
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
    ConfirmLogin() {
      const user = this.$store.state.username
      if (!user) {
        alert("로그인이 필요합니다.")
        this.$router.push({name: 'Login'})
      }
    },
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
    gotoDetail(r_movie) {
        const movie = r_movie
        this.$router.push({name: 'moviedetail', query : {data: JSON.stringify({movie: movie, })}})
    },
  },
  created() {
    this.getRecommendMovie()
  },
  mounted() {
    this.ConfirmLogin()
  },
}
</script>

<style>
.wrapper {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-between;
  height: 500px;
  width: 100%;
}

.rcmlist{
  position: relative;
  width: 245.44px;
  height: 350px;
}

.rcmPoster {
  width: 100%;
  height: 100%;
}

.cardrcm {
  height: 100%;
  width: 100%;
  position: relative;
  transition: 1s ;
  transform-style: preserve-3d;
}


.frontrcm, .backrcm {
  position: absolute;
  width: 100%; 
  height: 100%;
  backface-visibility: hidden;
}

.rcmlist:hover .cardrcm {
  transform: rotateY(180deg);
}

.backrcm {
  background-color: black;
  color:white;
  border-radius: 7px;
  line-height: 350px;
  font-size: 17px;
  transform: rotateY(180deg);
}
</style>