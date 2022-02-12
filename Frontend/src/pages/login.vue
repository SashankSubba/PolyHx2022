<template>
  <div>
      <h1>Welcome to Guardians !</h1>
    <img src=../assets/logo.jpg width="10%">
    <b-form onsubmit="submit" class="mt-5">
        <b-row>
          <b-col cols="5">
            <label>Email</label>
          </b-col>
          <b-col cols="5">
            <b-form-input
              v-model="email"
              placeholder="Enter your email">
            </b-form-input>
          </b-col>
        </b-row>

        <b-row>
          <b-col cols="5">
            <label>Password</label>
          </b-col>
          <b-col cols="5">
            <b-form-input
              v-model="password"
              placeholder="Enter your email">
            </b-form-input>
          </b-col>
        </b-row>

      <b-row class="mt-5">
        <b-col cols="4"></b-col>
        <b-col cols="4">
          <b-button style="margin-right: 20px">Login</b-button>
          <a href="signup.vue">Create Profile</a>
        </b-col>
        <b-col cols="4"></b-col>
      </b-row>
    </b-form>
  </div>
</template>

<script>

export default {
    name:"login",
    data(){
        return {
          email : "",
          password: ""
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
