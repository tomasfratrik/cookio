import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
// import CreateRecipeView from '../views/CreateRecipeView.vue'
import CreateRecipeView from '@/views/CreateRecipeView.vue'
import AssignRecipeClassView from '@/views/AssignRecipeClassView.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/assign_recipe_class',
    name: 'AssignRecipeClass',
    component: AssignRecipeClassView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
