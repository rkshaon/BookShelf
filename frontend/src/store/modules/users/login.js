// src/store/modules/users/login.js

import { loginUser } from '@/services/v1/userAPIService'

export default {
  state: {
    errors: null,
    loading: false,
    accessToken: null,
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
    }
  },
  actions: {
    async login ({ commit }, credentials) {
      commit('SET_LOADING', true)
      try {
        const response = await loginUser(credentials)
        console.log(response)
        commit('SET_TOKEN', response)
        commit('SET_ERROR', null)
      } catch (error) {
        console.log(error)
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
    }
  }
}
// const state = {
//     user: null,
//     token: null,
//     error: null,
// };

// const getters = {
//     isAuthenticated: state => !!state.token,
//     user: state => state.user,
//     authError: state => state.error,
// };

// const actions = {
//     async login({ commit }, credentials) {
//         try {
//             const response = await axios.post('/api/login', credentials);
//             commit('setUser', response.data.user);
//             commit('setToken', response.data.token);
//         } catch (error) {
//             commit('setError', error.response.data.message);
//         }
//     },
//     logout({ commit }) {
//         commit('setUser', null);
//         commit('setToken', null);
//     }
// };

// const mutations = {
//     setUser(state, user) {
//         state.user = user;
//     },
//     setToken(state, token) {
//         state.token = token;
//     },
//     setError(state, error) {
//         state.error = error;
//     }
// };

// export default {
//     state,
//     getters,
//     actions,
//     mutations
// };
