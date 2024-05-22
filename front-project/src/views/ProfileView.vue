<template>
    <div>
      <h2>Profile Page</h2>
      {{ userInfo.id }}
      <br>
      <div>
        <h3>작성한 리뷰</h3>
        <br>
        <div v-for="review in userInfo.reviews" :key="review.id" :review="review">
        <p>{{ review.title }}</p>
        <p>{{ review.content }}</p>
        <button @click="goToMovie(review.movie.pk)">리뷰보러 가기!!</button>
        <hr>
        <br>
        </div>
      </div>
      <hr>
    <div>
      <p>저장한 영화</p>
      <div v-for="movie in userInfo.like_movies" :key="movie.pk">
        <p>{{ movie.title }}</p>
        <p>{{ userInfo.like_movies.title }}</p>
      </div>
    </div>
    <p v-show="userInfo != {} && userInfo.like_movies == []"> 저장한 영화가 없습니다.</p>
  </div>
  <br>
    <h2>User 이미지 바꾸기</h2>
    <ProfileImage :userpk="userInfo.id" :userPic="userInfo.profile_pic"/> 
</template>

<script setup>
  import ProfileImage from '@/components/Profile/ProfileImage.vue'
  import axios from 'axios'
  import { ref, computed } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import { useAccountStore } from '@/stores/account';
  
  const store = useAccountStore()
  store.isDark = false

  const route = useRoute()
  const userpk = route.params.userpk
  const userInfo = ref({})

  // 유저 데이터 가져오기
  const getUserProfile = function () {
    axios({
      method:'get',
      url:`/profile/${userpk}/`,
      headers:{
        Authorization: `Token ${store.token}` // get이더라도 로그인이 필요하므로!!
      }
    })
    .then(res => {
      userInfo.value = res.data
      console.log('profilelink',res.data.profile_pic)
      console.log('completed')
    })
    .catch(err => {
      console.log(err)
    })
  }
  getUserProfile()

</script>

<style scoped>
  .profile-img {
    width:200px;
    height:200px;
  }

</style>