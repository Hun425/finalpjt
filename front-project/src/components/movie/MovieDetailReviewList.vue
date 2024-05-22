<template>
  <div class="review-container">
    <div v-if="reviews && reviews.length">
      <h4>{{ mvtitle }}에 대한 {{ reviews.length }}개의 리뷰가 있어요!</h4>
      <!-- null 이 아니면 다 값이 있다고 판단!! / 이부분 처리 필요!! / 받아오는 데이터가 비어있으면 []로 받아와서 인식 X-->
        <MovieReviewItem v-for="(review,index) in reviews"  :review="review" :moviepk="moviepk" :index="index" @deleteReview = "deleteReview"/>
    </div>
    <div v-else>
      <p>아직 리뷰가 없습니다. 리뷰를 작성해주세요!</p>
    </div>
    <br>
    <!-- 리뷰작성 form -->
    <div>
      <h4>리뷰작성</h4>
      <br>
      <div>
        <form @submit.prevent = "createReview">
          <div>
            <label for="title">Title : </label>
            <input type="text" v-model.trim="title" id="title">
          </div>
          <div>
            <label for="content">Content : </label>
            <div>
              <textarea v-if="store.isLogin" class="create-area" v-model.trim="content" id="content"></textarea>
              <!-- 로그인시에만 사용 -->
              <textarea v-else @click="store.goToLogin" class="create-area" value="로그인 후 이용해주세요"></textarea>
            </div>
          </div>
          <div>
            <label for="rate">Rate:</label>
            <input type="number" v-model="rate" id="rate" min="0" max="10" required />
          </div>
          <input type="submit">
        </form>
      </div>
    </div>
  </div>
</template>
  
<script setup>
  import MovieReviewItem from '@/components/movie/MovieReviewItem.vue'
  import {ref} from 'vue'
  import { useAccountStore } from '@/stores/account';
  import {useRouter} from 'vue-router'
  import axios from 'axios'
  import Swal from 'sweetalert2';

  const props = defineProps({
    moviepk:Number,
    mvtitle:String,
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
      method:'get',
      url:`/movies/${props.moviepk}/reviews/`,
    })
    .then(res => {
      console.log(res.data)
      reviews.value = res.data
      console.log('리뷰데이터',reviews.value)
      return 0
    })
    .catch(err => console.log(err))
  }
  getReviews() 

  // 리뷰 생성 (확인완료)
  const createReview = function () {
    if (title.value === '' | content.value === '') {
      Swal.fire({
        icon: 'error',
        title: 'ERROR',
        text: '제목과 내용에는 1자 이상 작성되어야합니다.',
        confirmButtonText: '확인'
      });
      return 0;
    }

    axios({
      method:'post',
      url:`/movies/${props.moviepk}/reviews/`,
      data: {
        title:title.value,
        content:content.value,
        rate:rate.value
      },
      headers: {
        Authorization: `Token ${store.token}`
      },
    })
    .then(res => {
      // console.log(res.data)
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
  // moviepk는 삭제요청시 url에 필요!!
  const deleteReview = function (reviewpk) {
    axios({
      method:'delete',
      url:`/movies/${props.moviepk}/reviews/${reviewpk}/`,
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

    textarea {
      width: 400px;
      height:300px;
      resize: none;  /* 크기 제한하기 */
    }

    .review {
      margin: 20px;
    }

  </style>