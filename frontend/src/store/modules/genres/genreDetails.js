// src/store/modules/genreDetails.js

import { fetchV1GenreDetails } from '@/services/v1/genreAPIService'

export default {
  state: {
    genreDetails: null,
    isLoading: false,
    errors: null
  },
  getters: {
    getGenreDetails: (state) => state.genreDetails,
    isGenreLoading: (state) => state.isLoading,
    genreDetailsError: (state) => state.errors
  },
  mutations: {
    SET_GENRE_DETAILS (state, genre) {
      state.genreDetails = genre
    },
    SET_LOADING (state, isLoading) {
      state.isLoading = isLoading
    },
    SET_ERROR (state, error) {
      state.errors = error
    }
  },
  actions: {
    async fetchGenreDetails ({ commit }, genreId) {
      commit('SET_LOADING', true)
      commit('SET_ERROR', null)
      try {
        const response = await fetchV1GenreDetails(genreId)
        commit('SET_GENRE_DETAILS', response)
      } catch (error) {
        const errorMessages = []
        for (const [key, value] of Object.entries(error.response.data)) {
          errorMessages.push(value)
          console.log(`Genre fetch... ${key}: ${value}`)
        }
        commit('SET_ERROR', errorMessages)
      } finally {
        commit('SET_LOADING', false)
      }
    }
  }
}
