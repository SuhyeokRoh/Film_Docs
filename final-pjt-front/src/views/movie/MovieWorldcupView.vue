<template>
  <div>
    <h1>Movie World Cup!</h1>
    <div>
      <button @click="call_WorldCup_data">처음부터 시작</button>
      <div>
        <button @click="pickworldcup">누르지 마세요</button>
        <div class="worldcup-container">
          <div class="OnePoster ableToClick">
            <div class="card" @click="clickLeft">
              <div class="front"><img class="posterlist" :src="this.random_movies[0].poster_path_original" ></div>
              <div class="back">{{this.random_movies[0].title}}</div>
            </div>
          </div>
          <div class="OnePoster ableToClick">
            <div class="card" @click="clickRight">
              <div class="front"><img class="posterlist" :src="this.random_movies[1].poster_path_original" ></div>
              <div class="back">{{this.random_movies[1].title}}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
// import _ from 'lodash'
import axios from 'axios'
const URL = "http://127.0.0.1:8000"


export default {
  name: 'MovieWorldcupView',
  data: function() {
    return {
      worldcup_arr : [],
      worldcup_movie: null,
      current_round: [],
      next_round: [],
      roundNum: 16,
      left: null,
      right: null,
      finishFlag: false,
      random_movies: [],
    }
  },
  methods: {
    setToken: function() {
      const token = this.$store.state.access_token
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },
    ConfirmLogin() {
      const user = this.$store.state.username
      if (!user) {
        alert("로그인이 필요합니다.")
        this.$router.push({name: 'Login'})
      }
    },
    call_WorldCup_data() {
      axios({
            method: 'get',
            url: `${URL}/movies/worldcup/`,
            headers: this.setToken(),
        })
        .then((res) => {
            console.log(res.data)
            this.random_movies = res.data
        })
        .catch((err) => {
            console.log(err)
        })
    },
    pickworldcup() {
      const rdMovies = this.random_movies
      // console.log(rdMovies)
      const worldcup = []
      worldcup.push(rdMovies[0])
      worldcup.push(rdMovies[1])
      // console.log(worldcup)
      // console.log(randomMovies)
      this.random_movies = worldcup
      console.log(this.random_movies)
    },
    worldcupres() {
      if (this.random_movies.length === 1) {
        alert('수고하셨습니다!')
        const movie = this.random_movies[0]
        this.$router.push({name: 'moviedetail', query : {data: JSON.stringify({movie: movie, })}})
      }

    },
    clickLeft() {
      const index = 1
      this.random_movies.splice(index,1)
      this.worldcup_arr.push(this.random_movies[0])
      console.log(this.worldcup_arr)
      this.worldcupres()
    },
    clickRight() {
      const index = 0
      this.random_movies.splice(index,1)
      this.worldcup_arr.push(this.random_movies[1])
      console.log(this.worldcup_arr)
      this.worldcupres()
    },
    next() {
      this.left = this.current_round.pop()
      this.right = this.current_round.pop()
    },
  },
  created() {
    this.call_WorldCup_data()
  },
  mounted() {
    this.ConfirmLogin()
  },
}
</script>

<style>
.worldcup-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
}

.OnePoster {
  margin: 10px;
  width: 230px;
  height: 345px;
  position: relative;
}

.posterlist {
  width: 100%;
  height: 100%;
}

.card {
  height: 100%;
  width: 100%;
  position: relative;
  transition: 1s;
  transform-style: preserve-3d;
}

.front,
.back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}

.OnePoster:hover .card {
  transform: rotateY(180deg);
}

.back {
  background-color: white;
  color: black;
  border-radius: 7px;
  line-height: 350px;
  font-size: 20px;
  transform: rotateY(180deg);
}
</style>

