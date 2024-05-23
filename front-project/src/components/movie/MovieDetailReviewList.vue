<template>
  <div class="review-container">
    <!-- 리뷰작성 form -->
    <div class="reviewCreateform">
      <h3>리뷰 작성하기</h3>
      <br>
      <div>
        <form @submit.prevent="createReview">
          <div class="form-group">
            <label for="title"></label>
            <input type="text" v-model.trim="title" id="title" placeholder="제목을 입력해주세요.">
          </div>
          <div class="form-group">
            <label for="content"></label>
            <div>
            </div>
            <textarea v-if="store.isLogin" class="create-area" v-model.trim="content" id="content" placeholder="내용을 입력해주세요."></textarea>
            <textarea v-else @click="store.goToLogin" class="create-area" placeholder="로그인 후 이용해주세요"></textarea>
          </div>
          <div class="form-group">
            <label></label>
            <div class="star-rating">
              <div class="rating-text">평점</div>
              <div class="stars">
                <font-awesome-icon
                  v-for="n in 5"
                  :key="n"
                  :icon="[ rate >= n * 2 ? 'fas' : rate >= (n * 2) - 1 ? 'fas' : 'far', rate >= n * 2 ? 'star' : rate >= (n * 2) - 1 ? 'star-half-alt' : 'star']"
                  @click="setRate(n * 2)"
                  @mouseover="hoverRate(n * 2)"
                  @mouseleave="hoverRate(rate)"
                />
              </div>
            </div>
            <button class="submit-btn" type="submit">➤</button>
          </div>
        </form>
      </div>
    </div>

    <div class="review-list" v-if="reviews && reviews.length">
      <h3>{{ mvtitle }}에 대한 {{ reviews.length }}개의 리뷰가 있어요!</h3>
      <MovieReviewItem v-for="review in reviews" :key="review.id" :review="review" :moviepk="moviepk"  @deleteReview="deleteReview" />
    </div>
    <div v-else class="no-review">
      <h2>아직 리뷰가 없습니다. 첫번째 리뷰를 작성해주세요!</h2>
    </div>
    <br>
  </div>
</template>

<script setup>
import MovieReviewItem from '@/components/movie/MovieReviewItem.vue'
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account';
import axios from 'axios'
import Swal from 'sweetalert2';

// Import FontAwesomeIcon and the icons you want to use
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faStar as fasStar, faStarHalfAlt } from '@fortawesome/free-solid-svg-icons';
import { faStar as farStar } from '@fortawesome/free-regular-svg-icons';

const props = defineProps({
  moviepk: Number,
  mvtitle: String,
})

const store = useAccountStore()

const title = ref('')
const content = ref('')
const rate = ref(0)


// 리뷰목록확인하기
const reviews = ref([])
const getReviews = function () {
  axios({
    method: 'get',
    url: `/movies/${props.moviepk}/reviews/`,
  })
    .then(res => {
      reviews.value = res.data
    })
    .catch(err => console.log(err))
}
getReviews()

// 리뷰 생성 (확인완료)
const createReview = function () {
  if (title.value === '' || content.value === '') {
    Swal.fire({
      icon: 'error',
      title: 'ERROR',
      text: '제목과 내용에는 1자 이상 작성되어야합니다.',
      confirmButtonText: '확인'
    });
    return 0;
  }

  axios({
    method: 'post',
    url: `/movies/${props.moviepk}/reviews/`,
    data: {
      title: title.value,
      content: content.value,
      rate: rate.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
    .then(res => {
      reviews.value.push(res.data)
      title.value = ''
      content.value = ''
      rate.value = 0
    })
    .catch(err => {
      console.log(err)
    })
}

// 리뷰 삭제
const deleteReview = function (reviewpk) {
  axios({
    method: 'delete',
    url: `/movies/${props.moviepk}/reviews/${reviewpk}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
    .then(res => {
      console.log(reviewpk)
      reviews.value = res.data
      console.log(reviews)
      console.log(res.data)
    })
    .catch(err => console.log(err))
}

// Set the rate
const setRate = (newRate) => {
  rate.value = newRate;
};

// Hover effect for rate
const hoverRate = (newRate) => {
  hoverRate.value = newRate;
};
</script>

<style scoped>
.review-container {
  width: 900px;
  margin: 30px auto;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.reviewCreateform {
  background: #fff;
  padding: 20px;
  margin-bottom: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.reviewCreateform h3 {
  margin-bottom: 10px;
  font-size: 24px;
  color: #333;
}

.form-group {
  margin-bottom: 15px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.form-group label {
  font-size: 14px;
  color: rgb(77, 77, 77);
  display: block;
  margin-bottom: 5px;
}

.form-group input,
.form-group textarea {
  width: calc(100% - 20px); /* 간격을 위한 여유 */
  padding: 8px;
  border: 1px solid rgb(172, 172, 172);
  border-radius: 5px;
  transition: border-color 0.3s;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: rgb(90, 0, 173);
  outline: none;
}

textarea {
  height: 100px;
  resize: none;
}

.star-rating {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  cursor: pointer;
}

.rating-text {
  font-size: 14px;
  margin-bottom: 5px;
}

.stars {
  display: flex;
  gap: 5px;
}

.submit-btn {
  padding: 10px 15px;
  background: rgb(90, 0, 173);
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-btn:hover {
  background: rgb(120, 0, 200);
}

.review-list {
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.review-list h3 {
  margin-bottom: 20px;
  font-size: 20px;
  color: #333;
}

.no-review {
  border-top: 1px solid rgb(97, 97, 97);
  padding: 40px;
  text-align: center;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
