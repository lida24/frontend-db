<template>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
        <router-link class="navbar-brand" :to="{ name: 'Home' }">Система контроля</router-link>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav mr-auto">
              <li class="nav-item">
                  <a class="nav-link" href="#">Admin</a>
              </li>
          </ul>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <!-- <a class="nav-link" href="#">Вход</a> -->
                        <!-- <router-link class="nav-link" :to="{ name: 'Login' }">Вход</router-link> -->
                    </li>
                    <li class="nav-item">
                        <!-- <a class="nav-link" href="#">Регистрация</a> -->
                        <a class="nav-link" href="#">{{logged_user}}</a>
                    </li>
                </ul>
        </div>
    </nav>
</template>

<script>
export default {
  name: "NavBar",
  props: {
    logged_user: String
  }
};
</script>