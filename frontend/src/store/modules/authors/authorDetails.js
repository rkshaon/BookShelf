// src/store/modules/bookDetails.js

import { fetchV1AuthorDetails } from '@/services/v1/authorAPIService'

export default {
  state: {
    authorDetails: null,
    isLoading: false,
    error: null
  },
  getters: {
    getAuthorDetails: (state) => state.authorDetails,
    isAuthorLoading: (state) => state.isLoading,
    authorDetailsError: (state) => state.error
  },
  mutations: {
    SET_AUTHOR_DETAILS (state, author) {
      state.authorDetails = author
    },
    SET_LOADING (state, isLoading) {
      state.isLoading = isLoading
    },
    SET_ERROR (state, error) {
      state.error = error
    }
  },
  actions: {
    async fetchAuthorDetails ({ commit }, authorId) {
      commit('SET_LOADING', true)
      commit('SET_ERROR', null)
      try {
        const response = await fetchV1AuthorDetails(authorId)
        commit('SET_AUTHOR_DETAILS', response)
      } catch (error) {
        const errorMessages = []
        for (const [key, value] of Object.entries(error.response.data)) {
          errorMessages.push(value)
          console.log(`Author fetch... ${key}: ${value}`)
        }
        commit('SET_ERROR', errorMessages)
      } finally {
        commit('SET_LOADING', false)
      }
    }
  }

}
