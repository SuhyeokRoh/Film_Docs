<template>
  <div id="review">
    <ReviewItemView 
    v-for="review in reviews" :key="review.id"
    :review="review" />
  </div>
</template>

<script>
import ReviewItemView from './ReviewItemView.vue'

export default {
  name: 'ReviewListView',
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