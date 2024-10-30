<template>
  <nav class="bg-gray-800 text-white">
    <div class="container mx-auto px-2 sm:px-6 lg:px-8">
      <div class="relative flex items-center justify-between h-16">
        <div class="flex-shrink-0">
          <router-link to="/" class="text-xl font-bold text-white">BookShelf</router-link>
        </div>
        <div class="flex-grow flex justify-end relative">
          <div class="relative w-full max-w-md">
            <input v-model="searchQuery" @input="performSearch" @focus="isDropdownVisible = true" type="text" class="w-full px-4 py-2 pl-10 rounded-md bg-gray-700 text-white placeholder-gray-400 focus:outline-none
            focus:bg-gray-600 focus:ring-2 focus:ring-blue-500" placeholder="Search books, authors, genres..." />
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M21 21l-4.35-4.35m1.42-4.61A7.5 7.5 0 1115.3 15.3z" />
              </svg>
            </div>
            <ul v-if="isDropdownVisible && searchResults.length > 0 && searchQuery"
              class="absolute w-full bg-white text-black shadow-md mt-2 rounded-lg z-10">
              <SearchItemComponent v-for="(result, index) in searchResults" :key="index" :result="result"
                @select-result="navigateToResult" />
            </ul>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SearchItemComponent from '@/components/SearchItemComponent.vue'

export default {
  name: 'NavBarComponent',
  components: {
    SearchItemComponent
  },
  data () {
    return {
      searchQuery: '',
      searchTimeout: null,
      isDropdownVisible: false
    }
  },
  computed: {
    ...mapGetters(['searchResults'])
  },
  methods: {
    ...mapActions(['searchBooks']),

    performSearch () {
      if (this.searchTimeout) {
        clearTimeout(this.searchTimeout)
      }

      this.searchTimeout = setTimeout(() => {
        if (this.searchQuery.trim()) {
          this.searchBooks({ query: this.searchQuery.trim() })
        }
      }, 500)
    },

    navigateToResult (result) {
      this.isDropdownVisible = false
      this.$router.push(`/book/${result.book_code}`)
    },

    handleClickOutside (event) {
      if (!this.$el.contains(event.target)) {
        this.isDropdownVisible = false
      }
    }
  },
  mounted () {
    document.addEventListener('click', this.handleClickOutside)
  },
  beforeUnmount () {
    document.removeEventListener('click', this.handleClickOutside)
  }
}
</script>

<style scoped>
/* Add any additional styling here */
</style>
