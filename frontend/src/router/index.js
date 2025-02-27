import { createRouter, createWebHistory } from 'vue-router'
import ApiTest from '@/components/ApiTest.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'api-test',
      component: ApiTest,
    }
  ],
})

export default router
