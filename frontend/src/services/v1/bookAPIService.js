// src/services/v1/bookAPIService.js

import axios from 'axios'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'book'
const version = 'v1'

export default {
  async fetchV1Books (page = 1, pageSize = 8, genre = null, topic = null) {
    page = page ?? 1
    pageSize = pageSize ?? 8
    let URL = `${API_BASE_URL}/${content}/${version}/?page_size=${pageSize}&page=${page}`

    if (genre) {
      URL += `&genre=${encodeURIComponent(genre)}`
    }

    if (topic) {
      URL += `&topic=${encodeURIComponent(topic)}`
    }
    console.log('Books API:', URL, page, pageSize)

    try {
      const response = await axios.get(URL)
      return response.data
    } catch (error) {
      console.error('Error fetching books:', error)
      throw error
    }
  },
  async fetchV1BookDetails (bookCode = null) {
    const URL = `${API_BASE_URL}/${content}/${version}/${bookCode}/`
    console.log('Book Details API:', URL)

    try {
      const response = await axios.get(URL)
      return response.data
    } catch (error) {
      console.error('Error fetching book:', error)
      throw error
    }
  },
  async searchV1Books (query = '', page = 1, pageSize = 8) {
    page = page ?? 1
    pageSize = pageSize ?? 8

    // Create URL for searching books
    const URL = `${API_BASE_URL}/${content}/${version}/?search=${encodeURIComponent(query)}&page_size=${pageSize}&page=${page}`
    console.log('Search Books API:', URL)

    try {
      const response = await axios.get(URL)
      return response.data
    } catch (error) {
      console.error('Error searching books:', error)
      throw error
    }
  }
}
