// src/services/v1/bookAPIService.js

import axios from 'axios'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL

export default {
  async fetchV1Books (page = 1, pageSize = 8) {
    page = page ?? 1
    pageSize = pageSize ?? 8
    console.log(page, pageSize)

    const URL = `${API_BASE_URL}/book/v1/?page_size=${pageSize}&page=${page}`

    try {
      const response = await axios.get(URL)
      return response.data
    } catch (error) {
      console.error('Error fetching books:', error)
      throw error
    }
  }
}
