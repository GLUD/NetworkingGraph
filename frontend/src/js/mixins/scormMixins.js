// En este archivo se pueden definir variables y funciones que pueden ser llamadas en los archivos en que se importen
//import { SCORM } from "pipwerks-scorm-api-wrapper" // importa la dependencia
export default {
  data() {
    return {
      varPru: "ejemplo de variable",
      totalgenera: 0,
      totaluno: 0,
      totaldos: 0,
      totaltres: 0,
      totalcuatro: 0,
      totalcinco: 0,
      //myscorm:SCORM
    }
  },
  methods: { // Funciones
    alertaParametros(event) {
      return "mensaje de prueba " + event
    }
  },
  mounted() { // Funcion que se ejecuta al abrirse la aplicacion
    //inicializar paginas
    var j = 0;
    var pages = new Array()
    for (var i = 0; i <= 11; i++) {
      pages[j] = "#/bienvenida/" + i
      j++
      this.totalgenera++
    }
    this.totaluno += this.totalgenera;
    for (i = 1; i <= 27; i++) {
      pages[j] = "#/unidaduno/" + i
      j++
      this.totaluno++
    }
    this.totaldos += this.totaluno;
    for (i = 1; i <= 16; i++) {
      pages[j] = "#/unidaddos/" + i
      j++
      this.totaldos++
    }
    this.totaltres += this.totaldos;
    for (i = 1; i <= 24; i++) {
      pages[j] = "#/unidadtres/" + i
      j++
      this.totaltres++
    }
    this.totalcuatro += this.totaltres;
    for (i = 1; i <= 25; i++) {
      pages[j] = "#/unidadcuatro/" + i
      j++
      this.totalcuatro++
    }
    this.totalcinco += this.totalcuatro;
    for (i = 1; i <= 19; i++) {
      pages[j] = "#/unidadcinco/" + i
      j++
      this.totalcinco++
    }
  }
}
