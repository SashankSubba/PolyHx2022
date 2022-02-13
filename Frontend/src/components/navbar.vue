<template>
    <div class="nav-container">
        <img class="logo fixed" src="@/assets/guardians-logo.jpg" @click="$router.push('/dashboard').catch(()=>{})"/>
        <b-button variant="light" class="logout" @click="logout">Logout</b-button>
        <b-navbar toggable class="nav" type="dark">
            <b-navbar-nav style="width:100%" fill>
            <b-nav-item class="nav-item" href="/record">Record</b-nav-item>
            <b-nav-item class="nav-item" href="/map">Map</b-nav-item>
            </b-navbar-nav>
        </b-navbar>
    </div>
</template>
<script>
import Vue from "vue";

export default{
    name:"navbar",
    methods: {
        logout() {
            Vue.$cookies.remove('firstName')
            Vue.$cookies.remove('lastName')
            Vue.$cookies.remove('number')
            Vue.$cookies.remove('userId')

            location.href  = '/'
        }
    },
}
</script>
<style scoped>
.nav-container {
    position: relative;
}
.logo{
  display: inline-block;
  margin: 0 auto 0 auto;
  height: 200px;
}
.logout {
  position:absolute;
  top:1rem;
  right:1rem;
  font-size:larger;
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
  .logout {
  font-size:medium;
}
}
</style>