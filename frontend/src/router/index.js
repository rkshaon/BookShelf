import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/HomePage.vue')
  },
  {
    path: '/book/:book_code',
    name: 'BookDetails',
    component: () => import('@/pages/books/BookDetailsPage.vue')
  },
  // { path: "/book/:book_code/view", name: "Book", component: BookPage },
  {
    path: '/book/:book_code/view',
    name: 'Book',
    component: () => import('@/pages/books/PdfView.vue')
  },
  {
    path: '/author/:id',
    name: 'AuthorDetails',
    component: () => import('@/pages/authors/AuthorPage.vue')
  },
  {
    path: '/genre/:id/:slug',
    name: 'GenreDetails',
    component: () => import('@/pages/genres/GenrePage.vue')
  },
  {
    path: '/topic/:id/:slug',
    name: 'TopicDetails',
    component: () => import('@/pages/topics/TopicPage.vue')
  },
  // user
  {
    path: '/signup',
    name: 'SignUp',
    component: () => import('@/pages/NotFoundPage.vue')
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: () => import('@/pages/user/SignInPage.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/pages/user/SignInPage.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
