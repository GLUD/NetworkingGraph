export default {
  data() {
    return {
      galsrc: require.context("./../../assets", true, /\.png$/)
    }
  },
  methods: {
    getImgUrl(galIma) {
      if (galIma !== "") {
        return this.galsrc("./" + galIma + ".png")
      }
    }
  }
}
