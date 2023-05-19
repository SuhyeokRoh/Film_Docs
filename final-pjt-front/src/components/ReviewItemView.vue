<template>
  <div>
    <p>확인</p>
    <p>{{review.content}}</p>
    <p>{{review.user_id}}</p>
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