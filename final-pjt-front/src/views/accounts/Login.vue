<template>
  <div>
    <h1>로그인</h1>
    <div>
      <label for="username">ID: </label>
      <input type="text" id="username" v-model="userdata.username" />
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="userdata.password" @keyup.enter="login" />
    </div>
    <button @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginView',
  data: function () {
    return {
      userdata: {
        username: null,
        password: null,
      },
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
        this.$store.dispatch('Login_create_username', this.userdata.username)
        localStorage.setItem("jwt", res.data.access)
        this.$emit('login')
        this.$router.push({name:'movie'})
      })
      .catch(() => {
        alert("회원 정보가 일치하지 않습니다.")
        this.userdata.username = ''
        this.userdata.password = ''
      })
     },
    //  
  },
}
</script>
