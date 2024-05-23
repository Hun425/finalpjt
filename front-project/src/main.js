import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import 'bulma/css/bulma.min.css' 

import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faStar as fasStar, faStarHalfAlt } from '@fortawesome/free-solid-svg-icons'
import { faStar as farStar } from '@fortawesome/free-regular-svg-icons'

// 아이콘을 라이브러리에 추가
library.add(fasStar, farStar, faStarHalfAlt)
// Axios
import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000";

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

const app = createApp(App);

app.config.globalProperties.$axios = axios;

app.use(pinia);
app.use(router);

app.component('font-awesome-icon', FontAwesomeIcon);
app.mount("#app");

// npm install pinia
// npm install pinia-plugin-persistedstate
