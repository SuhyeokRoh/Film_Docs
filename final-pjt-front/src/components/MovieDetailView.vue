<template>
  <div>
    <h1>Movie Detail Page</h1>
    <h3>제목 : {{ $route.params.movie.title }}</h3>
    <img :src=getPoster >
    <p>개봉일 : {{ $route.params.movie.release_date }}</p>
    <p>인기도 : {{ $route.params.movie.popularity }}</p>
    <p>투표수 : {{ $route.params.movie.vote_count }}</p>
    <p>투표 평점 : {{ $route.params.movie.vote_average }}</p>
    <p>줄거리 : {{ $route.params.movie.overview }}</p>
    <p>장르 : {{ $route.params.movie.genres }}</p>

    <div>
      <label for="review">리뷰 작성 : </label>
      <input type="text" id="review" v-model="Review" @keyup.enter="createReview">
      <ReviewItemView 
      v-for="review in $route.params.reviews" :key="review.id"
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
      Review: null,
    }
  },
  props: {
    movie: {
      type: Object,
    },
    reviews: {
      type: Array,
    }
  },
  components: {
    ReviewItemView,
  },
  computed: {
    getPoster() {
      // console.log(`https://image.tmdb.org/t/p/original/${this.movie.poster_path}`)
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
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
      const movieid = this.movie.id
      console.log(this.$route.params.movie)
      console.log(this.Review)
      console.log(movieid)
      axios({
        method: "post",
        url: `${URL}/movies/${this.movie.id}/reviews/`,
        data: { 'content' :this.Review, 'movie':movieid},
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        this.Review = ''
        
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