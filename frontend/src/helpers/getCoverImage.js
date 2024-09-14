export function getCoverImage (coverImage, baseURL) {
  console.log('cover file: ', baseURL)
  const fallbackImage = '/book/default-cover-image.jpg'
  const imageURL = coverImage ? `${baseURL}${coverImage}` : `${fallbackImage}`
  return imageURL
}
