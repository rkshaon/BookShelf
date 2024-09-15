<template>
    <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <!-- Previous and Next Page Buttons -->
        <div class="flex justify-between items-center mb-4">
            <button @click="prevPage" class="bg-blue-500 text-white px-4 py-2 rounded">Previous Page</button>
            <span>Page {{ currentPage }} of {{ totalPages }}</span>
            <button @click="nextPage" class="bg-blue-500 text-white px-4 py-2 rounded">Next Page</button>
        </div>

        <!-- Canvas for PDF Rendering -->
        <canvas ref="pdfCanvas" class="border border-gray-300 shadow-lg"></canvas>

        <LoaderComponent v-if="isLoading" />
    </div>
</template>

<script>
import * as pdfjsLib from 'pdfjs-dist/legacy/build/pdf'
import pdfjsWorker from 'pdfjs-dist/legacy/build/pdf.worker.entry' // Corrected worker import
import LoaderComponent from '@/components/LoaderComponent.vue'

export default {
  name: 'PdfViewer',
  components: { LoaderComponent },
  data () {
    return {
      pdf: null, // Holds the PDF document
      currentPage: 1, // Current page number
      totalPages: 0, // Total number of pages
      isLoading: true // Loader flag
    }
  },
  mounted () {
    // Set the worker source
    pdfjsLib.GlobalWorkerOptions.workerSrc = pdfjsWorker

    // Initialize the PDF viewer
    this.loadPdf('/path/to/your/pdf/document.pdf') // Replace with your PDF path
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
