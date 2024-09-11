// src/services/v1/bookAPIService.js

import axios from 'axios'

const API_BASE_URL = process.env.VUE_APP_API_BASE_URL

export default {
  async fetchV1Books (url = `${API_BASE_URL}/books/v1/`) {
    try {
      const response = await axios.get(url)
      return response.data
    } catch (error) {
      console.error('Error fetching books:', error)
      throw error
    }
  }
}
