<template>
  <div>
    <router-link aria-label="Página siguiente" v-if="nextPant && (screenTrack[0] < screenTrack[1])" class="rout-bot bot-right hvr-grow" :to="linksPath+(screenTrack[0]+1)"></router-link>
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
