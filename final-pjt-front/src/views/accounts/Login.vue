<template>
<div id="LoginBox">
  <div class="col" id="Login">
    <h1>Welcome Back!</h1>
    <br>
    <div class="form-group">
      <label for="username"></label>
      <input type="text" id="username" v-model="userdata.username" class="input-field" placeholder="ID를 입력해주세요!"/>
    </div>
    <div class="form-group">
      <label for="password"></label>
      <input type="password" id="password" v-model="userdata.password" @keyup.enter="login" class="input-field" placeholder="비밀번호를 입력해주세요!"/>
    </div>
    <br>
    <div>
      <button class="btn-5" @click="login">로그인</button>
    </div>
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
  height: 750px;
  display: flex;
  justify-content: center;
  align-items: center;
 }

 #Login {
  border-radius: 3px;
  box-shadow: 5px 5px 5px 5px #0f023b;
  width: 500px;
  height: 60%;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
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


.form-group {
  margin-bottom: 8px;
  padding: 3px;
  border-radius: 3px;
}

.label-left {
  width: 100px;
}

.input-field {
  width: 200px;
}

</style>