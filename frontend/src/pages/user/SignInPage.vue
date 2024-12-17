<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <LoaderComponent v-if="isLoading" />
    <div v-else class="w-full max-w-md bg-white shadow-lg rounded-lg p-8">
      <h2 class="text-2xl font-bold text-center text-gray-800 mb-6">Sign In for BookShelf</h2>
      <form @submit.prevent="logInUser">
        <div class="mb-4">
          <label for="credential" class="block text-gray-700 font-semibold mb-2">Credential</label>
          <input type="text" id="credential" v-model="credential"
            class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300" required />
        </div>
        <!--
        <div class="mb-6">
          <label for="password" class="block text-gray-700 font-semibold mb-2">Password</label>
          <input type="password" id="password" v-model="password"
            class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300" required />
        </div>
        -->
        <div class="mb-6 relative">
          <label for="password" class="block text-gray-700 font-semibold mb-2">Password</label>
          <input :type="showPassword ? 'text' : 'password'" id="password" v-model="password"
            class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300" required />
          <!-- <button type="button" @click="togglePassword"
            class="absolute top-1/2 right-3 transform -translate-y-1/2 text-blue-500 text-sm focus:outline-none">
            {{ showPassword ? 'Hide' : 'Show' }}
          </button> -->
          <!-- <button type="button" @click="togglePassword"
            class="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-500 focus:outline-none">
            <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M13.875 18.825A9.956 9.956 0 0112 19c-4.418 0-8.2-2.69-10-6.5a12.401 12.401 0 015.333-6.433m4.542 3.543a3 3 0 104.242-4.242m-4.242 4.242L3 3m6 15l3 3m9-9l-3-3" />
            </svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 12a3 3 0 11-6 0 3 3 0 016 0zM2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-.012.046-.035.136-.072.257m-1.918 2.5C18.15 15.854 15.264 17 12 17c-3.265 0-6.151-1.146-8.552-3.243a11.42 11.42 0 01-1.918-2.5m18.49-1.072L20 12m-4 0a4 4 0 01-8 0 4 4 0 018 0z" />
            </svg>
          </button> -->
          <!-- Eye Icon (Fixed Alignment) -->
          <button type="button" @click="togglePassword"
            class="absolute top-1/2 right-3 transform -translate-y-1/2 text-gray-500 focus:outline-none">
            <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <!-- Open Eye Icon -->
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M13.875 18.825A9.956 9.956 0 0112 19c-4.418 0-8.2-2.69-10-6.5a12.401 12.401 0 015.333-6.433m4.542 3.543a3 3 0 104.242-4.242m-4.242 4.242L3 3m6 15l3 3m9-9l-3-3" />
            </svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <!-- Closed Eye Icon -->
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 12a3 3 0 11-6 0 3 3 0 016 0zM2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-.012.046-.035.136-.072.257m-1.918 2.5C18.15 15.854 15.264 17 12 17c-3.265 0-6.151-1.146-8.552-3.243a11.42 11.42 0 01-1.918-2.5m18.49-1.072L20 12m-4 0a4 4 0 01-8 0 4 4 0 018 0z" />
            </svg>
          </button>
        </div>
        <button type="submit"
          class="w-full bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300">
          Sign In
        </button>
      </form>
      <p class="mt-4 text-center text-gray-600">
        Don't have an account?
        <router-link to="/signup" class="text-blue-500 hover:underline">Sign up here</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { useToast } from 'vue-toastification'
import LoaderComponent from '@/components/general/LoaderComponent.vue'

export default {
  name: 'SignInPage',
  components: {
    LoaderComponent
  },
  data () {
    return {
      credential: '',
      password: '',
      showPassword: false
    }
  },
  computed: {
    ...mapGetters({
      errors: 'loginError',
      isLoading: 'isLoading',
      isAuthenticated: 'isAuthenticated'
    })
  },
  watch: {
    errors (newErrors) {
      const toast = useToast()
      if (newErrors && newErrors.length) {
        newErrors.forEach(error => {
          toast.error(error)
        })
      }
    },
    isAuthenticated (val) {
      const toast = useToast()
      if (val) {
        toast.success('You have successfully logged in')
        this.$router.push({ name: 'Profile' })
      }
    }
  },
  mounted () {
    document.title = 'Book Shelf | Sign In'
  },
  methods: {
    ...mapActions(['login']),
    async logInUser () {
      const userCredential = {
        credential: this.credential,
        password: this.password
      }
      console.log(userCredential)
      this.login(userCredential)
    },
    togglePassword () {
      this.showPassword = !this.showPassword
    }
  }
}
</script>

<style scoped>
/* Add any additional styling if necessary */
</style>
