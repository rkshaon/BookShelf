<template>
    <div class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
        <h1 class="text-9xl font-bold text-red-500">404</h1>
        <p class="text-xl text-gray-700 mt-4">Oops! The page you're looking for doesn't exist.</p>
        <router-link to="/"
            class="mt-6 text-lg bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition duration-300">
            Go back to Home
        </router-link>
    </div>
</template>

<script>
export default {
  name: 'NotFoundPage',
  mounted () {
    document.title = 'Book Shelf | Page Not Found'
  }
}
</script>

<!-- Tailwind CSS styles applied through class attributes -->
