<template>
  <button :aria-label="aria" class="bot-one light-black hvr-grow-rotate">
    <p>
      <span class="part-1">{{partOne}}</span><br>
      <span class="part-2 font-red">{{partTwo}}</span><br>
      <span class="part-3 font-red">{{partThree}}</span>
    </p>
  </button>
</template>

<script>
export default {
  props: {
    aria: {
      type: String,
      required: true
    },
    partOne: {
      type: String,
      required: true
    },
    partTwo: {
      type: String,
      required: false
    },
    partThree: {
      type: String,
      required: false
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../../sass/helpers/variables";
@import "../../sass/helpers/mixins";
.bot-one {
  text-align: center;
  padding-top: 5px;
  width: 12rem;
  height: 12rem;
  margin: 10px auto;
  border-radius: 50%;
  line-height: 1.2rem;
  font-size: 1.2rem;
  display: table;
  position: relative;
  @include shadow(1px 1px 10px #989898);
  p {
    display: table-cell;
    vertical-align: middle;
    width: 12rem;
  }
  .part-1 {
    font-size: 1.1em;
    font-weight: bold;
  }
  .part-2 {
    font-size: 1em;
    font-weight: bold;
  }
  .part-3 {
    font-size: 1.6em;
    line-height: 1.2em;
    font-weight: bold;
  }
}

.dark {
  .bot-one {
    box-shadow: none;
    border: 2px solid $white;
  }
}
</style>
