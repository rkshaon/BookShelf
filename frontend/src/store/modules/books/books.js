// src/store/modules/books/books.js

import bookAPIService from '@/services/v1/bookAPIService'

export default {
  state: {
    books: [],
    nextPageUrl: null,
    previousPageUrl: null,
    pageSize: 8,
    loading: false
  },
  getters: {
    allBooks: (state) => state.books,
    nextPageUrl: (state) => state.nextPageUrl,
    previousPageUrl: (state) => state.previousPageUrl,
    currentBookPageSize: (state) => state.pageSize,
    isBookloading: (state) => state.loading
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
    }
  },
  actions: {
    async fetchBooks (
      { commit },
      { page = 1, pageSize = 8, genre = null, topic = null } = {}
    ) {
      commit('SET_LOADING', true)
      try {
        const response = await bookAPIService.fetchV1Books(
          page,
          pageSize,
          genre,
          topic
        )
        commit('SET_BOOKS', response.results)
        commit('SET_NEXT_PAGE', response.next)
        commit('SET_PREVIOUS_PAGE', response.previous)
        commit('SET_BOOK_PAGE_SIZE', pageSize)
      } catch (error) {
        console.error('Error fetching books:', error)
      } finally {
        commit('SET_LOADING', false)
      }
    }
  }
}
