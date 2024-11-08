<template>
  <div class="book-list-page p-6 bg-gray-50 min-h-screen">
    <div class="flex justify-end mb-4">
      <button class="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600 transition">
        Add Author
      </button>
    </div>
    <div class="overflow-x-auto bg-white shadow-md rounded-lg">
      <table class="table-auto w-full border-collapse">
        <thead class="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
          <tr>
            <th class="py-3 px-6 text-left">Name</th>
            <th class="py-3 px-6 text-left">Biography</th>
            <th class="py-3 px-6 text-center">Action</th>
          </tr>
        </thead>
        <tbody class="text-gray-700 text-sm">
          <tr v-for="author in authors" :key="author.id" class="border-b hover:bg-gray-100">
            <td class="py-3 px-6">
              <router-link :to="{ name: 'AuthorDetails', params: { id: author.id } }"
                class="px-4 py-2 bg-blue-100 text-blue-600 font-semibold rounded-md hover:bg-blue-200 hover:text-blue-700 transition">
                {{ author.full_name }}
              </router-link>
            </td>
            <td class="py-3 px-6">{{ author.biography }}</td>
            <td class="py-3 px-6 text-center space-x-2">
              <button class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition">
                Edit
              </button>
              <button class="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600 transition">
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="mt-6">
      <DashboardPaginationComponent :previousPage="previousPageUrl" :nextPage="nextPageUrl" :pageSize="pageSize"
        :currentPage="parseInt(currentPage, 10)" :totalCount="totalAuthorCount" @fetch-page="changePage" />
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import DashboardPaginationComponent from '@/components/dashboard/DashboardPaginationComponent .vue'

export default {
  name: 'AuthorListPage',
  components: {
    DashboardPaginationComponent
  },
  data () {
    return {
      isLoading: false,
      currentPage: 0
    }
  },
  computed: {
    ...mapGetters([
      'authors', 'nextPageUrl', 'previousPageUrl', 'totalAuthorCount', 'currentPageSize'
    ]),
    pageSize () {
      return this.currentPageSize
    }
  },
  watch: {
    '$route.query.page': {
      immediate: true,
      handler (newPage) {
        let page = parseInt(newPage, 10)
        this.currentPage = Number(page)

        if (!page || isNaN(page)) {
          this.$router.replace({ query: { page: 1 } })
          page = 1
          return
        }

        this.fetchAuthors({ page, pageSize: this.pageSize })
      }
    }
  },
  mounted () {
    const currentPage = this.$route.query.page
    this.currentPage = currentPage

    if (!currentPage || isNaN(currentPage)) {
      this.$router.replace({ query: { page: 1 } })
    }

    document.title = 'Book Shelf'
  },
  methods: {
    ...mapActions(['fetchAuthors']),
    addAuthor () {
      alert('Add Author Coming Soon...')
    },
    async fetchAuthors (payload) {
      this.isLoading = true
      this.$store.commit('SET_AUTHORS', [])
      try {
        await this.$store.dispatch('fetchAuthors', payload)
      } catch (error) {
        console.error('Error fetching authors:', error)
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
</style>
