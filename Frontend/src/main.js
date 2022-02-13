import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import { BootstrapVue} from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import login from './pages/login.vue'
import record from './pages/record.vue'
import map from './pages/map.vue'
import dashboard from './pages/dashboard.vue'
import signup from './pages/signup'
import recordAudio from "@/components/recordAudio";
import VueCookies from 'vue-cookies';
import VueGoogleHeatmap from 'vue-google-heatmap';
// import * as VueGoogleMaps from 'vue2-google-maps';

Vue.use(BootstrapVue)

Vue.use(VueRouter)
Vue.use(VueCookies)


Vue.use(VueGoogleHeatmap, {
  apiKey: process.env.VUE_APP_GOOGLE_MAPS_API,
});

// Vue.use(VueGoogleMaps, {
//     load: {
//         key: process.env.VUE_APP_GOOGLE_MAPS_API,
//         libraries: 'places',
//         installComponents: true,
//     }
// })

Vue.$cookies.config('5h')

const routes = [
  { path: '/', component: login},
  { path: '/record', component: record},
  { path: '/map', component: map},
  { path: '/dashboard', component: dashboard},
  { path: '/signup', component: signup},
  { path: '/record', component: recordAudio}
]

const router = new VueRouter({
  mode: 'history',
  routes
})

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
