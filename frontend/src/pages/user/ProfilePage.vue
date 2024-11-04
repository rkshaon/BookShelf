<template>
    <div class="min-h-screen bg-gray-100 flex flex-col items-center">
        <div class="bg-white shadow-md rounded-lg p-6 mt-10 w-full max-w-md">
            <div v-if="isLoading" class="flex justify-center">
                <LoaderComponent />
            </div>
            <div v-else>
                <div class="flex flex-col items-center">
                    <img class="w-24 h-24 rounded-full object-cover"
                        :src="getProfileImage(user.profile_image, API_BASE_URL)" alt="User Avatar" />
                    <h2 class="mt-4 text-xl font-semibold">{{ user.full_name || 'Full Name' }}</h2>
                    <p class="text-gray-600">{{ user.email || 'yourmail@example.com' }}</p>
                    <p class="text-gray-600">{{ user.role || 'User Role' }}</p>
                </div>
                <div class="mt-6">
                    <h3 class="text-lg font-medium">Profile Information</h3>
                    <div class="mt-4">
                        <label class="block text-gray-700">First Name</label>
                        <input type="text" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                            :value="user.first_name" />
                    </div>
                    <div class="mt-4">
                        <label class="block text-gray-700">Middle Name</label>
                        <input type="text" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                            :value="user.middle_name" />
                    </div>
                    <div class="mt-4">
                        <label class="block text-gray-700">Last Name</label>
                        <input type="text" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                            :value="user.last_name" />
                    </div>
                    <div class="mt-4">
                        <label class="block text-gray-700">Email</label>
                        <input type="email" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                            :value="user.email" />
                    </div>
                    <!-- <div class="mt-4">
                        <label class="block text-gray-700">Bio</label>
                        <textarea class="mt-1 block w-full border-gray-300 rounded-md shadow-sm" rows="3">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    </textarea>
                    </div> -->
                    <div class="mt-6 flex justify-end">
                        <button class="bg-blue-500 text-white px-4 py-2 rounded-md shadow-sm hover:bg-blue-600">
                            Save Changes
                        </button>
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
      isLoading: 'isLoading',
      user: 'userProfile'
    })
  },
  mounted () {
    this.fetchUserProfile()
    document.title = 'Book Shelf | Loading ...'
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
