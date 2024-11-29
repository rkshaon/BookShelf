// src/store/modules/genres/genres.js

import {
  searchV1Genres
} from '@/services/v1/genreAPIService'

export default {
  state: {
    genres: [],
    searchQuery: ''
  },
  getters: {
    genres: (state) => state.genres
  },
  mutations: {
    SET_GENRES (state, genres) {
      state.genres = genres
    },
    SET_SEARCH_QUERY (state, query) {
      state.searchQuery = query
    }
  },
  actions: {
    async searchGenres (
      { commit, state },
      { query, page = 1, pageSize = 8 } = {}
    ) {
      commit('SET_SEARCH_QUERY', query)
      try {
        const response = await searchV1Genres(query, page, pageSize)
        commit('SET_GENRES', response.results)
      } catch (error) {
        console.error('Error searching genres:', error)
      }
    }
  }
}
