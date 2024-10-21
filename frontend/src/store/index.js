import Vuex from 'vuex'

import books from '@/store/modules/books/books'
import bookDetails from '@/store/modules/books/bookDetails'
import bookSearch from '@/store/modules/books/bookSearch'
import authorDetails from '@/store/modules/authors/authorDetails'
import genreDetails from '@/store/modules/genres/genreDetails'
import topicDetails from '@/store/modules/topics/topicDetails'

export default new Vuex.Store({
  modules: {
    books,
    bookDetails,
    bookSearch,
    authorDetails,
    genreDetails,
    topicDetails
  }
})
