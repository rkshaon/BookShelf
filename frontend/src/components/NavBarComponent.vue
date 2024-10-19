<template>
    <nav class="bg-gray-800 text-white">
        <div class="container mx-auto px-2 sm:px-6 lg:px-8">
            <div class="relative flex items-center justify-between h-16">
                <!-- Logo -->
                <div class="flex-shrink-0">
                    <router-link to="/" class="text-xl font-bold text-white">BookShelf</router-link>
                </div>
                <!-- Search Box -->
                <div class="flex-grow flex justify-end">
                    <div class="relative w-full max-w-md">
                        <input type="text"
                            class="w-full px-4 py-2 pl-10 rounded-md bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:bg-gray-600 focus:ring-2 focus:ring-blue-500"
                            placeholder="Search books, authors, genres..." />
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M21 21l-4.35-4.35m1.42-4.61A7.5 7.5 0 1115.3 15.3z" />
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
  name: 'NavBarComponent'
}
</script>

<style scoped>
/* Add any additional styling here */
</style>
