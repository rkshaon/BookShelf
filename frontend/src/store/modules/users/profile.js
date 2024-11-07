// src/store/modules/users/profile.js

import {
  getUserProfile,
  editUserProfile
} from '@/services/v1/userAPIService'

export default {
  state: {
    user: {},
    loading: false,
    editFailed: false,
    errors: null
  },
  getters: {
    userProfile: (state) => state.user,
    isLoading: (state) => state.loading,
    isEditFailed: (state) => state.editFailed,
    editProfileError: (state) => state.errors
  },
  mutations: {
    SET_ERROR (state, error) {
      state.errors = error
    },
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
