import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '@/pages/HomePage.vue'
import NotFoundPage from '@/pages/NotFoundPage.vue'
import BookDetailsPage from '@/pages/BookDetailsPage.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/book/:book_code', name: 'BookDetails', component: BookDetailsPage },
  { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFoundPage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
