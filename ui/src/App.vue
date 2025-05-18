<template>
  <div class="container py-5">
    <h1 class="text-center mb-4">Welcome</h1>

    <!-- Logged -->
    <div v-if="isLoggedIn" class="text-center">
      <h3>Logged in as user #{{ currentUserId }}</h3>
      <button @click="logout" class="btn btn-outline-danger mt-3">Logout</button>
    </div>

    <!-- NOT Logged -->
    <div v-else class="d-flex flex-column flex-md-row justify-content-center gap-4">
      
      <!-- Register Form -->
      <form @submit.prevent="register" class="card p-4 w-100" style="max-width: 400px;">
        <h3 class="mb-3">Register</h3>
        <input v-model="registerData.username" class="form-control mb-2" placeholder="Username" required />
        <input v-model="registerData.password" class="form-control mb-3" type="password" placeholder="Password" required />
        <button type="submit" class="btn btn-primary w-100">Register</button>
        <div class="mt-2 text-success" v-if="registerMessage">{{ registerMessage }}</div>
      </form>

      <!-- Login Form -->
      <form @submit.prevent="login" class="card p-4 w-100" style="max-width: 400px;">
        <h3 class="mb-3">Login</h3>
        <input v-model="loginData.username" class="form-control mb-2" placeholder="Username" required />
        <input v-model="loginData.password" class="form-control mb-3" type="password" placeholder="Password" required />
        <button type="submit" class="btn btn-success w-100">Login</button>
        <div class="mt-2 text-success" v-if="loginMessage">{{ loginMessage }}</div>
      </form>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      registerData: { username: '', password: '' },
      loginData: { username: '', password: '' },
      registerMessage: '',
      loginMessage: '',
      isLoggedIn: false,
      currentUserId: null
    };
  },
  mounted() {
    const storedUser = localStorage.getItem("user_id");
    if (storedUser) {
      this.isLoggedIn = true;
      this.currentUserId = storedUser;
    }
  },
  methods: {
    async register() {
      try {
        const response = await fetch('http://localhost:8000/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.registerData)
        });
        const result = await response.json();
        this.registerMessage = result.message || result.detail;
      } catch (error) {
        this.registerMessage = "Registration failed.";
      }
    },
    async login() {
      try {
        const response = await fetch('http://localhost:8000/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.loginData)
        });
        const result = await response.json();
        if (response.ok) {
          localStorage.setItem("user_id", result.user_id);
          this.isLoggedIn = true;
          this.currentUserId = result.user_id;
        } else {
          this.loginMessage = result.detail || "Login failed.";
        }
      } catch (error) {
        this.loginMessage = "Login failed.";
      }
    },
    logout() {
      localStorage.removeItem("user_id");
      this.isLoggedIn = false;
      this.currentUserId = null;
    }
  }
};
</script>
