// src/services/v1/userAPIService.js

import api from '@/services/axiosInstance'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'user'
const version = 'v1'

// Register user
export const registerV1User = async (userData) => {
  const URL = `${API_BASE_URL}/${content}/${version}/registration`
  try {
    const response = await api.post(URL, userData)
    return response.data
  } catch (error) {
    throw error.response.data
  }
}

// Login user
export const loginV1User = async (credentials) => {
  try {
    const URL = `${API_BASE_URL}/${content}/${version}/login`
    const response = await api.post(URL, credentials)
    return response.data
  } catch (error) {
    throw error.response.data
  }
}

// Get user profile
export const getV1UserProfile = async () => {
  try {
    const URL = `${API_BASE_URL}/${content}/${version}/profile`
    const response = await api.get(URL, { requiresAuth: true })
    return response.data
  } catch (error) {
    throw error.response.data
  }
}

// Edit user profile
export const editV1UserProfile = async (userData) => {
  try {
    const URL = `${API_BASE_URL}/${content}/${version}/profile`
    const response = await api.put(URL, userData, { requiresAuth: true })
    return response.data
  } catch (error) {
    throw error.response.data
  }
}
