<template>
  <div id="app">
    <div id="nav">
      <div id=AboutMovie>
        <span>
          <router-link :to="{ name: 'movie' }">Movie</router-link>
        </span>
        <span>
          <router-link :to="{ name: 'recommend' }">Recommend</router-link>
        </span>
        <span>
          <router-link :to="{ name: 'search' }">Search</router-link>
        </span>
        <span>
          <router-link :to="{ name: 'worldcup' }">Worldcup</router-link>
        </span>
      </div>
      <div class="LogoCenter">
        <span>
          <router-link :to="{ name: 'home' }"><img id="logo" src="./assets/Logo_new.png"></router-link>
        </span>
      </div>
      <div id="AboutAccount">
        <span v-if="isLogin">
          <router-link :to="{ name: 'Profile', query : {user: this.$store.state.username} }">Profile</router-link>
        </span>
        <span v-else>
          <router-link :to="{ name: 'Signup' }">Signup</router-link>
        </span>
        <span v-if="isLogin">
          <router-link to="#" @click.native="logout">Logout</router-link>
        </span>
        <span v-else>
          <router-link :to="{ name: 'Login' }">Login</router-link> 
        </span>
      </div>
    </div>
    <router-view @login="isLogin=true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout() {
      this.isLogin = false
      this.$store.dispatch('Logout_delete')
      this.$router.push({name:'Login'})
    },

    confirmLogin() {
      const token = this.$store.state.access_token
      if (token) {
        this.isLogin = true
      } else {
        this.isLogin = false
      }
    }
  },
  created() {
    this.confirmLogin()
  },
  updated() {
    this.confirmLogin()
  }
}
</script>

<style>
@font-face {
    font-family: 'KOTRA_BOLD-Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10-21@1.1/KOTRA_BOLD-Bold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

* {
	font-family: 'KOTRA_BOLD-Bold';
}

html, body {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	vertical-align: baseline;
  background-color: black;
}
a {
  text-decoration-line: none;
  font-size: 25px;
}
body {
	line-height: 1;
}
p {
  font-size: 20px;
}

.ableToClick {
  cursor: pointer;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  margin: 0 auto;
  padding: 0 auto;
}

#logo {
  width: 300px;
}

#nav {
  display: flex;
  flex-direction: row;
  align-content: center;
  padding: 50px 20px;
}

#nav a {
  font-weight: bold;
  color: white; 
}

#nav a.router-link-exact-active {
  color: #FFDF00;
}

.inner {
  width: 1280px;
  margin: 0px auto;
  margin-top: 50px;
  padding: 0px auto;
  /* border: solid 3px black;
  border-radius: 7px; */
}

#AboutAccount {
  position: absolute;
  display: flex;
  width: 250px;
  top: 65px;
  justify-content: space-between;
  align-content: center;
  margin-right: 100px;
  left: 1480px;
}

#AboutMovie {
  position: absolute;
  display: flex;
  width: 600px;
  top: 65px;
  justify-content: space-between;
  margin-left: 100px;
}

.LogoCenter {
  position: absolute;
  top: 40px;
  left: 810px;
}

.row {
  display: flex;
  flex-direction: row;
}

.col {
  display: flex;
  flex-direction: column;
}

.contain {
  border: solid 1px white;
  border-radius: 7px;
  margin: 20px auto;
}

</style>
