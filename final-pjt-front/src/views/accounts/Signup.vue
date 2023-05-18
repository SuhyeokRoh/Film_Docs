<template>
  <div>
    <h1>SignUp</h1>
    <div>
      <label for="username">사용자 계정:</label>
      <input type="text" id="username" v-model="userdata.username" />
    </div>
    <div>
      <label for="last_name">성:</label>
      <input type="text" id="last_name" v-model="userdata.last_name" />
    </div>
    <div>
      <label for="first_name">이름:</label>
      <input type="text" id="first_name" v-model="userdata.first_name" />
    </div>
    <div>
      <label for="email">e-mail:</label>
      <input type="text" id="email" v-model="userdata.email" />
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
    <!-- <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p> -->
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
        // errorMessage: null,
      }
    }
  },
  methods: {
    signup: function () {
      const password = this.userdata.password
      const passwordConfirm = this.userdata.passwordConfirm
      // console.log(password)
      // console.log(passwordConfirm)
      if (password !== passwordConfirm) {
        // this.errorMessage = '비밀번호가 일치하지 않습니다.';
        alert('비밀번호가 일치하지 않습니다.')
        this.userdata.password = ''
        this.userdata.passwordConfirm = ''
        return;
      }

      axios({
        method: "post",
        // reqest 500 url: "http://127.0.0.1:8000/accounts/signup /가 빠져서..
        url: URL + "accounts/signup/",
        data: this.userdata,
      })
      .then(() => {
        this.$router.push({ name: 'Login' })
      })
      .catch((error) => {
        if (error.response && error.response.data && error.response.data.error) {
            // 중복된 ID 에러 메시지 처리
            if (error.response.status === 400 && error.response.data.error === '중복된 ID입니다.') {
              alert('중복된 ID입니다.');
              this.userdata.username = ''
              this.userdata.password = ''
              this.userdata.passwordConfirm = ''
            } else {
              alert('오류가 발생했습니다.');
            }
          } else {
            alert('오류가 발생했습니다.');

        if (error.response && error.response.data && error.response.data.error) {
            this.errorMessage = error.response.data.error;
          } else {
            this.errorMessage = '오류가 발생했습니다.';
          }

        this.userdata.username = ''
        this.userdata.password = ''
        this.userdata.passwordConfirm = ''

        // console.log(this.error) 비밀번호가 일치하지 않는데 저장이 안됨
          }
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