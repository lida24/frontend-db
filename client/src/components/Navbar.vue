<template>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
        <router-link class="navbar-brand" :to="{ name: 'SelectAction' }">Система контроля</router-link>
        <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <!-- <a class="nav-link" href="#">Admin</a> -->
            </li>
        </ul>
        <ul v-if="isLoggedIn" class="navbar-nav">
            <li class="nav-item">{{ User }}</li>
            <li class="nav-item"><a @click="logout">Logout</a></li>
        </ul>
        <ul v-else class="navbar-nav">
            <li class="nav-item">
                <router-link class="nav-link" :to="{ name: 'Register' }">Регистрация</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" :to="{ name: 'Login' }">Вход</router-link>
            </li>
        </ul>
        </div>
    </nav>
</template>



<script>
import { mapGetters } from "vuex";
export default {
  name: "NavBar",
  computed: {
    isLoggedIn() {
      return this.$store.getters.isAuthenticated;
    },
    ...mapGetters({ User: "StateUser" }),

  },
  methods: {
    async logout() {
      await this.$store.dispatch("LogOut");
      this.$router.push("/login");
    },
  },
};
</script>

<style>
a:hover {
  cursor: pointer;
}
</style>