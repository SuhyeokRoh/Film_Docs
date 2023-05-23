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
      <p>movie_title : {{ review.movie.title }}</p>
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

    <h3>내가 남긴 댓글</h3>
    <div v-for="comment in User.comment_set" :key="comment.id">
      <p>movie_title : {{ comment.movie_title }} </p>
      <p>review : {{ comment.review_content }}</p>
      <p>content : {{ comment.content }}</p>
    </div>


    
    <div>
      <p> 팔로워 : {{ follower }} </p>
      <button @click="followPerson">follow / 취소</button>
    </div>

    <div>
      <p>팔로잉 : {{ following }} </p>
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
        queryData: null,
        User: null,
        movieTitle: null,
        following: null,
        follower: null,
        isfollowed: false,
    }
  },
  mounted() {
    // this.followPerson()
    this.getUser()
  },
  methods: {
    setToken: function() {
      const token = this.$store.state.access_token
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
        // console.log(res.data)
        this.User = res.data
        this.following = res.data.followings.length
        this.follower = res.data.followers.length
        // console.log(this.User)
      })
      .catch((err) => console.log(err))
    },

    followPerson() {
      const username = this.$route.query.user
      
      axios({
        method: 'post',
        url: `${URL}/accounts/${username}/profile/follow/`,
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        // 여기서 키중복 경고가 발생함 그러나 follow 실시간 반영을 위해 일단 남겨두었음
        this.follower = res.data.followers.length
      })
      .catch((err) => {
        alert(err.response.data.err)
        })
    },

  },
  created() {
    this.getUser()
  },
}
</script>

<style>

</style>