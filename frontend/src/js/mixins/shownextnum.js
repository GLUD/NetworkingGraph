export default {
  data() {
    return {
      shownext: false,
      counter: []
    }
  },
  methods: {
    count(event) {
      this.counter[event] = 1
      var sumCounter = this.counter.reduce(add, 0)

      function add(a, b) {
        return a + b
      }

      if (sumCounter === this.botsvistos) {
        this.shownext = true
      }
    }
  }
}
