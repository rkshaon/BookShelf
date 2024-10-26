<template>
    <div class="flex justify-center items-center min-h-screen bg-gray-100">
        <div class="w-full max-w-md bg-white shadow-lg rounded-lg p-8">
            <h2 class="text-2xl font-bold text-center text-gray-800 mb-6">Sign Up for BookShelf</h2>
            <form @submit.prevent="registerUser">
                <div class="mb-4">
                    <label for="first_name" class="block text-gray-700 font-semibold mb-2">First Name</label>
                    <input type="text" id="first_name" v-model="first_name"
                        class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                        required />
                </div>
                <div class="mb-4">
                    <label for="middle_name" class="block text-gray-700 font-semibold mb-2">Middle Name</label>
                    <input type="text" id="middle_name" v-model="middle_name"
                        class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300" />
                </div>
                <div class="mb-4">
                    <label for="last_name" class="block text-gray-700 font-semibold mb-2">Last Name</label>
                    <input type="text" id="last_name" v-model="last_name"
                        class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                        required />
                </div>
                <div class="mb-4">
                    <label for="username" class="block text-gray-700 font-semibold mb-2">Username</label>
                    <input type="text" id="username" v-model="username"
                        class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                        required />
                </div>
                <div class="mb-4">
                    <label for="email" class="block text-gray-700 font-semibold mb-2">Email</label>
                    <input type="email" id="email" v-model="email"
                        class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                        required />
                </div>
                <div class="mb-6">
                    <label for="password" class="block text-gray-700 font-semibold mb-2">Password</label>
                    <input type="password" id="password" v-model="password"
                        class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                        required />
                </div>
                <button type="submit"
                    class="w-full bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300">
                    Sign Up
                </button>
                <div v-if="errorMessage" class="mt-4 text-red-500 text-center">{{ errorMessage }}</div>
                <div v-if="successMessage" class="mt-4 text-green-500 text-center">{{ successMessage }}</div>
            </form>
        </div>
    </div>
</template>

<script>
// import { useStore } from "vuex";

export default {
  name: 'SignUpPage',
  data () {
    return {
      username: '',
      email: '',
      first_name: '',
      middle_name: '',
      last_name: '',
      password: '',
      errorMessage: null,
      successMessage: null
    }
  },
  methods: {
    async registerUser () {
      this.errorMessage = null
      this.successMessage = null
      const user = {
        username: this.username,
        email: this.email,
        first_name: this.first_name,
        middle_name: this.middle_name,
        last_name: this.last_name,
        password: this.password
      }

      try {
        // Call store function to register the user
        await this.$store.dispatch('register', user)

        // Show success message and clear form fields
        this.successMessage = 'Registration successful!'
        this.username = ''
        this.email = ''
        this.password = ''
      } catch (error) {
        console.error('Error:', error)
        this.errorMessage = error.response?.data?.detail || 'Registration failed. Please try again.'
      }

      //   try {
      //     // Call store function to register the user
      //     await this.$store.dispatch("registerUser", {
      //       username: this.username,
      //       email: this.email,
      //       password: this.password,
      //     });

      //     // Show success message and clear form fields
      //     this.successMessage = "Registration successful!";
      //     this.username = "";
      //     this.email = "";
      //     this.password = "";
      //   } catch (error) {
      //     console.error("Error:", error);
      //     this.errorMessage = error.response?.data?.detail || "Registration failed. Please try again.";
      //   }
    }
  }
}
</script>

<style scoped>
/* Add any additional styling if necessary */
</style>
