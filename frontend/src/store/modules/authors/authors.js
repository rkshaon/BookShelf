// src/store/modules/authors/authorList.js

import { fetchV1Authors } from '@/services/v1/authorAPIService'

export default {
  state: {
    authors: [],
    nextPageUrl: null,
    previousPageUrl: null,
    pageSize: 8
  },
  getters: {
    authors: (state) => state.authors,
    nextPageUrl: (state) => state.nextPageUrl,
    previousPageUrl: (state) => state.previousPageUrl,
    currentPageSize: (state) => state.pageSize
  },
  mutations: {
    SET_AUTHORS (state, authors) {
      state.authors = authors
    },
    SET_NEXT_PAGE (state, url) {
      state.nextPageUrl = url
    },
    SET_PREVIOUS_PAGE (state, url) {
      state.previousPageUrl = url
    },
    SET_PAGE_SIZE (state, pageSize) {
      state.currentPageSize = pageSize
    }
  },
  actions: {
    async fetchAuthors ({ commit }, { page = 1, pageSize = 8 } = {}) {
      try {
        const response = await fetchV1Authors(page, pageSize)
        commit('SET_AUTHORS', response.results)
        commit('SET_NEXT_PAGE', response.next)
        commit('SET_PREVIOUS_PAGE', response.previous)
        commit('SET_PAGE_SIZE', pageSize)
      } catch (error) {
        console.error('Error fetching authors:', error)
      }
    }
  }
}
