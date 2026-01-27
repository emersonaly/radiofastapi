
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const isRegister = ref(false)
const username = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)
const router = useRouter()

const toggleAuthMode = () => {
    isRegister.value = !isRegister.value
    error.value = ''
    username.value = ''
    password.value = ''
}

const handleSubmit = async () => {
    loading.value = true
    error.value = ''
    
    if (isRegister.value) {
        await handleRegister()
    } else {
        await handleLogin()
    }
}

const handleRegister = async () => {
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/auth/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username.value,
                password: password.value
            })
        })
        
        const data = await res.json()
        
        if (res.ok) {
            // After registration, auto login or ask to login
            // Let's auto login for better UX
            await handleLogin()
        } else {
            error.value = data.detail || 'Registration failed'
            loading.value = false
        }
    } catch (e) {
        error.value = 'An error occurred during registration'
        loading.value = false
    }
}

const handleLogin = async () => {
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
      <h2 class="auth-title">{{ isRegister ? 'Register' : 'Login' }}</h2>
      
      <form @submit.prevent="handleSubmit">
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
            {{ loading ? 'Processing...' : (isRegister ? 'Register' : 'Login') }}
        </button>

        <p style="margin-top: 1rem; text-align: center;">
            <a href="#" @click.prevent="toggleAuthMode" style="color: var(--primary-color);">
                {{ isRegister ? 'Already have an account? Login' : 'Need an account? Register' }}
            </a>
        </p>
      </form>
    </div>
  </div>
</template>
