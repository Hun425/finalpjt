<template>
    <div>
      <p>리뷰목록</p>
        <div>
          <p>리뷰작성</p>
          <div v-if="store.isLogin">
            <form action="">
              <div>
                <label for="title"></label>
                <input type="text" v-model.trim="title" id="title">
              </div>
              <div>
                <label for="content"></label>
                <input type="text" v-model.trim="content" id="content">
              </div>
                
              <input type="submit">
            </form>
          </div>
          <div v-else>
            <p>로그인이 필요한 서비스입니다.</p>
          </div>
        </div>
        <hr>
    </div>
  </template>
  
  <script setup>
  import {ref} from 'vue'
  import { useAccountStore } from '@/stores/account';
  const store = useAccountStore()

  const title = ref(null)
  const content = ref(null)
  </script>
  
  <style scoped>
  
  </style>