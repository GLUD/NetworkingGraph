<template>
  <div>
    <router-link aria-label="Página anterior" v-if="screenTrack[0] >= 2" class="rout-bot bot-left hvr-grow" :to="'/'+mod.modurl+'/'+ (screenTrack[0]-1)"></router-link>
    <router-link aria-label="Página siguiente" v-if="nextPant" class="rout-bot bot-right hvr-grow" :to="'/'+mod.modurl+'/'+ (screenTrack[0]+1)"></router-link>
  </div>
</template>

<script>
export default {
  props: {
    mod: {
      type: Object,
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
.rout-bot {
  position: fixed;
  top: 40%;
  background-image: url("../../assets/logos-icons/flechas-nav.png");
  width: 55px;
  height: 68px;
  display: block;
  &.bot-left {
    left: 0;
    background-position: 0 0;
    &:hover,
    &:focus {
      background-position: 0 -68px;
    }
  }
  &.bot-right {
    right: 0;
    background-position: -55px 0;
    &:hover,
    &:focus {
      background-position: -55px -68px;
    }
  }
}

@media (min-width: 1264px) {
  .rout-bot {
    &.bot-left {
      left: 100px;
    }
    &.bot-right {
      right: 100px;
    }
  }
}
</style>
