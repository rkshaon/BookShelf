import { createApp } from 'vue'
import { createMetaManager } from 'vue-meta'
import App from './App.vue'
import router from '@/router'
import store from '@/store'
import Toast from 'vue-toastification'

import '@/assets/tailwind.css'
import 'vue-toastification/dist/index.css'

const app = createApp(App)

app.use(createMetaManager())
app.use(router)
app.use(store)
app.use(Toast, {
  duration: 1000,
  position: 'top-right'
})
app.mount('#app')
