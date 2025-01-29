<template>
  <div v-if="visible" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white rounded-lg shadow-lg w-full max-w-lg">
      <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center">
        <h3 class="text-lg font-semibold text-gray-700">{{ title }}</h3>
        <button @click="closeModal" class="text-gray-400 hover:text-gray-600 text-xl">
          &times;
        </button>
      </div>
      <div class="flex border-b border-gray-200">
        <button @click="currentTab = 'Book'" :class="[
          'py-2 px-4 focus:outline-none transition',
          currentTab === 'Book'
            ? 'border-b-2 border-blue-500 text-blue-500'
            : 'text-gray-500 hover:text-gray-700'
        ]">
          Book
        </button>
        <button @click="currentTab = 'Publish'" :class="[
          'py-2 px-4 focus:outline-none transition',
          currentTab === 'Publish'
            ? 'border-b-2 border-blue-500 text-blue-500'
            : 'text-gray-500 hover:text-gray-700'
        ]">
          Publish
        </button>
        <button @click="currentTab = 'Authors'" :class="[
          'py-2 px-4 focus:outline-none transition',
          currentTab === 'Authors'
            ? 'border-b-2 border-blue-500 text-blue-500'
            : 'text-gray-500 hover:text-gray-700'
        ]">
          Authors
        </button>
        <button @click="currentTab = 'Others'" :class="[
          'py-2 px-4 focus:outline-none transition',
            currentTab === 'Others'
            ? 'border-b-2 border-blue-500 text-blue-500'
            : 'text-gray-500 hover:text-gray-700'
        ]">
          Others
        </button>
      </div>
      <div class="p-6">
        <form @submit.prevent="onConfirm">
          <div v-if="currentTab === 'Book'">
            <div class="mb-4">
              <label for="title" class="block text-gray-700 text-sm font-bold mb-2">Title</label>
              <input type="text" id="title" v-model="localBook.title"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div class="mb-4">
              <label for="description" class="block text-gray-700 text-sm font-bold mb-2">Description</label>
              <textarea v-model="localBook.description" id="description"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
              </textarea>
            </div>
            <div class="mb-4">
              <label for="language" class="block text-gray-700 text-sm font-bold mb-2">Language</label>
              <input type="text" id="language" v-model="localBook.language"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div class="mb-4">
              <label for="book" class="block text-gray-700 text-sm font-bold mb-2">Book</label>
              <div v-if="previewImage" class="mb-4">
                <router-link :to="{ name: 'BookDetails', params: { book_code: book.book_code } }"
                  class="px-4 py-2 bg-blue-100 text-blue-600 font-semibold rounded-md hover:bg-blue-200 hover:text-blue-700 transition"
                  target="_blank">
                  {{ book.title }}
                </router-link>
              </div>
              <input type="file" id="book" accept="application/pdf" @change="handleBookFile"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div class="mb-4">
              <label for="cover_image" class="block text-gray-700 text-sm font-bold mb-2">Cover Image</label>
              <div v-if="previewImage" class="mb-4">
                <img :src="getCoverImage(previewImage, API_BASE_URL)" alt="Cover Preview"
                  class="w-32 h-32 object-cover rounded" />
              </div>
              <input type="file" id="cover_image" accept="image/*" @change="handleCoverImage"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
          </div>
          <div v-else-if="currentTab === 'Publish'">
            <div class="mb-4 relative">
              <label for="publisher" class="block text-gray-700 text-sm font-bold mb-2">Publisher</label>
              <input type="text" id="publisher" v-model="localBook.publisher.name" @input="performPublisherSearch"
                @blur="closeDropdown" @focus="performPublisherSearch"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
              <ul v-if="showDropdown && publishers.length"
                class="absolute z-10 bg-white border border-gray-300 rounded shadow-lg mt-1 w-full max-h-40 overflow-y-auto">
                <li v-for="publisher in publishers" :key="publisher.id" @click="selectPublisher(publisher)"
                  class="px-4 py-2 hover:bg-gray-200 cursor-pointer">
                  {{ publisher.name }}
                </li>
              </ul>
            </div>
            <div class="mb-4">
              <label for="published_year" class="block text-gray-700 text-sm font-bold mb-2">Published Year</label>
              <input type="text" id="published_year" v-model="localBook.published_year"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div class="mb-4">
              <label for="edition" class="block text-gray-700 text-sm font-bold mb-2">Edition</label>
              <input type="text" id="edition" v-model="localBook.edition"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div class="mb-4">
              <label for="isbn" class="block text-gray-700 text-sm font-bold mb-2">ISBN</label>
              <input type="text" id="isbn" v-model="localBook.isbn"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
          </div>
          <div v-else-if="currentTab === 'Authors'">
            <div class="mb-4">
              <label for="authors" class="block text-gray-700 text-sm font-bold mb-2">Authors</label>
              <input type="text" id="authors" v-model="localAuthor" @input="performAuthorSearch" @blur="closeDropdown"
                @focus="performAuthorSearch"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <!-- Dropdown for search results -->
            <ul v-if="showDropdown && authors.length"
              class="absolute z-10 bg-white border border-gray-300 rounded shadow-lg mt-1 w-full max-h-40 overflow-y-auto">
              <li v-for="author in authors" :key="author.id" @click="selectAuthor(author)"
                class="px-4 py-2 hover:bg-gray-200 cursor-pointer">
                {{ author.full_name }}
              </li>
            </ul>
            <div class="flex flex-wrap mt-2">
              <span v-for="(author, index) in localBook.authors" :key="author.id"
                class="flex items-center bg-gray-200 text-gray-700 px-2 py-1 mr-2 mb-2 rounded-full shadow">
                {{ author.full_name }}
                <button @click="removeAuthor(index)" class="ml-2 text-gray-500 hover:text-gray-700 focus:outline-none">
                  &times;
                </button>
              </span>
            </div>
          </div>
          <div v-else-if="currentTab === 'Others'">
            <!-- Genre -->
            <div class="mb-4">
              <label for="genres" class="block text-gray-700 text-sm font-bold mb-2">Genres</label>
              <input type="text" id="genres" v-model="localGenre" @input="performGenreSearch" @blur="closeDropdown"
                @focus="performGenreSearch"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <ul v-if="showDropdown && genres.length"
              class="absolute z-10 bg-white border border-gray-300 rounded shadow-lg mt-1 w-full max-h-40 overflow-y-auto">
              <li v-for="genre in genres" :key="genre.id" @click="selectGenre(genre)"
                class="px-4 py-2 hover:bg-gray-200 cursor-pointer">
                {{ genre.name }}
              </li>
            </ul>
            <div class="flex flex-wrap mt-2">
              <span v-for="(genre, index) in localBook.genres" :key="genre.id"
                class="flex items-center bg-gray-200 text-gray-700 px-2 py-1 mr-2 mb-2 rounded-full shadow">
                {{ genre.name }}
                <button @click="removeGenre(index)" class="ml-2 text-gray-500 hover:text-gray-700 focus:outline-none">
                  &times;
                </button>
              </span>
            </div>
            <!-- Topic -->
            <div class="mb-4">
              <label for="topics" class="block text-gray-700 text-sm font-bold mb-2">Topics</label>
              <input type="text" id="topics" v-model="localTopic" @input="performTopicSearch" @blur="closeDropdown"
                @focus="performTopicSearch"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <ul v-if="showTopicDropdown && topics.length"
              class="absolute z-10 bg-white border border-gray-300 rounded shadow-lg mt-1 w-full max-h-40 overflow-y-auto">
              <li v-for="topic in topics" :key="topic.id" @click="selectTopic(topic)"
                class="px-4 py-2 hover:bg-gray-200 cursor-pointer">
                {{ topic.name }}
              </li>
            </ul>
            <div class="flex flex-wrap mt-2">
              <span v-for="(topic, index) in localBook.topics" :key="topic.id"
                class="flex items-center bg-gray-200 text-gray-700 px-2 py-1 mr-2 mb-2 rounded-full shadow">
                {{ topic.name }}
                <button @click="removeTopic(index)" class="ml-2 text-gray-500 hover:text-gray-700 focus:outline-none">
                  &times;
                </button>
              </span>
            </div>
          </div>
        </form>
      </div>
      <div class="px-6 py-4 border-t border-gray-200 flex justify-end space-x-3">
        <slot name="footer">
          <button @click="clearForm" class="bg-gray-300 text-gray-700 py-2 px-4 rounded hover:bg-gray-400 transition">
            Clear
          </button>
          <button @click="closeModal" class="bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-600 transition">
            Cancel
          </button>
          <button @click="onConfirm" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition">
            {{ title }}
          </button>
        </slot>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { getCoverImage } from '@/helpers/getCoverImage'

export default {
  name: 'AddAuthorModal',
  props: {
    visible: {
      type: Boolean,
      required: true
    },
    title: {
      type: String,
      default: 'Modal Title'
    },
    bookId: {
      type: String,
      required: true,
      default: '',
      validator (value) {
        return value !== null
      }
    },
    book: {
      type: Object,
      required: true,
      default: () => ({
        title: '',
        genres: [],
        topics: [],
        authors: [],
        publisher: null,
        description: '',
        edition: '',
        isbn: '',
        published_year: null,
        language: '',
        book: '',
        cover_image: ''
      })
    }
  },
  data () {
    return {
      currentTab: 'Book',
      localBook: { ...this.book },
      selectedAuthors: [],
      selectedGenres: [],
      selectedTopics: [],
      showDropdown: false,
      showTopicDropdown: false,
      searchTimeout: null,
      localPublisher: '',
      localAuthor: '',
      localGenre: '',
      localTopic: '',
      previewImage: null
    }
  },
  watch: {
    book: {
      handler (newValue) {
        console.log('in watcher... Book updated:', newValue)
        this.localBook = { ...newValue }
        this.previewImage = newValue.cover_image || null
      },
      immediate: true, // Trigger the watcher on component mount
      deep: true // Watch nested properties
    }
  },
  computed: {
    ...mapGetters([]),
    API_BASE_URL () {
      return process.env.VUE_APP_BACKEND_URL
    }
  },
  emits: ['close', 'confirm'],
  methods: {
    ...mapActions([]),
    getCoverImage,
    closeModal () {
      this.$emit('close')
    },
    onConfirm () {
      const formData = new FormData()

      if (this.book.description !== this.localBook.description) {
        formData.append('description', this.localBook.description || '')
      }

      formData.forEach((value, key) => {
        console.log(`${key}: ${value}`)
      })

      this.$emit('confirm', { bookId: this.bookId, editedData: formData })
    }
  }
}
</script>
