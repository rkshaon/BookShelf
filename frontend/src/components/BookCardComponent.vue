<template>
  <div class="bg-white shadow-lg rounded-lg overflow-hidden">
    <router-link :to="{
      name: 'BookDetails', params: {
        book_code: book.book_code
      }
    }">
      <img :src="getCoverImage(book.cover_image, API_BASE_URL)" alt="Book Cover" class="w-full h-48 object-cover">
      <div class="p-4">
        <h3 class="text-lg font-bold text-gray-800">{{ book.title }}</h3>
        <p class="text-gray-600">{{ book.authors.map(author => author.full_name).join(', ') }}</p>
        <p v-if="book.published_year" class="text-gray-400">
          <strog>Published</strog>: {{ book.published_year }}
        </p>
      </div>
    </router-link>
  </div>
</template>

<script>
import { getCoverImage } from '@/helpers/getCoverImage'

export default {
  name: 'BookCardComponent',
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    API_BASE_URL () {
      return process.env.VUE_APP_BACKEND_URL
    }
  },
  methods: {
    getCoverImage
  }
}
</script>

<style scoped>
/* Additional styles if needed */
</style>
