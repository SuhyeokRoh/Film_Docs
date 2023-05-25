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
        <button v-if="is_my_profile" @click="withdrawalChange">회원 탈퇴</button>
        <div class="black-bg" v-if="this.drawalVal == true">
          <div class="white-bg col">
            <h1>계정을 삭제하시겠습니까?</h1>
            <div class="row buttons">
              <span>
                <button class="deletebutton" @click="Deleteaccount">Yes</button>
              </span>
              <span>
                <button class="deletebutton" @click="withdrawalChange">No</button>
              </span>
            </div>
          </div>
        </div>

        <div class="col">
          <div class="row follow">
            <p> 팔로워 : {{ follower }} </p>
            <p>팔로잉 : {{ following }} </p>
          </div>
          <div v-if="is_my_profile"></div>
          <div v-else>
            <button @click="followPerson">
            <p v-if="isfollowed">취소</p>
            <p v-else>follow</p>
          </button>
          </div>
          
        
        </div>
      </div>

      <div class="col contain trace">
        <div class="col contain likemovie">
          <h3>{{User.nickname}}님이 좋아요 누른 영화</h3>
          <div class="row likeposterlist">
            <span class="posterbox" v-for="movie in User.movielike" :key="movie.id">
                <div class="TwoPoster">
                  <div class="card ableToClick" @click="gotoDetail(movie)">
                    <div class="frontprofile"><img class="likeposter" :src="movie.poster_path_original" ></div>
                    <div class="backprofile">{{movie.title}}</div>
                  </div>
                </div>
            </span>
          </div>
        </div>
        <div class="row">
          <div class="col contain division">
            <h3>{{User.nickname}}님이 좋아요 누른 리뷰</h3>
            <div class="output ableToClick" v-for="likereview in User.like_reviews" :key="likereview.id" @click="gotoDetailReview(likereview)">
              <p>{{likereview.movie.title}} - {{likereview.content}}</p>
            </div>
          </div>
          <div class="col contain division">
            <h3>{{User.nickname}}님이 좋아요 누른 댓글</h3>
            <div class="output ableToClick" v-for="likecomment in User.comment_set" :key="likecomment.id">
              <p>{{likecomment.movie.title}} - {{likecomment.content}}</p>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col contain division">
            <h3>{{User.nickname}}님이 남긴 리뷰</h3>
            <div class="output ableToClick" v-for="review in User.review_set" :key="review.id" @click="gotoDetail(review.movie)">
              <p>movie_title : {{ review.movie.title }}</p>
              <p>content : {{ review.content }}</p>
            </div>
          </div>
          <div class="col contain division">
            <h3>{{User.nickname}}님이 남긴 댓글</h3>
            <div class="output ableToClick" v-for="comment in comments" :key="comment.id">
              <p>movie_title : {{ comment.movie.title }} </p>
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
      isfollowed: true,
      comments: null,

      is_my_profile: false,
      drawalVal: false,
      UpdateVal: false,
    }
  },
  mounted() {
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

    withdrawalChange() {
      this.drawalVal = !this.drawalVal
    },

    Deleteaccount() {
      const username = this.$store.state.username

      axios({
        method: 'delete',
        url: `${URL}/accounts/${username}/profile/delete/`,
        headers: this.setToken()
      })
      .then(() => {
        this.$store.dispatch('Logout_delete')
        this.$router.replace({name:'home'})
      })
      .catch(err => console.log(err))
    },

    getUser() {
      const username = this.$route.query.user

      if(username === this.$store.state.username) {
        this.is_my_profile = true
      } else {
        this.is_my_profile = false
      }

      axios({
        method: 'get',
        url: `${URL}/accounts/${username}/profile/`,
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        this.User = res.data
        this.following = res.data.followings.length
        this.follower = res.data.followers.length
        this.comments = res.data.comment_set
        this.isfollowed = false
        this.User.followers.forEach(element => {
          if (element.username === this.$store.state.username) {
            this.isfollowed = true
            return 
          }
        });
      })
      .catch((err) => console.log(err))
    },

    followPerson() {
      const username = this.$route.query.user
      if (this.isfollowed) {
        this.isfollowed = false
      } else {
        this.isfollowed = true
      }
      
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
    },

    gotoDetailReview(select_review) {
      const key = this.$store.state.access_token
      if(key) {
        const reviews = select_review
        const user = {
          'username' : this.username,
          'nickname' : this.nickname,
        }
        this.$router.push({name: 'reviewdetail', query : {data: JSON.stringify({reviews: reviews, user: user, })}})
      } else {
        alert('로그인이 필요합니다!')
        this.$router.push({name: 'Login'})
      }
    },

  },
  created() {
    this.getUser()
  },
}
</script>

<style>

.TwoPoster {
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

.frontprofile, .backprofile {
  position: absolute;
  width: 100%; 
  height: 100%;
  backface-visibility: hidden;
}

.TwoPoster:hover .card {
  transform: rotateY(180deg);
}

.backprofile {
  background-color: white;
  color:black;
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

.likeposterlist {
  width: 100%;
  height: 100%;
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

.black-bg {
  width: 1880px;
  height: 860px;
  background: rgba(0,0,0,0.5);
  position: absolute;
  top: 0px;
  left: 0px;
  padding: 20px;
}
.white-bg {
  width: 50%;
  height: 20%;
  background: white;
  position: absolute;
  top: 25%;
  left: 25%;
  border-radius: 8px;
  padding: 20px;
}

.buttons {
  height: 50%;
  margin: auto;
}

.deletebutton {
  width: 100px;
  height: 50px;
  margin: 0 10px auto;
  align-items: center;
}
</style>