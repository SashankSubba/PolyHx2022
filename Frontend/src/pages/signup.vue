<template>
  <div style="margin: 2rem">
    <h1>Signup</h1>
    <img src=../assets/logo.jpg width="10%">
    <b-form onsubmit="submit" class="mt-5">
      <b-container>

        <b-row>
          <b-col sm="2"></b-col>
          <b-col sm="2">
            <label>Email</label>
          </b-col>
          <b-col sm="5">
            <b-form-input
              v-model="email"
              placeholder="Enter your email">
            </b-form-input>
          </b-col>
          <b-col sm="2"></b-col>
        </b-row>

        <b-row class="mt-3">
          <b-col sm="2"></b-col>
          <b-col sm="2">
            <label>Password</label>
          </b-col>
          <b-col sm="5">
            <b-form-input
              v-model="password"
              placeholder="Enter your password">
            </b-form-input>
          </b-col>
          <b-col sm="2"></b-col>
        </b-row>

        <b-row class="mt-3">
          <b-col sm="2"></b-col>
          <b-col sm="2">
            <label>Confirm Password</label>
          </b-col>
          <b-col sm="5">
            <b-form-input
              v-model="confirmPassword"
              placeholder="Confirm your password">
            </b-form-input>
          </b-col>
          <b-col sm="2"></b-col>
        </b-row>

        <b-row class="mt-3">
          <b-col sm="2"></b-col>
          <b-col sm="2">
            <label>First Name</label>
          </b-col>
          <b-col sm="5">
            <b-form-input
              v-model="firstName"
              placeholder="First Name">
            </b-form-input>
          </b-col>
          <b-col sm="2"></b-col>
        </b-row>

        <b-row class="mt-3">
          <b-col sm="2"></b-col>
          <b-col sm="2">
            <label>Last Name</label>
          </b-col>
          <b-col sm="5">
            <b-form-input
              v-model="lastName"
              placeholder="Last Name">
            </b-form-input>
          </b-col>
          <b-col sm="2"></b-col>
        </b-row>

        <b-row class="mt-3">
          <b-col sm="2"></b-col>
          <b-col sm="2">
            <label>Phone Number</label>
          </b-col>
          <b-col sm="5">
            <b-form-input
              v-model="phoneNumber"
              placeholder="Phone Number">
            </b-form-input>
          </b-col>
          <b-col sm="2"></b-col>
        </b-row>

      <b-row class="mt-5">
        <b-col sm="4"></b-col>
        <b-col sm="4">
          <b-button style="margin-bottom: 10px">Create Account</b-button>
          <br>
          <b-link to="/">Already have an Account ? Login</b-link>
        </b-col>
        <b-col sm="4"></b-col>
      </b-row>
      </b-container>
    </b-form>
  </div>
</template>

<script>

export default {
    name:"signup",
    data(){
        return {
          email : "",
          password: "",
          confirmPassword: "",
          firstName: "",
          lastName: "",
          phoneNumber: ""
        }
    },
    methods: {

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
