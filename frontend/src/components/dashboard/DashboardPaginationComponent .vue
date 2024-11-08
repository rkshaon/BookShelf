<template>
  <div class="flex justify-between items-center mt-8 mb-8">
    <div class="flex-1">
      <button v-if="previousPage" @click="changePage(previousPage)" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
        Previous
      </button>
    </div>
    <div class="flex-1 text-center">Page {{ currentPage }} of {{ totalPages }}</div>
    <div class="flex-1 text-right">
      <button v-if="nextPage" @click="changePage(nextPage)" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
        Next
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DashboardPaginationComponent',
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
    },
    currentPage: {
      type: Number,
      default: 1
    },
    totalPages: {
      type: Number,
      default: 0
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
