<template>
    <div>
      <h4>리뷰목록</h4>
      <br>
      <div v-if="reviews" id="reviewList">
        <div v-for="review in reviews" :key="review.id" :review="review"  class="review">
        <p>{{ review.title }}</p>
        <p>{{ review.content }}</p>
        <p>{{ review.like_user_count }}</p>
        <button v-if="store.userData.username == review.user.username" @click="deleteReview(moviepk,review.id)">삭제</button>
        <hr>
        </div>
      </div>
      <div v-else>
        <p>아직 리뷰가 없습니다. 리뷰를 작성해주세요!</p>
      </div>
      <br>
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
                  <textarea v-if="store.isLogin" class="textarea" v-model.trim="content" id="content"></textarea>
                  <textarea v-else @click="goToLogin" class="textarea" value="로그인 후 이용해주세요"></textarea>
                </div>
              </div>
              <div>
                <label for="rate">Rate:</label>
                <input type="number" v-model="rate" id="rate" min="1" max="5" required />
              </div>
              <input type="submit">
            </form>
          </div>
        </div>
    </div>
  </template>
  
  <script setup>
  import {ref} from 'vue'
  import { useAccountStore } from '@/stores/account';
  import {useRouter} from 'vue-router'
  import axios from 'axios'
  const props = defineProps({
    moviepk:Number,
  })
  
  const router = useRouter()
  const store = useAccountStore()
  

  const title = ref(null)
  const content = ref(null)
  const rate = ref(null)



  // 로그인시에만 리뷰작성 가능하도록!
  const goToLogin = function () {
    router.push({name:'login'})
  }


  // 리뷰목록확인하기
  const reviews = ref(null)
  const getReviews = function () {
    axios({
      method:'get',
      url:`/movies/${props.moviepk}/articles/`,
    })
    .then(res => {
      reviews.value = res.data
      console.log(reviews.value)

      return 0
    })
    .catch(err => console.log(err))
  }
  getReviews()
 
  // 리뷰 생성
  const createReview = function () {
    axios({
      method:'post',
      url:`/movies/${props.moviepk}/articles/`,
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
      console.log('completed')
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
  const deleteReviews = function () {
    axios({
      method:'get',
      url:`/movies/${props.moviepk}/articles/`,
    })
    .then(res => {
      reviews.value = res.data
      console.log(reviews.value)

      return 0
    })
    .catch(err => console.log(err))
  }

</script>
  
  <style scoped>
    .textarea {
      width: 400px;
      height:300px;
      resize: none;  /* 크기 제한하기 */
    }

    .review {
      margin: 20px;

    }
  </style>