// src/store/modules/users/profile.js

import {
  getUserProfile,
  editUserProfile
} from '@/services/v1/userAPIService'

export default {
  state: {
    user: {},
    loading: false
  },
  getters: {
    userProfile: (state) => state.user,
    isLoading: (state) => state.loading
  },
  mutations: {
    SET_USER (state, user) {
      console.log('before', state.user)
      state.user = user
      console.log('after', state.user)
    },
    SET_LOADING (state, loading) {
      state.loading = loading
    }
  },
  actions: {
    async fetchUserProfile ({ commit }) {
      commit('SET_LOADING', true)
      try {
        const response = await getUserProfile()
        console.log('Fetch User', response)
        commit('SET_USER', response)
      } catch (error) {
        console.log(error)
      } finally {
        commit('SET_LOADING', false)
      }
    },
    async editUserProfile ({ commit }, userData) {
      commit('SET_LOADING', true)
      try {
        const response = await editUserProfile(userData)
        console.log('Update User', response)
        commit('SET_USER', response)
      } catch (error) {
        console.log(error)
      } finally {
        commit('SET_LOADING', false)
      }
    }
  }
}
