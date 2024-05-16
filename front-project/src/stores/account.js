import {defineStore} from 'pinia'
import {ref} from 'vue'
import axios from 'axios'
const JANGO_URL = 'http://127.0.0.1:8000'

export const useAccountStore = defineStore('account', () => {
    const signup = function (payload) {
        const username = payload.username
        const password1 = payload.password1
        const password2 = payload.password2
        // const {username, password, passwordCheck} = payload
        console.log(username, password1, password2)
        axios({
            method: 'post',
            url: `${JANGO_URL}/accounts/signup/`,
            data: {
                username, password, password2
            }
        })
        .then(res => {
            console.log('회원가입이 완료되었습니다.')
        })
        .catch(err => console.log(err))
    }




    return {JANGO_URL, signup}
}, {persist:true})