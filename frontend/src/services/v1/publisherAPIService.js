// src/services/v1/publisherAPIService.js

import api from '@/services/axiosInstance'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'publisher'
const version = 'v1'

export const searchV1Publishers = async (
  query = '',
  page = 1,
  pageSize = 8
) => {
  page = page ?? 1
  pageSize = pageSize ?? 10

  const URL = `${API_BASE_URL}/${content}/${version}/?search=${encodeURIComponent(
    query
  )}`

  console.log('Search Publisher API:', URL)

  try {
    const response = await api.get(URL)
    return response.data
  } catch (error) {
    console.error('Error searching publishers:', error)
    throw error
  }
}
