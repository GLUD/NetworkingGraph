<template>
  <div>
    <router-link aria-label="Página anterior" v-if="screenTrack[0] >= 2" class="rout-bot bot-left hvr-grow" :to="linksPath+ (screenTrack[0]-1)"></router-link>
  </div>
</template>

<script>
export default {
  props: {
    linksPath: {
      type: String,
      required: true
    }
  },
  data() {
    return {};
  },
  computed: {
    nextPant() {
      return this.$store.state.nextPant;
    },
    screenTrack() {
      return this.$store.state.screens;
    }
  }
};
</script>

<style lang="scss" scoped>

</style>
