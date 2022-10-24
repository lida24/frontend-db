<template>
<div class="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center bg-dark" style="color:white">
    <div class="col-md-5 p-lg-5 mx-auto my-5">
        <h1 class="display-4 font-weight-normal">Выберите необходимое действие</h1>
        <div class="wrapper">
            <div class="components-btn">
                <router-link class="btn btn-primary component-btn" :to="{ name: 'CreateComponent', params: { username: User }}">Добавить компонент</router-link>
                <!-- <router-link class="btn btn-primary component-btn" :to="/create_component/${this.username}/">Добавить компонент</router-link>  -->
                <router-link class="btn btn-primary component-btn" :to="{ name: 'ComponentList' }">Просмотреть все компоненты</router-link>
            </div>
            <div class="servers-btn">
                <router-link class="btn btn-primary server-btn" :to="{ name: 'AddChassis' }">Собрать сервер</router-link>
                <!-- <router-link class="btn btn-primary server-btn" :to="{ name: 'AddServer' }">Собрать сервер</router-link> -->
                <router-link class="btn btn-primary server-btn" :to="{ name: 'ServerList' }">Просмотреть все серверы</router-link>
            </div>
        </div>
    </div>
    <div class="product-device box-shadow d-none d-md-block"></div>
    <div class="product-device product-device-2 box-shadow d-none d-md-block"></div>
</div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  computed: {
    isLoggedIn() {
      return this.$store.getters.isAuthenticated;
    },
    ...mapGetters({ User: "StateUser" }),

  },
};
</script>

<style>
.wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 100px;
}

.components-btn,
.servers-btn {
    display: inline-grid;
}

.components-btn {
    margin-right: 100px;
}

.component-btn,
.server-btn {
    width: 390px;
    margin-bottom: 50px;
    padding: 1.375rem 1.75rem;
    font-size: 1.5rem;
}

</style>