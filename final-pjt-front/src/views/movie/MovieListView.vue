<template>
  <div>
    <button @click="getchoiceMovies">옵션 적용</button>
    <div id="optionbox">
      <p>장르</p>
      <hr>
      <span @click="actionclick">
        <p v-if="isActionclicked">Action</p>
        <p v-else>cancel</p>
      </span>
      <span @click="adventureclick">
        <p v-if="isAdventureclicked">Adventure</p>
        <p v-else>cancel</p>
        </span>
      <span @click="animationclick">
        <p v-if="isAnimationclicked">Animation</p>
        <p v-else>cancel</p>
        </span>
      <span @click="comedyclick">
        <p v-if="isComedyclicked">Comedy</p>
        <p v-else>cancel</p>
        </span>
      <span @click="crimeclick">
        <p v-if="isCrimeclicked">Crime</p>
        <p v-else>cancel</p>
        </span>
      <span @click="documentaryclick">
        <p v-if="isDocumentaryclicked">Documentary</p>
        <p v-else>cancel</p>
        </span>
      <span @click="dramaclick">
        <p v-if="isDramaclicked">Drama</p>
        <p v-else>cancel</p>
        </span>
      <span @click="familyclick">
        <p v-if="isFamilyclicked">Family</p>
        <p v-else>cancel</p>
        </span>
      <span @click="fantasyclick">
        <p v-if="isFantasyclicked">Fantasy</p>
        <p v-else>cancel</p>
        </span>
      <span @click="historyclick">
        <p v-if="isHistoryclicked">History</p>
        <p v-else>cancel</p>
        </span>
      <span @click="horrorclick">
        <p v-if="isHorrorclicked">Horror</p>
        <p v-else>cancel</p>
        </span>
      <span @click="musicclick">
        <p v-if="isMusicclicked">Music</p>
        <p v-else>cancel</p>
      </span>
      <span @click="mysteryclick">
        <p v-if="isMysteryclicked">Mystery</p>
        <p v-else>cancel</p>
      </span>
      <span @click="romanceclick">
        <p v-if="isRomanceclicked">Romance</p>
        <p v-else>cancel</p>
      </span>
      <span @click="SFclick">
        <p v-if="isScience_Fictionclicked">Science Fiction</p>
        <p v-else>cancel</p>
      </span>
      <span @click="tvmovieclick">
        <p v-if="isTV_Movieclicked">TV Movie</p>
        <p v-else>cancel</p>
      </span>
      <span @click="thrillerclick">
        <p v-if="isThrillerclicked">Thriller</p>
        <p v-else>cancel</p>
      </span>
      <span @click="warclick">
        <p v-if="isWarclicked">War</p>
        <p v-else>cancel</p>
      </span>
      <span @click="westernclick">
        <p v-if="isWesternclicked">Western</p>
        <p v-else>cancel</p>
      </span>
    </div>
    <div>
      <p>평점</p>
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
      selectedGenres : [],
      isActionclicked: true,
      isAdventureclicked: true,
      isAnimationclicked: true,
      isComedyclicked: true,
      isCrimeclicked: true,
      isDocumentaryclicked: true,
      isDramaclicked: true,
      isFamilyclicked: true,
      isFantasyclicked: true,
      isHistoryclicked: true,
      isHorrorclicked: true,
      isMusicclicked: true,
      isMysteryclicked: true,
      isRomanceclicked: true,
      isScience_Fictionclicked: true,
      isTV_Movieclicked: true,
      isThrillerclicked: true,
      isWarclicked: true,
      isWesternclicked: true,
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
    getchoiceMovies() {
  
      if (this.isActionclicked) {
        this.selectedGenres.push('Action')
        } else {
          const valueToRemove = 'Action'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }

      if (this.isAdventureclicked) {
        this.selectedGenres.push('Adventure')
      } else {
          const valueToRemove = 'Adventure'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }

      if (this.isAnimationclicked) {
        this.selectedGenres.push('Animation')
        } else {
          const valueToRemove = 'Animation'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isComedyclicked) {
        this.selectedGenres.push('Comedy')
      } else {
          const valueToRemove = 'Comedy'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isCrimeclicked) {
        this.selectedGenres.push('Crime')
        } else {
          const valueToRemove = 'Crime'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isDocumentaryclicked) {
        this.selectedGenres.push('Documentary')
        } else {
          const valueToRemove = 'Documentary'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isDramaclicked) {
        this.selectedGenres.push('Drama')
        } else {
          const valueToRemove = 'Drama'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isFamilyclicked) {
        this.selectedGenres.push('Family')
        } else {
          const valueToRemove = 'Family'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isFantasyclicked) {
        this.selectedGenres.push('Fantasy')
        } else {
          const valueToRemove = 'Fantasy'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isHistoryclicked) {
        this.selectedGenres.push('History')
        } else {
          const valueToRemove = 'History'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isHorrorclicked) {
        this.selectedGenres.push('Horror')
        } else {
          const valueToRemove = 'Horror'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isMusicclicked) {
        this.selectedGenres.push('Music')
        } else {
          const valueToRemove = 'Music'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isMysteryclicked) {
        this.selectedGenres.push('Mystery')
        } else {
          const valueToRemove = 'Mystery'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isRomanceclicked) {
        this.selectedGenres.push('Romance')
        } else {
          const valueToRemove = 'Romance'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isScience_Fictionclicked) {
        this.selectedGenres.push('Science Fiction')
        } else {
          const valueToRemove = 'Science Fiction'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isTV_Movieclicked) {
        this.selectedGenres.push('TV Movie')
        } else {
          const valueToRemove = 'TV Movie'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isThrillerclicked) {
        this.selectedGenres.push('Thriller')
        } else {
          const valueToRemove = 'Thriller'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isWarclicked) {
        this.selectedGenres.push('War')
        } else {
          const valueToRemove = 'War'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      if (this.isWesternclicked) {
        this.selectedGenres.push('Western')
        } else {
          const valueToRemove = 'Western'
          for(let i = 0; i < this.selectedGenres.length; i++){
            if (this.selectedGenres[i] === valueToRemove) {
              this.selectedGenres.splice(i, 1);
              i--;
            }
          }
        }
      // 초기값으로 넣어지는 것 확인
      console.log(this.selectedGenres)
      
      axios({
        method: 'get',
        url: `${URL}/movies/choice/`,
        params: { genres: this.selectedGenres.join(',') }, // 선택한 장르 정보를 쿼리 파라미터로 전달
      })
      .then(res => {
        console.log(res)
        this.movies = res.data
      })
      .catch(err => {
        console.log(err)
      })
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
#optionbox {
  border: 3px solid black;
}
</style>
