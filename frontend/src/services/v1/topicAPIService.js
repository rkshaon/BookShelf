// src/services/v1/topicAPIService.js

import axios from 'axios'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'topic'
const version = 'v1'

export default {
  async fetchV1TopicDetails (id = null) {
    const URL = `${API_BASE_URL}/book/${version}/${content}/${id}/`
    console.log('topic Details API:', URL)

    try {
      const response = await axios.get(URL)
      return response.data
    } catch (error) {
      console.error('Error fetching topic:', error)
      throw error
    }
  }
}
