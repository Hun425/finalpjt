<template>
  <div v-if="review">
    <div :class="['review', { commentOpen: isCommentOpen }]" :id="`review-${review.id}`">
      <div class='review-content'>
        <div class="profile-box">
          <img :src="`http://localhost:8000${review.user.profile_pic}`" alt="Profile Picture">
          <p class="username">@{{ review.user.username }}</p>
        </div>
        <div class="rate-box">
          <p>{{ review.rate }}</p>
        </div>
        <div class="reviewText">
          <div v-if="isUpdate">
            <div class="reviewCreateform">
              <form @submit.prevent="updateReview(moviepk, review.id)">
                <div>
                  <label for="title">Title</label><br>
                  <input type="text" v-model.trim="title" id="title" placeholder="제목을 입력해주세요.">
                </div>
                <div>
                  <label for="content">Content</label>
                  <div>
                    <textarea class="create-area" v-model.trim="content" id="content" placeholder="내용을 입력해주세요."></textarea>
                  </div> 
                </div>
                <div>
                  <label for="rate">Rate</label><br>
                  <input class="rate" type="number" v-model="rate" id="rate" min="0" max="10" required placeholder="점수를 입력해주세요." />
                  <button class="submit-btn" type="submit">➤</button>
                </div>
                <button @click="canceled">취소</button>
              </form>
            </div>
          </div>
          <div v-else>
            <p><strong>{{ review.title }}</strong></p>
            <p>{{ review.content }} {{ review.id }}</p>
          </div>
        </div>
        <div class="button-box">
          <p class="likeBtn" @click="handleLikeBtn">{{ likeBtnLabel }} {{ review.like_user_count }}</p>
          <p @click="handleComment"><img src="@/assets/comment.png" alt="comment" class="comment-img"> {{ commentLength }}</p>
        </div>
        <div v-if="review.user.username === store.userData.username && !isUpdate" class="menu-box">
          <button @click="toggleMenu">{{ showMenu ? '닫기' : '메뉴' }}</button>
          <div v-if="showMenu" class="menu">
            <button @click="useUpdate">수정하기</button>
            <button @click="handleDeleteReview(review.id)">삭제하기</button>
          </div>
        </div>
      </div>
      <MovieReviewCommentList v-show="isCommentOpen" :comments="review.comments" :reviewpk="review.id" :moviepk="moviepk" @updateComments="updateComments" />
    </div>
  </div>
</template>

<script setup>
import MovieReviewCommentList from '@/components/movie/MovieReviewCommentList.vue'
import { ref, computed, defineProps, defineEmits } from 'vue'
import { useAccountStore } from '@/stores/account';
import axios from 'axios'
import Swal from 'sweetalert2';
import router from '@/router';

const store = useAccountStore()
const props = defineProps({
  review: Object,
  moviepk: Number,
})
const emit = defineEmits(["deleteReview"])

const review = ref(props.review)
const isUpdate = ref(false)
const title = ref(null)
const content = ref(null)
const rate = ref(null)
const showMenu = ref(false)
const isOpen = ref(true)

const likeBtnLabel = computed(() => {
  if (!store.isLogin) {
    return '🤍'
  }
  const liked = review.value.like_users.some(user => user.pk === store.userData.pk)
  return liked ? '❤️' : '🤍'
})

const useUpdate = function () {
  isUpdate.value = true // 수정하기위한 form 열기
  isOpen.value = false
  title.value = props.review.title
  content.value = props.review.content
  rate.value = props.review.rate
}
const canceled = function () {
  isUpdate.value = false
  isOpen.value = true
  showMenu.value = false
}

const updateReview = function (moviepk, reviewpk) {
  if (title.value === '' || content.value === '') {
    Swal.fire({
      icon: 'error',
      title: 'ERROR',
      text: '제목과 내용에는 1자 이상 작성되어야합니다.',
      confirmButtonText: '확인'
    });
    return;
  }
  axios({
    method: 'put',
    url: `/movies/${props.moviepk}/reviews/${reviewpk}/`,
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
      isUpdate.value = false // 수정form 닫기
      isOpen.value = true
      showMenu.value = false
      review.value = res.data[0] // review 데이터 수정하기
    })
    .catch(err => {
      console.log(err)
      Swal.fire({
        icon: 'error',
        title: 'ERROR',
        text: '오류가 발생했습니다.',
        confirmButtonText: '확인'
      });
    })
}

const handleDeleteReview = function (reviewpk) {
  showMenu.value = false
  console.log(reviewpk)
  emit("deleteReview", reviewpk)
}

const handleLikeBtn = function () {
  if (!store.isLogin) {
    router.push({ name: 'account' })
    return;
  }

  axios({
    method: 'post',
    url: `/movies/${props.moviepk}/reviews/${review.value.id}/comments/like/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
    .then(res => {
      review.value = res.data
    })
    .catch(err => {
      console.log('error 발생', err)
    })
}

const isCommentOpen = ref(false)
const handleComment = function () {
  isCommentOpen.value = !isCommentOpen.value
}

const commentLength = computed(() => review.value.comments.length)

const updateComments = (newComments) => {
  review.value.comments = newComments
}

const toggleMenu = () => {
  showMenu.value = !showMenu.value
}
</script>

<style scoped>
  .review {
    margin: 20px;
    border: 1px solid rgb(193, 193, 193);
    border-radius: 30px;
    box-shadow: 1px;
  }
  .commentOpen {
    border-radius: 30px;
  }
  .review-content {
    display: grid;
    grid-template-columns: 100px 100px 600px;
    position: relative;
    width: 95%;
    min-height: 120px;
  }
  .reviewText {
    padding: 10px;
    padding-bottom: 30px;
    position: relative;
  }
  .reviewText p {
    padding-top: 5px;
  }
  .profile-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }
  .profile-box img {
    width: 50px;
    height: 50px;
    object-fit: cover;
    border-radius: 50%;
  }
  .profile-box p {
    font-weight: bold;
    font-size: 13px;
  }
  .rate-box {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-weight: bold;
    font-size: 36px;
    color: rgb(66, 5, 122);
  }
  .button-box {
    display: flex;
    gap: 5px;
    position: absolute;
    bottom: 10px;
    right: 0px;
    height: 30px;
    border-radius: 30px;
    padding: 10px;
  }


  .menu-box {
    position: absolute;
    top: 10px;
    right: 15px;
  }
  .menu {
    display: flex;
    flex-direction: column;
    gap: 5px;
    background-color: white;
    border: 1px solid gray;
    border-radius: 5px;
    padding: 5px;
  }
  .comment-img {
    height: 15px;
  }

  .reviewCreateform {
    margin: auto;
  }
  textarea {
    width: 90%;
    height: 100px;
    resize: none; /* 크기 제한하기 */
  }
  label {
    font-size: 14px;
    color: rgb(77, 77, 77);
  }
  input {
    all: unset;
    width: 90%;
    margin-bottom: 15px;
    border-bottom: 1px solid rgb(172, 172, 172);
    transition: border-bottom 0.3s;
  }
  input:focus {
    border-bottom: 2px solid rgb(90, 0, 173);
  }
  .rate {
    width: 90%;
  }
  .submit-btn {
    all: unset;
    width: 5%;
    text-align: center;
  }
</style>
