// src/services/v1/topicAPIService.js

import api from '@/services/axiosInstance'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'topic'
const version = 'v1'

export const fetchV1TopicDetails = async (id = null) => {
  const URL = `${API_BASE_URL}/book/${version}/${content}/${id}/`
  console.log('topic Details API:', URL)

  try {
    const response = await api.get(URL)
    return response.data
  } catch (error) {
    console.error('Error fetching topic:', error)
    throw error
  }
}

export const searchV1Topics = async (query = '', page = 1, pageSize = 8) => {
  page = page ?? 1
  pageSize = pageSize ?? 10

  const URL = `${API_BASE_URL}/book/${version}/${content}/?search=${encodeURIComponent(
    query
  )}`

  try {
    const response = await api.get(URL)
    return response.data
  } catch (error) {
    console.error('Error searching Topics:', error)
    if (error.response && error.response.status === 403) {
      return { error: true, message: 'Permission denied to create an author' }
    }
    throw error
  }
}
