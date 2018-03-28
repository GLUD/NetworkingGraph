<template>
<div class="container">
  <div class="jumbotron text-center">
    <h1>Networking Graph</h1>
    <p>Laboratorio traza de rutas locales y remotas</p>
    <img class="rounded imagenUD" src="./assets/escudoUD.png" alt="Cinque Terre">
    <br>
    <h2>Ingenieria de sistemas</h2>
    <h3>Autores</h3>
    <h4>Andres Mauricio Acosta Pulido 20142020111</h4>
    <h4>Daniel David Leal Lara 20151020057</h4>
  </div>
  <!-- <div class="row text-center">
      <div class="col-sm-12">
        <router-link to="./iniciar" aria-label="Iniciar">
          <button type="button" class="btn btn-primary">Iniciar</button>
        </router-link>
      </div>
    </div> -->
  <div class="row text-center">
    <div class="col-sm-6">
      <h1>Remotamente</h1>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-block" @click="dominio=true, ecuador()">Ecuador</button>
        <br>
      </div>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-block" @click="dominio=true, EEUU()">Estados Unidos</button>
        <br>
      </div>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-block" @click="dominio=true, SurAmerica()">Sur America</button>
        <br>
      </div>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-block" @click="dominio=true, Oceania()">Oceania</button>
        <br>
      </div>
    </div>
    <div class="col-sm-6">
      <h1>Localmente</h1>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-block" @click="dominio=true, local()">local</button>
        <br>
      </div>
    </div>
    <div class="col-sm-12" v-if="dominio">
      <h4>Ingrese DNS</h4>
      <form class="text-center">
        <label class="radio-inline">
            <input type="radio" name="optradio">1. Google.com
        </label>
        <label class="radio-inline">
            <input type="radio" name="optradio">2. Youtube.com
          </label>
        <label class="radio-inline">
            <input type="radio" name="optradio">3. Facebook.com
          </label>
      </form>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      dominio: false,
    };
  },
  methods: {
    ecuador() {
      console.log("Hello");
      var traceroute = require('traceroute');
      traceroute.trace('google.com', function(err, hops) {
        if (!err) console.log(hops);
      });
    }
  }
}
</script>
<style lang="scss">
.imagenUD {
    width: 30%;
    margin-top: -1.5em;
}
</style>
