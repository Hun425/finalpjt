<template>
  <div>
    <!-- 목록 보여주기 -->
    <div v-show="props.comments">
      <div v-for="comment in comments" style="padding-left: 20px; color:red">
        <p>{{ comment.content }}</p>
        {{ comment }}
        <button v-if="comment.user.username === store.userData.username" @click="deleteComment(moviepk,reviewpk,comment.pk)">delete</button>
      </div>
    </div>
    <!-- 없을때 보여주기 -->
    <div v-show="!props.comments">
      <p>댓글이 없습니다. 댓글을 남겨주세요!</p>
    </div>
    <div>
      <form v-if="store.isLogin" @submit.prevent="createComment(moviepk,reviewpk)" >
        <label for="content">댓글:</label>
        <input  v-model.trim="content" id="content">
        <!-- 로그인시에만 작성 가능하도록하기 -->
        <br>
        <input type="submit" value="작성하기">
      </form>
      <button v-else @click="store.goToLogin">로그인해주세요</button>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/account'
  import axios from 'axios'

  const comments = ref(null)
  const props = defineProps({
    comments:Array,
    moviepk:Number,
    reviewpk:Number,
  })
  comments.value = props.comments
  // console.log(props.comments,'asdfa;')
  const store = useAccountStore()

  // 댓글 작성하기
  // /movies/<int:movie_pk>/article/<int:article_pk>/comments/
  const content = ref(null)
  const createComment = function (moviepk, reviewpk) {
    if (content.value === '') {
      Swal.fire({
        icon: 'error',
        title: 'ERROR',
        text: '내용을 입력해주세요.',
        confirmButtonText: '확인'
      })
      return 0
    }
    axios({
      method:'post',
      url:`/movies/${moviepk}/reviews/${reviewpk}/comments/`,
      data:{
        content:content.value
      },
      headers: {
        Authorization: `Token ${store.token}`
      },
    }) 
    .then(res => {
      console.log('completed')
      comments.value = res.data // 성공시에는 comments데이터를 수정하기!!
      content.value = ''
      })
    .catch(err => {
      console.log('error!!')
    })
    }
  

  // 댓글 삭제하기
  const deleteComment = function (moviepk, reviewpk,commentpk) {
    axios({
      method:'delete',
      url:`/movies/${moviepk}/reviews/${reviewpk}/comments/${commentpk}/`,
      headers: {
        Authorization: `Token ${store.token}`
      },
    })
    .then(res => {
      comments.value = res.data

    })
    .catch(err => {
      console.log(err)
    })
  }
</script>
<style scoped>

</style>