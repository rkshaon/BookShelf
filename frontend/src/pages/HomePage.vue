<template>
    <main class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <div class="bg-white shadow rounded-lg p-6 mb-8">
            <h1 class="text-2xl font-bold text-gray-800 mb-4">Welcome to BookShelf</h1>
            <p class="text-gray-600">
                Explore a vast collection of books, share your reviews, and connect with other book lovers.
            </p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <BookCardComponent v-for="(book, index) in books" :key="index" :book="book" />
        </div>
    </main>
</template>

<script>
import BookCardComponent from '@/components/BookCardComponent.vue'

export default {
  name: 'HomePage',
  components: {
    BookCardComponent
  },
  data () {
    return {
      books: [
        {
          coverImage: null, // Placeholder for no image
          title: 'Test Book',
          author: 'Myself'
        },
        {
          coverImage: 'https://example.com/book2.jpg',
          title: 'Book Two',
          author: 'Author Two'
        },
        {
          coverImage: 'https://example.com/book3.jpg',
          title: 'Book Three',
          author: 'Author Three'
        },
        {
          coverImage: null, // Placeholder for no image
          title: 'Test Book',
          author: 'Myself'
        },
        {
          coverImage: 'https://example.com/book2.jpg',
          title: 'Book Two',
          author: 'Author Two'
        },
        {
          coverImage: 'https://example.com/book3.jpg',
          title: 'Book Three',
          author: 'Author Three'
        }
      ]
    }
  }
}
</script>

<style scoped>
/* Additional custom styles can go here if needed */
</style>
