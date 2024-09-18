// src/store/modules/bookDetails.js

import authorAPIService from "@/services/v1/authorAPIService";

const state = {
  authorDetails: null,
  isLoading: false,
  error: null,
};

const getters = {
  getAuthorDetails: (state) => state.authorDetails,
  isAuthorLoading: (state) => state.isLoading,
  authorDetailsError: (state) => state.error,
};

const actions = {
  async fetchAuthorDetails({ commit }, authorId) {
    commit("SET_LOADING", true);
    commit("SET_ERROR", null);
    try {
      const response = await authorAPIService.fetchV1AuthorDetails(authorId);
      commit("SET_AUTHOR_DETAILS", response.data);
    } catch (error) {
      commit("SET_ERROR", "Error fetching author details");
    } finally {
      commit("SET_LOADING", false);
    }
  },
};

const mutations = {
  SET_AUTHOR_DETAILS(state, author) {
    state.authorDetails = author;
  },
  SET_LOADING(state, isLoading) {
    state.isLoading = isLoading;
  },
  SET_ERROR(state, error) {
    state.error = error;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
