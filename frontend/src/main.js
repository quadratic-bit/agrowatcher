// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueMeta from 'vue-meta'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import App from './App'
import router from './router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap-icons/font/bootstrap-icons.css'

Vue.config.productionTip = false
Vue.use(VueMeta)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
