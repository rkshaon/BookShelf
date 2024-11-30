// src/store/modules/publishers/publishers.js

import { searchV1Publishers } from '@/services/v1/publisherAPIService'

export default {
  state: {
    publishers: [],
    searchQuery: ''
  },
  getters: {
    publishers: (state) => state.publishers,
    searchQuery: (state) => state.searchQuery
  },
  mutations: {
    SET_PUBLISHERS (state, publishers) {
      state.publishers = publishers
    },
    SET_SEARCH_QUERY (state, query) {
      state.searchQuery = query
    }
  },
  actions: {
    async searchPublisher (
      { commit, state },
      { query, page = 1, pageSize = 8 } = {}
    ) {
      commit('SET_SEARCH_QUERY', query)
      try {
        const response = await searchV1Publishers(query, page, pageSize)
        commit('SET_PUBLISHERS', response.results)
      } catch (error) {
        console.error('Error searching books:', error)
      }
    }
  }
}
