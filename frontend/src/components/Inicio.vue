<template>
<div class="container">
  <div class="jumbotron text-center">
    <h2>Networking Graph</h2>
    <p>Laboratorio traza de rutas locales y remotas</p>
    <div class="col-sm-12">
      <img class="imagenUD" src="../assets/logos-icons/escudoUD.png">
    </div>
    <h3>Ingenieria de sistemas</h3>
    <div class="col-sm-12 text-center animated flip dura_2">
      <router-link :to="linksPath+'1'" aria-label="Iniciar el curso">
        <button-inicio aria-hidden="true" class="animated bounceIn dura_1" aria=""></button-inicio>
      </router-link>
    </div>
  </div>
</div>
</template>

<script>
export default {
  data() {
    return {};
  },
  computed: {
    color() {
      return this.$store.state.color;
    },
    linksPath() {
      return this.$store.state.linksPath;
    }
  }
};
</script>
<style>
.imagenUD {
  width: 20% !important;
  margin-top: -1.5em !important;
}
</style>
