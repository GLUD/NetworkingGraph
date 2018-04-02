// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import BootstrapVue from "bootstrap-vue"
import App from './App'
import VueResource from 'vue-resource';
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import { SweetModal, SweetModalTab } from 'sweet-modal-vue';
import router from './js/router'
import {
  store
} from './js/store/store'
// Register here all the components
import Headerapp from './components/ui/Header'
import Footerapp from './components/ui/Footer'
import NavButtons from './components/ui/Navbuttons'
import NavAtras from './components/ui/NavAtras'
import NavAdel from './components/ui/NavAdel'
// new components
import Buttoncirclesecondary from './components/ui/Buttoncirclesecondary'
Vue.config.productionTip = false

// This is the UI componentlibrary

Vue.use(BootstrapVue);
Vue.use(VueResource);
Vue.config.productionTip = false
// Register here all the components
Vue.component('header-app', Headerapp)
Vue.component('footer-app', Footerapp)
Vue.component('navbuttons-app', NavButtons)
Vue.component('navatras-app', NavAtras)
Vue.component('navadel-app', NavAdel)
Vue.component('sweet-modal', SweetModal);
Vue.component('sweet-modal-tab', SweetModalTab);
// UI Components
Vue.component('ui-button-circle-secondary', Buttoncirclesecondary)

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
