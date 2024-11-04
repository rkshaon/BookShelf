// src/services/v1/userAPIService.js

// import axios from 'axios'

import { getAccessToken } from '@/helpers/getToken'
import api from '@/services/axiosInstance'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'user'
const version = 'v1'

// Register user
export const registerUser = async (userData) => {
  const URL = `${API_BASE_URL}/${content}/${version}/registration`
  console.log(URL)
  try {
    const response = await api.post(URL, userData)
    return response.data
  } catch (error) {
    throw error.response.data
  }
}

// Login user
export const loginUser = async (credentials) => {
  try {
    const URL = `${API_BASE_URL}/${content}/${version}/login`
    console.log(URL)
    const response = await api.post(URL, credentials)
    return response.data
  } catch (error) {
    throw error.response.data
  }
}

// Get user profile
export const getUserProfile = async () => {
  try {
    const URL = `${API_BASE_URL}/${content}/${version}/profile`
    const token = getAccessToken()
    console.log('URL', URL)
    const response = await api.get(URL, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    return response.data
  } catch (error) {
    throw error.response.data
  }
}
