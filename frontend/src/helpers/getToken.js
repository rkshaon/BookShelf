// get access token from localStorage
export function getAccessToken () {
  return localStorage.getItem('accessToken')
}

// get refresh token from localStorage
export function getRefreshToken () {
  return localStorage.getItem('refreshToken')
}

// set access token to localStorage
export function setAccessToken (token) {
  localStorage.setItem('accessToken', token)
}

// set refresh token to localStorage
export function setRefreshToken (token) {
  localStorage.setItem('refreshToken', token)
}

// remove access token from localStorage
export function removeAccessToken () {
  localStorage.removeItem('accessToken')
}

// remove refresh token from localStorage
export function removeRefreshToken () {
  localStorage.removeItem('refreshToken')
}

export default {
  getAccessToken,
  getRefreshToken,
  setAccessToken,
  setRefreshToken,
  removeAccessToken,
  removeRefreshToken
}
