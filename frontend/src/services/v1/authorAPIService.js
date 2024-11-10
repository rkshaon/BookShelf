// src/services/v1/authorAPIService.js

import api from '@/services/axiosInstance'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'author'
const version = 'v1'

export const fetchV1AuthorDetails = async (id = null) => {
  const URL = `${API_BASE_URL}/${content}/${version}/${id}/`
  try {
    const response = await api.get(URL)
    return response.data
  } catch (error) {
    console.error('Error fetching author:', error)
    throw error
  }
}

export const fetchV1Authors = async (
  page = 1,
  pageSize = 10
) => {
  page = page ?? 1
  pageSize = pageSize ?? 10
  const URL = `${API_BASE_URL}/${content}/${version}/?page_size=${pageSize}&page=${page}`
  try {
    const response = await api.get(URL, { requireAuth: true })
    return response.data
  } catch (error) {
    console.error('Error fetching authors:', error)
    throw error
  }
}

export const createV1Author = async (data) => {
  const URL = `${API_BASE_URL}/${content}/${version}/`
  try {
    const response = await api.post(URL, data)
    return response.data
  } catch (error) {
    console.error('Error creating author:', error)
    throw error
  }
}
