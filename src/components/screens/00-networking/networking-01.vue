<template>
<div class="container">
  <router-link aria-label="Página anterior" class="rout-bot bot-left hvr-grow" to="/"></router-link>
  <div class="row text-center">
    <div class="col-sm-12">
      <h4>Seleccioné dominio</h4>
      <br>
      <form class="text-center">
        <label class="col-sm-3 radio-inline">
            <input type="radio" name="google" value="google.com" @click="servidor=true" v-model="GuardarDato">1. Google.com
        </label>
        <label class="col-sm-3 radio-inline">
            <input type="radio" name="youtube" value="youtube.com" @click="servidor=true" v-model="GuardarDato">2. Youtube.com
          </label>
        <label class="col-sm-3 radio-inline">
            <input type="radio" name="facebook" value="facebook.com" @click="servidor=true" v-model="GuardarDato">3. Facebook.com
          </label>
      </form>
    </div>
    <div class="col-sm-6" v-if="servidor">
      <h1>Remotamente</h1>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="ecuador">Ecuador</button>
        <br>
      </div>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="EEUU">Estados Unidos</button>
        <br>
      </div>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="SurAmerica">Sur America</button>
        <br>
      </div>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="Oceania">Oceania</button>
        <br>
      </div>
    </div>
    <div class="col-sm-6" v-if="servidor">
      <h1>Localmente</h1>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="local">local</button>
        <br>
      </div>
    </div>
  </div>
  <!-- Ya guardo el dato -->
  {{this.$store.state.pregunta.direccion}}
</div>
</template>
<!-- http://gcoch.github.io/D3-tutorial/asociar-datos.html -->
<!-- https://www.w3schools.com/bootstrap4/default.asp -->
<script>
export default {
  data() {
    return {
      servidor: false,
      dominio: "",
    };
  },
  mounted() {

  },
  methods: {
    ecuador() {
      this.dominio = this.$store.state.pregunta.direccion
      console.log("Espere...");
      this.$http.get("http://127.0.0.1:8000/ws4/"+this.dominio, {
      }).then(function(data) {
        console.log(data)
      });
    },
    EEUU() {
      this.dominio = this.$store.state.pregunta.direccion
    },
    SurAmerica() {
      this.dominio = this.$store.state.pregunta.direccion
    },
    Oceania() {
      this.dominio = this.$store.state.pregunta.direccion
    },
    local() {
      this.dominio = this.$store.state.pregunta.direccion
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
