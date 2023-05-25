<template>
  <div class="inner">
    <div class="row">
      <div class="col" id="optionbox">
        <h1>필터 선택</h1>
        <div class="col" id="check">
          <div class="row box">
            <span class="optionspan">
              <label for="Adventure" class="ableToClick"><input type="checkbox" name="genre" id="Adventure" value="Adventure" class="ableToClick"> Adventure</label>
            </span>
            <span class="optionspan">
              <label for="Fantasy" class="ableToClick"><input type="checkbox" name="genre" id="Fantasy" value="Fantasy" class="ableToClick"> Fantasy</label>
            </span>
          </div>
          <div class="row box">
            <span class="optionspan">
              <label for="Animation" class="ableToClick"><input type="checkbox" name="genre" id="Animation" value="Animation" class="ableToClick"> Animation</label>
            </span>
            <span class="optionspan">
              <label for="Drama" class="ableToClick"><input type="checkbox" name="genre" id="Drama" value="Drama" class="ableToClick"> Drama</label>
            </span>
          </div>
          <div class="row box">
            <span class="optionspan">
              <label for="Horror" class="ableToClick"><input type="checkbox" name="genre" id="Horror" value="Horror" class="ableToClick"> Horror</label>
            </span>
            <span class="optionspan">
              <label for="Action" class="ableToClick"><input type="checkbox" name="genre" id="Action" value="Action" class="ableToClick"> Action</label>
            </span>
          </div>
          <div class="row box">
            <span class="optionspan">
              <label for="Comedy" class="ableToClick"><input type="checkbox" name="genre" id="Comedy" value="Comedy" class="ableToClick"> Comedy</label>
            </span>
            <span class="optionspan">              
              <label for="History" class="ableToClick"><input type="checkbox" name="genre" id="History" value="History" class="ableToClick"> History</label>
            </span>
          </div>
          <div class="row box">
            <span class="optionspan">
              <label for="Western" class="ableToClick"><input type="checkbox" name="genre" id="Western" value="Western" class="ableToClick"> Western</label>
            </span>
            <span class="optionspan">
              <label for="Thriller" class="ableToClick"><input type="checkbox" name="genre" id="Thriller" value="Thriller" class="ableToClick"> Thriller</label>
            </span>
          </div>
          <div class="row box">
            <span class="optionspan">
              <label for="Crime" class="ableToClick"><input type="checkbox" name="genre" id="Crime" value="Crime" class="ableToClick"> Crime</label>
            </span>
            <span class="optionspan">
              <label for="Documentary" class="ableToClick"><input type="checkbox" name="genre" id="Documentary" value="Documentary" class="ableToClick"> Documentary</label>
            </span>
          </div>
          <div class="row box">
            <span class="optionspan">
              <label for="Science Fiction" class="ableToClick"><input type="checkbox" name="genre" id="Science Fiction" value="Science Fiction" class="ableToClick"> Science Fiction</label>
            </span>
            <span class="optionspan">
              <label for="Mystery" class="ableToClick"><input type="checkbox" name="genre" id="Mystery" value="Mystery" class="ableToClick"> Mystery</label>
            </span>
          </div>
          <div class="row box">
            <span class="optionspan">
              <label for="Music" class="ableToClick"><input type="checkbox" name="genre" id="Music" value="Music" class="ableToClick"> Music</label>
            </span>
            <span class="optionspan">
              <label for="Romance" class="ableToClick"><input type="checkbox" name="genre" id="Romance" value="Romance" class="ableToClick"> Romance</label>
            </span>
          </div>
          <div class="row box">
            <span class="optionspan">
              <label for="Family" class="ableToClick"><input type="checkbox" name="genre" id="Family" value="Family" class="ableToClick"> Family</label>
            </span>
            <span class="optionspan">
              <label for="War" class="ableToClick"><input type="checkbox" name="genre" id="War" value="War" class="ableToClick"> War</label>
            </span>
          </div>
          <div class="row box">
            <span class="optionspan">
              <label for="TV Movie" class="ableToClick"><input type="checkbox" name="genre" id="TV Movie" value="TV Movie" class="ableToClick"> TV Movie</label>
            </span>
          </div>
        </div><br>
        <div>
          <div class="clearfilter" @click="filterReset"><p class="choicetext">Reset</p></div>
        </div>
        <div style="margin: 20px 10px auto;">
          <div class="completechoice" @click="getchoiceMovies"><p class="choicetext">Choose</p></div>
        </div>
      </div>
      <div class="col" id="movielists">
        <div class="wrappling">
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

    filterReset() {
      const checkboxes = document.querySelectorAll('input[type="checkbox"]');
  
      checkboxes.forEach((checkbox) => {
        checkbox.checked = false
      })
    },

    getchoiceMovies() {
      const checkbox = document.getElementsByName('genre')
      const selectedGenres = []
      checkbox.forEach(item => {
        if(item.checked) {
          selectedGenres.push(item.value)
          // item.checked = false
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
.ableToClick {
  cursor: pointer;
}

#optionbox {
  position: absolute;
  border: 3px solid white;
  border-radius: 7px;
  width: 370px;
  top: 190px;
  left: 170px;
  height: 680px;
}

#check {
  display: flex;
  margin: 10px 0px 0px 23px;
  padding: 0 auto;
  justify-content: space-evenly;
  font-size: 20px;
}

#movielists {
  position: absolute;
  width: 60%;
  left: 570px;
  border-radius: 7px;
}

.wrappling {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-between;
  padding: 30px;
}

.box {
  margin: 10px 0px auto;
  justify-content: left;
}

.optionspan {
  width: 170px;
  height: 33px;
  text-align: left;
}


.clearfilter{
  width: 100px;
  height: 35px;
  background-color: grey;
  color: white;
  border-radius: 7px;
  margin-left: auto;
  margin-right: 10px;
  align-content: center;
  font-size: 23px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  text-align: center;
  /* 이거 가운데 정렬 말한거지? */
  padding-top: 15px;
  padding-bottom: auto;
}

.clearfilter:hover {
  transition: all 0.2s linear;
  transform: scale(1.05);
  background-color: red;
}

.completechoice {
  width: 100%;
  height: 50px;
  background-color: grey;
  color: white;
  border-radius: 7px;
  align-content: center;
  font-size: 35px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  padding-top: 15px;
  padding-bottom: auto;
}

.completechoice:hover {
  transition: all 0.2s linear;
  transform: scale(1.05);
  background-color: rgb(26, 187, 53);
}

.choicetext {
  margin: 0px 0px auto;
}
</style>
