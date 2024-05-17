<template>
  <div>
    <div>
      <h3>메인페이지</h3>
    </div>
    <div class="movieNav" @click="category">
      <div :class="{pocus: isPocus===1, rest:!(isPocus===1) }">주요내용</div>|
      <div :class="{pocus: isPocus===2, rest:!(isPocus===2) }">관람평</div>|
      <div :class="{pocus: isPocus===3, rest:!(isPocus===3) }">예고편</div>|
    </div>
      <MovieDetailInfo v-if="isPocus===1"/>
      <MovieDetailReview v-if="isPocus===2"/>
      <MovieDetailTrailer v-if="isPocus===3"/>
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
  const category = function (event) {
    const categories = {
    '주요내용': 1,
    '관람평': 2,
    '예고편': 3
    };
    isPocus.value = categories[event.target.innerText];
  }

</script>

<style scoped> 
  .movieNav {
    display: flex;
    width: 1100px;
    margin: auto;
  }
  .pocus {
    width:400px;
    background-color: blue;
  }
  .rest {
    width:350px;
    background-color: blueviolet;
  }


</style>