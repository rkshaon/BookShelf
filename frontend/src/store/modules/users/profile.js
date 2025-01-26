// src/store/modules/users/profile.js

import {
  getV1UserProfile,
  editV1UserProfile
} from '@/services/v1/userAPIService'

export default {
  state: {
    user: {},
    loading: false,
    editFailed: false,
    editSuccessMessage: null,
    errors: null,
    isAdmin: null
  },
  getters: {
    userProfile: (state) => state.user,
    isLoading: (state) => state.loading,
    isEditFailed: (state) => state.editFailed,
    editProfileError: (state) => state.errors,
    editSuccessMessage: (state) => state.editSuccessMessage,
    isAdmin: (state) => state.isAdmin
  },
  mutations: {
    SET_ERROR (state, error) {
      state.errors = error
    },
    SET_USER (state, user) {
      state.user = user
    },
    SET_LOADING (state, loading) {
      state.loading = loading
    },
    SET_EDIT_SUCCESS_MESSAGE (state, success) {
      state.editSuccessMessage = success
    },
    CLEAR_SUCCESS_MESSAGE (state) {
      state.editSuccessMessage = null
    },
    CLEAR_PROFILE_DATA (state) {
      state.user = {}
    },
    SET_IS_ADMIN (state, role) {
      if (role === 1) {
        state.isAdmin = true
      } else {
        state.isAdmin = false
      }
    }
  },
  actions: {
    async fetchUserProfile ({ commit }) {
      commit('SET_LOADING', true)
      try {
        const response = await getV1UserProfile()
        commit('SET_USER', response)
        commit('SET_IS_ADMIN', response.role)
      } catch (error) {
        console.log(error)
      } finally {
        commit('SET_LOADING', false)
      }
    },
    async editUserProfile ({ commit }, userData) {
      commit('SET_LOADING', true)
      try {
        const response = await editV1UserProfile(userData)
        commit('SET_USER', response)
        commit('SET_EDIT_SUCCESS_MESSAGE', 'Profile updated successfully')
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
    },
    clearProfileData ({ commit }) {
      commit('CLEAR_PROFILE_DATA')
    },
    clearSuccessMessage ({ commit }) {
      commit('CLEAR_SUCCESS_MESSAGE')
    }
  }
}
