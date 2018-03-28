<template>
  <div aria-hidden="true" class="acces-word">
    <button >
      <div class="acces-icon back-red hvr-grow">
        <v-icon class="always-white">fa fa-sign-language</v-icon>
      </div>
    </button>
    <div class="accef-gif back-red animated fadeIn" :class="pos">
      <img :src="getImgUrl(gifSrc)" alt="">
    </div>
  </div>
</template>

<script>
export default {
  props: {
    gifPos: {
      type: String,
      required: false
    },
    gifSrc: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      galsrc: require.context("./../../assets", true, /\.gif$/),
      pos: this.gifPos ? this.gifPos : "gif-bottom"
    };
  },
  methods: {
    getImgUrl(galIma) {
      if (galIma !== "") {
        return this.galsrc("./" + galIma + ".gif");
      }
    }
  }
};
</script>

<style lang="scss" scoped>

</style>

