<template>
  <div class="profile-container">
    <div v-if="userInfo.username === store.userData.username" class="welcome-text">
      <p>저희와 함께한지 <span class="highlight">{{ daysSinceJoined }}</span>일이 되었어요!</p>
    </div>
    <div class="profile">
      <div class="profile-image">
        <img :src="profilePic" alt="프로필 이미지">
        <button v-if="userInfo.username === store.userData.username" @click="changeProfilePic">프로필 변경</button>
      </div>
      <div class="user-info">
        <p>Name: {{ userInfo.username }}</p>
        <p>Email: {{ userInfo.email }}</p>
        <p>Age: {{ userInfo.age }}</p>
        <p>Created: {{ formattedDate }}</p>
      </div>
    </div>
    <div class="user-pick">
      <p><span>{{ userInfo.like_movies.length }} </span>개의 관심있는 영화가 있습니다.</p>
      <MovieCarousel :movies="userInfo.like_movies" />
    </div>
    <div class="user-pick">
      <p><span>{{ userInfo.reviews.length }} </span>개의 작성한 리뷰가 있습니다.</p>
      <ReviewCarousel :reviews="userInfo.reviews" />
    </div>
    <div class="user-pick">
      <p><span>{{ userInfo.liked_reviews.length }} </span>개의 관심있는 리뷰가 있습니다.</p>
      <LikeReviewList :likeReviews="userInfo.liked_reviews" />
    </div>
  </div>
</template>



  <!-- <ProfileImage :userpk="userInfo.id" :userPic="userInfo.profile_pic"/>  -->
  <!-- <img :src="`http://localhost:8000${userPic}`" alt=""> -->

  <script setup>
    import axios from 'axios'
    import { ref, computed, onMounted } from 'vue'
    import { useRouter, useRoute } from 'vue-router'
    import { useAccountStore } from '@/stores/account';
    import MovieCarousel from '@/components/Profile/MovieCarousel.vue';
    import ReviewCarousel from '@/components/Profile/ReviewCarousel.vue';
    import LikeReviewList from '@/components/Profile/LikeReviewList.vue';
    import defaultProfilePic from '@/assets/profile.jpg' // Default profile picture import
    import Swal from 'sweetalert2'
    
    const store = useAccountStore()
    const route = useRoute()
    const userpk = route.params.userpk
    const userInfo = ref({})
    
    const getUserProfile = async () => {
      try {
        const res = await axios.get(`/profile/${userpk}/`, {
          headers: {
            Authorization: `Token ${store.token}`
          }
        })
        userInfo.value = res.data
        console.log(userInfo.value)
      } catch (err) {
        console.error(err)
      }
    }
    getUserProfile()
    // onMounted(getUserProfile)
    
    const selectedFile = ref(null)
    
    const changeProfilePic = () => {
      const input = document.createElement('input')
      input.type = 'file'
      input.accept = 'image/*'
      input.onchange = (e) => {
        if (e.target.files.length === 0) {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: '이미지를 다시 업로드 해주세요!',
          })
        } else {
          selectedFile.value = e.target.files[0]
          uploadProfilePic()
        }
      }
      input.click()
    }
    
    const uploadProfilePic = async () => {
      const formData = new FormData()
      formData.append('profile_pic', selectedFile.value)
    
      try {
        const response = await axios.put(`/profile/${userpk}/update/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: `Token ${store.token}`,
          },
        })
        if (response && response.data) {
          userInfo.value.profile_pic = response.data.profile_pic
        } else {
          userInfo.value.profile_pic = URL.createObjectURL(selectedFile.value)
        }
      } catch (error) {
        console.error('Error uploading profile picture:', error)
      }
    }
    
    const daysSinceJoined = computed(() => {
      if (!userInfo.value.date_joined) return 0
      const joinDate = new Date(userInfo.value.date_joined)
      const currentDate = new Date()
      const timeDiff = currentDate - joinDate
      return Math.floor(timeDiff / (1000 * 60 * 60 * 24))
    })
    
    const formattedDate = computed(() => {
      if (!userInfo.value.date_joined) return ''
      const joinDate = new Date(userInfo.value.date_joined)
      const year = joinDate.getFullYear()
      const month = String(joinDate.getMonth() + 1).padStart(2, '0')
      const day = String(joinDate.getDate()).padStart(2, '0')
      return `${year}년 ${month}월 ${day}일`
    })
    
    const profilePic = computed(() => {
      return userInfo.value.profile_pic ? `http://localhost:8000${userInfo.value.profile_pic}` : defaultProfilePic
    })
  </script>
  

  

<style scoped>
.profile-container {
  width: 1440px;
  min-height: 1000px;
  margin: 40px auto;
  padding: 20px;
}

.profile-container p {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
}

.welcome-text {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
}

.welcome-text span {
  color: blueviolet;
}

.profile {
  margin: 20px auto;
  border: 1px solid rgb(181, 181, 181);
  border-radius: 20px;
  width: 800px;
  height: auto;
  display: grid;
  grid-template-columns: 200px 1fr;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.profile-image {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.profile img {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  border: 1px solid black;
}

.profile button {
  all: unset;
  border: 1px solid rgb(181, 181, 181);
  border-radius: 30px;
  background-color: white;
  font-size: 16px;
  padding: 4px 8px;
  margin-top: 10px;
  transition: 0.3s;
  cursor: pointer;
}

.profile button:hover {
  color: white;
  border: 1px solid rgb(255, 255, 255);
  background-color: blueviolet;
}

.user-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 20px;
}

.user-info p {
  font-weight: 400;
  margin: 5px 0;
}

.user-pick {
  margin: 100px 0;
}

.user-pick p {
  margin: 20px 0;
  text-align: center;
}

.user-pick span {
  color: blueviolet;
  padding-right: 2px;
}
</style>

  