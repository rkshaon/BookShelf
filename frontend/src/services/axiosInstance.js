import axios from 'axios'
import store from '@/store'
import { useToast } from 'vue-toastification'
import {
  getAccessToken,
  getRefreshToken,
  setAccessToken
} from '@/helpers/getToken'

const api = axios.create({
  baseURL: process.env.VUE_APP_BACKEND_URL
})

// Request Interceptor: Conditionally attach the access token to headers
api.interceptors.request.use(
  (config) => {
    console.log('URL', config.url)
    if (config.requiresAuth) {
      // Check for custom requiresAuth flag
      const token = getAccessToken()
      if (token) {
        config.headers.Authorization = `Bearer ${token}`
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
          const response = await axios.post(
            `${process.env.VUE_APP_BACKEND_URL}/user/v1/refresh`,
            {
              refresh: refreshToken
            }
          )
          const newAccessToken = response.data.access

          setAccessToken(newAccessToken)
          originalRequest.headers.Authorization = `Bearer ${newAccessToken}`

          return api(originalRequest)
        } else {
          throw new Error('No refresh token available')
        }
      } catch (refreshError) {
        const toast = useToast()
        toast.error('Session expired, login again!')
        console.log('Invalid Refresh Token')
        store.dispatch('logout') // Optional: dispatch logout if refresh fails
        return Promise.reject(refreshError)
      }
    }

    return Promise.reject(error)
  }
)

export default api
