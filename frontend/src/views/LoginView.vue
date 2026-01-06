
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)
const router = useRouter()

const handleLogin = async () => {
    loading.value = true
    error.value = ''
    
    const formData = new FormData()
    formData.append('username', username.value)
    formData.append('password', password.value)

    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/auth/login/access-token`, {
            method: 'POST',
            body: formData
        })
        
        const data = await res.json()
        
        if (res.ok) {
            localStorage.setItem('token', data.access_token)
            router.push('/admin')
        } else {
            error.value = data.detail || 'Login failed'
        }
    } catch (e) {
        error.value = 'An error occurred'
    } finally {
        loading.value = false
    }
}
</script>

<template>
  <div class="auth-container">
    <div class="auth-card">
      <h2 class="auth-title">Login</h2>
      
      <form @submit.prevent="handleLogin">
        <div class="form-group">
            <label class="form-label">Username</label>
            <input v-model="username" type="text" class="form-input" required>
        </div>
        
        <div class="form-group">
            <label class="form-label">Password</label>
            <input v-model="password" type="password" class="form-input" required>
        </div>
        
        <div v-if="error" style="color: var(--danger-color); margin-bottom: 1rem;">
            {{ error }}
        </div>
        
        <button type="submit" class="btn" :disabled="loading">
            {{ loading ? 'Logging in...' : 'Login' }}
        </button>
      </form>
    </div>
  </div>
</template>
