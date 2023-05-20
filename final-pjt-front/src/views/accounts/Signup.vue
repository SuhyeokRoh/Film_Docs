<template>
  <div>
    <h1>SignUp</h1>
    <div>
      <label for="username">사용자 계정 : </label>
      <input type="text" id="username" v-model="userdata.username" />
    </div>
    <div>
      <label for="last_name">성 : </label>
      <input type="text" id="last_name" v-model="userdata.last_name" />
    </div>
    <div>
      <label for="first_name">이름 : </label>
      <input type="text" id="first_name" v-model="userdata.first_name" />
    </div>
    <div>
      <label for="nickname">닉네임 : </label>
      <input type="text" id="nickname" v-model="userdata.nickname" />
    </div>
    <div>
      <label for="email">e-mail : </label>
      <input type="text" id="email" v-model="userdata.email" />
    </div>
    <div>
      <label for="password">비밀번호 : </label>
      <input type="password" id="password" v-model="userdata.password" />
    </div>
    <div>
      <label for="passwordConfirm">비밀번호 확인:</label>
      <input type="password" id="passwordConfirm" v-model="userdata.passwordConfirm" @keyup.enter="signup" />
    </div>
    <button @click="signup">회원 가입</button>
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
.error-message {
  color: red;
}
</style>