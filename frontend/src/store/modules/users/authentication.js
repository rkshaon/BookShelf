// src/store/modules/users/authentication.js

import { loginV1User } from '@/services/v1/userAPIService'
import {
  getAccessToken, getRefreshToken, setAccessToken, setRefreshToken,
  removeAccessToken, removeRefreshToken
} from '@/helpers/getToken'

export default {
  state: {
    errors: null,
    loading: false,
    accessToken: getAccessToken(),
    refreshToken: null
  },
  getters: {
    loginError: (state) => state.errors,
    isLoading: (state) => state.loading,
    isAuthenticated: (state) => !!state.accessToken
  },
  mutations: {
    SET_ERROR (state, error) {
      state.errors = error
    },
    SET_LOADING (state, loading) {
      state.loading = loading
    },
    SET_TOKEN (state, token) {
      state.accessToken = token.access
      state.refreshToken = token.refresh
      // localStorage.setItem('accessToken', token.access)
      // localStorage.setItem('refreshToken', token.refresh)
      setAccessToken(token.access)
      setRefreshToken(token.refresh)
    },
    CLEAR_AUTH (state) {
      state.accessToken = null
      state.refreshToken = null
      // localStorage.removeItem('accessToken')
      // localStorage.removeItem('refreshToken')
      removeAccessToken()
      removeRefreshToken()
    }
  },
  actions: {
    async login ({ commit }, credentials) {
      console.log('Before login')
      console.log(getAccessToken())
      console.log(getRefreshToken())
      commit('SET_LOADING', true)
      try {
        const response = await loginV1User(credentials)
        commit('SET_TOKEN', response)
        commit('SET_ERROR', null)
      } catch (error) {
        const errorMessages = []
        for (const [field, messages] of Object.entries(error)) {
          messages.forEach((message) => {
            console.log(`${field}: ${message}`)
            errorMessages.push(message)
          })
        }
        console.log(errorMessages)
        commit('SET_ERROR', errorMessages)
      } finally {
        commit('SET_LOADING', false)
      }
      console.log('After login')
      console.log(getAccessToken())
      console.log(getRefreshToken())
    },
    async logout ({ commit }) {
      console.log('Before logout')
      console.log(getAccessToken())
      console.log(getRefreshToken())
      commit('CLEAR_AUTH')
      console.log('After logout')
      console.log(getAccessToken())
      console.log(getRefreshToken())
    }
  }
}
