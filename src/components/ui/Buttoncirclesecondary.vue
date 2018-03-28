<template>
<div class="">
  <button class="ini-bot light-black hvr-grow-rotate" :aria-label="aria">
    Haga<br>
    <span class="part-1 font-red">CLIC</span><br>-para-<br>
    <span class="part-2 font-red davi-curs">continuar</span>
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
@import "../../sass/helpers/variables.scss";

.ini-bot {
    padding: 15px;
    width: 150px;
    height: 150px;
    margin: auto;
    border: dashed 3px rgb(25, 31, 163);
    border-radius: 50%;
    line-height: 22px;
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
