<template>
    <div class="flex justify-center items-center min-h-screen bg-gray-100">
        <LoaderComponent v-if="isLoading" />
        <div v-else class="w-full max-w-md bg-white shadow-lg rounded-lg p-8">
            <h2 class="text-2xl font-bold text-center text-gray-800 mb-6">Sign In for BookShelf</h2>
            <form @submit.prevent="logInUser">
                <div class="mb-4">
                    <label for="credential" class="block text-gray-700 font-semibold mb-2">Credential</label>
                    <input type="text" id="credential" v-model="credential"
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
                    Sign In
                </button>
            </form>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { useToast } from 'vue-toastification'
import LoaderComponent from '@/components/LoaderComponent.vue'

export default {
  name: 'SignInPage',
  components: {
    LoaderComponent
  },
  data () {
    return {
      credential: '',
      password: ''
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
    }
    // If the user is authenticated, redirect to the home page
    // '$store.state.auth.isAuthenticated' (val) {
    //   if (val) {
    //     this.$router.push({ name: 'Home' })
    //   }
    // }
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
      // Call the login action from the store
      // await this.$store.dispatch('auth/login', { credential: this.credential, password: this.password })
      // If the user is authenticated, redirect to the home page
      // if (this.$store.state.auth.isAuthenticated) {
      //   this.$router.push({ name: 'Home' })
      // }
    }
  }
}
</script>

<style scoped>
/* Add any additional styling if necessary */
</style>
