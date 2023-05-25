<template>
  <div v-if="queryData" class="inner">
    <div class="col reviewcontent">
      <div v-if="is_review_user" class="row reviewupdate">
        <div class="row updatebutton">
          <span>
            <input class="ableToClick reviewupdatebutton" type="button" @click="changeupdate_state" value="리뷰 수정하기" />
          </span>
          <span>
            <input class="ableToClick reviewdeletebutton" type="button" @click="deleteReview" value="삭제" />
          </span>
        </div>
      </div>
      <div class="col">
        <div v-if="isReviewupdate">
          <div>
            <h1 class="title">{{queryData.reviews.title}}</h1>
          </div>
          <div style="border-bottom: solid 2px white; width: 91.5%; margin: auto; margin-bottom: 10px;"></div>
          <div class="row titleuser">
            <p>영화 : {{queryData.reviews.movie.title}}</p>
            <p class="ableToClick" @click="gotoProfile">작성자 : {{queryData.user.nickname}}</p>
          </div>
          <div class="reviewText">
            <p style="margin: 20px 20px auto;">{{queryData.reviews.content}}</p>
          </div>
          <div class="row likebutton">
            <div class="col reviewlikebutton">
              <p>Like : {{like_reviews.length}}</p>
              <div v-if="like_state">
                <font-awesome-icon class="ableToClick likeheart" v-if="dislike_state" @click="likeReview" size="2xl" :icon="['far', 'heart']" style="color: #ff0000;" />
                <font-awesome-icon class="ableToClick likeheart" v-else @click="likeReview" size="2xl" :icon="['fas', 'heart']" style="color: #ff0000;" />
              </div>
            </div>
            <div class="col reviewlikebutton">
              <p>Unlike : {{dislike_reviews.length}}</p>
              <div v-if="dislike_state">
                <font-awesome-icon class="ableToClick unlikex" v-if="like_state" @click="dislikeReview" :icon="['far', 'circle-xmark']" size="2xl" style="color: #001df5;" />
                <font-awesome-icon class="ableToClick unlikex" v-else @click="dislikeReview" :icon="['fas', 'circle-xmark']" size="2xl" style="color: #001df5;" />
              </div>
            </div>
          </div>
          <div class="col reviewcontent">
            <div class="row inputcommentbox">
              <label for="comment_content"><h3>댓글 남기기 : </h3></label>
              <input type="text" id="comment_content" placeholder="댓글을 입력해주세요" v-model="commentContent" @keyup.enter="saveComment" />
              <button class="ableToClick commentcomfirmbutton" style="width: 55px;" @click="saveComment">입력</button>
            </div>
            <div class="col">
              <div v-if="is_comment_find">
                <div v-for="comment in comments" :key="comment.id" class="commentbox">
                  <div v-if="isCommentupdate">
                    <div>
                      <p>{{comment.content}}</p>
                    </div>
                    <div>
                      <span class="ableToClick" @click="gotoProfile">작성자 : {{comment.user.nickname}}</span>
                    </div>
                    <div @click="getCommentLike(comment)" class="row commentlikebutton">
                      <div class="col commentbutton">
                        <p>Like : {{like_comments.length}}</p>
                        <div v-if="comment_like_state">
                          <font-awesome-icon class="ableToClick likeheart" v-if="comment_dislike_state" @click="likeComment(comment)" size="2xl" :icon="['far', 'heart']" style="color: #ff0000;" />
                          <font-awesome-icon class="ableToClick likeheart" v-else @click="likeComment(comment)" size="2xl" :icon="['fas', 'heart']" style="color: #ff0000;" />
                        </div>
                      </div>
                      <div class="col commentbutton">
                        <p>Unlike : {{dislike_comments.length}}</p>
                        <div v-if="comment_dislike_state">
                          <font-awesome-icon class="ableToClick unlikex" v-if="comment_like_state" @click="dislikeComment(comment)" :icon="['far', 'circle-xmark']" size="2xl" style="color: #001df5;" />
                          <font-awesome-icon class="ableToClick unlikex" v-else @click="dislikeComment(comment)" :icon="['fas', 'circle-xmark']" size="2xl" style="color: #001df5;" />
                        </div>
                      </div>
                    </div>
                    <div class="row commentupdate">
                      <div v-if="is_comment_user(comment)" class="row updatebutton">
                        <span>
                          <input class="ableToClick reviewupdatebutton" type="button" @click="changeupdate_comment_state(comment)" value="댓글 수정하기" />
                        </span>
                        <span style="margin-right: 25px;">
                          <input class="ableToClick reviewdeletebutton" type="button" @click="deleteComment(comment)" value="삭제" />
                        </span>
                      </div>
                    </div>
                  </div>
                  <div class="col commentupdatebox" v-else>
                    <div class="row">
                      <label for="commentupdate_content"><h3>comment : </h3></label>
                      <input type="text" id="commentupdate_content" v-model="updatecomment" />
                    </div>
                    <div style="justify-content: center; margin: 30px auto; width: 100%;">
                      <input type="button" class="ableToClick commentupdate_button" @click="updateComment(comment)" value="댓글 수정" />
                    </div>
                  </div>
                </div>
              </div>
              <div v-else>
                <p>아직 달린 댓글이 없어요</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col inputupdatebox" v-else>
          <div class="row">
            <label for="reviewupdate_title"><h3>review title : </h3></label>
            <input type="text" id="reviewupdate_title" v-model="updatereviewtitle" />
          </div>
          <div class="row">
            <label for="reviewupdate_content"><h3>review content : </h3></label>
            <input type="text" id="reviewupdate_content" v-model="updatereviewcontent" />
          </div>
          <div style="justify-content: center; margin: 30px auto; width: 100%;">
            <input type="button" class="ableToClick updatecompletebutton" @click="updateReview" value="리뷰 수정" />
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

      is_comment_find: false,
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
    this.getComment()
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
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id

      axios({
        method: 'get',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/comment/`,
        headers: this.setToken(),
      })
      .then((res) => {
        this.comments = res.data
        if (this.comments.length) {
          this.is_comment_find = true
        } else {
          this.is_comment_find = false
        }
      })
      .catch(err => console.log(err))
    },

    saveComment() {
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id
      const content = this.commentContent

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
          alert('본인 리뷰만 수정 가능합니다.')
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
      axios({
        method: 'post',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/comment/${comment.id}/like/`,
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        this.like_comments = res.data.like_comment_users
        this.comment_dislike_state = !this.comment_dislike_state
        this.getCommentLike(comment)
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
        this.getCommentLike(comment)
      })
      .catch((err) => console.log(err))
    },

    getCommentLike(comment) {
      const movieid = this.queryData.reviews.movie.id
      const reviewid = this.queryData.reviews.id
      const user_name = this.queryData.user.username

      axios({
        method: 'get',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/comment/${comment.id}`,
        headers: this.setToken()
      })
      .then((res) => {
        this.like_comments = res.data.like_comment_users
        this.dislike_comments = res.data.dislike_comment_users
        const like_comments = this.like_comments
        const dislike_comments = this.dislike_comments

        const like = like_comments.find(element => {
            if (element.username === user_name) {
              return true;
            }
          })

        const dislike = dislike_comments.find(element => {
          if (element.username === user_name) {
            return true;
          }
        })

        if (like) {
          this.comment_dislike_state = false
        }
        if (dislike) {
          this.comment_like_state = false
        }
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
  width: 280px;
  height: 70px;
  justify-content: space-between;
}

.reviewupdatebutton {
  text-align: center;
  align-content: center;
  border-radius: 7px;
  width: 120px;
  height: 50px;
  font-size: 15px;
  text-align: center;
}

.reviewupdatebutton:hover {
  background-color: #2d43ed;
  transition: all 0.2s linear;
  transform: scale(1.2);
}

.reviewdeletebutton {
  text-align: center;
  align-content: center;
  border-radius: 7px;
  width: 120px;
  height: 50px;
  font-size: 20px;
  text-align: center;
}

.reviewdeletebutton:hover {
  background-color: #e81c0e;
  transition: all 0.2s linear;
  transform: scale(1.2);
}

.commentbox {
  width: 92%;
  margin: auto;
  margin-top: 10px;
  margin-bottom: 10px;
  border: solid 1px white;
  border-radius: 7px;
}

.reviewupdate {
  margin-top: 50px;
  margin-left: auto;
  margin-right: 50px;
}

.commentupdate {
  justify-content:flex-end;
}

.likebutton {
  justify-content: center;
  margin: 0 auto;
}

.commentlikebutton {
  text-align: center;
  align-content: center;
  justify-content: center;
}

.commentbutton {
  text-align: center;
  align-content: center;
  margin: 10px 10px auto;
}

.reviewlikebutton {
  text-align: center;
  align-content: center;
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
  border: solid 2px white;
  border-radius: 7px;
  letter-spacing: 1.5px;
  white-space: normal;
}

.likeheart:hover {
  transition: all 0.3s linear;
  transform: scale(1.5);
}

.unlikex:hover {
  transition: all 0.3s linear;
  transform: scale(1.5);
}

.inputupdatebox {
  margin-bottom: 20px;
}

#reviewupdate_title {
  margin-left: 30px;
  width: 70%;
  height: 40px;
  border: none;
  border-bottom: dashed 2px orange;
  background-color: black;
  color: white;
  font-size: 15px;
  letter-spacing: 3px;
}

#reviewupdate_content {
  margin-top: 10px;
  margin-left: 30px;
  margin-right: 40px;
  width: 70%;
  height: 40px;
  border: none;
  border-bottom: dashed 2px orange;
  background-color: black;
  color: white;
  font-size: 18px;
  letter-spacing: 3px;
}

.updatecompletebutton {
  text-align: center;
  align-content: center;
  border-radius: 7px;
  width: 35%;
  height: 70px;
  font-size: 30px;
}

.updatecompletebutton:hover {
  background-color: #05e31e;
  transition: all 0.2s linear;
  transform: scale(1.2);
}

#comment_content {
  margin-top: 10px;
  margin-left: 30px;
  margin-right: 40px;
  width: 65%;
  height: 40px;
  border: none;
  border-bottom: dashed 2px orange;
  background-color: black;
  color: white;
  font-size: 18px;
  letter-spacing: 3px;
}

.inputcommentbox {
  justify-content: center;
}

.commentcomfirmbutton:hover {
  background-color: #05e31e;
  transition: all 0.2s linear;
  transform: scale(1.2);
}

.commentupdatebox {
  height: 180px;
  padding: 10px 30px;
  align-content: center;
  text-align: center;
}

#commentupdate_content {
  margin-top: 10px;
  margin-left: 30px;
  margin-right: 40px;
  width: 70%;
  height: 40px;
  border: none;
  border-bottom: dashed 2px orange;
  background-color: black;
  color: white;
  font-size: 18px;
  letter-spacing: 3px;
}

.commentupdate_button {
  text-align: center;
  align-content: center;
  border-radius: 7px;
  width: 35%;
  height: 70px;
  font-size: 30px;
}

.commentupdate_button:hover {
  background-color: #05e31e;
  transition: all 0.2s linear;
  transform: scale(1.2);
}
</style>