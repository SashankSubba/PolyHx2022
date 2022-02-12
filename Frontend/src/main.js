import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import { BootstrapVue} from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import login from './pages/login.vue'
import signup from './pages/signup'

Vue.use(BootstrapVue)

Vue.use(VueRouter)

const routes = [
  { path: '/signup', component: signup},
  { path: '/', component: login},

]

const router = new VueRouter({
  mode: 'history',
  routes
})

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
