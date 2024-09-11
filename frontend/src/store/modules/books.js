// src/store/modules/books.js

import bookAPIService from '@/services/v1/bookAPIService'

export default {
  state: {
    books: [],
    nextPageUrl: null,
    previousPageUrl: null
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
    }
  },
  actions: {
    async fetchBooks ({ commit }, url = null) {
      try {
        const response = await bookAPIService.fetchV1Books(url)
        commit('SET_BOOKS', response.results) // Assuming 'results' contains the books array
        commit('SET_NEXT_PAGE', response.next) // Assuming pagination 'next' URL
        commit('SET_PREVIOUS_PAGE', response.previous) // Assuming pagination 'previous' URL
      } catch (error) {
        console.error('Error fetching books:', error)
      }
    }
  }
}
