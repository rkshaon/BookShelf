<template>
  <div class="bg-white shadow-lg rounded-lg overflow-hidden">
    <router-link :to="{
  name: 'BookDetails', params: {
        book_code: book.book_code
      }
    }">
    <img :src="getCoverImageUrl(book.cover_image)" alt="Book Cover" class="w-full h-48 object-cover">
    <div class="p-4">
      <h3 class="text-lg font-bold text-gray-800">{{ book.title }}</h3>
      <p class="text-gray-600">{{ book.authors.map(author => author.full_name).join(', ') }}</p>
    </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'BookCardComponent',
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  methods: {
    getCoverImageUrl (coverImage) {
      const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
      return coverImage ? `${API_BASE_URL}${coverImage}` : 'https://fastly.picsum.photos/id/1/200/300.jpg?hmac=jH5bDkLr6Tgy3oAg5khKCHeunZMHq0ehBZr6vGifPLY' // Fallback to default image if cover_image is null
    }
  }
}
</script>

<style scoped>
/* Additional styles if needed */
</style>
