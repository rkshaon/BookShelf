// src/store/modules/users/register.js

import { registerUser } from '@/services/v1/userAPIService'

export default {
  state: {
    user: null,
    error: null,
    loading: false
  },
  getters: {
    user: (state) => state.user,
    error: (state) => state.error,
    loading: (state) => state.loading
  },
  mutations: {
    setUser (state, user) {
      state.user = user
    },
    setError (state, error) {
      state.error = error
    },
    setLoading (state, loading) {
      state.loading = loading
    }
  },
  actions: {
    async register ({ commit }, userData) {
      commit('setLoading', true)
      try {
        const response = await registerUser(userData)
        commit('setUser', response.data)
        commit('setError', null)
      } catch (error) {
        commit('setError', error.response.data.message)
      } finally {
        commit('setLoading', false)
      }
    }
  }
}
