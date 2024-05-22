<template>
  <div>
    <Navbar />
    <RouterView />
    <Chatbot v-if="isChatbotOpen" @close="isChatbotOpen = false" /> <!-- 챗봇 컴포넌트 -->
    <button @click="toggleChatbot" class="open-chatbot-button">Open Chatbot</button> <!-- 챗봇 열기 버튼 -->
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Navbar from '@/components/common/Navbar.vue'
import Chatbot from '@/components/common/ChatBotModal.vue'

const isChatbotOpen = ref(false)

const toggleChatbot = () => {
  isChatbotOpen.value = !isChatbotOpen.value
}
</script>

<style scoped>
.open-chatbot-button {
  position: fixed;
  bottom: 20px;
  right: 20px; /* 오른쪽 하단에 위치 */
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  z-index: 1000;
}
</style>
