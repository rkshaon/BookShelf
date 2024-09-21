<template>
    <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <div v-if="isTopicLoading" class="flex justify-center">
                <LoaderComponent />
            </div>
            <div v-else-if="topic">
                <div class="bg-white shadow rounded-lg p-6 mb-8">
                    <h1 class="text-4xl font-bold text-center text-gray-800 mb-4">
                        #{{ topic.slug }}
                    </h1>
                </div>
                <h2 class="text-2xl font-semibold text-gray-800 mb-6">
                    Books on #{{ topic.slug }}
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
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import LoaderComponent from '@/components/LoaderComponent.vue'
import PaginationComponent from '@/components/PaginationComponent.vue'
import BookCardComponent from '@/components/BookCardComponent.vue'
import NotFoundComponent from '@/components/NotFoundComponent.vue'

export default {
  name: 'TopicPage',
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
      topic: 'getTopicDetails',
      isTopicLoading: 'isTopicLoading',
      error: 'topicDetailsError',
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
    topic (newTopic) {
      if (newTopic && newTopic.name) {
        document.title = `Book Shelf | ${newTopic.name}`
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

        this.fetchBooks({ page, pageSize: this.pageSize, topic: this.$route.params.id })
      }
    }
  },
  mounted () {
    const topicId = this.$route.params.id
    const currentPage = this.$route.query.page

    if (!currentPage || isNaN(currentPage)) {
      this.$router.replace({ query: { page: 1 } })
    }

    this.fetchTopicDetails(topicId)
    document.title = 'Book Shelf | Loading ...'
  },
  methods: {
    ...mapActions(['fetchTopicDetails', 'fetchBooks']),
    async fetchBooks (payload) {
      console.log(payload)
      this.isBookLoading = true
      this.$store.commit('SET_BOOKS', [])
      try {
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
