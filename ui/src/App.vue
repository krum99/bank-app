<template>
  <div class="container py-5">
    <h1 class="text-center mb-4">Welcome</h1>
    <div class="d-flex flex-column flex-md-row justify-content-center gap-4">
      
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
      loginMessage: ''
    };
  },
  methods: {
    async register() {
      const response = await fetch('http://localhost:8000/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this.registerData)
      });
      const result = await response.json();
      this.registerMessage = result.message || result.detail;
    },
    async login() {
      const response = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this.loginData)
      });
      const result = await response.json();
      this.loginMessage = result.message || result.detail;
    }
  }
};
</script>
