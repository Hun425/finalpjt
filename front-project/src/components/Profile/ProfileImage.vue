<template>
    <div class="profile-pic-container mb-4 text-center">
    </div>
    <div>
        <img :src="`http://localhost:8000${userPic}`" alt="">
      <button @click="changeProfilePic">프로필 사진 변경</button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useAccountStore } from '@/stores/account';
  
  const store = useAccountStore()
  const props = defineProps({
    userpk: Number,
    userPic: String,
  })
  
  const userProfilePic = ref(props.userPic)
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
  }
  </script>
  
  <style scoped>
  .profile-pic-container img {
    max-width: 100%;
    height: auto;
    border-radius: 50%;
  }
  </style>
  