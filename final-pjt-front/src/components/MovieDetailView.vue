<template>
  <div id="movie_detail" v-if="queryData">
    <div>
      <img id="backimage" :src="queryData.movie.backdrop_path_original" >
      <iframe id="trailer" :src="queryData.movie.trailerUrl" width="500" height="255" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen></iframe>
    </div>
    <div class="row">
      <div class="col" id="left">
        <img id="poster" :src="queryData.movie.poster_path_500" >
      </div>
      <div class="col" id="right">
        <p id="title">{{ queryData.movie.title }}</p>
        <div class="row container">
          <p>개봉일 : {{ queryData.movie.release_date }}</p>
          <p>인기도 : {{ queryData.movie.popularity }}</p>
        </div>
        <div class="row container">
          <p>투표수 : {{ queryData.movie.vote_count }}</p>
          <p>투표 평점 : {{ queryData.movie.vote_average }}</p>
        </div>
        <p>줄거리 : {{ queryData.movie.overview }}</p>
        <div class="row container">
          장르 : <p v-for="(genre,index) in getGenreData" :key="index">{{ genre.name }}</p>
        </div>
        <div class="row container">
          <div>
            <button v-if="like_state" @click="likeMovie">
              <p v-if="dislike_state">좋아요</p>
              <p v-else>좋아요 취소</p>
              </button>
            <p>좋아요 수 : {{like_user.length}}</p>
          </div>
          <div>
            <button v-if="dislike_state" @click="dislikeMovie">
              <p v-if="like_state">싫어요</p>
              <p v-else>싫어요 취소</p>
              </button>
            <p>싫어요 수 : {{dislike_user.length}}</p>
          </div>
        </div>
        <div class="col">
          <label for="review_title">제목 </label>
          <input type="text" id="review_title" v-model="NewReviewTitle"><br>
          <label for="review_content">리뷰 내용</label>
          <textarea id="review_content" cols="30" rows="5" v-model="NewReviewContent" @keyup.enter="createReview"></textarea><br>
          <button @click="createReview">리뷰 등록</button>
          <div>
            <ReviewItemView 
            v-for="review in Reviews" :key="review.id"
            :review="review" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewItemView from './ReviewItemView.vue'
import axios from 'axios'

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
  },
  computed: {
    getGenreData() {
      return this.Genre
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

    getMovieLike() {
      const movieid = this.queryData.movie.id
      const user_name = this.$store.state.username
      axios({
        method: 'get',
        url: `${URL}/movies/${movieid}/`,
      })  
      .then(res => {
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
      })
      .catch(err => console.log(err))
    },

    createReview: function() {
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
        // headers: this.setToken()
      })
      .then((res) => {
        this.Genre = res.data.genres
      })
      .catch((err) => {
        console.log(err)
      })
    },

    likeMovie() {
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
  },
}
</script>

<style>
#movie_detail {
  width: 1280px;
  margin: 10px auto;
  /* border: solid 3px black;
  border-radius: 7px; */
}

#backimage{
  width: 1280px;
  height: 600px;
  /* filter: blur(1px); */
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
  justify-content: space-around;
}

#left {
  position: relative;
  top: -450px;
  padding: 20px;
  width: 30%
}
#right {
  position: relative;
  top: -450px;
  padding: 20px;
  width: 70%
}

#trailer{
  position: relative;
  width: 650px;
  height: 450px;
  top: -550px;
  left: 250px
}

#poster {
  position: relative;
  width: 300px;
  object-fit: cover;
  top: -150px;  
  left: 15px;
}

#title {
  font-size: 50px;
  text-align: left;
  padding-left: 20px;
}
</style>