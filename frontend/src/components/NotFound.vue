<template>
  <div class="container d-flex align-items-center" id="text">
    <div class="row" id="text-row">
      <div class="col-md-2 d-flex align-items-center justify-content-center"><h1 class="mr-3 pr-3">404</h1></div>
      <div class="d-flex col-md-1 justify-content-center" id="divider"><div class="vr"></div></div>
      <div class="d-flex col-md-6 align-items-center">
        <h2 class="font-weight-normal lead" id="desc">The page you requested was not found.</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
  metaInfo () {
    return {
      title: 'Page Not Found'
    }
  }
}
</script>

<style scoped>
#text {
  height: 100vh;
}
#divider {
  height: 4em;
}
#text-row {
  width: 100%;
  margin: 0 10% 0 30%;
}
</style>
