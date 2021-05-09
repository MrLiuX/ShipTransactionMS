import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import Personnel from '../components/basicInfo/Personnel.vue'
import Department from '../components/basicInfo/Department.vue'
import Ship from '../components/basicInfo/Ship.vue'
import Inventory from '../components/materials/Inventory.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/login', component: Login },
  { path: '/', redirect: '/home' },
  {
    path: '/home',
    component: Home,
    children: [
      { path: '/personnel', component: Personnel },
      { path: '/department', component: Department },
      { path: '/ship', component: Ship },
      { path: '/inventory', component: Inventory }
    ]
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path === '/login') return next()
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/login')
  next()
})

export default router
