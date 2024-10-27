import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '@/pages/HomePage.vue'
import NotFoundPage from '@/pages/NotFoundPage.vue'
import BookDetailsPage from '@/pages/BookDetailsPage.vue'
import AuthorPage from '@/pages/AuthorPage.vue'
// import BookPage from '@/pages/BookPage.vue'
import PdfView from '@/pages/PdfView.vue'
import GenrePage from '@/pages/GenrePage.vue'
import TopicPage from '@/pages/TopicPage.vue'

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/book/:book_code', name: 'BookDetails', component: BookDetailsPage },
  // { path: "/book/:book_code/view", name: "Book", component: BookPage },
  { path: '/book/:book_code/view', name: 'Book', component: PdfView },
  { path: '/author/:id', name: 'AuthorDetails', component: AuthorPage },
  { path: '/genre/:id/:slug', name: 'GenreDetails', component: GenrePage },
  { path: '/topic/:id/:slug', name: 'TopicDetails', component: TopicPage },
  // user
  {
    path: '/signup',
    name: 'SignUp',
    component: () => import('@/pages/SignUpPage.vue')
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: () => import('@/pages/SignInPage.vue')
  },
  { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFoundPage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
