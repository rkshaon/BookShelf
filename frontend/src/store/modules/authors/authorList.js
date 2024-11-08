// src/store/modules/authors/authorList.js

import { fetchV1Authors } from '@/services/v1/authorAPIService'

export default {
  state: {
    authors: [],
    isLoading: false,
    error: null
  },
  getters: {
    getAuthors: (state) => state.authors,
    isAuthorsLoading: (state) => state.isLoading,
    authorsError: (state) => state.error
  },
  mutations: {
    SET_AUTHORS (state, authors) {
      state.authors = authors
    },
    SET_LOADING (state, isLoading) {
      state.isLoading = isLoading
    },
    SET_ERROR (state, error) {
      state.error = error
    }
  },
  actions: {
    async fetchAuthors ({ commit }) {
      commit('SET_LOADING', true)
      commit('SET_ERROR', null)
      try {
        const response = await fetchV1Authors()
        commit('SET_AUTHORS', response)
      } catch (error) {
        const errorMessages = []
        for (const [key, value] of Object.entries(error.response.data)) {
          errorMessages.push(value)
          console.log(`Authors fetch... ${key}: ${value}`)
        }
        commit('SET_ERROR', errorMessages)
      } finally {
        commit('SET_LOADING', false)
      }
    }
  }
}
