<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center">
    <div class="bg-white shadow-md rounded-lg p-6 mt-10 w-full max-w-md">
      <div v-if="isLoading" class="flex justify-center">
        <LoaderComponent />
      </div>
      <div v-else>
        <form @submit.prevent="editProfile">
          <div class="flex flex-col items-center">
            <img class="w-24 h-24 rounded-full object-cover" :src="getProfileImage(user.profile_image, API_BASE_URL)"
              alt="User Avatar" />
          </div>
          <div class="mt-6">
            <h3 class="text-lg font-medium">Profile Information</h3>
            <div class="mt-4">
              <label class="block text-gray-700">First Name</label>
              <input type="text" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                v-model="user.first_name" />
            </div>
            <div class="mt-4">
              <label class="block text-gray-700">Middle Name</label>
              <input type="text" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                v-model="user.middle_name" />
            </div>
            <div class="mt-4">
              <label class="block text-gray-700">Last Name</label>
              <input type="text" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                v-model="user.last_name" />
            </div>
            <div class="mt-6 flex justify-end">
              <button class="bg-blue-500 text-white px-4 py-2 rounded-md shadow-sm hover:bg-blue-600">
                Save Changes
              </button>
            </div>
          </div>
        </form>

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
    getProfileImage,
    async editProfile () {
      console.log('Edit Profile')
      console.log(this.user)
    }
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
