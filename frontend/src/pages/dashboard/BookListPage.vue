<template>
  <div class="book-list-page p-6 bg-gray-50 min-h-screen">
    <AddBookModal :visible="showBookAddModal" :book="book" :isAPISuccess="isAPISuccess" title="Add Book"
      @close="showBookAddModal = false" @confirm="handleConfirm" />
    <EditBookModal :visible="showBookEditModal" :book="editBook" :isAPISuccess="isAPISuccess" title="Edit Book"
      @close="showBookEditModal = false" @confirm="handleConfirm" />
    <div class="flex justify-end mb-4">
      <button @click="showBookAddModal = true"
        class="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600 transition">
        Add Book
      </button>
    </div>
    <div class="mt-6">
      <DashboardPaginationComponent :previousPage="previousPageUrl" :nextPage="nextPageUrl" :pageSize="10"
        :currentPage="parseInt(currentPage, 10)" :totalCount="totalBookCount" @fetch-page="changePage" />
    </div>
    <div class="overflow-x-auto bg-white shadow-md rounded-lg">
      <div v-if="isBookloading" class="p-4">
        <LoaderComponent />
      </div>
      <table v-else class="table-auto w-full border-collapse">
        <thead class="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
          <tr>
            <th class="py-3 px-6 text-left">Title</th>
            <th class="py-3 px-6 text-left">Cover</th>
            <th class="py-3 px-6 text-center">Action</th>
          </tr>
        </thead>
        <tbody class="text-gray-700 text-sm">
          <tr v-for="book in allBooks" :key="book.id" class="border-b hover:bg-gray-100">
            <td class="py-3 px-6">
              <router-link :to="{ name: 'BookDetails', params: { book_code: book.book_code } }"
                class="px-4 py-2 bg-blue-100 text-blue-600 font-semibold rounded-md hover:bg-blue-200 hover:text-blue-700 transition"
                target="_blank"
              >
                {{ book.title }}
              </router-link>
            </td>
            <td class="py-3 px-6">
              <img :src="getCoverImage(book.cover_image, API_BASE_URL)" alt="Book Cover"
                class="w-24 h-24 shadow-lg rounded-lg" />
            </td>
            <td class="py-3 px-6 text-center space-x-2">
              <button @click="showBookEditModal = true; setBookData(book)"
                 class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition">
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
      <DashboardPaginationComponent :previousPage="previousPageUrl" :nextPage="nextPageUrl" :pageSize="10"
        :currentPage="parseInt(currentPage, 10)" :totalCount="totalBookCount" @fetch-page="changePage" />
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { useToast } from 'vue-toastification'
import { getCoverImage } from '@/helpers/getCoverImage'
import DashboardPaginationComponent from '@/components/dashboard/DashboardPaginationComponent .vue'
import LoaderComponent from '@/components/general/LoaderComponent.vue'
import AddBookModal from '@/modals/book/AddBookModal.vue'
import EditBookModal from '@/modals/book/EditBookModal.vue'

export default {
  name: 'BookListPage',
  components: {
    DashboardPaginationComponent,
    LoaderComponent,
    AddBookModal,
    EditBookModal
  },
  data () {
    return {
      isSaving: false,
      currentPage: 0,
      showBookAddModal: false,
      showBookEditModal: false,
      book: {
        title: '',
        genres: [],
        topics: [],
        authors: [],
        publisher: null,
        description: '',
        edition: '',
        isbn: '',
        published_year: '',
        language: '',
        book: '',
        cover_image: ''
      },
      editBook: {},
      isAPISuccess: false
    }
  },
  computed: {
    ...mapGetters([
      'allBooks', 'nextPageUrl', 'previousPageUrl', 'totalBookCount',
      'currentBookPageSize', 'isBookloading', 'bookErrors'
    ]),
    API_BASE_URL () {
      return process.env.VUE_APP_BACKEND_URL
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

        this.fetchBooks({ page, pageSize: 10 })
      }
    },
    bookErrors (newErrors) {
      const toast = useToast()
      if (newErrors && newErrors.length) {
        newErrors.forEach(error => {
          console.log(error)
          toast.error(error)
        })
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
    ...mapActions([
      'fetchBooks', 'addBook'
    ]),
    getCoverImage,
    changePage (page) {
      this.$router.push({ query: { page } })
    },
    async handleConfirm (updatedBook) {
      console.log('before prepare data to save:', updatedBook)
      const toast = useToast()
      const formData = new FormData()

      formData.append('title', updatedBook.title || '')
      formData.append('description', updatedBook.description || '')
      formData.append('published_year', updatedBook.published_year || '')
      formData.append('publisher', updatedBook.publisher || '')
      formData.append('edition', updatedBook.edition || '')
      // formData.append('isbn', updatedBook.isbn || '')
      if (updatedBook.isbn) {
        formData.append('isbn', updatedBook.isbn)
      }
      formData.append('language', updatedBook.language || '')

      updatedBook.authors.forEach((authorId) => {
        formData.append('authors', authorId)
      })

      updatedBook.genres.forEach((genreId) => {
        formData.append('genres', genreId)
      })

      updatedBook.topics.forEach((topicId) => {
        formData.append('topics', topicId)
      })

      if (updatedBook.book) {
        formData.append('book', updatedBook.book)
      }

      if (updatedBook.cover_image) {
        formData.append('cover_image', updatedBook.cover_image)
      }

      try {
        this.isSaving = true
        console.log('updatedBook:', formData)
        const result = await this.addBook(formData)

        if (result.success) {
          this.showBookAddModal = false
          this.isAPISuccess = true
          toast.success('Book created successfully!')
        } else {
          console.log('Else Error:', result.message)
          toast.error(result.message || 'An error occurred.')
        }
      } catch (error) {
        console.error('Catch Error:', error)
        toast.error('Unexpected error occurred.')
      } finally {
        this.isSaving = false
      }
    },
    setBookData (book) {
      console.log('exist book data:', this.editBook)
      console.log('selected book:', book)
      this.editBook = book
      console.log('updated book data:', this.editBook)
    }
  }
}
</script>

<style scoped></style>
