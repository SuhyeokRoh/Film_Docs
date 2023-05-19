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
    <!-- <p>장르 : {{ queryData.movie.genres }}</p> -->
    <div>
      장르 : <p v-for="(genre,index) in getGenreData" :key="index">{{ genre.name }}</p>
    </div>

    <div>
      <label for="review">리뷰 작성 : </label>
      <input type="text" id="review" v-model="NewReview" @keyup.enter="createReview">
      <ReviewItemView 
      v-for="review in this.Reviews" :key="review.id"
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
      NewReview: '',
      Genre: null,
      Reviews: [],
    }
  },
  mounted() {
    this.queryData = JSON.parse(this.$route.query.data)
    this.getGenre()
    // this.getReview()
  
  },
  components: {
    ReviewItemView,
  },
  computed: {
    getPoster() {
      return `https://image.tmdb.org/t/p/w500/${this.queryData.movie.poster_path}`
    },
    getGenreData() {
      return this.Genre
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
    getReview() {
      const movieid = this.queryData.movie.id
      axios({
        method: 'get',
        url: `${URL}/movies/${movieid}/`,
        headers: this.setToken()
      })  
      .then(res => {
        this.queryData.reviews = res.data
      })
      .catch(err => console.log(err))
    },

    createReview: function() {
      const movieid = this.queryData.movie.id 
      // console.log(this.NewReview)
      // console.log(movieid)
      console.log(this.queryData.reviews)

      axios({
        method: "post",
        url: `${URL}/movies/${movieid}/reviews/`,
        data: { 'content' :this.NewReview, 'movie':movieid},
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        this.queryData.reviews = res.data
        console.log(this.queryData.reviews)
        this.Reviews.push(this.queryData.reviews)
        this.NewReview = ''
        
      }).catch((err) => {
        console.log(err)
      })
    },
    getGenre: function() {
      const movieid = this.queryData.movie.id 
      axios({
        method: "get",
        url: `${URL}/movies/${movieid}/`,
        headers: this.setToken()
      })
      .then((res) => {
        // console.log(res)
        this.Genre = res.data.genres
      })
      .catch((err) => {
        console.log(err)
      })
      
    },

  },
  // created() {
  //   console.log('실행되냐?');
  //   // this.createReview()
  //   this.getReview()
   
  // },
}
</script>

<style>

</style>