<template>
<div class="">
  <button class="ini-bot light-black hvr-grow-rotate" :aria-label="aria">
    Haga<br>
    <span class="part-1 font-red">CLIC</span><br>-Aqui-<br>
  </button>
</div>
</template>

<script>
export default {
  props: {
    aria: {
      type: String,
      required: true
    }
  }
};
</script>

<style lang="scss" scoped>

.ini-bot {
    padding: 1em;
    width: 7em;
    height: 7em;
    margin: auto;
    border: ridge 2px rgb(25, 31, 163);
    border-radius: 20%;
    line-height: 1.5em;
    font-size: 17px;
    .part-1 {
        font-size: 1.6em;
        font-weight: bold;
    }
    .part-2 {
        font-size: 1.5em;
        font-weight: bold;
    }
}
</style>
