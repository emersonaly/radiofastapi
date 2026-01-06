
<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const stations = ref([])
const router = useRouter()
const newStation = ref({ name: '', stream_url: '', genre: '' })

const fetchStations = async () => {
   const res = await fetch(`${import.meta.env.VITE_API_URL}/stations/`)
   if (res.ok) stations.value = await res.json()
}

const logout = () => {
    localStorage.removeItem('token')
    router.push('/login')
}

const addStation = async () => {
    const token = localStorage.getItem('token')
    if (!token) return router.push('/login')
    
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/stations/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(newStation.value)
        })
        
        if (res.ok) {
            newStation.value = { name: '', stream_url: '', genre: '' }
            fetchStations()
        } else {
            alert('Failed to add station')
        }
    } catch (e) {
        alert('Error adding station')
    }
}

const deleteStation = async (id) => {
    if (!confirm('Are you sure?')) return
    
    const token = localStorage.getItem('token')
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/stations/${id}`, {
            method: 'DELETE',
             headers: {
                'Authorization': `Bearer ${token}`
            }
        })
        if (res.ok) fetchStations()
    } catch (e) {
        alert('Error deleting')
    }
}

onMounted(() => {
    fetchStations()
})
</script>

<template>
  <div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
        <h1>Admin Panel</h1>
        <button @click="logout" class="btn" style="width: auto; background-color: var(--danger-color);">Logout</button>
    </div>

    <!-- Add Station Form -->
    <div class="auth-card" style="max-width: 100%; margin-bottom: 2rem;">
        <h3 style="margin-bottom: 1rem;">Add New Station</h3>
        <form @submit.prevent="addStation" style="display: flex; gap: 1rem; align-items: flex-end; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 200px;">
                <label class="form-label">Name</label>
                <input v-model="newStation.name" class="form-input" required>
            </div>
             <div style="flex: 2; min-width: 300px;">
                <label class="form-label">Stream URL</label>
                <input v-model="newStation.stream_url" class="form-input" required>
            </div>
             <div style="flex: 1; min-width: 150px;">
                <label class="form-label">Genre</label>
                <input v-model="newStation.genre" class="form-input">
            </div>
            <button type="submit" class="btn" style="width: auto;">Add</button>
        </form>
    </div>

    <!-- Stations List -->
    <div class="table-responsive auth-card" style="max-width: 100%; padding: 0;">
        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>URL</th>
                    <th>Genre</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="station in stations" :key="station.id">
                    <td>{{ station.id }}</td>
                    <td>{{ station.name }}</td>
                    <td style="max-width: 300px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{{ station.stream_url }}</td>
                    <td>{{ station.genre }}</td>
                    <td>
                        <button @click="deleteStation(station.id)" class="btn-icon">🗑️</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
  </div>
</template>
