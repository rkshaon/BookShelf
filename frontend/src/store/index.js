import Vuex from 'vuex'

// book modules
import books from '@/store/modules/books/books'
import bookDetails from '@/store/modules/books/bookDetails'
import bookSearch from '@/store/modules/books/bookSearch'
// author modules
import authorDetails from '@/store/modules/authors/authorDetails'
import authors from '@/store/modules/authors/authors'
// genre modules
import genreDetails from '@/store/modules/genres/genreDetails'
// topic modules
import topicDetails from '@/store/modules/topics/topicDetails'
// user modules
import register from '@/store/modules/users/register'
import authentication from '@/store/modules/users/authentication'
import profile from '@/store/modules/users/profile'

export default new Vuex.Store({
  modules: {
    books,
    bookDetails,
    bookSearch,
    authorDetails,
    authors,
    genreDetails,
    topicDetails,
    register,
    authentication,
    profile
  }
})
