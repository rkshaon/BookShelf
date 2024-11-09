// src/store/modules/authors/authorList.js

import {
  fetchV1Authors,
  createV1Author
} from '@/services/v1/authorAPIService'

export default {
  state: {
    authors: [],
    nextPageUrl: null,
    previousPageUrl: null,
    pageSize: 10,
    totalCount: 0,
    loading: false
  },
  getters: {
    authors: (state) => state.authors,
    nextPageUrl: (state) => state.nextPageUrl,
    previousPageUrl: (state) => state.previousPageUrl,
    currentAuthorPageSize: (state) => state.pageSize,
    totalAuthorCount: (state) => state.totalCount,
    isAuthorLoading: (state) => state.loading
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
      state.currentAuthorPageSize = pageSize
    },
    SET_TOTAL_COUNT (state, totalCount) {
      state.totalCount = totalCount
    },
    SET_LOADING (state, loading) {
      state.loading = loading
    }
  },
  actions: {
    async fetchAuthors ({ commit }, { page = 1, pageSize = 10 } = {}) {
      commit('SET_LOADING', true)
      try {
        const response = await fetchV1Authors(page, pageSize)
        commit('SET_AUTHORS', response.results)
        commit('SET_NEXT_PAGE', response.next)
        commit('SET_PREVIOUS_PAGE', response.previous)
        commit('SET_PAGE_SIZE', pageSize)
        commit('SET_TOTAL_COUNT', response.count)
      } catch (error) {
        console.error('Error fetching authors:', error)
      } finally {
        commit('SET_LOADING', false)
      }
    },
    async createAuthor ({ commit }, author) {
      try {
        const response = await createV1Author(author)
        return response
      } catch (error) {
        console.error('Error creating author:', error)
        throw error
      }
    }
  }
}
