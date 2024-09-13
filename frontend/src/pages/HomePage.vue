<template>
  <main class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <div class="bg-white shadow rounded-lg p-6 mb-8">
      <h1 class="text-2xl font-bold text-gray-800 mb-4">Welcome to BookShelf</h1>
      <p class="text-gray-600">
        Explore a vast collection of books, share your reviews, and connect with other book lovers.
      </p>
    </div>

    <!-- PaginationComponent for navigation -->
    <PaginationComponent :previousPage="previousPageUrl" :nextPage="nextPageUrl" :pageSize="pageSize"
      @fetch-page="changePage" />

    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      <BookCardComponent v-for="(book, index) in books" :key="index" :book="book" />
    </div>

    <!-- PaginationComponent at the bottom -->
    <PaginationComponent :previousPage="previousPageUrl" :nextPage="nextPageUrl" :pageSize="pageSize"
      @fetch-page="changePage" />
  </main>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import BookCardComponent from '@/components/BookCardComponent.vue'
import PaginationComponent from '@/components/PaginationComponent.vue'

export default {
  name: 'HomePage',
  components: {
    BookCardComponent,
    PaginationComponent
  },
  computed: {
    ...mapGetters(['allBooks', 'nextPageUrl', 'previousPageUrl', 'currentPageSize']),
    books () {
      return this.allBooks
    },
    pageSize () {
      return this.currentPageSize
    }
  },
  watch: {
    '$route.query.page': {
      immediate: true,
      handler (newPage) {
        const page = newPage || 1
        this.fetchBooks({ page, pageSize: this.pageSize })
      }
    }
  },
  mounted () {
    // this.fetchBooks()
    const currentPage = this.$route.query.page || 1
    if (!this.$route.query.page) {
      this.fetchBooks({ page: currentPage, pageSize: this.pageSize })
    }
  },
  methods: {
    ...mapActions(['fetchBooks']),
    changePage (page) {
      this.$router.push({ query: { page } })
      // this.fetchBooks({ page, pageSize: this.pageSize })
    }
  }
}
</script>

<style scoped>
/* Custom styles for HomePage.vue */
</style>
