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
  // watch: {
  //   '$route.query.page': {
  //     immediate: true,
  //     handler (newPage) {
  //       // const page = newPage || 1
  //       let page = newPage
  //       // let page = parseInt(newPage, 10)

  //       if (!page || isNaN(page)) {
  //         console.log('page number: ', page)
  //         this.$router.replace({ query: { page: 1 } })
  //         page = 1
  //       }

  //       this.fetchBooks({ page, pageSize: this.pageSize })
  //     }
  //   }
  // },
  watch: {
    '$route.query.page': {
      immediate: true,
      handler (newPage) {
        // If the 'newPage' is undefined, null, or not a number, set it to 1
        let page = parseInt(newPage, 10)

        if (!page || isNaN(page)) {
          console.log('Invalid or missing page number:', page)
          this.$router.replace({ query: { page: 1 } })
          page = 1
        }

        // Fetch the correct page data
        this.fetchBooks({ page, pageSize: this.pageSize })
      }
    }
  },
  // mounted () {
  //   // const currentPage = this.$route.query.page || 1
  //   // if (!this.$route.query.page) {
  //   //   this.fetchBooks({ page: currentPage, pageSize: this.pageSize })
  //   // }
  //   // When the component is mounted, ensure there's always a valid 'page' parameter
  //   const currentPage = this.$route.query.page

  //   // If no page query is present, redirect to page 1
  //   if (!currentPage || isNaN(currentPage)) {
  //     this.$router.replace({ query: { page: 1 } })
  //   }
  //   // else {
  //   //   // Otherwise, fetch the books for the existing page
  //   //   console.log('Current Page: ', currentPage)

  //   //   // this.fetchBooks({ page: currentPage, pageSize: this.pageSize })
  //   // }
  // },
  mounted () {
    // When the component is mounted, check if there's no 'page' query
    const currentPage = this.$route.query.page

    // If there's no page parameter, set it to 1 and let the watcher handle the API call
    if (!currentPage || isNaN(currentPage)) {
      this.$router.replace({ query: { page: 1 } })
    }
    // DO NOT call fetchBooks here because the watcher will handle it
  },
  methods: {
    ...mapActions(['fetchBooks']),

    // This method updates the URL query when the next or previous button is clicked
    changePage (page) {
      this.$router.push({ query: { page } })
      // No need to call fetchBooks here, the watcher will handle it
    }
  }
  // methods: {
  //   ...mapActions(['fetchBooks']),
  //   changePage (page) {
  //     this.$router.push({ query: { page } })
  //   }
  // }
}
</script>

<style scoped>
/* Custom styles for HomePage.vue */
</style>
