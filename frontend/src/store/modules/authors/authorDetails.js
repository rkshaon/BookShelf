// src/store/modules/bookDetails.js

import authorAPIService from '@/services/v1/authorAPIService'

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
      console.log('just testing')

      state.isLoading = isLoading
      console.log('loading value', state.isLoading)
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
        const response = await authorAPIService.fetchV1AuthorDetails(authorId)
        console.log('response:', response)
        commit('SET_AUTHOR_DETAILS', response)
      } catch (error) {
        commit('SET_ERROR', 'Error fetching author details')
      } finally {
        // console.log('loading...', this.state.isLoading)
        commit('SET_LOADING', false)
        //   console.log("loading...", this.state.isLoading)
      }
    }
  }

}
