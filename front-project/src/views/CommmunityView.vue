<template>
  <div>
    <div class="intro">
      <p>총 <span>{{ reviews.length }}</span> 개의 리뷰가 있습니다.</p>
    </div>
    <div class="movie-post-list">
      <div class="grid-item" v-for="(review, index) in reviews" :key="index" @click="goToMovieDetail(review.movie)">
        <div class="wrap">
          <div class="img">
              <img :src="'https://image.tmdb.org/t/p/w500/' + review.backdrop_path" :alt="review.title">
          </div>
          <div class="cont">
            <h3 class="tit">{{ review.title }}</h3>
            <p class="txt">{{ truncatedContent(review.content) }}</p>
            <p class="time">{{ timeAgo(review.created_at) }}</p>
            <p class="meta">
              <span>👍 {{ review.like_user_count }}</span> <span>💬 {{ review.comments_count }}</span>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios'


const reviews = ref([])
const getReviews = function () {
  axios({
    method:'get',
    url:'/movies/reviews/',
  })
  .then(res => {
    reviews.value = res.data
    console.log(res.data)
    
  })
  .catch(err => {
    console.log(err)
  })
}
onMounted(() => {
  getReviews()
})

const router = useRouter();

const truncatedContent = (content) => {
  return content.length > 100 ? content.substring(0, 100) + '...' : content;
};

const goToMovieDetail = (movieId) => {
  router.push({ name: 'movieDetail', params: { moviepk: movieId } });
};

const timeAgo = (time) => {
  const currentTime = new Date();
  const reviewTime = new Date(time);
  const timeDiff = (currentTime - reviewTime) / 1000 / 60; // time difference in minutes

  if (timeDiff < 60) {
    return Math.floor(timeDiff) + '분 전';
  } else if (timeDiff < 1440) {
    return Math.floor(timeDiff / 60) + '시간 전';
  } else {
    return Math.floor(timeDiff / 1440) + '일 전';
  }
};
</script>

<style scoped>
.intro {
  margin: 50px;
  font-size: 24px;
  text-align: center;
  font-weight: bold;
}

.intro span {
  color: blueviolet;
}
.movie-post-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, 260px);
  gap: 20px; /* 각 카드 사이의 간격 설정 */
  justify-content: center;
  width: 1200px;
  margin: 0 auto;
  overflow: hidden;
  min-height: 500px;
}

.movie-post-list .grid-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  width: 260px;
  cursor: pointer;
}

.movie-post-list .wrap {
  overflow: hidden;
  display: block;
  border-radius: 10px;
  background-color: #fff;
  width: 100%; /* 260px 너비를 고정 */
}

.movie-post-list .img {
  overflow: hidden;
  width: 100%;
  height: auto;
  aspect-ratio: 16 / 9;
  text-align: center;
  font-size: 0;
  line-height: 0;
  border: 1px solid transparent;
  border-radius: 10px 10px 0 0;
  background-color: #f5f5f5;
}

.movie-post-list .img img {
  width: 100%;
  height: auto;
}

.movie-post-list .cont {
  position: relative;
  padding: 20px;
  border: 1px solid #ebebeb;
  border-top: 0;
  border-radius: 0 0 10px 10px;
}

.movie-post-list .tit {
  margin: 0;
  padding: 0 0 10px 0;
  font-size: 16px;
  line-height: 1.3;
  color: #444;
}

.movie-post-list .txt {
  margin: 0;
  padding: 0;
  font-size: 13px;
  line-height: 1.3;
  color: #444;
}

.movie-post-list .time {
  margin: 10px 0 0 0;
  font-size: 12px;
  color: #888;
}

.movie-post-list .meta {
  margin-top: 10px;
  margin-right:10px;
  font-size: 14px;
  color: #444;
  /* margin-top: 10px;
  font-size: 14px;
  color: #444;
  display: flex;
  justify-content: space-between; */
}



</style>



