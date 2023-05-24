<template>
  <div v-if="queryData" class="inner">
    <div class="col reviewcontent">
      <div v-if="is_review_user" class="row reviewupdate">
        <div class="row updatebutton">
          <span>
            <button @click="changeupdate_state">리뷰 수정하기</button>
          </span>
          <span>
            <button @click="deleteReview">삭제</button>
          </span>
        </div>
      </div>
      <div class="col">

        <div v-if="isReviewupdate">
          <div>
            <h1 class="title">{{queryData.reviews.title}}</h1>
          </div>
          <div class="row titleuser">
            <p>영화 : {{queryData.reviews.movie.title}}</p>
            <p class="ableToClick" @click="gotoProfile">작성자 : {{queryData.user.nickname}}</p>
          </div>
          <div class="reviewText">
            <p style="margin: 15px 15px auto;">{{queryData.reviews.content}}</p>
          </div>
        </div>

        <div v-else>
          <div class="row">
            <label for="review">review title 수정하기 : </label>
            <input type="text" id="review" v-model="updatereviewtitle">
          </div>
          <div class="row">
            <label for="review">review content 수정하기 : </label>
            <input type="text" id="review" v-model="updatereviewcontent">
          </div>
          <button @click="updateReview">리뷰 수정</button>
        </div>

        <div class="row likebutton">
          <div class="col reviewlikebutton">
            <p>좋아요 : {{like_reviews.length}}</p>
            <button v-if="like_state" @click="likeReview">
              <p v-if="dislike_state">좋아요</p>
              <p v-else>좋아요 취소</p>
            </button>
          </div>
          <div class="col reviewlikebutton">
            <p>싫어요 : {{dislike_reviews.length}}</p>
            <button v-if="dislike_state" @click="dislikeReview">
              <p v-if="like_state">싫어요</p>
              <p v-else>싫어요 취소</p>
            </button>
          </div>
        </div>

      </div>
    </div>
    <div class="col reviewcontent contain">
      <div>
        <label for="comment">댓글 남기기 : </label>
        <input type="text" id="comment" v-model="commentContent" @keyup.enter="saveComment">
        <button @click="saveComment">입력</button>
      </div>
      <div class="col">
        <div v-for="comment in comments" :key="comment.id" class="commentbox">
          <div v-if="isCommentupdate">
            <div>
              <p>{{comment.content}}</p>
            </div>
            <div>
              <span class="ableToClick" @click="gotoProfile">작성자 : {{comment.user.nickname}}</span>
            </div>
            <div class="row commentlikebutton">
              <div class="col commentbutton">
                <p>좋아요 : {{like_comments.length}}</p>
                <button v-if="comment_like_state" @click="likeComment(comment)">
                  <p v-if="comment_dislike_state">좋아요</p>
                  <p v-else>좋아요 취소</p>
                </button>
              </div>
              <div class="col commentbutton">
                <p>싫어요 : {{dislike_comments.length}}</p>
                <button v-if="comment_dislike_state" @click="dislikeComment(comment)">
                  <p v-if="comment_like_state">싫어요</p>
                  <p v-else>싫어요 취소</p>
                </button>
              </div>
            </div>
            <div class="row commentupdate">
              <div v-if="is_comment_user(comment)" class="row updatebutton">
                <span>
                  <button @click="changeupdate_comment_state(comment)">댓글 수정 하기</button>
                </span>
                <span>
                  <button @click="deleteComment(comment)">삭제</button>
                </span>
              </div>
            </div>
          </div>
          <div v-else>
            <label for="comment">comment 수정하기 : </label>
            <input type="text" id="comment" v-model="updatecomment">
            <button @click="updateComment(comment)">댓글 수정</button>
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
  name: 'ReviewDetailView',
  data() {
    return {
      queryData: null,
      like_reviews: [],
      dislike_reviews: [],
      like_comments: [],
      dislike_comments: [],

      comment_up_state_arr: [],

      is_review_user: false,

      like_state: true,
      dislike_state: true,
      isReviewupdate: true,
      isCommentupdate: true,
      comment_like_state:true,
      comment_dislike_state:true,
      updatereviewtitle : null,
      updatereviewcontent : null,
      commentContent: null,
      updatecomment: null,
      comments: [],
    }
  },
  mounted() {
    this.queryData = JSON.parse(this.$route.query.data)
    this.getReviewLike()
    this.comments = this.getComment()
    this.confirmUser()
  },
  created() {
    
  },
  methods: {
    setToken: function() {
      const token = this.$store.state.access_token
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },

    confirmUser() {
      if (this.queryData.user.username === this.$store.state.username) {
        this.is_review_user = true
      }
    },

    is_comment_user(select_comment) {
      if (select_comment.user.username === this.$store.state.username) {
        return true;
      } else {
        return false;
      }
    },

    getReviewLike() {
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id
      const user_name = this.queryData.user.username

      axios({
        method: 'get',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.like_reviews = res.data.like_users
        this.dislike_reviews = res.data.dislike_users
        const like_reviews = this.like_reviews
        const dislike_reviews = this.dislike_reviews

        const like = like_reviews.find(element => {
          if (element.username === user_name) {
            return true;
          }
        })

        const dislike = dislike_reviews.find(element => {
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
      .catch((err) => console.log(err))
    },

    likeReview() {
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id

      axios({
        method: 'post',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/like/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.like_reviews = res.data.like_users
        this.dislike_state = !this.dislike_state
      })
      .catch((err) => console.log(err))
    },

    dislikeReview() {
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id

      axios({
        method: 'post',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/dislike/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.dislike_reviews = res.data.dislike_users
        this.like_state = !this.like_state
      })
      .catch((err) => console.log(err))
    },

    getComment() {
      console.log(this.comment_up_state_arr)
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id
      axios({
        method: 'get',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/comment/`,
        headers: this.setToken(),
      })
      .then((res) => {
        this.comments = res.data
        console.log(this.comments)
        // this.like_comments = res.data.like_comment_users
        // this.dislike_comments = res.data.dislike_comment_users
      })
      .catch(err => console.log(err))
    },

    saveComment() {
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id
      const content = this.commentContent
      console.log()

      axios({
        method: 'post',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/comment/create/`,
        data: { 
          'movie': movieid,
          'review': reviewid,
          'content': content,
        },
        headers: this.setToken(),
      })
      .then(() => {
        this.getComment()
        this.commentContent = ''
        
      })
      .catch(err => console.log(err))
    },

    gotoProfile() {
      const username = this.queryData.user.username
      this.$router.push({name: 'Profile', query : {user: username}})
    },

    deleteReview: function () {
      const movie = this.queryData.reviews.movie
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id
    
      axios({
        method: 'delete',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/update/`,
        headers: this.setToken()

      }).then(res => {
          console.log(res, reviewid)
          this.$router.push({name: 'moviedetail', query : {data: JSON.stringify({movie: movie, })}})
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteComment: function (comment) {
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id
    
      axios({
        method: 'delete',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/comment/${comment.id}/update`,
        headers: this.setToken()

      }).then(res => {
          console.log(res, comment)
          this.getComment()
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateReview: function () {
      // console.log(this.queryData.reviews)
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id
      
      this.isReviewupdate = false
      axios({
        method: 'put',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/update/`,
        headers: this.setToken(),
        data: {
          title: this.updatereviewtitle, content: this.updatereviewcontent, movie:movieid,
        },

      }).then(res => {
          console.log(res, reviewid)
          this.queryData.reviews.title = res.data.title
          this.queryData.reviews.content = res.data.content
          this.isReviewupdate = true
        })
        .catch(err => {
          console.log(err)
          alert('본인 댓글만 수정 가능합니다.')
          this.isReviewupdate = true
        })
    },
    updateComment: function (comment) {
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id
      
      this.isCommentupdate = false

      axios({
        method: 'put',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/comment/${comment.id}/update/`,
        headers: this.setToken(),
        data: {
          movie:movieid,
          review:reviewid,
          user:comment.user,
          content: this.updatecomment,
        }

      }).then(res => {
          console.log(res, this.comments)
          comment.content = res.data.content
          this.isCommentupdate = true
        })
        .catch(err => {
          console.log(err)
          alert('본인 댓글만 수정 가능합니다.')
          this.isCommentupdate = true
        })
    },
    changeupdate_state() {
      if (this.isReviewupdate) {
        this.isReviewupdate = false
      }

    },
    changeupdate_comment_state() {
    if (this.isCommentupdate) {
        this.isCommentupdate = false
      }
    },

    likeComment(comment) {
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id
      // console.log(comment)
      axios({
        method: 'post',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/comment/${comment.id}/like/`,
        headers: this.setToken()
      })
      .then((res) => {
        // console.log(res)
        this.like_comments = res.data.like_comment_users
        this.comment_dislike_state = !this.comment_dislike_state
        // this.getCommentLike(comment)
      })
      .catch((err) => console.log(err))
     },
    
    dislikeComment(comment) {
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id

      axios({
        method: 'post',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/comment/${comment.id}/dislike/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.dislike_comments = res.data.dislike_comment_users
        this.comment_like_state = !this.comment_like_state
        // this.getCommentLike(this.comment)
      })
      .catch((err) => console.log(err))
    },
  }
}
</script>

<style>
.reviewcontent {
  margin: auto;
  width: 1176px;
  margin-top: 20px;
  margin-bottom: 20px;
}

.updatebutton {
  width: 200px;
  height: 70px;
  /* margin: 0 auto; */
  justify-content: space-evenly;
}

.commentbox {
  width: 80%;
  margin: auto;
  margin-top: 10px;
  margin-bottom: 10px;
  border: solid 1px black;
  border-radius: 7px;
}

.reviewupdate {
  margin-left: auto;
}

.commentupdate {
  /* margin-left: auto; */
  justify-content:flex-end;
}

.likebutton {
  margin: 0 auto;
}

.commentlikebutton {
  justify-content: center;
}

.commentbutton {
  margin: 10px 10px auto;
}

.reviewlikebutton {
  margin: 10px 10px auto;
}

.title {
  text-align: left;
  margin-left: 50px;
  font-size: 40px;
}

.titleuser {
  justify-content: space-between;
  margin: 0px 50px auto;
  font-size: 20px;
}

.reviewText {
  text-align: left;
  margin: 10px 50px;
  font-size: 15px;
  min-height: 300px;
  border: solid 2px black;
  border-radius: 7px;
}
</style>