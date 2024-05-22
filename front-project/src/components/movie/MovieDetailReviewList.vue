<template>
  <div class="review-container">
    <!-- 리뷰작성 form -->
    <div class="reviewCreateform">
      <h3>리뷰 작성하기</h3>
      <br>
      <div>
        <form @submit.prevent = "createReview">
          <div>
            <label for="title">Title</label><br>
            <input type="text" v-model.trim="title" id="title" placeholder="제목을 입력해주세요.">
          </div>
          <div>
            <label for="content">Content</label>
            <div>
              <textarea v-if="store.isLogin" class="create-area" v-model.trim="content" id="content" placeholder="내용을 입력해주세요."></textarea>
              <!-- 로그인시에만 사용 -->
              <textarea v-else @click="store.goToLogin" class="create-area" value="로그인 후 이용해주세요"></textarea>
            </div>
          </div>
          <div >
            <label for="rate">Rate</label><br>
            <input class="rate" type="number" v-model="rate" id="rate" min="0" max="10" required placeholder="점수를 입력해주세요."/>
            <button class="submit-btn" type="submit">➤</button>
          </div>
        </form>
      </div>
    </div>
    <div v-if="reviews && reviews.length">
      <h3>{{ mvtitle }}에 대한 {{ reviews.length }}개의 리뷰가 있어요!</h3>
      <!-- null 이 아니면 다 값이 있다고 판단!! / 이부분 처리 필요!! / 받아오는 데이터가 비어있으면 []로 받아와서 인식 X-->
        <MovieReviewItem v-for="(review,index) in reviews"  :review="review" :moviepk="moviepk" :index="index" @deleteReview = "deleteReview"/>
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
import { useRouter } from 'vue-router'
import axios from 'axios'
import Swal from 'sweetalert2';

const props = defineProps({
  moviepk: Number,
  mvtitle: String,
})

const router = useRouter()
const store = useAccountStore()

const title = ref(null)
const content = ref(null)
const rate = ref(null)

// 리뷰목록확인하기
const reviews = ref(null)
const getReviews = function () {
  axios({
    method: 'get',
    url: `/movies/${props.moviepk}/reviews/`,
  })
    .then(res => {
      console.log(res.data)
      reviews.value = res.data
      console.log('리뷰데이터', reviews.value)
      return 0
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
      rate.value = null
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
      reviews.value = reviews.value.filter(review => review.id !== reviewpk)
    })
    .catch(err => console.log(err))
}
</script>
  
<style scoped>
  .review-container {
    width: 900px;
    margin: 30px auto;
  }
  .reviewCreateform {
    margin:  auto;
  }
  textarea {
    width: 100%;
    height:100px;
    resize: none;  /* 크기 제한하기 */
  }

  .review {
    margin: 20px;
  }
  label {
    font-size: 14px;
    color: rgb(77, 77, 77);
  }
  input {
    all:unset;
    width: 100%;
    margin-bottom: 15px;
    border-bottom:1px solid rgb(172, 172, 172);
    transition: border-bottom 0.3s;
  }
  input:focus {
    border-bottom: 2px solid rgb(90, 0, 173);
  }
  .rate {
    width:95%
  }

  .submit-btn {
    all:unset;
    width:5%;
    text-align: center;
  }

  .no-review {
    border-top: 1px solid rgb(97, 97, 97);
    padding: 40px;
    text-align: center;
  }
</style>