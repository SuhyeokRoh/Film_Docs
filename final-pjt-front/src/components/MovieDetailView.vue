<template>
  <div v-if="queryData">
    <h1>Movie Detail Page</h1>
    <h3>제목 : {{ queryData.movie.title }}</h3>
    <img :src=getPoster >
    <p>개봉일 : {{ queryData.movie.release_date }}</p>
    <p>인기도 : {{ queryData.movie.popularity }}</p>
    <p>투표수 : {{ queryData.movie.vote_count }}</p>
    <p>투표 평점 : {{ queryData.movie.vote_average }}</p>
    <p>줄거리 : {{ queryData.movie.overview }}</p>
    <p>장르 : {{ queryData.movie.genres }}</p>

    <div>
      <label for="review">리뷰 작성 : </label>
      <input type="text" id="review" v-model="NewReview" @keyup.enter="createReview">
      <ReviewItemView 
      v-for="review in queryData.reviews" :key="review.id"
      :review="review" />
      <button @click="createReview">리뷰 작성</button>
    </div>
  </div>
</template>

<script>
import ReviewItemView from './ReviewItemView.vue'
import axios from 'axios'

const URL = "http://127.0.0.1:8000"
export default {
  name: "MovieDetailView",
  data() {
    return {
      queryData: null,
      NewReview: null,
    }
  },
  mounted() {
    this.queryData = JSON.parse(this.$route.query.data)
  },
  components: {
    ReviewItemView,
  },
  computed: {
    getPoster() {
      return `https://image.tmdb.org/t/p/w500/${this.queryData.movie.poster_path}`
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
    getReview: function() {
      // this.$store.dispatch('getReviews')
       
       axios({
        method: 'get',
        url: `${URL}/movies/${this.movie.id}/reviews`,
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          this.review = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },

    createReview: function() {
      const movieid = this.queryData.movie.id 
      console.log(this.NewReview)
      console.log(movieid)
      axios({
        method: "post",
        url: `${URL}/movies/${movieid}/reviews/`,
        data: { 'content' :this.NewReview, 'movie':movieid},
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        this.NewReview = ''
        
      }).catch((err) => {
        console.log(err)
      })
    },
  },
  create() {
    this.getReview()
    this.createtReview()
  },
}
</script>

<style>

</style>