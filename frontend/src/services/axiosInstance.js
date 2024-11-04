import axios from 'axios'
import store from '@/store'
import { getAccessToken, getRefreshToken, setAccessToken } from '@/utils/tokenUtils'

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL, // Your API base URL
})

// Request Interceptor: Conditionally attach the access token to headers
api.interceptors.request.use(
  (config) => {
    if (config.requiresAuth) { // Check for custom requiresAuth flag
      const token = getAccessToken() // Retrieve the access token
      if (token) {
        config.headers['Authorization'] = `Bearer ${token}`
      }
    }
    return config
  },
  (error) => Promise.reject(error)
)

// Response Interceptor for handling token expiration
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true // Prevent multiple retries

      try {
        const refreshToken = getRefreshToken()
        if (refreshToken) {
          const response = await axios.post(`${process.env.VUE_APP_API_URL}/auth/refresh`, {
            refresh: refreshToken,
          })
          const newAccessToken = response.data.access

          setAccessToken(newAccessToken)
          originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`

          return api(originalRequest) // Retry the original request with the new token
        } else {
          throw new Error('No refresh token available')
        }
      } catch (refreshError) {
        store.dispatch('auth/logout') // Optional: dispatch logout if refresh fails
        return Promise.reject(refreshError)
      }
    }

    return Promise.reject(error)
  }
)

export default api
