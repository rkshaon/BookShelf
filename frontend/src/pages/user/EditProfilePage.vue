<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center">
    <div class="bg-white shadow-md rounded-lg p-6 mt-10 w-full max-w-md">
      <div v-if="isLoading" class="flex justify-center">
        <LoaderComponent />
      </div>
      <div v-else>
        <form @submit.prevent="editProfile">
          <div class="flex flex-col items-center">
            <img class="w-24 h-24 rounded-full object-cover" :src="getProfileImage(userData.profile_image, API_BASE_URL)"
              alt="User Avatar" />
          </div>
          <div class="mt-6">
            <h3 class="text-lg font-medium">Profile Information</h3>
            <div class="mt-4">
              <label class="block text-gray-700">First Name</label>
              <input type="text" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                v-model="userData.first_name" />
            </div>
            <div class="mt-4">
              <label class="block text-gray-700">Middle Name</label>
              <input type="text" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                v-model="userData.middle_name" />
            </div>
            <div class="mt-4">
              <label class="block text-gray-700">Last Name</label>
              <input type="text" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                v-model="userData.last_name" />
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
import { useToast } from 'vue-toastification'
import LoaderComponent from '@/components/general/LoaderComponent.vue'

export default {
  name: 'ProfilePage',
  components: {
    LoaderComponent
  },
  data () {
    return {
      user: { },
      userData: { }
    }
  },
  computed: {
    API_BASE_URL () {
      return process.env.VUE_APP_BACKEND_URL
    },
    ...mapGetters({
      isAuthenticated: 'isAuthenticated',
      isLoading: 'isLoading',
      userProfile: 'userProfile',
      errors: 'editProfileError',
      successMessage: 'editSuccessMessage'
    })
  },
  mounted () {
    document.title = 'Book Shelf | Edit Profile'
    if (this.isAuthenticated && (!this.user || Object.keys(this.user).length === 0)) {
      this.fetchUserProfile()
    }
    this.user = { ...this.userProfile }
    this.userData = { ...this.userProfile }
  },
  methods: {
    ...mapActions([
      'fetchUserProfile', 'editUserProfile', 'clearSuccessMessage'
    ]),
    getProfileImage,
    getUpdatedFields () {
      const updatedFields = {}
      for (const key in this.userData) {
        if (this.userData[key] !== this.user[key]) {
          updatedFields[key] = this.userData[key]
        }
      }
      return updatedFields
    },
    async editProfile () {
      const updatedFields = this.getUpdatedFields()
      const toast = useToast()

      if (Object.keys(updatedFields).length === 0) {
        toast.info('No changes to save')
        return
      }

      try {
        await this.editUserProfile(updatedFields)
        this.$router.push({ name: 'Profile' })
        this.clearSuccessMessage()
      } catch (error) {
        toast.error('Failed to update profile')
      }
    }
  },
  watch: {
    user (newProfile) {
      this.userData = { ...newProfile }
    },
    errors (newErrors) {
      const toast = useToast()
      if (newErrors && newErrors.length) {
        newErrors.forEach(error => {
          toast.error(error)
        })
      }
    },
    successMessage (newMessage) {
      const toast = useToast()
      if (newMessage) {
        toast.success(newMessage)
      }
    }
  }
}
</script>

<style scoped>
/* Add any additional styling here */
</style>
