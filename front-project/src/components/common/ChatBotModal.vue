<template>
  <div class="chatbot-modal">
    <div class="chatbot-header">
      <h3>Chatbot</h3>
      <button @click="closeChatbot">Clear</button>
    </div>
    <div class="chatbot-body">
      <div class="messages" ref="messagesContainer">
        <div v-for="(message, index) in messages" :key="index" :class="messageClass(message)">
          <p>{{ message.text }}</p>
        </div>
      </div>
      <div class="input-container">
        <textarea v-model="userMessage" @keydown="handleKeydown" placeholder="Type your message here..."></textarea>
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, nextTick } from 'vue'
import { userMessage, messages, errorMessage } from '@/stores/chatbotStore'
import { useUserStore } from '@/stores/userStore'
import { useAccountStore } from "@/stores/account"
const accountStore = useAccountStore()
const messagesContainer = ref(null)
const userStore = useUserStore()

const MAX_MESSAGES = 1000; // 최대 메시지 개수 설정

// 로컬 스토리지에서 메시지를 로드하는 함수
const loadMessagesFromLocalStorage = () => {
  const savedMessages = localStorage.getItem('chatbot-messages')
  if (savedMessages) {
    messages.value = JSON.parse(savedMessages)
  }
}

// 메시지를 로컬 스토리지에 저장하는 함수
const saveMessagesToLocalStorage = () => {
  // 최대 메시지 개수를 초과하면 오래된 메시지를 삭제
  if (messages.value.length > MAX_MESSAGES) {
    messages.value = messages.value.slice(messages.value.length - MAX_MESSAGES)
  }
  localStorage.setItem('chatbot-messages', JSON.stringify(messages.value))
}

const sendMessage = async () => {
  if (userMessage.value.trim()) {
    messages.value.push({ text: userMessage.value, sender: 'user' })
    await nextTick(scrollToBottom)
    saveMessagesToLocalStorage() // 메시지를 로컬 스토리지에 저장

    try {
      const response = await fetch('http://localhost:8000/gpt/chat/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${accountStore.token}`
        },
        body: JSON.stringify({ message: userMessage.value })
      })

      const text = await response.text()
      console.log(accountStore.token)
      if (!text) {
        throw new Error('Empty response from server')
      }
      const data = JSON.parse(text)
      if (response.ok) {
        messages.value.push({ text: data.response, sender: 'bot' })
      } else if (response.status === 401) {
        messages.value.push({ text: "로그인 해주세요", sender: 'bot' }) // 로그인 요청 메시지를 추가
      } else {
        errorMessage.value = data.error || 'An error occurred'
      }
      saveMessagesToLocalStorage() // 메시지를 로컬 스토리지에 저장
      await nextTick(scrollToBottom)
    } catch (error) {
      errorMessage.value = 'Failed to fetch: ' + error.message
    }

    userMessage.value = ''
  }
}
const handleLogout = async () => {
  await accountStore.logout()
  messages.value = [] // 메시지 기록 초기화
  window.location.reload()
}
const closeChatbot = () => {
  messages.value = []
  localStorage.removeItem('chatbot-messages') // 로그아웃 시 로컬 스토리지 초기화
}

const scrollToBottom = () => {
  const container = messagesContainer.value
  if (container) {
    container.scrollTop = container.scrollHeight
  }
}

watch(messages, () => {
  nextTick(scrollToBottom)
})

onMounted(() => {
  loadMessagesFromLocalStorage() // 컴포넌트가 마운트될 때 메시지를 로드
  userStore.checkAuthStatus()
})

const getCookie = (name) => {
  let cookieValue = null
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';')
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim()
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}

const messageClass = (message) => {
  return message.sender === 'user' ? 'message user' : 'message bot'
}

const handleKeydown = (event) => {
  if (event.key === 'Enter') {
    if (!event.shiftKey) {
      event.preventDefault()
      sendMessage()
    }
  }
}

// 로그인 상태가 변경될 때 로컬 스토리지를 초기화하는 함수
watch(() => userStore.isLoggedIn, (newVal) => {
  if (!newVal) {
    messages.value = []
    localStorage.removeItem('chatbot-messages') // 로그아웃 시 로컬 스토리지 초기화
  }
})
</script>

<style scoped>
.chatbot-modal {
  position: fixed;
  bottom: 80px;
  right: 20px; /* 오른쪽 하단에 위치 */
  width: 300px;
  height: 400px;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  z-index: 1000; /* 다른 요소보다 앞에 오도록 설정 */
}

.chatbot-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #4F6D7A;
  color: white;
  padding: 10px;
}

.chatbot-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.messages {
  flex: 1;
  overflow-y: auto; /* 스크롤 가능하도록 설정 */
  padding: 10px;
  word-wrap: break-word; /* 긴 메시지가 줄바꿈되도록 추가 */
}

.message {
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 5px;
  max-width: 70%;
}

.message.user {
  background-color: #4F6D7A;
  color: white;
  align-self: flex-end;
}

.message.bot {
  background-color: #E8DAB2;
  color: black;
  align-self: flex-start;
}

.input-container {
  display: flex;
  padding: 10px;
  background-color: white;
}

textarea {
  flex: 1;
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 5px;
  resize: none; /* 크기 조절 비활성화 */
  height: 60px; /* 고정된 높이 설정 */
  margin-right: 10px; /* 버튼과 간격 추가 */
}

button {
  background-color: #C0D6DF;
  color: black;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
}
</style>
