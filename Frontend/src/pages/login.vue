<template>
  <div style="margin: 2rem">
    <h1>Welcome to Guardians !</h1>
    <img src=../assets/logo.jpg width="10%">
      <b-container>
      <b-form onsubmit="submit" class="mt-5">
        <b-row>
          <b-col sm="4"></b-col>
          <b-col sm="4">
            <div class="text-start">
              <label >Email</label>
            </div>
            <b-form-input
                v-model="email"
                placeholder="Enter your email">
            </b-form-input>
          </b-col>
          <b-col sm="4"></b-col>
        </b-row>

        <b-row class="mt-3">
          <b-col sm="4"></b-col>
          <b-col sm="4">
            <div class="text-start">
              <label>Password</label>
            </div>
            <b-form-input
                v-model="password"
                placeholder="Enter your password">
            </b-form-input>
          </b-col>
          <b-col sm="4"></b-col>
        </b-row>

        <b-row class="mt-5">
          <b-col sm="4"></b-col>
          <b-col sm="4">
            <b-button style="margin-right: 20px">Login</b-button>
            <b-link to="/signup">Create Profile</b-link>
          </b-col>
          <b-col sm="4"></b-col>
        </b-row>
        </b-form>
      </b-container>
  </div>
</template>

<script>

export default {
  name: "login",
  data() {
    return {
      email: "",
      password: ""
    }
  },
  methods: {}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
