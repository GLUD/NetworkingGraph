<template>
<div id="main">

  <navatras-app :linksPath='linksPath'></navatras-app>

  <!-- Contenidos -->
  <component :is="'NetworkingGraph'+$route.params.unipage+'-app'"></component>

  <navadel-app :linksPath='linksPath'></navadel-app>
</div>
</template>

<script>
// Importar páginas internas
import NetworkingGraph from "./NetworkingGraph.vue";


export default {
  components: {
    "NetworkingGraph-app": NetworkingGraph,

  },
  data() {
    return {
      headcol: "",
    };
  },
  computed: {
    currentPage() {
      return Math.floor(this.$route.params.unipage);
    },
    linksPath() {
      return this.$store.state.linksPath;
    }
  },
  mounted() {
    this.$store.commit("screenTrack", [this.currentPage, 1]);
  },
  updated() {
    this.$store.commit("screenTrack", [this.currentPage, 1]);
  }
};
</script>

<style lang='scss' scoped>
// .notshow {
//     display: none;
// }
</style>
