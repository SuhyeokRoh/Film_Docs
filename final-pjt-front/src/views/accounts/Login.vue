<template>
<div id="LoginBox">
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
 #LoginBox {
  height: 720px;
  display: flex;
  justify-content: center;
  align-items: center;
 }

 #Login {

  box-shadow: 5px 5px 5px 5px rgba(51, 51, 96, 96);
  width: 500px;
  height: 60%;
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