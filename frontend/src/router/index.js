import { createRouter, createWebHistory } from 'vue-router'
import { useToast } from 'vue-toastification'

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
    component: () => import('@/pages/user/SignUpPage.vue')
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: () => import('@/pages/user/SignInPage.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('@/pages/user/ProfilePage.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/edit/profile',
    name: 'EditProfile',
    component: () => import('@/pages/user/EditProfilePage.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('@/pages/user/DashboardPage.vue')
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

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requiresAuth) &&
    !isAdminLoggedIn()
  ) {
    const toast = useToast()
    toast.error('You must be logged in to access this page')
    console.log('Log in is required.')
    next('/signin')
  } else {
    next()
  }
})

function isAdminLoggedIn () {
  if (
    !localStorage.getItem('accessToken') &&
    !localStorage.getItem('refreshToken')
  ) {
    return false
  }

  return true
}

export default router
