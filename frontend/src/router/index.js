import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
// import CreateRecipeView from '../views/CreateRecipeView.vue'
import CreateRecipeView from '@/views/CreateRecipeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/createrecipe',
    name: 'createrecipe',
    // component: () => import('../views/CreateRecipeView.vue')
    component: CreateRecipeView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
