import Vue from "vue"
import Vuex from "vuex"
import VueResource from 'vue-resource';

Vue.use(VueResource);
Vue.config.productionTip = false
Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    nextPant: false,
    screens: [0, 0],
    video: null,
    tema: '',
    linksPath: '/NetworkingGraph/',
    cantPagsMods: {
      moduloUno: 0
    },
    pregunta: {
      direccion: []
    }
  },
  mutations: {
    nextShow: (state, event) => state.nextPant = event,
    screenTrack: (state, [currentScr, cantScr]) => state.screens = [currentScr, cantScr],
    temaName: (state, event) => state.tema = event,
    guardarPregunta: (state, respuesta) => state.pregunta.direccion = respuesta,
  }
});
