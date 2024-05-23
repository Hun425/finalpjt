<template>
  <div v-show="movie" class="background">
    <div class="contents">
      <img v-if="movie && movie.backdrop_path" class="backdrop" :src="'https://image.tmdb.org/t/p/w500/' + movie.backdrop_path" alt="backdrop">
      <img v-else class="backdrop" src="@/assets/backdrop.webp" alt="backdrop">
      <img v-if="movie && movie.poster_path" class="poster" :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" alt="poster">
      <p v-if="movie && movie.title" class="title">{{ movie.title }}</p>
      <p class="releaseDate">개봉일 : {{ movie.release_date }}</p>
      <p class="score">{{ roundedScore }}</p>
      <div class="pieChart">
        <div class="flex-wrapper">
          <div class="single-chart">
            <svg viewBox="-10 -10 50 50" class="circular-chart blue">
              <path class="circle-bg"
                d="M18 2.0845
                  a 15.9155 15.9155 0 0 1 0 31.831
                  a 15.9155 15.9155 0 0 1 0 -31.831"
              />
              <path class="circle"
                :stroke-dasharray="`${movie.vote_average*10}, 100`"
                d="M18 2.0845
                  a 15.9155 15.9155 0 0 1 0 31.831
                  a 15.9155 15.9155 0 0 1 0 -31.831"
              />
            </svg>
          </div>
        </div>
      </div>
      <div class="like-section">
        <p class="like_count">{{ movie.like_users.length }}명의 유저가 이 영화를 좋아합니다.</p>
        <button :class="['likeBtn', { 'is-like': isLike }]" @click="likeMovie">Like</button>
      </div>
    </div>
  </div>
</template>

<script setup>
  import axios from 'axios';
  import { ref, computed, watch } from 'vue';
  import { useAccountStore } from '@/stores/account';
  import Swal from 'sweetalert2';
  import { useRouter } from 'vue-router';

  const store = useAccountStore();
  const movie = ref({});
  const props = defineProps({
    movie: Object,
  });
  movie.value = props.movie;
  const isLike = computed(() => {
    return movie.value.like_users.some(user => user.username === store.userData.username);
  });

  const roundedScore = computed(()=>{
    return movie.value.vote_average.toFixed(1)
  })
  const router = useRouter();

  const likeMovie = function () {
    if (!store.isLogin) {
      Swal.fire({
        text: "로그인 후에 이용가능합니다.",
        showCancelButton: true,
        confirmButtonText: '로그인',
        cancelButtonText: '취소'
      }).then((result) => {
        if (result.isConfirmed) {
          router.push({ name: 'account' });
        }
      });
      return;
    }
    axios({
      method: 'post',
      url: `/movies/${movie.value.id}/likemovie/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then(res => {
      movie.value = res.data;
      console.log('Like updated!');
    })
    .catch(err => {
      console.log(err);
    });
  };




// const movie = ref(props.movie);

// Watch for changes in props.movie and update the local movie ref
watch(() => props.movie, (newMovie) => {
  movie.value = newMovie;
}, { immediate: true });


</script>

<style scoped>
  .background {
    height: 524px;
    background-color: black;
  }
  .contents {
    position: relative;
    width: 842px;
    margin: 0 auto;
    color: white;
  }
  .backdrop {
    height: 524px;
    width: 842px;
    filter: brightness(0.5) contrast(1); /* 밝기와 대비 조절 */
  }
  .title {
    position: absolute;
    top: 100px;
    right: 80px;
    font-size: 28px;
    font-weight: bold;
    color: white;
  }
  .releaseDate {
    position: absolute;
    top: 150px;
    right: 80px;
    font-size: 16px;
    font-weight: bold;
  }
  .poster {
    position: absolute;
    top: 120px;
    left: 60px;
    width: 200px;
    height: 312px;
    border-radius: 10px;
  }
  .like-section {
    position: absolute;
    display: flex;
    flex-direction: column;
    align-items: end;
    top: 175px;
    right: 80px;
    text-align: center;
  }
  .likeBtn {
    margin-top:10px;
    width: 120px;
    height: 40px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 10px;
    border: 1px solid rgba(255, 254, 254, 0.532);
    background-color: #ffffff00;
    color: rgb(255, 255, 255);
    transition: 0.5s;
  }
  .is-like {
    background-color: #ffffff;
    color: rgb(0, 0, 0);
  }
  .likeBtn:hover {
    background-color: blueviolet;
    color: white;
  }
  .like_count {
    margin-top: 10px;
    font-size: 16px;
    font-weight: bold;
  }
  .score {
    position: absolute;
    width: 50px;
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    top: 330px;
    right: 140px;
  }
  .pieChart {
    position: absolute;
    width: 180px;
    top: 260px;
    right: 80px;
  }
  .flex-wrapper {
    display: flex;
    flex-flow: row nowrap;
  }
  .single-chart {
    width: 100%;
  }
  .circle-bg {
    fill: none;
    stroke: #ffffff;
    stroke-width: 5.8;
  }
  .circle {
    fill: none;
    stroke-width: 4.8;
    stroke-linecap: round;
    stroke: white;
    animation: progress 1s ease-out forwards;
  }
  @keyframes progress {
    0% {
      stroke-dasharray: 0 100;
    }
  }
  .circular-chart.blue .circle {
    stroke: #07eea5;
    stroke-opacity: 0.6;
  }
  .percentage {
    fill: #ffffff;
    font-size: 15;
  }
</style>

