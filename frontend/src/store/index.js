import Vuex from 'vuex'

// book modules
import books from '@/store/modules/books/books'
import bookDetails from '@/store/modules/books/bookDetails'
import bookSearch from '@/store/modules/books/bookSearch'
// publisher modules
import publishers from '@/store/modules/publishers/publishers'
// author modules
import authorDetails from '@/store/modules/authors/authorDetails'
import authors from '@/store/modules/authors/authors'
// genre modules
import genres from '@/store/modules/genres/genres'
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
    publishers,
    authorDetails,
    authors,
    genres,
    genreDetails,
    topicDetails,
    register,
    authentication,
    profile
  }
})
