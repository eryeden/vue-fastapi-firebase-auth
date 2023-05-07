import { createRouter, createWebHistory } from 'vue-router'
import Top from '../components/Top.vue'
import Api from '../components/Api.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'top',
      component: Top
    },
    {
      path: '/api',
      name: 'api',
      component: Api
    }
  ]
})

export default router
