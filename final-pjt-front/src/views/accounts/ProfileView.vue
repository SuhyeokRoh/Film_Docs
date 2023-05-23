<template>
  <div class="inner" v-if="User">
    <div class="row">
      <div class="col contain private">
        <h1>{{User.nickname}}님의 정보</h1>
        <p>User Id : {{User.username}}</p>
        <p>User Email : {{User.email}}</p>
        <p>User First Name : {{User.first_name}}</p>
        <p>User Last Name : {{User.last_name}}</p>
        <p>User Nick Name : {{User.nickname}}</p>
        <button>회원정보 수정</button>

        <div class="col">
          <div class="row follow">
            <p> 팔로워 : {{ follower }} </p>
            <p>팔로잉 : {{ following }} </p>
          </div>
          <button @click="followPerson">follow / 취소</button>
        </div>
      </div>

      <div class="col contain trace">
        <div class="col contain likemovie">
          <h3>{{User.nickname}}님이 좋아요 누른 영화</h3>
          <div class="row posterlist">
            <span class="posterbox" v-for="movie in User.movielike" :key="movie.id">
                <div class="OnePoster">
                  <div class="card ableToClick" @click="gotoDetail(movie)">
                    <div class="front"><img class="likeposter" :src="movie.poster_path_original" ></div>
                    <div class="back">{{movie.title}}</div>
                  </div>
                </div>
            </span>
          </div>
        </div>
        <div class="row">
          <div class="col contain division">
            <h3>{{User.nickname}}님이 좋아요 누른 리뷰</h3>
            <div class="output" v-for="likereview in User.like_reviews" :key="likereview.id">
              <p>{{likereview.movie.title}} - {{likereview.content}}</p>
            </div>
          </div>
          <div class="col contain division">
            <h3>{{User.nickname}}님이 좋아요 누른 댓글</h3>
            <div class="output" v-for="likereview in User.like_reviews" :key="likereview.id">
              <p>{{likereview.movie.title}} - {{likereview.content}}</p>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col contain division">
            <h3>{{User.nickname}}님이 남긴 리뷰</h3>
            <div class="output" v-for="review in User.review_set" :key="review.id">
              <p>movie_title : {{ review.movie.title }}</p>
              <p>content : {{ review.content }}</p>
            </div>
          </div>
          <div class="col contain division">
            <h3>{{User.nickname}}님이 남긴 댓글</h3>
            <div class="output" v-for="comment in User.comment_set" :key="comment.id">
              <p>movie_title : {{ comment.movie_title }} </p>
              <p>review : {{ comment.review_content }}</p>
              <p>content : {{ comment.content }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const URL = "http://127.0.0.1:8000"
export default {
  name: 'ProfileView',
  data() {
    return {
        queryData: null,
        User: null,
        movieTitle: null,
        following: null,
        follower: null,
        isfollowed: false,
    }
  },
  mounted() {
    // this.followPerson()
    this.getUser()
  },
  methods: {
    setToken: function() {
      const token = this.$store.state.access_token
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },

    getUser() {
      const username = this.$route.query.user
      axios({
        method: 'get',
        url: `${URL}/accounts/${username}/profile/`,
        headers: this.setToken()
      })
      .then((res) => {
        // console.log(res.data)
        this.User = res.data
        this.following = res.data.followings.length
        this.follower = res.data.followers.length
        // console.log(this.User)
      })
      .catch((err) => console.log(err))
    },

    followPerson() {
      const username = this.$route.query.user
      
      axios({
        method: 'post',
        url: `${URL}/accounts/${username}/profile/follow/`,
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        // 여기서 키중복 경고가 발생함 그러나 follow 실시간 반영을 위해 일단 남겨두었음
        this.follower = res.data.followers.length
      })
      .catch((err) => {
        alert(err.response.data.err)
        })
    },

    gotoDetail(select_movie) {
      const movie = select_movie

      this.$router.push({name: 'moviedetail', query : {data: JSON.stringify({movie: movie, })}})
    }

  },
  created() {
    this.getUser()
  },
}
</script>

<style>

.OnePoster {
  position: relative;
  width: 133.33px;
  height: 200px;
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
  line-height: 200px;
  font-size: 10px;
  transform: rotateY(180deg);
}

.private {
  width: 25%;
  height: 500px;
  margin: 0px auto;
  margin-right: 20px;
}

.trace {
  width: 70%;
  margin: 0px auto;
}

.follow {
  justify-content: space-evenly;
}

.likemovie {
  width: 90%;
}

.division {
  width: 45%;
  justify-content: space-evenly;
}

.posterlist {
  width: 100%;
  height: 250px;
  overflow: auto;
  text-align: center;
  overflow-y: hidden;
}

.posterbox {
  margin: 5px 20px;
}

.likeposter {
  height: 200px;
  border-radius: 7px;
  margin: auto;
}

.output {
  border: solid 1px black;
  border-radius: 7px;
  width: 80%;
  margin: 10px auto;
}
</style>