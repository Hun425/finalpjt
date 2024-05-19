import {defineStore} from 'pinia'
import {ref, computed} from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2';
export const useAccountStore = defineStore('account', () => {
    const router = useRouter()

    // 발행될 토큰 저장할 token 선언
    const token = ref(null)
    // 유저 데이터 활용위해서 store에 저장하기
    const userData = ref({
        pk: null,
        username: "",
      });

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
                userData.value = {
                    pk:res.data.pk,
                    username:username,
                }
                router.push({name:'home'})
            })
            .catch(err => {
                console.log(err)
                Swal.fire({
                    icon: 'error',
                    title: 'ERROR',
                    text: '닉네임과 비밀번호를 확인해주세요.',
                    confirmButtonText: '확인'
                  });

            })}

    const isLogin = computed(() => {
        if (token.value === null) {
            return false
        } else {
            return true
        }
    })

    const logOut = function () {
        token.value = null
        userData.value = {
            pk:null,
            username:''
        }
        router.push({name:'home'})
    }


    const goToLogin = function () {
        router.push({name:'login'})
      }

    return { userData, logIn, token, isLogin, logOut, goToLogin}
}, {persist:true})