// src/store/modules/books.js

import bookAPIService from '@/services/v1/bookAPIService'

export default {
  state: {
    books: [],
    nextPageUrl: null,
    previousPageUrl: null
  },
  getters: {
    allBooks: (state) => state.books,
    nextPage: (state) => state.nextPageUrl,
    previousPage: (state) => state.previousPageUrl
  },
  mutations: {
    SET_BOOKS (state, books) {
      state.books = books
    },
    SET_NEXT_PAGE (state, url) {
      state.nextPageUrl = url;
    },
    SET_PREVIOUS_PAGE (state, url) {
      state.previousPageUrl = url;
    }
  },
  actions: {
    async fetchBooks({ commit }, url = null) {      
      try {
        const response = await bookAPIService.fetchV1Books(url)
        commit('SET_BOOKS', response.results)
        commit('SET_NEXT_PAGE', response.next)
        commit('SET_PREVIOUS_PAGE', response.previous)
      } catch (error) {
        console.error('Error fetching books:', error)
      }
    }
  }
}
