<template>
  <div>
    <h1 class="cup-h1">Movie Cup!</h1>
    <div>
      <button id="rebtn" @click="call_WorldCup_data">처음부터 시작</button>
      <div>
        <div @click="pickworldcup"></div>
        <div class="worldcup-container">
          <div class="cup-OnePoster ableToClick">
            <div class="cup-card" @click="clickLeft">
              <div class="cup-front"><img class="cup-posterlist" :src="this.random_movies[0].poster_path_original" ></div>
              <div class="cup-back">{{this.random_movies[0].title}}</div>
            </div>
          </div>
          <h1>VS</h1>
          <div class="cup-OnePoster ableToClick">
            <div class="cup-card" @click="clickRight">
              <div class="cup-front"><img class="cup-posterlist" :src="this.random_movies[1].poster_path_original" ></div>
              <div class="cup-back">{{this.random_movies[1].title}}</div>
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
        
        const movie = this.random_movies[0]
        alert(`선택한 영화는 ${movie.title} 입니다. ${movie.title}의 상세페이지로 이동합니다!`)
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

#rebtn {
  background:#1AAB8A;
  color:#fff;
  border:none;
  position:relative;
  height:60px;
  font-size:1.6em;
  padding:0 2em;
  cursor:pointer;
  transition:800ms ease all;
  outline:none;
}
#rebtn:hover{
  background:#fff;
  color:#1AAB8A;
}
#rebtn:before,#rebtn:after{
  content:'';
  position:absolute;
  top:0;
  right:0;
  height:2px;
  width:0;
  background: #1AAB8A;
  transition:400ms ease all;
}
#rebtn:after{
  right:inherit;
  top:inherit;
  left:0;
  bottom:0;
}
#rebtn:hover:before,#rebtn:hover:after{
  width:100%;
  transition:800ms ease all;
}

.cup-h1 {
  font-weight: bold;
  font-size: 70px;
}
.worldcup-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
  margin-top: 40px;
}

.cup-OnePoster {
  margin: 10px;
  width: 600px;
  height: 500px;
  position: relative;
}

.cup-posterlist {
  width: 100%;
  height: 100%;
}

.cup-card {
  height: 100%;
  width: 100%;
  position: relative;
  transition: 1s;
  transform-style: preserve-3d;
}

.cup-front,
.cup-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}

.cup-OnePoster:hover .cup-card {
  transform: rotateY(180deg);
}

.cup-back {
  background-color: white;
  color: black;
  border-radius: 7px;
  line-height: 350px;
  font-size: 20px;
  transform: rotateY(180deg);
}
</style>

