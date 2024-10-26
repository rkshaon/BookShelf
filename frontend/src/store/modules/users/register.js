// src/store/modules/users/register.js

import { registerUser } from '@/services/v1/userAPIService'

export default {
  state: {
    user: null,
    errors: null,
    successMessage: null,
    loading: false
  },
  getters: {
    user: (state) => state.user,
    registerError: (state) => state.errors,
    isLoading: (state) => state.loading
  },
  mutations: {
    setUser (state, user) {
      state.user = user
    },
    SET_ERROR (state, error) {
      state.errors = error
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
        commit('SET_ERROR', null)
      } catch (error) {
        const errorMessages = []
        for (const [field, messages] of Object.entries(error)) {
          messages.forEach((message) => {
            console.log(`${field}: ${message}`)
            errorMessages.push(message)
          })
        }
        commit('SET_ERROR', errorMessages)
      } finally {
        commit('setLoading', false)
      }
    }
  }
}
