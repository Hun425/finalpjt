<template>
  <div v-show="movie" class="background">
    <div class="contents">
      <img v-if="movie && movie.backdrop_path" class="backdrop" :src="'https://image.tmdb.org/t/p/w500/' + movie.backdrop_path" alt="backdrop">
      <img v-else class="backdrop" src="@/assets/backdrop.webp" alt="backdrop">
      <img v-if="movie && movie.poster_path" class="poster" @click="goToDetail(movie.pk)" :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" alt="poster">
      <p v-if="movie && movie.title" class="title">{{ movie.title }}</p>
      <p class="releaseDate">개봉일 : {{ movie.release_date }}</p>
      <div class="star-rating">
        <font-awesome-icon v-for="n in fullStars" :key="'full-' + n" icon="star" />
        <font-awesome-icon v-if="hasHalfStar" icon="star-half-alt" />
        <font-awesome-icon v-for="n in emptyStars" :key="'empty-' + n" icon="star" class="empty-star" />
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

const fullStars = computed(() => Math.floor(movie.value.vote_average / 2));
const hasHalfStar = computed(() => (movie.value.vote_average / 2) % 1 !== 0);
const emptyStars = computed(() => 5 - fullStars.value - (hasHalfStar.value ? 1 : 0));

const goToDetail = (movie_pk) => {
  router.push({ name: 'movieDetail', params: { moviepk: movie_pk } })
}

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
  transition: transform 0.3s ease; /* 부드러운 애니메이션 효과 */
}

.poster:hover {
  transform: scale(1.5); /* 호버 시 확대 */
}

.star-rating {
  position: absolute;
  top: 190px;
  right: 80px;
  display: flex;
  align-items: center;
  font-size: 24px;
  color: gold;
}

.empty-star {
  color: #d3d3d3;
}

.like-section {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: end;
  top: 360px;
  right: 80px;
  text-align: center;
}

.likeBtn {
  margin-top: 10px;
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
</style>
