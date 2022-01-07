import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Ping from '@/components/Ping'
import NotFound from '@/components/NotFound'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
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
