import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Dashboard from '@/components/Dashboard'
import Terms from '@/components/Terms'
import Ping from '@/components/Ping'
import NotFound from '@/components/NotFound'
import Privacy from '@/components/Privacy'
import Login from '@/components/Login'
import Signup from '@/components/Signup'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/index',
      redirect: '/'
    },
    {
      path: '/dashboard',
      component: Dashboard
    },
    {
      path: '/terms',
      component: Terms
    },
    {
      path: '/privacy',
      component: Privacy
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/signup',
      component: Signup
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ]
})
