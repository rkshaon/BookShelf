// src/services/v1/userAPIService.js

import axios from 'axios'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'user'
const version = 'v1'

// Register user
export const registerUser = async (userData) => {
  const URL = `${API_BASE_URL}/${content}/${version}/registration`
  console.log(URL)
  try {
    const response = await axios.post(URL, userData)
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
    const response = await axios.post(URL, credentials)
    return response.data
  } catch (error) {
    throw error.response.data
  }
}

// Get user profile
export const getUserProfile = async (token) => {
  try {
    const URL = `${API_BASE_URL}/${content}/${version}/profile`
    console.log(URL)
    const response = await axios.get(URL, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    return response.data
  } catch (error) {
    throw error.response.data
  }
}
