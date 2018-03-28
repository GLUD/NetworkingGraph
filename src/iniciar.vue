<template>
<div class="container">
  <div class="row text-center">
    <div class="col-sm-6">
      <br>
      <h1>Trazado de rutas remotamente</h1>
      <div class="col-sm-3">
        <button type="button" class="btn btn-primary">Ecuador</button>
      </div>
      <div class="col-sm-3">
        <button type="button" class="btn btn-primary">Estados Unidos</button>
      </div>
      <div class="col-sm-3">
        <button type="button" class="btn btn-primary">Sur America</button>
      </div>
      <div class="col-sm-3">
        <button type="button" class="btn btn-primary">Oceania</button>
      </div>
    </div>
    <div class="col-sm-6">
      <br>
      <h1>Trazado de rutas localmente</h1>
      <div class="col-sm-3">
        <button type="button" class="btn btn-primary">local</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'iniciar',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style lang="scss">
</style>
