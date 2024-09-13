<template>
    <div class="flex flex-col items-center justify-center">
        <div class="text-center">
            <h1 class="text-4xl font-bold text-red-500 mb-4">Sorry!</h1>
            <h1 class="text-4xl font-bold text-green-500 mb-4">{{ contentType }}</h1>
            <p class="text-gray-600 mb-6">{{ errorMessage }}</p>
            <router-link to="/"
                class="bg-blue-500 text-white px-6 py-2 rounded hover:bg-blue-600 transition duration-200">
                Go Back to Home
            </router-link>
        </div>
    </div>
</template>

<script>
export default {
  name: 'NotFoundComponent',
  props: {
    contentType: {
      type: String,
      default: 'The Content'
    },
    errorMessage: {
      type: String,
      default: 'Our System Does Not Have What You Are Looking For.'
    }
  }
}
</script>

<style scoped>
/* Additional styling (optional) */
</style>
