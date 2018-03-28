import Vue from 'vue'
import BootstrapVue from "bootstrap-vue"
import App from './App.vue'
// import Iniciar from './iniciar.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"

Vue.use(BootstrapVue)

new Vue({
  el: '#app',
  render: h => h(App)
})
// new Vue({
//   el: '#iniciar',
//   render: h => h(Iniciar)
// })
