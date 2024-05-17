<template>
    <div>
        <h1>LoginView</h1>
        <form @submit.prevent = "logIn">
            <div>
                <label for="username">username:</label>
                <input type="text" v-model.trim="username" id="username" @blur="checkusername">
                <!-- <span v-if="usernameError">존재하지않는 이름입니다.</span> -->
            </div>
            <div>
                <label for="password">password:</label>
                <input type="password" v-model.trim="password" id="password">
            </div>

            <input type="submit" value = LOGIN>
        </form>
    </div>
    
</template>
<!-- export default 구문 사용시에는 setup 작성 X !!-->
<!-- vue3 composition code로 변환하기도 생각해보자 -->
<script setup>
import { ref } from 'vue'

const username = ref(null)
const password = ref(null)

import { useAccountStore } from '@/stores/account';

const store = useAccountStore()

const logIn = function () {
        const payload = {
            username: username.value,
            password: password.value
        }
        store.logIn(payload)
    }




// 수정전 코드!

// import router from "@/router"
// import axios from 'axios'
// import Swal from 'sweetalert2'

// export default {
//     data() {
//         return {
//             username = '',
//             password = '',
//             usernameError = false,
//         };
//     },
//     method:{
//         // checkusername : user DB에 해당 username 존재 여부 확인
//         checkusername() {
//             axios
//             .get("/validate_username/",{params: {username: this.username}})
//             .then((res) => {
//                 // 돌아오는 답이 있다면 에러표시 X
//                 if (res.data.is_taken) {
//                     this.usernameError = true
//                 } else {
//                     this.usernameError = false
//                 }
//             });
//         },
//         // 로그인 요청
//         loginForm() {
//             // 올바르게 작성했는지 
//             if (this.username. === '' || this.email === '') {
//                 Swal.fire({
//                     icon:'error',
//                     title:'누락된 필드',
//                     text: '유저네임과 비밀번호를 모두 입력해주세요.',
//                     confirmButtonText:'확인'
//                 });
//                 return; 
//             }
//             const formData = {
//                 username: this.username,
//                 password: this.password,
//             }

//             // 요청보내기
//             axios
//             .post('/accouts/user', formData)
//             .then((res) => {
//                 router.push({name:'movies'})
//             })
//             .catch((error) => {
//                 console.log(error)
//             })
//         }   
        
//     }
// }




</script>

<style scoped>

</style>