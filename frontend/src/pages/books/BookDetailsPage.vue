<template>
  <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <LoaderComponent v-if="isLoading" />
    <div v-else-if="bookDetails" class="bg-white shadow rounded-lg p-6 grid grid-cols-1 md:grid-cols-2 gap-8">
      <div class="book-cover-container">
        <img :src="getCoverImage(bookDetails.cover_image, API_BASE_URL)" alt="Book Cover"
          class="max-w-full h-auto shadow-lg rounded-lg book-cover-image" />
        <div v-if="isAdmin && bookDetails.cover_image == null" class="cover-overlay">
          Update Cover Image from
          <input type="number" v-model="updateCoverPageNumber" class="cover-input"> page
          <button @click="updateCoverPage" class="bg-green-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition cover-button">Update</button>
        </div>
      </div>
    <div>
        <router-link :to="{
          name: 'Book',
          params: { book_code: bookDetails.book_code },
          state: { bookURL: bookDetails.book }
        }"
          class="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300">
          Read
        </router-link>
        <h1 class="text-3xl font-bold text-gray-800 mb-4 mt-4">{{ bookDetails.title }}</h1>
        <div class="text-gray-600 mb-4">
          <strong>Authors:</strong>
          <div class="flex flex-wrap gap-2 mt-2">
            <router-link v-for="author in bookDetails.authors" :key="author.id"
              :to="{ name: 'AuthorDetails', params: { id: author.id } }"
              class="px-4 py-2 bg-blue-100 text-blue-600 font-semibold rounded-md hover:bg-blue-200 hover:text-blue-700 transition">
              {{ author.full_name }}
            </router-link>
          </div>
        </div>
        <p v-if="bookDetails.genres && bookDetails.genres.length > 0" class="text-gray-600 mb-4 flex items-center">
          <strong class="mr-2">Genre:</strong>
          <span class="flex flex-wrap gap-2">
            <router-link v-for="genre in bookDetails.genres" :key="genre.id"
              :to="{ name: 'GenreDetails', params: { id: genre.id, slug: genre.slug } }"
              class="inline-block px-2 py-1 bg-green-100 text-green-700 rounded-md text-sm hover:bg-green-200 transition">
              {{ genre.name }}
            </router-link>
          </span>
        </p>
        <p v-if="bookDetails.topics && bookDetails.topics.length > 0" class="text-gray-600 mb-4">
          <span class="flex flex-wrap gap-2">
            <router-link v-for="topic in bookDetails.topics" :key="topic.id"
              :to="{ name: 'TopicDetails', params: { id: topic.id, slug: topic.slug } }"
              class="inline-block px-2 py-1 bg-yellow-100 text-yellow-700 rounded-md text-sm hover:bg-green-200 transition">
              #{{ topic.slug }}
            </router-link>
          </span>
        </p>
        <p class="text-gray-600 mb-4">{{ bookDetails.description }}</p>
        <div class="grid grid-cols-1 gap-4">
          <div v-if="bookDetails.publisher">
            <strong>Publisher:</strong> {{ bookDetails.publisher.name }}
          </div>
          <div v-if="bookDetails.edition">
            <strong>Edition:</strong> {{ bookDetails.edition }}
          </div>
          <div v-if="bookDetails.isbn">
            <strong>ISBN:</strong> {{ bookDetails.isbn }}
          </div>
          <div v-if="bookDetails.pages">
            <strong>Pages:</strong> {{ bookDetails.pages }}
          </div>
          <div v-if="bookDetails.language">
            <strong>Language:</strong> {{ bookDetails.language }}
          </div>
          <div v-if="bookDetails.published_year">
            <strong>Published Year:</strong> {{ bookDetails.published_year }}
          </div>
        </div>
      </div>
    </div>
    <div v-else-if="errors" class="text-red-500">
      <div v-for="(error, index) in errors" :key="index">
        <NotFoundComponent contentType="Book" :errorMessage="error" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { useToast } from 'vue-toastification'
import { getCoverImage } from '@/helpers/getCoverImage'

import LoaderComponent from '@/components/general/LoaderComponent.vue'
import NotFoundComponent from '@/components/NotFoundComponent.vue'

export default {
  name: 'BookDetailsPage',
  components: {
    LoaderComponent,
    NotFoundComponent
  },
  metaInfo () {
    return {
      title: `${this.book.title} - BookShelf`,
      meta: [
        {
          name: 'description',
          content: `${this.book.title} by ${this.book.authors.map(a => a.full_name).join(', ')}. Find out more about this book on BookShelf.`
        },
        {
          name: 'keywords',
          content: `books, ${this.book.title}, ${this.book.authors.map(a => a.full_name).join(', ')}`
        },
        {
          property: 'og:title',
          content: `${this.book.title} - BookShelf`
        },
        {
          property: 'og:description',
          content: `${this.book.title} by ${this.book.authors.map(a => a.full_name).join(', ')}.`
        }
      ]
    }
  },
  data () {
    return {
      updateCoverPageNumber: 1
    }
  },
  computed: {
    ...mapGetters({
      bookDetails: 'getBookDetails',
      isLoading: 'isBookLoading',
      errors: 'bookDetailsError',
      isAdmin: 'isAdmin'
    }),
    API_BASE_URL () {
      return process.env.VUE_APP_BACKEND_URL
    }
  },
  watch: {
    '$route.params.book_code': {
      immediate: true,
      handler (newBookCode) {
        this.fetchBookDetails(newBookCode)
      }
    },
    bookDetails (newBookDetails) {
      if (newBookDetails && newBookDetails.title) {
        document.title = `Book Shelf | ${newBookDetails.title}`
      }
    },
    errors (newErrors) {
      const toast = useToast()
      if (newErrors && newErrors.length) {
        newErrors.forEach(error => {
          toast.error(error)
        })
      }
    }
  },
  mounted () {
    const bookCode = this.$route.params.book_code
    this.fetchBookDetails(bookCode)
    document.title = 'Book Shelf | Loading ...'
  },
  methods: {
    ...mapActions(['fetchBookDetails', 'updateBookCoverPage']),
    getCoverImage,
    async updateCoverPage () {
      console.log('cover page', this.updateCoverPageNumber)
      await this.updateBookCoverPage({
        data: {
          page_number: this.updateCoverPageNumber
        },
        bookCode: this.bookDetails.book_code
      })
    }
  }
}
</script>

<style scoped>
/* Container for the book cover */
.book-cover-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Book cover image */
.book-cover-image {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Overlay that appears on hover */
.cover-overlay {
  position: absolute;
  top: 0; /* Fix to the top */
  left: 50%; /* Center horizontally */
  transform: translateX(-50%); /* Adjust centering */
  background: rgba(0, 0, 0, 0.6);
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
  border-radius: 8px;
  height: 50%; /* Set height */
  width: 50%; /* Ensure full width */
  margin: auto;
}

/* Show overlay when hovering */
.book-cover-container:hover .cover-overlay {
  opacity: 1;
}

/* Styling for input field */
.cover-input {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 5px;
  width: 160px;
  margin: 8px 0;
  text-align: center;
  color: black;
}

/* Styling for button */
.cover-button {
  background: #28a745;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s ease-in-out;
  margin-top:9px;
  width: 160px;
}

.cover-button:hover {
  background: #1e7e34;
}
</style>
