template>
  <div id="reviewbox">
    <div @click="gotoProfile()">
      <p>content : {{review.content}}</p>
      <p>작성자 : {{username}}</p>
    </div>
    <div>
      <button @click="likeReview">리뷰 좋아요 / 취소</button>
      <p>좋아요 : {{like_reviews}}</p>
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
      username: null,
      like_reviews: null,
    }
  },
  created() {
    this.getUsername()
  },
  mounted() {
    this.like_reviews = this.review.like_users.length
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem("jwt")
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
        headers: this.setToken()
      })
      .then((res) => {
        this.username = res.data.username
      })
      .catch((err) => console.log(err))
    },

    gotoProfile() {
      const username = this.username
      this.$router.push({name: 'Profile', query : {user: username}})
    },

    likeReview() {
      const movieid = this.review.movie.id
      const reviewid = this.review.id

      axios({
        method: 'post',
        url: `${URL}/movies/${movieid}/reviews/${reviewid}/like/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.like_reviews = res.data.like_users.length
      })
      .catch((err) => console.log(err))
    },
  }
}
</script>

<style>
#reviewbox {
  border: solid 1px black;
}
</style>