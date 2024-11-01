export function getProfileImage (profileImage, baseURL) {
  console.log('cover file: ', baseURL)
  const fallbackImage = 'https://via.placeholder.com/150'
  const imageURL = profileImage
    ? `${baseURL}${profileImage}`
    : `${fallbackImage}`
  return imageURL
}
