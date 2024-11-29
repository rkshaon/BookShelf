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
              <input type="file" id="book" accept="application/pdf" @change="handleBookFile"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div class="mb-4">
              <label for="cover_image" class="block text-gray-700 text-sm font-bold mb-2">Cover Image</label>
              <input type="file" id="cover_image" accept="image/*" @change="handleCoverImage"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
          </div>
          <div v-else-if="currentTab === 'Publish'">
            <!-- <div class="mb-4">
              <label for="publisher" class="block text-gray-700 text-sm font-bold mb-2">Publisher</label>
              <input type="text" id="publisher" v-model="localBook.publisher" @input="performSearch"
                @blur="closeDropdown" @focus="performSearch"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div> -->
            <div class="mb-4 relative">
              <label for="publisher" class="block text-gray-700 text-sm font-bold mb-2">Publisher</label>
              <input type="text" id="publisher" v-model="localPublisher" @input="performSearch"
                @blur="closeDropdown" @focus="performSearch"
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
              <input type="text" id="authors" v-model="localBook.authors"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
          </div>
          <div v-else-if="currentTab === 'Others'">
            <div class="mb-4">
              <label for="genres" class="block text-gray-700 text-sm font-bold mb-2">Genres</label>
              <input type="text" id="genres" v-model="localBook.genres"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div class="mb-4">
              <label for="topics" class="block text-gray-700 text-sm font-bold mb-2">Topics</label>
              <input type="text" id="topics" v-model="localBook.topics"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
          </div>
        </form>
      </div>
      <div class="px-6 py-4 border-t border-gray-200 flex justify-end space-x-3">
        <slot name="footer">
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
    book: {
      type: Object,
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
        languages: '',
        book: '',
        cover_image: ''
      })
    }
  },
  data () {
    return {
      currentTab: 'Book',
      localBook: { ...this.book },
      showDropdown: false,
      searchTimeout: null,
      localPublisher: ''
    }
  },
  computed: {
    ...mapGetters([
      'publishers'
    ])
  },
  emits: ['close', 'confirm'],
  methods: {
    ...mapActions([
      'searchPublisher'
    ]),
    handleBookFile (event) {
      const file = event.target.files[0]
      if (file && file.type === 'application/pdf') {
        this.localBook.book = file
      } else {
        alert('Please select a valid PDF file.')
      }
    },
    handleCoverImage (event) {
      const file = event.target.files[0]
      if (file && file.type.startsWith('image/')) {
        this.localBook.cover_image = file
      } else {
        alert('Please select a valid image file.')
      }
    },
    async performSearch () {
      if (this.localPublisher.length < 2) {
        this.showDropdown = false
        return
      }
      if (this.searchTimeout) {
        clearTimeout(this.searchTimeout)
      }

      this.searchTimeout = setTimeout(() => {
        if (this.localPublisher.trim()) {
          this.showDropdown = true
          this.searchPublisher({ query: this.localPublisher.trim() })
        } else {
          this.showDropdown = false
        }
      }, 500)
    },
    selectPublisher (publisher) {
      this.localBook.publisher = publisher.id
      this.localPublisher = publisher.name
      this.showDropdown = false
    },
    closeDropdown () {
      setTimeout(() => {
        this.showDropdown = false
      }, 200)
    },
    closeModal () {
      this.$emit('close')
    },
    onConfirm () {
      this.$emit('confirm', this.localBook)
    }
  }
}
</script>
