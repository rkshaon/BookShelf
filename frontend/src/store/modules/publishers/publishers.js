// src/store/modules/publishers/publishers.js

import { searchV1Publishers } from '@/services/v1/publisherAPIService'

export default {
  state: {
    publishers: []
    // searchResults: [],
    // nextPageUrl: null,
    // previousPageUrl: null,
    // pageSize: 8,
    // searchQuery: "",
    // searchNextPageUrl: null,
    // searchPreviousPageUrl: null,
  },
  getters: {
    publishers: (state) => state.publishers,
    // searchResults: (state) => state.searchResults,
    // nextPageUrl: (state) => state.nextPageUrl,
    // previousPageUrl: (state) => state.previousPageUrl,
    // currentPageSize: (state) => state.pageSize,
    searchQuery: (state) => state.searchQuery
    // searchNextPageUrl: (state) => state.searchNextPageUrl,
    // searchPreviousPageUrl: (state) => state.searchPreviousPageUrl,
  },
  mutations: {
    SET_PUBLISHERS (state, publishers) {
      state.publishers = publishers
    },
    // SET_NEXT_PAGE(state, url) {
    //   state.nextPageUrl = url;
    // },
    // SET_PREVIOUS_PAGE(state, url) {
    //   state.previousPageUrl = url;
    // },
    // SET_PAGE_SIZE(state, pageSize) {
    //   state.currentPageSize = pageSize;
    // },
    // SET_SEARCH_RESULTS(state, results) {
    //   state.searchResults = results;
    // },
    SET_SEARCH_QUERY (state, query) {
      state.searchQuery = query
    }
    // SET_SEARCH_NEXT_PAGE(state, url) {
    //   state.searchNextPageUrl = url;
    // },
    // SET_SEARCH_PREVIOUS_PAGE(state, url) {
    //   state.searchPreviousPageUrl = url;
    // },
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
        // commit("SET_SEARCH_RESULTS", response.results);
        // commit("SET_SEARCH_NEXT_PAGE", response.next);
        // commit("SET_SEARCH_PREVIOUS_PAGE", response.previous);
        console.log('Search Books:', response.results)
        // console.log(state.publishers)
      } catch (error) {
        console.error('Error searching books:', error)
      }
    }
    // async searchNextPage({ dispatch, state }) {
    //   if (state.searchNextPageUrl) {
    //     const nextPageNumber = new URL(
    //       state.searchNextPageUrl
    //     ).searchParams.get("page");
    //     await dispatch("searchBooks", {
    //       query: state.searchQuery,
    //       page: nextPageNumber,
    //       pageSize: state.pageSize,
    //     });
    //   }
    // },
    // async searchPreviousPage({ dispatch, state }) {
    //   if (state.searchPreviousPageUrl) {
    //     const previousPageNumber = new URL(
    //       state.searchPreviousPageUrl
    //     ).searchParams.get("page");
    //     await dispatch("searchBooks", {
    //       query: state.searchQuery,
    //       page: previousPageNumber,
    //       pageSize: state.pageSize,
    //     });
    //   }
    // },
  }
}
