// get access token from localStorage
export function getAccessToken () {
  return localStorage.getItem('accessToken')
}

// get refresh token from localStorage
export function getRefreshToken () {
  return localStorage.getItem('refreshToken')
}

export default {
  getAccessToken,
  getRefreshToken
}
