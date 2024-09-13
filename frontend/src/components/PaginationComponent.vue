<template>
  <div class="flex justify-between mt-8 mb-8">
    <!-- Previous button -->
    <div v-if="previousPage" class="flex-1">
      <button @click="changePage(previousPage)" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
        Previous
      </button>
    </div>
    <!-- Spacer to balance layout -->
    <div class="flex-1"></div>
    <!-- Next button -->
    <div v-if="nextPage" class="flex-1 text-right">
      <button @click="changePage(nextPage)" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
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
    },
    pageSize: {
      type: Number,
      default: 8
    }
  },
  methods: {
    changePage (url) {
      if (url) {
        const urlParams = new URL(url)
        const newPage = urlParams.searchParams.get('page')
        this.$emit('fetch-page', newPage)
      }
    }
  }
}
</script>

<style scoped>
/* Custom styles for PaginationComponent.vue */
</style>
