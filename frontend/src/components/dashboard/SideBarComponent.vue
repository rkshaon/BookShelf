<template>
    <aside class="w-64 bg-gray-800 text-white flex flex-col">
        <div class="p-6 text-2xl font-semibold text-center">
            Dashboard
        </div>
        <nav class="flex-grow">
            <ul>
                <li class="p-4 hover:bg-gray-700 cursor-pointer">
                    <router-link to="/dashboard/" class="flex items-center">
                        <span class="ml-2">Overview</span>
                    </router-link>
                </li>
                <li class="p-4 hover:bg-gray-700 cursor-pointer">
                    <router-link to="/dashboard/authors" class="flex items-center">
                        <span class="ml-2">Authors</span>
                    </router-link>
                </li>
                <li class="p-4 hover:bg-gray-700 cursor-pointer">
                    <router-link to="/dashboard/books?page=1" class="flex items-center">
                        <span class="ml-2">Books</span>
                    </router-link>
                </li>
                <li class="p-4 hover:bg-gray-700 cursor-pointer">
                    <router-link to="/dashboard/users" class="flex items-center">
                        <span class="ml-2">Users</span>
                    </router-link>
                </li>
                <li class="p-4 hover:bg-gray-700 cursor-pointer">
                    <router-link to="/dashboard/reports" class="flex items-center">
                        <span class="ml-2">Reports</span>
                    </router-link>
                </li>
            </ul>
        </nav>
        <div class="p-4">
            <button @click="logoutUser()" class="bg-red-500 px-4 py-2 rounded text-white w-full hover:bg-red-600">
                Logout
            </button>
        </div>
    </aside>
</template>

<script>
import { useToast } from 'vue-toastification'
import { mapActions } from 'vuex'

export default {
  name: 'SideBarComponent',
  methods: {
    ...mapActions(['logout']),
    async logoutUser () {
      const toast = useToast()
      await this.logout()
      toast.info('Logged out successfully')
      this.$router.push({ name: 'SignIn' })
    }
  }
}
</script>
