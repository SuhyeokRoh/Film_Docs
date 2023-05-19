<template>
  <div>
    <p>content : {{review.content}}</p>
    <p>작성자 : {{review.user}}</p>
  </div>
</template>

<script>
export default {
  name: "ReviewItemView",
  props: {
    review: Object,
  },
}
</script>

<style>

</style>