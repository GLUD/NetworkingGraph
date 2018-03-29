<template>
<div class="container">
  <div class="row text-center">
    <div class="col-sm-6">
      <h1>Remotamente</h1>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="servidor=true, ecuador()">Ecuador</button>
        <br>
      </div>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="servidor=true, EEUU()">Estados Unidos</button>
        <br>
      </div>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="servidor=true, SurAmerica()">Sur America</button>
        <br>
      </div>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="servidor=true, Oceania()">Oceania</button>
        <br>
      </div>
    </div>
    <div class="col-sm-6">
      <h1>Localmente</h1>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="servidor=true, local()">local</button>
        <br>
      </div>
    </div>
    <div class="col-sm-12" v-if="servidor">
      <h4>Seleccioné DNS</h4>
      <br>
      <form class="text-center">
        <label class="col-sm-3 radio-inline">
            <input type="radio" name="google" value="google.com" v-model="GuardarDato">1. Google.com
        </label>
        <label class="col-sm-3 radio-inline">
            <input type="radio" name="youtube" value="youtube.com" v-model="GuardarDato">2. Youtube.com
          </label>
        <label class="col-sm-3 radio-inline">
            <input type="radio" name="facebook" value="facebook.com" v-model="GuardarDato">3. Facebook.com
          </label>
      </form>
    </div>
  </div>
</div>
</template>
<!-- http://gcoch.github.io/D3-tutorial/asociar-datos.html -->
<!-- https://www.w3schools.com/bootstrap4/default.asp -->
<script>
export default {
  data() {
    return {
      servidor: false,
    };
  },
  methods: {
    ecuador() {

    },
    EEUU() {

    },
    SurAmerica() {

    },
    Oceania() {

    },
    local() {

    },
    preguntas() {
      console.log(this.$store.state.pregunta.direccion);
      return this.$store.state.pregunta.direccion;
    },
  },
  computed: {
    GuardarDato: {
      get() {
        return this.$store.state.pregunta.direccion;
      },
      set(value) {
        this.$store.commit("guardarPregunta", value);
      }
    },
  }
}
</script>
<style lang="scss">
.imagenUD {
    width: 30%;
    margin-top: -1.5em;
}
</style>
