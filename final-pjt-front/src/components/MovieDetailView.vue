<template>
  <div class="inner" v-if="queryData">
    <div>
      <img id="backimage" :src="queryData.movie.backdrop_path_original" >
    </div>
    <div class="row lowerbox">
      <div class="col" id="left">
        <img id="poster" :src="queryData.movie.poster_path_original" >
        <div>
          <h1 class="trailertitle">예고편</h1>
          <iframe id="trailer" :src="queryData.movie.trailerUrl" width="500" height="255" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
        </div>
      </div>
      <div class="col" id="right">
        <p id="title">{{ queryData.movie.title }}</p>
        <div style="border-bottom: solid 1px white; height: 3px; width:100%; margin-bottom: 10px;"></div>
        <div class="row container_update">
          <div class="col textbox">
            <h1 style="color: #ed8b13;">개봉일</h1>
            <p> {{ queryData.movie.release_date }}</p>
          </div>
          <div class="col textbox">
            <h1 style="color: #ed8b13;">인기도</h1>
            <p>{{ queryData.movie.popularity }}</p>
          </div>
          <div class="col textbox">
            <h1 style="color: #ed8b13;">투표수</h1>
            <p>{{ queryData.movie.vote_count }}</p>
          </div>
          <div class="col textbox">
            <h1 style="color: #ed8b13;">투표 평점</h1>
            <p>{{ queryData.movie.vote_average }}</p>
          </div>
        </div>
        <div class="col textboxtitle">
          <h1 style="color: #ed8b13;">줄거리</h1>
          <p class="overviewtextbox">{{ queryData.movie.overview }}</p>
        </div>
        <div class="col textboxtitle">
          <h1 style="color: #ed8b13;">장르</h1>
          <div class="row genrebox">
            <div v-for="(genre,index) in getGenreData" :key="index">
              <p> {{ genre.name }} </p>
            </div>
          </div>
        </div>
        <div class="col textboxtitle">
          <h1 style="color: #ed8b13;">배급사</h1>
          <div class="row pro_box">
            <div v-for="production in queryData.movie.production_companies" :key="production.id">
              <p>{{production.name}}</p>
            </div>
          </div>
        </div>
        <div class="col textboxtitle">
          <h1 style="color: #ed8b13;">출연 배우</h1>
          <vueper-slides
            class="no-shadow"
            :visible-slides="3"
            :slide-ratio="1 / 4"
            :dragging-distance="70"
            fixed-height="300px">
            <vueper-slide v-for="actor in queryData.movie.actor" :key="actor.id">
              <template #content>
                <div class="actorimagebox">
                  <img @click="gotoActorPage(actor)" class="vueperslide__content-wrapper ableToClick actorprofile" :src="actor.profile_path">
                </div>
              </template>
            </vueper-slide>
          </vueper-slides>
        </div>
        <div class="row container">
          <div style="padding-left: 265px;">
            <div v-if="like_state">
              <font-awesome-icon class="ableToClick likeheart" v-if="dislike_state" @click="likeMovie" size="2xl" :icon="['far', 'heart']" style="color: #ff0000;" />
              <font-awesome-icon class="ableToClick likeheart" v-else @click="likeMovie" size="2xl" :icon="['fas', 'heart']" style="color: #ff0000;" />
            </div>
            <p>like : {{like_user.length}}</p>
          </div>
          <div style="padding-right: 250px;">
            <div v-if="dislike_state">
              <font-awesome-icon class="ableToClick unlikex" v-if="like_state" @click="dislikeMovie" :icon="['far', 'circle-xmark']" size="2xl" style="color: #001df5;" />
              <font-awesome-icon class="ableToClick unlikex" v-else @click="dislikeMovie" :icon="['fas', 'circle-xmark']" size="2xl" style="color: #001df5;" />
            </div>
            <p>unlike : {{dislike_user.length}}</p>
          </div>
        </div>
        <div class="col textboxtitle">
          <h1 style="color: #ed8b13;">사용자 영화 리뷰</h1>
          <div class="col inputbox">
            <h2>리뷰 작성란</h2>
            <div class="row">
              <label for="review_title"><h3>제목 : </h3></label>
              <input type="text" id="review_title" v-model="NewReviewTitle" placeholder="제목을 입력해주세요"><br>
            </div>
            <div class="row">
              <label for="review_content"><h3>리뷰 내용 : </h3></label>
              <textarea id="review_content" cols="30" rows="5" v-model="NewReviewContent" @keyup.enter="createReview" placeholder="내용을 입력해주세요"></textarea><br>
              <button @click="createReview">리뷰 등록</button>
            </div>
          </div>
          <div>
            <h1>달린 리뷰</h1>
            <div v-if="is_review_find">
              <ReviewItemView
              v-for="review in Reviews" :key="review.id"
              :review="review" />
            </div>
            <div v-else>
              <p>아직 달린 리뷰가 없어요</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewItemView from './ReviewItemView.vue'
import axios from 'axios'
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

// const key = 'e66fa81c4a87396b24dd94a15cc7a8b1'
const URL = "http://127.0.0.1:8000"
export default {
  name: "MovieDetailView",
  data() {
    return {
      queryData: null,
      NewReviewTitle: '',
      NewReviewContent: '',
      Genre: null,
      Reviews: null,
      is_review_find: false,

      like_state: true,
      dislike_state: true,
      like_user: [],
      dislike_user: [],
    }
  },
  mounted() {
    this.queryData = JSON.parse(this.$route.query.data)
    this.getGenre()
    this.getReview()
    this.getMovieLike()
  },
  components: {
    ReviewItemView,
    VueperSlides,
    VueperSlide 
  },
  computed: {
    getGenreData() {
      return this.Genre
    }
  },
  methods: {
    ConfirmLogin() {
      const user = this.$store.state.username
      if (!user) {
        alert("로그인이 필요합니다.")
        return this.$router.push({name: 'Login'})
      }
    },

    setToken: function() {
      const token = this.$store.state.access_token
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },

    getMovieLike() {
      const movieid = this.queryData.movie.id
      const user_name = this.$store.state.username
      axios({
        method: 'get',
        url: `${URL}/movies/${movieid}/`,
      })  
      .then(res => {
        // console.log(res.data)
        this.like_user = res.data.movie_like_users
        this.dislike_user = res.data.movie_dislike_users
        const like_user = this.like_user
        const dislike_user = this.dislike_user

        const like = like_user.find(element => {
          if (element.username === user_name) {
            return true;
          }
        })

        const dislike = dislike_user.find(element => {
          if (element.username === user_name) {
            return true;
          }
        })

        if (like) {
          this.dislike_state = false
        }
        if (dislike) {
          this.like_state = false
        }
      })
      .catch(err => console.log(err))
    },

    getReview() {
      const movieid = this.queryData.movie.id
      axios({
        method: 'get',
        url: `${URL}/movies/${movieid}/reviews/`,
      })  
      .then(res => {
        this.Reviews = res.data
        if (this.Reviews.length) {
          this.is_review_find = true
        }
      })
      .catch(err => console.log(err))
    },

    createReview: function() {
      this.ConfirmLogin()

      const movieid = this.queryData.movie.id
      if (!this.NewReviewTitle) {
        this.NewReviewContent = ''
        this.NewReviewTitle = ''
        alert("제목을 입력해주세요")
        return ;
      }

      if (!this.NewReviewContent) {
        this.NewReviewContent = ''
        this.NewReviewTitle = ''
        alert("내용을 입력해주세요")
        return ;
      }
      
      axios({
        method: "post",
        url: `${URL}/movies/${movieid}/reviews/create/`,
        data: { 
          'title':this.NewReviewTitle,
          'content':this.NewReviewContent,
          'movie':movieid},
        headers: this.setToken()
      })
      .then(() => {
        this.getReview()
        this.NewReviewContent = ''
        this.NewReviewTitle = ''
        
      }).catch((err) => {
        console.log(err)
      })
    },

    getGenre: function() {
      const movieid = this.queryData.movie.id 
      axios({
        method: "get",
        url: `${URL}/movies/${movieid}/`,
      })
      .then((res) => {
        this.Genre = res.data.genres
      })
      .catch((err) => {
        console.log(err)
      })
    },

    likeMovie() {
      this.ConfirmLogin()

      const movieid = this.queryData.movie.id 

      axios({
        method: "post",
        url: `${URL}/movies/${movieid}/like/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.like_user = res.data.movie_like_users
        this.dislike_state = !this.dislike_state
      }).catch((err) => {
        console.log(err)
      })
    },

    dislikeMovie() {
      this.ConfirmLogin()
      
      const movieid = this.queryData.movie.id 

      axios({
        method: "post",
        url: `${URL}/movies/${movieid}/dislike/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.dislike_user = res.data.movie_dislike_users
        this.like_state = !this.like_state
      }).catch((err) => {
        console.log(err)
      })
    },

    gotoActorPage(select_actor) {
      const actor = select_actor

      this.$router.push({name: 'actor', query: {data: JSON.stringify({actor: actor, })}})
    }
  },
}
</script>

<style scoped>

#backimage{
  width: 1280px;
  height: 700px;
}

.container_update {
  justify-content: space-between;
  align-content: center;
}

.ableToClick {
  cursor: pointer;
}

.row {
  display: flex;
  flex-direction: row;
}
.col {
  display: flex;
  flex-direction: column;
}
.container {
  justify-content: space-evenly;
}

.lowerbox {
  width: 66.3%;
  position: absolute;
}

.textbox {
  width: 100%;
  text-align: left;
  align-items: center;
}

.textboxtitle {
  width: 100%;
  text-align: left;
  padding-left: 20px;
  align-items: left;
  align-content: center;
}

.overviewtextbox {
  word-spacing : 5px;
  line-height: 1.5;
}

#left {
  position: relative;
  top: -0px;
  padding: 20px;
  width: 28%
}

#right {
  position: relative;
  top: -10px;
  padding: px;
  width: 68%
}

#trailer{
  position: relative;
  width: 400px;
  height: 300px;
  left: -30px;
  top: 0px;
}

.trailertitle {
  position: absolute;
  top: 350px;
  left: 140px;
}

#poster {
  position: relative;
  width: 300px;
  object-fit: cover;
  top: -200px;  
  left: 30px;
}

#title {
  font-size: 50px;
  text-align: left;
  padding-left: 20px;
}

.a_box {
  height: 300px;
  align-items: center;
  overflow: auto;
  overflow-y: hidden;
}

.vueperslides {
  justify-content: center;
  align-content: center;
}

.actorbox {
  width: 80%;
  height: 250px;
  margin: 10px auto;
}

.actorimagebox {
  width: 220px;
  height: 220px;
  margin: 10px 10px auto;
  justify-content: center;
  align-content: center;
}

.actorprofile {
  width: 220px;
  height: 220px;
  border-radius: 70%;
  object-fit: cover;
  cursor: pointer;
}

.actorprofile:hover {
  transition: all 0.3s linear;
  transform: scale(1.1);
}

.pro_box {
  height: 100px;
  align-items: center;
  justify-content: space-evenly;
}


.proimagebox {
  width: 300px;
  height: 300px;
  margin: 0 auto;
  align-content: center;
}

.production {
  width: 100%;
  height: 100%;
  border-radius: 30%;
  object-fit: cover;
  overflow: hidden;
}

.likeheart:hover {
  transition: all 0.3s linear;
  transform: scale(1.5);
}

.unlikex:hover {
  transition: all 0.3s linear;
  transform: scale(1.5);
}

.genrebox {
  justify-content: space-evenly;
}

.vueperslides__track-inner{
  cursor: default;
}

#review_title {
  margin-left: 30px;
  width: 70%;
  height: 40px;
  border: none;
  border-bottom: dashed 2px orange;
  background-color: black;
  color: white;
  font-size: 15px;
}


#review_content {
  margin-top: 10px;
  margin-left: 30px;
  margin-right: 10px;
  width: 70%;
  height: 40px;
  border: none;
  border-bottom: dashed 2px orange;
  background-color: black;
  color: white;
  font-size: 18px;
}

.inputbox {
  margin-bottom: 20px;
}
</style>