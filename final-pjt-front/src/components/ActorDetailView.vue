<template>
  <div v-if="actor" class="inner row contain">
    <div class="col actorMainImage">
      <img :src="actor.profile_path">
    </div>
    <div class="col actorcontent">
      <div>
        <p class="actorname">{{actor.name}}</p>
      </div>
      <div class="row">
        <span>
          {{actor.gender}}
        </span>
        <span>
          {{birthday}}
        </span>
        <span v-if="actor.deathday">
          {{actor.deathday}}
        </span>
      </div>
      <div class="col elect">
        <p class="electitle">Biography</p>
        <div class="biography">
          <div v-if="actor.biography">
            <p>{{actor.biography}}</p>
          </div>
          <div v-else>
            <p>내용이 없습니다</p>
          </div>
        </div>
      </div>
      <div class="col">
        <p class="comingmovie">출연작</p>
        <div class="row comeposterlist">
          <span class="comebox" v-for="movie in movies" :key="movie.id">
            <div class="ThreePoster">
              <div class="comecard ableToClick" @click="gotoDetail(movie)">
                <div class="frontcome"><img class="comeposterimg" :src="movie.poster_path_original"></div>
                <div class="backcome">{{movie.title}}</div>
              </div>
            </div>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

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

<style>
.actorname{
  font: bolder;
  font-size: 35px;
}
.actorMainImage {
  width: 25%;
  margin: 10px auto;
}
.actorcontent {
  width: 70%;
  margin: 10px auto;
}
.elect{
  text-align: left;
}
.electitle{
  padding-left: 20px;
}
.biography{
  widows: 80%;
  height: 200px;
  margin: 0px 0px auto;
  margin-top: 10px;
  padding: 20px;
  border: solid 1px black;
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
}

.comebox {
  margin: 5px 20px;
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
  background-color: black;
  color:white;
  border-radius: 7px;
  line-height: 300px;
  font-size: 17px;
  transform: rotateY(180deg);
}
.comeposterimg {
  height: 300px;
  border-radius: 7px;
  margin: 0 0 auto;
  border: solid 1px black;
}
.comeposterlist {
  width: 100%;
  height: 120%;
  overflow: auto;
  text-align: center;
  overflow-y: hidden;
  border: solid 1px black;
  border-radius: 7px;
}
</style>