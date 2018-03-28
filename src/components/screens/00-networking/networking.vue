<template>
<div id="main">

  <navatras-app :linksPath='linksPath'></navatras-app>

  <!-- Contenidos -->
  <component :is="'networking'+$route.params.unipage+'-app'"></component>

  <navadel-app :linksPath='linksPath'></navadel-app>
</div>
</template>

<script>
// Importar páginas internas
import Networking01 from "./networking-01.vue";


export default {
  components: {
    "networking1-app": Networking01,

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
