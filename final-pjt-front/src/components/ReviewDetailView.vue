<template>
  <div>
    <h1>리뷰 상세 페이지</h1>
    <h2>{{queryData.reviews.title}}</h2>
    <p @click="gotoProfile">작성자 : {{queryData.username}}</p>
    <p>{{queryData.reviews.content}}</p>
    <div>
      <button @click="likeReview">리뷰 좋아요 / 취소</button>
      <p>좋아요 : {{like_reviews}}</p>
    </div>
    <div>
      <button @click="dislikeReview">리뷰 싫어요 / 취소</button>
      <p>싫어요 : {{dislike_reviews}}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const URL = "http://127.0.0.1:8000"
export default {
  name: 'ReviewDetailView',
  data() {
    return {
      queryData: null,
      like_reviews: null,
      dislike_reviews: null,
    }
  },
  mounted() {
    this.queryData = JSON.parse(this.$route.query.data)
    this.like_reviews = this.queryData.reviews.like_users.length
    this.dislike_reviews = this.queryData.reviews.dislike_users.length
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem("jwt")
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },

    likeReview() {
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id

      axios({
        method: 'post',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/like/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.like_reviews = res.data.like_users.length
      })
      .catch((err) => console.log(err))
    },

    dislikeReview() {
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id

      axios({
        method: 'post',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/dislike/`,
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        this.dislike_reviews = res.data.dislike_users.length
      })
      .catch((err) => console.log(err))
    },

    gotoProfile() {
      const username = this.queryData.username
      this.$router.push({name: 'Profile', query : {user: username}})
    },
  }
}
</script>

<style>

</style>