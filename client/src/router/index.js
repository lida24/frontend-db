import Vue from 'vue';
import Router from "vue-router";
import CreateComponent from "@/components/CreateComponent";
import Ping from "@/components/Ping";
import Home from "@/components/Home";
import SelectAction from "@/components/SelectAction";
import ComponentList from "@/components/ComponentList";
import ComponentDetail from "@/components/ComponentDetail";
import ServerList from "@/components/ServerList";
import AddChassis from "@/components/AddChassis";
import AddFan140 from "@/components/AddFan140";
import AddFanControlBoard from "@/components/AddFanControlBoard";
import AddFan40 from "@/components/AddFan40";
import AddIndicatorBoard from "@/components/AddIndicatorBoard";
import AddPowerManagementModule from "@/components/AddPowerManagementModule";
import AddMotherBoard from "@/components/AddMotherBoard";
import AddDDR4MemoryModule from "@/components/AddDDR4MemoryModule";
import AddM2SSD from "@/components/AddM2SSD";
import AddRaiser2UBoard from "@/components/AddRaiser2UBoard";
import AddNetworkCard from "@/components/AddNetworkCard";
import AddRaiser1UBoard from "@/components/AddRaiser1UBoard";
import AddRaidCard from "@/components/AddRaidCard";
import AddDiskBasket from "@/components/AddDiskBasket";
import AddPowerSupply2K6 from "@/components/AddPowerSupply2K6";
import AddServer from "@/components/AddServer";
import Testing from "@/components/Testing";
import Login from "@/components/Login";
import Register from "@/components/Register";
import { store } from "../store";


Vue.use(Router);


const routes = [
  {
    path: "/ping",
    name: "Ping",
    component: Ping,
  },
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
    path: "/create_component",
    name: "CreateComponent",
    component: CreateComponent,
    meta: { requiresAuth: true },
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/select_action',
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
    path: '/server_list',
    name: 'ServerList',
    component: ServerList,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_chassis',
    name: 'AddChassis',
    component: AddChassis,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_fan140/:id',
    name: 'AddFan140',
    component: AddFan140,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_fan_control_board/:id',
    name: 'AddFanControlBoard',
    component: AddFanControlBoard,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_fan40/:id',
    name: 'AddFan40',
    component: AddFan40,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_indicator_board/:id',
    name: 'AddIndicatorBoard',
    component: AddIndicatorBoard,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_power_management_module/:id',
    name: 'AddPowerManagementModule',
    component: AddPowerManagementModule,
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
    path: '/add_ddr4_memory_module/:id',
    name: 'AddDDR4MemoryModule',
    component: AddDDR4MemoryModule,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_m2_ssd/:id',
    name: 'AddM2SSD',
    component: AddM2SSD,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_raiser_2U_board/:id',
    name: 'AddRaiser2UBoard',
    component: AddRaiser2UBoard,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_network_card/:id',
    name: 'AddNetworkCard',
    component: AddNetworkCard,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_raiser_1U_board/:id',
    name: 'AddRaiser1UBoard',
    component: AddRaiser1UBoard,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_raid_card/:id',
    name: 'AddRaidCard',
    component: AddRaidCard,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_disk_basket/:id',
    name: 'AddDiskBasket',
    component: AddDiskBasket,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_power_supply_2k6/:id',
    name: 'AddPowerSupply2K6',
    component: AddPowerSupply2K6,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/add_server',
    name: 'AddServer',
    component: AddServer,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/testing/:id',
    name: 'Testing',
    component: Testing,
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