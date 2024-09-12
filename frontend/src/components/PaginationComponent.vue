<template>
    <div class="flex justify-between mt-8 mb-8">
        <!-- Previous button -->
        <div v-if="previousPage" class="flex-1">
            <button @click="goToPage(previousPage)" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
                Previous
            </button>
        </div>
        <!-- Spacer to balance layout -->
        <div class="flex-1"></div>
        <!-- Next button -->
        <div v-if="nextPage" class="flex-1 text-right">
            <button @click="goToPage(nextPage)" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
                Next
            </button>
        </div>
    </div>
</template>

<script>
export default {
  name: 'PaginationComponent',
  props: {
    previousPage: {
      type: String,
      default: null
    },
    nextPage: {
      type: String,
      default: null
    }
  },
  methods: {
    goToPage (url) {
      this.$emit('fetch-page', url) // Emit an event to the parent component
    }
  }
}
</script>

<style scoped>
/* Custom styles for pagination can be added here */
</style>
