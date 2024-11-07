<template>
  <div class="flex min-h-screen bg-gray-100">
    <!-- Sidebar -->

    <!-- Main Content -->
    <main class="flex-1 p-6">
      <!-- Page Title -->
      <h1 class="text-3xl font-bold mb-6">Welcome to Your Dashboard</h1>

      <!-- Metric Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
        <div class="bg-white shadow rounded-lg p-6 text-center">
          <p class="text-gray-500 text-sm font-medium">Users</p>
          <h2 class="text-2xl font-semibold">1,234</h2>
        </div>
        <div class="bg-white shadow rounded-lg p-6 text-center">
          <p class="text-gray-500 text-sm font-medium">New Signups</p>
          <h2 class="text-2xl font-semibold">56</h2>
        </div>
        <div class="bg-white shadow rounded-lg p-6 text-center">
          <p class="text-gray-500 text-sm font-medium">Revenue</p>
          <h2 class="text-2xl font-semibold">$12,345</h2>
        </div>
        <div class="bg-white shadow rounded-lg p-6 text-center">
          <p class="text-gray-500 text-sm font-medium">Active Users</p>
          <h2 class="text-2xl font-semibold">789</h2>
        </div>
      </div>

      <!-- Recent Activity Section -->
      <section>
        <h2 class="text-2xl font-semibold mb-4">Recent Activities</h2>
        <div class="bg-white shadow rounded-lg p-6 space-y-4">
          <div v-for="(activity, index) in recentActivities" :key="index" class="flex justify-between items-center">
            <p class="text-gray-700">{{ activity.description }}</p>
            <span class="text-gray-500 text-sm">{{ activity.time }}</span>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import { useToast } from 'vue-toastification'
import { mapActions } from 'vuex'

export default {
  name: 'OverviewPage',
  data () {
    return {
      recentActivities: [
        { description: 'User John Doe signed up', time: '2 hours ago' },
        { description: 'New report generated', time: '5 hours ago' },
        { description: 'System maintenance completed', time: '1 day ago' },
        { description: 'User Jane Smith upgraded account', time: '2 days ago' }
      ]
    }
  },
  methods: {
    ...mapActions(['logout']),
    async handleLogout () {
      const toast = useToast()
      await this.logout()
      toast.info('Logged out successfully')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
/* Styling for the sidebar and other elements */
</style>
