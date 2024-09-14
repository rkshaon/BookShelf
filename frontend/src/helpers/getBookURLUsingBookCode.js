export function getBookURLUsingBookCode (bookCode, baseURL) {
  const URL = `${baseURL}/media/books/${bookCode}.pdf`
  return URL
}
