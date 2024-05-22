<template>
  <div class="profile-container">
    <div v-if="userInfo.username == store.userData.username" class="welcome-text">
      <p>저희와 함께한지 <span class="highlight">{{ daysSinceJoined }}</span>일이 되었어요!</p>
    </div>
    <div class="profile">
      <div class="profile-image">
        <!-- <img :src="profilePic" alt="프로필 이미지"> -->
        <img src="@/assets/profile.jpg" alt="프로필 이미지">
        <button @click="changeProfilePic">프로필 변경</button>
      </div>
      <div class="user-info">
        <p>Name: {{ userInfo.username }}</p>
        <p>Email: {{ userInfo.email }}</p>
        <p>Age: {{ userInfo.age }}</p>
        <p>Created: {{ formattedDate }}</p>
      </div>
    </div>
    <div class="user-pick">
      <p>관심있는 영화</p>
      <MovieCarousel :movies="userInfo.like_movies"/>
    </div>
    <div class="user-pick">
      <p>작성한 리뷰</p>
      <ReviewCarousel :reviews="userInfo.reviews"/>
    </div>
  </div>
</template>

  <!-- <ProfileImage :userpk="userInfo.id" :userPic="userInfo.profile_pic"/>  -->
  <!-- <img :src="`http://localhost:8000${userPic}`" alt=""> -->

<script setup>
  import axios from 'axios'
  import { ref, computed, toRefs } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import { useAccountStore } from '@/stores/account';
  import MovieCarousel from '@/components/Profile/MovieCarousel.vue';
  import ReviewCarousel from '@/components/Profile/ReviewCarousel.vue';
  
  const store = useAccountStore()
  store.isDark = false
  const movies = ref([])
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
      movies.value = res.data.like_movies
      console.log('profilelink',res.data.profile_pic)
      console.log(userInfo)
    })
    .catch(err => {
      console.log(err)
    })
  }
  getUserProfile()
  
  const userProfilePic = ref(userInfo.profile_pic)
  const selectedFile = ref(null)
  
  const changeProfilePic = () => {
    const input = document.createElement('input')
    input.type = 'file'
    input.accept = 'image/*'
    input.onchange = (e) => {
      selectedFile.value = e.target.files[0]
      uploadProfilePic()
    }
    input.click()
  }
  
  const uploadProfilePic = async () => {
    const formData = new FormData()
    formData.append('profile_pic', selectedFile.value)
  
    try {
      const response = await profilePicEdit(props.userpk, formData)
      if (response && response.data) {
        userProfilePic.value = response.data.profile_pic
      } else {
        userProfilePic.value = URL.createObjectURL(selectedFile.value)
      }
    } catch (error) {
      console.error('Error uploading profile picture:', error)
    }
  }
  
  const profilePicEdit = (userpk, payload) => {
    console.log('token',store.token)
    return axios.put(`/profile/${userpk}/update/`, payload, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Token ${store.token}`,
      },
    })
    .then(res => {
    })
  }
  const daysSinceJoined = computed(() => {
  const joinDate = new Date(userInfo.value.date_joined)
  const currentDate = new Date()
  const timeDiff = currentDate - joinDate
  return Math.floor(timeDiff / (1000 * 60 * 60 * 24))
})

  const formattedDate = computed(() => {
    const joinDate = new Date(userInfo.value.date_joined)
    const year = joinDate.getFullYear()
    const month = String(joinDate.getMonth() + 1).padStart(2, '0')
    const day = String(joinDate.getDate()).padStart(2, '0')
    return `${year}년 ${month}월 ${day}일`
  })

  const profilePic = computed(() => {
    return `http://localhost:8000${userInfo.value.profile_pic}`
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
  color:blueviolet;
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
  /* justify-content:left;  가운데 정렬*/
  align-items: flex-start; /* 이건 좌측 정렬 */
  padding: 20px;
}

.user-info p {
  font-weight: 400;
  margin: 5px 0;
}


.user-pick{
  margin: 100px 0;
}


.user-pick p {
  margin: 20px 0;
  text-align: center;
}


</style>