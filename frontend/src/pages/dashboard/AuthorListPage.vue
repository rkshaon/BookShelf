<template>
    <div class="book-list-page">
        <button @click="uploadBook">Upload Book</button>
        <table>
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Author</th>
                    <th>Genre</th>
                    <th>Published Date</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="book in paginatedBooks" :key="book.id">
                    <td>{{ book.title }}</td>
                    <td>{{ book.author }}</td>
                    <td>{{ book.genre }}</td>
                    <td>{{ book.publishedDate }}</td>
                </tr>
            </tbody>
        </table>
        <div class="pagination">
            <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
            <span>Page {{ currentPage }} of {{ totalPages }}</span>
            <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
        </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      books: [], // This should be populated with the list of books
      currentPage: 1,
      pageSize: 10
    }
  },
  computed: {
    totalPages () {
      return Math.ceil(this.books.length / this.pageSize)
    },
    paginatedBooks () {
      const start = (this.currentPage - 1) * this.pageSize
      const end = start + this.pageSize
      return this.books.slice(start, end)
    }
  },
  methods: {
    uploadBook () {
      // Logic to upload a book
    },
    prevPage () {
      if (this.currentPage > 1) {
        this.currentPage--
      }
    },
    nextPage () {
      if (this.currentPage < this.totalPages) {
        this.currentPage++
      }
    }
  }
}
</script>

<style scoped>
.book-list-page {
    padding: 20px;
}

button {
    margin-bottom: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th,
td {
    border: 1px solid #ddd;
    padding: 8px;
}

th {
    background-color: #f2f2f2;
}

.pagination {
    margin-top: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.pagination button {
    margin: 0 10px;
}
</style>
