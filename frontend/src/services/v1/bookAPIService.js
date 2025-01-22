// src/services/v1/bookAPIService.js

import api from '@/services/axiosInstance'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL
const content = 'book'
const version = 'v1'

export const fetchV1Books = async (
  page = 1,
  pageSize = 8,
  genre = null,
  topic = null
) => {
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
    const response = await api.get(URL)
    return response.data
  } catch (error) {
    console.error('Error fetching books:', error)
    throw error
  }
}

export const fetchV1BookDetails = async (bookCode = null) => {
  const URL = `${API_BASE_URL}/${content}/${version}/${bookCode}/`
  console.log('Book Details API:', URL)

  try {
    const response = await api.get(URL)
    return response.data
  } catch (error) {
    console.error('Error fetching book:', error)
    throw error
  }
}

export const searchV1Books = async (query = '', page = 1, pageSize = 8) => {
  page = page ?? 1
  pageSize = pageSize ?? 8

  // const URL = `${API_BASE_URL}/${content}/${version}/?search=${encodeURIComponent(query)}&page_size=${pageSize}&page=${page}`
  const URL = `${API_BASE_URL}/${content}/${version}/?search=${encodeURIComponent(
    query
  )}`

  console.log('Search Books API:', URL)

  try {
    const response = await api.get(URL)
    // console.log(response.data)
    return response.data
  } catch (error) {
    console.error('Error searching books:', error)
    throw error
  }
}

export const createV1Book = async (data) => {
  const URL = `${API_BASE_URL}/${content}/${version}/`
  try {
    const response = await api.post(URL, data)
    return response.data
  } catch (error) {
    console.error('Error creating book at service:', error)

    if (error.response && error.response.status === 403) {
      return { error: true, message: 'Permission denied to create an author' }
    }

    throw error
  }
}

export const updateCoverPageV1Book = async (data, bookCode = null) => {
  const URL = `${API_BASE_URL}/${content}/${version}/update-cover-page/${bookCode}/`
  try {
    const response = await api.patch(URL, data)
    return response.data
  } catch (error) {
    console.error('Error creating book at service:', error)

    if (error.response && error.response.status === 403) {
      return { error: true, message: 'Permission denied to create an author' }
    }

    throw error
  }
}
