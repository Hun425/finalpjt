<template>
  <div>
    <!-- 목록 보여주기 -->
    <div v-show="props.comments">
      <div v-for="comment in comments">
        <!-- <p>{{ comment }}</p> -->
        <hr>
        <!-- <p>{{ review }}</p> -->
        <button v-if="comment.user.username === store.userData.username" @click="deleteComment(moviepk,review.id,comment.pk)">delete</button>
      </div>
    </div>
    <!-- 없을때 보여주기 -->
    <div v-show="!props.comments">
      <p>댓글이 없습니다. 댓글을 남겨주세요!</p>
    </div>
    <div>
      <form v-if="store.isLogin" @submit.prevent="createComment(moviepk,review.id)" >
        <label for="comment">댓글:</label>
        <input  v-model.trim="comment" id="comment"></input>
        <!-- 로그인시에만 작성 가능하도록하기 -->
        <br>
        <input type="submit">
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
    review:Object,
  })
  comments.value = props.comments
  console.log(props.comments,'asdfa;')
  const store = useAccountStore()

  // 댓글 작성하기
  // /movies/<int:movie_pk>/article/<int:article_pk>/comments/
  const comment = ref(null)
  const createComment = function (moviepk, reviewpk) {
    if (comment.value === '') {
      Swal.fire({
        icon: 'error',
        title: 'ERROR',
        text: '닉네임과 비밀번호를 확인해주세요.',
        confirmButtonText: '확인'
      })
      return 0
    }
    axios({
      method:'post',
      url:`/movies/${moviepk}/article/${reviewpk}/comments/`,
      data:{
        comment:comment.value
      },
      headers: {
        Authorization: `Token ${store.token}`
      },
    })
    .then(res => {
      console.log('completed')
      review.value = res.data
        // 
      })
    .catch(err => {
      console.log(err)
      console.log('error!!')
    })
    }
  


  // 댓글 삭제하기
  const deleteComment = function () {
    axios({
      method:'delete',
      url:``,
      confirmButtonText
    })
  }
</script>
<style scoped>

</style>