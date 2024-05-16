<template>
  <div>
    <form @submit.prevent="register">
      <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" required />
        <div v-if="errors.username" class="error">{{ errors.username }}</div>
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" required />
        <div v-if="errors.email" class="error">{{ errors.email }}</div>
      </div>
      <div>
        <label for="age">Age:</label>
        <input type="number" v-model="age" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" required />
      </div>
      <div>
        <label for="password2">Confirm Password:</label>
        <input type="password" v-model="password2" required />
      </div>
      <button type="submit">Sign Up</button>
    </form>
    <div v-if="errors.non_field_errors" class="error">
      {{ errors.non_field_errors }}
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      email: "",
      age: null,
      password: "",
      password2: "",
      errors: {},
    };
  },
  methods: {
    async register() {
      this.errors = {};
      try {
        const response = await axios.post("/accounts/signup/", {
          username: this.username,
          email: this.email,
          age: this.age,
          password1: this.password,
          password2: this.password2,
        });
        console.log("회원가입 성공:", response.data);
      } catch (err) {
        if (err.response && err.response.data) {
          this.errors = err.response.data;
        } else {
          this.errors.non_field_errors = [
            "An unexpected error occurred. Please try again.",
          ];
        }
      }
    },
  },
};
</script>

<style>
.error {
  color: red;
}
</style>
