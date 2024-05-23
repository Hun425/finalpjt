import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    isLoggedIn: false,
    user: null,
    token: null,
  }),
  actions: {
    login(user, token) {
      this.isLoggedIn = true
      this.user = user
      this.token = token
    },
    logout() {
      this.isLoggedIn = false
      this.user = null  
      this.token = null
    },
    async checkAuthStatus() {
      try {
        const response = await fetch('/api/check-auth/', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${this.token}`,
          }
        })
        const data = await response.json()
        if (data.isLoggedIn) {
          this.login(data.user, this.token)
        } else {
          this.logout()
        }
      } catch (error) {
        this.logout()
      }
    }
  }
})
