<template>
  <div @click="gotoProfile">
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
  methods: {
    gotoProfile() {
      const user = this.review.user
      // const content = this.review.content

      this.$router.push({name: 'Profile', query : {data: JSON.stringify({user: user, })}})
    },
  },
}
</script>

<style>

</style>