<template>
  <div id="app">
    <div id="nav">

      <span v-if="isLogin">
        <router-link :to="{ name: 'movie' }">Movie</router-link> | 
        <router-link :to="{ name: 'Profile', query : {user: this.$store.state.username} }">Profile</router-link> |
        <router-link to="#" @click.native="logout">Logout</router-link>
      </span>

      <span v-else>
        <router-link :to="{ name: 'movie' }">Movie</router-link> | 
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </span>

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
      isMySessionActive: false
    }
  },
  methods: {
    logout() {
      this.isLogin = false
      this.$store.dispatch('Logout_delete_username')
      localStorage.removeItem('jwt')
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
    const token = localStorage.getItem('jwt')
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
