// src/services/v1/genreAPIService.js

import api from '@/services/axiosInstance'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'genres'
const version = 'v1'

export const fetchV1GenreDetails = async (id = null) => {
  const URL = `${API_BASE_URL}/book/${version}/${content}/${id}/`
  console.log('Genre Details API:', URL)

  try {
    const response = await api.get(URL)
    return response.data
  } catch (error) {
    console.error('Error fetching genre:', error)
    throw error
  }
}

export const searchV1Genres = async (query = '', page = 1, pageSize = 8) => {
  page = page ?? 1
  pageSize = pageSize ?? 10

  const URL = `${API_BASE_URL}/book/${version}/${content}/?search=${encodeURIComponent(
    query
  )}`

  try {
    const response = await api.get(URL)
    return response.data
  } catch (error) {
    console.error('Error searching Genres:', error)
    if (error.response && error.response.status === 403) {
      return { error: true, message: 'Permission denied to create an author' }
    }
    throw error
  }
}
