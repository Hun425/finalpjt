import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// npm install pinia
// npm install pinia-plugin-persistedstate

import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'


// Axios
import axios from 'axios'

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

const app = createApp(App)

app.config.globalProperties.$axios = axios

app.use(pinia)
app.use(router)

app.mount('#app')