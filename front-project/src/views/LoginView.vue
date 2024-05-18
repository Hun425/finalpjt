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


</script>

<style scoped>

</style>