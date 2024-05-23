<template>
  <div>
    <h2>회원가입</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" @blur="checkUsername" />
        <span v-if="usernameError" class="error">{{ usernameError }}</span>
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" @blur="checkEmail" />
        <span v-if="emailError" class="error">{{ emailError }}</span>
      </div>
      <div>
        <label for="age">Age:</label>
        <input type="number" v-model="age" @blur="checkAge"/>
        <span v-if="ageError">{{ ageError }}</span>
      </div>
      <div>
        <label for="password1" >Password:</label>
        <input type="password" v-model="password1" />
      </div>
      <div>
        <label for="password2">Confirm Password:</label>
        <input type="password" v-model="password2" />
      </div>
      <button type="submit">가입하기</button>
    </form>
  </div>
</template>

<script>
  import router from "@/router";
  import axios from "axios";
  import Swal from 'sweetalert2';

  export default {
    data() {
      return {
        username: "",
        email: "",
        age:"",
        password1: "",
        password2: "",
        usernameError: "",
        emailError: "",
      };
    },
    methods: {
      checkUsername() {
        axios
          .get("/validate_username/", { params: { username: this.username } })
          .then((response) => {
            if (response.data.is_taken) {
              this.usernameError = "이 사용자 이름은 이미 사용 중입니다.";
            } else {
              this.usernameError = "";
            }
          });
      },
      checkEmail() {
        axios
          .get("/validate_email/", { params: { email: this.email } })
          .then((response) => {
            if (response.data.is_taken) {
              this.emailError = "이 이메일은 이미 사용 중입니다.";
            } else {
              this.emailError = "";
            }
          });
      },
      checkAge() {
        if (this.age > 80 || this.age < 1) {
          this.emailError = "80세 이하만 가입 가능합니다.";
        } else {
          this.emailError = "";
        }
      },
      submitForm() {
        // 입력 필드 검증
        if (this.username.trim() === '' || this.email.trim() === '') {
          Swal.fire({
            icon: 'error',
            title: '누락된 필드',
            text: '이메일과 유저네임을 모두 입력해주세요.',
            confirmButtonText: '확인'
          });
          return; // 공백이면 함수 종료
        }

        const formData = {
          username: this.username,
          email: this.email,
          age:this.age,
          password1: this.password1,
          password2: this.password2,
        };

        axios
          .post("/accounts/signup/", formData)
          .then((response) => {
            // 회원가입이 성공적으로 완료되었을 때 SweetAlert2 알림창 표시
            Swal.fire({
              icon: 'success',
              title: '회원가입 성공',
              text: '회원가입이 성공적으로 완료되었습니다.',
              confirmButtonText: '확인'
            }).then((result) => {
              // 확인 버튼을 클릭하면 홈 페이지로 이동
              if (result.isConfirmed) {
                router.push({name:'home'});
              }
            });
          })
          .catch((error) => {
            // 에러 처리
            console.log(error);
            Swal.fire({
            icon: 'error',
            title: '오류 발생',
            text: '입력을 확인해주세요.',
            confirmButtonText: '확인'
          });
          });
      },
    },
  };
</script>



<style>
.error {
  color: red;
}
</style>
