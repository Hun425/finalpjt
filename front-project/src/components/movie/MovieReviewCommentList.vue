<template>
  <div class="comment-box">
    <!-- 목록 보여주기 -->
    <div class="comment-content" v-for="comment in comments" :key="comment.id">
      <div class="profile-box">
        <img :src="`http://localhost:8000${comment.user.profile_pic}`" alt="Profile Picture">
      </div>
      <div class="comment">
        <p><strong>@{{ comment.user.username }}</strong></p>
        <p>{{ comment.content }}</p>
        <button class="delete-btn" v-if="comment.user.username === store.userData.username" @click="deleteComment(moviepk, reviewpk, comment.pk)">☒</button>
      </div>
    </div>
    <div class="comment-form">
      <form v-if="store.isLogin" @submit.prevent="createComment(moviepk, reviewpk)">
        <label for="content">댓글 : </label>
        <input type="text" v-model.trim="content" placeholder="댓글 추가...">
        <!-- 로그인시에만 작성 가능하도록 하기 -->
        <button class="submit-btn">➤</button>
      </form>
      <button v-else @click="store.goToLogin">로그인해주세요</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'
import axios from 'axios'

const props = defineProps({
  comments: Array,
  moviepk: Number,
  reviewpk: Number,
})
const emit = defineEmits(['updateComments'])
const comments = ref(props.comments)
const store = useAccountStore()

// 댓글 작성하기
const content = ref(null)
const createComment = function (moviepk, reviewpk) {
  if (content.value === '') {
    Swal.fire({
      icon: 'error',
      title: 'ERROR',
      text: '내용을 입력해주세요.',
      confirmButtonText: '확인'
    })
    return
  }
  axios({
    method: 'post',
    url: `/movies/${moviepk}/reviews/${reviewpk}/comments/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
    .then(res => {
      console.log('completed')
      comments.value = res.data // 성공시에는 comments 데이터 수정하기!!
      content.value = ''
      emit('updateComments', comments.value)
    })
    .catch(err => {
      console.log('error!!', err)
    })
}

// 댓글 삭제하기
const deleteComment = function (moviepk, reviewpk, commentpk) {
  axios({
    method: 'delete',
    url: `/movies/${moviepk}/reviews/${reviewpk}/comments/${commentpk}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
    .then(res => {
      comments.value = res.data
      emit('updateComments', comments.value)
      console.log(res.data)
    })
    .catch(err => {
      console.log(err)
    })
}
</script>
<style scoped>
  .profile-box {
  padding-top: 20px;;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content:flex-start;
  }
  .profile-box img {
    margin-top:0px;
    width: 50px;
    height: 50px;
    /* object-fit: cover; */
    border-radius: 50%;
  }
  .profile-box p {
    font-size: 13px;
  }
  .comment-box {
    padding-left:80px;
    border-top:1px solid rgb(192, 192, 192);
  }
  .comment-content {
    display: grid;
    grid-template-columns: 100px 600px;
    width:95%;
    min-height: 120px;
  }
  
  .comment {
    padding:10px;
    position: relative;
  }
  .comment p {
    padding-top:5px;
  }
  .delete-btn {
    all:unset;
    position:absolute;
    top:20px;
    right:30px;
    width:10px;
    height:10px;
    font-size: 20px;
  }
  .comment-form {
    margin-top:10px;
    height: 50px;
  }

  input {
    all:unset;
    width:600px;
    border-bottom:1px solid rgb(172, 172, 172);
    transition: border-bottom 0.3s;
  }
  input:focus {
    border-bottom: 2px solid rgb(90, 0, 173);
  }

  .submit-btn {
    all:unset;
    width:30px;
    text-align: center;
  }

</style>