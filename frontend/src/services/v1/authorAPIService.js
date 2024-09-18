// src/services/v1/authorAPIService.js

import axios from 'axios'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'author'
const version = 'v1'

export default {
  async fetchV1AuthorDetails (id = null) {
    const URL = `${API_BASE_URL}/${content}/${version}/${id}/`
    console.log('Author Details API:', URL)

    try {
      const response = await axios.get(URL)
      return response.data
    } catch (error) {
      console.error('Error fetching author:', error)
      throw error
    }
  }
}
