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
              <label>Email</label>
            </div>
            <b-form-input
                v-model="email"
                type="email"
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
                type="password"
                placeholder="Enter your password">
            </b-form-input>
          </b-col>
          <b-col sm="4"></b-col>
        </b-row>

        <b-row class="mt-5">
          <b-col sm="4"></b-col>
          <b-col sm="4">
            <b-button style="margin-right: 20px" v-on:click="login">Login</b-button>
            <b-link to="/signup">Create Profile</b-link>
          </b-col>
          <b-col sm="4"></b-col>
        </b-row>
      </b-form>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "login",
  data() {
    return {
      email: "",
      password: ""
    }
  },
  methods: {
    login() {
      axios.post("http://localhost:5000/login", {
        'email': this.email,
        'password': this.password
      }, {
        'Content-Type': 'application/json'
      })
          .then((result) => {
            this.$router.push('/dashboard');
            console.log(result)
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
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
