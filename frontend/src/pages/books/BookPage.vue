<template>
    <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8 h-screen flex flex-col">
        <router-link v-if="bookCode" :to="{ name: 'BookDetails', params: { book_code: bookCode } }"
            class="bg-blue-500 w-32 text-center text-white font-bold py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300">
            Go Back
        </router-link>
        <LoaderComponent v-else />
        <div class="relative flex-grow overflow-hidden shadow-lg rounded-lg border border-gray-300 mt-4">
            <iframe :src="bookURL" class="w-full h-full border-none" />
        </div>
    </div>
</template>

<script>
import { getBookURL } from '@/helpers/getBookURL'
import { getBookURLUsingBookCode } from '@/helpers/getBookURLUsingBookCode'

import LoaderComponent from '@/components/general/LoaderComponent.vue'

export default {
  name: 'BookPage',
  components: {
    LoaderComponent
  },
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
