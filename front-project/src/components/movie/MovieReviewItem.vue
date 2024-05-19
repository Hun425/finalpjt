<template>
  <div>
    <div id="reviewList"  class="review">
      <!-- 수정버튼 누르기 전 -->
      <div v-if="!isUpdate">
        <h4 >{{ review.title }}</h4>
        <hr>
        <p>{{ review.content }}</p>
        <p>{{ review.like_user_count }}</p>
          <button v-if="store.userData.username == review.user.username" @click="deleteReview(moviepk,review.id)">삭제</button>
          <button v-if="store.userData.username == review.user.username" @click="useUpdate">수정</button>
      </div>
      <!-- 수정버튼 누른 후 -->
      <div v-else>
        <form @submit.prevent = "updateReview(moviepk,review.id,index)">
          <div>
            <label for="title">Title : </label>
            <input type="text" v-model.trim="title" id="title">
          </div>
          <div>
            <label for="content">Content : </label>
            <div>
              <textarea class="update-area" v-model.trim="content" id="content"></textarea>
            </div>
          </div>
          <div>
            <label for="rate">Rate:</label>
            <input type="number" v-model="rate" id="rate" min="0" max="10" required />
          </div>
          <input type="submit">
        </form>
      </div>
      <!-- 여기에 댓글 작성하기!! -->
      <MovieReviewCommentList :comments="review.comments" :review="review" :moviepk="moviepk" />
      <hr>
      <div style="padding-left: 50px;">
      </div>
    </div>
  </div>


</template>

<script setup>
  import MovieReviewCommentList from '@/components/movie/MovieReviewCommentList.vue'
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/account';
  import axios from 'axios'
  import Swal from 'sweetalert2';

  const review = ref(null)
  const props = defineProps({
    review:Object,
    moviepk:Number,
    index:Number,
  })
  review.value = props.review
  
  const store = useAccountStore()

  // 리뷰 삭제
  const deleteReview = function (moviepk, reviewpk) {
    axios({
      method:'delete',
      url:`/movies/${moviepk}/articles/${reviewpk}/`,
      headers: {
        Authorization: `Token ${store.token}`
      },
    })
    .then(res => {
      reviews.value = reviews.value.filter(review => review.id !== reviewpk)
    })
    .catch(err => console.log(err))
  }

  const isUpdate = ref(false)
  const title = ref(null)
  const content = ref(null)
  const rate = ref(null)
  // 리뷰 수정
  const useUpdate = function () {
    isUpdate.value = true
    title.value = props.review.title
    content.value = props.review.content
    rate.value = props.review.rate
  }

  const updateReview = function (moviepk, reviewpk,index) {
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
      method:'put',
      url:`/movies/${props.moviepk}/articles/${reviewpk}/`,
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
      isUpdate.value = false
      console.log(review.value,123)
      review.value.title = title.value
      review.value.content = content.value
      review.value.rate = rate.value
    })
    .catch(err => {
      console.log(err)
      Swal.fire({
        icon: 'error',
        title: 'ERROR',
        text: '오류가 발생했습니다.',
        confirmButtonText: '확인'
      });
      return 0;
    })
  }
</script>

<style scoped>
  .review {
  margin: 20px;
  border: 1px solid rgb(193, 193, 193);
  border-radius: 10px;
  box-shadow: 1px;
  }

  .update-area {
      width: 400px;
      height:300px;
      resize: none;  /* 크기 제한하기 */
    }

</style>