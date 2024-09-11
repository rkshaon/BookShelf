// src/store/modules/books.js

import bookAPIService from '@/services/v1/bookAPIService'

export default {
  state: {
    books: [],
    nextPageUrl: null,
    previousPageUrl: null
  },
  getters: {
    allBooks: (state) => state.books
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
    async fetchBooks ({ commit }) {
      try {
        console.log("it's working")

        const response = await bookAPIService.fetchV1Books()
        commit('SET_BOOKS', response.results) // Assuming 'results' contains the books array
        commit('SET_NEXT_PAGE', response.next) // Assuming pagination 'next' URL
        commit('SET_PREVIOUS_PAGE', response.previous) // Assuming pagination 'previous' URL
      } catch (error) {
        console.error('Error fetching books:', error)
      }
    }
  }
}
