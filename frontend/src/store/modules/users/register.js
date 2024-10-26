// src/store/modules/users/register.js

import userAPIService from '@/services/v1/userAPIService'

// Initial state
const state = {
  user: null,
  error: null,
  loading: false
}

// Getters
const getters = {
  user: (state) => state.user,
  error: (state) => state.error,
  loading: (state) => state.loading
}

// Actions
const actions = {
  async register ({ commit }, userData) {
    commit('setLoading', true)
    try {
      const response = await userAPIService.registerUser(userData)
      commit('setUser', response.data)
      commit('setError', null)
    } catch (error) {
      commit('setError', error.response.data.message)
    } finally {
      commit('setLoading', false)
    }
  }
}

// Mutations
const mutations = {
  setUser (state, user) {
    state.user = user
  },
  setError (state, error) {
    state.error = error
  },
  setLoading (state, loading) {
    state.loading = loading
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
