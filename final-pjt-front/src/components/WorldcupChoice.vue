<template>
  <div v-if="!!movie">
    <h2>{{movie.title}}</h2>
    <div
      v-on:mouseenter="hover = true"
      v-on:mouseleave="hover = false"
      v-bind:class="{ 'elevation-12': hover, 'elevation-2': !hover }"
      @click="select"
    >
      <img
        :src="movie.poster_path_500"
        alt=""
        width="400px"
        height="600px"
      >
    </div>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  data() {
    return {
      movieObject: null,
      hover: false,
    };
  },

  props: {
    movie: {
      type: Object,
      required: false,
    },
  },

  methods: {
    select() {
      this.$emit('choiceEvent', true);
    },
  },
};
</script>

<style scoped>



</style>