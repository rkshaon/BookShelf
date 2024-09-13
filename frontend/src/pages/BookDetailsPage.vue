<template>
  <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <LoaderComponent v-if="isLoading" />
    <div v-else-if="bookDetails" class="bg-white shadow rounded-lg p-6">
      <h1 class="text-3xl font-bold text-gray-800 mb-4">{{ bookDetails.title }}</h1>
      <p class="text-gray-600 mb-2">{{ bookDetails.authors.map(author => author.full_name).join(', ') }}</p>
      <img :src="getCoverImage(bookDetails.cover_image, API_BASE_URL)" alt="Book Cover"
        class="w-full h-64 object-cover mb-4" />
      <p class="text-gray-600">{{ bookDetails.description }}</p>
    </div>
    <div v-else-if="error" class="text-red-500">
      <!-- <p>{{ error }}</p> -->
      <NotFoundComponent contentType="Book" />
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
  mounted () {
    const bookCode = this.$route.params.book_code
    this.fetchBookDetails(bookCode)
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
