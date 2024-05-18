<template>
    <div>
      <h4>리뷰목록</h4>
      <br>
      <div v-if="reviews">
        리뷰가 있어요!
      </div>
      <div v-else>
        <p>아직 리뷰가 없습니다. 리뷰를 작성해주세요!</p>
      </div>
      <br>
        <div>
          <h4>리뷰작성</h4>
          <br>
          <div>
            <form>
              <div>
                <label for="title">Title : </label>
                <input type="text" v-model.trim="title" id="title">
              </div>
              <div>
                <label for="content">Content : </label>
                <div v-if="store.isLogin">
                  <textarea class="textarea" v-model.trim="content" id="content"></textarea>
                </div>
                <div v-else>
                  <textarea @click="goToLogin" class="textarea" id="content" value="로그인 후 이용해주세요"></textarea>
                </div>
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
  const router = useRouter()
  const store = useAccountStore()

  const title = ref(null)
  const content = ref(null)

  const reviews = ref(null)


  // 로그인시에만 리뷰작성 가능하도록!
  const goToLogin = function () {
    router.push({name:'login'})
  }
  </script>
  
  <style scoped>
    .textarea {
      width: 400px;
      height:300px;
      resize: none;  /* 크기 제한하기 */
    }
  </style>