<template>
  <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <LoaderComponent v-if="isLoading" />
    <div v-else-if="bookDetails" class="bg-white shadow rounded-lg p-6 grid grid-cols-1 md:grid-cols-2 gap-8">
      <div class="flex justify-center">
        <img :src="getCoverImage(bookDetails.cover_image, API_BASE_URL)" alt="Book Cover"
          class="max-w-full h-auto shadow-lg rounded-lg" />
      </div>
      <div>
        <router-link :to="{
          name: 'Book',
          params: { book_code: bookDetails.book_code },
          state: { bookURL: bookDetails.book }
        }"
          class="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300">
          Read
        </router-link>
        <h1 class="text-3xl font-bold text-gray-800 mb-4 mt-4">{{ bookDetails.title }}</h1>
        <p class="text-gray-600 mb-4">
          <strong>Authors:</strong> {{ bookDetails.authors.map(author => author.full_name).join(', ') }}
        </p>
        <p class="text-gray-600 mb-4">{{ bookDetails.description }}</p>
        <div class="grid grid-cols-1 gap-4">
          <div v-if="bookDetails.publisher">
            <strong>Publisher:</strong> {{ bookDetails.publisher.name }}
          </div>
          <div v-if="bookDetails.edition">
            <strong>Edition:</strong> {{ bookDetails.edition }}
          </div>
          <div v-if="bookDetails.isbn">
            <strong>ISBN:</strong> {{ bookDetails.isbn }}
          </div>
          <div v-if="bookDetails.pages">
            <strong>Pages:</strong> {{ bookDetails.pages }}
          </div>
          <div v-if="bookDetails.language">
            <strong>Language:</strong> {{ bookDetails.language }}
          </div>
          <div v-if="bookDetails.published_date">
            <strong>Published Date:</strong> {{ new Date(bookDetails.published_date).toLocaleDateString() }}
          </div>
        </div>
      </div>
    </div>
    <div v-else-if="error" class="text-red-500">
      <NotFoundComponent contentType="Book" :errorMessage="error" />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { getCoverImage } from '@/helpers/getCoverImage'

import LoaderComponent from '@/components/LoaderComponent.vue'
import NotFoundComponent from '@/components/NotFoundComponent.vue'

export default {
  name: 'BookDetailsPage',
  components: {
    LoaderComponent,
    NotFoundComponent
  },
  computed: {
    ...mapGetters({
      bookDetails: 'getBookDetails',
      isLoading: 'isBookLoading',
      error: 'bookDetailsError'
    }),
    API_BASE_URL () {
      return process.env.VUE_APP_BACKEND_URL
    }
  },
  watch: {
    bookDetails (newBookDetails) {
      if (newBookDetails && newBookDetails.title) {
        document.title = `Book Shelf | ${newBookDetails.title}`
      }
    }
  },
  mounted () {
    const bookCode = this.$route.params.book_code
    this.fetchBookDetails(bookCode)
    document.title = 'Book Shelf | Loading ...'
  },
  methods: {
    ...mapActions(['fetchBookDetails']),
    getCoverImage
  }
}
</script>

<style scoped>
/* Custom styles for BookDetailsPage.vue */
</style>
