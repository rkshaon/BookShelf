export function getBookURL (bookURL, baseURL) {
  console.log('book file: ', baseURL)
  const URL = `${baseURL}${bookURL}`
  return URL
}
