<template>
  <div>
    <h1>Profile</h1>
    <p>User Id : {{User.username}}</p>
    <p>User Email : {{User.email}}</p>
    <p>User First Name : {{User.first_name}}</p>
    <p>User Last Name : {{User.last_name}}</p>
    <p>User Nick Name : {{User.nickname}}</p>
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
        const username = this.$store.state.username
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
    }
  },
  created() {
    this.getUser()
  }
}
</script>

<style>

</style>