import Vuex from 'vuex'

import books from '@/store/modules/books'
import bookDetails from '@/store/modules/bookDetails'

export default new Vuex.Store({
  modules: {
    books,
    bookDetails
  }
})
