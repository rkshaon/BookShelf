// src/services/v1/bookAPIService.js

import axios from 'axios'

// const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const API_BASE_URL = 'http://localhost:8001'

console.log('url', API_BASE_URL)

export default {
  async fetchV1Books (url = `${API_BASE_URL}/book/v1/`) {
    try {
      const response = await axios.get(url)
      console.log(response.data)

      return response.data
    } catch (error) {
      console.error('Error fetching books:', error)
      throw error
    }
  }
}
