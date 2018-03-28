<template>
<header class="light-dark-int">
  <div class="col-sm-12">
    <h1>Networking Graph</h1>
    <p>Laboratorio traza de rutas locales y remotas</p>
  </div>
</header>
</template>

<script>
export default {
  data() {
    return {};
  },
  computed: {
    screenTrack() {
      return this.$store.state.screens;
    }
  },
  watch: {}
};
</script>

<style lang="scss" scope>
@import "../../sass/helpers/variables.scss";

header {
    width: 100%;
    min-height: 60px;
    font-size: 1rem;
    line-height: 1.5rem;
    box-shadow: 4px 0 15px black;
    text-align: right;
    margin-bottom: 20px;
    padding: 10px;
    font-style: italic;
    position: relative;
    z-index: 10 !important;
    .nombre {
        font-size: 1.1em;
        color: $primary-red;
    }
    p {
        margin-bottom: 0;
    }
}

.user-info {
    position: relative;
    z-index: 6;
    margin-right: 20px;
}

</style>
