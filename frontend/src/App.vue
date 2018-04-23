<template>
<div id="app" class="">
  <v-app :class="color">
    <header-app></header-app>
    <main class="animated fadeInDown">
      <section class="main-container" aria-label="contenido">
        <v-layout justify-center wrap class="appcontain">
          <v-flex xs12 sm12 md12 lg8>
            <router-view></router-view>
          </v-flex>
        </v-layout>
      </section>
    </main>
    <footer-app></footer-app>
  </v-app>
</div>
</template>

<script>
export default {
  name: "app",
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

<style src="./sass/styles.scss" lang="scss">
body,
html {
    height: 100vh;
}
</style>
