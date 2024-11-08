<template>
    <div class="book-list-page">
        <button @click="uploadBook">Upload Book</button>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Biography</th>
                    <th>Total Books</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="author in paginatedAuthors" :key="author.id">
                    <td>{{ author.title }}</td>
                    <td>{{ author.author }}</td>
                    <td>{{ author.genre }}</td>
                    <td>Delete / Edit</td>
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
      authors: [],
      currentPage: 1,
      pageSize: 10
    }
  },
  computed: {
    totalPages () {
      return Math.ceil(this.authors.length / this.pageSize)
    },
    paginatedAuthors () {
      const start = (this.currentPage - 1) * this.pageSize
      const end = start + this.pageSize
      return this.authors.slice(start, end)
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
