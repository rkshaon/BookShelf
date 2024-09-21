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
        <div class="text-gray-600 mb-4">
          <strong>Authors:</strong>
          <div class="flex flex-wrap gap-2 mt-2">
            <router-link v-for="author in bookDetails.authors" :key="author.id"
              :to="{ name: 'AuthorDetails', params: { id: author.id } }"
              class="px-4 py-2 bg-blue-100 text-blue-600 font-semibold rounded-md hover:bg-blue-200 hover:text-blue-700 transition">
              {{ author.full_name }}
            </router-link>
          </div>
        </div>
        <p v-if="bookDetails.genres && bookDetails.genres.length > 0" class="text-gray-600 mb-4 flex items-center">
          <strong class="mr-2">Genre:</strong>
          <span class="flex flex-wrap gap-2">
            <router-link v-for="genre in bookDetails.genres" :key="genre.id"
              :to="{ name: 'GenreDetails', params: { id: genre.id, slug: genre.slug } }"
              class="inline-block px-2 py-1 bg-green-100 text-green-700 rounded-md text-sm hover:bg-green-200 transition">
              {{ genre.name }}
            </router-link>
          </span>
        </p>
        <p v-if="bookDetails.topics && bookDetails.topics.length > 0" class="text-gray-600 mb-4">
          <span class="flex flex-wrap gap-2">
            <router-link v-for="topic in bookDetails.topics" :key="topic.id"
              :to="{ name: 'TopicDetails', params: { id: topic.id, slug: topic.name } }"
              class="inline-block px-2 py-1 bg-yellow-100 text-yellow-700 rounded-md text-sm hover:bg-green-200 transition">
              #{{ topic.name }}
            </router-link>
          </span>
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
          <div v-if="bookDetails.published_year">
            <strong>Published Year:</strong> {{ bookDetails.published_year }}
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
