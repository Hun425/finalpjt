<template>
  <div>
    <div>
      <h3>메인페이지</h3>
    </div>
    <div>
      <span :class="{pocus:isPocus == 1, rest:!isPocus == 1}" >주요내용</span>|
      <span :class="{pocus:isPocus == 2, rest:!isPocus == 2}" >관람평</span>|
      <span :class="{pocus:isPocus == 3, rest:!isPocus == 3}" >예고편</span>|
    </div>
      <MovieDetailInfo />
      <MovieDetailReview />
      <MovieDetailTrailer />
  </div>
</template>

<script setup>
  import MovieDetailInfo from '@/components/movie/MovieDetailInfo.vue'
  import MovieDetailReview from '@/components/movie/MovieDetailReview.vue'
  import MovieDetailTrailer from '@/components/movie/MovieDetailTrailer.vue'

  import {ref} from 'vue'
  import { useAccountStore } from '@/stores/account';
  const store = useAccountStore()

  const isPocus = ref(1)
  // 클릭시에 보이는 화면이 바뀌도록 설정하기
  const Category = function (event) {
    console.log(event.target.innerText)
  }



</script>

<style scoped> 
  .mainInfo {
    width: 1100px;
    margin: 0px auto;
  }
</style>