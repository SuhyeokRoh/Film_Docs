<template>
  <div>
    <h1>Movie World Cup!</h1>
    <div>
      <button @click="call_WorldCup_data">데이터를 불러주세요</button>
      <div>
        <button @click="pickworldcup">시작</button>
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
</template>


<script>
import _ from 'lodash'
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
      roundNum: 32,
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
    call_WorldCup_data() {
      axios({
            method: 'get',
            url: `${URL}/movies/worldcup/`,
            headers: this.setToken(),
        })
        .then((res) => {
            console.log(res)
            this.current_round.push(res.data)
            this.random_movies = res.data


        })
        .catch((err) => {
            console.log(err)
        })
    },
    pickworldcup() {
      const rdMovies = this.random_movies
      const randomMovies = _.sampleSize(rdMovies, 2)
      console.log(randomMovies)
      this.random_movies = randomMovies
    },
    clickLeft() {
      this.next_round.push(this.left)
      this.left = null
      this.right = null
      this.next()
    },
    clickRight() {
      this.next_round.push(this.right)
      this.left = null
      this.right = null
      this.next()
    },
    next() {
      this.left = this.current_round.pop()
      this.right = this.current_round.pop()
    },
  },
  created() {
    this.call_WorldCup_data()
  }
}
</script>


<style>
.OnePoster {
  position: relative;
  margin-bottom: 30px;
  width: 230px;
  height: 345px;
}

.posterlist {
  width: 100%;
  height: 100%;
}

.card {
  height: 100%;
  width: 100%;
  position: relative;
  transition: 1s ;
  transform-style: preserve-3d;
}


.front, .back {
  position: absolute;
  width: 100%; 
  height: 100%;
  backface-visibility: hidden;
}

.OnePoster:hover .card {
  transform: rotateY(180deg);
}

.back {
  background-color: black;
  color:white;
  border-radius: 7px;
  line-height: 350px;
  font-size: 20px;
  transform: rotateY(180deg);
}

</style>