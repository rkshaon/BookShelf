<template>
    <div>
        <iframe :src="bookURL" width="100%" height="500"></iframe>
    </div>
</template>

<script>
import { getBookURL } from '@/helpers/getBookURL'
import { getBookURLUsingBookCode } from '@/helpers/getBookURLUsingBookCode'

export default {
  name: 'BookPage',
  data () {
    return {
      bookURL: ''
    }
  },
  computed: {
    API_BASE_URL () {
      return process.env.VUE_APP_BACKEND_URL
    }
  },
  methods: {
    getBookURL,
    getBookURLUsingBookCode
  },
  mounted () {
    const bookPath = this.$route.state?.bookURL || ''
    const bookCode = this.$route.params.book_code

    if (bookPath) {
      this.bookURL = getBookURL(bookPath, this.API_BASE_URL)
    } else {
      console.error('No book path found')
    }

    if (bookCode) {
      this.bookURL = getBookURLUsingBookCode(bookCode, this.API_BASE_URL)
    } else {
      console.log('No book code found')
    }
  }
}
</script>
