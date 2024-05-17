import {defineStore} from 'pinia'
import {ref, computed} from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useAccountStore = defineStore('account', () => {
    const router = useRouter()

    // 발행될 토큰 저장할 token 선언
    const token = ref(null)

    // 로그인을 위한 함수 작성
    const logIn = function (payload) {
        const username = payload.username
        const password = payload.password
        axios({
            method: 'post',
            url: '/accounts/login/',
            data: {
                username, password
            }
        })
            .then(res => {
                console.log('로그인이 완료되었습니다.')
                console.log(res.data) // Token 발행 확인하기
                token.value = res.data.key // pinia에서 확인하자!!
                router.push({name:'movies'})
            })
            .catch(err => console.log(err))
    }


    const isLogin = computed(() => {
        if (token.value === null) {
            return false
        } else {
            return true
        }
    })
    return { logIn, token, isLogin }
}, {persist:true})