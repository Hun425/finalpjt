<template>
  <div class="body">
    <h2>Hello, My world!</h2>
    <br>
    <div class="container" id="container">
      <!-- 회원가입 form -->
      <div class="form-container sign-up-container">
        <form @submit.prevent="submitForm">
          <div>
            <label for="username"></label>
            <input type="text" v-model.trim="signupUsername" @blur="checkUsername"  placeholder="Username"/>
            <span v-if="usernameError" class="error">{{ usernameError }}</span>
          </div>
          <div>
            <label for="email"></label>
            <input type="email"  v-model.trim="signupEmail" @blur="checkEmail" placeholder="Email"/>
            <span v-if="emailError" class="error">{{ emailError }}</span>
          </div>
          <div>
            <label for="age"></label>
            <input type="number"  v-model="age" @blur="checkAge" placeholder="Age"/>
            <span v-if="ageError">{{ ageError }}</span>
          </div>
          <div>
            <label for="password1" ></label>
            <input type="password"  v-model.trim="password1" placeholder="password"/>
          </div>
          <div>
            <label for="password2"></label>
            <input type="password" v-model.trim="password2" placeholder="Confirm password"/>
          </div>
          <button type="submit">Sign Up</button>
        </form>
      </div>
      <!-- Sign In ( 로그인 페이지 ) -->
      <div class="form-container sign-in-container">
        <form @submit.prevent = "logIn">
          <h1>Sign in</h1>
          <br>
          <label for="username"></label>
          <input placeholder="Username" type="text" v-model.trim="username" id="username" @blur="checkusername" >
          <label for="password"></label>
          <input type="password" v-model.trim="password" id="password" placeholder="Password">
          <br>
          <button>Sign In</button>
        </form>
      </div>
      <div class="overlay-container">
      <div class="overlay">
        <div class="overlay-panel overlay-left">
          <h1>Welcome Back!</h1>
          <p>To keep connected with us please login with your personal info</p>
          <button class="ghost" id="signIn">Sign In</button>
        </div>
        <div class="overlay-panel overlay-right">
          <h1>Hello, Friend!</h1>
          <p>Enter your personal details and start journey with us</p>
          <button class="ghost" id="signUp">Sign Up</button>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script setup>
  import { ref } from 'vue'
  import router from "@/router";
  import axios from "axios";
  import Swal from 'sweetalert2';
  
  // 회원가입용
  const signupUsername =  ref("")
  const signupEmail =  ref("")
  const age = ref("")
  const password1 = ref("")
  const password2 = ref("")
  const usernameError = ref("")
  const emailError = ref("")
  const ageError = ref("")

  // 필요한 함수들
  const checkUsername = () => {
      axios
        .get("/validate_username/", { params: { username: signupUsername.value } })
        .then((response) => {
          if (response.data.is_taken) {
            usernameError.value = "이 사용자 이름은 이미 사용 중입니다.";
          } else {
            usernameError.value = "";
          }
        });
    };

  const checkEmail = () => {
    axios
      .get("/validate_email/", { params: { email: signupEmail.value } })
      .then((response) => {
        if (response.data.is_taken) {
          emailError.value = "이 이메일은 이미 사용 중입니다.";
        } else {
          emailError.value = "";
        }
      });
    };
  const checkAge = () => {
    if (age.value > 80 || age.value < 1) {
      emailError.value = "80세 이하만 가입 가능합니다.";
    } else {
      emailError.value = "";
    }
  };

  const submitForm = () => {
    console.log(signupUsername.value, signupEmail.value)
    if (signupUsername.value.trim() === '' || signupEmail.value.trim() === '') {
      Swal.fire({
        icon: 'error',
        title: '누락된 필드',
        text: '이메일과 유저네임을 모두 입력해주세요.',
        confirmButtonText: '확인'
      });
      return;
    }

    const formData = {
      username: signupUsername.value,
      email: signupEmail.value,
      age: age.value,
      password1: password1.value,
      password2: password2.value,
    };
    axios
      .post("/accounts/signup/", formData)
      .then((response) => {
        Swal.fire({
          icon: 'success',
          title: '회원가입 성공',
          text: '회원가입이 성공적으로 완료되었습니다.',
          confirmButtonText: '확인'
        }).then((result) => {
          if (result.isConfirmed) {
            router.push({ name: 'home' });
          }
        });
      })
      .catch((error) => {
        console.log(error);
        Swal.fire({
          icon: 'error',
          title: '오류 발생',
          text: '입력을 확인해주세요.',
          confirmButtonText: '확인'
        });
      });
  };



  // 로그인용
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
<script>
  // 모든 페이지가 다 구성되고 난 후에 js 코드를 추가하는 것!!
  window.onload = function () {
    const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');
    signUpButton.addEventListener('click', () => {
      container.classList.add("right-panel-active");
    });
    
    signInButton.addEventListener('click', () => {
      container.classList.remove("right-panel-active");
    });
  }
</script>

<style scoped>
  .body {
  background: #ffffff;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 80vh;
  margin: -20px 0 50px;
  }

  h1 {
    font-weight: bold;
    margin: 0;
  }

  h2 {
    text-align: center;
  }

  p {
    font-size: 14px;
    font-weight: 100;
    line-height: 20px;
    letter-spacing: 0.5px;
    margin: 20px 0 30px;
  }

  span {
    font-size: 12px;
  }

  a {
    color: #333;
    font-size: 14px;
    text-decoration: none;
    margin: 15px 0;
  }

  button {
    border-radius: 20px;
    border: 1px solid #450093;
    background-color: #450093;
    color: #FFFFFF;
    font-size: 12px;
    font-weight: bold;
    padding: 12px 45px;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: transform 80ms ease-in;
  }

  button:active {
    transform: scale(0.95);
  }

  button:focus {
    outline: none;
  }

  button.ghost {
    background-color: transparent;
    border-color: #FFFFFF;
  }

  form {
    background-color: #FFFFFF;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0 50px;
    height: 100%;
    text-align: center;
  }

  input {
    background-color: #eee;
    border: none;
    padding: 12px 15px;
    margin: 8px 0;
    width: 300px;
  }

  .container {
    background-color: #fff;
    border-radius: 10px;
      box-shadow: 0 14px 28px rgba(0,0,0,0.25), 
        0 10px 10px rgba(0,0,0,0.22);
    position: relative;
    overflow: hidden;
    width: 768px;
    max-width: 100%;
    min-height: 480px;
  }

  .form-container {
    position: absolute;
    top: 0;
    height: 100%;
    transition: all 0.6s ease-in-out;
  }

  .sign-in-container {
    left: 0;
    width: 50%;
    z-index: 2;
  }

  .container.right-panel-active .sign-in-container {
    transform: translateX(100%);
  }

  .sign-up-container {
    left: 0;
    width: 50%;
    opacity: 0;
    z-index: 1;
  }

  .container.right-panel-active .sign-up-container {
    transform: translateX(100%);
    opacity: 1;
    z-index: 5;
    animation: show 0.6s;
  }

  @keyframes show {
    0%, 49.99% {
      opacity: 0;
      z-index: 1;
    }
    
    50%, 100% {
      opacity: 1;
      z-index: 5;
    }
  }

  .overlay-container {
    position: absolute;
    top: 0;
    left: 50%;
    width: 50%;
    height: 100%;
    overflow: hidden;
    transition: transform 0.6s ease-in-out;
    z-index: 100;
  }

  .container.right-panel-active .overlay-container{
    transform: translateX(-100%);
  }

  .overlay {
    background: #450093;
    background: -webkit-linear-gradient(to right, #450093, #450093);
    background: linear-gradient(to right, #450093, #450093);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: 0 0;
    color: #FFFFFF;
    position: relative;
    left: -100%;
    height: 100%;
    width: 200%;
      transform: translateX(0);
    transition: transform 0.6s ease-in-out;
  }

  .container.right-panel-active .overlay {
      transform: translateX(50%);
  }

  .overlay-panel {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0 40px;
    text-align: center;
    top: 0;
    height: 100%;
    width: 50%;
    transform: translateX(0);
    transition: transform 0.6s ease-in-out;
  }

  .overlay-left {
    transform: translateX(-20%);
  }

  .container.right-panel-active .overlay-left {
    transform: translateX(0);
  }

  .overlay-right {
    right: 0;
    transform: translateX(0);
  }

  .container.right-panel-active .overlay-right {
    transform: translateX(20%);
  }

  .social-container {
    margin: 20px 0;
  }

  .social-container a {
    border: 1px solid #DDDDDD;
    border-radius: 50%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    margin: 0 5px;
    height: 40px;
    width: 40px;
  }
</style>