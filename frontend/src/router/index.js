import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
// import CreateRecipeView from '../views/CreateRecipeView.vue'
import AssignRecipeClassView from '@/views/AssignRecipeClassView.vue'
import InstanceDetailView from '@/views/InstanceDetailView.vue'
import ClassInstancesView from '@/views/ClassInstancesView.vue'


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
  },
  {
    path: '/instance/:id',
    name: 'InstanceDetail',
    component: InstanceDetailView
  },
  {
    path: '/recipe_class/:id/instances',
    name: 'ClassInstances',
    component: ClassInstancesView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
