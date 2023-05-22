<template>
<div>
  <div id="Login">
    <h1>로그인</h1>
    <div class="form-group">
      <label for="username">ID: </label>
      <input type="text" id="username" v-model="userdata.username" class="input-field" />
    </div>
    <div class="form-group">
      <label for="password">PW: </label>
      <input type="password" id="password" v-model="userdata.password" @keyup.enter="login" class="input-field" />
    </div>
    <button @click="login">로그인</button>
  </div>
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
        const payload = {
          'username' : this.userdata.username,
          'access_token' :  res.data.access
        }
        this.$store.dispatch('Login_create', payload)
        this.$emit('login')
        this.$router.push({name:'home'})
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

<style>
 #Login {
  border: 5px solid white;
  width: 500px;
  height: 720px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
 }

.form-group {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.label-left {
  width: 100px;
}

.input-field {
  width: 200px;
}

</style>