// src/store/modules/topicDetails.js

import topicAPIService from '@/services/v1/topicAPIService'

export default {
  state: {
    topicDetails: null,
    isLoading: false,
    errors: null
  },
  getters: {
    getTopicDetails: (state) => state.topicDetails,
    isTopicLoading: (state) => state.isLoading,
    topicDetailsError: (state) => state.errors
  },
  mutations: {
    SET_TOPIC_DETAILS (state, topic) {
      state.topicDetails = topic
    },
    SET_LOADING (state, isLoading) {
      state.isLoading = isLoading
    },
    SET_ERROR (state, error) {
      state.errors = error
    }
  },
  actions: {
    async fetchTopicDetails ({ commit }, topicId) {
      commit('SET_LOADING', true)
      commit('SET_ERROR', null)
      try {
        const response = await topicAPIService.fetchV1TopicDetails(topicId)
        commit('SET_TOPIC_DETAILS', response)
      } catch (error) {
        const errorMessages = []
        for (const [key, value] of Object.entries(error.response.data)) {
          errorMessages.push(value)
          console.log(`Topic fetch... ${key}: ${value}`)
        }
        commit('SET_ERROR', errorMessages)
      } finally {
        commit('SET_LOADING', false)
      }
    }
  }
}
