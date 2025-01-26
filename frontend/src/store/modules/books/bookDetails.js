// src/store/modules/bookDetails.js

import {
  fetchV1BookDetails,
  updateCoverPageV1Book
} from '@/services/v1/bookAPIService'

export default {
  state: {
    bookDetails: null,
    isLoadingBookDetails: false,
    bookDetailsError: null
  },
  getters: {
    getBookDetails: (state) => state.bookDetails,
    isBookLoading: (state) => state.isLoadingBookDetails,
    bookDetailsError: (state) => state.bookDetailsError
  },
  mutations: {
    SET_BOOK_DETAILS (state, bookDetails) {
      state.bookDetails = bookDetails
    },
    SET_BOOK_LOADING (state, isLoading) {
      state.isLoadingBookDetails = isLoading
    },
    SET_BOOK_ERROR (state, error) {
      state.bookDetailsError = error
    }
  },
  actions: {
    async fetchBookDetails ({ commit }, bookCode) {
      commit('SET_BOOK_LOADING', true)
      commit('SET_BOOK_ERROR', null)
      try {
        const bookDetails = await fetchV1BookDetails(bookCode)
        commit('SET_BOOK_DETAILS', bookDetails)
      } catch (error) {
        const errorMessages = []
        for (const [key, value] of Object.entries(error.response.data)) {
          errorMessages.push(value)
          console.log(`Book fetch... ${key}: ${value}`)
        }
        commit('SET_BOOK_ERROR', errorMessages)
      } finally {
        commit('SET_BOOK_LOADING', false)
      }
    },
    async updateBookCoverPage ({ commit }, { data, bookCode }) {
      commit('SET_BOOK_LOADING', true)
      commit('SET_BOOK_ERROR', null)
      try {
        const bookDetails = await updateCoverPageV1Book(data, bookCode)
        commit('SET_BOOK_DETAILS', bookDetails)
      } catch (error) {
        const errorMessages = []
        for (const [key, value] of Object.entries(error.response.data)) {
          errorMessages.push(value)
          console.log(`Book fetch... ${key}: ${value}`)
        }
        commit('SET_BOOK_ERROR', errorMessages)
      } finally {
        commit('SET_BOOK_LOADING', false)
      }
    }
  }
}
