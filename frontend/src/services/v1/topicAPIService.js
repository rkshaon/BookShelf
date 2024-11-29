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
