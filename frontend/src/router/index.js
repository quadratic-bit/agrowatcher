import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Ping from '@/components/Ping'
import NotFound from '@/components/NotFound'

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
