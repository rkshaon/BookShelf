// src/store/modules/users/profile.js

import { getUserProfile } from '@/services/v1/userAPIService'

export default {
  state: {
    user: null,
    loading: false
  },
  getters: {
    userProfile: (state) => state.user,
    isLoading: (state) => state.loading
  },
  mutations: {
    SET_USER (state, user) {
      state.user = user
    },
    SET_LOADING (state, loading) {
      state.loading = loading
    }
  },
  actions: {
    async fetchUserProfile ({ commit }, token) {
      commit('SET_LOADING', true)
      try {
        const response = await getUserProfile(token)
        commit('SET_USER', response)
      } catch (error) {
        console.log(error)
      } finally {
        commit('SET_LOADING', false)
      }
    }
  }
}
