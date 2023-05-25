<template>
  <div id="signupbox">
    <div id="signup">

    <h1 class="sign_up">SignUp</h1>
    <div id="id">
      <label for="username">ID  </label>
      <input type="text" id="username" v-model="userdata.username" />
    </div>
    <div id="lastname">
      <label for="last_name">성  </label>
      <input type="text" id="last_name" v-model="userdata.last_name" />
    </div>
    <div id="firstname">
      <label for="first_name">이름  </label>
      <input type="text" id="first_name" v-model="userdata.first_name" />
    </div>
    <div id="nickname">
      <label for="nickname">닉네임  </label>
      <input type="text" id="nickname" v-model="userdata.nickname" />
    </div>
    <div id="email">
      <label for="email">e-mail  </label>
      <input type="text" id="email" v-model="userdata.email" />
    </div>
    <div id="pw">
      <label for="password">PW  </label>
      <input type="password" id="password" v-model="userdata.password" />
    </div>
    <div id="pwcf">
      <label for="passwordConfirm">PW 확인</label>
      <input type="password" id="passwordConfirm" v-model="userdata.passwordConfirm" @keyup.enter="signup" />
    </div>
    <button class="btn-5" @click="signup">회원 가입</button>
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
    height: 750px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin:0;
  }

  #signup {
    border-radius: 3px;
    box-shadow: 5px 5px 5px 5px #0f023b;
    width: 500px;
    height: 60%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
  }
  #signup label {
  display: inline-block;
  width: 120px; /* Adjust the width to your preference */
  margin-right: 10px; /* Adjust the right margin to create spacing */
}

.btn-5 {
  width: 130px;
  height: 40px;
  line-height: 42px;
  padding: 0;
  font-weight: bold;
  border-radius: 5px;
  border: none;
  background: rgb(228, 215, 39);
background: linear-gradient(0deg, rgb(228, 215, 39) 0%, rgb(236, 230, 135) 100%);
}
.btn-5:hover {
  color: #f0094a;
  background: transparent;
   box-shadow:none;
}
.btn-5:before,
.btn-5:after{
  content:'';
  position:absolute;
  top:0;
  right:0;
  height:2px;
  width:0;
  background: #f0de3f;
  box-shadow:
   -1px -1px 5px 0px #fff,
   7px 7px 20px 0px #0003,
   4px 4px 5px 0px #0002;
  transition:400ms ease all;
}
.btn-5:after{
  right:inherit;
  top:inherit;
  left:0;
  bottom:0;
}
.btn-5:hover:before,
.btn-5:hover:after{
  width:100%;
  transition:800ms ease all;
}


#signup input {
  margin-bottom: 10px; /* Adjust the bottom margin to create spacing */
}

</style>