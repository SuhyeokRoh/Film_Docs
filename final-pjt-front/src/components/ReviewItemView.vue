<template>
  <div class="ableToClick" id="reviewbox" @click="gotoDetailReview">
    <div class="col paddingon">
      <h2 class="reviewtitlebox">{{review.title}}</h2>
      <div class="col textleft">
        <p>작성자 : {{nickname}}</p>
        <div class="row center textleft">
          <font-awesome-icon size="2xl" :icon="['fas', 'heart']" style="color: #ff0000;" />
          <p class="nomargin">  {{like_reviews}}</p>
        </div>
        <div class="row center textleft">
          <font-awesome-icon :icon="['fas', 'circle-xmark']" size="2xl" style="color: #001df5;" />
          <p class="nomarginx">  {{dislike_reviews}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const URL = "http://127.0.0.1:8000"
export default {
  name: "ReviewItemView",
  props: {
    review: Object,
  },
  data() {
    return {
      query: null,
      nickname: null,
      username: null,
      like_reviews: null,
      dislike_reviews: null,
    }
  },
  created() {
    this.getUsername()
  },
  mounted() {
    this.like_reviews = this.review.like_users.length
    this.dislike_reviews = this.review.dislike_users.length
  },
  methods: {
    setToken: function() {
      const token = this.$store.state.access_token
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },

    getUsername() {
      const userid = this.review.user
      axios({
        method: 'get',
        url: `${URL}/accounts/${userid}/`,
      })
      .then((res) => {
        this.nickname = res.data.nickname
        this.username = res.data.username
      })
      .catch((err) => console.log(err))
    },

    gotoDetailReview() {
      const key = this.$store.state.access_token
      if(key) {
        const reviews = this.review
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
  }
}
</script>

<style>
#reviewbox {
  border: solid 1px white;
  border-radius: 7px;
  margin: 10px auto;
  padding: 10px auto;
}

.paddingon {
  padding: 10px 10px;
}

.reviewtitlebox {
  text-align: center;
  margin-bottom: 5px;
  font-size: 30px;
}

.center {
  align-content: center;
  color: white;
}

.nomargin {
  margin: 6px 0px 0px 10px;
}

.nomarginx {
  margin: 7px 0px 0px 10px;
}

.textleft {
  justify-content: right;
  text-align: right;
  padding-right: 10px;
}
</style>