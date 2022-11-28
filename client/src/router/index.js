import Vue from 'vue';
import Router from "vue-router";
import CreateComponent from "@/components/CreateComponent";
import SelectAction from "@/components/SelectAction";
import ComponentList from "@/components/ComponentList";
import ComponentDetail from "@/components/ComponentDetail";
import ServerList from "@/components/ServerList";
import AddChassis from "@/components/AddChassis";
import AddMotherBoard from "@/components/AddMotherBoard";
import AddDiskBasket4 from "@/components/AddDiskBasket4";
import AddDiskBasket3 from "@/components/AddDiskBasket3";
import AddDiskBasket2 from "@/components/AddDiskBasket2";
import AddDiskBasket1 from "@/components/AddDiskBasket1";
import AddServer from "@/components/AddServer";
import Login from "@/components/Login";
import Register from "@/components/Register";
import CurrentComponent from "@/components/CurrentComponent";
import CurrentServer from "@/components/CurrentServer";
import HandTesting from "@/components/HandTesting";
import { store } from "../store";


Vue.use(Router);


const routes = [
  {
    path: "/register",
    name: "Register",
    component: Register,
    meta: { guest: true },
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: { guest: true },
  },
  {
    path: "/create_component/:username",
    name: "CreateComponent",
    component: CreateComponent,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/',
    name: 'SelectAction',
    component: SelectAction,
    meta: { requiresAuth: true },
  },
  {
    path: '/component_list',
    name: 'ComponentList',
    component: ComponentList,
    meta: { requiresAuth: true },
  },
  {
    path: '/component_detail/:id',
    name: 'ComponentDetail',
    component: ComponentDetail,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/current_component/:id',
    name: 'CurrentComponent',
    component: CurrentComponent,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/server_list',
    name: 'ServerList',
    component: ServerList,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_chassis/:username',
    name: 'AddChassis',
    component: AddChassis,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_motherboard/:id',
    name: 'AddMotherBoard',
    component: AddMotherBoard,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_disk_basket4/:id',
    name: 'AddDiskBasket4',
    component: AddDiskBasket4,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_disk_basket3/:id',
    name: 'AddDiskBasket3',
    component: AddDiskBasket3,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_disk_basket2/:id',
    name: 'AddDiskBasket2',
    component: AddDiskBasket2,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_disk_basket1/:id',
    name: 'AddDiskBasket1',
    component: AddDiskBasket1,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_server/:id',
    name: 'AddServer',
    component: AddServer,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/current_server/:id',
    name: 'CurrentServer',
    component: CurrentServer,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/hand_testing/:id',
    name: 'HandTesting',
    component: HandTesting,
    props: true,
    meta: { requiresAuth: true },
  },
];

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next("/login");
  } else {
    next();
  }
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.guest)) {
    if (store.getters.isAuthenticated) {
      next("/");
      return;
    }
    next();
  } else {
    next();
  }
});

export default router;