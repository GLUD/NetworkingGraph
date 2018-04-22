import Vue from "vue"
import Router from "vue-router"
import Inicio from "@/components/Inicio"
import ruta from "@/components/screens/00-networking/networking"

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: "/",
      name: "inicio",
      component: Inicio
    },
    {
      path: "/NetworkingGraph/:unipage",
      component: ruta
    },
  ]
})
