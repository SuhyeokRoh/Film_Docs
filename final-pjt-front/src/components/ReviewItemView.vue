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
  data() {
    return {
      query: null,
    }
  },
  methods: {
    gotoProfile() {
      const user = this.review.user
      // const content = this.review.content
      console.log(user)
      console.log(this.review)
      this.$router.push({name: 'Profile', query : {user: user,}})
      // this.$router.push({name: 'Profile', params: { user: user }})
    },
  },
}
</script>

<style>

</style>