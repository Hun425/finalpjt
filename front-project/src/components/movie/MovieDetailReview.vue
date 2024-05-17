<template>
    <div>
      <p>리뷰목록</p>
        <div>
          <p>리뷰작성</p>
          <div v-if="store.isLogin">
            <form action="">
              <label for="title"></label>
              <input type="text" v-model.trim="title" id="title">
  
              <label for="content"></label>
              <input type="text" v-model.trim="content" id="content">
  
              <input type="submit">
            </form>
          </div>
          <div v-else>
            <p>로그인이 필요한 서비스입니다.</p>
          </div>
        </div>
    </div>
  </template>
  
  <script setup>
  
  </script>
  
  <style scoped>
  
  </style>