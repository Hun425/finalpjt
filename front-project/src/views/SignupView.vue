<!-- 회원가입 페이지! 사용정보 : username, password, passwordCheck -->

<template>
    <div>
        <h1>SignupView</h1>
        <form @submit.prevent="signup">
            <label for="username">username : </label>
            <input type="text" v-model.trim="username" id="username">
            <br>
            <label for="password1">password : </label>
            <input type="password" v-model.trim="password1" id="password">
            <br>
            <label for="password2">check your password : </label>
            <input type="password" v-model.trim="password2" id="password2">
            <br>
            <input type="submit" value="가입하기">
        </form>
    </div>
</template>

<script setup>
    import {useRouter} from 'vue-router'

    import {ref} from 'vue'
    
    // v-model 생성
    const username = ref(null)
    const password1 = ref(null)
    const password2 = ref(null)

    // store의 signup 함수 불러오기
    import {useAccountStore} from '@/stores/account'
    
    const accountStore = useAccountStore()

    // 올바르지않은 형식으로 반환될시에 어떻게 처리될지 생각해보자!
    const signup = function () {
        console.log(1234)
        const payload = {
            username: username.value,
            password1: password1.value,
            password2: password2.value
        }
        accountStore.signup(payload)
    }




</script>

<style scoped>

</style>