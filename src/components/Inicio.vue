<template>
<div class="container">
  <div class="jumbotron text-center">
    <h1>Networking Graph</h1>
    <p>Laboratorio traza de rutas locales y remotas</p>
    <img class="rounded imagenUD" src="../assets/logos-icons/escudoUD.png" alt="Cinque Terre">
    <br>
    <h2>Ingenieria de sistemas</h2>
    <h3>Autores</h3>
    <h4>Andres Mauricio Acosta Pulido 20142020111</h4>
    <h4>Daniel David Leal Lara 20151020057</h4>
    <br>
    <div class="col-sm-12 text-center">
      <router-link :to="linksPath+'1'" aria-label="Iniciar el curso">
        <ui-button-circle-secondary aria-hidden="true" class="animated bounceIn dura_1" aria=""></ui-button-circle-secondary>
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
<style lang="scss">
.imagenUD {
    width: 30%;
    margin-top: -1.5em;
}
</style>
