<template>
  <div>
    <MovieDetailMain :movie="movie"/>
    <div class="movieDetailInfo" v-if="movie">
      <div class="movieNav" @click="category">
        <div :class="{navItem:true, focus: isFocus===1, rest:!(isFocus===1) }">주요내용</div>
        <div :class="{navItem:true, focus: isFocus===2, rest:!(isFocus===2) }">관람평</div>
        <div :class="{navItem:true, focus: isFocus===3, rest:!(isFocus===3)}">예고편</div>
      </div>
      <MovieDetailInfo v-show="isFocus===1" :actors="movie.actors" :overview="movie.overview" />
      <MovieDetailReviewList v-show="isFocus===2" :moviepk="movie.id" :mvtitle="movie.title"/>
      <MovieDetailTrailer v-show="isFocus===3" :title="movie.title" />
    </div>
  </div>
</template>

<script setup>
  // 1) Component 구성 및 Focus
  import MovieDetailMain from '@/components/movie/MovieDetailMain.vue'
  import MovieDetailInfo from '@/components/movie/MovieDetailInfo.vue'
  import MovieDetailReviewList from '@/components/movie/MovieDetailReviewList.vue'
  import MovieDetailTrailer from '@/components/movie/MovieDetailTrailer.vue'

  import {ref} from 'vue'
  import axios from 'axios'
  import { useRoute } from 'vue-router'
  import { useAccountStore } from '@/stores/account';
  const store = useAccountStore()
  const isFocus = ref(1)
  // 클릭시에 보이는 화면이 바뀌도록 설정하기
  const category = function (event) {
    const categories = {
    '주요내용': 1,
    '관람평': 2,
    '예고편': 3
    };
    isFocus.value = categories[event.target.innerText];
  }


  // 2)영화데이터 분배
  const movie = ref(null) // 초기에 null로 설정해놔야 변화할 때에 인식하고 수정해준다!!
  // 영화데이터 받기
  const route = useRoute()
  axios({
    method:'get',
    url:'/movies/'+`${route.params.moviepk}/`,
  })
  .then(res => {
    console.log(res.data)
    movie.value = res.data
    console.log(movie.value)
    return 0
  })
  .catch(err => console.log(err))
</script>

<style scoped> 
  .movieDetailInfo {
    width: 1100px;
    margin: 10px auto;
  }
  .movieNav {
    display: flex;
    height: 40px;
  }
  .navItem {
    height: 40px;
    padding: 12px 0 0 0;
    border-color: #3b006e;
    border-style: solid;
    font-weight: bold;
    text-align: center;
  }
  .focus {
    
    width:370px;
    border-width: 2px 2px 0px 2px;
  }
  .rest {
    width:365px;
    border-width: 0 0 2px 0;
  }


</style>

<style>


</style>