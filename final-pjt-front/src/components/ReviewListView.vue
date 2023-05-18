<template>
  <div id="review">
    <label for="CreateReview">리뷰 작성 : </label>
    <input type="text" id="CreateReview" v-model="CreateReview" @keyup.enter="this.CreateReview">
    <ReviewItemView 
    v-for="review in reviews" :key="review.id"
    :review="review" />
  </div>
</template>

<script>
import ReviewItemView from './ReviewItemView.vue'

export default {
  name: 'ReviewListView',
  data: function() {
    return {
      CreateReview : ''
    }
  },
  components: {
    ReviewItemView,
  },
  props: {
    reviews: Array,
  },
}
</script>

<style>

</style>