// src/store/modules/genreDetails.js

import genreAPIService from '@/services/v1/genreAPIService'

export default {
  state: {
    genreDetails: null,
    isLoading: false,
    error: null
  },
  getters: {
    getGenreDetails: (state) => state.genreDetails,
    isGenreLoading: (state) => state.isLoading,
    genreDetailsError: (state) => state.error
  },
  mutations: {
    SET_GENRE_DETAILS (state, genre) {
      state.genreDetails = genre
    },
    SET_LOADING (state, isLoading) {
      state.isLoading = isLoading
    },
    SET_ERROR (state, error) {
      state.error = error
    }
  },
  actions: {
    async fetchGenreDetails ({ commit }, genreId) {
      commit('SET_LOADING', true)
      commit('SET_ERROR', null)
      try {
        const response = await genreAPIService.fetchV1GenreDetails(genreId)
        commit('SET_GENRE_DETAILS', response)
      } catch (error) {
        commit('SET_ERROR', 'Error fetching genre details')
      } finally {
        commit('SET_LOADING', false)
      }
    }
  }
}
