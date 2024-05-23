import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
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
    age: "",
  });

  // 로그인을 위한 함수 작성
  const logIn = async (payload) => {
    const username = payload.username
    const password = payload.password
    try {
      const res = await axios.post('/accounts/login/', { username, password })
      token.value = res.data.key // pinia에서 확인하자!!
      await getuserData()
      await getuserData2()
      Swal.fire({
        icon: 'success',
        title: '로그인 성공',
        text: '로그인이 성공적으로 완료되었습니다.',
        confirmButtonText: '확인',
        scrollbarPadding: false ,
      }).then((result) => {
        if (result.isConfirmed) {
          router.push({ name: 'home' });
        }
      });
    } catch (err) {
      console.log(err)
      Swal.fire({
        icon: 'error',
        title: 'ERROR',
        text: '닉네임과 비밀번호를 확인해주세요.',
        confirmButtonText: '확인',
        scrollbarPadding: false ,
      });
    }
  }

  const getuserData = async () => {
    try {
      const res = await axios.get('/accounts/user/', {
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      userData.value = res.data
    } catch (err) {
      console.log(err)
    }
  }

  const getuserData2 = async () => {
    try {
      const res = await axios.get(`/profile/${userData.value.pk}/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      userData.value.age = res.data.age
      console.log(userData.value.pk)
    } catch (err) {
      console.log(userData.value.pk)
      console.log(err)
    }
  }

  const isLogin = computed(() => {
    return token.value !== null;
  })

  const logOut = async () => {
    try {
      await axios.post('/accounts/logout/', {}, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      token.value = null;
      userData.value = {
        pk: null,
        username: '',
        age: '',
      };
      localStorage.removeItem('chatbot-messages'); // 로그아웃 시 로컬 스토리지 초기화
      Swal.fire({
        icon: 'success',
        title: '로그아웃 성공',
        text: '로그아웃이 성공적으로 완료되었습니다.',
        confirmButtonText: '확인',
        scrollbarPadding: false ,
        
      }).then((result) => {
        if (result.isConfirmed) {
          router.push({ name: "home" })
        }
      });
    } catch (err) {
      console.log(err);
      Swal.fire({
        icon: 'error',
        title: '오류 발생',
        text: '로그아웃 중 문제가 발생했습니다.',
        confirmButtonText: '확인',
        scrollbarPadding: false ,
      });
    }
  }

  const goToLogin = () => {
    router.push({ name: 'account' });
  }

  const isDark = ref(true)
  return { userData, logIn, token, isLogin, logOut, goToLogin, isDark }
}, { persist: true })
