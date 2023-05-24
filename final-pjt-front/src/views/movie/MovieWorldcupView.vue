<template>
  <v-container class="worldcup">
    <div v-if="!finishFlag">
      <h1>더 좋아하는 영화를 선택해 주세요</h1>
      <hr>
      <div v-if="!left">
        <v-btn @click="next">{{ roundNum }}강 시작하기</v-btn>
      </div>
      <v-row align="center" justify="center">
        <v-col cols="6" align="center">
          <worldcup-choice id="left" :movie="left" @choiceEvent="leftChoice" />
        </v-col>
        <v-col cols="6" align="center">
          <worldcup-choice id="right" :movie="right" @choiceEvent="rightChoice" />
        </v-col>
      </v-row>
    </div>

    <div v-if="finishFlag">
      <h1>우승!</h1>
      <hr>
      <v-row align="center" justify="center">
        <v-col cols="6">
          <worldcup-choice id="winner" :movie="left" />
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import axios from 'axios';
import WorldcupChoice from '@/components/WorldcupChoice.vue';

const URL = 'http://127.0.0.1:8000';

export default {
  data() {
    return {
      current_round: [],
      next_round: [],
      roundNum: 8,
      left: null,
      right: null,
      finishFlag: false,
    };
  },

  components: {
    WorldcupChoice,
  },

  methods: {
    setToken() {
      const token = this.$store.state.access_token;
      const config = {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      };
      return config;
    },
    randomMovieCall() {
      axios
        .get(`${URL}/movies/worldcup/`, this.setToken())
        .then((res) => {
          res.data.movies.forEach((code) => {
            axios
              .get(`${URL}/movies/worldcup/${code}`, this.setToken())
              .then((res) => {
                this.current_round.push(res.data);
              });
          });
        });
    },

    leftChoice() {
      this.next_round.push(this.left);
      this.left = null;
      this.right = null;
      this.next();
    },

    rightChoice() {
      this.next_round.push(this.right);
      this.left = null;
      this.right = null;
      this.next();
    },

    next() {
      this.left = this.current_round.pop();
      this.right = this.current_round.pop();
    },
  },

  watch: {
    // 라운드 종료 판별
    left() {
      if (this.current_round.length === 0 && !this.left) {
        this.current_round = this.next_round;
        this.next_round = [];
        this.roundNum = this.current_round.length;
      }
    },

    // 우승자 판별
    right() {
      if (
        this.next_round.length === 0 &&
        this.current_round.length === 1 &&
        !this.left &&
        !this.right
      ) {
        this.left = this.current_round.pop();
        this.finishFlag = true;
      }
      console.log(this.left);
    },
  },

  created() {
    this.randomMovieCall();
  },
};
</script>

<style>
</style>