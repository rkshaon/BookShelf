<template>
  <div class="bg-gray-600 text-white py-2" @click="closeDropdown">
    <div class="container mx-auto px-4 flex justify-between items-center">
      <div class="overflow-hidden h-6">
        <div class="flex flex-col animate-slide">
          <span v-for="(item, index) in adList" :key="index">
            <a :href="item.url" target="_blank" class="hover:text-gray-300">{{ item.title }}</a>
          </span>
        </div>
      </div>
      <div class="flex space-x-4">
        <div v-if="isAuthenticated" class="flex space-x-4" @click.stop>
          <!-- <div class="flex space-x-4"> -->
          <button @click="toggleDropdown"
            class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 flex items-center">
            <img :src="getProfileImage(user.profile_image, API_BASE_URL)" alt="Profile" class="w-6 h-6 rounded-full">
            <span class="text-white ml-2">Profile</span>
          </button>
          <div v-if="dropdownOpen" class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-20">
            <router-link to="/profile" class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
              @click="closeDropdown">Profile</router-link>
            <router-link to="/dashboard" class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
              @click="closeDropdown">Dashboard</router-link>
            <a href="#" class="block px-4 py-2 text-gray-800 hover:bg-gray-100" @click="closeDropdown">Account
              Settings</a>
            <button v-if="isAuthenticated" @click="closeDropdown(); logoutUser()"
              class="block px-4 py-2 text-gray-800 hover:bg-gray-100">
              Logout
            </button>
          </div>
          <!-- </div> -->
        </div>
        <div v-else class="flex space-x-4">
          <router-link to="signup" class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600">
            Sign Up
          </router-link>
          <router-link to="signin" class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600">
            Sign In
          </router-link>
        </div>
        <button class="px-3 py-1 bg-gray-700 text-white rounded hover:bg-gray-600">Language</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { useToast } from 'vue-toastification'
import { getProfileImage } from '@/helpers/getProfileImage'

export default {
  name: 'TopBarComponent',
  data () {
    return {
      adList: [
        {
          id: 1,
          title: 'Welcome to BookShelf!',
          url: ''
        },
        {
          id: 2,
          title: 'Follow the developer',
          url: 'https://rkshaon.info'
        },
        {
          id: 3,
          title: 'Join our community of book lovers!',
          url: 'https://rkshaon.info'
        }
      ],
      dropdownOpen: false
    }
  },
  computed: {
    ...mapGetters({
      isAuthenticated: 'isAuthenticated',
      user: 'userProfile'
    }),
    API_BASE_URL () {
      return process.env.VUE_APP_BACKEND_URL
    }
  },
  methods: {
    ...mapActions(['logout', 'fetchUserProfile']),
    getProfileImage,
    toggleDropdown () {
      this.dropdownOpen = !this.dropdownOpen
    },
    closeDropdown () {
      this.dropdownOpen = false
    },
    handleClickOutside (event) {
      if (!this.$el.contains(event.target)) {
        this.dropdownOpen = false
      }
    },
    async logoutUser () {
      console.log('Logout')
      await this.logout()
      const toast = useToast()
      toast.info('You have successfully logged out')
      this.$router.push({ name: 'SignIn' })
    }
  },
  mounted () {
    document.addEventListener('click', this.handleClickOutside)

    if (this.isAuthenticated && (!this.user || Object.keys(this.user).length === 0)) {
      this.fetchUserProfile()
    }
  },
  beforeUnmount () {
    document.removeEventListener('click', this.handleClickOutside)
  }
}
</script>

<style scoped>
/* Animation for sliding text */
@keyframes slide {
  0% {
    transform: translateY(0);
  }

  33% {
    transform: translateY(-100%);
  }

  66% {
    transform: translateY(-200%);
  }

  100% {
    transform: translateY(0);
  }
}

.animate-slide {
  animation: slide 9s linear infinite;
}
</style>
