<template>
  <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <div v-if="isLoading" class="flex justify-center">
      <LoaderComponent />
    </div>
    <div v-else-if="author">
      <div class="bg-white shadow-lg rounded-lg p-6 grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="flex justify-center">
          <!-- Image Field will appear here -->
        </div>
        <div>
          <h1 class="text-3xl font-bold text-gray-800 mb-4">{{ author.full_name }}</h1>
          <p class="text-gray-600 mb-4"><strong>Biography:</strong> {{ author.biography || 'N/A' }}</p>
          <p class="text-gray-600 mb-4">
            <strong>Status:</strong>
            <span v-if="author.is_alive">Alive</span>
            <span v-else>Deceased
              ({{ author.died_date }})
            </span>
          </p>
          <p class="text-gray-600 mb-4">
            <strong>Born:</strong> {{ author.birth_date || 'Unknown' }}
          </p>
        </div>
      </div>
      <div v-if="author.books.length > 0" class="mt-6">
        <h3 class="text-xl font-semibold text-gray-700 mb-4">Bibliography</h3>
        <ul class="list-disc list-inside text-gray-600">
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <BookCardComponent v-for="(book, index) in author.books" :key="index" :book="book" />
          </div>
        </ul>
      </div>
    </div>
    <div v-else-if="error" class="text-red-500">
      <NotFoundComponent contentType="Author" :errorMessage="error" />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import LoaderComponent from '@/components/LoaderComponent.vue'
import BookCardComponent from '@/components/BookCardComponent.vue'
import NotFoundComponent from '@/components/NotFoundComponent.vue'

export default {
  name: 'AuthorPage',
  components: {
    LoaderComponent,
    BookCardComponent,
    NotFoundComponent
  },
  computed: {
    ...mapGetters({
      author: 'getAuthorDetails',
      isLoading: 'isAuthorLoading',
      error: 'authorDetailsError'
    })
  },
  watch: {
    '$route.params.id': {
      immediate: true,
      handler (newAuthorId) {
        this.fetchAuthorDetails(newAuthorId)
      }
    },
    author (newAuthor) {
      if (newAuthor && newAuthor.full_name) {
        document.title = `Book Shelf | ${newAuthor.full_name}`
      }
    }
  },
  mounted () {
    const authorId = this.$route.params.id
    this.fetchAuthorDetails(authorId)
    document.title = 'Book Shelf | Loading ...'
  },
  methods: {
    ...mapActions(['fetchAuthorDetails'])
  }
}
</script>

<style scoped>
/* Custom styles for AuthorDetailsPage.vue */
</style>
