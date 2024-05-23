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
            // console.log(res) // Token 발행 확인하기
            token.value = res.data.key // pinia에서 확인하자!!
            getuserData()
            Swal.fire({
                icon: 'success',
                title: '로그인 성공',
                text: '로그인이 성공적으로 완료되었습니다.',
                confirmButtonText: '확인'
            }).then((result) => {
                if (result.isConfirmed) {
                router.push({ name: 'home' });
                }
            router.push({name:'home'})
        })
        })
        .catch(err => {
            console.log(err)
            Swal.fire({
                icon: 'error',
                title: 'ERROR',
                text: '닉네임과 비밀번호를 확인해주세요.',
                confirmButtonText: '확인'
                })
        })}

    const getuserData = function () {
        axios({
            method:'get',
            url:'/accounts/user/',
            headers:{
                Authorization:`Token ${token.value}`
            }
        })
        .then(res => {
            userData.value = res.data
        })
        .catch(err => {
            console.log(err)
        })
    }  

    const isLogin = computed(() => {
        if (token.value === null) {
            return false
        } else {
            return true
        }
    })
    const logOut = function () {
        // 현재 페이지의 URL을 저장합니다.
        const currentPage = window.location.href;
    
        axios({
            method: 'post',
            url: '/accounts/logout/',
            headers: {
                Authorization: `Token ${token.value}`
            },
        })
        .then(res => {
            token.value = null;
            userData.value = {
                username: ''
            };
            localStorage.removeItem('chatbot-messages'); // 로그아웃 시 로컬 스토리지 초기화
            Swal.fire({
                icon: 'success',
                title: '로그아웃 성공',
                text: '로그아웃이 성공적으로 완료되었습니다.',
                confirmButtonText: '확인'
            }).then((result) => {
                if (result.isConfirmed) {
                    // 이전 페이지로 리다이렉션합니다.
                    window.location.href = currentPage;
                }
            });
        })
        .catch(err => {
            console.log(err);
            Swal.fire({
                icon: 'error',
                title: '오류 발생',
                text: '로그아웃 중 문제가 발생했습니다.',
                confirmButtonText: '확인'
            });
        });
    };
    


    const goToLogin = function () {
        router.push({name:'account'})
      }
    
    const isDark = ref(true)
    return { userData, logIn, token, isLogin, logOut, goToLogin, isDark}
}, {persist:true})