// src/store/modules/books/books.js

import {
  fetchV1Books,
  createV1Book,
  editV1Book
} from '@/services/v1/bookAPIService'

export default {
  state: {
    books: [],
    nextPageUrl: null,
    previousPageUrl: null,
    pageSize: 8,
    loading: false,
    totalCount: 0,
    error: null
  },
  getters: {
    allBooks: (state) => state.books,
    nextPageUrl: (state) => state.nextPageUrl,
    previousPageUrl: (state) => state.previousPageUrl,
    currentBookPageSize: (state) => state.pageSize,
    isBookloading: (state) => state.loading,
    totalBookCount: (state) => state.totalCount,
    bookErrors: (state) => state.error
  },
  mutations: {
    SET_BOOKS (state, books) {
      state.books = books
    },
    SET_NEXT_PAGE (state, url) {
      state.nextPageUrl = url
    },
    SET_PREVIOUS_PAGE (state, url) {
      state.previousPageUrl = url
    },
    SET_BOOK_PAGE_SIZE (state, pageSize) {
      state.currentBookPageSize = pageSize
    },
    SET_LOADING (state, loading) {
      state.loading = loading
    },
    SET_TOTAL_COUNT (state, totalCount) {
      state.totalCount = totalCount
    },
    SET_ERROR (state, error) {
      state.error = error
    }
  },
  actions: {
    async fetchBooks (
      { commit },
      { page = 1, pageSize = 8, genre = null, topic = null } = {}
    ) {
      commit('SET_LOADING', true)
      try {
        const response = await fetchV1Books(page, pageSize, genre, topic)
        commit('SET_BOOKS', response.results)
        commit('SET_NEXT_PAGE', response.next)
        commit('SET_PREVIOUS_PAGE', response.previous)
        commit('SET_BOOK_PAGE_SIZE', pageSize)
        commit('SET_TOTAL_COUNT', response.count)
      } catch (error) {
        console.error('Error fetching books:', error)
      } finally {
        commit('SET_LOADING', false)
      }
    },
    async addBook ({ commit }, book) {
      try {
        const response = await createV1Book(book)
        console.log('Created book:', response)
        if (response.error) {
          const errorMessages = []
          errorMessages.push(response.message)
          commit('SET_ERROR', errorMessages)
          return { success: false, message: response.message }
        }
        return { success: true, data: response }
      } catch (error) {
        const errorMessages = []
        for (const [key, value] of Object.entries(error.response.data)) {
          errorMessages.push(value[0])
          console.log(`Book create... ${key}: ${value}`)
        }
        commit('SET_ERROR', errorMessages)
        // throw error
        const message =
          error.response?.data?.message || 'Failed to add book.'
        return { success: false, message }
      }
    },
    async editBook ({ commit }, { bookId, book }) {
      console.log('store file... book id: ', bookId)
      console.log('store file... data: ', book)
      try {
        const response = await editV1Book(bookId, book)
        console.log('Edit book:', response)
        if (response.error) {
          const errorMessages = []
          errorMessages.push(response.message)
          commit('SET_ERROR', errorMessages)
          return { success: false, message: response.message }
        }
        return { success: true, data: response }
      } catch (error) {
        const errorMessages = []
        for (const [key, value] of Object.entries(error.response.data)) {
          errorMessages.push(value[0])
          console.log(`Book edit... ${key}: ${value}`)
        }
        commit('SET_ERROR', errorMessages)
        const message =
          error.response?.data?.message || 'Failed to edit book.'
        return { success: false, message }
      }
    }
  }
}
