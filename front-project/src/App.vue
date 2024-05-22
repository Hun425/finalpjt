<template>
  <div>
    <Navbar />
    <RouterView />
    <Chatbot v-if="isChatbotOpen" @close="isChatbotOpen = false" /> <!-- 챗봇 컴포넌트 -->
    <button @click="toggleChatbot" class="open-chatbot-button">GPT와 대화하기</button> <!-- 챗봇 열기 버튼 -->
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
  background-color: #BFC8EA;
  color: black;
  border: none;
  padding: 12px 24px;
  border-radius: 50px;
  cursor: pointer;
  font-size: 16px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s, transform 0.3s;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.open-chatbot-button:hover {
  background-color: #005cbf;
  transform: translateY(-2px);
}

.open-chatbot-button:active {
  background-color: #004085;
  transform: translateY(0);
}

.open-chatbot-button::before {
  content: '💬';
  margin-right: 8px;
  font-size: 20px;
}
</style>
