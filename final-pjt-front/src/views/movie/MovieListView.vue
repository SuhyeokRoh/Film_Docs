<template>
  <div class="inner">
    <div class="row">
      <div class="col" id="optionbox">
        <h1>장르</h1>
        <div class="col" id="check">
          <div class="row box">
            <span>
              <input type="checkbox" name="genre" id="Adventure" value="Adventure">Adventure
            </span>
            <span>
              <input type="checkbox" name="genre" id="Fantasy" value="Fantasy">Fantasy
            </span>
          </div>
          <div class="row box">
            <span>
              <input type="checkbox" name="genre" id="Animation" value="Animation">Animation
            </span>
            <span>
              <input type="checkbox" name="genre" id="Drama" value="Drama">Drama
            </span>
          </div>
          <div class="row box">
            <span>
              <input type="checkbox" name="genre" id="Horror" value="Horror">Horror
            </span>
            <span>
              <input type="checkbox" name="genre" id="Action" value="Action">Action
            </span>
          </div>
          <div class="row box">
            <span>
              <input type="checkbox" name="genre" id="Comedy" value="Comedy">Comedy
            </span>
            <span>              
              <input type="checkbox" name="genre" id="History" value="History">History
            </span>
          </div>
          <div class="row box">
            <span>
              <input type="checkbox" name="genre" id="Western" value="Western">Western
            </span>
            <span>
              <input type="checkbox" name="genre" id="Thriller" value="Thriller">Thriller
            </span>
          </div>
          <div class="row box">
            <span>
              <input type="checkbox" name="genre" id="Crime" value="Crime">Crime
            </span>
            <span>
              <input type="checkbox" name="genre" id="Documentary" value="Documentary">Documentary
            </span>
          </div>
          <div class="row box">
            <span>
              <input type="checkbox" name="genre" id="Science Fiction" value="Science Fiction">Science Fiction
            </span>
            <span>
              <input type="checkbox" name="genre" id="Mystery" value="Mystery">Mystery
            </span>
          </div>
          <div class="row box">
            <span>
              <input type="checkbox" name="genre" id="Music" value="Music">Music
            </span>
            <span>
              <input type="checkbox" name="genre" id="Romance" value="Romance">Romance
            </span>
          </div>
          <div class="row box">
            <span>
              <input type="checkbox" name="genre" id="Family" value="Family">Family
            </span>
            <span>
              <input type="checkbox" name="genre" id="War" value="War">War
            </span>
          </div>
          <div class="row box">
            <span>
              <input type="checkbox" name="genre" id="TV Movie" value="TV Movie">TV Movie
            </span>
          </div>
        </div><br>
        <button @click="getchoiceMovies">옵션 적용</button>
      </div>
      <div class="col" id="movielists">
        <div>
          <MovieItemView v-for="movie in movies" :key="movie.id" 
          :movie="movie" />
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import MovieItemView from '@/components/MovieItemView'

const URL = "http://127.0.0.1:8000"
export default {
  name: 'MovieListView',
  components: {
    MovieItemView,
  },
  data: function() {
    return {
      movies: null,
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      axios({
        method: 'get',
        url: `${URL}/movies/`,
      })
      .then(res => {
        console.log(res)
        this.movies = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    getchoiceMovies() {
      const checkbox = document.getElementsByName('genre')
      const selectedGenres = []
      checkbox.forEach(item => {
        if(item.checked) {
          selectedGenres.push(item.value)
        }
      })
      
      axios({
        method: 'get',
        url: `${URL}/movies/choice/`,
        params: { genres: selectedGenres.join(',') }, // 선택한 장르 정보를 쿼리 파라미터로 전달
      })
      .then(res => {
        console.log(res)
        this.movies = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
  }
}
</script>

<style>
#optionbox {
  border: 3px solid black;
  width: 22%;
  height: 600px;
  margin-right: 10px;
}

#check {
  display: flex;
  margin: 0px auto;
  padding: 0 auto;
  justify-content: space-evenly;
  font-size: 20px;
}

#movielists {
  width: 75%;
  margin-left: 10px;
}

.box {
  margin: 10px 0px;
}
</style>
