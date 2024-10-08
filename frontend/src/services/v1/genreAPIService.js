// src/services/v1/genreAPIService.js

import axios from 'axios'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'genre'
const version = 'v1'

export default {
  async fetchV1GenreDetails (id = null) {
    const URL = `${API_BASE_URL}/book/${version}/${content}/${id}/`
    console.log('Genre Details API:', URL)

    try {
      const response = await axios.get(URL)
      return response.data
    } catch (error) {
      console.error('Error fetching genre:', error)
      throw error
    }
  }
}
