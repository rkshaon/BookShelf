<template>
  <div class="book-list-page">
    <button class="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600" @click="addAuthor">Add Author</button>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Biography</th>
          <!-- <th>Total Books</th> -->
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="author in authors" :key="author.id">
          <td>
            <router-link :to="{ name: 'AuthorDetails', params: { id: author.id } }"
              class="px-4 py-2 bg-blue-100 text-blue-600 font-semibold rounded-md hover:bg-blue-200 hover:text-blue-700 transition">
              {{ author.full_name }}
            </router-link>
          </td>
          <td>{{ author.biography }}</td>
          <!-- <td>Coming Soon</td> -->
          <td>
            <button class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">Edit</button>
            <button class="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- <div class="pagination">
      <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
    </div> -->
    <DashboardPaginationComponent :previousPage="previousPageUrl" :nextPage="nextPageUrl" :pageSize="pageSize"
      @fetch-page="changePage" />
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
      isLoading: false
    }
  },
  computed: {
    ...mapGetters([
      'authors', 'nextPageUrl', 'previousPageUrl', 'totalAuthorCount'
    ]),
    totalPages () {
      return Math.ceil(this.totalAuthorCount / this.pageSize)
    },
    // paginatedAuthors () {
    //   const start = (this.currentPage - 1) * this.pageSize
    //   const end = start + this.pageSize
    //   return this.authors.slice(start, end)
    // }
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

        this.fetchAuthors({ page, pageSize: this.pageSize })
      }
    }
  },
  mounted () {
    // this.fetchAuthors()
    const currentPage = this.$route.query.page

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
    // prevPage () {
    //   if (this.currentPage > 1) {
    //     this.currentPage--
    //   }
    // },
    // nextPage () {
    //   if (this.currentPage < this.totalPages) {
    //     this.currentPage++
    //   }
    // }
  }
}
</script>

<style scoped>
.book-list-page {
    padding: 20px;
}

button {
    margin-bottom: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th,
td {
    border: 1px solid #ddd;
    padding: 8px;
}

th {
    background-color: #f2f2f2;
}

.pagination {
    margin-top: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.pagination button {
    margin: 0 10px;
}
</style>
