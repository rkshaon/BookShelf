<template>
    <div class="flex flex-col min-h-screen">
        <!-- Header or Navbar Component -->
        <!-- <HeaderComponent /> -->

        <!-- Main Content -->
        <main class="flex-grow">
            <router-view />
        </main>

        <!-- Footer -->
        <footer class="bg-gray-800 text-white text-center py-4 sticky bottom-0">
            <div class="container mx-auto px-4">
                <p>&copy; 2024 BookShelf. All rights reserved.</p>
                <div class="flex justify-center space-x-4 mt-2">
                    <a href="#" class="text-gray-400 hover:text-white">Privacy Policy</a>
                    <a href="#" class="text-gray-400 hover:text-white">Terms of Service</a>
                    <a href="#" class="text-gray-400 hover:text-white">Contact Us</a>
                </div>
            </div>
        </footer>
    </div>
</template>

<script>

export default {
  components: {
  }
}
</script>

<style scoped>
/* Additional styles if needed */
</style>
