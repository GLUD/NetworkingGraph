<template>
<div class="container">
  <router-link aria-label="Página anterior" to="/">
    <img class="hvr-grow flechas-atras" src="../../../assets/logos-icons/flechas-atras.jpg" alt="fecha atras">
  </router-link>
  <div class="row text-center">
    <div class="col-sm-12">
      <h4 class="animated rubberBand">Seleccioné dominio</h4>
      <br>
      <form class="text-center">
        <label class="col-sm-3 radio-inline animated fadeInLeft dura_1">
            <input type="radio" name="google" value="google.com" @click="servidor=true" v-model="GuardarDato">1. Google.com
        </label>
        <label class="col-sm-3 radio-inline animated fadeInLeft dura_2">
            <input type="radio" name="youtube" value="youtube.com" @click="servidor=true" v-model="GuardarDato">2. Youtube.com
          </label>
        <label class="col-sm-3 radio-inline animated fadeInLeft dura_3">
            <input type="radio" name="facebook" value="facebook.com" @click="servidor=true" v-model="GuardarDato">3. Facebook.com
          </label>
        <label class="col-sm-3 radio-inline animated fadeInLeft dura_3">
              <input type="radio" name="otros" value="otros.com" @click="otro = true, servidor=true">4. ¿Otro?
        </label>
        <div class="opcionDiferente fadeInLeft dura_1" v-if="otro == true">
          <strong>¿Cuál?:</strong>
          <input id="entrada" type="text" name="otro" v-model="GuardarDato">
        </div>
      </form>
    </div>
    <div class="col-sm-6 animated jello" v-if="servidor">
      <h3>trazar ruta desde servidor remoto</h3>

      <div class="col-sm-12 animated bounceInRight dura_1">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="AmericaNorte">America del Norte</button>
        <br>
      </div>
      <div class="col-sm-12 animated bounceInRight dura_2">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="SurAmerica">Sur America</button>
        <br>
      </div>
      <div class="col-sm-12 animated bounceInRight dura_3">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="asia">Asia</button>
        <br>
      </div>
      <div class="col-sm-12 animated bounceInRight dura_4">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="europa">Europa</button>
        <br>
      </div>
      <div class="col-sm-12 animated bounceInRight dura_5">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="oceania">Oceania</button>
        <br>
      </div>
    </div>
    <div class="col-sm-6 animated jello" v-if="servidor">
      <h3>trazar ruta desde servidor local</h3>
      <div class="col-sm-12 animated bounceInRight dura_1">
        <button type="button" class="btn btn-primary btn-sm btn-block" @click="local">local</button>
        <br>
      </div>
    </div>
    <div class="col-sm-11" v-if="info">
      <div class="col-sm-1"></div>
      <h3 class="animated fadeInDown dura_3">{{continente}}</h3>
      <h4 class="animated fadeInDown dura_4">{{pais}}</h4>
      <h5 class="animated fadeInDown dura_5">{{nomServer}}</h5>
    </div>
    <br>
    <div class="col-sm-4"></div>
    <div class="grafico col-sm-8 text-left" v-if="info">
      <ul id="example-1">
        <li style="position:relative;" v-for="(item,index) in items">
          <div class="num" :class="'animated fadeInLeft dura_'+index"> {{ item.num }} </div>
          <div class="ip" :class="'animated fadeInLeft dura_'+index"> {{ item.hostname }} <br> {{ item.ip }}</div>
          <div class="linea" :class="'animated fadeInUp dura_'+index"></div>
          <div class="ttl" :class="'animated fadeInLeft dura_'+index"> {{ item.ttl1 }} <br> {{ item.ttl2 }} <br> {{ item.ttl3 }} </div>
        </li>
      </ul>
    </div>
  </div>
  <!-- Ya guardo el dato -->
  <!-- {{this.$store.state.pregunta.direccion}} -->
  <sweet-modal ref="cargando" overlay-theme="light" hide-close-button blocking modal-theme="light">
    <img src="../../../assets/tenor.gif" alt="">
  </sweet-modal>
</div>
</template>
<!-- http://gcoch.github.io/D3-tutorial/asociar-datos.html -->
<!-- https://www.w3schools.com/bootstrap4/default.asp -->
<script>
import axios from 'axios';

export default {
  data() {
    return {
      servidor: false,
      dominio: "",
      continente: "",
      pais: "",
      nomServer: "",
      info: false,
      otro: false,
      items: [],
    };
  },
  mounted() {

  },
  methods: {
    AmericaNorte() {
      this.$refs.cargando.open();
      this.info = false
      this.continente = "Ameria del Norte",
        this.pais = "Canada",
        this.nomServer = "netmon.physics.carleton.ca"
      this.dominio = this.$store.state.pregunta.direccion
      console.log("Espere...");
      // https://medium.com/techtrument/handling-ajax-request-in-vue-applications-using-axios-1d26c47fab0
      axios.get('https://glud-traceroute-webscraper.herokuapp.com/ws1/' + this.dominio + '/')
        .then((response) => {
          console.log('success response', response);
          this.$refs.cargando.close();
          this.info = true
          this.items = response.data;
          console.log(this.item);

        }, (error) => {
          console.log('error', error);
        })
    },
    SurAmerica() {
      this.$refs.cargando.open();
      this.info = false
      this.continente = "Ameria del Sur",
        this.pais = "Brazil",
        this.nomServer = "ping.unesp.br"
      this.dominio = this.$store.state.pregunta.direccion
      console.log("Espere...");
      // https://medium.com/techtrument/handling-ajax-request-in-vue-applications-using-axios-1d26c47fab0
      axios.get('https://glud-traceroute-webscraper.herokuapp.com/ws2/' + this.dominio + '/')
        .then((response) => {
          console.log('success response', response);
          this.$refs.cargando.close();
          this.info = true
          this.items = response.data;
          console.log(this.item);

        }, (error) => {
          console.log('error', error);
        })
    },
    asia() {
      this.$refs.cargando.open();
      this.info = false
      this.continente = "Asia",
        this.pais = "China",
        this.nomServer = "ihep.ac.cn"
      this.dominio = this.$store.state.pregunta.direccion
      console.log("Espere...");
      // https://medium.com/techtrument/handling-ajax-request-in-vue-applications-using-axios-1d26c47fab0
      axios.get('https://glud-traceroute-webscraper.herokuapp.com/ws3/' + this.dominio + '/')
        .then((response) => {
          console.log('success response', response);
          this.$refs.cargando.close();
          this.info = true
          this.items = response.data;
          console.log(this.item);

        }, (error) => {
          console.log('error', error);
        })
    },
    europa() {
      this.$refs.cargando.open();
      this.info = false
      this.continente = "Europa",
        this.pais = "Austria",
        this.nomServer = "nemox.net"
      this.dominio = this.$store.state.pregunta.direccion
      console.log("Espere...");
      // https://medium.com/techtrument/handling-ajax-request-in-vue-applications-using-axios-1d26c47fab0
      axios.get('https://glud-traceroute-webscraper.herokuapp.com/ws4/' + this.dominio + '/')
        .then((response) => {
          console.log('success response', response);
          this.$refs.cargando.close();
          this.info = true
          this.items = response.data;
          console.log(this.item);

        }, (error) => {
          console.log('error', error);
        })
    },
    oceania() {
      this.$refs.cargando.open()
      this.info = false
      this.continente = "Oceania",
        this.pais = "Australia",
        this.nomServer = "hafey.org"
      this.dominio = this.$store.state.pregunta.direccion
      console.log("Espere...");
      // https://medium.com/techtrument/handling-ajax-request-in-vue-applications-using-axios-1d26c47fab0
      axios.get('https://glud-traceroute-webscraper.herokuapp.com/ws5/' + this.dominio + '/')
        .then((response) => {
          console.log('success response', response);
          this.$refs.cargando.close();
          this.info = true
          this.items = response.data;
          console.log(this.item);

        }, (error) => {
          console.log('error', error);
        })
    },
    local() {
      this.$refs.cargando.open();
      this.continente = "Local"
      this.pais = ""
      this.nomServer = ""
      this.info = false
      this.dominio = this.$store.state.pregunta.direccion
      console.log("Espere...");
      // https://medium.com/techtrument/handling-ajax-request-in-vue-applications-using-axios-1d26c47fab0
      axios.get('https://glud-traceroute-webscraper.herokuapp.com/local?host=' + this.dominio)
        .then((response) => {
          console.log('success response', response);
          this.info = true
          this.$refs.cargando.close();
          this.items = response.data;
          console.log(this.item);

        }, (error) => {
          console.log('error', error);
        })
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
<style lang="scss" scoped>
.imagenUD {
    width: 30%;
    margin-top: -1.5em;
}
.grafico {
    ul {
        list-style-type: none;
    }
    #lista-nodos li {
        position: relative;
    }
    .num {
        border-radius: 50%;
        background: #ffed00;
        padding: 0;
        width: 30px;
        height: 30px;
        text-align: center;
        vertical-align: middle;
        margin-left: 8px;
    }
    .ip {
        position: absolute;
        top: 1px;
        left: 50px;
    }
    .linea {
        width: 3px;
        height: 300px;
        background: #000;
        margin-left: 21.5px;
    }
    .ttl {
        position: absolute;
        top: 100px;
        left: 100px;
    }
}

.opcionDiferente {
    #entrada {
        background-color: #DDD;
    }
}
</style>
