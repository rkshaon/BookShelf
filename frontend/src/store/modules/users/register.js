// src/store/modules/users/register.js

import { registerUser } from '@/services/v1/userAPIService'

export default {
  state: {
    errors: null,
    successMessage: null,
    loading: false
  },
  getters: {
    registerError: (state) => state.errors,
    isLoading: (state) => state.loading,
    registerSuccess: (state) => state.successMessage
  },
  mutations: {
    SET_ERROR (state, error) {
      state.errors = error
    },
    SET_LOADING (state, loading) {
      state.loading = loading
    },
    SET_SUCCESS_MESSAGE (state, message) {
      state.successMessage = message
    }
  },
  actions: {
    async register ({ commit }, userData) {
      commit('SET_LOADING', true)
      try {
        const response = await registerUser(userData)
        console.log(response)
        console.log(response.data)
        commit('SET_SUCCESS_MESSAGE', response.message)
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
        commit('SET_LOADING', false)
      }
    }
  }
}
