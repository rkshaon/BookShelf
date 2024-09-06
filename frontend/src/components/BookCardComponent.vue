<template>
    <div class="bg-white shadow-lg rounded-lg overflow-hidden">
        <img :src="book.coverImage" alt="Book Cover" class="w-full h-48 object-cover">
        <div class="p-4">
            <h3 class="text-lg font-bold text-gray-800">{{ book.title }}</h3>
            <p class="text-gray-600">{{ book.authors.join(', ') }}</p>
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
  }
}
</script>

<style scoped>
/* Additional styles if needed */
</style>
