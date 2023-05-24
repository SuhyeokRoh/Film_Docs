<template>
  <div class="inner">
    <label for="search" class="search-label">검색어를 입력하세요 : </label>
    <input type="text" id="search" v-model="searchContent" @keyup.enter="searchMovie" class="search-input">
    <button @click="searchMovie">검색</button>
    <div v-if="searchresults">
        <div v-if="issearchVaild" id="searchResbox">
            <div class="wrap" v-for="searchresult in searchresults" :key="searchresult.id"
                :searchresult="searchresult" @click="gotoDetail(searchresult)">
                <div><img class="posterlist" :src="searchresult.poster_path_original" ></div>
                <p>{{searchresult.title}}</p>
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
.posterlist {
  width: 400px;
}

#searchResbox {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.wrap {
  width: 400px;
  margin: 10px;
  text-align: center;
}

.wrap p {
  text-align: center;
  margin: 0 auto;
  display: inline-block;
}
.search-label {
  display: inline-block;
  width: 180px; /* 원하는 크기로 조정 */
  text-align: right;
}

.search-input {
  width: 300px; /* 원하는 크기로 조정 */
  padding: 5px;
}


@media (min-width: 768px) {
  .wrap {
    flex: 0 0 calc(33.33% - 20px);
  }
}
</style>