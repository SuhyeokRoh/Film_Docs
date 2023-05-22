<template>
  <div class="ableToClick" id="reviewbox" @click="gotoDetailReview">
    <div>
      <h3>{{review.title}}</h3>
      <p>작성자 : {{nickname}}</p>
      <p>좋아요 : {{like_reviews}}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const URL = "http://127.0.0.1:8000"
export default {
  name: "ReviewItemView",
  props: {
    review: Object,
  },
  data() {
    return {
      query: null,
      nickname: null,
      username: null,
      like_reviews: null,
    }
  },
  created() {
    this.getUsername()
  },
  mounted() {
    this.like_reviews = this.review.like_users.length
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem("jwt")
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },

    getUsername() {
      const userid = this.review.user
      axios({
        method: 'get',
        url: `${URL}/accounts/${userid}/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.nickname = res.data.nickname
        this.username = res.data.username
      })
      .catch((err) => console.log(err))
    },

    gotoDetailReview() {
      const reviews = this.review
      const user = {
        'username' : this.username,
        'nickname' : this.nickname,
      }
      this.$router.push({name: 'reviewdetail', query : {data: JSON.stringify({reviews: reviews, user: user, })}})
    },
  }
}
</script>

<style>
#reviewbox {
  border: solid 1px black;
}
</style>