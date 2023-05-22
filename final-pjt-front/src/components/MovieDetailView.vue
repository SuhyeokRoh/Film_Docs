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
    <div>
      장르 : <p v-for="(genre,index) in getGenreData" :key="index">{{ genre.name }}</p>
    </div>

    <div>
      <p>예고편 : </p>
      <iframe :src="trailerSrc" width="500" height="255" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen></iframe>
    </div>

    <div>
      <button @click="likeMovie">좋아요 / 취소</button>
      <p>{{like_user}}</p>
    </div>

    <div>
      <label for="review_title">제목 작성: </label>
      <input type="text" id="review_title" v-model="NewReviewTitle"><br>
      <label for="review_content">리뷰 작성 : </label>
      <textarea id="review_content" cols="30" rows="10" v-model="NewReviewContent" @keyup.enter="createReview"></textarea>
      <button @click="createReview">리뷰 등록</button>
      <ReviewItemView 
      v-for="review in Reviews" :key="review.id"
      :review="review" />
    </div>
  </div>
</template>

<script>
import ReviewItemView from './ReviewItemView.vue'
import axios from 'axios'

const key = 'e66fa81c4a87396b24dd94a15cc7a8b1'
const URL = "http://127.0.0.1:8000"
export default {
  name: "MovieDetailView",
  data() {
    return {
      queryData: null,
      NewReviewTitle: '',
      NewReviewContent: '',
      Genre: null,
      Reviews: [],
      like_user: null,
      trailerSrc: null,
    }
  },
  mounted() {
    this.queryData = JSON.parse(this.$route.query.data)
    this.getGenre()
    this.Reviews = this.getReview()
    this.like_user = this.queryData.movie.movie_like_users.length
    this.getTrailer()
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
        url: `${URL}/movies/${movieid}/reviews/`,
      })  
      .then(res => {
        this.Reviews = res.data
      })
      .catch(err => console.log(err))
    },

    createReview: function() {
      const movieid = this.queryData.movie.id 
      
      axios({
        method: "post",
        url: `${URL}/movies/${movieid}/reviews/create/`,
        data: { 
          'title':this.NewReviewTitle,
          'content':this.NewReviewContent,
          'movie':movieid},
        headers: this.setToken()
      })
      .then(() => {
        this.getReview()
        this.NewReviewContent = ''
        this.NewReviewTitle = ''
        
      }).catch((err) => {
        console.log(err)
      })
    },

    getGenre: function() {
      const movieid = this.queryData.movie.id 
      axios({
        method: "get",
        url: `${URL}/movies/${movieid}/`,
        // headers: this.setToken()
      })
      .then((res) => {
        this.Genre = res.data.genres
      })
      .catch((err) => {
        console.log(err)
      })
    },

    likeMovie() {
      const movieid = this.queryData.movie.id 

      axios({
        method: "post",
        url: `${URL}/movies/${movieid}/like/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.like_user = res.data.movie_like_users.length
      }).catch((err) => {
        console.log(err)
      })
    },

    getTrailer() {
      const movieid = this.queryData.movie.movie_id
      axios({
        method: "get",
        url: `https://api.themoviedb.org/3/movie/${movieid}/videos?api_key=${key}`
      })
      .then((res) => {
        this.trailerSrc = `https://www.youtube.com/embed/${res.data.results[0].key}?autoplay=1`
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}
</script>

<style>

</style>