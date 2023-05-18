<template>
  <div>
    <label for="reView">리뷰 작성 : </label>
    <input type="text" id="reView" v-model="Review" @keyup.enter="createReview">
    <ReviewItemView 
    v-for="review in reviews" :key="review.id"
    :review="review" />
  </div>
</template>

<script>
import ReviewItemView from './ReviewItemView.vue'
import axios from 'axios'
const URL = "http://127.0.0.1:8000"

export default {
  name: 'ReviewListView',
  data: function() {
    return {
      Review : '',
    }
  },
  components: {
    ReviewItemView,
  },
  props: {
    reviews: Array,
    movie: Object,
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem("jwt")
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },

    createReview: function() {
      // console.log(this.movie.id)
      // const movie = 
      // const token = this.setToken()
      const user = this.$store.state.username
      console.log(this.Review)

      axios({
        method: "post",
        url: `${URL}/movies/${this.movie.id}/reviews/`,
        data: { 'content' :this.Review, 'user': user},
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        // console.log(this.Review)
        // this.reviews.push(this.Review)
      }).catch((err) => {
        console.log(err)
      })
    },
  },
  created() {
  const token = localStorage.getItem("jwt");
  this.saveTokenToLocalStorage(token);
  this.setAuthHeader();
},
  
}
</script>

<style>

</style>