<template>
  <div>
    <h1>로그인</h1>
    <div>
      <label for="username">ID:</label>
      <input type="text" id="username" v-model="userdata.username"/>
    </div>
    <div>
      <label for="password">비밀번호:</label>
      <input type="password" id="password" keyup.enter="login" v-model="userdata.password"/>
    </div>
    <button @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LogIn',
  data: function () {
    return {
      userdata: {
        username: null,
        password: null,

      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/token/",
        data: this.userdata,

      })
      .then((res) => {
        localStorage.setItem("jwt", res.data.access)
        this.$emit('login')
        this.$router.push({name:'TodoList'})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
