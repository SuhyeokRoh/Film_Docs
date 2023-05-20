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
      <p>title : {{ getMovie(review.movie) }}</p>
      <p>content : {{ review.content }}</p>
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
        console.log(this.$store.state.username)
        console.log(this.$route.query.user)
        console.log(username)
        axios({
            method: 'get',
            url: `${URL}/accounts/${username}/profile/`,
            headers: this.setToken()
        })
        .then((res) => {
            this.User = res.data
        })
        .catch((err) => console.log(err))
    },
    getMovie(movie_pk) {
      axios({
        method: 'get',
        url: `${URL}/movies/${movie_pk}/`,
        headers: this.setToken()
      })
      .then(res => {
        this.movieTitle = res.data.title
        return res.data.title
      })
      .catch(err => console.log(err))
    }
  
  },
  created() {
    // this.inputUser = this.$route.params.user;
    this.getUser()
  },
  // mounted() {
  //   // this.User = JSON.parse(this.$route.data.user)
  //   // this.inputUser = this.$route.params.user;
  //   // this.query = JSON.parse(this.$route.data.user)
  //   const User = this.$route.query.user
  // },
}
</script>

<style>

</style>