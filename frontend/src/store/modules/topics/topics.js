// src/store/modules/topics/topics.js

import { searchV1Topics } from '@/services/v1/topicAPIService'

export default {
  state: {
    topics: [],
    searchQuery: ''
  },
  getters: {
    topics: (state) => state.topics
  },
  mutations: {
    SET_TOPICS (state, topics) {
      state.topics = topics
    },
    SET_SEARCH_QUERY (state, query) {
      state.searchQuery = query
    }
  },
  actions: {
    async searchTopics (
      { commit, state },
      { query, page = 1, pageSize = 8 } = {}
    ) {
      commit('SET_SEARCH_QUERY', query)
      try {
        const response = await searchV1Topics(query, page, pageSize)
        commit('SET_TOPICS', response.results)
      } catch (error) {
        console.error("Error searching topics:", error);
      }
    }
  }
}
