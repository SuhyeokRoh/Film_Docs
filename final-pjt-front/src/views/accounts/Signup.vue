<template>
  <div>
    <h1>SignUp</h1>
    <div>
      <label for="username">사용자 이름:</label>
      <input type="text" id="username" v-model="userdata.username" />
    </div>
    <div>
      <label for="password">비밀번호:</label>
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

const URL = 'http://127.0.0.1:8000/'
export default {
  name: 'SignUpView',
  data: function () {
    return {
      userdata: {
        username: null,
        password: null,
        passwordConfirm: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: "post",
        // reqest 500 url: "http://127.0.0.1:8000/accounts/signup /가 빠져서..
        url: URL + "accounts/signup/",
        data: this.userdata,
      })
      .then(() => {
        this.$router.push({ name: 'Login' })
      })
      .catch((err) => {
        this.userdata.username = ''
        this.userdata.password = ''
        this.userdata.passwordConfirm = ''
        console.log(err)
      })
    }
  }
}
</script>
