// src/store/modules/books/bookSearch.js

import bookAPIService from '@/services/v1/bookAPIService'

export default {
  state: {
    books: [],
    searchResults: [],
    nextPageUrl: null,
    previousPageUrl: null,
    pageSize: 8,
    searchQuery: '',
    searchNextPageUrl: null,
    searchPreviousPageUrl: null
  },
  getters: {
    allBooks: (state) => state.books,
    searchResults: (state) => state.searchResults,
    nextPageUrl: (state) => state.nextPageUrl,
    previousPageUrl: (state) => state.previousPageUrl,
    currentPageSize: (state) => state.pageSize,
    searchQuery: (state) => state.searchQuery,
    searchNextPageUrl: (state) => state.searchNextPageUrl,
    searchPreviousPageUrl: (state) => state.searchPreviousPageUrl
  },
  mutations: {
    SET_BOOKS (state, books) {
      state.books = books
    },
    SET_NEXT_PAGE (state, url) {
      state.nextPageUrl = url
    },
    SET_PREVIOUS_PAGE (state, url) {
      state.previousPageUrl = url
    },
    SET_PAGE_SIZE (state, pageSize) {
      state.currentPageSize = pageSize
    },
    SET_SEARCH_RESULTS (state, results) {
      state.searchResults = results
    },
    SET_SEARCH_QUERY (state, query) {
      state.searchQuery = query
    },
    SET_SEARCH_NEXT_PAGE (state, url) {
      state.searchNextPageUrl = url
    },
    SET_SEARCH_PREVIOUS_PAGE (state, url) {
      state.searchPreviousPageUrl = url
    }
  },
  actions: {
    async fetchBooks (
      { commit },
      { page = 1, pageSize = 8, genre = null, topic = null } = {}
    ) {
      try {
        const response = await bookAPIService.fetchV1Books(
          page,
          pageSize,
          genre,
          topic
        )
        commit('SET_BOOKS', response.results)
        commit('SET_NEXT_PAGE', response.next)
        commit('SET_PREVIOUS_PAGE', response.previous)
        commit('SET_PAGE_SIZE', pageSize)
      } catch (error) {
        console.error('Error fetching books:', error)
      }
    },
    async searchBooks (
      { commit, state },
      { query, page = 1, pageSize = 8 } = {}
    ) {
      commit('SET_SEARCH_QUERY', query)
      try {
        const response = await bookAPIService.searchV1Books(
          query,
          page,
          pageSize
        )
        commit('SET_SEARCH_RESULTS', response.results)
        commit('SET_SEARCH_NEXT_PAGE', response.next)
        commit('SET_SEARCH_PREVIOUS_PAGE', response.previous)
      } catch (error) {
        console.error('Error searching books:', error)
      }
    },
    async searchNextPage ({ dispatch, state }) {
      if (state.searchNextPageUrl) {
        const nextPageNumber = new URL(
          state.searchNextPageUrl
        ).searchParams.get('page')
        await dispatch('searchBooks', {
          query: state.searchQuery,
          page: nextPageNumber,
          pageSize: state.pageSize
        })
      }
    },
    async searchPreviousPage ({ dispatch, state }) {
      if (state.searchPreviousPageUrl) {
        const previousPageNumber = new URL(
          state.searchPreviousPageUrl
        ).searchParams.get('page')
        await dispatch('searchBooks', {
          query: state.searchQuery,
          page: previousPageNumber,
          pageSize: state.pageSize
        })
      }
    }
  }
}
