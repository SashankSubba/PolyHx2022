<template>
  <div id="app">
  <div class="bg">
  <!-- <img class="logo fixed" src="./assets/guardians-logo.jpg" @click="$router.push('/dashboard').catch(()=>{})"/>
    <b-navbar toggable class="nav" type="dark">
        <b-navbar-nav style="width:100%" fill>
          <b-nav-item class="nav-item" href="/record">Record</b-nav-item>
          <b-nav-item class="nav-item" href="/map">Map</b-nav-item>
        </b-navbar-nav>
    </b-navbar> -->
      <router-view></router-view>
  </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>

<style>

html, body {
  height:100%;
  margin-top: 0;
}
body {
  background: linear-gradient(to bottom,  #000000 0%, #000000 39.06%, #252525 76.56%, #3E3E3E 100%);
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height:100%;
  margin-top: 0 !important;
}
/* .logo{
  display: inline-block;
  margin: 0 auto 0 auto;
  height: 200px;
}
.nav {
  background-color: #000000;
  height: 100px;
}
.nav-item {
  font-size: xx-large;
  font-weight: bold;
}

@media only screen and (max-width: 768px){
  .logo {
    height:150px;
    margin: 0 auto 0 auto;
  }
} */
</style>
