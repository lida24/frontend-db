<!-- <template>
    <div class="login">
    <form method="post" @submit.prevent="Login">
      <input
        type="text"
        placeholder="Username"
        v-model="formData.username"
        class="form-control"
      />
      <br />
      <input
        type="password"
        placeholder="Password"
        v-model="formData.password"
        class="form-control"
      />
      <br />
      <button type="submit" class="btn btn-primary">
        Login
      </button>
    </form>
    </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      formData: {
        username: "",
        password: "",
      }
    };
  },
  methods: {
    Login() {
        axios
        .post("http://192.168.75.11:5000/app/login", this.formData)
        .then((response) => {
          /* console.log(response);
          console.log(response.data); */
          if (response.data.status == "success") {
            this.$emit("authenticated", true, response.data.data);
          }
        })
        .catch((error) => {
          console.log(error, error.response);
        });
    },
  },
};
</script>

<style scoped>
.login {
  width: 500px;
  border: 1px solid #cccccc;
  background-color: #ffffff;
  margin: auto;
  margin-top: 200px;
  padding: 20px;
}
.input-form {
  margin-bottom: 9px;
}
</style> -->

<template>
  <form @submit="login">
    <input v-model="username" placeholder="Username">
    <input v-model="password" type="password">
    <input type="submit" value="Submit">
  </form>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  data: () => ({
    user: {
      username: null,
      password: null
    }
  }),
  computed: {
    ...mapGetters({
      authUser: '/'
    })
  },
  methods: {
    ...mapActions({
      loginUser: '/login'
    }),
    async login() {
      await this.loginUser(this.user)
        .then(() => {
          if (this.authUser.authenticated) {
            this.$router.push('/ping')
          } else {
            // Handle error
            this.user = {
              username: null,
              password: null
            }
          }
        })
      
    }
  }
}
</script>