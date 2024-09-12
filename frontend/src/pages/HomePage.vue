<template>
  <main class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <div class="bg-white shadow rounded-lg p-6 mb-8">
      <h1 class="text-2xl font-bold text-gray-800 mb-4">Welcome to BookShelf</h1>
      <p class="text-gray-600">
        Explore a vast collection of books, share your reviews, and connect with other book lovers.
      </p>
    </div>
    <div class="flex justify-between mt-8 mb-8">
      <div v-if="previousPage" class="flex-1">
        <button @click="fetchBooks(previousPage)" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Previous
        </button>
      </div>
      <div class="flex-1"></div>
      <div v-if="nextPage" class="flex-1 text-right">
        <button @click="fetchBooks(nextPage)" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Next
        </button>
      </div>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      <BookCardComponent v-for="(book, index) in books" :key="index" :book="book" />
    </div>
    <div class="flex justify-between mt-8">
      <div v-if="previousPage" class="flex-1">
        <button @click="fetchBooks(previousPage)" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Previous
        </button>
      </div>
      <div class="flex-1"></div>
      <div v-if="nextPage" class="flex-1 text-right">
        <button @click="fetchBooks(nextPage)" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Next
        </button>
      </div>
    </div>
  </main>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import BookCardComponent from '@/components/BookCardComponent.vue'

export default {
  name: 'HomePage',
  components: {
    BookCardComponent
  },
  computed: {
    ...mapGetters(['allBooks', 'nextPage', 'previousPage']),
    books () {
      return this.allBooks
    }
  },
  mounted () {
    this.fetchBooks()
  },
  methods: {
    ...mapActions(['fetchBooks'])
  }
}
</script>

<style scoped>
/* Additional custom styles can go here if needed */
</style>
