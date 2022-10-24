import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import Vuex from "vuex";
import App from './App.vue';
import router from './router';
import { store } from './store';
import 'bootstrap/dist/css/bootstrap.css';
import axios from "axios";

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

Vue.use(Vuex);

Vue.prototype.$store = store;

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount('#app');