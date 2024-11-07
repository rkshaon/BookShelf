<!-- src/layouts/DashboardLayout.vue -->
<template>
    <div class="flex min-h-screen bg-gray-100">
        <SideBarComponent />
        <div class="flex-1 p-6">
            <router-view />
        </div>
    </div>
</template>

<script>
import SideBarComponent from '@/components/dashboard/SideBarComponent.vue'

export default {
  components: {
    SideBarComponent
  }
}
</script>

<style scoped>
/* Any layout-specific styles */
</style>
