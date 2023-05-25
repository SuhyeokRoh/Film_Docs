<template>
  <div v-if="actor" class="inner row">
    <div class="col actorMainImage">
      <img class="actormainposter" :src="actor.profile_path">
    </div>
    <div class="col actorcontent">
      <div>
        <h1 class="actorname">{{actor.name}}</h1>
      </div>
      <div class="row conup">
        <div class="col texbox">
          <h1 style="color: #ed8b13;">Gender</h1>
          <p>{{actor.gender}}</p>
        </div>
        <div class="col texbox">
          <h1 style="color: #ed8b13;">Birthday</h1>
          <p>{{birthday}}</p>
        </div>
        <div class="col texbox">
          <h1 style="color: #ed8b13;">Deathday</h1>
          <p v-if="actor.deathday">{{actor.deathday}}</p>
          <p v-else>Still Alive</p>
        </div>
      </div>
      <div class="col elect">
        <h1 class="electitle">Biography</h1>
        <div class="biography">
          <div v-if="actor.biography">
            <p>{{actor.biography}}</p>
          </div>
          <div v-else>
            <p>내용이 없습니다</p>
          </div>
        </div>
      </div>
      <div class="col elect">
        <h1 class="electitle">출연작</h1>
        <!-- <div class="row">
          <span class="comebox" v-for="movie in movies" :key="movie.id">
            <div class="ThreePoster">
              <div class="comecard ableToClick" @click="gotoDetail(movie)">
                <div class="frontcome"><img class="comeposterimg" :src="movie.poster_path_original"></div>
                <div class="backcome">{{movie.title}}</div>
              </div>
            </div>
          </span>
        </div> -->
        <div class="comebox">
          <vueper-slides
            class="no-shadow"
            :visible-slides="3"
            :slide-ratio="1 / 4"
            :dragging-distance="70"
            fixed-height="320px">
            <vueper-slide v-for="movie in movies" :key="movie.id">
              <template #content>
                <div class="ThreePoster">
                  <div class="comecard ableToClick" @click="gotoDetail(movie)">
                    <div class="frontcome"><img class="comeposterimg" :src="movie.poster_path_original"></div>
                    <div class="backcome">{{movie.title}}</div>
                  </div>
                </div>
              </template>
            </vueper-slide>
          </vueper-slides>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

const URL = "http://127.0.0.1:8000"
export default {
  name: 'ActorDetailView',
  data() {
    return {
      actor: null,
      birthday: null,
      movies: null,
    }
  },
  components: {
    VueperSlides,
    VueperSlide 
  },
  mounted() {
    this.actor = JSON.parse(this.$route.query.data).actor
    this.birthday = this.actor.birthday.substr(0, 10)
    this.getMovies()
  },
  methods: {
    getMovies() {
      const actor_pk = this.actor.id

      axios({
        method: 'get',
        url: `${URL}/movies/${actor_pk}/actor/`,
      })
      .then(res => {
        this.movies = res.data.movie_actor
      })
      .catch(err => console.log(err))
    },

    gotoDetail(select_movie) {
      const movie = select_movie

      this.$router.push({name: 'moviedetail', query : {data: JSON.stringify({movie: movie, })}})
    },
  }
}
</script>

<style scoped>


.actorname{
  font: bolder;
  font-size: 45px;
}

.actorMainImage {
  width: 25%;
  margin: 10px auto;
  border-radius: 7px;
}

.actormainposter{
  position: absolute;
  width: 325px;
  border-radius: 7px;
  top: 180px;
}

.conup {
  justify-content: space-between;
  align-content: center;
}

.texbox {
  width: 100%;
  text-align: center;
  padding-left: 20px;
  align-items: left;
  align-content: center;
}

.actorcontent {
  width: 70%;
  margin: 10px auto;
}
.elect{
  text-align: left;
  padding-left: 20px;
}
.electitle{
  font-size: 32px;
  color: #ed8b13;
}
.biography{
  widows: 80%;
  height: 200px;
  margin: 0px 0px auto;
  margin-top: 10px;
  padding: 20px;
  border: solid 1px white;
  border-radius: 7px;
  text-align: left;
}
.comingmovie{
  padding-left: 20px;
  text-align: left;
}

.ThreePoster {
  position: relative;
  width: 200px;
  height: 300px;
  margin: auto;
}

.comebox {
  height: 400px;
}

.comecard {
  height: 100%;
  width: 100%;
  position: relative;
  transition: 1s ;
  transform-style: preserve-3d;
}

.frontcome, .backcome {
  position: absolute;
  width: 100%; 
  height: 100%;
  backface-visibility: hidden;
}

.ThreePoster:hover .comecard {
  transform: rotateY(180deg);
}

.backcome {
  background-color: white;
  color:black;
  border-radius: 7px;
  line-height: 300px;
  font-size: 17px;
  transform: rotateY(180deg);
}
.comeposterimg {
  height: 300px;
  border-radius: 7px;
  margin: 0 0 auto;
  border: solid 1px white;
}
.comeposterlist {
  width: 100%;
  height: 120%;
  overflow: auto;
  text-align: center;
  overflow-y: hidden;
  border: solid 1px white;
  border-radius: 7px;
}
</style>