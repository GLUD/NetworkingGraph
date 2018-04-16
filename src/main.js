// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import BootstrapVue from "bootstrap-vue"
import App from './App'
import VueResource from 'vue-resource';
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import {
  SweetModal,
  SweetModalTab
} from 'sweet-modal-vue';
import router from './js/router'
import {
  store
} from './js/store/store'
// Register here all the components
import Headerapp from './components/ui/Header'
import Footerapp from './components/ui/Footer'

// new components
import BotonInicio from './components/ui/BotonInicio'
Vue.config.productionTip = false

// This is the UI componentlibrary

Vue.use(BootstrapVue);
Vue.use(VueResource);
Vue.config.productionTip = false
// Register here all the components
Vue.component('header-app', Headerapp);
Vue.component('footer-app', Footerapp);
Vue.component('sweet-modal', SweetModal);
Vue.component('sweet-modal-tab', SweetModalTab);
// UI Components
Vue.component('button-inicio', BotonInicio);

Vue.prototype.$color = 'light';

/* eslint-disable no-new */
new Vue({
  store: store,
  el: '#app',
  router,
  template: '<App/>',
  components: {
    App
  }
});
