<template>
  <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <div v-if="isGenreLoading" class="flex justify-center">
      <LoaderComponent />
    </div>
    <div v-else-if="genre">
      <div class="bg-white shadow rounded-lg p-6 mb-8">
        <h1 class="text-4xl font-bold text-center text-gray-800 mb-4">
          {{ genre.name }}
        </h1>
        <p class="text-lg text-center text-gray-600 mb-8 max-w-3xl mx-auto">
          {{ genre.description || 'No description available for this genre.' }}
        </p>
      </div>
      <h2 class="text-2xl font-semibold text-gray-800 mb-6">
        Books on {{ genre.name }}
      </h2>
      <div v-if="isBookLoading" class="flex justify-center">
        <LoaderComponent />
      </div>
      <div v-else>
        <PaginationComponent :previousPage="previousPageUrl" :nextPage="nextPageUrl" :pageSize="pageSize"
          @fetch-page="changePage" />
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          <BookCardComponent v-for="(book, index) in books" :key="index" :book="book" />
        </div>
      </div>
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
import PaginationComponent from '@/components/PaginationComponent.vue'
import BookCardComponent from '@/components/BookCardComponent.vue'
import NotFoundComponent from '@/components/NotFoundComponent.vue'

export default {
  name: 'GenrePage',
  components: {
    LoaderComponent,
    NotFoundComponent,
    PaginationComponent,
    BookCardComponent
  },
  data () {
    return {
      isBookLoading: false
    }
  },
  computed: {
    ...mapGetters({
      genre: 'getGenreDetails',
      isGenreLoading: 'isGenreLoading',
      error: 'genreDetailsError',
      allBooks: 'allBooks',
      nextPageUrl: 'nextPageUrl',
      previousPageUrl: 'previousPageUrl',
      currentPageSize: 'currentPageSize'
    }),
    books () {
      return this.allBooks
    },
    pageSize () {
      return this.currentPageSize
    }
  },
  watch: {
    genre (newGenre) {
      if (newGenre && newGenre.name) {
        document.title = `Book Shelf | ${newGenre.name}`
        console.log('new genre', newGenre)
        console.log('new genre id', newGenre.id)
      }
    },
    '$route.query.page': {
      immediate: true,
      handler (newPage) {
        let page = parseInt(newPage, 10)

        if (!page || isNaN(page)) {
          this.$router.replace({ query: { page: 1 } })
          page = 1
          return
        }

        this.fetchBooks({ page, pageSize: this.pageSize, genre: this.genre.id })
      }
    }
  },
  mounted () {
    const genreId = this.$route.params.id
    const currentPage = this.$route.query.page

    if (!currentPage || isNaN(currentPage)) {
      this.$router.replace({ query: { page: 1 } })
    }

    console.log('Genre ID', genreId)
    this.fetchGenreDetails(genreId)
    document.title = 'Book Shelf | Loading ...'
  },
  methods: {
    ...mapActions(['fetchGenreDetails', 'fetchBooks']),
    async fetchBooks (payload) {
      console.log('PayLoad...', payload)
      this.isBookLoading = true
      this.$store.commit('SET_BOOKS', [])
      try {
        console.log('PayLoad...', payload)
        await this.$store.dispatch('fetchBooks', payload)
      } catch (error) {
        console.error('Error fetching books:', error)
      } finally {
        this.isBookLoading = false
      }
    },
    changePage (page) {
      this.$router.push({ query: { page } })
    }
  }
}
</script>

<style scoped>
/* Additional styles if needed */
</style>
