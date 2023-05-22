<template>
  <div id="app">
    <div id="nav" v-if="isLogin">
      <div id=AboutMovie>
        <span>
          <router-link :to="{ name: 'home' }"><img src="./assets/Logo_new.png"></router-link>
        </span>
        <span>
          <router-link :to="{ name: 'movie' }">Movie</router-link>
        </span>
        <span>
          <router-link :to="{ name: 'recommend' }">Recommend</router-link>
        </span>
      </div>
      <div id="AboutAccount">
        <span>
          <router-link :to="{ name: 'Profile', query : {user: this.$store.state.username} }">안녕하세요, {{$store.state.username}}</router-link>
        </span>
        <span>
          <router-link to="#" @click.native="logout">Logout</router-link>
        </span>
      </div>
    </div>

    <div id="nav" v-else>
      <div id=AboutMovie>
        <span>
          <router-link :to="{ name: 'home' }"><img id="logo" src="./assets/Logo_new.png"></router-link>
        </span>
        <span>
          <router-link :to="{ name: 'movie' }">Movie</router-link>
        </span>
        <span>
          <router-link :to="{ name: 'recommend' }">Recommend</router-link>
        </span>
      </div>
      <div id="AboutAccount">
        <span>
          <router-link :to="{ name: 'Signup' }">Signup</router-link>
        </span>
        <span>
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
      // isMySessionActive: false
    }
  },
  methods: {
    logout() {
      this.isLogin = false
      this.$store.dispatch('Logout_delete')
      // localStorage.removeItem('jwt')
      this.$router.push({name:'Login'})
    },
    // onLoad() {
    //   window.localStorage.setItem("isMySessionActive", true);
    // },
    // onUnload(event) {
    //   window.localStorage.setItem("isMySessionActive", false);
    //   // this.$store.dispatch('Logout_delete_username');
    //   localStorage.removeItem('jwt');
    //   event.returnValue = "";
    // }
    
  },
  created() {
    const token = this.$store.state.access_token
    if (token) {
      this.isLogin = true
    }
  },
  // beforeMount() {
  //   window.addEventListener("load", this.onLoad);
  //   window.addEventListener("beforeunload", this.onUnload);
  // },
  // beforeDestroy() {
  //   window.removeEventListener("load", this.onLoad);
  //   window.removeEventListener("beforeunload", this.onUnload);
  // },
}
</script>

<style>
/* http://meyerweb.com/eric/tools/css/reset/ 
   v2.0 | 20110126
   License: none (public domain)
*/

html, body {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
a {
  text-decoration-line: none;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}
span {
  margin: auto;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0 auto;
  padding: 0 auto;
}

#logo {
  width: 140px;
  /* height: 30px; */
}

#nav {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-content: center;
  /* width: 100%; */
  /* height: 50px; */
  /* background-color: black; */
  padding: 20px;
  font-size: 20px;
}

#nav a {
  font-weight: bold;
  color: black; 
}

#nav a.router-link-exact-active {
  color: #FFDF00;
}

#AboutAccount {
  display: flex;
  width: 180px;
  justify-content: space-between;
  align-content: center;
  margin-right: 20px;
}

#AboutMovie {
  display: flex;
  width: 380px;
  justify-content: space-between;
}

.ableToClick {
  cursor: pointer;
}
</style>
