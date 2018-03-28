<template>
<div class="container">
  <div class="row text-center">
    <div class="col-sm-6">
      <h1>Remotamente</h1>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="dominio=true, ecuador()">Ecuador</button>
        <br>
      </div>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="dominio=true, EEUU()">Estados Unidos</button>
        <br>
      </div>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="dominio=true, SurAmerica()">Sur America</button>
        <br>
      </div>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="dominio=true, Oceania()">Oceania</button>
        <br>
      </div>
    </div>
    <div class="col-sm-6">
      <h1>Localmente</h1>
      <div class="col-sm-12">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="dominio=true, local()">local</button>
        <br>
      </div>
    </div>
    <div class="col-sm-12" v-if="dominio">
      <h4>Ingrese DNS</h4>
      <form class="text-center">
        <label class="radio-inline">
            <input type="radio" name="google" value="google.com" v-model="GuardarDato">1. Google.com
        </label>
        <label class="radio-inline">
            <input type="radio" name="youtube" value="youtube.com" v-model="GuardarDato">2. Youtube.com
          </label>
        <label class="radio-inline">
            <input type="radio" name="facebook" value="facebook.com" v-model="GuardarDato">3. Facebook.com
          </label>
      </form>
    </div>
  </div>
  {{this.$store.state.pregunta.direccion}}
</div>
</template>

<script>
export default {
  data() {
    return {
      dominio: false,
    };
  },
  methods: {
    ecuador() {
      // const Traceroute = require('nodejs-traceroute');
      // try {
      //   const tracer = new Traceroute();
      //   tracer
      //     .on('pid', (pid) => {
      //       console.log(`pid: ${pid}`);
      //     })
      //     .on('destination', (destination) => {
      //       console.log(`destination: ${destination}`);
      //     })
      //     .on('hop', (hop) => {
      //       console.log(`hop: ${JSON.stringify(hop)}`);
      //     })
      //     .on('close', (code) => {
      //       console.log(`close: code ${code}`);
      //     });
      //
      //   tracer.trace('github.com');
      // } catch (ex) {
      //   console.log(ex);
      // }
    },
    EEUU() {
      // const Traceroute = require('nodejs-traceroute');
      // try {
      //   const tracer = new Traceroute();
      //   tracer
      //     .on('pid', (pid) => {
      //       console.log(`pid: ${pid}`);
      //     })
      //     .on('destination', (destination) => {
      //       console.log(`destination: ${destination}`);
      //     })
      //     .on('hop', (hop) => {
      //       console.log(`hop: ${JSON.stringify(hop)}`);
      //     })
      //     .on('close', (code) => {
      //       console.log(`close: code ${code}`);
      //     });
      //
      //   tracer.trace('github.com');
      // } catch (ex) {
      //   console.log(ex);
      // }
    },
    SurAmerica() {
      // const Traceroute = require('nodejs-traceroute');
      // try {
      //   const tracer = new Traceroute();
      //   tracer
      //     .on('pid', (pid) => {
      //       console.log(`pid: ${pid}`);
      //     })
      //     .on('destination', (destination) => {
      //       console.log(`destination: ${destination}`);
      //     })
      //     .on('hop', (hop) => {
      //       console.log(`hop: ${JSON.stringify(hop)}`);
      //     })
      //     .on('close', (code) => {
      //       console.log(`close: code ${code}`);
      //     });
      //
      //   tracer.trace('github.com');
      // } catch (ex) {
      //   console.log(ex);
      // }
    },
    Oceania() {
      // const Traceroute = require('nodejs-traceroute');
      // try {
      //   const tracer = new Traceroute();
      //   tracer
      //     .on('pid', (pid) => {
      //       console.log(`pid: ${pid}`);
      //     })
      //     .on('destination', (destination) => {
      //       console.log(`destination: ${destination}`);
      //     })
      //     .on('hop', (hop) => {
      //       console.log(`hop: ${JSON.stringify(hop)}`);
      //     })
      //     .on('close', (code) => {
      //       console.log(`close: code ${code}`);
      //     });
      //
      //   tracer.trace('github.com');
      // } catch (ex) {
      //   console.log(ex);
      // }
    },
    local() {
      // const Traceroute = require('nodejs-traceroute');
      // try {
      //   const tracer = new Traceroute();
      //   tracer
      //     .on('pid', (pid) => {
      //       console.log(`pid: ${pid}`);
      //     })
      //     .on('destination', (destination) => {
      //       console.log(`destination: ${destination}`);
      //     })
      //     .on('hop', (hop) => {
      //       console.log(`hop: ${JSON.stringify(hop)}`);
      //     })
      //     .on('close', (code) => {
      //       console.log(`close: code ${code}`);
      //     });
      //
      //   tracer.trace('github.com');
      // } catch (ex) {
      //   console.log(ex);
      // }
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
    preguntas() {
      console.log(this.$store.state.pregunta.direccion);
      return this.$store.state.pregunta.direccion;
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
