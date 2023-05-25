<template>
  <div class="search-inner">
    <p class="search-label">검색어를 입력하세요</p>
    <br>
    <input type="text" v-model="searchContent" @keyup.enter="searchMovie" class="search-input" placeholder="">
    <br>
    <br>
    <button id="searbtn" @click="searchMovie"><font-awesome-icon :icon="['fasr', 'magnifying-glass']" beat size="xl" style="color: #bcbec2;" /></button>
    <div v-if="searchresults">
        <div v-if="issearchVaild" id="searchResbox">
            <div class="search-wrap" v-for="searchresult in searchresults" :key="searchresult.id"
                :searchresult="searchresult" @click="gotoDetail(searchresult)">
              <div class="sea-OnePoster ableToClick">
              <div class="sea-card">
                <div class="sea-front"><img class="search-posterlist" :src="searchresult.poster_path_original" ></div>
                <div class="sea-back">{{searchresult.title}}</div>
              </div>
              </div>
            </div>
        </div>
        <div v-else>
            <p>찾으시는 검색 결과가 없습니다.</p>
        </div>
    </div>
  </div>
</template>

<script>

// import _ from 'lodash'
import axios from 'axios'
const URL = "http://127.0.0.1:8000"


export default {
  name: 'MovieSearchView',
  data: function() {
    return {
     searchContent: '',
     searchcontentlist: [],
     searchresults: [],
     issearchVaild: false,
    }
  },
  components: {
  
  },
  methods: {
    setToken: function() {
      const token = this.$store.state.access_token
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },
    
    searchMovie() {
    //   this.searchresults = []
      if ((this.searchContent).trim() === '' || this.searchContent === ''){
        alert('검색어를 입력해주세요')
        // this.searchresults = []
        return
      } else { 
        this.searchcontentlist.push(this.searchContent)
        this.issearchVaild = true
        //   console.log(this.searchcontentlist)
        axios({
            method: 'get',
            url: `${URL}/movies/search/`,
            headers: this.setToken(),
            params: {
            searchcontentlist: this.searchcontentlist.join(',')
            }
        })
        .then((res) => {
            console.log(res)
            this.searchresults = res.data
            // console.log(this.searchresults)
            this.searchcontentlist = []
            this.searchContent = ''
            // this.vote_rate_movies = res.data[0]
        })
        .catch((err) => {
            console.log(err)
            this.issearchVaild = false
            this.searchcontentlist = []
        })
     }
    },
    gotoDetail(searchresult) {
        const movie = searchresult
        this.$router.push({name: 'moviedetail', query : {data: JSON.stringify({movie: movie, })}})
    },
  },
  created() {
   
  },
  mounted() {
   
  },
}
</script>

<style>
#searchResbox {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
}

.search-wrap {
  width: 400px;
  margin: 10px;
  text-align: center;
}

.search-wrap {
  width: 400px;
  margin: 10px;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}
.search-label {
  display: inline-block;
  width: 250px; /* 원하는 크기로 조정 */
  /* text-align: right; */
  margin-top: 35px;
  font-size: 20px;
  font-weight: bold;
}

.search-input {
  border-radius: 5px;
  width: 600px; /* 원하는 크기로 조정 */
  height: 50px;
  padding: 5px;
}

#searbtn {
  border-radius: 5px;
  background:#1AAB8A;
  color:#fff;
  border:none;
  position:relative;
  height:60px;
  font-size:1.6em;
  padding:0 2em;
  cursor:pointer;
  transition:800ms ease all;
  outline:none;
}
#searbtn:hover{
  background:#fff;
  color:#1AAB8A;
}
#searbtn:before,#searbtn:after{
  content:'';
  position:absolute;
  top:0;
  right:0;
  height:2px;
  width:0;
  background: #1AAB8A;
  transition:400ms ease all;
}
#searbtn:after{
  right:inherit;
  top:inherit;
  left:0;
  bottom:0;
}
#searbtn:hover:before,#searbtn:hover:after{
  width:100%;
  transition:800ms ease all;
}

@media (min-width: 768px) {
  .wrap {
    flex: 0 0 calc(33.33% - 20px);
  }
}

.sea-OnePoster {
  margin: 10px;
  width: 600px;
  height: 500px;
  position: relative;
}

.search-posterlist {
  width: 100%;
  height: 100%;
}

.sea-card {
  height: 100%;
  width: 100%;
  position: relative;
  transition: 1s;
  transform-style: preserve-3d;
}

.sea-front,
.sea-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}

.sea-OnePoster:hover .sea-card {
  transform: rotateY(180deg);
}

.sea-back {
  background-color: white;
  color: black;
  border-radius: 7px;
  line-height: 350px;
  font-size: 20px;
  transform: rotateY(180deg);
}

</style>