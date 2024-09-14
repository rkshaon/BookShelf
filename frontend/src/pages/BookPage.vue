<template>
    <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <router-link :to="{ name: 'BookDetails', params: { book_code: bookCode } }"
            class="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300">
            Go Back
        </router-link>
        <a href="#"
            class="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300">
            Go Back
        </a>
        <div class="relative w-full overflow-hidden shadow-lg rounded-lg border border-gray-300 mt-4">
            <iframe :src="bookURL" class="w-full h-96 border-none" />
        </div>
    </div>
</template>

<script>
import { getBookURL } from '@/helpers/getBookURL'
import { getBookURLUsingBookCode } from '@/helpers/getBookURLUsingBookCode'

export default {
  name: 'BookPage',
  data () {
    return {
      bookURL: '',
      bookCode: ''
    }
  },
  computed: {
    API_BASE_URL () {
      return process.env.VUE_APP_BACKEND_URL
    }
  },
  mounted () {
    this.bookCode = this.$route.params.book_code
    const bookPath = this.$route.state?.bookURL

    if (bookPath) {
      this.bookURL = getBookURL(bookPath, this.API_BASE_URL)
    } else if (this.bookCode) {
      this.bookURL = getBookURLUsingBookCode(this.bookCode, this.API_BASE_URL)
    } else {
      console.error('No book path or code found')
    }
  }
}
</script>
