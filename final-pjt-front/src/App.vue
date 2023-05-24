<template>
  <div id="app">
    <div id="nav" v-if="isLogin">
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
        <span>
          <router-link :to="{ name: 'search' }">Search</router-link>
        </span>
        <span>
          <router-link :to="{ name: 'worldcup' }">worldcup</router-link>
        </span>
      </div>
      <div id="AboutAccount">
        <span>
          <router-link :to="{ name: 'Profile', query : {user: this.$store.state.username} }">Hi, {{$store.state.username}}님</router-link>
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
        <span>
          <router-link :to="{ name: 'search' }">Search</router-link>
        </span>
        <span>
          <router-link :to="{ name: 'worldcup' }">worldcup</router-link>
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
    }
  },
  methods: {
    logout() {
      this.isLogin = false
      this.$store.dispatch('Logout_delete')
      // localStorage.removeItem('jwt')
      this.$router.push({name:'Login'})
    },
  },
  created() {
    const token = this.$store.state.access_token
    if (token) {
      this.isLogin = true
    }
  },
}
</script>

<style>


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
  font-size: 25px;
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
  padding: auto;
  display: block; 
  /* justify-content: center; */
  text-align: center;
}
img{
  border-radius: 7px;
}
p{
  font-size: 20px;
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
  width: 200px;
  /* height: 30px; */
}

#nav {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-content: center;
  padding: 30px 20px;
}

#nav a {
  font-weight: bold;
  color: black; 
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
  display: flex;
  width: 400px;
  justify-content: space-between;
  align-content: center;
  margin-right: 100px;
}

#AboutMovie {
  display: flex;
  width: 800px;
  justify-content: space-between;
  margin-left: 50px;
}

.ableToClick {
  cursor: pointer;
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
  border: solid 1px black;
  border-radius: 7px;
  margin: 20px auto;
}
</style>
