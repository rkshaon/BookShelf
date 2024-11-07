<!-- src/layouts/DashboardLayout.vue -->
<template>
    <div class="flex min-h-screen bg-gray-100">
        <!-- Sidebar Component -->
        <SideBarComponent />

        <!-- Main Content Area for Dashboard Pages -->
        <div class="flex-1 p-6">
            <!-- Render the matched route's component here -->
            <router-view />
        </div>
    </div>
</template>

<script>
import SideBarComponent from '@/components/user/SideBarComponent.vue'

export default {
  components: {
    SideBarComponent
  }
}
</script>

<style scoped>
/* Any layout-specific styles */
</style>
