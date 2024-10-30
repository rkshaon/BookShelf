<template>
  <div class="bg-white shadow-lg rounded-lg overflow-hidden">
    <router-link :to="{
      name: 'BookDetails', params: {
        book_code: book.book_code
      }
    }">
      <img :src="getCoverImage(book.cover_image, API_BASE_URL)" alt="Book Cover" class="w-full h-48 object-cover">
    </router-link>
    <div class="p-4">
      <router-link :to="{
        name: 'BookDetails', params: {
          book_code: book.book_code
        }
      }">
        <h3 class="text-lg font-bold text-gray-800">{{ book.title }}</h3>
      </router-link>
      <div class="flex flex-wrap gap-1 mt-2">
        <router-link v-for="author in book.authors" :key="author.id"
          :to="{ name: 'AuthorDetails', params: { id: author.id } }"
          class="inline-block px-1 py-0.5 text-sm bg-blue-100 text-blue-600 rounded-md font-semibold hover:bg-blue-200 hover:text-blue-700 transition">
          {{ author.full_name }}
        </router-link>
      </div>
      <p v-if="book.published_year" class="text-gray-400">
        <strong>Published</strong>: {{ book.published_year }}
      </p>
    </div>
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
