<template>
  <div v-if="User">
    <h1>Profile</h1>
    <p>User Id : {{User.username}}</p>
    <p>User Email : {{User.email}}</p>
    <p>User First Name : {{User.first_name}}</p>
    <p>User Last Name : {{User.last_name}}</p>
    <p>User Nick Name : {{User.nickname}}</p>
    <h3>내가 남긴 리뷰</h3>
    <div v-for="review in User.review_set" :key="review.id">
      <p>title : {{ review.movie.title }}</p>
      <p>content : {{ review.content }}</p>
    </div>
    <h3>좋아요 누른 영화</h3>
    <div v-for="movie in User.movielike" :key="movie.id">
      <p>{{movie.title}}</p>
    </div>
    <h3>좋아요 누른 리뷰</h3>
    <div v-for="likereview in User.like_reviews" :key="likereview.id">
      <p>{{likereview.movie.title}} - {{likereview.content}}</p>
    </div>
    <h3>팔로워</h3>
    <div>

    </div>
    <h3>팔로잉</h3>
    <div>
      
    </div>

  </div>
</template>

<script>
import axios from 'axios'

const URL = "http://127.0.0.1:8000"
export default {
  name: 'ProfileView',
  data() {
    return {
        User: null,
        movieTitle: null,
        inputUser: null, 
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

    getUser() {
      const username = this.$route.query.user
      axios({
        method: 'get',
        url: `${URL}/accounts/${username}/profile/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.User = res.data
        console.log(this.User)
      })
      .catch((err) => console.log(err))
    },

    followPerson() {
      const username = this.$route.query.user

      axios({
        method: 'post',
        url: `${URL}/accounts/${username}/profile/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.User = res.data
        console.log(this.User)
      })
      .catch((err) => console.log(err))
    },

  },
  created() {
    this.getUser()
  },
}
</script>

<style>

</style>