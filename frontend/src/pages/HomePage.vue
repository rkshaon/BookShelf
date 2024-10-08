<template>
  <main class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <div class="bg-white shadow rounded-lg p-6 mb-8">
      <h1 class="text-2xl font-bold text-gray-800 mb-4">Welcome to BookShelf</h1>
      <p class="text-gray-600">
        Explore a vast collection of books, share your reviews, and connect with other book lovers.
      </p>
    </div>
    <PaginationComponent :previousPage="previousPageUrl" :nextPage="nextPageUrl" :pageSize="pageSize"
      @fetch-page="changePage" />
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      <BookCardComponent v-for="(book, index) in books" :key="index" :book="book" />
    </div>
    <div v-if="isLoading">
      <LoaderComponent />
    </div>
    <PaginationComponent :previousPage="previousPageUrl" :nextPage="nextPageUrl" :pageSize="pageSize"
      @fetch-page="changePage" />
  </main>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import BookCardComponent from '@/components/BookCardComponent.vue'
import PaginationComponent from '@/components/PaginationComponent.vue'
import LoaderComponent from '@/components/LoaderComponent.vue'

export default {
  name: 'HomePage',
  metaInfo: {
    title: 'Welcome to BookShelf - Your Online Library',
    meta: [
      {
        name: 'description',
        content: 'Explore a vast collection of books and connect with other book lovers at BookShelf.'
      },
      {
        name: 'keywords',
        content: 'online library, books, book lovers, authors, reading'
      },
      {
        property: 'og:title',
        content: 'BookShelf - Explore a Vast Collection of Books'
      },
      {
        property: 'og:description',
        content: 'Discover new books and connect with fellow readers at BookShelf.'
      },
      {
        property: 'og:type',
        content: 'website'
      }
    ]
  },
  components: {
    BookCardComponent,
    PaginationComponent,
    LoaderComponent
  },
  data () {
    return {
      isLoading: false
    }
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
        let page = parseInt(newPage, 10)

        if (!page || isNaN(page)) {
          this.$router.replace({ query: { page: 1 } })
          page = 1
          return
        }

        this.fetchBooks({ page, pageSize: this.pageSize })
      }
    }
  },
  mounted () {
    const currentPage = this.$route.query.page

    if (!currentPage || isNaN(currentPage)) {
      this.$router.replace({ query: { page: 1 } })
    }

    document.title = 'Book Shelf'
  },
  methods: {
    ...mapActions(['fetchBooks']),
    async fetchBooks (payload) {
      this.isLoading = true
      this.$store.commit('SET_BOOKS', [])
      try {
        await this.$store.dispatch('fetchBooks', payload)
      } catch (error) {
        console.error('Error fetching books:', error)
      } finally {
        this.isLoading = false
      }
    },
    changePage (page) {
      this.$router.push({ query: { page } })
    }
  }
}
</script>

<style scoped>
/* Custom styles for HomePage.vue */
</style>
