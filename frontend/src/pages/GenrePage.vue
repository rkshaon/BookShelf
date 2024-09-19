<template>
  <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <div v-if="isLoading" class="flex justify-center">
      <LoaderComponent />
    </div>
    <div v-else-if="genre">
      <h1 class="text-4xl font-bold text-center text-gray-800 mb-4">
        {{ genre.name }}
      </h1>
      <p class="text-lg text-center text-gray-600 mb-8 max-w-3xl mx-auto">
        {{ genre.description || 'No description available for this genre.' }}
      </p>
      <h2 class="text-2xl font-semibold text-gray-800 mb-6">
        Books on {{ genre.name }}
      </h2>
    </div>
    <div v-else-if="error" class="text-red-500">
      <NotFoundComponent contentType="Genre" :errorMessage="error" />
    </div>
    <!-- <h2 class="text-2xl font-semibold text-gray-800 mb-6">Books in {{ genre.name }}</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div v-for="book in genre.books" :key="book.id" class="bg-white shadow-lg rounded-lg overflow-hidden">
                <router-link :to="{ name: 'BookDetails', params: { book_code: book.book_code } }">
                    <img :src="getCoverImage(book.cover_image, API_BASE_URL)" alt="Book Cover"
                        class="w-full h-48 object-cover">
                </router-link>
                <div class="p-4">
                    <router-link :to="{ name: 'BookDetails', params: { book_code: book.book_code } }">
                        <h3 class="text-lg font-bold text-gray-800">{{ book.title }}</h3>
                    </router-link>
                    <p class="text-gray-600">{{ book.authors.map(author => author.full_name).join(', ') }}</p>
                    <p v-if="book.published_year" class="text-gray-400">
                        <strong>Published:</strong> {{ book.published_year }}
                    </p>
                </div>
            </div>
        </div> -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import LoaderComponent from '@/components/LoaderComponent.vue'
// import BookCardComponent from '@/components/BookCardComponent.vue'
import NotFoundComponent from '@/components/NotFoundComponent.vue'

export default {
  name: 'GenrePage',
  components: {
    LoaderComponent,
    NotFoundComponent
  },
  computed: {
    ...mapGetters({
      genre: 'getGenreDetails',
      isLoading: 'isGenreLoading',
      error: 'genreDetailsError'
    })
  },
  watch: {
    genre (newGenre) {
      if (newGenre && newGenre.name) {
        document.title = `Book Shelf | ${newGenre.name}`
      }
    }
  },
  mounted () {
    const genreId = this.$route.params.id
    console.log('Genre ID', genreId)
    this.fetchGenreDetails(genreId)
    document.title = 'Book Shelf | Loading ...'
  },
  methods: {
    ...mapActions(['fetchGenreDetails'])
  }
}
</script>

<style scoped>
/* Additional styles if needed */
</style>
