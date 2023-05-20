<template>
  <div @click="gotoProfile()">
    <p>content : {{review.content}}</p>
    <p>작성자 : {{username}}</p>
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
      username: null,
    }
  },
  created() {
    this.getUsername()
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
        this.username = res.data.username
      })
      .catch((err) => console.log(err))
    },

    gotoProfile() {
      const username = this.username
      this.$router.push({name: 'Profile', query : {user: username}})
    },
  },
}
</script>

<style>

</style>