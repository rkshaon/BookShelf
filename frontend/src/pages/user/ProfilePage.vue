<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center">
    <div class="bg-white shadow-md rounded-lg p-6 mt-10 w-full max-w-md">
      <div v-if="isLoading" class="flex justify-center">
        <LoaderComponent />
      </div>
      <div v-else>
        <div class="flex flex-col items-center">
          <img class="w-24 h-24 rounded-full object-cover" :src="getProfileImage(user.profile_image, API_BASE_URL)"
            alt="User Avatar" />
          <h2 class="mt-4 text-xl font-semibold">{{ user.full_name || 'Full Name' }}</h2>
          <p class="text-gray-600">{{ user.email || 'yourmail@example.com' }}</p>
          <p class="text-gray-600">{{ user.role_display || 'User Role' }}</p>
        </div>
        <div class="mt-6">
          <h3 class="text-lg font-medium">Profile Information</h3>
          <div class="mt-4">
            <label class="block text-gray-700">First Name</label>
            <p class="mt-1 text-gray-800">{{ user.first_name || 'N/A' }}</p>
          </div>
          <div class="mt-4">
            <label class="block text-gray-700">Middle Name</label>
            <p class="mt-1 text-gray-800">{{ user.middle_name || 'N/A' }}</p>
          </div>
          <div class="mt-4">
            <label class="block text-gray-700">Last Name</label>
            <p class="mt-1 text-gray-800">{{ user.last_name || 'N/A' }}</p>
          </div>
          <div class="mt-4">
            <label class="block text-gray-700">Email</label>
            <p class="mt-1 text-gray-800">{{ user.email || 'N/A' }}</p>
          </div>
          <!-- Optional bio section
                    <div class="mt-4">
                        <label class="block text-gray-700">Bio</label>
                        <p class="mt-1 text-gray-800">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                    </div> -->
          <div class="mt-6 flex justify-end">
            <router-link to="/edit/profile" class="bg-blue-500 text-white px-4 py-2 rounded-md shadow-sm hover:bg-blue-600">
              Edit
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { getProfileImage } from '@/helpers/getProfileImage'
import LoaderComponent from '@/components/general/LoaderComponent.vue'

export default {
  name: 'ProfilePage',
  components: {
    LoaderComponent
  },
  computed: {
    API_BASE_URL () {
      return process.env.VUE_APP_BACKEND_URL
    },
    ...mapGetters({
      isAuthenticated: 'isAuthenticated',
      isLoading: 'isLoading',
      user: 'userProfile'
    })
  },
  mounted () {
    document.title = 'Book Shelf | Loading ...'
    if (this.isAuthenticated && (!this.user || Object.keys(this.user).length === 0)) {
      this.fetchUserProfile()
      document.title = `Book Shelf | ${this.user.full_name || 'User Profile'}`
    }
    if (this.user && Object.keys(this.user).length > 0) {
      document.title = `Book Shelf | ${this.user.full_name || 'User Profile'}`
    }
  },
  methods: {
    ...mapActions(['fetchUserProfile']),
    getProfileImage
  },
  watch: {
    user (newProfile) {
      if (newProfile && Object.keys(newProfile).length > 0) {
        document.title = `Book Shelf | ${newProfile.full_name || 'User Profile'}`
      }
    }
  }
}
</script>

<style scoped>
/* Add any additional styling here */
</style>
