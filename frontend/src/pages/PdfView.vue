<template>
  <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <LoaderComponent v-if="isLoading" />
    <div v-else>
      <div class="mb-4">
        <router-link v-if="bookCode" :to="{ name: 'BookDetails', params: { book_code: bookCode } }"
          class="bg-blue-500 w-32 text-center text-white font-bold py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300">
          Go Back
        </router-link>
      </div>
      <div class="flex justify-between items-center mb-4">
        <button @click="prevPage" class="bg-blue-500 text-white px-4 py-2 rounded">Previous</button>
        <span>Page {{ currentPage }} of {{ totalPages }}</span>
        <button @click="nextPage" class="bg-blue-500 text-white px-4 py-2 rounded">Next</button>
      </div>
    </div>
    <div>
      <canvas ref="pdfCanvas" class="border border-gray-300 shadow-lg"></canvas>
    </div>
  </div>
</template>

<script>
import * as pdfjsLib from 'pdfjs-dist/legacy/build/pdf'
import { getBookURL } from '@/helpers/getBookURL'
import { getBookURLUsingBookCode } from '@/helpers/getBookURLUsingBookCode'

export default {
  name: 'PdfViewer',
  data () {
    return {
      pdf: null,
      currentPage: 1,
      totalPages: 0,
      isLoading: true,
      bookCode: '',
      bookURL: ''
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
    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.10.377/pdf.worker.min.js'
    this.loadPdf(this.bookURL)
  },
  methods: {
    async loadPdf (url) {
      const loadingTask = pdfjsLib.getDocument(url)
      try {
        const pdfDoc = await loadingTask.promise
        this.pdf = pdfDoc
        this.totalPages = pdfDoc.numPages
        this.isLoading = false
        this.renderPage(this.currentPage)
      } catch (error) {
        console.error('Error loading PDF:', error)
      }
    },
    async renderPage (pageNum) {
      this.isLoading = true
      const canvas = this.$refs.pdfCanvas
      const context = canvas.getContext('2d')

      try {
        const page = await this.pdf.getPage(pageNum)
        const viewport = page.getViewport({ scale: 1.5 })
        canvas.height = viewport.height
        canvas.width = viewport.width

        const renderContext = {
          canvasContext: context,
          viewport: viewport
        }

        await page.render(renderContext).promise
        this.isLoading = false
      } catch (error) {
        console.error('Error rendering page:', error)
      }
    },
    prevPage () {
      if (this.currentPage <= 1) return
      this.currentPage--
      this.renderPage(this.currentPage)
    },
    nextPage () {
      if (this.currentPage >= this.totalPages) return
      this.currentPage++
      this.renderPage(this.currentPage)
    }
  }
}
</script>

<style scoped>
canvas {
  width: 100%;
  max-width: 100%;
}
</style>
