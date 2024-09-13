<template>
  <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <div v-if="book" class="bg-white shadow rounded-lg p-6">
      <h1 class="text-3xl font-bold text-gray-800 mb-4">{{ book.title }}</h1>
      <p class="text-gray-600 mb-2">By {{ book.authors.map(author => author.full_name).join(', ') }}</p>
      <img v-if="book.coverImage" :src="book.coverImage" alt="Book Cover" class="w-full h-64 object-cover mb-4" />
      <p class="text-gray-600">{{ book.description }}</p>
    </div>
    <div v-else>
      <LoaderComponent />
    </div>
  </div>
</template>

<script>
import LoaderComponent from '@/components/LoaderComponent.vue'

export default {
  name: 'BookDetailsPage',
  components: {
    LoaderComponent
  },
  data () {
    return {
      book: null // Store book data
    }
  },
  mounted () {
    // this.fetchBookDetails();
  },
  methods: {
    // async fetchBookDetails() {
    //   const bookId = this.$route.params.id;
    //   try {
    //     const response = await this.$axios.get(`${process.env.VUE_APP_BACKEND_URL}/book/v1/${bookId}/`);
    //     this.book = response.data;
    //   } catch (error) {
    //     console.error('Error fetching book details:', error);
    //   }
    // }
  }
}
</script>

<style scoped>
/* Add custom styles here */
</style>
