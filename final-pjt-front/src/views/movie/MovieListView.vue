<template>
  <div>
    <div>
      <p>옵션</p>
      <p>장르</p>
      <button @click="actionclick">
        <p v-if="isActionclicked">Action</p>
        <p v-else>cancel</p>
        </button>
      <button @click="adventureclick">
        <p v-if="isAdventureclicked">Adventure</p>
        <p v-else>cancel</p>
        </button>
      <button @click="animationclick">
        <p v-if="isAnimationclicked">Animation</p>
        <p v-else>cancel</p>
        </button>
      <button @click="comedyclick">
        <p v-if="isComedyclicked">Comedy</p>
        <p v-else>cancel</p>
        </button>
      <button @click="crimeclick">
        <p v-if="isCrimeclicked">Crime</p>
        <p v-else>cancel</p>
        </button>
      <button @click="documentaryclick">
        <p v-if="isDocumentaryclicked">Documentary</p>
        <p v-else>cancel</p>
        </button>
      <button @click="dramaclick">
        <p v-if="isDramaclicked">Drama</p>
        <p v-else>cancel</p>
        </button>
      <button @click="familyclick">
        <p v-if="isFamilyclicked">Family</p>
        <p v-else>cancel</p>
        </button>
      <button @click="fantasyclick">
        <p v-if="isFantasyclicked">Fantasy</p>
        <p v-else>cancel</p>
        </button>
      <button @click="historyclick">
        <p v-if="isHistoryclicked">History</p>
        <p v-else>cancel</p>
        </button>
      <button @click="horrorclick">
        <p v-if="isHorrorclicked">Horror</p>
        <p v-else>cancel</p>
        </button>
      <button @click="musicclick">
        <p v-if="isMusicclicked">Music</p>
        <p v-else>cancel</p>
      </button>
      <button @click="mysteryclick">
        <p v-if="isMysteryclicked">Mystery</p>
        <p v-else>cancel</p>
      </button>
      <button @click="romanceclick">
        <p v-if="isRomanceclicked">Romance</p>
        <p v-else>cancel</p>
      </button>
      <button @click="SFclick">
        <p v-if="isScience_Fictionclicked">Science Fiction</p>
        <p v-else>cancel</p>
      </button>
      <button @click="tvmovieclick">
        <p v-if="isTV_Movieclicked">TV Movie</p>
        <p v-else>cancel</p>
      </button>
      <button @click="thrillerclick">
        <p v-if="isThrillerclicked">Thriller</p>
        <p v-else>cancel</p>
      </button>
      <button @click="warclick">
        <p v-if="isWarclicked">War</p>
        <p v-else>cancel</p>
      </button>
      <button @click="westernclick">
        <p v-if="isWesternclicked">Western</p>
        <p v-else>cancel</p>
      </button>
    </div>
    <div>
      <p>평점</p>
    </div>
    <div>
      <p>인기도</p>
    </div>
    <ul>
      <MovieItemView v-for="movie in movies" :key="movie.id" 
      :movie="movie" />
    </ul>
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
      isActionclicked: false,
      isAdventureclicked: false,
      isAnimationclicked: false,
      isComedyclicked: false,
      isCrimeclicked: false,
      isDocumentaryclicked: false,
      isDramaclicked: false,
      isFamilyclicked: false,
      isFantasyclicked: false,
      isHistoryclicked: false,
      isHorrorclicked: false,
      isMusicclicked: false,
      isMysteryclicked: false,
      isRomanceclicked: false,
      isScience_Fictionclicked: false,
      isTV_Movieclicked: false,
      isThrillerclicked: false,
      isWarclicked: false,
      isWesternclicked: false,
    }
  },
  created() {
    this.getMovies()
    // this.getchoiceMovies()
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
    // getchoiceMovies() {
    //   axios({
    //     method: 'get',
    //     url: `${URL}/movies/choice/`,
    //   })
    //   .then(res => {
    //     console.log(res.data)
    //     // this.movies = res.data
    //   })
    //   .catch(err => {
    //     console.log(err)
    //   })
    // },
    choosegenre() {
      const selectedGenres = []
      if (this.isActionclicked) selectedGenres.push('Action')
      if (this.isAdventureclicked) selectedGenres.push('Adventure')
      if (this.isAnimationclicked) selectedGenres.push('Animation')
      if (this.isComedyclicked) selectedGenres.push('Comedy')
      if (this.isCrimeclicked) selectedGenres.push('Crime')
      if (this.isDocumentaryclicked) selectedGenres.push('Documentary')
      if (this.isDramaclicked) selectedGenres.push('Drama')
      if (this.isFamilyclicked) selectedGenres.push('Family')
      if (this.isFantasyclicked) selectedGenres.push('Fantasy')
      if (this.isHistoryclicked) selectedGenres.push('History')
      if (this.isHorrorclicked) selectedGenres.push('Horror')
      if (this.isMusicclicked) selectedGenres.push('Music')
      if (this.isMysteryclicked) selectedGenres.push('Mystery')
      if (this.isRomanceclicked) selectedGenres.push('Romance')
      if (this.isScience_Fictionclicked) selectedGenres.push('Science Fiction')
      if (this.isTV_Movieclicked) selectedGenres.push('TV Movie')
      if (this.isThrillerclicked) selectedGenres.push('Thriller')
      if (this.isWarclicked) selectedGenres.push('War')
      if (this.isWesternclicked) selectedGenres.push('Western')

      if (selectedGenres.length === 0) {
        // 모든 장르의 영화를 출력
        // this.getchoiceMovies()
        this.getMovies()
      } else {
        // 선택된 장르의 영화만 출력
        axios({
          method: 'get',
          url: `${URL}/movies/choice/`,
          params: {
            genre: selectedGenres.join(',')
          }
        })
        .then(res => {
          // console.log(res.data)
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
    actionclick() {
      if (this.isActionclicked) {
        this.isActionclicked = false
      } else {
        this.isActionclicked = true
      }
      console.log(this.isActionclicked)
    },
    adventureclick() {
      if (this.isAdventureclicked) {
        this.isAdventureclicked = false
      } else {
        this.isAdventureclicked = true
      }
    },
    animationclick() {
      if (this.isAnimationclicked) {
        this.isAnimationclicked = false
      } else {
        this.isAnimationclicked = true
      }
    },
    comedyclick() {
      if (this.isComedyclicked) {
        this.isComedyclicked = false
      } else {
        this.isComedyclicked = true
      }
    },
    crimeclick() {
      if (this.isCrimeclicked) {
        this.isCrimeclicked = false
      } else {
        this.isCrimeclicked = true
      }
    },
    documentaryclick() {
      if (this.isDocumentaryclicked) {
        this.isDocumentaryclicked = false
      } else {
        this.isDocumentaryclicked = true
      }
    },
    dramaclick() {
      if (this.isDramaclicked) {
        this.isDramaclicked = false
      } else {
        this.isDramaclicked = true
      }
    },
    familyclick() {
      if (this.isFamilyclicked) {
        this.isFamilyclicked = false
      } else {
        this.isFamilyclicked = true
      }
    },
    fantasyclick() {
      if (this.isFantasyclicked) {
        this.isFantasyclicked = false
      } else {
        this.isFantasyclicked = true
      }
    },
    historyclick() {
      if (this.isHistoryclicked) {
        this.isHistoryclicked = false
      } else {
        this.isHistoryclicked = true
      }
    },
    horrorclick() {
      if (this.isHorrorclicked) {
        this.isHorrorclicked = false
      } else {
        this.isHorrorclicked = true
      }
    },
    musicclick() {
      if (this.isMusicclicked) {
        this.isMusicclicked = false
      } else {
        this.isMusicclicked = true
      }
    },
    mysteryclick() {
      if (this.isMysteryclicked) {
        this.isMysteryclicked = false
      } else {
        this.isMysteryclicked = true
      }
    },
    romanceclick() {
      if (this.isRomanceclicked) {
        this.isRomanceclicked = false
      } else {
        this.isRomanceclicked = true
      }
    },
    SFclick() {
      if (this.isScience_Fictionclicked) {
        this.isScience_Fictionclicked = false
      } else {
        this.isScience_Fictionclicked = true
      }
    },
    tvmovieclick() {
      if (this.isTV_Movieclicked) {
        this.isTV_Movieclicked = false
      } else {
        this.isTV_Movieclicked = true
      }
    },
    thrillerclick() {
      if (this.isThrillerclicked) {
        this.isThrillerclicked = false
      } else {
        this.isThrillerclicked = true
      }
    },
    warclick() {
      if (this.isWarclicked) {
        this.isWarclicked = false
      } else {
        this.isWarclicked = true
      }
    },
    westernclick() {
      if (this.isWesternclicked) {
        this.isWesternclicked = false
      } else {
        this.isWesternclicked = true
      }
    },
  }
}
</script>

<style>

</style>
