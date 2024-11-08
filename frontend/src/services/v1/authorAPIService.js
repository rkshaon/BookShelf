// src/services/v1/authorAPIService.js

import api from '@/services/axiosInstance'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'author'
const version = 'v1'

export const fetchV1AuthorDetails = async (id = null) => {
  const URL = `${API_BASE_URL}/${content}/${version}/${id}/`
  try {
    const response = await api.get(URL)
    return response.data
  } catch (error) {
    console.error('Error fetching author:', error)
    throw error
  }
}

export const fetchV1Authors = async () => {
  const URL = `${API_BASE_URL}/${content}/${version}/`
  try {
    const response = await api.get(URL, { requireAuth: true })
    return response.data
  } catch (error) {
    console.error('Error fetching authors:', error)
    throw error
  }
}
