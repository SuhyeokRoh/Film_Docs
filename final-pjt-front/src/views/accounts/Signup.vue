<template>
  <div id="signupbox">
    <div id="signup">

    <h1 class="sign_up">SignUp</h1>
    <div id="id">
      <label for="username">사용자 계정 : </label>
      <input type="text" id="username" v-model="userdata.username" />
    </div>
    <div id="lastname">
      <label for="last_name">성 : </label>
      <input type="text" id="last_name" v-model="userdata.last_name" />
    </div>
    <div id="firstname">
      <label for="first_name">이름 : </label>
      <input type="text" id="first_name" v-model="userdata.first_name" />
    </div>
    <div id="nickname">
      <label for="nickname">닉네임 : </label>
      <input type="text" id="nickname" v-model="userdata.nickname" />
    </div>
    <div id="email">
      <label for="email">e-mail : </label>
      <input type="text" id="email" v-model="userdata.email" />
    </div>
    <div id="pw">
      <label for="password">비밀번호 : </label>
      <input type="password" id="password" v-model="userdata.password" />
    </div>
    <div id="pwcf">
      <label for="passwordConfirm">비밀번호 확인:</label>
      <input type="password" id="passwordConfirm" v-model="userdata.passwordConfirm" @keyup.enter="signup" />
    </div>
    <button @click="signup">회원 가입</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const URL = 'http://127.0.0.1:8000'
export default {
  name: 'SignUpView',
  data: function () {
    return {
      userdata: {
        username: null,
        last_name: null,
        first_name: null,
        nickname: null,
        email: null,
        password: null,
        passwordConfirm: null,
      }
    }
  },
  methods: {
    signup: function () {

      axios({
        method: "post",
        url: `${URL}/accounts/signup/`,
        data: this.userdata,
      })
      .then(() => {
        alert("회원가입이 완료되었습니다.")
        this.$router.push({ name: 'Login' })
      })
      .catch((error) => {
        alert(error.response.data.error)

        this.userdata.username = ''
        this.userdata.password = ''
        this.userdata.passwordConfirm = ''
        this.userdata.email = ''
        this.userdata.nickname = ''
        this.userdata.last_name = ''
        this.userdata.first_name = ''
      })
    }
  }
}
</script>

<style>
  #signupbox {
    height: 800px;
    display: flex;
    justify-content: center;
    align-items: center;

    margin:0;
    
    font:600 16px/18px 'Open Sans',sans-serif;
  }

  #signup {
    color:#6a6f8c;
    background:#c8c8c8;
    font:600 16px/18px 'Open Sans',sans-serif;

    border: 3px solid black;
    width: 500px;
    height: 60%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
  }
</style>