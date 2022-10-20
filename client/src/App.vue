<template>
  <div id="app">
<!--     <Login v-if="!authenticated" v-on:authenticated="setAuthenticated"  />
    <b-container v-else> -->
      <!-- <Navbar :logged_user="logged_user_username" /> -->
      <Navbar />
<!--     </b-container> -->
    <router-view/>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Login from "@/components/Login.vue";

export default {
  name: 'App',
  components: {
    Navbar,
    Login
  },
  data: function() {
    return {
      logged_user_id: null,
      logged_user_username: null,
      authenticated: false
    };
  },
  methods: {
    async setAuthenticated(login_status, user_data) {
      // Update the states
      this.logged_user_id = user_data.id;
      this.logged_user_username = user_data.username;
      this.authenticated = login_status;
      this.token = user_data.token;
    }
  }
};
</script>

<style>
.logged_user {
  color: white;
}
</style>

