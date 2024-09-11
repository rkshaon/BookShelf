<template>
  <div class="bg-white shadow-lg rounded-lg overflow-hidden">
    <!-- <img :src="book.cover_image" alt="Book Cover" class="w-full h-48 object-cover"> -->
    <img :src="getCoverImageUrl(book.cover_image)" alt="Book Cover" class="w-full h-48 object-cover">
    <div class="p-4">
      <h3 class="text-lg font-bold text-gray-800">{{ book.title }}</h3>
      <!-- <p class="text-gray-600">{{ book.authors.join(', ') }}</p> -->
      <p class="text-gray-600">{{ book.authors.map(author => author.full_name).join(', ') }}</p>
    </div>
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
      const baseURL = 'http://localhost:8001/'
      return coverImage ? `${baseURL}${coverImage}` : 'https://fastly.picsum.photos/id/1/200/300.jpg?hmac=jH5bDkLr6Tgy3oAg5khKCHeunZMHq0ehBZr6vGifPLY' // Fallback to default image if cover_image is null
    }
  }
}
</script>

<style scoped>
/* Additional styles if needed */
</style>
