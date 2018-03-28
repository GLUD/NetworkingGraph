import Vue from "vue"
import Router from "vue-router"
import Inicio from "@/components/Inicio"
import ruta from "@/components/screens/Networking/ruta"

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
